#!/usr/bin/env python3
"""Check native Home, tracker and recording UI with a recipient's private one-use code."""
from pathlib import Path
from urllib.parse import urlsplit
import argparse,json,os,stat
from playwright.sync_api import sync_playwright
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--base-url',default='http://127.0.0.1:18530');p.add_argument('--code-file',type=Path,default=Path.home()/'.local/state/video-operations/owner-code.txt');p.add_argument('--output',type=Path,default=Path('.local/browser-proof'));p.add_argument('--executable');a=p.parse_args()
 s=a.code_file.lstat()
 if not stat.S_ISREG(s.st_mode) or s.st_nlink!=1 or s.st_uid!=os.geteuid() or stat.S_IMODE(s.st_mode)&0o077:raise ValueError('Use the private owner code file.')
 code=a.code_file.read_text().strip();a.output.mkdir(parents=True,exist_ok=True);origin=urlsplit(a.base_url);rows=[]
 with sync_playwright() as p:
  launch={'headless':True}
  if a.executable:launch['executable_path']=a.executable
  browser=p.chromium.launch(**launch);login=browser.new_context();r=login.request.post(a.base_url+'/api/session',data={'code':code},headers={'X-Rocoto-Page':'1'});del code;assert r.status==200,r.status;storage=login.storage_state();login.close()
  for width in [1512,390]:
   context=browser.new_context(storage_state=storage,viewport={'width':width,'height':982 if width==1512 else 844},reduced_motion='reduce');page=context.new_page();errors=[];missing=[];external=[]
   def route(r):
    u=urlsplit(r.request.url)
    if u.scheme in ['http','https'] and (u.scheme,u.netloc)!=(origin.scheme,origin.netloc):external.append(u.path);return r.abort()
    r.continue_()
   context.route('**/*',route);page.on('pageerror',lambda e:errors.append(str(e)));page.on('response',lambda r:missing.append({'status':r.status,'path':urlsplit(r.url).path}) if r.status>=400 else None)
   r=page.goto(a.base_url+'/',wait_until='networkidle');page.wait_for_timeout(1200);frame=next(f for f in page.frames if '/control-room/' in f.url)
   home_text=frame.locator('body').inner_text();assert 'Example shop' in home_text and 'Visitors' in home_text and 'Product interactions' in home_text
   page.screenshot(path=str(a.output/f'home-{width}.png'));overflow=page.evaluate('document.documentElement.scrollWidth>innerWidth') or frame.evaluate('document.documentElement.scrollWidth>innerWidth')
   rows.append({'entry':'Home','width':width,'http_200':r.status==200,'overflow':overflow,'page_errors':len(errors),'missing_resources':len(missing),'external_requests':len(external)})
   r=page.goto(a.base_url+'/control-room/',wait_until='networkidle');page.wait_for_function('document.querySelector("#video").readyState>=2');video=page.locator('#video');duration=video.evaluate('(e)=>e.duration');assert duration==12
   page.evaluate('document.querySelector("#video").currentTime=4.5');page.wait_for_timeout(150);assert page.evaluate('allEvents().length')==3
   assert page.locator('#overlayModel').input_value()=='fixture';assert 'Authored annotations' in page.locator('#overlayModel').inner_text()
   video.evaluate('(e)=>e.play()');page.wait_for_timeout(300);advanced=video.evaluate('(e)=>e.currentTime')>4.5;video.evaluate('(e)=>e.pause()');assert advanced
   page.screenshot(path=str(a.output/f'player-{width}.png'));overflow=page.evaluate('document.documentElement.scrollWidth>innerWidth')
   rows.append({'entry':'Player','width':width,'http_200':r.status==200,'overflow':overflow,'duration_seconds':duration,'authored_annotations':3,'playback_advanced':advanced,'page_errors':len(errors),'missing_resources':len(missing),'external_requests':len(external)})
   assert not errors and not missing and not external,{'errors':errors,'missing':missing,'external':external};context.close()
  browser.close()
 result={'source':'actual native product with authored fixture','rows':rows,'credential_values_in_artifacts':False};(a.output/'proof.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));assert all(r['http_200'] and not r['overflow'] for r in rows)
if __name__=='__main__':main()
