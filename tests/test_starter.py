from pathlib import Path
import importlib.util,json,stat,sys
import pytest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import seed

def test_native_seed_persists_and_repeats_without_duplicate_observations(tmp_path):
 state=tmp_path/'owned';first=seed.seed(state);second=seed.seed(state)
 assert first['source_id']==second['source_id']=='synthetic-shop-1'
 assert first['admitted_annotation_count']==second['admitted_annotation_count']==3
 assert second['skipped_annotation_count']==0 and second['core_tracker_count']==9
 page=Path(second['page']['bundle_directory']);data=json.load(open(page/'data.json'));manifest=json.load(open(page/'manifest.json'))
 assert len(data['clips'])==1
 clip=data['clips'][0];assert set(clip['models'])=={'fixture'} and clip['source_provenance']['kind']=='authored_fixture'
 assert manifest['privacy']['publisher']=='Peter Neyra' and manifest['privacy']['licence']=='MIT'
 tiles={t['key']:t for t in data['core_trackers']};assert tiles['visitors']['value']==1 and tiles['product_interactions']['value']==3
 assert stat.S_IMODE((state/'owner-code.txt').stat().st_mode)==0o600

def test_existing_unrelated_state_is_refused(tmp_path):
 state=tmp_path/'other';state.mkdir(mode=0o700);(state/'other-project.json').write_text('{}')
 with pytest.raises(ValueError):seed.seed(state)
 assert list(state.iterdir())==[state/'other-project.json']

def test_source_checkout_state_is_refused():
 with pytest.raises(ValueError):seed.private_state(ROOT/'private-data')

def test_empty_provider_workspace_is_denied_before_approval_file_read(tmp_path):
 from compute_guard import validate_approval,ApprovalError
 with pytest.raises(ApprovalError,match='own Modal workspace'):
  validate_approval(tmp_path/'absent.json',workspace='',planned_gross_usd='1.50')


def test_authenticated_control_room_keeps_strict_policy_and_admits_navigation_images(tmp_path,monkeypatch):
 from fastapi.testclient import TestClient
 monkeypatch.setenv('ROCOTO_VERTICAL','retail')
 monkeypatch.setenv('ROCOTO_RETAIL_LOCATION_CONTEXT','off')
 monkeypatch.setenv('ROCOTO_RETAIL_REALTIME_READS','legacy')
 monkeypatch.setenv('ROCOTO_TILE_RUNNER','off')
 import server
 state=tmp_path/'viewer';seed.seed(state)
 with TestClient(server.create_app(state)) as client:
  code=(state/'owner-code.txt').read_text().strip()
  assert client.post('/api/session',json={'code':code},headers={'X-Rocoto-Page':'1'}).status_code==200
  page=client.get('/control-room/')
  assert page.status_code==200 and 'native-nav/atelier-nav.js' in page.text
  assert page.headers['content-security-policy']=="default-src 'self'; img-src 'self' data: https://atelierneyra.com https://demo.soyrocoto.com; media-src 'self'; script-src 'self'; worker-src 'self'; style-src 'self' 'unsafe-inline'; connect-src 'self'; frame-ancestors 'self'; base-uri 'none'; object-src 'none'"
  assert 'https://demo.soyrocoto.com' not in client.get('/api/session').headers['content-security-policy']
