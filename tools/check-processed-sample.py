#!/usr/bin/env python3
"""Verify the downloadable processed sample through the real HTTP backend."""
from pathlib import Path
import argparse
import http.cookiejar
import json
import os
import signal
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request

from processed_sample import download_sample, verify_sample

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sample-dir', type=Path)
    parser.add_argument('--public-preview', action='store_true')
    args = parser.parse_args()
    sample = verify_sample(args.sample_dir) if args.sample_dir else download_sample()
    with socket.socket() as reservation:
        reservation.bind(('127.0.0.1', 0))
        port = reservation.getsockname()[1]
    with tempfile.TemporaryDirectory(prefix='processed-retail-check-') as temporary:
        temporary = Path(temporary)
        state = temporary / 'state'
        environment = {key: value for key, value in os.environ.items() if key in {'PATH', 'HOME', 'LANG', 'LC_ALL', 'SSL_CERT_FILE', 'SSL_CERT_DIR'}}
        with (temporary / 'server.log').open('w') as log:
            command = [sys.executable, str(ROOT / 'tools/dev.py'), '--state', str(state), '--sample-dir', str(sample), '--port', str(port)]
            prefix = '/apps/video' if args.public_preview else ''
            if args.public_preview:
                command += ['--public-preview', '--prefix', prefix]
            process = subprocess.Popen(command, env=environment, stdout=log, stderr=log, start_new_session=True)
            try:
                origin = f'http://127.0.0.1:{port}'
                client = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))

                def get(path, headers=None):
                    return client.open(urllib.request.Request(origin + prefix + path, headers=headers or {}), timeout=30)

                for _ in range(100):
                    if process.poll() is not None:
                        raise RuntimeError('The processed-sample backend stopped before readiness.')
                    try:
                        with get('/healthz') as response:
                            if response.status == 200:
                                break
                    except (OSError, urllib.error.URLError):
                        time.sleep(.2)
                else:
                    raise RuntimeError('The processed-sample backend did not become ready.')
                if args.public_preview:
                    with get('/api/session') as response:
                        session = json.load(response)
                    assert session['read_only'] is True and session['can_query'] is False
                    assert session['viewing_as']['principal']['id'] == 'peter'
                    for path in ['/api/observer', '/api/session', '/api/retail/location']:
                        request = urllib.request.Request(origin + prefix + path, data=b'{}', headers={'Content-Type': 'application/json', 'Origin': origin, 'X-Rocoto-Page': '1'})
                        try:
                            client.open(request, timeout=30)
                        except urllib.error.HTTPError as denied:
                            assert denied.code == 403
                        else:
                            raise AssertionError('Public sample writes must remain server-denied.')
                else:
                    code = (state / 'owner-code.txt').read_text().strip()
                    request = urllib.request.Request(origin + '/api/session', data=json.dumps({'code': code}).encode(), headers={'Content-Type': 'application/json', 'Origin': origin, 'X-Rocoto-Page': '1'})
                    with client.open(request, timeout=30) as response:
                        assert response.status == 200
                with get('/api/retail/viewer/bootstrap') as response:
                    bootstrap = json.load(response)
                assert bootstrap['read_authority'] == 'legacy'
                assert bootstrap['capabilities']['location_context'] is False
                with get('/control-room/data.json') as response:
                    data = json.load(response)
                assert len(data['clips']) == 45
                assert sum(bool(clip.get('models', {}).get('8b', {}).get('processed')) for clip in data['clips']) == 9
                assert sum('dataset_reference' in clip.get('models', {}) for clip in data['clips']) == 40
                assert len(data['core_trackers']) == 9
                assert data['coverage']['raw_events'] == data['coverage']['quarantined'] == 17
                latest = next(clip for clip in data['clips'] if clip['id'] == 'retailaction-000027-rank0')
                assert latest['models']['8b']['processed'] is True
                assert len(latest['models']['8b']['windows']) == 2
                assert sum(len(window['events']) for window in latest['models']['8b']['windows']) == 0
                with get('/control-room/' + latest['media'], {'Range': 'bytes=1024-2047'}) as response:
                    assert response.status == 206 and len(response.read()) == 1024
                    assert response.headers['Content-Range'].startswith('bytes 1024-2047/')
                with get('/api/retail/location') as response:
                    location = json.load(response)
                assert len(location['locations']) == 1
                with get('/control-room/') as response:
                    assert 'Authored annotations' not in response.read().decode()
                assert json.loads((state / 'outbound-attempts.json').read_text())['blocked_outbound_attempts'] == 0
                print(json.dumps({'processed_sample': 'passed', 'public_preview': args.public_preview, 'recordings': 45, 'model_answer_recordings': 9, 'reference_recordings': 40, 'latest_quarantined_observations': 17, 'core_trackers': 9, 'native_byte_range': 'passed', 'provider_calls': 0}))
            finally:
                os.killpg(process.pid, signal.SIGTERM)
                process.wait(timeout=15)


if __name__ == '__main__':
    main()
