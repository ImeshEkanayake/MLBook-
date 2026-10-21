"""Explicit acquisition of the immutable public TabPFN v2 asset for Chapter35.3.
Ordinary notebook execution is offline. Weights stay in ignored build/model-cache.
"""
from pathlib import Path
import hashlib,json
from huggingface_hub import hf_hub_download
ROOT=Path(__file__).resolve().parents[1]
ASSET={'repository': 'Prior-Labs/TabPFN-v2-clf', 'revision': 'f851f2a3c941544733b712d8c0f96dfae9b28862', 'filename': 'tabpfn-v2-classifier-v2_default.ckpt', 'sha256': 'cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49', 'bytes': 29009539, 'cache_relative_path': 'build/model-cache/models--Prior-Labs--TabPFN-v2-clf/snapshots/f851f2a3c941544733b712d8c0f96dfae9b28862/tabpfn-v2-classifier-v2_default.ckpt', 'licence_notice': 'notices/TABPFN_V2_LICENSE.txt'}
if __name__=='__main__':
 p=Path(hf_hub_download(ASSET['repository'],ASSET['filename'],revision=ASSET['revision'],cache_dir=ROOT/'build/model-cache'))
 data=p.read_bytes();assert len(data)==ASSET['bytes'] and hashlib.sha256(data).hexdigest()==ASSET['sha256']
 print(json.dumps({'repository':ASSET['repository'],'revision':ASSET['revision'],'filename':ASSET['filename'],'sha256':ASSET['sha256'],'bytes':len(data),'verified':True}))
