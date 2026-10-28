#!/usr/bin/env python3
"""Run source contracts and the recipient-owned fixture without provider access."""
from pathlib import Path
import json,os,subprocess,sys,time,tempfile
R=Path(__file__).resolve().parents[1]
SUITES={
 'starter':['tests/test_starter.py','tests/test_configure.py','tests/test_web_mount.py'],
 'source-pipeline':['harness/tests/'+n for n in ['test_source_intake.py','test_source_visibility.py','test_source_worker.py','test_source_embedding.py','test_source_routes.py','test_source_host_routes.py']],
 'retrieval-budget':['harness/tests/'+n for n in ['test_compute_guard.py','test_qdrant_retrieval.py','test_cosmos_publication.py','test_cosmos_retrieval.py','test_cosmos_inspect.py']],
 'events-player':['harness/tests/'+n for n in ['test_visit_basket.py','test_retail_stream_import.py','test_retail_script_signals.py','test_retail_settings.py','test_retail_urls.py','test_control_room.py']],
}
def main():
 env={k:v for k,v in os.environ.items() if k in ['PATH','HOME','LANG','LC_ALL','TMPDIR']};env.update(ROCOTO_VERTICAL='retail',VIDEO_OPERATIONS_MODAL_WORKSPACE='fixture-workspace',ROCOTO_OPERATOR_ID='operator@example.invalid',ROCOTO_RETAIL_LOCATION_CONTEXT='off',PYTHONPATH=str(R/'tools/offline'))
 out=R/'.local/verification';out.mkdir(parents=True,exist_ok=True);scratch=tempfile.TemporaryDirectory(prefix='video-operations-tests-');temporary=Path(scratch.name);rows=[]
 for name,paths in SUITES.items():
  paths=[str(R/p) for p in paths if (R/p).is_file()]
  start=time.monotonic();r=subprocess.run([sys.executable,'-m','pytest','-q','--basetemp='+str(temporary/name),*paths],cwd=R,env=env,capture_output=True,text=True)
  log=r.stdout+r.stderr;(out/(name+'.log')).write_text(log);row={'suite':name,'returncode':r.returncode,'seconds':round(time.monotonic()-start,2),'summary':log.splitlines()[-1:]};rows.append(row);print(name,'passed' if not r.returncode else 'FAILED; inspect private .local verification log',flush=True)
 (out/'checks.json').write_text(json.dumps({'external_network':'blocked','provider_service_clis':'blocked','suites':rows},indent=2)+'\n');scratch.cleanup();return int(any(x['returncode'] for x in rows))
if __name__=='__main__':raise SystemExit(main())
