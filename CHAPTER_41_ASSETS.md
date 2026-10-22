# Chapter 41.3 — explicitly cached foundation checkpoint

code_218 uses the real pinned TabPFN v2 classifier, reusing the existing Chapter35 acquisition. Four other Chapter41 laboratories generate all inputs internally. No new dependency or checkpoint is introduced.

From the companion root, explicitly acquire once in the main pinned environment:

```bash
python scripts/acquire_chapter35_model.py
```

Read the [existing acquisition details](CHAPTER_35_ASSETS.md), [Chapter41 manifest](CHAPTER_41_ASSET_MANIFEST.json) and retained [licence/notice](notices/TABPFN_V2_LICENSE.txt). Built with PriorLabs-TabPFN. Immutable repository `Prior-Labs/TabPFN-v2-clf`, revision `f851f2a3c941544733b712d8c0f96dfae9b28862`, file `tabpfn-v2-classifier-v2_default.ckpt`,29,009,539 bytes, SHA256 `cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49`. Full cache-relative path is in the manifest. The notebook checks bytes/hash and sets `HF_HUB_OFFLINE=1`; missing or changed files fail explicitly. Ordinary inference is offline/CPU with no credentials. The library's newer default weights are not substituted.

Pretraining is upstream information; source-context fitting is recorded separately and performs no gradient update. The first inference call prepares the dtype/device representation, then unchanged-parameter checks cover subsequent predictions. Resource timings are observations, not guaranteed performance. Only code/guides/metadata are published; weights remain ignored.
