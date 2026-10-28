#!/usr/bin/env python3
"""Save explicit recipient configuration with hidden input outside the checkout."""
from pathlib import Path
import argparse,getpass,json,os,re,stat
ROOT=Path(__file__).resolve().parents[1]
DEFAULT=Path.home()/'.config/video-operations/runtime.env'
GROUPS={
 'openai':['ROCOTO_OPENAI_API_KEY','ROCOTO_PUBLIC_ORIGIN','ROCOTO_OPERATOR_ID','ROCOTO_AGENT_AUTH_MODE','ROCOTO_MANAGED_SPENDING_MODE'],
 'modal':['VIDEO_OPERATIONS_MODAL_WORKSPACE','ROCOTO_RETAIL_MODAL_PYTHON','ROCOTO_RETAIL_MODAL_CONFIG_PATH','ROCOTO_OPERATOR_ID'],
 'qdrant':['ROCOTO_RETAIL_QDRANT_URL'],
 'database':['RUNTIME_DATABASE_URL','ROCOTO_RETAIL_REALTIME_READS'],
 'maps':['ROCOTO_RETAIL_LOCATION_CONTEXT','ROCOTO_RETAIL_MAPBOX_TOKEN','ROCOTO_RETAIL_GOOGLE_MAPS_API_KEY'],
}
def private_path(path):
 path=path.expanduser().absolute()
 if path.resolve().is_relative_to(ROOT):raise ValueError('Choose a private configuration file outside source.')
 path.parent.mkdir(parents=True,mode=0o700,exist_ok=True)
 s=path.parent.lstat()
 if path.parent.resolve()!=path.parent or not stat.S_ISDIR(s.st_mode) or s.st_uid!=os.geteuid() or stat.S_IMODE(s.st_mode)&0o077:raise ValueError('Use an owner-only configuration directory.')
 return path
def read_env(path):
 path=private_path(path)
 if not path.exists():return {}
 s=path.lstat()
 if not stat.S_ISREG(s.st_mode) or s.st_nlink!=1 or s.st_uid!=os.geteuid() or stat.S_IMODE(s.st_mode)&0o077:raise ValueError('Use an owner-only regular configuration file.')
 values={}
 for line in path.read_text().splitlines():
  if not line or line.startswith('#'):continue
  key,sep,value=line.partition('=')
  if not sep or not re.fullmatch(r'[A-Z][A-Z0-9_]+',key) or '\x00' in value:raise ValueError('Use NAME=value entries.')
  values[key]=value
 return values
def write_env(path,values):
 path=private_path(path);read_env(path);temp=path.with_name(path.name+'.new');fd=os.open(temp,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
 try:
  with os.fdopen(fd,'w') as f:
   for key,value in sorted(values.items()):
    if not re.fullmatch(r'[A-Z][A-Z0-9_]+',key) or any(c in value for c in ['\n','\r','\x00']):raise ValueError('Use single-line configuration values.')
    f.write(key+'='+value+'\n')
   f.flush();os.fsync(f.fileno())
  os.replace(temp,path)
 finally:
  if temp.exists():temp.unlink()
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['init','doctor']);p.add_argument('--env-file',type=Path,default=DEFAULT);p.add_argument('--features',default='openai');a=p.parse_args();features=a.features.split(',')
 if set(features)-GROUPS.keys():raise ValueError('Select documented feature names.')
 values=read_env(a.env_file);names=list(dict.fromkeys(k for f in features for k in GROUPS[f]))
 if a.command=='init':
  if 'openai' in features:
   values.setdefault('ROCOTO_AGENT_AUTH_MODE','openai_api');values.setdefault('ROCOTO_MANAGED_SPENDING_MODE','enforced')
  for key in names:
   value=getpass.getpass(key+' (hidden; Enter keeps the current entry): ').strip()
   if value:values[key]=value
  write_env(a.env_file,values);print(json.dumps({'saved':str(a.env_file),'configured_names':sorted(values),'values_printed':False}));return
 missing=[k for k in names if not values.get(k)];print(json.dumps({'configuration_file':str(a.env_file),'features':features,'missing_names':missing,'values_printed':False},indent=2));return int(bool(missing))
if __name__=='__main__':raise SystemExit(main())
