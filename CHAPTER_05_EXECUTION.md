# Chapter 5 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** all five published and executed; remote tree verified.

Every cell ran in order in a fresh kernel using the unchanged runner. The five jobs ran concurrently; wall times include kernel lifecycle and are measurements, not performance promises. The notebooks import no private helpers and require no ordinary-run files, data downloads, keys or GPU. No dependency was added. Each printed CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0 and scikit-learn 1.9.0 on Darwin arm64 CPU. The full dependency lock remains unchanged.

| Example | Section | Code cells | Inline figures | Wall seconds incl. kernel |
| --- | --- | ---: | ---: | ---: |
| [code_022](CODE_EXAMPLES.md#code_022) | 5.1 | 6 | 2 | 1.461 |
| [code_023](CODE_EXAMPLES.md#code_023) | 5.2 | 5 | 2 | 1.635 |
| [code_024](CODE_EXAMPLES.md#code_024) | 5.3 | 6 | 2 | 1.879 |
| [code_025](CODE_EXAMPLES.md#code_025) | 5.4 | 6 | 2 | 1.505 |
| [code_026](CODE_EXAMPLES.md#code_026) | 5.5 | 6 | 2 | 1.481 |

Total: **29 executed code cells and ten inline figures**. Seeds 522–526, actual results, versions and kernel elapsed times are stored in the notebooks' final JSON summaries. All assertions passed. The source notebooks contain executed outputs.

## Results and interpretation

- **code_022:** 24 training buildings supply 384 training readings; known-building final has 96 readings, new-building final 144 readings from six independent buildings. The same fitted rule has development RMSE .0703773502/.7809324189 mm and final RMSE .0811412695/.7891573161 mm for known/new buildings. Training-only site intercepts are reused only for known buildings; new sites use the training-site mean. Row and equal-site MSE coincide because sizes are balanced. A query inside both feature ranges has joint-support distance .566609892 in declared normalized coordinates. This threshold diagnostic is not uncertainty calibration.
- **code_023:** training MSE for degrees 1/3/7/15 is .053791636/.033104144/.028436266/.020602649 mm². Development MSE is .064387295/.031858742/.040691856/796840.030915286 mm². The extreme degree-15 instability is retained, with a log-scaled figure, rather than changing the seed. Development selects degree three; the frozen cubic has final MSE .0387689419 mm². Across 250 independently generated training sets at x=.6, squared bias plus ddof=0 prediction variance exactly equals mean squared deviation from the known generator mean. Adding independent .18² mm² noise yields .064278221/.035739881/.040161619 mm² at degrees 1/3/7. This identity is specific to squared error and the stated conditioning/noise assumptions.
- **code_024:** OLS/ridge/20-step coefficient norms are .885549230/.761380303/.862591112. Ridge stationarity and equivalent predictions under a changed coefficient penalty pass. Line/spline/tree/isotonic fits use identical training rows; unsupported input regions are shaded. Separate actual additive, monotone and two-hidden-layer neural predictors use 240/100/100 train/development/final members and fixed settings. Structural additivity and monotonicity checks pass; the MLP converges in 440 iterations. Final RMSE is .086051263/.095921123/.086318395 mm for additive/monotone/neural models. These are predeclared mechanism fits, not equal-budget family benchmarks. An isotropic scalar rotation check preserves .5 m displacement.
- **code_025:** mean development MSE for nested sizes 12/24/48/96/192 is .025651429/.019197038/.017253071/.016677803/.016467091 mm². The plotted 10–90% band describes 30 training pools conditional on one fixed development set. In a separate known-slope sampling experiment, exact intercept MSE is .105675 mm² for 4×32 readings versus .011825 mm² for 36×2, with 400-repetition simulations retaining finite-simulation fluctuations. A ledger exposes missing material-B coverage despite 800 A readings. The predeclared cubic with a new n=192 training pool has .0156825776 mm² MSE on 500 fresh final members; no best replicate is selected.
- **code_026:** affine-model deviations from a known nonlinear generator are .0159181994 mm in range and .5086008290 mm at high loads. A constructed +.3 mm later-window offset changes the observation process. Shared-offset readings have within/between variance .000833564/.180942847 mm². Equal 500 N forces along anisotropic principal directions produce .5/.125 m ideal displacements. Physical force rotation with fixed anisotropic stiffness is not scalar target-preserving. Consistent rotation of stiffness, force and displacement is equivariant to 5.55e-17 m. A small equilibrium residual validates the declared solve, not a real structure.

## Assessment and scope boundaries

Training-only transformations and fits, development-only selection and fixed-rule final outcomes are explicit. Pure algebra, simulator-known means, acquisition designs and deliberately shifted stress cases are identified as such rather than reported as independent field assessment. Reading a final result spends that evidence for subsequent redesign; extensions need fresh final cases. Building independence, balanced sampling, mean-zero independent noise, loss units and representation scales are stated where required. Exchangeability is distinguished from independence.

All ten inline figures are visually reviewed with labels, units, descriptive text and grayscale line/marker distinctions. Seven selected experiments are reproduced as vector book figures by the local manuscript authoring pipeline and checked against the exact executed result dictionaries. Source/schema/sequential execution/no-error/meaningful assertions, manifest/summary agreement and local guide anchors are checked by scripts/check_chapter05.py. The 21 previous notebooks and manifest entries are preserved exactly. Only companion notebooks and documentation are published, not the manuscript or outline.

The laboratories do not establish real engineering validity, causal acquisition benefits, universally U-shaped validation curves, uncertainty calibration, general model-family rankings or a universal bias–variance decomposition for arbitrary losses. Hard constraints, finite penalties, checkpoint selection and augmentation assumptions have distinct meanings.

## Publication evidence

The first published content commit is [9ee5b87797374e258b7495d46e9d02d6baae8575](https://github.com/ImeshEkanayake/MLBook-/commit/9ee5b87797374e258b7495d46e9d02d6baae8575). The GitHub main-branch tree matched all 49 local tracked file blobs, including the five executed notebooks, registry, manifest, guide, report and checker. The following metadata commit records this successful check. Final branch/tree and raw-file byte comparisons are also recorded by the manuscript handoff.
