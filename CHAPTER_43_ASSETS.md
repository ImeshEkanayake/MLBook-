# Chapter 43 — explicit existing pretrained assets

code_226 runs actual TabPFN v2 classification, and code_228 runs actual Chronos-BoltTiny forecasting. The remaining three capstones generate every input internally. All task observations are generated. Native pretrained inference is not replaced by a teaching proxy when an asset is missing.

From the companion root in the main pinned environment, explicitly acquire once:

```bash
python scripts/acquire_chapter43_models.py
```

Optional `--assets tabpfn_v2_classifier` or `--assets bolt` limits acquisition. Existing Chapter28/29/35 caches are reused after verification. This script acquires only the required files; it does not fetch the unrelated TimesFM model. The [asset manifest](CHAPTER_43_ASSET_MANIFEST.json) fixes every revision, filename, byte count, SHA256 and cache-relative location. Missing or changed bytes fail explicitly. Notebooks verify hashes before native loading, use local paths and enable Hub offline mode. Ordinary execution is CPU-only and offline, with no credentials or gated acceptance. Weights remain ignored and are not published.

- **TabPFN v2 classifier:** `Prior-Labs/TabPFN-v2-clf`, revision `f851f2a3c941544733b712d8c0f96dfae9b28862`,29,009,539-byte `tabpfn-v2-classifier-v2_default.ckpt`. Built with PriorLabs-TabPFN; read the retained [licence and notice](notices/TABPFN_V2_LICENSE.txt). One CPU estimator uses explicit float32 inference; context fitting performs no gradient update.
- **Chronos-BoltTiny:** `amazon/chronos-bolt-tiny`, revision `a0e552de83495b5c28c14c71c374f3e33280b340`, README/config plus34,622,352-byte `model.safetensors`. Apache-2.0; retained [licence](notices/FORECASTING_APACHE_LICENSE.txt). Frozen local CPU float32 inference; its upstream pretraining differs from locally fitted baselines.

No new dependency or model asset is introduced; these exact caches and runtimes were used earlier in the book. Runtime/quality claims remain specific to the executed capstone and declared cohorts. Resource observations are actual run measurements and vary between kernel and separate vector-export runs; deterministic scientific RESULTS are checked independently.
