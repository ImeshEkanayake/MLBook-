"""Explicitly acquire only the immutable public weights used by Chapter43 capstones."""
from pathlib import Path
import argparse,hashlib,json
from huggingface_hub import hf_hub_download
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'CHAPTER_43_ASSET_MANIFEST.json').read_text())
p=argparse.ArgumentParser();p.add_argument('--assets',nargs='+',choices=sorted(manifest['checkpoints']),default=sorted(manifest['checkpoints']));args=p.parse_args()
for name in args.assets:
 model=manifest['checkpoints'][name]
 for file in model['files']:
  path=ROOT/file['cache_relative_path']
  if not path.is_file():path=Path(hf_hub_download(model['repository'],file['filename'],revision=model['revision'],cache_dir=ROOT/'build/model-cache'))
  blob=path.read_bytes()
  if len(blob)!=file['bytes'] or hashlib.sha256(blob).hexdigest()!=file['sha256']:raise ValueError(f'Pinned bytes differ: {name}/{file["filename"]}')
  print(name,file['filename'],'verified',len(blob),'bytes')
