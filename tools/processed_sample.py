"""Install the retained retail sample into a fresh, recipient-owned workspace."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import os
import shutil
import sqlite3
import sys
import tarfile
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DESCRIPTOR = ROOT / 'examples/processed-retail.json'


def digest(path):
    result = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            result.update(block)
    return result.hexdigest()


def verify_sample(directory):
    directory = Path(directory).resolve()
    descriptor = json.loads(DESCRIPTOR.read_text())
    if digest(directory / 'files.sha256.json') != descriptor['file_manifest_sha256']:
        raise ValueError('Use the sample manifest matching the published checksum.')
    manifest = json.loads((directory / 'files.sha256.json').read_text())
    if {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file()} != set(manifest) | {'files.sha256.json'}:
        raise ValueError('Use exactly the published sample files.')
    for name, expected in manifest.items():
        relative = PurePosixPath(name)
        if relative.is_absolute() or any(part in {'.', '..'} for part in relative.parts):
            raise ValueError('Use the published sample file paths.')
        path = directory / name
        if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(directory):
            raise ValueError('Restore the complete published sample.')
        if path.stat().st_size != expected['bytes'] or digest(path) != expected['sha256']:
            raise ValueError('Restore the sample file matching its published checksum.')
    return directory


def download_sample():
    descriptor = json.loads(DESCRIPTOR.read_text())
    cache = Path.home() / '.cache/camera-video-search' / descriptor['id']
    if (cache / 'files.sha256.json').is_file():
        return verify_sample(cache)
    cache.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='sample-', dir=cache.parent) as scratch:
        scratch = Path(scratch)
        archive = scratch / 'sample.tar.gz'
        print('Downloading the retained retail sample…', flush=True)
        with urllib.request.urlopen(descriptor['url'], timeout=120) as response, archive.open('wb') as target:
            total = 0
            while block := response.read(1024 * 1024):
                total += len(block)
                if total > descriptor['bytes']:
                    raise ValueError('Use the published sample archive size.')
                target.write(block)
        if total != descriptor['bytes'] or digest(archive) != descriptor['sha256']:
            raise ValueError('Use the sample archive matching its published checksum.')
        unpacked = scratch / 'unpacked'
        unpacked.mkdir()
        with tarfile.open(archive, 'r:gz') as package:
            members = package.getmembers()
            if len({item.name for item in members}) != len(members):
                raise ValueError('Use unique published sample paths.')
            if sum(item.size for item in members) > 300 * 1024 * 1024:
                raise ValueError('Use the bounded retail sample.')
            for item in members:
                name = PurePosixPath(item.name)
                if (name.is_absolute() or any(part in {'.', '..'} for part in name.parts)
                        or not (item.isfile() or item.isdir())):
                    raise ValueError('Use regular files from the published sample.')
            package.extractall(unpacked, members=members, filter='data')
        verify_sample(unpacked)
        if cache.exists():
            raise ValueError('Choose a fresh sample cache directory.')
        shutil.move(str(unpacked), cache)
    return verify_sample(cache)


def install_sample(state, sample):
    sys.path.insert(0, str(ROOT / 'harness'))
    import layout
    layout.install('retail')
    from seed import private_state, write_json
    from access import AccessStore
    from workspace_identity import workspace_scope
    from control_room_routes import owner_directory

    sample = verify_sample(sample)
    state = private_state(state)
    metadata = json.loads((sample / 'sample.json').read_text())
    marker = {'schema': 1, 'product': 'video-operations', 'sample_basis': metadata['id']}
    marker_path = state / 'video-operations.json'
    if marker_path.exists() and json.loads(marker_path.read_text()) != marker:
        raise ValueError('Choose a fresh directory for the processed retail sample.')
    fresh = not marker_path.exists()
    # Recording-local visit identifiers were derived from this logical principal.
    # Authorization is created afresh in the recipient's own access registry.
    owner = 'peter'
    company = workspace_scope(state)
    access = AccessStore(state)
    access.create_environment('demo', 'Retail sample')

    def rebind(value):
        if isinstance(value, dict):
            return {key: rebind(item) for key, item in value.items()}
        if isinstance(value, list):
            return [rebind(item) for item in value]
        return company if value == '__SAMPLE_COMPANY__' else owner if value == '__SAMPLE_OWNER__' else value

    if fresh:
        stores = json.loads((sample / 'stores.json').read_text())
        allowed = {'business-scope.sqlite', 'location-intelligence.sqlite', 'monitoring.sqlite', 'stream-ingestion.sqlite', 'tracker-runs.sqlite'}
        if set(stores) != allowed:
            raise ValueError('Use the five published retail data stores.')
        for filename, tables in stores.items():
            path = state / filename
            if path.exists():
                raise ValueError('Import the sample into a fresh workspace.')
            with sqlite3.connect(path) as db:
                for table, spec in tables.items():
                    if not table.replace('_', '').isalnum():
                        raise ValueError('Use the published table names.')
                    db.execute(spec['schema'])
                    placeholders = ','.join('?' for _ in spec['columns'])
                    rows = []
                    for row in spec['rows']:
                        rebound = []
                        for value in row:
                            if isinstance(value, str):
                                try:
                                    decoded = json.loads(value)
                                except ValueError:
                                    value = rebind(value)
                                else:
                                    value = json.dumps(rebind(decoded), separators=(',', ':'), ensure_ascii=False)
                            rebound.append(value)
                        rows.append(rebound)
                    db.executemany('INSERT INTO "' + table + '" VALUES (' + placeholders + ')', rows)
            path.chmod(0o600)
        destination = owner_directory(state, owner)
        shutil.copytree(sample / 'bundle', destination)
        manifest = rebind(json.loads((destination / 'manifest.json').read_text()))
        write_json(destination / 'manifest.json', manifest)
        for path in destination.rglob('*'):
            path.chmod(0o700 if path.is_dir() else 0o600)
        write_json(state / 'processed-sample.json', metadata)
        write_json(marker_path, marker)
    code = access.issue('demo', owner=True, principal_id=owner, display_name='Owner')
    codefile = state / 'owner-code.txt'
    codefile.write_text(code + '\n')
    codefile.chmod(0o600)
    return {'state': str(state), 'owner_code_file': str(codefile), 'basis': metadata['id'], 'provider_calls': 0}
