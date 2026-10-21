"""Explicit acquisition and immutable hash verification for Chapter30 local models."""
from pathlib import Path
import hashlib,json
from huggingface_hub import hf_hub_download
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'CHAPTER_30_ASSET_MANIFEST.json').read_text())
for model in manifest['checkpoints'].values():
 for file in model['files']:
  path=Path(hf_hub_download(model['repository'],file['filename'],revision=model['revision'],cache_dir=ROOT/'build/model-cache'))
  blob=path.read_bytes();assert len(blob)==file['bytes'] and hashlib.sha256(blob).hexdigest()==file['sha256']
  print(model['repository'],file['filename'],'verified',len(blob),'bytes')
