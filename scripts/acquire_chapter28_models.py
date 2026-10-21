"""Acquire only the immutable, ungated checkpoints used in Chapter 28.

Run explicitly once before the asset-dependent notebooks. Ordinary notebook execution
is offline and verifies the same hashes. No credentials or gated licence acceptance
are required. Model weights remain in ignored build/model-cache; do not commit them.
"""
from pathlib import Path
import hashlib,json
from huggingface_hub import hf_hub_download
ROOT=Path(__file__).resolve().parents[1]
MODELS=[
 {'repository':'Prior-Labs/TabPFN-v2-clf','revision':'f851f2a3c941544733b712d8c0f96dfae9b28862','filename':'tabpfn-v2-classifier-v2_default.ckpt','sha256':'cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49','bytes':29009539},
 {'repository':'jingang/TabICL','revision':'4dcd344ece2c00be9e831fdd35bed57b5ad83e19','filename':'tabicl-classifier-v2-20260212.ckpt','sha256':'bdc7dbd5e4ff21f8f0456fcf90c6b7cdf72dbea960f2d05b19bec19f9b3d4ed0','bytes':110368038},
 {'repository':'jingang/TabICL','revision':'4dcd344ece2c00be9e831fdd35bed57b5ad83e19','filename':'tabicl-regressor-v2-20260212.ckpt','sha256':'0db9cb538f114e79026bf08f45f41ad8dd7ad2de2aaca9a5ca8cd3bd9748ae7a','bytes':114324594},
]
if __name__=='__main__':
 for row in MODELS:
  path=Path(hf_hub_download(row['repository'],row['filename'],revision=row['revision'],cache_dir=ROOT/'build/model-cache'));data=path.read_bytes();assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'];print(json.dumps({**row,'verified':True}))
