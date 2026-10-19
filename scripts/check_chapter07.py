"""Validate Chapter 7 notebook evidence, permanent IDs and local links."""
from pathlib import Path
import re,json
import nbformat
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'examples.json').read_text())['examples']
assert len({r['id'] for r in manifest})==len(manifest)
registry=(ROOT/'CODE_EXAMPLES.md').read_text()
for r in manifest:
 assert (ROOT/r['path']).is_file()
 assert f'<a id="{r["id"]}"></a>' in registry
chapter=[r for r in manifest if r['chapter']==7]
assert [r['id'] for r in chapter]==[f'code_{n:03d}' for n in range(32,37)]
code_count=figure_count=0
for r in chapter:
 path=ROOT/r['path'];book=nbformat.read(path,as_version=4);nbformat.validate(book)
 cells=[c for c in book.cells if c.cell_type=='code'];text='\n'.join(c.source for c in book.cells)
 assert [c.execution_count for c in cells]==list(range(1,len(cells)+1))
 assert not any(o.output_type=='error' for c in cells for o in c.outputs)
 source='\n'.join(c.source for c in cells)
 for forbidden in ['requests.','httpx.','urlopen(','read_csv(','read_parquet(','/Users/','sys.path','pip install','torch.hub','from examples']:
  assert forbidden not in source,(path.name,forbidden)
 assert len(re.findall(r'\bassert\b',source))>=6
 for target in re.findall(r'\]\(([^)]+)\)',text):
  if target.startswith(('https://','http://')):continue
  file,_,anchor=target.partition('#');dest=(path.parent/file).resolve() if file else path
  assert dest.exists(),(path.name,target)
  if anchor and dest.suffix=='.md':assert f'id="{anchor}"' in dest.read_text(),target
 count=sum('image/png' in o.get('data',{}) for c in cells for o in c.outputs)
 assert len(cells)==r['code_cells_executed'] and count==r['inline_figures']
 summaries=[]
 for c in cells:
  for o in c.outputs:
   if o.output_type=='stream':
    for line in o.text.splitlines():
     if line.startswith('EXECUTION_SUMMARY_JSON:'):summaries.append(json.loads(line.split(':',1)[1]))
 assert len(summaries)==1 and summaries[0]['example_id']==r['id']
 assert summaries[0]['versions']==r['tested_versions']
 code_count+=len(cells);figure_count+=count
for target in re.findall(r'\]\((notebooks/[^)]+)\)',(ROOT/'CHAPTER_07_GUIDE.md').read_text()):
 file,_,anchor=target.partition('#');dest=ROOT/file;assert dest.is_file()
 if anchor:
  book=nbformat.read(dest,as_version=4)
  assert f'id="{anchor}"' in '\n'.join(c.source for c in book.cells),(file,anchor)
assert code_count==29 and figure_count==10
print(json.dumps({'status':'passed','registry_examples':len(manifest),'chapter07_notebooks':5,
'executed_code_cells':code_count,'inline_figures':figure_count,'local_links_and_anchors':'valid',
'source_self_containment':'checked; inputs defined in notebook'},indent=2))

# Recover the actual committed reference input and verify the narrower code hash.
import base64,hashlib,ast
record=next(r for r in chapter if r['id']=='code_034')
book=nbformat.read(ROOT/record['path'],as_version=4)
summary=None;program=None
for c in book.cells:
 if c.cell_type!='code':continue
 for o in c.outputs:
  if o.output_type=='stream':
   for line in o.text.splitlines():
    if line.startswith('EXECUTION_SUMMARY_JSON:'):summary=json.loads(line.split(':',1)[1])
 for node in ast.parse(c.source).body:
  if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='MODEL_PROGRAM' for t in node.targets):program=ast.literal_eval(node.value)
result=summary['results'];snapshot=base64.b64decode(result['snapshot_base64']);header,payload=snapshot.split(bytes([10]),1)
assert hashlib.sha256(snapshot).hexdigest()==result['snapshot_sha256']
assert json.loads(header)['shape']==[360] and len(payload)==360*8
assert hashlib.sha256(program.encode()).hexdigest()==result['critical_program_sha256']
assert result['exact_replay'] and result['mutated_snapshot_rejected']
print('Recoverable snapshot and executed critical-program provenance: valid')
