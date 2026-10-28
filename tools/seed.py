#!/usr/bin/env python3
"""Create a recipient-owned synthetic recording through the original retail pipeline."""
from pathlib import Path
from datetime import datetime,timedelta,timezone
import argparse,hashlib,json,os,stat,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'harness'))
import layout
layout.install('retail')

def private_state(path):
 path=path.expanduser().absolute()
 if path.resolve()!=path or path.is_relative_to(ROOT):raise ValueError('Use a private state directory outside the source checkout.')
 if path.exists():
  s=path.lstat()
  if not stat.S_ISDIR(s.st_mode) or s.st_uid!=os.geteuid() or stat.S_IMODE(s.st_mode)&0o077:raise ValueError('Use an owner-only state directory.')
  if any(path.iterdir()) and not (path/'video-operations.json').is_file():raise ValueError('Choose a fresh directory for this sample workspace.')
 else:path.mkdir(mode=0o700,parents=True)
 return path

def write_json(path,data):
 path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(data,indent=2)+'\n');path.chmod(0o600)

def seed(path, *, issue_code=True):
 from access import AccessStore
 import retail_records as records
 from seed_control_room import seed_location
 from core_trackers import install_core_trackers,load_recipe
 from core_trackers.run import run_trackers
 from cosmos_archive_import import ingest_recording,retail_profile
 from import_control_room_bundle import publish_core_trackers
 from control_room_routes import owner_directory
 from tracker_runner import host_pass
 path=private_state(path);owner='owner';collection='retail-demo'
 marker={'schema':1,'product':'video-operations','sample_basis':'authored synthetic media and annotations'}
 if (path/'video-operations.json').exists() and json.loads((path/'video-operations.json').read_text())!=marker:raise ValueError('Choose this sample workspace.')
 write_json(path/'video-operations.json',marker)
 access=AccessStore(path)
 access.create_environment('demo','Video operations')
 code=access.issue('demo',owner=True,principal_id=owner,display_name='Owner')
 if issue_code:
  codefile=path/'owner-code.txt';codefile.write_text(code+'\n');codefile.chmod(0o600)
 place=seed_location(path,path/'access.sqlite','demo',owner,lifecycle='development',collection=collection,name='Example shop · synthetic data')
 location,room=place['location_id'],place['room_id'];company=records.company_from_access(path,path,'demo',owner,collection)
 install_core_trackers(company,location)
 source='synthetic-shop-1';camera=records.ensure_camera(company,location,room,'Synthetic camera',[source])
 original=ROOT/'examples/synthetic-shop.mp4';poster=ROOT/'examples/synthetic-shop.jpg';annotations=json.load(open(ROOT/'examples/annotations.json'));digest=hashlib.sha256(original.read_bytes()).hexdigest()
 bundle=owner_directory(path,owner);folder=bundle/'sources'/source;folder.mkdir(parents=True,exist_ok=True)
 import shutil
 for name,p in [('recording.mp4',original),('poster.jpg',poster)]:
  target=folder/name
  if target.exists() and hashlib.sha256(target.read_bytes()).digest()!=hashlib.sha256(p.read_bytes()).digest():raise ValueError('Preserve the immutable sample recording.')
  if not target.exists():shutil.copyfile(p,target)
  target.chmod(0o600)
 write_json(folder/'tracks.json',annotations['viewer_tracks'])
 relative='sources/'+source;media_url='/control-room/'+relative+'/recording.mp4';thumbnail_url='/control-room/'+relative+'/poster.jpg'
 previous=company.monitoring.registered_source(owner,source)
 capture=(previous or {}).get('source_capture_start_utc') or (datetime.now(timezone.utc)-timedelta(minutes=2)).isoformat()
 manifest=bundle/'manifest.json'
 if not manifest.exists():write_json(manifest,{'schema_version':1,'owner_principal_id':owner,'revision':'authored-fixture-v1','generated_assets':{},'source_ids':[],'location':{'id':location,'name':'Example shop · synthetic data'},'privacy':{'face_redaction':'source_as_published','basis':'Programmatically authored scene with supplied annotations','licence':'MIT','publisher':'Peter Neyra'},'files':[]})
 clip={'id':source,'video_id':source,'title':'Synthetic shop · authored annotations','name':'Synthetic shop · authored annotations','camera':'Synthetic camera','start':0,'end':12,'duration':12,'duration_s':12,'media':relative+'/recording.mp4','poster':relative+'/poster.jpg','is_primary_trial':True,'viewer_enabled':True,'viewer_default':True,'room_id':room,'room_name':'Example shop','media_url':relative+'/recording.mp4','thumbnail':relative+'/poster.jpg','thumbnail_url':relative+'/poster.jpg','tracks_url':relative+'/tracks.json','fps':10,'width':640,'height':360,'source_provenance':{'kind':'authored_fixture','data_basis':'generated_history','credit':'Authored fixture · MIT','note':'Synthetic scene and supplied labels; model execution is a separate setup path.'}}
 tracks=annotations['tracks'];answer=annotations['answer'];answer_digest=hashlib.sha256(json.dumps(answer,sort_keys=True).encode()).hexdigest()
 admitted=ingest_recording(company,location,camera,{'source_id':source,'duration_s':12,'sha256':digest,'media_url':media_url,'thumbnail_url':thumbnail_url,'capture_start_utc':capture},tracks,[{'start_s':0.,'end_s':12.,'model':'authored-fixture/v1','sampling':'supplied frame-by-frame annotations','processing_seconds':0.,'answer':answer,'answer_ref':{'file':'examples/annotations.json','sha256':answer_digest,'generator':'authored-fixture/v1'}}],profile=retail_profile(company,location),vocabulary=load_recipe()['vocabulary'],data_basis='generated_history',title='Synthetic shop · authored annotations',files=[relative+'/'+n for n in ['recording.mp4','poster.jpg','tracks.json']],clip=clip,publisher_note='Authored synthetic fixture · MIT')
 with host_pass(company,location) as held:
  held.mark();result=run_trackers(company,location);page=publish_core_trackers(company,location,location_name='Example shop · synthetic data');held.done(result,page)
 return {'state':str(path),'owner_code_file':str(path/'owner-code.txt'),'source_id':source,'recording_sha256':digest,'admitted_annotation_count':len(admitted['admitted']),'skipped_annotation_count':len(admitted['skipped']),'core_tracker_count':len(result['outputs']),'provider_calls':0,'basis':'authored synthetic fixture','page':page}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--state',type=Path,default=Path.home()/'.local/state/video-operations');a=p.parse_args();print(json.dumps(seed(a.state),indent=2))
if __name__=='__main__':main()
