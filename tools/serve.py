#!/usr/bin/env python3
"""Start the connected host with explicitly selected recipient configuration."""
from pathlib import Path
import argparse,json,os,subprocess,sys
from configure import read_env,DEFAULT
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--state',type=Path,required=True);p.add_argument('--env-file',type=Path,default=DEFAULT);p.add_argument('--port',type=int,default=18530);a=p.parse_args()
 from seed import private_state,write_json
 state=private_state(a.state)
 if not (state/'video-operations.json').exists():write_json(state/'video-operations.json',{'schema':1,'product':'video-operations','mode':'connected recipient host'})
 if not 1024<=a.port<=65535:raise ValueError('Choose an unprivileged local port.')
 values=read_env(a.env_file)
 sys.path.insert(0,str(ROOT/'harness'))
 import layout;layout.install('retail')
 from access import AccessStore
 access=AccessStore(state);access.create_environment('demo','Video operations');code=access.issue('demo',owner=True,principal_id='owner',display_name='Owner')
 codefile=state/'owner-code.txt';codefile.write_text(code+'\n');codefile.chmod(0o600)
 env={k:v for k,v in os.environ.items() if k in ['PATH','HOME','LANG','LC_ALL','SSL_CERT_FILE','SSL_CERT_DIR']}
 allowed={k:v for k,v in values.items() if k.startswith('ROCOTO_') or k in ['VIDEO_OPERATIONS_MODAL_WORKSPACE','RUNTIME_DATABASE_URL','HF_HOME','HF_TOKEN']}
 env.update(allowed);env['ROCOTO_VERTICAL']='retail'
 print(json.dumps({'mode':'connected recipient host','state':str(state),'configuration_names':sorted(allowed),'values_printed':False}),flush=True)
 return subprocess.call([sys.executable,str(ROOT/'harness/run.py'),'server','--state',str(state),'--port',str(a.port)],cwd=ROOT,env=env)
if __name__=='__main__':raise SystemExit(main())
