"""Real ASGI mount contracts: URLs, canonical writes, cookie scope and read-only admission."""
from pathlib import Path
import sys,json
import pytest,httpx
from fastapi import FastAPI,Request,Response
from fastapi.responses import HTMLResponse,StreamingResponse
from fastapi.testclient import TestClient
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'harness/mechanics'))
from web_mount import MountedApp,base_path

@pytest.mark.parametrize('path',['relative','//elsewhere','/apps/../other','/apps/%2e%2e/other','/apps/x?query=1','/apps/x#hash','/apps/x\\y'])
def test_mount_rejects_ambiguous_paths(path):
 with pytest.raises(ValueError):base_path(path)

def sample():
 app=FastAPI()
 @app.get('/')
 def root():return HTMLResponse('<!doctype html><script src="/static/harness/app.js"></script><a href="/">Home</a>')
 @app.get('/api/item')
 def item(response:Response):
  response.set_cookie('test_session','private-test-token',httponly=True,samesite='strict',secure=True,path='/')
  return {'image':'/sample-hardware/rocoto/sample/lever.webp','preview':'/api/manufacturer/preview/version','origin':'http://127.0.0.1:18781/sample-hardware/rocoto/','text':'Saved catalogue'}
 @app.post('/api/item')
 async def save(request:Request):return await request.json()
 @app.post('/api/observer')
 def observer():return {'escaped':True}
 @app.delete('/api/session')
 def logout():return {'ok':True}
 @app.get('/api/events')
 def events():return StreamingResponse(iter([b'data: first\n\n',b'data: second\n\n']),media_type='text/event-stream')
 return app

def test_real_routes_have_prefixed_assets_and_no_double_prefix():
 with TestClient(MountedApp(sample(),prefix='/apps/manufacturer-order-desk',orders_origin='http://127.0.0.1:18781',company='sample-hardware')) as client:
  html=client.get('/apps/manufacturer-order-desk/').text
  assert 'src="/apps/manufacturer-order-desk/static/harness/app.js"' in html
  assert 'href="/apps/manufacturer-order-desk/"' in html
  assert '/apps/manufacturer-order-desk/apps/' not in html
  assert client.get('/api/item').status_code==404
  response=client.get('/apps/manufacturer-order-desk/api/item');value=response.json()
  assert value['image']=='/apps/manufacturer-order-desk/orders/sample-hardware/rocoto/sample/lever.webp'
  assert value['preview']=='/apps/manufacturer-order-desk/api/manufacturer/preview/version'
  assert value['origin']=='http://testserver/apps/manufacturer-order-desk/orders/sample-hardware/rocoto/'
  cookie=response.headers['set-cookie'];assert 'Path=/apps/manufacturer-order-desk/' in cookie and 'HttpOnly' in cookie and 'SameSite=strict' in cookie and 'Secure' in cookie
  saved=client.post('/apps/manufacturer-order-desk/api/item',json=value).json()
  # Request values return to canonical source URLs before the real native handler.
  assert saved==value

def test_canonical_write_handler_receives_original_resource_paths():
 app=sample();observed=[]
 @app.post('/api/capture')
 async def capture(request:Request):observed.append(await request.json());return {'ok':True}
 with TestClient(MountedApp(app,prefix='/x',orders_origin='http://127.0.0.1:18781',company='sample-hardware')) as client:
  client.post('/x/api/capture',json={'image':'/x/orders/sample-hardware/rocoto/a.webp','endpoint':'/x/api/config','text':'A source note'})
 assert observed==[{'image':'/sample-hardware/rocoto/a.webp','endpoint':'/api/config','text':'A source note'}]

def test_public_read_only_blocks_observer_escape_and_all_native_writes():
 with TestClient(MountedApp(sample(),prefix='/x',read_only=True)) as client:
  assert client.post('/x/api/observer',json={}).status_code==403
  assert client.post('/x/api/item',json={}).status_code==403
  assert client.patch('/x/api/item',json={}).status_code==403
  assert client.delete('/x/api/session').status_code==200
  assert client.get('/x/api/item').status_code==200

def test_generic_mount_preserves_streaming_sse():
 with TestClient(MountedApp(sample(),prefix='/video')) as client:
  response=client.get('/video/api/events');assert response.status_code==200
  assert response.content==b'data: first\n\ndata: second\n\n'

@pytest.mark.parametrize('origin',['https://outside.test','http://outside.test','http://127.0.0.1:1/private','http://user:pass@localhost:1'])
def test_orders_transport_stays_at_owned_loopback_origin(origin):
 with pytest.raises(ValueError):MountedApp(sample(),orders_origin=origin)


def test_sandboxed_native_preview_fonts_have_anonymous_cors():
 app=sample()
 @app.get('/static/harness/inter.woff2')
 def font():return Response(b'owned-font-fixture',media_type='font/woff2')
 with TestClient(MountedApp(app,prefix='/x')) as client:
  response=client.get('/x/static/harness/inter.woff2')
  assert response.headers['access-control-allow-origin']=='*'
  assert response.headers['cross-origin-resource-policy']=='cross-origin'

def test_control_room_media_urls_are_mounted_for_native_video():
 mount=MountedApp(sample(),prefix='/apps/video')
 assert mount.value({'media':'/control-room/clip.mp4'})=={'media':'/apps/video/control-room/clip.mp4'}
 assert "'/apps/video/control-room/" in mount.text("const media='/control-room/';")


def test_native_root_stylesheet_imports_and_script_urls_are_prefixed():
 mount=MountedApp(sample(),prefix='/apps/video')
 assert "url('/apps/video/theme.css')" in mount.text("@import url('/theme.css');")
 assert mount.value({'sheet':'/style.css'})=={'sheet':'/apps/video/style.css'}
 assert "'/apps/video/app.js'" in mount.text("const script='/app.js';")


@pytest.mark.parametrize(('location','expected'),[
 ('https://preview.example.test/control-room/?clip=1#frame','https://preview.example.test/apps/video/control-room/?clip=1#frame'),
 ('https://preview.example.test/apps/video/control-room/','https://preview.example.test/apps/video/control-room/'),
 ('https://preview.example.test/apps/video','https://preview.example.test/apps/video'),
 ('https://other.example.test/control-room/','https://other.example.test/control-room/'),
 ('//other.example.test/control-room/','//other.example.test/control-room/'),
 ('/control-room/?clip=1#frame','/apps/video/control-room/?clip=1#frame'),
])
def test_redirects_preserve_same_origin_mount(location,expected):
 app=sample()
 @app.get('/redirect')
 def redirect():return Response(status_code=307,headers={'Location':location})
 with TestClient(MountedApp(app,prefix='/apps/video',public_origin='https://preview.example.test'),base_url='https://preview.example.test') as client:
  assert client.get('/apps/video/redirect',follow_redirects=False).headers['location']==expected

def test_native_fastapi_slash_redirect_retains_mount():
 app=FastAPI()
 @app.get('/control-room/')
 def control_room():return {'ok':True}
 with TestClient(MountedApp(app,prefix='/apps/video',public_origin='https://preview.example.test'),base_url='https://preview.example.test') as client:
  response=client.get('/apps/video/control-room?clip=1',follow_redirects=False)
  assert response.headers['location']=='https://preview.example.test/apps/video/control-room/?clip=1'
