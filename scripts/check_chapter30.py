"""Validate Chapter 30 notebook evidence, permanent IDs and local links."""
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
chapter=[r for r in manifest if r['chapter']==30]
assert [r['id'] for r in chapter]==[f'code_{n:03d}' for n in range(155,161)]
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
 run=json.loads((ROOT/f'build/{r["id"]}.summary.json').read_text())
 assert summaries[0]['results']==run['results'] and summaries[0]['disclosed_warnings']==run['disclosed_warnings']
 code_count+=len(cells);figure_count+=count
for target in re.findall(r'\]\((notebooks/[^)]+)\)',(ROOT/'CHAPTER_30_GUIDE.md').read_text()):
 file,_,anchor=target.partition('#');dest=ROOT/file;assert dest.is_file()
 if anchor:
  book=nbformat.read(dest,as_version=4)
  assert f'id="{anchor}"' in '\n'.join(c.source for c in book.cells if c.cell_type=='markdown'),(file,anchor)
assert code_count==24 and figure_count==12

assets=json.loads((ROOT/'CHAPTER_30_ASSET_MANIFEST.json').read_text())
for row in chapter:
 keys=assets['example_checkpoints'][row['id']]
 assert row['data']['downloads_required']==bool(keys) and row['data']['runtime_downloads_required'] is False
 assert row['data']['checkpoint_assets']==[assets['checkpoints'][k] for k in keys]
 assert row['dependency_files']==assets['runtime_requirements'] and row['python_runtime']==assets['python_runtime']
 assert row['tested_versions']['python']=='3.12.13' and row['tested_versions']['torch']=='2.8.0'
 book=nbformat.read(ROOT/row['path'],as_version=4);source='\n'.join(c.source for c in book.cells if c.cell_type=='code');stderr='\n'.join(o.get('text','') for c in book.cells if c.cell_type=='code' for o in c.outputs if o.get('name')=='stderr')
 assert '/Users/' not in stderr
 if keys:
  assert "os.environ['HF_HUB_OFFLINE']='1'" in source
  assert 'TqdmWarning: IProgress not found' in stderr and 'NOTE: Redirects are currently not supported in Windows or MacOs.' in stderr
 else:assert not stderr
 if row['id'] in ['code_158','code_159']:assert 'choice:11+=' in stderr and 'RuntimeWarning' in stderr
 if row['id']=='code_158':assert 'causal_conv1d_fn' in stderr and 'chunk_gated_delta_rule' in stderr
 summary=json.loads((ROOT/f'build/{row["id"]}.summary.json').read_text())
 assert row['disclosed_warnings']==summary['disclosed_warnings']
for model in assets['checkpoints'].values():
 for file in model['files']:
  import hashlib
  path=ROOT/file['cache_relative_path'];assert path.stat().st_size==file['bytes']
  with path.open('rb') as stream:digest=hashlib.file_digest(stream,'sha256').hexdigest()
  assert digest==file['sha256']
for path in assets['publication_files']:assert (ROOT/path).is_file()
print(json.dumps({'status':'passed','registry_examples':len(manifest),'chapter30_notebooks':6,
'executed_code_cells':code_count,'inline_figures':figure_count,'local_links_and_anchors':'valid',
'source_self_containment':'checked; inputs defined in notebook'},indent=2))

