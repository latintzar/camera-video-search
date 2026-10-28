#!/usr/bin/env python3
"""Generate navigation for the retained product's named source definitions."""
from pathlib import Path
import ast,json,re
ROOT=Path(__file__).resolve().parents[1]
def main():
 symbols=[];routes=[];configuration=set()
 folders=[ROOT/'harness',ROOT/'backend/realtime',ROOT/'tools']
 for folder in folders:
  for p in sorted(folder.rglob('*.py')):
   if any(x in p.parts for x in ['tests','__pycache__','vendor']):continue
   tree=ast.parse(p.read_text());rel=str(p.relative_to(ROOT))
   for n in ast.walk(tree):
    if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
     doc=(ast.get_docstring(n) or '').split('\n\n')[0].replace('\n',' ')
     args=[a.arg for a in n.args.posonlyargs+n.args.args+n.args.kwonlyargs]
     if n.args.vararg:args.append('*'+n.args.vararg.arg)
     if n.args.kwarg:args.append('**'+n.args.kwarg.arg)
     symbols.append({'language':'Python','file':rel,'line':n.lineno,'name':n.name,'arguments':args,'description':doc[:380]})
     for d in n.decorator_list:
      if isinstance(d,ast.Call) and isinstance(d.func,ast.Attribute) and d.func.attr in ['get','post','patch','delete','put'] and d.args and isinstance(d.args[0],ast.Constant) and isinstance(d.args[0].value,str):routes.append({'method':d.func.attr.upper(),'path':d.args[0].value,'file':rel,'line':n.lineno,'function':n.name})
    if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr in ['getenv','get'] and n.args and isinstance(n.args[0],ast.Constant) and isinstance(n.args[0].value,str) and re.fullmatch(r'[A-Z][A-Z0-9_]+',n.args[0].value):configuration.add(n.args[0].value)
 for folder in [ROOT/'harness/web',ROOT/'harness/verticals/retail/web']:
  for p in sorted(folder.rglob('*.js')):
   if 'vendor' in p.parts:continue
   for number,line in enumerate(p.read_text().splitlines(),1):
    match=re.match(r'\s*(?:export\s+)?(?:async\s+)?function\s+(\w+)\s*\(([^)]*)\)',line)
    if match:symbols.append({'language':'JavaScript','file':str(p.relative_to(ROOT)),'line':number,'name':match[1],'arguments':[x.strip() for x in match[2].split(',') if x.strip()],'description':''})
 symbols.sort(key=lambda r:(r['file'],r['line'],r['name']))
 data={'scope':'Named Python definitions and JavaScript function declarations in the product, shared runtime and selected backend; containing source retains callbacks/local context.','symbols':symbols,'routes':routes,'configuration_names':sorted(configuration)}
 (ROOT/'docs/video-source-map.json').write_text(json.dumps(data,indent=2)+'\n')
 lines=['# Function reference','','[Architecture](video-architecture.md) · [Workflows](workflows.md) · [Setup](video-setup.md)','','Named Python definitions and JavaScript function declarations. Arguments list names; source links preserve the containing module and its callbacks.','','## Routes','','| Method | Path | Source |','| --- | --- | --- |']
 for r in routes:lines.append(f"| {r['method']} | `{r['path']}` | [{r['function']}](../{r['file']}#L{r['line']}) |")
 lines+=['','## Configuration','','Values belong in recipient-owned private runtime configuration.','',', '.join('`'+x+'`' for x in sorted(configuration)),'','## Definitions'];current=None
 for r in symbols:
  if current!=r['file']:current=r['file'];lines+=['','### '+current,'','| Function | Arguments | Source description |','| --- | --- | --- |']
  description=r['description'].replace('|','/').replace('\n',' ')
  lines.append(f"| [{r['name']}](../{r['file']}#L{r['line']}) | {', '.join(r['arguments'])} | {description} |")
 lines+=['','[made by atelier neyra](https://atelierneyra.com)',''];(ROOT/'docs/video-reference.md').write_text('\n'.join(lines));print(json.dumps({'symbols':len(symbols),'routes':len(routes),'configuration_names':len(configuration)}))
if __name__=='__main__':main()
