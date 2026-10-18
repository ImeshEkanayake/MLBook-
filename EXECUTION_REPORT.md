# Execution report — code_001

**Verified:** 18 October 2026, Australia/Melbourne. **Publication:** Published on `main`; remote registry and notebook paths verified.

The [reference notebook](notebooks/001_Chapter_18_01_Decision_Tree.ipynb) was run top-to-bottom in a fresh kernel inside an isolated virtual environment installed from the pinned requirements. System site packages were disabled. `pip check` reported no broken requirements. The runner uses its exact interpreter and a temporary kernel specification; it imports no private project code. Ordinary notebook execution makes no network requests or data downloads. The full package set is preserved in [requirements-lock.txt](requirements-lock.txt).

## Actual reference environment and runtime

| Component | Version / observation |
| --- | --- |
| CPython | 3.14.3 |
| scikit-learn | 1.9.0 |
| NumPy / SciPy | 2.4.4 / 1.17.1 |
| pandas / Matplotlib | 3.0.3 / 3.11.0 |
| nbformat / nbclient / ipykernel | 5.11.1 / 0.11.0 / 7.4.0 |
| Hardware | Darwin arm64 CPU |
| Kernel execution | 21 code cells; no error outputs; 19 embedded PNG figures |
| Elapsed inside notebook | 1.640 seconds |
| Wall time including kernel lifecycle | 3.011 seconds |
| Main seed and split | 418; 1080 training / 360 validation / 360 sealed final rows |

Times describe this machine and run. Startup, font caches, package installation and other platforms can change them. macOS ARM64 with CPython 3.14.3 is the tested platform; broader compatibility is not asserted.

## Observed final assessment

The selection rule and 24 eligible depth × leaf-minimum candidates were declared before evaluation. Only training and validation were used to choose the final settings: **max_depth = 6, min_samples_leaf = 20**, with the remaining defaults and random state 418 fixed. The selected development validation balanced accuracy was **0.936111**. The selected configuration and prior baseline were refitted on the combined development rows and then assessed together once on the sealed 360-row test set.

| Model | Accuracy | Balanced accuracy | Log loss | Brier score |
| --- | ---: | ---: | ---: | ---: |
| Prior baseline | 0.500000 | 0.500000 | 0.693147 | 0.250000 |
| Selected tree | 0.933333 | 0.933333 | 0.635775 | 0.055044 |

These are synthetic-task observations, not engineering reliability measurements. A single split does not establish exact population performance or calibration. The tree's label accuracy improves strongly over the prior baseline, while its log loss shows that some probability estimates remain confidently wrong. No settings were changed in response to these test metrics. A subsequent edit shortened chart labels and made the runner clean up its kernel explicitly; the complete rerun preserved the same selected settings and final metrics.

## Substantive verification

- Main row identifiers are disjoint and exhaustive across the three splits. Exploration helpers access training/validation only. Final features/labels are materialized only in the final-assessment cell after choices are fixed; a guard prevents reuse within the same running kernel.
- The installed constructor's parameter/default dictionary matches the coverage table, and the executed experiment names match all 13 constructor controls: `ccp_alpha`, `class_weight`, `criterion`, `max_depth`, `max_features`, `max_leaf_nodes`, `min_impurity_decrease`, `min_samples_leaf`, `min_samples_split`, `min_weight_fraction_leaf`, `monotonic_cst`, `random_state`, `splitter`.
- The repeated fixed-seed fit has identical structure and labels. Stochastic comparisons report eight declared seeds, not a chosen best seed.
- The actual leaf probabilities match their training-label proportions. Minimum row support and weighted leaf-mass constraints are checked directly; the weighted demonstration uses non-uniform row weights.
- `entropy` and `log_loss` produce equivalent fitted outputs under fixed conditions. Integer/fractional leaf controls are checked at equivalent required counts. Pruning candidates are derived from training data only.
- The monotonic demonstration uses ordered synthetic load/resistance indices and a binary target. On the declared 51 × 51 grid, the constrained model has zero load/resistance order violations; the unconstrained fit has 96 and 146 respectively. Grid checks illustrate the mechanism and do not replace the implementation's stated constraint scope or independent physical validity tests.
- Representative conceptual, tree, boundary, complexity, weighting, pruning, monotonic, interaction and final-assessment figures were rendered and visually inspected. Long pruning-axis labels were shortened to readable values, and sweep axes explicitly identify categorical setting positions.
- Notebook format, execution counts, output sizes, registry paths, Markdown anchors and book links are checked before publication. Environments, build outputs and QA images remain ignored.

The notebook contains no assessment confidence intervals, real structural dataset, deployment pipeline or claim that all future book examples exist. Those are meaningful limits of this first teaching exemplar.
