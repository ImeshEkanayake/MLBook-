# Chapter 28 checkpoint acquisition and attribution

Built with PriorLabs-TabPFN.

These experiments explicitly use **TabPFN v2 classifier weights**, not the newer default TabPFN 3.5 weights. Code and weight licences differ. Read the [TabPFN v2 licence](notices/TABPFN_V2_LICENSE.txt) and [TabICL licence](notices/TABICL_LICENSE.txt). TabICLv2 is credited to Jingang Qu, David Holzmüller, Gaël Varoquaux and Marine Le Morvan, Soda team at Inria. No model weights are redistributed in this repository.

After installing the pinned environment, explicitly acquire the three ungated public checkpoints:

```bash
python scripts/acquire_chapter28_models.py
```

Acquisition is a separate network operation requiring about 254 MB of checkpoint bytes. No account, API key or automatic gated-terms acceptance is needed. Files are cached in ignored `build/model-cache/`. The script pins immutable Hub revisions and checks SHA-256 and byte length. Notebook inference sets Hub offline mode and checks local asset hashes again; missing assets produce an explicit acquisition instruction rather than an undisclosed download or substitute model.

| Model | Public repository and revision | File | Bytes | SHA-256 |
| --- | --- | --- | ---: | --- |
| TabPFN v2 classifier | `Prior-Labs/TabPFN-v2-clf`, `f851f2a3c941544733b712d8c0f96dfae9b28862` | `tabpfn-v2-classifier-v2_default.ckpt` | 29,009,539 | `cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49` |
| TabICLv2 classifier | `jingang/TabICL`, `4dcd344ece2c00be9e831fdd35bed57b5ad83e19` | `tabicl-classifier-v2-20260212.ckpt` | 110,368,038 | `bdc7dbd5e4ff21f8f0456fcf90c6b7cdf72dbea960f2d05b19bec19f9b3d4ed0` |
| TabICLv2 regressor | `jingang/TabICL`, `4dcd344ece2c00be9e831fdd35bed57b5ad83e19` | `tabicl-regressor-v2-20260212.ckpt` | 114,324,594 | `0db9cb538f114e79026bf08f45f41ad8dd7ad2de2aaca9a5ca8cd3bd9748ae7a` |

All three hashes and sizes match the corresponding Hub LFS objects. Repository metadata last changed on 26 April 2026 and 18 February 2026 respectively, before the book's 18 October 2026 literature cutoff. Native package releases TabPFN9.2.0 (12 October2026) and TabICL2.2.0 (2 September2026) are recorded separately from the checkpoint versions. Current family documentation is not evidence that these older checkpoint limits or licences describe every newer release.

Google TabFM1.0.0's code and default weights have separate terms. The default weights' `tabfm-non-commercial-v1.0` licence restricts commercial/production use, including outputs, and redistribution. They are not acquired or redistributed by this workflow; do not infer executed TabFM performance from the open-checkpoint comparisons. Its primary model documentation is discussed separately in the book.
