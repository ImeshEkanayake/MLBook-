# Chapter 2: mathematics concept-to-code guide

Five independent laboratories accompany the chapter's five numbered sections. Each contains setup, mathematical meaning, prediction prompts, controlled calculations, diagnostics, exercises, separate hints and source links. Permanent IDs are in [CODE_EXAMPLES.md](CODE_EXAMPLES.md); measurements are in [CHAPTER_02_EXECUTION.md](CHAPTER_02_EXECUTION.md). These demonstrate mechanisms rather than exhaust estimator constructors.

| Manuscript mechanism | Notebook section | Evidence or extension |
| --- | --- | --- |
| Scalar/vector/matrix/array axes; measurement units; affine map and dot products | [code_007: shape ledger](notebooks/007_Chapter_02_01_Vectors_Matrices_And_Tensors.ipynb#shape-ledger) | Labelled axes/units, elementwise versus contracted multiplication, deliberate same-shape unit error; tensor/missingness ledger exercise. |
| Broadcasting and row identity | [code_007: broadcasting](notebooks/007_Chapter_02_01_Vectors_Matrices_And_Tensors.ipynb#broadcast) | Paired versus accidental all-pairs loss, numeric heatmap and expected shapes; row-ID permutation exercise. |
| Linear maps, constrained equilibrium, units and rigid modes | [code_007: equilibrium](notebooks/007_Chapter_02_01_Vectors_Matrices_And_Tensors.ipynb#equilibrium) | Solve, force recovery, independent tensions and free-chain null vector; nonzero internal force exercise. |
| Unequal graph batches, masks and pooling units | [code_007: graph batches](notebooks/007_Chapter_02_01_Vectors_Matrices_And_Tensors.ipynb#graph-batches) | Block-diagonal/separate equivalence, no cross-graph edges and masked means. |
| Norms, similarity and reference scales | [code_008: scales](notebooks/008_Chapter_02_02_Geometry_Projections_And_Decompositions.ipynb#scales) | Unit conversion reverses raw nearest-neighbor choice; consistent reference scaling preserves normalized distance; one/infinity/Frobenius norm interpretations in prose/exercises. |
| Orthogonal projections, SVD, PCA, eigenvalues, arbitrary signs | [code_008: projection/SVD](notebooks/008_Chapter_02_02_Geometry_Projections_And_Decompositions.ipynb#projection-svd) | Rank 0/1/2 reconstructions, discarded-energy identity, orthogonal residual, sign invariance and covariance spectrum. |
| Compression versus task information and training-only representation fits | [code_008: weak signal](notebooks/008_Chapter_02_02_Geometry_Projections_And_Decompositions.ipynb#weak-signal) | Controlled low-variance perturbation is removed despite high retained variance; interpretation/assessment-boundary worksheet. |
| Nearly dependent columns, singular values and sensitivity | [code_008: conditioning](notebooks/008_Chapter_02_02_Geometry_Projections_And_Decompositions.ipynb#conditioning) | Fixed perturbation, changing column separation; coefficient and prediction norms distinguish instability. |
| Functions/domains, partial derivatives, units and first-order approximation | [code_009: spring derivatives](notebooks/009_Chapter_02_03_Derivatives_And_The_Chain_Rule.ipynb#spring-derivatives) | Analytic derivatives, normalized elasticities and increasing-increment approximation error. |
| Composite functions and chain rule | [code_009: chain rule](notebooks/009_Chapter_02_03_Derivatives_And_The_Chain_Rule.ipynb#chain-rule) | Positive stiffness parameterization, dimensionless loss, forward graph and analytic/finite-difference comparison. |
| Gradients, Jacobians, reverse accumulation, directional products | [code_009: reverse check](notebooks/009_Chapter_02_03_Derivatives_And_The_Chain_Rule.ipynb#reverse-check) | Manual tiny neural reverse pass, coordinate and five-direction checks; branching and force-direction Jacobian-solve exercises. |
| Finite differences, truncation, roundoff and autodiff distinction | [code_009: error sweep](notebooks/009_Chapter_02_03_Derivatives_And_The_Chain_Rule.ipynb#difference-sweep) | Float64 error-versus-increment curve and analytic reference; float32 extension; scope of automatic differentiation discussed explicitly. |
| Objective, curvature/Hessian, stable step interval and coordinate preconditioning | [code_010: quadratic](notebooks/010_Chapter_02_04_Optimization_And_Numerical_Computation.ipynb#quadratic) | Same loss/start, stable and unstable constant steps and exact-curvature scaled route. |
| Constraints and appropriate stopping diagnostics | [code_010: constraints](notebooks/010_Chapter_02_04_Optimization_And_Numerical_Computation.ipynb#constraints) | Feasible box optimum with nonzero gradient and negligible projected movement; stopping-report exercise. |
| Finite precision and cancellation | [code_010: precision](notebooks/010_Chapter_02_04_Optimization_And_Numerical_Computation.ipynb#precision) | Controlled float32/float64 increment calculation, distinguished from observation noise. |
| Solve versus inverse; residual/forward/backward error; least squares; regularization scope | [code_010: linear solves](notebooks/010_Chapter_02_04_Optimization_And_Numerical_Computation.ipynb#linear-solves) | Exact perturbation example, condition/residual diagnostics, least squares and squared normal-equations condition; penalty-preference worksheet rather than claiming information recovery. |
| Integrals, quadrature weights and physical averages | [code_011: integration](notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb#integration) | Exact linear integral on an irregular grid and wrong node-average interpretation; x² refinement extension. |
| ODE/PDE objects, initial and boundary conditions | [code_011: worksheet and diffusion](notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb#diffusion) | Object-role worksheet, complete fixed-end PDE specification, units and explicit time update. ODE integration is explained and classified, not claimed as a new implemented general ODE solver. |
| Discretization and graph Laplacians | [code_011: diffusion](notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb#diffusion) | Stencil/matrix equivalence, interior versus unconstrained path boundary degrees, constant-mode distinction; periodic conservation extension. |
| Stability, reference accuracy and refinement | [code_011: stability](notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb#stability) and [reference/refinement](notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb#reference-refinement) | Excited high-frequency failure, maximum-principle check, exact sine solution and three-grid equal-final-time comparison. |
| Fourier basis, frequency units and sampling ambiguity | [code_011: FFT/aliasing](notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb#fft-aliasing) | Periodic reconstruction, known cosine amplitudes/frequency labels and identical low/high-frequency samples. |
| Solution function, rate model, residual model and function-to-function operator | [code_011: reference/refinement](notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb#reference-refinement) and [exercises](notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb#exercises) | One simulator applied to several input fields; input/output/condition worksheet. No neural operator or PINN training is claimed. |

## Controls and interpretation

Graph masks and schema are representation controls. Reference scales and coordinate transformations define geometry. Step size, dtype, finite-difference increment, mesh spacing and time step are numerical controls. Stiffness, diffusion coefficient, forcing and boundary values are assumed system quantities. PCA rank is a representation choice. They should not all be called model hyperparameters.

No empirical score is selected on a repeatedly viewed final set here. The tests compare algebraic identities, known solutions and controlled perturbations. If adapting the examples to learned predictive models, restore entity/time/spatial information boundaries and reserve fresh assessment data. Numerical correctness supports only the stated calculation. It cannot establish physical validity, identifiability, causality or generalization on its own.

## Run

From the activated environment at repository root:

```bash
python scripts/run_notebook.py notebooks/007_Chapter_02_01_Vectors_Matrices_And_Tensors.ipynb
python scripts/run_notebook.py notebooks/008_Chapter_02_02_Geometry_Projections_And_Decompositions.ipynb
python scripts/run_notebook.py notebooks/009_Chapter_02_03_Derivatives_And_The_Chain_Rule.ipynb
python scripts/run_notebook.py notebooks/010_Chapter_02_04_Optimization_And_Numerical_Computation.ipynb
python scripts/run_notebook.py notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb
```

The default output goes to ignored `build/`, preserving the committed reference. Source paths passed with `--output` intentionally replace that reference after a successful complete run. Restart and run all after editing; do not rely on stored outputs or partial execution.
