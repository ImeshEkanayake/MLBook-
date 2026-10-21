# Chapter 30 local model assets

All task records are generated locally. Examples155/156/160 use a pinned small public instruction LLM;158 compares actual local Laya/Kev artifacts;159 uses Laya;157 trains an original small typed model internally. Jev is documented without calling its hosted service, spending account credits or claiming unobserved performance.

Use the dedicated [Python 3.12 runtime](CHAPTER_30_RUNTIME.md), then explicitly acquire assets:

```bash
build/chapter30-runtime/bin/python scripts/acquire_chapter30_models.py
```

The [manifest](CHAPTER_30_ASSET_MANIFEST.json) pins 33 files with SHA-256 and byte length, approximately 2.95 GB combined. Ordinary notebooks hash-check files and set Hub offline mode; they never silently download models. Weights/config/tokenizers live under ignored build/model-cache and are not redistributed. No private inputs, API credentials or GPU are needed for the declared CPU experiments.

- **HuggingFaceTB/SmolLM2-135M-Instruct**, revision 12fd25f77366fa6b3b4b768ec3050bf629380bac: actual small text-generating instruction model. Its restricted-label projection is explicitly distinguished from free generation and from probability calibration.
- **convaiinnovations/laya**, English revision 7b928d828b7b0e022f929d9bd2e44165aa270148: non-autoregressive typed model. The cached bundle includes its own encoder configuration, head, temperatures and tokenizer. No multilingual or separately task-adapted checkpoint is substituted.
- **jaredpalmer/kev-0.8b**, revision bf75a6a8848ea6960ff2ed108d9ed44c2941174f: adapter plus pointer head, tokenizer and provenance. Its head pins **Qwen/Qwen3.5-0.8B-Base** at dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68; that exact base is separately acquired. The adapter alone is not a complete model. Its stored temperature is upstream calibration evidence, not a guarantee for generated inspection tasks.

These artifacts' model cards identify Apache-2.0; an [Apache notice](notices/TEXT_DECISION_APACHE_LICENSE.txt) is retained. Author code and base/adapted weights are distinct artifacts with their own revision records. The numerical experiments, runtime controls and output diagnostics belong to their linked execution evidence; developer speed/accuracy claims are not local measurements. Model cards and provenance contain public source information only. No model weights or manuscript pages are published in this repository.
