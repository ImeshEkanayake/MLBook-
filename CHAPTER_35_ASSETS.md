# Chapter 35.3 — explicit public checkpoint asset

Notebook 185 executes native TabPFN v2 inference; it does not replace a missing model with a teaching proxy. Inputs and helpers are defined in the notebook, but the pretrained public checkpoint must be acquired explicitly once. No credentials, gated licence acceptance or ordinary-run network is required.

From the companion root in the main pinned environment:

```bash
python scripts/acquire_chapter35_model.py
```

This downloads only the immutable TabPFN v2 classifier used in the [asset manifest](CHAPTER_35_ASSET_MANIFEST.json). Existing Chapter 28 cache bytes can be reused: repository `Prior-Labs/TabPFN-v2-clf`, revision `f851f2a3c941544733b712d8c0f96dfae9b28862`, file `tabpfn-v2-classifier-v2_default.ckpt`, 29,009,539 bytes, SHA-256 `cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49`. The cache-relative path is in the manifest. The executed notebook verifies length/hash and sets `HF_HUB_OFFLINE=1`; missing or changed bytes fail explicitly.

Built with PriorLabs-TabPFN. Read the retained [TabPFN v2 licence and notice](notices/TABPFN_V2_LICENSE.txt). Checkpoint context/labels are task information, while pretraining is upstream information with a different compute history. The library's newer default models are not substituted. Only guides, code and metadata are published here; weights remain ignored.

Other Chapter 35 notebooks generate their own inputs. Notebook 186 uses the separate [AutoGluon runtime](CHAPTER_35_RUNTIME.md) and creates temporary fitted models during execution; those files are outputs, not downloaded model inputs.
