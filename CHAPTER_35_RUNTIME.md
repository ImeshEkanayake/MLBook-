# Chapter 35 runtime boundaries

Notebooks 183,184,185 and 187 use the unchanged main CPython 3.14.3 [requirements](requirements-lock.txt). Notebook 185 additionally requires the explicit [public checkpoint](CHAPTER_35_ASSETS.md).

Notebook 186 executes AutoGluon.tabular 1.6.3 in a separate CPython 3.12.13 environment. Upstream excludes Python 3.14; do not install it into the main or Chapter 30 environment. Tested on Apple Silicon CPU, one thread, no GPU. The direct [requirements](requirements-chapter35.txt) and complete [81-package lock](requirements-chapter35-lock.txt) pin the actual installed environment. Releases were checked against primary PyPI version records and all predate 19 October 2026 UTC; the book's literature cutoff remains 18 October 2026. Installation used an explicit pre-cutoff resolver limit. Access and execution date 22 October 2026.

From the companion root, with uv available:

```bash
uv venv --python 3.12 build/chapter35-runtime
uv pip sync --python build/chapter35-runtime/bin/python requirements-chapter35-lock.txt
build/chapter35-runtime/bin/python scripts/run_notebook.py notebooks/186_Chapter_35_04_native_automl_budget_and_auditable_workflow.ipynb
```

Tested key versions: AutoGluon 1.6.3, Torch 2.14.1, NumPy 2.5.4, SciPy 1.18.1, pandas 2.3.3, scikit-learn 1.9.1, LightGBM 4.7.0, Matplotlib 3.11.2. Native Torch imports before AutoGluon; the runner sets OMP/OpenBLAS/MKL thread counts to one, and native models request CPU 1/GPU 0. Ordinary execution is offline and creates temporary model files which are removed after prediction. No optional foundation model downloads are enabled.

The native generator is fitted on source features before the AutoML call. A fit-call audit verifies source-only fitting. Development labels guide stopping/selection/ensembling; final labels only assess the locked result. The manual comparator uses the same log-loss selection objective, grouped data roles and 15-second ceiling. These are finite teaching workflows with newly measured resource observations, not guarantees of identical wall time or exhaustive search.

One initial preflight without Torch emitted optional hardware-detection notices. The initial Torch-enabled shell produced no result JSON; later command success did not establish that the fit succeeded. A fresh Torch-first, one-thread preflight executed LightGBM, RandomForest, NeuralNetTorch and weighted ensemble successfully. The final notebook uses those verified controls and contains no stderr. Keep failure and version evidence when reproducing a workflow; do not infer a result from a later shell command's exit status.
