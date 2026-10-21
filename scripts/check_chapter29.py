"""Validate Chapter 29 notebook evidence, permanent IDs and local links."""
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
chapter=[r for r in manifest if r['chapter']==29]
assert [r['id'] for r in chapter]==[f'code_{n:03d}' for n in range(150,155)]
code_count=figure_count=0
for r in chapter:
 path=ROOT/r['path'];book=nbformat.read(path,as_version=4);nbformat.validate(book)
 cells=[c for c in book.cells if c.cell_type=='code'];text='\n'.join(c.source for c in book.cells if c.cell_type=='markdown')
 assert [c.execution_count for c in cells]==list(range(1,len(cells)+1))
 assert not any(o.output_type=='error' for c in cells for o in c.outputs)
 source='\n'.join(c.source for c in cells)
 for forbidden in ['requests.','httpx.','urlopen(','read_csv(','read_parquet(','/Users/','sys.path','pip install','torch.hub','from examples']:
  assert forbidden not in source,(path.name,forbidden)
 assert len(re.findall(r'\bassert\b|\b(?:np|torch)\.testing\.assert_',source))>=3
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
for target in re.findall(r'\]\((notebooks/[^)]+)\)',(ROOT/'CHAPTER_29_GUIDE.md').read_text()):
 file,_,anchor=target.partition('#');dest=ROOT/file;assert dest.is_file()
 if anchor:
  book=nbformat.read(dest,as_version=4)
  assert f'id="{anchor}"' in '\n'.join(c.source for c in book.cells if c.cell_type=='markdown'),(file,anchor)
assert code_count==20 and figure_count==10

assets=json.loads((ROOT/'CHAPTER_29_ASSET_MANIFEST.json').read_text())
for row in chapter:
 keys=assets['example_checkpoints'][row['id']]
 assert row['data']['downloads_required']==bool(keys) and row['data']['runtime_downloads_required'] is False
 assert row['data']['checkpoint_assets']==[assets['checkpoints'][k] for k in keys]
 book=nbformat.read(ROOT/row['path'],as_version=4);source='\n'.join(c.source for c in book.cells if c.cell_type=='code')
 stderr=[''.join(o.get('text','')) for c in book.cells if c.cell_type=='code' for o in c.outputs if o.get('name')=='stderr']
 if keys:
  assert "os.environ['HF_HUB_OFFLINE']='1'" in source
  assert len(stderr)==1 and 'NOTE: Redirects are currently not supported in MacOs.' in stderr[0] and '/Users/' not in stderr[0]
 else:assert not stderr
for model in assets['checkpoints'].values():
 for file in model['files']:
  blob=(ROOT/file['cache_relative_path']).read_bytes()
  import hashlib
  assert len(blob)==file['bytes'] and hashlib.sha256(blob).hexdigest()==file['sha256']
for path in assets['publication_files']:assert (ROOT/path).is_file()
print(json.dumps({'status':'passed','registry_examples':len(manifest),'chapter29_notebooks':5,
'executed_code_cells':code_count,'inline_figures':figure_count,'local_links_and_anchors':'valid',
'source_self_containment':'checked; inputs defined in notebook'},indent=2))

