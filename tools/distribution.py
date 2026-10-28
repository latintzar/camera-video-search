#!/usr/bin/env python3
"""Export a reviewed source-only archive with credentials/state/builds excluded."""
from pathlib import Path
import argparse,hashlib,json,os,tarfile
ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'.git','.venv','.local','__pycache__','.pytest_cache','node_modules','dist-preview'}
def files():
 for p in sorted(ROOT.rglob('*')):
  rel=p.relative_to(ROOT)
  if any(x in EXCLUDED for x in rel.parts) or not p.is_file():continue
  if p.is_symlink():raise ValueError('Review source symlinks before export.')
  if p.name.startswith('.env') and p.name!='.env.example':raise ValueError('Keep recipient configuration outside the export.')
  if p.suffix in ['.pyc','.sqlite','.sqlite3','.db'] or p.name.endswith('.tar.gz'):continue
  yield p
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--manifest',action='store_true');p.add_argument('--scan-directory',type=Path);p.add_argument('--archive',type=Path);a=p.parse_args();selected=list(files())
 if a.manifest:
  names={str(p.relative_to(ROOT)) for p in selected}|{'provenance/file-sha256.json'}
  (ROOT/'provenance/release-files.json').write_text(json.dumps({'files':sorted(names)},indent=2)+'\n')
  record={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files() if p!=ROOT/'provenance/file-sha256.json'}
  (ROOT/'provenance/file-sha256.json').write_text(json.dumps({'algorithm':'SHA-256','self_excluded':True,'files':record},indent=2)+'\n')
 if a.scan_directory:
  a.scan_directory.mkdir(mode=0o700,parents=True,exist_ok=False)
  for p in files():
   target=a.scan_directory/p.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True);os.link(p,target)
 if a.archive:
  if a.archive.resolve().is_relative_to(ROOT):raise ValueError('Export outside source.')
  with tarfile.open(a.archive,'x:gz') as t:
   for p in files():t.add(p,arcname='video-operations/'+str(p.relative_to(ROOT)),recursive=False)
  a.archive.chmod(0o600)
 print(json.dumps({'source_files':sum(1 for _ in files()),'source_bytes':sum(p.stat().st_size for p in files()),'history_included':False,'private_contexts_included':False}))
if __name__=='__main__':main()
