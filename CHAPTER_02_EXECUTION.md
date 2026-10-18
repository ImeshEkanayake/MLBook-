# Chapter 2 execution evidence

**Date:** 18 October 2026 (Australia/Melbourne). **Status:** all five notebooks executed; publication verification pending.

Every code cell ran in order in a fresh kernel using the existing runner and unchanged pinned environment. Each notebook supplies all imports, inputs, generators and helpers. Ordinary runs use no network data, keys, private project modules or GPU. No new dependency was introduced. Versions printed by every kernel: CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0 and scikit-learn 1.9.0. Hardware: Darwin arm64 CPU. Full pins are in [requirements-lock.txt](requirements-lock.txt).

| Example | Section | Code cells | Inline figures | Wall seconds incl. kernel lifecycle |
| --- | --- | ---: | ---: | ---: |
| [code_007](CODE_EXAMPLES.md#code_007) | 2.1 | 6 | 1 | 1.237 |
| [code_008](CODE_EXAMPLES.md#code_008) | 2.2 | 6 | 2 | 2.611 |
| [code_009](CODE_EXAMPLES.md#code_009) | 2.3 | 6 | 2 | 1.366 |
| [code_010](CODE_EXAMPLES.md#code_010) | 2.4 | 6 | 1 | 2.563 |
| [code_011](CODE_EXAMPLES.md#code_011) | 2.5 | 7 | 3 | 2.653 |

Total: **31 code cells, nine inline figures**. Runtimes are observed on this machine, not portability or performance guarantees. The first run executed all five notebooks concurrently; the final figure corrections reran code_007 and code_009 independently, and their table values reflect those final runs.

## Observed results and independent checks

- **code_007:** exact paired MSE is 0; the accidental all-pairs MSE is 1.3333333333 on the same three paired values. Two-spring displacements are 0.05 and 0.15 m; both recovered tensions are 100 N. Matrix residual and the unconstrained chain's rigid mode are checked. Separate and block-batched graph aggregation agree; graph means 2 and 5 match masked padded means.
- **code_008:** squared reconstruction errors for ranks 0/1/2 are 371.05814335, 5.50904436 and approximately 4.63e-30. One direction retains 98.5153% of centered squared variation yet removes an injected 0.2-norm low-variance signal to within 4.45e-16. Orthogonality, sign-invariant reconstruction and covariance/SVD eigenvalue correspondence pass. At condition number about 200000, a fixed 1e-4 response perturbation changes coefficient norm by 14.1421 while fitted-response change remains 1e-4.
- **code_009:** ideal du/dP=0.0005 m/N and du/dk=-0.000025 m²/N. The dimensionless stiffness-loss gradient is -0.3833860893. A manual neural reverse pass agrees with coordinate differences; maximum absolute error across five declared random directions is below 2.2e-12. The central-difference sweep has its best observed increment near 5.47e-6; at 1e-16 its relative error is about 0.117857. This is a scale/precision diagnostic, not a universal optimal increment.
- **code_010:** after 160 updates, ordinary stable loss is 0.00431631, deliberately unstable loss is about 8.803e14 and exact-curvature-scaled loss is about 5.302e-70. The feasible box optimum has loss 0.02 and a nonzero unconstrained gradient norm of 0.2, with negligible projected movement. Float32 cancellation yields 0 while float64 yields 1 for the chosen increment. A right-hand-side change near 1e-6 gives solution-change norm 1 despite tiny residuals. Full-rank design conditioning (~1045.79) is squared by its normal equations (~1093672.89).
- **code_011:** weighted integration gives 1 N while the unweighted node mean is 0.543333 N/m. Stencil/matrix maximum disagreement is about 1.11e-16. The stable field maximum ends at 0.781205 K; the deliberately unstable calculation grows to about 3.147e12 K. On 21/41/81-point grids at the same final time, max errors are 4.68559e-4, 1.16741e-4 and 2.91604e-5 K; error ratios are 4.01367 and 4.00340. Fixed endpoints, graph boundary conventions and multiple-input simulator shapes are checked. Periodic FFT amplitudes are 1 and 0.3; aliased cosine samples agree within 3.11e-15.

## Review scope

Notebook format, sequential execution counts, absence of error outputs, meaningful assertions, local links, explicit anchors, manifest uniqueness and self-containment are checked. All nine notebook figures are visually inspected; contrast in the error matrix and arrow endpoints in the dependency diagram were repaired and the affected notebooks rerun. Plot labels use declared units or dimensionless scales and distinguish curves by shape or line style. `pip check` verifies the existing environment. Original notebooks code_001–code_006 and their manifest records are preserved.

These are controlled mathematics laboratories, not fitted population-performance studies. A supervised split is not required to verify an algebraic identity or a numerical reference solution. A future predictive pipeline must fit scales, PCA and other representations on training information only. The exact-curvature optimization advantage is disclosed; fixed-end and periodic physical conventions are separated. No trained neural operator, generic autodiff library, causal effect or field-valid structural model is claimed. The manuscript and book figure sources remain outside this public repository.
