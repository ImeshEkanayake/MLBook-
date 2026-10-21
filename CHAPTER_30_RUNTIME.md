# Chapter 30 isolated CPU runtime

Kev's pinned author source requires Python>=3.12,<3.14, Torch>=2.6,<2.9, NumPy>=2.5.3 and scikit-learn>=1.9.1. The earlier chapters' tested Python 3.14/Torch 2.14 environment remains unchanged. Chapter 30 therefore uses its own explicit Python 3.12 virtual environment; do not upgrade the earlier .venv to satisfy this chapter.

Verified interpreter for setup: CPython 3.12.13 on Darwin arm64. From this repository:

```bash
python3.12 -m venv build/chapter30-runtime
build/chapter30-runtime/bin/python -m pip install setuptools==84.0.0
build/chapter30-runtime/bin/python -m pip install --no-build-isolation -r requirements-chapter30-lock.txt
build/chapter30-runtime/bin/python -m pip check
build/chapter30-runtime/bin/python scripts/acquire_chapter30_models.py
```

The [direct requirements](requirements-chapter30.txt) name actual native packages and the immutable Kev source commit. The [complete lock](requirements-chapter30-lock.txt) pins 103 installed package selections, including NumPy 2.5.3, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.1, Torch 2.8.0, Laya 0.4.11, Transformers 5.20.1, PEFT 0.21.2, Accelerate 1.15.0 and Hub 1.33.0. All resolved package releases were checked against the 18 October 2026cutoff; six default post-cutoff choices were replaced before installation. The verified source build constrained setuptools 84.0.0. The setup above installs that backend first and disables build isolation so a later backend is not silently selected. Pip check passes. The earlier119-package environment remains byte-for-byte unchanged in its freeze record.

Execute a laboratory in a fresh kernel using the same runtime:

```bash
build/chapter30-runtime/bin/python scripts/run_notebook.py notebooks/155_Chapter_30_01_structured_records_and_native_language_prediction.ipynb
```

All task-generating helpers are internal to their notebooks. Declared model assets are explicit external prerequisites; missing or mismatched files fail with acquisition instructions. Use the same dedicated interpreter for this chapter's figure producer/checker. Kernel outputs retain their actual versions and CPU controls; Python 3.12 results are not mislabelled as the earlier3.14 environment. No hosted model calls or paid infrastructure are required.
