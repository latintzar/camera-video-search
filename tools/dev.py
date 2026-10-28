#!/usr/bin/env python3
"""Serve the original video workspace with retained processing and recipient-owned state."""
from pathlib import Path
import argparse,json,os,socket,ipaddress,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--state',type=Path,default=Path.home()/'.local/state/camera-video-search');parser.add_argument('--port',type=int,default=18530);parser.add_argument('--sample-dir',type=Path,help='Verified processed sample directory for an offline installation');parser.add_argument('--worker',action='store_true',help=argparse.SUPPRESS);args=parser.parse_args()
 if not 1024<=args.port<=65535:raise ValueError('Choose an unprivileged local port.')
 if not args.worker:
  from processed_sample import download_sample,verify_sample
  sample=verify_sample(args.sample_dir) if args.sample_dir else download_sample()
  env={k:v for k,v in os.environ.items() if k in ['PATH','HOME','LANG','LC_ALL','SSL_CERT_FILE','SSL_CERT_DIR']}
  env.update(ROCOTO_VERTICAL='retail',ROCOTO_RETAIL_LOCATION_CONTEXT='off',ROCOTO_RETAIL_REALTIME_READS='legacy',ROCOTO_BROWSE_SESSIONS='0',ROCOTO_TILE_RUNNER='off',ROCOTO_TILE_SCRIPT_EVENT_RUNS='off',ROCOTO_CUSTOM_EXECUTOR_ENABLED='0',ROCOTO_OPERATOR_ID='owner',ROCOTO_OPERATOR_NAME='Owner')
  return subprocess.call([sys.executable,str(Path(__file__).resolve()),'--worker','--state',str(args.state),'--port',str(args.port),'--sample-dir',str(sample)],cwd=ROOT,env=env)
 blocked=[0];audit=[None]
 def record_attempt():
  blocked[0]+=1
  if audit[0]:audit[0].write_text(json.dumps({'blocked_outbound_attempts':blocked[0]}))
 original_connect=socket.socket.connect;original_connect_ex=socket.socket.connect_ex;original_dns=socket.getaddrinfo
 def local(address):
  if isinstance(address,str):return True
  host=address[0]
  if host in ['localhost','']:return True
  try:return ipaddress.ip_address(host).is_loopback
  except ValueError:return False
 def connect(s,address):
  if not local(address):record_attempt();raise RuntimeError('Use the connected setup guide to enable provider networking.')
  return original_connect(s,address)
 def connect_ex(s,address):
  if not local(address):record_attempt();raise RuntimeError('Use the connected setup guide to enable provider networking.')
  return original_connect_ex(s,address)
 def dns(host,*a,**kw):
  if host is not None and not local((host,0)):record_attempt();raise RuntimeError('Use the connected setup guide to enable provider networking.')
  return original_dns(host,*a,**kw)
 socket.socket.connect=connect;socket.socket.connect_ex=connect_ex;socket.getaddrinfo=dns
 from processed_sample import install_sample
 result=install_sample(args.state,args.sample_dir)
 audit[0]=Path(result['state'])/'outbound-attempts.json';audit[0].write_text(json.dumps({'blocked_outbound_attempts':blocked[0]}));audit[0].chmod(0o600)
 print(json.dumps({**{k:result[k] for k in ['state','owner_code_file','basis','provider_calls']},'url':f'http://127.0.0.1:{args.port}/control-room/#clip=retailaction-000027-rank0'}),flush=True)
 sys.path.insert(0,str(ROOT/'harness'))
 import server,uvicorn
 uvicorn.run(server.create_app(args.state),host='127.0.0.1',port=args.port,log_level='warning',access_log=False)
 return 0
if __name__=='__main__':raise SystemExit(main())
