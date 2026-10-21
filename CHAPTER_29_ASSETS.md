# Chapter 29 explicit forecasting assets

Examples151/152 need explicitly acquired public model files before offline CPU inference. Examples150/153/154 generate all inputs and train their own declared teaching models. No named scientific checkpoint is silently replaced by these own models.

Run from this repository after installing requirements-lock.txt:

```bash
.venv/bin/python scripts/acquire_chapter29_models.py
```

The [machine-readable manifest](CHAPTER_29_ASSET_MANIFEST.json) pins every revision, SHA-256 and byte count. It covers the exact config, model card and safetensors files, approximately960MB combined. Caches live in ignored build/model-cache, never in Git. The notebooks verify every declared file before loading local directories and set Hub offline mode. Missing or mismatched assets fail with instructions. No credentials or GPU are needed for these ungated checkpoints.

- **TimesFM 2.5 200M PyTorch:** Google Research, immutable revision1d952420fba87f3c6dee4f240de0f1a0fbc790e3. Apache-2.0 weights and source; retained [notice](notices/FORECASTING_APACHE_LICENSE.txt). Label200M refers to the backbone; the loaded artifact includes an additional quantile head. The executed package3.0.2 can load this deliberately historical2.5 checkpoint. The cutoff source already offers TimesFM3.0, whose separately restricted default weights are not acquired here. Hosted-service terms are distinct.
- **Chronos-Bolt Tiny:** Amazon Science, immutable revisiona0e552de83495b5c28c14c71c374f3e33280b340. Apache-2.0; retained notice above. This is the patch-based direct quantile model, not original token-sampling Chronos or multivariate Chronos-2. Package2.3.2, Transformers5.20.1 and Accelerate1.15.0 are pinned.

Only code and provenance are published. The acquisition script performs an explicit download rather than making ordinary notebook execution silently access a remote service. Author corpus/benchmark claims are separated from these locally generated sensor comparisons. Generation after checkpoint publication does not establish private-site representativeness.
