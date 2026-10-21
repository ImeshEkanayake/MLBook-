# Book code examples

This directory is the stable destination for book code hyperlinks. IDs persist independently of chapter numbering and filenames. Only implemented, verified examples are listed; planned future notebooks are not represented as completed work.

A visible book marker must be an actual link:

```markdown
[#code_001](https://github.com/ImeshEkanayake/MLBook-/blob/main/CODE_EXAMPLES.md#code_001)
```

A bare `#code_001` does not create a remote hyperlink. If a notebook moves, retain its anchor here and update the relative target and [machine-readable registry](examples.json). For a printed book, use the readable ID plus this repository's code directory URL.

<a id="code_001"></a>
## code_001 — Decision trees: rules, complexity and controlled experiments

| Field | Reference |
| --- | --- |
| Permanent ID | `code_001` |
| Book home | Chapter 18, subtopic 18.1 — Decision trees and recursive partitioning |
| Notebook | [001_Chapter_18_01_Decision_Tree.ipynb](notebooks/001_Chapter_18_01_Decision_Tree.ipynb) |
| Dataset | Deterministic local synthetic moons; separate weighted, imbalanced, extra-noise-feature and ordered-feature development demonstrations. No measured structural data. |
| Dependencies | [Direct pins](requirements.txt) · [Complete tested environment](requirements-lock.txt) |
| Tested environment | CPython 3.14.3; scikit-learn 1.9.0; NumPy 2.4.4; SciPy 1.17.1; pandas 3.0.3; Matplotlib 3.11.0 |
| Hardware | macOS ARM64 CPU; no GPU or external data services |
| Measured runtime | 3.011 seconds including fresh-kernel lifecycle; 1.640 seconds inside the notebook on the reference run. Allow extra time for installation, startup and font caches. |
| Coverage | All 13 exposed classifier constructor parameters, one depth × leaf-support interaction, model guide, 19 inline figures and eight exercises |
| Verification | 21 code cells executed in order in a fresh kernel; assertions passed; final test used only after selection; [execution evidence](EXECUTION_REPORT.md) |
| Status | Published on `main`; remote registry and notebook paths verified. |
| Checked date | 18 October 2026 (Australia/Melbourne) |

[Open the notebook](notebooks/001_Chapter_18_01_Decision_Tree.ipynb) and work through predictions before changing settings. Use [AUTHORING_GUIDE.md](AUTHORING_GUIDE.md) when adding another example. This is one complete reference example, not executable coverage of the entire book.

<!-- CHAPTER_01_ENTRIES -->

## Chapter 1 companion series

Five independent, executable concept notebooks. Read the [concept traceability guide](CHAPTER_01_GUIDE.md) and [measured run report](CHAPTER_01_EXECUTION.md). These introduce task families and assumptions; complete model-specific parameter labs are deferred to their model chapters.

<a id="code_002"></a>
### code_002 — Specify the task and respect the information clock

- **Book home:** section 1.1.
- **Notebook:** [002_Chapter_01_01_Task_Framing.ipynb](notebooks/002_Chapter_01_01_Task_Framing.ipynb).
- **Data and dependencies:** local synthetic data; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** task specification, observation versus action units, event versus availability time, future-information leakage, label horizon, follow-up and repeated entities.
- **Verification:** 5 code cells, 1 figures; fresh-kernel wall time 1.296 seconds on CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main and remote paths verified; checked 18 October 2026. [Run evidence](CHAPTER_01_EXECUTION.md).

<a id="code_003"></a>
### code_003 — Prediction and discovery on related observations

- **Book home:** section 1.2.
- **Notebook:** [003_Chapter_01_02_Prediction_And_Discovery.ipynb](notebooks/003_Chapter_01_02_Prediction_And_Discovery.ipynb).
- **Data and dependencies:** local synthetic data; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** regression, classification, ranking and capacity metrics, clustering, anomaly reference, descriptive versus causal claims.
- **Verification:** 5 code cells, 2 figures; fresh-kernel wall time 5.389 seconds on CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main and remote paths verified; checked 18 October 2026. [Run evidence](CHAPTER_01_EXECUTION.md).

<a id="code_004"></a>
### code_004 — Generate scenarios, simulate forward, and infer what is identifiable

- **Book home:** section 1.3.
- **Notebook:** [004_Chapter_01_03_Generation_Simulation_And_Inversion.ipynb](notebooks/004_Chapter_01_03_Generation_Simulation_And_Inversion.ipynb).
- **Data and dependencies:** local synthetic data; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** scenario generation and dependence, Hooke-law units and assumptions, forward simulation, surrogate approximation, inverse effective compliance, structural non-identifiability, additional measurements.
- **Verification:** 5 code cells, 2 figures; fresh-kernel wall time 1.956 seconds on CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main and remote paths verified; checked 18 October 2026. [Run evidence](CHAPTER_01_EXECUTION.md).

<a id="code_005"></a>
### code_005 — Turn scores into actions and follow their consequences

- **Book home:** section 1.4.
- **Notebook:** [005_Chapter_01_04_Decisions_And_Sequential_Interaction.ipynb](notebooks/005_Chapter_01_04_Decisions_And_Sequential_Interaction.ipynb).
- **Data and dependencies:** local synthetic data; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** probabilities versus actions, capacity and expected cost, causal prevention assumptions, policy and state, sequential transitions, terminal fairness, planning baseline versus RL.
- **Verification:** 4 code cells, 2 figures; fresh-kernel wall time 1.825 seconds on CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main and remote paths verified; checked 18 October 2026. [Run evidence](CHAPTER_01_EXECUTION.md).

<a id="code_006"></a>
### code_006 — One small building, several useful representations

- **Book home:** section 1.5.
- **Notebook:** [006_Chapter_01_05_Representations_And_Reading_Map.ipynb](notebooks/006_Chapter_01_05_Representations_And_Reading_Map.ipynb).
- **Data and dependencies:** local synthetic data; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** tabular entities, relational keys and cardinality, graph adjacency and permutation, spatial coordinates, temporal order versus summaries, task architecture objective adaptation, baseline-first resource plan.
- **Verification:** 5 code cells, 2 figures; fresh-kernel wall time 1.298 seconds on CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main and remote paths verified; checked 18 October 2026. [Run evidence](CHAPTER_01_EXECUTION.md).

<!-- CHAPTER_02_ENTRIES -->

## Chapter 2 mathematics laboratories

Five independent numerical laboratories. Use the [concept-to-code guide](CHAPTER_02_GUIDE.md) and [actual run evidence](CHAPTER_02_EXECUTION.md). They check mathematical mechanisms under declared assumptions; they do not claim empirical engineering performance or exhaustive estimator API coverage.

<a id="code_007"></a>
### code_007 — Vectors, matrices and tensors as data

- **Book home:** section 2.1.
- **Notebook:** [007_Chapter_02_01_Vectors_Matrices_And_Tensors.ipynb](notebooks/007_Chapter_02_01_Vectors_Matrices_And_Tensors.ipynb).
- **Data/dependencies:** local synthetic arrays and exact toy equations; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** axis and units ledger, dot products and affine maps, broadcast failure, constrained spring equilibrium, graph batching and masks.
- **Verification:** 6 code cells, 1 inline figures; 1.237 seconds including fresh-kernel lifecycle, CPython 3.14.3 / NumPy 2.4.4, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 18 October 2026. [Run evidence](CHAPTER_02_EXECUTION.md).

<a id="code_008"></a>
### code_008 — Geometry, projections and decompositions

- **Book home:** section 2.2.
- **Notebook:** [008_Chapter_02_02_Geometry_Projections_And_Decompositions.ipynb](notebooks/008_Chapter_02_02_Geometry_Projections_And_Decompositions.ipynb).
- **Data/dependencies:** local synthetic arrays and exact toy equations; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** norms and reference scales, orthogonal projection, SVD and PCA reconstruction, discarded low-variance signal, conditioning and coefficient sensitivity.
- **Verification:** 6 code cells, 2 inline figures; 2.611 seconds including fresh-kernel lifecycle, CPython 3.14.3 / NumPy 2.4.4, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 18 October 2026. [Run evidence](CHAPTER_02_EXECUTION.md).

<a id="code_009"></a>
### code_009 — Functions, derivatives and the chain rule

- **Book home:** section 2.3.
- **Notebook:** [009_Chapter_02_03_Derivatives_And_The_Chain_Rule.ipynb](notebooks/009_Chapter_02_03_Derivatives_And_The_Chain_Rule.ipynb).
- **Data/dependencies:** local synthetic arrays and exact toy equations; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** derivative units, spring sensitivities, chain rule and dimensionless loss, manual reverse accumulation, coordinate and directional finite differences, step-size error tradeoff.
- **Verification:** 6 code cells, 2 inline figures; 1.366 seconds including fresh-kernel lifecycle, CPython 3.14.3 / NumPy 2.4.4, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 18 October 2026. [Run evidence](CHAPTER_02_EXECUTION.md).

<a id="code_010"></a>
### code_010 — Optimization and numerical computation

- **Book home:** section 2.4.
- **Notebook:** [010_Chapter_02_04_Optimization_And_Numerical_Computation.ipynb](notebooks/010_Chapter_02_04_Optimization_And_Numerical_Computation.ipynb).
- **Data/dependencies:** local synthetic arrays and exact toy equations; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** quadratic curvature and step stability, coordinate scaling and preconditioning, box constraints, float32 cancellation, residual versus solution sensitivity, least squares and squared conditioning.
- **Verification:** 6 code cells, 1 inline figures; 2.563 seconds including fresh-kernel lifecycle, CPython 3.14.3 / NumPy 2.4.4, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 18 October 2026. [Run evidence](CHAPTER_02_EXECUTION.md).

<a id="code_011"></a>
### code_011 — Just-in-time mathematics for scientific models

- **Book home:** section 2.5.
- **Notebook:** [011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb](notebooks/011_Chapter_02_05_Mathematics_For_Scientific_Models.ipynb).
- **Data/dependencies:** local synthetic arrays and exact toy equations; no downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** weighted integration, ODE versus PDE worksheet, explicit diffusion and boundary conditions, time-step stability, stencil and graph correspondence, sine reference and refinement, periodic FFT and aliasing, function-to-function operator family.
- **Verification:** 7 code cells, 3 inline figures; 2.653 seconds including fresh-kernel lifecycle, CPython 3.14.3 / NumPy 2.4.4, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 18 October 2026. [Run evidence](CHAPTER_02_EXECUTION.md).

<!-- CHAPTER_03_ENTRIES -->

## Chapter 3 probability, statistics and uncertainty

Five independent laboratories with explicit sampling and measurement assumptions. Read the [traceability guide](CHAPTER_03_GUIDE.md) and [actual run evidence](CHAPTER_03_EXECUTION.md). These are scoped mechanism experiments, not empirical safety assessments or exhaustive estimator-constructor labs.

<a id="code_012"></a>
### code_012 — Random variables and conditional distributions

- **Book home:** section 3.1.
- **Notebook:** [012_Chapter_03_01_Random_Variables_And_Conditional_Distributions.ipynb](notebooks/012_Chapter_03_01_Random_Variables_And_Conditional_Distributions.ipynb).
- **Data/dependencies:** self-contained invented populations and generated measurements; no data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** joint marginal and conditional probabilities, explicit denominators and reverse conditionals, independence, population mixtures, expectation and variance, continuous density units.
- **Verification:** 6 code cells, 2 inline figures; 1.620 seconds including fresh-kernel lifecycle on CPython 3.14.3 / SciPy 1.17.1, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_03_EXECUTION.md).

<a id="code_013"></a>
### code_013 — Sampling and data-generating processes

- **Book home:** section 3.2.
- **Notebook:** [013_Chapter_03_02_Sampling_And_Data_Generating_Processes.ipynb](notebooks/013_Chapter_03_02_Sampling_And_Data_Generating_Processes.ipynb).
- **Data/dependencies:** self-contained invented populations and generated measurements; no data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** population and observation units, hierarchical dependence, equal-row sampling designs, design effect and sampling distribution, selection bias, measurement offset.
- **Verification:** 6 code cells, 2 inline figures; 1.659 seconds including fresh-kernel lifecycle on CPython 3.14.3 / SciPy 1.17.1, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_03_EXECUTION.md).

<a id="code_014"></a>
### code_014 — Estimation, likelihood and Bayesian updating

- **Book home:** section 3.3.
- **Notebook:** [014_Chapter_03_03_Estimation_Likelihood_And_Bayesian_Updating.ipynb](notebooks/014_Chapter_03_03_Estimation_Likelihood_And_Bayesian_Updating.ipynb).
- **Data/dependencies:** self-contained invented populations and generated measurements; no data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** binomial likelihood and MLE, beta prior and posterior, sequential equivalence, credible intervals, predictive versus parameter uncertainty, zero outcomes and prior sensitivity.
- **Verification:** 7 code cells, 2 inline figures; 1.650 seconds including fresh-kernel lifecycle on CPython 3.14.3 / SciPy 1.17.1, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_03_EXECUTION.md).

<a id="code_015"></a>
### code_015 — Statistical comparisons and resampling

- **Book home:** section 3.4.
- **Notebook:** [015_Chapter_03_04_Statistical_Comparisons_And_Resampling.ipynb](notebooks/015_Chapter_03_04_Statistical_Comparisons_And_Resampling.ipynb).
- **Data/dependencies:** self-contained invented populations and generated measurements; no data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** paired equal-building estimand, cluster versus row bootstrap, percentile interval limitations, practical effect size, assumption-dependent sign-flip test, multiple comparisons and Bonferroni.
- **Verification:** 6 code cells, 2 inline figures; 1.664 seconds including fresh-kernel lifecycle on CPython 3.14.3 / SciPy 1.17.1, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_03_EXECUTION.md).

<a id="code_016"></a>
### code_016 — Kinds and sources of uncertainty

- **Book home:** section 3.5.
- **Notebook:** [016_Chapter_03_05_Kinds_And_Sources_Of_Uncertainty.ipynb](notebooks/016_Chapter_03_05_Kinds_And_Sources_Of_Uncertainty.ipynb).
- **Data/dependencies:** self-contained invented populations and generated measurements; no data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** predictive variance decomposition, mean versus future-outcome intervals, measurement noise versus bias, training-only compliance estimate, held-out material shift, coverage and interval scope ledger.
- **Verification:** 7 code cells, 2 inline figures; 1.650 seconds including fresh-kernel lifecycle on CPython 3.14.3 / SciPy 1.17.1, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_03_EXECUTION.md).

<!-- CHAPTER_04_ENTRIES -->

## Chapter 4: how models learn

Five independent laboratories connect objectives, updates, reusable state and diagnostics. Read the [traceability guide](CHAPTER_04_GUIDE.md) and [actual execution evidence](CHAPTER_04_EXECUTION.md). These are scoped mechanism experiments with declared synthetic data, not exhaustive estimator-constructor or foundation-model benchmarks.

<a id="code_017"></a>
### code_017 — Parameters, predictions and objectives

- **Book home:** section 4.1.
- **Notebook:** [017_Chapter_04_01_Parameters_Predictions_And_Objectives.ipynb](notebooks/017_Chapter_04_01_Parameters_Predictions_And_Objectives.ipynb).
- **Data/dependencies:** generated observations, source samples and tasks; no ordinary-run data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** task and independent split contract, parameter hyperparameter state ledger, unit-aware empirical risk, training-only least squares and baseline, gradient stationarity, one-example predict compare adjust.
- **Verification:** 7 code cells, 1 inline figures; 2.277 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_04_EXECUTION.md).

<a id="code_018"></a>
### code_018 — Loss functions and output meanings

- **Book home:** section 4.2.
- **Notebook:** [018_Chapter_04_02_Loss_Functions_And_Output_Meanings.ipynb](notebooks/018_Chapter_04_02_Loss_Functions_And_Output_Meanings.ipynb).
- **Data/dependencies:** generated observations, source samples and tasks; no ordinary-run data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** squared absolute and pinball output meanings, mean median and quantile fit, sigmoid and Bernoulli cross entropy, stable score-space loss, declared split and estimator controls, held-out output assessment.
- **Verification:** 6 code cells, 2 inline figures; 2.618 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_04_EXECUTION.md).

<a id="code_019"></a>
### code_019 — Gradients and iterative optimization

- **Book home:** section 4.3.
- **Notebook:** [019_Chapter_04_03_Gradients_And_Iterative_Optimization.ipynb](notebooks/019_Chapter_04_03_Gradients_And_Iterative_Optimization.ipynb).
- **Data/dependencies:** generated observations, source samples and tasks; no ordinary-run data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** hand-calculated two-feature gradient, finite-difference check, full stochastic and minibatch updates, unbiased with-replacement batch gradients, gradient variance scaling, update versus exposure budgets.
- **Verification:** 6 code cells, 1 inline figures; 2.362 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_04_EXECUTION.md).

<a id="code_020"></a>
### code_020 — Training, inference and reusable learned state

- **Book home:** section 4.4.
- **Notebook:** [020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb](notebooks/020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb).
- **Data/dependencies:** generated observations, source samples and tasks; no ordinary-run data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** training-only fitted preprocessing, frozen prediction state round trip, actual autoencoder reconstruction pretraining, frozen encoder downstream head, episodically pretrained contextual kernel, context changes output without parameter updates.
- **Verification:** 7 code cells, 2 inline figures; 2.504 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_04_EXECUTION.md).

<a id="code_021"></a>
### code_021 — Learning failures and useful diagnostics

- **Book home:** section 4.5.
- **Notebook:** [021_Chapter_04_05_Learning_Failures_And_Diagnostics.ipynb](notebooks/021_Chapter_04_05_Learning_Failures_And_Diagnostics.ipynb).
- **Data/dependencies:** generated observations, source samples and tasks; no ordinary-run data downloads or keys; [pinned environment](requirements-lock.txt).
- **Scope:** flat zero-step loss with nonzero gradients, reported versus true derivative, corrected training and reference optimum, capacity floor versus optimization failure, tiny-data memorization limitation, target availability and objective-role ledger.
- **Verification:** 6 code cells, 2 inline figures; 2.427 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published on main; remote tree and notebook paths verified. Checked 19 October 2026. [Run evidence](CHAPTER_04_EXECUTION.md).

<!-- CHAPTER_05_ENTRIES -->

## Chapter 5: generalization and model assumptions

Five independent synthetic laboratories connect target populations, capacity, preferences, learning curves and stress tests. Use the [traceability guide](CHAPTER_05_GUIDE.md) and [actual execution evidence](CHAPTER_05_EXECUTION.md). These are scoped mechanism experiments, not exhaustive estimator-constructor labs or field-performance benchmarks.

<a id="code_022"></a>
### code_022 — Generalization and the target population

- **Book home:** section 5.1.
- **Notebook:** [022_Chapter_05_01_Generalization_And_The_Target_Population.ipynb](notebooks/022_Chapter_05_01_Generalization_And_The_Target_Population.ipynb).
- **Data/dependencies:** generated observations and numerical checks; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** known-site versus new-site estimands, row and group information boundaries, training-only site state, equal-site versus row averaging, joint support and extrapolation.
- **Verification:** 6 code cells, 2 inline figures; 1.461 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote file tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_05_EXECUTION.md).

<a id="code_023"></a>
### code_023 — Capacity, overfitting and bias–variance

- **Book home:** section 5.2.
- **Notebook:** [023_Chapter_05_02_Capacity_Overfitting_And_Bias_Variance.ipynb](notebooks/023_Chapter_05_02_Capacity_Overfitting_And_Bias_Variance.ipynb).
- **Data/dependencies:** generated observations and numerical checks; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** controlled polynomial capacity curve, development-only degree selection, fresh final assessment, repeated-sample prediction variation, squared-error bias variance identity.
- **Verification:** 5 code cells, 2 inline figures; 1.635 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote file tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_05_EXECUTION.md).

<a id="code_024"></a>
### code_024 — Regularization and inductive bias

- **Book home:** section 5.3.
- **Notebook:** [024_Chapter_05_03_Regularization_And_Inductive_Bias.ipynb](notebooks/024_Chapter_05_03_Regularization_And_Inductive_Bias.ipynb).
- **Data/dependencies:** generated observations and numerical checks; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** same-data line smooth local monotone lenses, ridge shrinkage coordinate dependence, early stopping as a preference, smooth additive versus monotone versus deep predictors, valid augmentation under a declared symmetry.
- **Verification:** 6 code cells, 2 inline figures; 1.879 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote file tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_05_EXECUTION.md).

<a id="code_025"></a>
### code_025 — Learning curves and data value

- **Book home:** section 5.4.
- **Notebook:** [025_Chapter_05_04_Learning_Curves_And_Data_Value.ipynb](notebooks/025_Chapter_05_04_Learning_Curves_And_Data_Value.ipynb).
- **Data/dependencies:** generated observations and numerical checks; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** nested training-size development curve, repeat-sample descriptive variability, readings versus independent sites, subgroup coverage and data value, sealed final fixed-rule assessment.
- **Verification:** 6 code cells, 2 inline figures; 1.505 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote file tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_05_EXECUTION.md).

<a id="code_026"></a>
### code_026 — Assumptions as testable commitments

- **Book home:** section 5.5.
- **Notebook:** [026_Chapter_05_05_Assumptions_As_Testable_Commitments.ipynb](notebooks/026_Chapter_05_05_Assumptions_As_Testable_Commitments.ipynb).
- **Data/dependencies:** generated observations and numerical checks; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** assumption ledger with observable stress tests, linearity and load extrapolation, local support and stationarity failures, exchangeability as a sampling commitment, anisotropic rotation versus coordinate equivariance, physical residual versus empirical validity.
- **Verification:** 6 code cells, 2 inline figures; 1.481 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote file tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_05_EXECUTION.md).

<!-- CHAPTER_06_ENTRIES -->

## Chapter 6: the different ways machines learn

Five independent laboratories separate evidence, objectives, architecture, adaptation and task. Use the [traceability guide](CHAPTER_06_GUIDE.md) and [measured execution evidence](CHAPTER_06_EXECUTION.md). Actual masked pretraining, sparse-label fitting, meta-learning, contextual prediction and action-feedback learning are distinguished from objective-only checks, known-model planning and the illustrative transformer worksheet.

<a id="code_027"></a>
### code_027 — Learning from labelled examples

- **Book home:** section 6.1.
- **Notebook:** [027_Chapter_06_01_Learning_From_Labelled_Examples.ipynb](notebooks/027_Chapter_06_01_Learning_From_Labelled_Examples.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** label and feature availability, regression classification and vector outputs, training-only fitted state, label eligibility and independent assessment, output-specific baselines and metrics.
- **Verification:** 5 code cells, 2 inline figures; 1.726 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_06_EXECUTION.md).

<a id="code_028"></a>
### code_028 — Learning structure without target labels

- **Book home:** section 6.2.
- **Notebook:** [028_Chapter_06_02_Learning_Structure_Without_Target_Labels.ipynb](notebooks/028_Chapter_06_02_Learning_Structure_Without_Target_Labels.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** clustering density and reconstruction are different objectives, training-only standardization, actual nonlinear autoencoder training, external regime versus finding interpretation, density and reconstruction limits.
- **Verification:** 5 code cells, 2 inline figures; 2.019 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_06_EXECUTION.md).

<a id="code_029"></a>
### code_029 — Self-supervision and partial supervision

- **Book home:** section 6.3.
- **Notebook:** [029_Chapter_06_03_Self_Supervision_And_Partial_Supervision.ipynb](notebooks/029_Chapter_06_03_Self_Supervision_And_Partial_Supervision.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** masked historical reconstruction with explicit mask, actual encoder pretraining and sparse-label fine tuning, contrastive positive-pair loss and collapse check, pseudo-label provenance and consistency, independent final assessment without final-input pretraining.
- **Verification:** 7 code cells, 2 inline figures; 1.768 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_06_EXECUTION.md).

<a id="code_030"></a>
### code_030 — Transfer, adaptation and learning across tasks

- **Book home:** section 6.4.
- **Notebook:** [030_Chapter_06_04_Transfer_Adaptation_And_Learning_Across_Tasks.ipynb](notebooks/030_Chapter_06_04_Transfer_Adaptation_And_Learning_Across_Tasks.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** pooled pretraining frozen and updated weights, actual one-step meta-learned initialization, learned fixed context-conditioned predictor, multi-task shared slope and task heads, task-disjoint final assessment and negative-transfer stress.
- **Verification:** 7 code cells, 2 inline figures; 1.651 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_06_EXECUTION.md).

<a id="code_031"></a>
### code_031 — Learning from actions and overlapping categories

- **Book home:** section 6.5.
- **Notebook:** [031_Chapter_06_05_Learning_From_Actions_And_Overlapping_Categories.ipynb](notebooks/031_Chapter_06_05_Learning_From_Actions_And_Overlapping_Categories.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, API keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual contextual bandit exploration and reward fitting, independent frozen-policy simulation assessment, offline action-support diagnostic, known-model Bellman planning versus learning, four-axis taxonomy worksheet without fake transformer training.
- **Verification:** 6 code cells, 2 inline figures; 1.705 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_06_EXECUTION.md).

<!-- CHAPTER_07_ENTRIES -->

## Chapter 7: what makes an experiment trustworthy?

Five independent laboratories make comparison claims and information boundaries inspectable. Use the [traceability guide](CHAPTER_07_GUIDE.md) and [measured execution evidence](CHAPTER_07_EXECUTION.md). All data are generated locally; ideal mechanics, controlled failure checks, exact observational tables and actual fitted mechanisms retain distinct evidential meanings.

<a id="code_032"></a>
### code_032 — Baselines and experimental questions

- **Book home:** section 7.1.
- **Notebook:** [032_Chapter_07_01_Baselines_And_Experimental_Questions.ipynb](notebooks/032_Chapter_07_01_Baselines_And_Experimental_Questions.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** falsifiable improvement claim, constant heuristic mechanistic and simple learned baselines, unit-checked beam calculation, development-only equal-candidate tuning, paired final errors and practical threshold.
- **Verification:** 5 code cells, 2 inline figures; 2.793 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_07_EXECUTION.md).

<a id="code_033"></a>
### code_033 — Leakage and information boundaries

- **Book home:** section 7.2.
- **Notebook:** [033_Chapter_07_02_Leakage_And_Information_Boundaries.ipynb](notebooks/033_Chapter_07_02_Leakage_And_Information_Boundaries.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** target temporal group relational and preprocessing leakage, event time versus arrival time, as-of eligible join and cardinality repair, outcome-derived aggregate sensitivity, clean refit and protected new-building assessment.
- **Verification:** 6 code cells, 2 inline figures; 1.381 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_07_EXECUTION.md).

<a id="code_034"></a>
### code_034 — Reproducibility and provenance

- **Book home:** section 7.3.
- **Notebook:** [034_Chapter_07_03_Reproducibility_And_Provenance.ipynb](notebooks/034_Chapter_07_03_Reproducibility_And_Provenance.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** canonical data snapshot and schema hash, critical training-code and configuration provenance, exact same-environment replay, seed variation versus independent-data replication, rolling one-step forecast information boundary.
- **Verification:** 6 code cells, 2 inline figures; 1.712 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_07_EXECUTION.md).

<a id="code_035"></a>
### code_035 — Fair comparisons and ablation

- **Book home:** section 7.4.
- **Notebook:** [035_Chapter_07_04_Fair_Comparisons_And_Ablation.ipynb](notebooks/035_Chapter_07_04_Fair_Comparisons_And_Ablation.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual one-hop graph and matched relational predictor, equal data features parameter and search access, predeclared repeated initializations, aligned-neighbor ablations, failed-attempt ledger and fixed paired final assessment.
- **Verification:** 6 code cells, 2 inline figures; 2.755 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_07_EXECUTION.md).

<a id="code_036"></a>
### code_036 — Prediction, explanation and causal claims

- **Book home:** section 7.5.
- **Notebook:** [036_Chapter_07_05_Prediction_Explanation_And_Causal_Claims.ipynb](notebooks/036_Chapter_07_05_Prediction_Explanation_And_Causal_Claims.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run downloads, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** observed maintenance association versus intervention, actual predictive model and coefficient interpretation, two observationally identical causal mechanisms, explicit unobserved confounding, randomized simulator check without field identification.
- **Verification:** 6 code cells, 2 inline figures; 2.735 seconds including fresh-kernel lifecycle, CPython 3.14.3 / scikit-learn 1.9.0, macOS ARM64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_07_EXECUTION.md).

<!-- CHAPTER_08_ENTRIES -->

## Chapter 8: constructing the learning dataset

Five independent construction laboratories: [concept guide](CHAPTER_08_GUIDE.md) and [actual execution evidence](CHAPTER_08_EXECUTION.md). Keys, time windows, record eligibility, sampling, label provenance and storage semantics precede model choice. Four laboratories test data contracts; the sampling lab alone fits fixed constant probability predictors and assesses an independent final population.

<a id="code_037"></a>
### code_037 — Units of observation and target design

- **Book home:** section 8.1.
- **Notebook:** [037_Chapter_08_01_Units_And_Targets.ipynb](notebooks/037_Chapter_08_01_Units_And_Targets.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** entity cutoff and horizon form the example key, closed-right target window, censored versus delayed versus resolved outcomes, unknown labels are not negatives, repeated units and overlapping horizons.
- **Verification:** 5 code cells, 2 figures; 2.240 seconds including fresh-kernel lifecycle, CPython 3.14.3 / pandas 3.0.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_08_EXECUTION.md).

<a id="code_038"></a>
### code_038 — Joins, keys and relational structure

- **Book home:** section 8.2.
- **Notebook:** [038_Chapter_08_02_Joins_Keys_And_Relations.ipynb](notebooks/038_Chapter_08_02_Joins_Keys_And_Relations.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** primary foreign and composite keys, join multiplicity and duplicate amplification, aggregation at the declared learning unit, missing-related-record preservation, flattened views retain source lineage.
- **Verification:** 5 code cells, 2 figures; 1.256 seconds including fresh-kernel lifecycle, CPython 3.14.3 / pandas 3.0.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_08_EXECUTION.md).

<a id="code_039"></a>
### code_039 — Time-aware information availability

- **Book home:** section 8.3.
- **Notebook:** [039_Chapter_08_03_Time_Aware_Availability.ipynb](notebooks/039_Chapter_08_03_Time_Aware_Availability.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** event arrival and prediction clocks, revision-aware historical snapshots, backward as-of matching after eligibility filtering, staleness and missing-history contracts, future revision invariance.
- **Verification:** 5 code cells, 2 figures; 2.255 seconds including fresh-kernel lifecycle, CPython 3.14.3 / pandas 3.0.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_08_EXECUTION.md).

<a id="code_040"></a>
### code_040 — Sampling, labels and dataset documentation

- **Book home:** section 8.4.
- **Notebook:** [040_Chapter_08_04_Sampling_Labels_And_Documentation.ipynb](notebooks/040_Chapter_08_04_Sampling_Labels_And_Documentation.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** sampling frame and inspection selection, known-probability weighting with support, weak labels abstention and annotator disagreement, dataset card with provenance, fixed constant predictors and protected final population.
- **Verification:** 5 code cells, 2 figures; 2.224 seconds including fresh-kernel lifecycle, CPython 3.14.3 / pandas 3.0.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_08_EXECUTION.md).

<a id="code_041"></a>
### code_041 — Representations and storage contracts

- **Book home:** section 8.5.
- **Notebook:** [041_Chapter_08_05_Representations_And_Storage.ipynb](notebooks/041_Chapter_08_05_Representations_And_Storage.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, keys or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** linked tables wide views sequences and graph edge lists, node ID order and permutation consistency, missingness masks versus physical zero, mesh connectivity changes interpolation, versioned schema units and safe numeric round trips.
- **Verification:** 6 code cells, 2 figures; 3.415 seconds including fresh-kernel lifecycle, CPython 3.14.3 / pandas 3.0.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_08_EXECUTION.md).

<!-- CHAPTER_09_ENTRIES -->

## Chapter 9: exploring and understanding data

Use the [concept guide](CHAPTER_09_GUIDE.md) and [execution evidence](CHAPTER_09_EXECUTION.md). Exploratory distributions, associations, subgroup intervals and dependence checks are distinct from the final hypothesis laboratory's frozen predictive assessment. All evidence is synthetic.

<a id="code_042"></a>
### code_042 — Distributions, scale and support

- **Book home:** section 9.1.
- **Notebook:** [042_Chapter_09_01_Distributions_Scale_And_Support.ipynb](notebooks/042_Chapter_09_01_Distributions_Scale_And_Support.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** physical and observed support, common bins and subgroup distributions, zeros tails and unit-error review, empirical CDF without bin choices, category absence and logarithm domain.
- **Verification:** 5 code cells, 2 figures; 1.357 seconds including fresh-kernel lifecycle, CPython 3.14.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_09_EXECUTION.md).

<a id="code_043"></a>
### code_043 — Dependencies and confounding patterns

- **Book home:** section 9.2.
- **Notebook:** [043_Chapter_09_02_Dependencies_And_Confounding.ipynb](notebooks/043_Chapter_09_02_Dependencies_And_Confounding.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** pooled versus material-conditional associations, covariance decomposition with group context, nonlinear dependence with near-zero linear correlation, rank correlation and redundant features, association is not intervention.
- **Verification:** 5 code cells, 2 figures; 1.288 seconds including fresh-kernel lifecycle, CPython 3.14.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_09_EXECUTION.md).

<a id="code_044"></a>
### code_044 — Subgroups, rare cases and coverage

- **Book home:** section 9.3.
- **Notebook:** [044_Chapter_09_03_Subgroups_Rare_Cases_And_Coverage.ipynb](notebooks/044_Chapter_09_03_Subgroups_Rare_Cases_And_Coverage.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** counts and prevalence by operational group, rare-group zero-event uncertainty, Wilson interval assumptions and limits, row counts versus independent structures, unobserved schema categories.
- **Verification:** 5 code cells, 2 figures; 1.261 seconds including fresh-kernel lifecycle, CPython 3.14.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_09_EXECUTION.md).

<a id="code_045"></a>
### code_045 — Temporal, spatial and relational patterns

- **Book home:** section 9.4.
- **Notebook:** [045_Chapter_09_04_Temporal_Spatial_And_Relational_Patterns.ipynb](notebooks/045_Chapter_09_04_Temporal_Spatial_And_Relational_Patterns.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** autocorrelation and seasonal structure, nearby sensor dependence, connected components and split units, cluster dependence changes mean variance, effective sample size is estimand-specific.
- **Verification:** 5 code cells, 2 figures; 1.490 seconds including fresh-kernel lifecycle, CPython 3.14.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_09_EXECUTION.md).

<a id="code_046"></a>
### code_046 — Exploration as a recorded hypothesis process

- **Book home:** section 9.5.
- **Notebook:** [046_Chapter_09_05_Recorded_Hypotheses_And_Confirmation.ipynb](notebooks/046_Chapter_09_05_Recorded_Hypotheses_And_Confirmation.ipynb).
- **Data/dependencies:** locally generated; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** exploration ledger and alternative explanations, temperature-load interaction discovered on development, training-only fit and group-disjoint roles, frozen candidate selection and one final assessment, paired building uncertainty and limits.
- **Verification:** 5 code cells, 2 figures; 1.445 seconds including fresh-kernel lifecycle, CPython 3.14.3, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verified. Checked 19 October 2026. [Run evidence](CHAPTER_09_EXECUTION.md).

<!-- CHAPTER_10_ENTRIES -->

## Chapter 10: Cleaning imperfect data

Use the [concept guide](CHAPTER_10_GUIDE.md) and [actual execution evidence](CHAPTER_10_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_047"></a>
### code_047 — Missingness and observation processes

- **Book home:** section 10.1.
- **Notebook:** [047_Chapter_10_01_Missingness_And_Observation_Processes.ipynb](notebooks/047_Chapter_10_01_Missingness_And_Observation_Processes.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** absent censored structural and failed measurements, MCAR MAR and MNAR as generator assumptions, training-only imputation and missingness indicators, development-only policy selection, protected final comparison without identifying missingness from data.
- **Verification:** 6 code cells, 2 figures; 1.347 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_10_EXECUTION.md).

<a id="code_048"></a>
### code_048 — Duplicates, identities and inconsistent records

- **Book home:** section 10.2.
- **Notebook:** [048_Chapter_10_02_Duplicates_Identities_And_Updates.ipynb](notebooks/048_Chapter_10_02_Duplicates_Identities_And_Updates.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** reimported records versus legitimate repeat events, composite entity identity, version conflicts and known-at-cutoff resolution, provenance retention during deduplication, duplicate event leakage across role assignments.
- **Verification:** 5 code cells, 2 figures; 1.257 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_10_EXECUTION.md).

<a id="code_049"></a>
### code_049 — Measurement units, timestamps and validity

- **Book home:** section 10.3.
- **Notebook:** [049_Chapter_10_03_Units_Timestamps_And_Validity.ipynb](notebooks/049_Chapter_10_03_Units_Timestamps_And_Validity.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** quantity-aware unit conversion, offset-aware timestamp ordering and repeated local clocks, event-arrival validity checks, independent reference calibration, schema checks precede statistical scaling.
- **Verification:** 5 code cells, 2 figures; 1.285 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_10_EXECUTION.md).

<a id="code_050"></a>
### code_050 — Noisy and uncertain labels

- **Book home:** section 10.4.
- **Notebook:** [050_Chapter_10_04_Noisy_And_Uncertain_Labels.ipynb](notebooks/050_Chapter_10_04_Noisy_And_Uncertain_Labels.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** continuous severity and threshold ambiguity, annotator disagreement and exclusion, explicit measurement-model soft targets, training-only adjudication and extra evidence budget, fixed logistic objectives and independent reference assessment.
- **Verification:** 6 code cells, 2 figures; 1.326 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_10_EXECUTION.md).

<a id="code_051"></a>
### code_051 — Outliers, corruption and rare events

- **Book home:** section 10.5.
- **Notebook:** [051_Chapter_10_05_Outliers_Corruption_And_Rare_Events.ipynb](notebooks/051_Chapter_10_05_Outliers_Corruption_And_Rare_Events.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** provenance-led investigation of extreme strain, known loading event versus isolated source-unit fault, blind outlier deletion erases valid rare cases, fixed-threshold Huber response robustness, verified repair and independent final assessment.
- **Verification:** 5 code cells, 2 figures; 1.442 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_10_EXECUTION.md).

<!-- CHAPTER_11_ENTRIES -->

## Chapter 11: Choosing preprocessing steps

Use the [concept guide](CHAPTER_11_GUIDE.md) and [actual execution evidence](CHAPTER_11_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_052"></a>
### code_052 — Preprocessing as a learned pipeline

- **Book home:** section 11.1.
- **Notebook:** [052_Chapter_11_01_Fold_Fitting_And_Stored_State.ipynb](notebooks/052_Chapter_11_01_Fold_Fitting_And_Stored_State.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** deterministic validation versus learned transforms, fold-only imputation and scaling, paired leakage audit, stored state and batch-invariant inference.
- **Verification:** 5 code cells, 2 figures; 1.487 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_11_EXECUTION.md).

<a id="code_053"></a>
### code_053 — Scaling and numerical conditioning

- **Book home:** section 11.2.
- **Notebook:** [053_Chapter_11_02_Scaling_Distance_And_Penalties.ipynb](notebooks/053_Chapter_11_02_Scaling_Distance_And_Penalties.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** unit conversion versus learned scaling, distance and ridge penalty geometry, standard robust and row normalization, model-dependent sensitivity and conditioning.
- **Verification:** 4 code cells, 2 figures; 1.678 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_11_EXECUTION.md).

<a id="code_054"></a>
### code_054 — Encoding categories and unknown values

- **Book home:** section 11.3.
- **Notebook:** [054_Chapter_11_03_Categories_And_Cross_Fitted_Targets.ipynb](notebooks/054_Chapter_11_03_Categories_And_Cross_Fitted_Targets.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** one-hot unknown handling and ordinal assumptions, group-aware target cross-fitting, high-cardinality identifiers and leakage, encoding compatibility and learned embeddings.
- **Verification:** 5 code cells, 2 figures; 1.317 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_11_EXECUTION.md).

<a id="code_055"></a>
### code_055 — Imputation and internal missing-value handling

- **Book home:** section 11.4.
- **Notebook:** [055_Chapter_11_04_Imputation_And_Native_Routes.ipynb](notebooks/055_Chapter_11_04_Imputation_And_Native_Routes.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** simple and conditional imputation, posterior-draw predictive averaging, native tree missing-value routes, same-cohort missingness-shift assessment.
- **Verification:** 4 code cells, 2 figures; 1.574 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_11_EXECUTION.md).

<a id="code_056"></a>
### code_056 — Transformations and model input contracts

- **Book home:** section 11.5.
- **Notebook:** [056_Chapter_11_05_Target_Transforms_And_Input_Contracts.ipynb](notebooks/056_Chapter_11_05_Target_Transforms_And_Input_Contracts.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** log-target estimands and inverse-transform bias, training-residual smearing and original-unit scoring, clipping and power-transform state, release-pinned documentary input contract.
- **Verification:** 5 code cells, 2 figures; 1.460 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_11_EXECUTION.md).

<!-- CHAPTER_12_ENTRIES -->

## Chapter 12: Engineering and selecting features

Use the [concept guide](CHAPTER_12_GUIDE.md) and [actual execution evidence](CHAPTER_12_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_057"></a>
### code_057 — Domain features and interactions

- **Book home:** section 12.1.
- **Notebook:** [057_Chapter_12_01_Physical_Features_And_Sample_Efficiency.ipynb](notebooks/057_Chapter_12_01_Physical_Features_And_Sample_Efficiency.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** beam-inspired feature and domain assumptions, dimensionless group and unit invariance, interaction basis versus raw main effects, predeclared learning-size comparisons.
- **Verification:** 4 code cells, 2 figures; 1.662 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_12_EXECUTION.md).

<a id="code_058"></a>
### code_058 — Aggregates and history summaries

- **Book home:** section 12.2.
- **Notebook:** [058_Chapter_12_02_Cutoff_Safe_History_And_Relations.ipynb](notebooks/058_Chapter_12_02_Cutoff_Safe_History_And_Relations.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** event and arrival clocks in trailing windows, RMS and spectral energy summaries, prior inspection counts and recency, relational aggregates and future-append invariance.
- **Verification:** 4 code cells, 2 figures; 1.440 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_12_EXECUTION.md).

<a id="code_059"></a>
### code_059 — Feature selection and stability

- **Book home:** section 12.3.
- **Notebook:** [059_Chapter_12_03_Correlated_Channels_And_Selection.ipynb](notebooks/059_Chapter_12_03_Correlated_Channels_And_Selection.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** filter wrapper and embedded selectors, selection inside validation pipelines, correlated proxies and resample variation, frequency diagnostics without error-control claims.
- **Verification:** 5 code cells, 2 figures; 1.701 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_12_EXECUTION.md).

<a id="code_060"></a>
### code_060 — Compact representations and learned features

- **Book home:** section 12.4.
- **Notebook:** [060_Chapter_12_04_Spectra_PCA_And_Autoencoder.ipynb](notebooks/060_Chapter_12_04_Spectra_PCA_And_Autoencoder.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** hand-built spectral and low-rank features, self-contained nonlinear autoencoder, training-only representation fitting, reconstruction versus downstream performance.
- **Verification:** 5 code cells, 2 figures; 1.668 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_12_EXECUTION.md).

<a id="code_061"></a>
### code_061 — Leakage, cost and feature availability

- **Book home:** section 12.5.
- **Notebook:** [061_Chapter_12_05_Operational_Feature_Packages.ipynb](notebooks/061_Chapter_12_05_Operational_Feature_Packages.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** feature acquisition cost and latency, future target proxies and apparent error, development-only package choice, train-serving column contract.
- **Verification:** 4 code cells, 2 figures; 1.438 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_12_EXECUTION.md).

<!-- CHAPTER_13_ENTRIES -->

## Chapter 13: Preparing graphs, sequences, and physical systems

Use the [concept guide](CHAPTER_13_GUIDE.md) and [actual execution evidence](CHAPTER_13_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_062"></a>
### code_062 — Graph construction and relational meaning

- **Book home:** section 13.1.
- **Notebook:** [062_Chapter_13_01_Typed_Graphs_And_Construction_Boundaries.ipynb](notebooks/062_Chapter_13_01_Typed_Graphs_And_Construction_Boundaries.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** physical member and sensor node types, directed typed relations and self-loops, training-only correlation graph, stable identifiers and permutation equivariance.
- **Verification:** 4 code cells, 2 figures; 1.315 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_13_EXECUTION.md).

<a id="code_063"></a>
### code_063 — Sequence windows and irregular observations

- **Book home:** section 13.2.
- **Notebook:** [063_Chapter_13_02_Irregular_Windows_And_Overlap.ipynb](notebooks/063_Chapter_13_02_Irregular_Windows_And_Overlap.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** context forecast stride and raw-record overlap, event and arrival aligned windows, bounded forward hold and masks, future-invariant construction and label maturity.
- **Verification:** 4 code cells, 2 figures; 1.366 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_13_EXECUTION.md).

<a id="code_064"></a>
### code_064 — Spatial coordinates, geometry and meshes

- **Book home:** section 13.3.
- **Notebook:** [064_Chapter_13_03_Mesh_Fields_And_Boundary_Tags.ipynb](notebooks/064_Chapter_13_03_Mesh_Fields_And_Boundary_Tags.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** points cells edges and material fields, boundary tags and scalar vector units, consistent mesh renumbering, coordinate frames and field transformations.
- **Verification:** 4 code cells, 2 figures; 1.396 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_13_EXECUTION.md).

<a id="code_065"></a>
### code_065 — Physical constraints and conditions

- **Book home:** section 13.4.
- **Notebook:** [065_Chapter_13_04_Forward_Conditions_And_Inverse_Ambiguity.ipynb](notebooks/065_Chapter_13_04_Forward_Conditions_And_Inverse_Ambiguity.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** constitutive assumptions and conservation balance, supports boundary loads and initial-state schema, forward input completeness, inverse load-stiffness non-identifiability.
- **Verification:** 4 code cells, 2 figures; 1.350 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_13_EXECUTION.md).

<a id="code_066"></a>
### code_066 — Batching and structure-preserving transformations

- **Book home:** section 13.5.
- **Notebook:** [066_Chapter_13_05_Disconnected_Batches_And_Equivariance.ipynb](notebooks/066_Chapter_13_05_Disconnected_Batches_And_Equivariance.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** disconnected graph batching and offsets, mask-safe sequence aggregation, neighbor-sampling variability, covariant geometry loads stiffness and targets.
- **Verification:** 5 code cells, 2 figures; 1.370 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote tree verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_13_EXECUTION.md).

<!-- CHAPTER_14_ENTRIES -->

## Chapter 14: Validation under real-world conditions

Use the [concept guide](CHAPTER_14_GUIDE.md) and [actual execution evidence](CHAPTER_14_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_067"></a>
### code_067 — Random, grouped and nested validation

- **Book home:** section 14.1.
- **Notebook:** [067_Chapter_14_01_Nested_Building_Validation.ipynb](notebooks/067_Chapter_14_01_Nested_Building_Validation.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** exchangeability and repeated member measurements, row versus building split, nested grouped model selection, locked new-building assessment.
- **Verification:** 4 code cells, 2 figures; 1.661 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_14_EXECUTION.md).

<a id="code_068"></a>
### code_068 — Temporal backtesting and delayed labels

- **Book home:** section 14.2.
- **Notebook:** [068_Chapter_14_02_Backtesting_Label_Arrival.ipynb](notebooks/068_Chapter_14_02_Backtesting_Label_Arrival.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** expanding and rolling origins, one-day and seven-day horizons, label-arrival admission, overlap versus availability and independence.
- **Verification:** 4 code cells, 2 figures; 1.477 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_14_EXECUTION.md).

<a id="code_069"></a>
### code_069 — Spatial and graph-aware evaluation

- **Book home:** section 14.3.
- **Notebook:** [069_Chapter_14_03_Spatial_And_Graph_Protocols.ipynb](notebooks/069_Chapter_14_03_Spatial_And_Graph_Protocols.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** random interpolation versus held spatial region, unseen nodes in known graphs, unseen graphs with request-time features, label-free neighborhood construction.
- **Verification:** 4 code cells, 2 figures; 1.536 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_14_EXECUTION.md).

<a id="code_070"></a>
### code_070 — Limited labels, imbalance and rare events

- **Book home:** section 14.4.
- **Notebook:** [070_Chapter_14_04_Rare_Events_Within_Buildings.ipynb](notebooks/070_Chapter_14_04_Rare_Events_Within_Buildings.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** grouped stratification limits, training-only weights and oversampling, undefined rare-event metrics, whole-building bootstrap with missing-positive draws.
- **Verification:** 4 code cells, 2 figures; 1.536 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_14_EXECUTION.md).

<a id="code_071"></a>
### code_071 — Shift, stress tests and external evidence

- **Book home:** section 14.5.
- **Notebook:** [071_Chapter_14_05_Performance_Envelope_Under_Shift.ipynb](notebooks/071_Chapter_14_05_Performance_Envelope_Under_Shift.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** source-only procedure selection, separate site material and support shifts, frozen sensor-bias stress tests, synthetic challenge versus external field evidence.
- **Verification:** 4 code cells, 2 figures; 1.616 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 19 October 2026. [Run evidence](CHAPTER_14_EXECUTION.md).

<!-- CHAPTER_15_ENTRIES -->

## Chapter 15: Linear, additive, and interpretable models

Use the [concept guide](CHAPTER_15_GUIDE.md) and [actual execution evidence](CHAPTER_15_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_072"></a>
### code_072 — Linear regression and robust alternatives

- **Book home:** section 15.1.
- **Notebook:** [072_Chapter_15_01_Losses_Residuals_And_Quantiles.ipynb](notebooks/072_Chapter_15_01_Losses_Residuals_And_Quantiles.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** least squares geometry and rank deficiency, contaminated training responses, median and conditional quantile targets, fitting versus inference assumptions.
- **Verification:** 4 code cells, 2 figures; 1.545 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_15_EXECUTION.md).

<a id="code_073"></a>
### code_073 — Generalized linear models

- **Book home:** section 15.2.
- **Notebook:** [073_Chapter_15_02_Bernoulli_Counts_And_Exposure.ipynb](notebooks/073_Chapter_15_02_Bernoulli_Counts_And_Exposure.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** Bernoulli logit versus count log-mean, exposure offset and weighted rates, Poisson mean versus overdispersion, count means are not event probabilities.
- **Verification:** 4 code cells, 2 figures; 1.462 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_15_EXECUTION.md).

<a id="code_074"></a>
### code_074 — Regularization and high-dimensional fitting

- **Book home:** section 15.3.
- **Notebook:** [074_Chapter_15_03_Correlated_Sensors_And_Shrinkage.ipynb](notebooks/074_Chapter_15_03_Correlated_Sensors_And_Shrinkage.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** Ridge Lasso ElasticNet common penalty convention, training-only standardization and development selection, correlated sensor coefficient paths, bootstrap coefficient and prediction stability.
- **Verification:** 4 code cells, 2 figures; 1.996 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_15_EXECUTION.md).

<a id="code_075"></a>
### code_075 — Additive, spline and shape-constrained models

- **Book home:** section 15.4.
- **Notebook:** [075_Chapter_15_04_Additive_Risk_And_Monotone_Load.ipynb](notebooks/075_Chapter_15_04_Additive_Risk_And_Monotone_Load.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** linear versus additive response on a fixed cohort, training-fitted spline basis and penalty selection, nonnegative monotone load increments, independent isotonic calibration and limits.
- **Verification:** 4 code cells, 2 figures; 1.551 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_15_EXECUTION.md).

<a id="code_076"></a>
### code_076 — Rules, sparse scores and symbolic models

- **Book home:** section 15.5.
- **Notebook:** [076_Chapter_15_05_Compact_Rules_And_Dimensional_Search.ipynb](notebooks/076_Chapter_15_05_Compact_Rules_And_Dimensional_Search.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** finite symbolic dictionary with dimensional guards, development complexity selection and locked assessment, decision list sparse score and rule ensemble, compactness fidelity and expression limits.
- **Verification:** 4 code cells, 2 figures; 1.488 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_15_EXECUTION.md).

<!-- CHAPTER_16_ENTRIES -->

## Chapter 16: Probabilistic and Bayesian models

Use the [concept guide](CHAPTER_16_GUIDE.md) and [actual execution evidence](CHAPTER_16_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_077"></a>
### code_077 — Naive Bayes and generative classification

- **Book home:** section 16.1.
- **Notebook:** [077_Chapter_16_01_Alarm_Dependence_And_Naive_Bayes.ipynb](notebooks/077_Chapter_16_01_Alarm_Dependence_And_Naive_Bayes.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** Bernoulli class prior and likelihood score, Laplace smoothing and absent indicators, duplicate conditional dependence, classification versus probability calibration.
- **Verification:** 4 code cells, 2 figures; 1.322 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_16_EXECUTION.md).

<a id="code_078"></a>
### code_078 — Bayesian estimation and hierarchical models

- **Book home:** section 16.2.
- **Notebook:** [078_Chapter_16_02_Hierarchical_Building_Rates.ipynb](notebooks/078_Chapter_16_02_Hierarchical_Building_Rates.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** prior likelihood posterior and prediction, full hyperparameter grid integration, unequal group partial pooling, prior predictive versus future evidence.
- **Verification:** 4 code cells, 2 figures; 1.489 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_16_EXECUTION.md).

<a id="code_079"></a>
### code_079 — Posterior computation and model checking

- **Book home:** section 16.3.
- **Notebook:** [079_Chapter_16_03_Grid_MCMC_Variational_And_Checks.ipynb](notebooks/079_Chapter_16_03_Grid_MCMC_Variational_And_Checks.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** conjugate conditional and joint grid reference, transformed random-walk MCMC with Jacobian, classical split Rhat and simple ESS, mean-field grid approximation and predictive criticism.
- **Verification:** 4 code cells, 2 figures; 1.987 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_16_EXECUTION.md).

<a id="code_080"></a>
### code_080 — Gaussian processes and scalable approximations

- **Book home:** section 16.4.
- **Notebook:** [080_Chapter_16_04_Temperature_GP_And_Low_Rank_Prior.ipynb](notebooks/080_Chapter_16_04_Temperature_GP_And_Low_Rank_Prior.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** fixed covariance and Gaussian conditioning, latent versus observation intervals, away-from-support conditional uncertainty, low-rank prior approximation and variance loss.
- **Verification:** 4 code cells, 2 figures; 1.867 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_16_EXECUTION.md).

<a id="code_081"></a>
### code_081 — Graphical models and latent states

- **Book home:** section 16.5.
- **Notebook:** [081_Chapter_16_05_Regime_HMM_And_Probability_Graphs.ipynb](notebooks/081_Chapter_16_05_Regime_HMM_And_Probability_Graphs.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** directed probability factorization and latent regimes, forward filtering versus offline smoothing and Viterbi, exact enumeration and undirected conditional independence, continuous Gaussian state-space filtering.
- **Verification:** 4 code cells, 2 figures; 1.304 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verification passed. Checked 20 October 2026. [Run evidence](CHAPTER_16_EXECUTION.md).

<!-- CHAPTER_17_ENTRIES -->

## Chapter 17: Similarity, kernels, and margins

Use the [concept guide](CHAPTER_17_GUIDE.md) and [actual execution evidence](CHAPTER_17_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_082"></a>
### code_082 — Distances, metrics and meaningful neighbourhoods

- **Book home:** section 17.1.
- **Notebook:** [082_Chapter_17_01_Units_Missingness_And_Metric_Geometry.ipynb](notebooks/082_Chapter_17_01_Units_Missingness_And_Metric_Geometry.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** raw units versus dimensionless reference scales, unit-consistent Mahalanobis covariance, categorical and missing shared features, distance eligibility and neighborhood geometry.
- **Verification:** 4 code cells, 2 figures; 1.523 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_17_EXECUTION.md).

<a id="code_083"></a>
### code_083 — Nearest-neighbour prediction and retrieval

- **Book home:** section 17.2.
- **Notebook:** [083_Chapter_17_02_Neighbor_Support_And_Search.ipynb](notebooks/083_Chapter_17_02_Neighbor_Support_And_Search.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** development neighborhood and weighting selection, inside versus unusual query support, exact tree versus brute retrieval, candidate-subset approximation and zero-distance behavior.
- **Verification:** 4 code cells, 2 figures; 1.619 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_17_EXECUTION.md).

<a id="code_084"></a>
### code_084 — Kernels and implicit feature spaces

- **Book home:** section 17.3.
- **Notebook:** [084_Chapter_17_03_Kernel_Assumptions_And_Seasonality.ipynb](notebooks/084_Chapter_17_03_Kernel_Assumptions_And_Seasonality.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** positive-semidefinite Gram matrices, explicit polynomial feature identity, common-objective kernel ridge, linear radial and periodic assumptions.
- **Verification:** 4 code cells, 2 figures; 1.514 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_17_EXECUTION.md).

<a id="code_085"></a>
### code_085 — Support vector machines and margins

- **Book home:** section 17.4.
- **Notebook:** [085_Chapter_17_04_Margins_Calibration_And_Regression_Tubes.ipynb](notebooks/085_Chapter_17_04_Margins_Calibration_And_Regression_Tubes.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** soft margins and balanced penalties, kernel boundary versus schematic feature map, independent score calibration, epsilon-insensitive regression.
- **Verification:** 4 code cells, 2 figures; 1.659 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_17_EXECUTION.md).

<a id="code_086"></a>
### code_086 — Scalability and learned similarity

- **Book home:** section 17.5.
- **Notebook:** [086_Chapter_17_05_Learned_Retrieval_And_Kernel_Approximations.ipynb](notebooks/086_Chapter_17_05_Learned_Retrieval_And_Kernel_Approximations.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** linear supervised NCA and tuned neighbors, fold-contained label-valued retrieval context, candidate-budget recall and array memory, random Fourier and Nystroem Gram approximations.
- **Verification:** 4 code cells, 2 figures; 1.761 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_17_EXECUTION.md).

<!-- CHAPTER_18_ENTRIES -->

## Chapter 18: Trees and ensemble learning

Use the [concept guide](CHAPTER_18_GUIDE.md) and [actual execution evidence](CHAPTER_18_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_087"></a>
### code_087 — Decision trees and recursive partitioning

- **Book home:** section 18.1.
- **Notebook:** [087_Chapter_18_01_Paths_Routes_And_Instability.ipynb](notebooks/087_Chapter_18_01_Paths_Routes_And_Instability.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** weighted impurity and actual decision paths, small label perturbation and root instability, missing routes versus unknown categories, linked original tree-control laboratory.
- **Verification:** 4 code cells, 2 figures; 2.226 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_18_EXECUTION.md).

<a id="code_088"></a>
### code_088 — Bagging, random forests and extra trees

- **Book home:** section 18.2.
- **Notebook:** [088_Chapter_18_02_Aggregation_Diversity_And_OOB_Limits.ipynb](notebooks/088_Chapter_18_02_Aggregation_Diversity_And_OOB_Limits.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** bootstrap and randomized threshold ensembles, prediction instability and covariance, out-of-bag rows versus new entities, correlated measurements and fixed held-out comparison.
- **Verification:** 4 code cells, 2 figures; 2.317 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_18_EXECUTION.md).

<a id="code_089"></a>
### code_089 — Boosting and additive correction

- **Book home:** section 18.3.
- **Notebook:** [089_Chapter_18_03_Residual_Steps_And_Reweighting.ipynb](notebooks/089_Chapter_18_03_Residual_Steps_And_Reweighting.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** manual squared-error residual correction, loss gradients versus ordinary residuals, AdaBoost weight updates, development-selected stage count.
- **Verification:** 4 code cells, 2 figures; 1.871 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_18_EXECUTION.md).

<a id="code_090"></a>
### code_090 — Modern boosted-tree implementations

- **Book home:** section 18.4.
- **Notebook:** [090_Chapter_18_04_Native_Boosters_Identical_Group_Protocol.ipynb](notebooks/090_Chapter_18_04_Native_Boosters_Identical_Group_Protocol.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual XGBoost LightGBM and CatBoost execution, common group splits and equal candidate count, native categorical and numeric missing contracts, growth and leaf-count resource boundaries.
- **Verification:** 4 code cells, 2 figures; 2.007 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_18_EXECUTION.md).

<a id="code_091"></a>
### code_091 — Stacking, blending and hybrid ensembles

- **Book home:** section 18.5.
- **Notebook:** [091_Chapter_18_05_OOF_Tree_Linear_Neural_Stack.ipynb](notebooks/091_Chapter_18_05_OOF_Tree_Linear_Neural_Stack.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** entire-pipeline out-of-fold base predictions, boosted tree ridge and trained neural base learners, honest holdout blending versus full-memory deployment, soft-routing candidate as a scoped mechanism.
- **Verification:** 4 code cells, 2 figures; 1.859 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_18_EXECUTION.md).

<a id="code_092"></a>
### code_092 — Constraints, distributions and practical tradeoffs

- **Book home:** section 18.6.
- **Notebook:** [092_Chapter_18_06_Monotone_Quantiles_And_Cost_Audit.ipynb](notebooks/092_Chapter_18_06_Monotone_Quantiles_And_Cost_Audit.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** monotonic and additive interaction constraints, separate mean and quantile loss targets, coverage crossings and support challenges, version-specific tree-array resource ledger.
- **Verification:** 4 code cells, 2 figures; 1.819 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_18_EXECUTION.md).

<!-- CHAPTER_19_ENTRIES -->

## Chapter 19: Clustering and anomaly detection

Use the [concept guide](CHAPTER_19_GUIDE.md) and [actual execution evidence](CHAPTER_19_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_093"></a>
### code_093 — Centroid and mixture-based clustering

- **Book home:** section 19.1.
- **Notebook:** [093_Chapter_19_01_Centroids_Medoids_And_Mixture_Responsibilities.ipynb](notebooks/093_Chapter_19_01_Centroids_Medoids_And_Mixture_Responsibilities.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** Euclidean centroid versus observed-case medoid objectives, full versus spherical mixture assumptions, unit scaling and initialization sensitivity, model responsibilities versus external regime evidence.
- **Verification:** 4 code cells, 2 figures; 1.773 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_19_EXECUTION.md).

<a id="code_094"></a>
### code_094 — Hierarchical, density and graph clustering

- **Book home:** section 19.2.
- **Notebook:** [094_Chapter_19_02_Shapes_Densities_And_Connectivity.ipynb](notebooks/094_Chapter_19_02_Shapes_Densities_And_Connectivity.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** same-point centroid hierarchy density and spectral partitions, native HDBSCAN density hierarchy, noise labels and scale controls, boundary sensitivity without comparing arbitrary label IDs.
- **Verification:** 4 code cells, 2 figures; 1.660 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_19_EXECUTION.md).

<a id="code_095"></a>
### code_095 — Evaluating discovered groups

- **Book home:** section 19.3.
- **Notebook:** [095_Chapter_19_03_Stability_Separation_And_Downstream_Utility.ipynb](notebooks/095_Chapter_19_03_Stability_Separation_And_Downstream_Utility.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** internal separation versus external agreement, training-only clustering in downstream prediction, sensor resampling and permutation-invariant stability, development selection without final interpretation tuning.
- **Verification:** 4 code cells, 2 figures; 1.860 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_19_EXECUTION.md).

<a id="code_096"></a>
### code_096 — Point anomalies, novelty and density scores

- **Book home:** section 19.4.
- **Notebook:** [096_Chapter_19_04_Reference_Scores_And_Valid_Rarity.ipynb](notebooks/096_Chapter_19_04_Reference_Scores_And_Valid_Rarity.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** marginal versus joint unusualness, robust covariance isolation local density and one-class boundaries, LOF novelty-only scoring contract, calibration thresholds versus rare valid observations.
- **Verification:** 4 code cells, 2 figures; 1.765 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_19_EXECUTION.md).

<a id="code_097"></a>
### code_097 — Contextual and structured anomalies

- **Book home:** section 19.5.
- **Notebook:** [097_Chapter_19_05_Graph_Context_Sequence_And_Alarm_Burden.ipynb](notebooks/097_Chapter_19_05_Graph_Context_Sequence_And_Alarm_Burden.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** contemporaneous graph residual versus common-mode extremes, training-only PCA reconstruction and reference contamination, calibration thresholds sequential delay and alarm burden, selective review with unreviewed cases kept unknown.
- **Verification:** 4 code cells, 2 figures; 1.667 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_19_EXECUTION.md).

<!-- CHAPTER_20_ENTRIES -->

## Chapter 20: Representation learning and dimensionality reduction

Use the [concept guide](CHAPTER_20_GUIDE.md) and [actual execution evidence](CHAPTER_20_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_098"></a>
### code_098 — Linear factorization and latent components

- **Book home:** section 20.1.
- **Notebook:** [098_Chapter_20_01_factorization_and_lost_signal.ipynb](notebooks/098_Chapter_20_01_factorization_and_lost_signal.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** centered PCA/SVD identity, nonnegative factorization, independent components, small-signal attenuation.
- **Verification:** 4 code cells, 2 figures; 1.561 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_20_EXECUTION.md).

<a id="code_099"></a>
### code_099 — Manifolds and nonlinear visualization

- **Book home:** section 20.2.
- **Notebook:** [099_Chapter_20_02_manifold_displays.ipynb](notebooks/099_Chapter_20_02_manifold_displays.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual t-SNE and UMAP, neighborhood diagnostics, transductive visualization, new-query transforms.
- **Verification:** 4 code cells, 2 figures; 8.489 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_20_EXECUTION.md).

<a id="code_100"></a>
### code_100 — Embeddings for entities and relationships

- **Book home:** section 20.3.
- **Notebook:** [100_Chapter_20_03_entity_and_graph_embeddings.ipynb](notebooks/100_Chapter_20_03_entity_and_graph_embeddings.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** masked matrix factorization, whole-entity holdout, inductive descriptor mapping, transductive graph coordinates.
- **Verification:** 4 code cells, 2 figures; 1.435 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_20_EXECUTION.md).

<a id="code_101"></a>
### code_101 — Autoencoders and reconstruction learning

- **Book home:** section 20.4.
- **Notebook:** [101_Chapter_20_04_autoencoders_and_reconstruction.ipynb](notebooks/101_Chapter_20_04_autoencoders_and_reconstruction.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual CPU autoencoder training, denoising measurement targets, bottleneck versus identity, analytic Gaussian KL connection.
- **Verification:** 4 code cells, 2 figures; 2.773 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_20_EXECUTION.md).

<a id="code_102"></a>
### code_102 — Evaluating and transferring representations

- **Book home:** section 20.5.
- **Notebook:** [102_Chapter_20_05_representation_transfer.ipynb](notebooks/102_Chapter_20_05_representation_transfer.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** whole-building representation assessment, frozen linear probes, actual encoder fine-tuning, invariance can remove task information.
- **Verification:** 4 code cells, 2 figures; 3.256 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_20_EXECUTION.md).

<!-- CHAPTER_21_ENTRIES -->

## Chapter 21: Building and training neural networks

Use the [concept guide](CHAPTER_21_GUIDE.md) and [actual execution evidence](CHAPTER_21_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_103"></a>
### code_103 — Feedforward networks and output heads

- **Book home:** section 21.1.
- **Notebook:** [103_Chapter_21_01_mixed_features_and_heads.ipynb](notebooks/103_Chapter_21_01_mixed_features_and_heads.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** continuous and categorical inputs, shared feedforward torso, Gaussian and classification heads, output-shape and unknown-category contracts.
- **Verification:** 4 code cells, 2 figures; 2.284 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_21_EXECUTION.md).

<a id="code_104"></a>
### code_104 — Automatic differentiation and backpropagation

- **Book home:** section 21.2.
- **Notebook:** [104_Chapter_21_02_autodiff_and_gradient_checks.ipynb](notebooks/104_Chapter_21_02_autodiff_and_gradient_checks.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** explicit computational graph, manual reverse-mode derivatives, finite differences and gradcheck, gradient accumulation and updates.
- **Verification:** 4 code cells, 2 figures; 2.172 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_21_EXECUTION.md).

<a id="code_105"></a>
### code_105 — Initialization and activation behaviour

- **Book home:** section 21.3.
- **Notebook:** [105_Chapter_21_03_initialization_and_activations.ipynb](notebooks/105_Chapter_21_03_initialization_and_activations.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** activation and gradient propagation, Xavier and Kaiming controls, dead ReLU units, finite-depth initialization diagnostics.
- **Verification:** 4 code cells, 2 figures; 2.457 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_21_EXECUTION.md).

<a id="code_106"></a>
### code_106 — Normalization, optimization and regularization

- **Book home:** section 21.4.
- **Notebook:** [106_Chapter_21_04_normalization_and_training_health.ipynb](notebooks/106_Chapter_21_04_normalization_and_training_health.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual AdamW/SGD ablations, batch and layer normalization, dropout train/eval contracts, development early stopping, controlled instability dashboard.
- **Verification:** 4 code cells, 2 figures; 2.332 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_21_EXECUTION.md).

<a id="code_107"></a>
### code_107 — Debugging, batching and computational resources

- **Book home:** section 21.5.
- **Notebook:** [107_Chapter_21_05_debugging_padding_and_resources.ipynb](notebooks/107_Chapter_21_05_debugging_padding_and_resources.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** padding shortcut and explicit masking, tiny-set overfitting, weighted microbatch gradients, checkpoint exact next step, actual process peak RSS and CPU timing.
- **Verification:** 5 code cells, 2 figures; 9.869 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_21_EXECUTION.md).

<!-- CHAPTER_22_ENTRIES -->

## Chapter 22: Neural architecture families

Use the [concept guide](CHAPTER_22_GUIDE.md) and [actual execution evidence](CHAPTER_22_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_108"></a>
### code_108 — MLPs, residual networks and tabular architectures

- **Book home:** section 22.1.
- **Notebook:** [108_Chapter_22_01_residual_and_efficient_tabular_models.ipynb](notebooks/108_Chapter_22_01_residual_and_efficient_tabular_models.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** whole-building tabular comparison, residual computation, actual rank-one fast-weight ensemble, numerical basis contract, named-model implementation boundaries.
- **Verification:** 4 code cells, 2 figures; 3.985 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_22_EXECUTION.md).

<a id="code_109"></a>
### code_109 — Convolutions for signals and structured fields

- **Book home:** section 22.2.
- **Notebook:** [109_Chapter_22_02_causal_convolutions_and_spectral_features.ipynb](notebooks/109_Chapter_22_02_causal_convolutions_and_spectral_features.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual causal Conv1d model, dilation and receptive field, spectral order invariance, whole-machine holdout, future-input perturbation audit.
- **Verification:** 4 code cells, 2 figures; 4.404 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_22_EXECUTION.md).

<a id="code_110"></a>
### code_110 — Recurrent and gated architectures

- **Book home:** section 22.3.
- **Notebook:** [110_Chapter_22_03_recurrent_state_and_truncated_training.ipynb](notebooks/110_Chapter_22_03_recurrent_state_and_truncated_training.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual RNN GRU and LSTM, irregular-time input contract, masked losses, truncated derivative history, streaming state and entity resets.
- **Verification:** 4 code cells, 2 figures; 2.856 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_22_EXECUTION.md).

<a id="code_111"></a>
### code_111 — Attention and transformers

- **Book home:** section 22.4.
- **Notebook:** [111_Chapter_22_04_attention_tokens_and_access.ipynb](notebooks/111_Chapter_22_04_attention_tokens_and_access.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** scaled dot-product attention identity, actual multihead transformer blocks, feature versus time tokens, position and padding contracts, causal future-perturbation test.
- **Verification:** 4 code cells, 2 figures; 3.231 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_22_EXECUTION.md).

<a id="code_112"></a>
### code_112 — State-space and recurrent-attention hybrids

- **Book home:** section 22.5.
- **Notebook:** [112_Chapter_22_05_selective_state_and_reference_attention.ipynb](notebooks/112_Chapter_22_05_selective_state_and_reference_attention.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual input-dependent diagonal state model, exact diagonal discretization, paired context-length assessment, reference attention comparison, untrained summary-attention hybrid contract, measured CPU inference resources.
- **Verification:** 5 code cells, 2 figures; 21.375 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_22_EXECUTION.md).

<a id="code_113"></a>
### code_113 — Mixture-of-experts and conditional computation

- **Book home:** section 22.6.
- **Notebook:** [113_Chapter_22_06_conditional_experts_and_capacity.ipynb](notebooks/113_Chapter_22_06_conditional_experts_and_capacity.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual selected-row expert execution, learned top-one routing, load-balance ablation, declared linear-MAC budget, capacity fallback and queue order.
- **Verification:** 4 code cells, 2 figures; 2.442 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_22_EXECUTION.md).

<a id="code_114"></a>
### code_114 — Emerging function and geometry-aware designs

- **Book home:** section 22.7.
- **Notebook:** [114_Chapter_22_07_spline_edge_functions_and_geometry.ipynb](notebooks/114_Chapter_22_07_spline_edge_functions_and_geometry.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual differentiable cubic edge splines, SciPy basis and gradient checks, additive spline versus composed functions, locked extrapolation test, separate rotation-invariant task.
- **Verification:** 4 code cells, 2 figures; 3.789 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_22_EXECUTION.md).

<!-- CHAPTER_23_ENTRIES -->

## Chapter 23: Graph neural networks and relational learning

Use the [concept guide](CHAPTER_23_GUIDE.md) and [actual execution evidence](CHAPTER_23_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_115"></a>
### code_115 — Graph tasks and relational baselines

- **Book home:** section 23.1.
- **Notebook:** [115_Chapter_23_01_prediction_units_and_relational_baselines.ipynb](notebooks/115_Chapter_23_01_prediction_units_and_relational_baselines.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** node versus existing-edge targets, non-neural aggregated baseline, actual shared graph encoder and task heads, whole-building holdout, whole-graph mean readout.
- **Verification:** 4 code cells, 2 figures; 3.174 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_23_EXECUTION.md).

<a id="code_116"></a>
### code_116 — Message passing and graph convolutions

- **Book home:** section 23.2.
- **Notebook:** [116_Chapter_23_02_messages_aggregation_and_graph_convolutions.ipynb](notebooks/116_Chapter_23_02_messages_aggregation_and_graph_convolutions.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** edge-feature message trace, GCN SAGE and GIN-style learned operators, two-hop derivative support, permutation and pooling identities, disconnected mini-batch contract.
- **Verification:** 4 code cells, 2 figures; 3.176 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_23_EXECUTION.md).

<a id="code_117"></a>
### code_117 — Graph attention and graph transformers

- **Book home:** section 23.3.
- **Notebook:** [117_Chapter_23_03_local_attention_and_distant_information.ipynb](notebooks/117_Chapter_23_03_local_attention_and_distant_information.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual masked graph attention, global graph attention with distance bias, distant-source derivative audit, permutation of structural encodings, oversmoothing and bottleneck fixtures.
- **Verification:** 4 code cells, 2 figures; 4.493 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_23_EXECUTION.md).

<a id="code_118"></a>
### code_118 — Heterogeneous, temporal and knowledge graphs

- **Book home:** section 23.4.
- **Notebook:** [118_Chapter_23_04_typed_relations_and_time_bounded_links.ipynb](notebooks/118_Chapter_23_04_typed_relations_and_time_bounded_links.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual relation-specific graph update, node and edge availability clocks, historical-only typed snapshot, trained typed link decoder, future-positive negative audit.
- **Verification:** 4 code cells, 2 figures; 2.546 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_23_EXECUTION.md).

<a id="code_119"></a>
### code_119 — Geometric and physical graph learning

- **Book home:** section 23.5.
- **Notebook:** [119_Chapter_23_05_coordinate_transformations_and_graph_solver.ipynb](notebooks/119_Chapter_23_05_coordinate_transformations_and_graph_solver.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual vector-valued graph propagation, learned relaxation with a known physical operator, fixed numerical and coordinate-MLP baselines, joint rotation reflection translation audits, ground-reaction equilibrium.
- **Verification:** 4 code cells, 2 figures; 2.511 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_23_EXECUTION.md).

<a id="code_120"></a>
### code_120 — Scaling, failure analysis and graph explanations

- **Book home:** section 23.6.
- **Notebook:** [120_Chapter_23_06_graph_size_sampling_and_explanation_checks.ipynb](notebooks/120_Chapter_23_06_graph_size_sampling_and_explanation_checks.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual graph-size holdout, mean versus sum aggregation transfer, uniform neighbor sampling with known degree correction, heterophily counterexample, edge-attribution fidelity and stability.
- **Verification:** 4 code cells, 2 figures; 3.091 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_23_EXECUTION.md).

<!-- CHAPTER_24_ENTRIES -->

## Chapter 24: Time-series and spatiotemporal learning

Use the [concept guide](CHAPTER_24_GUIDE.md) and [actual execution evidence](CHAPTER_24_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_121"></a>
### code_121 — Forecasting tasks, horizons and baselines

- **Book home:** section 24.1.
- **Notebook:** [121_Chapter_24_01_forecast_origins_and_demand_baselines.ipynb](notebooks/121_Chapter_24_01_forecast_origins_and_demand_baselines.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual temporal forecast contract, persistence and seasonal references, local versus shared direct Ridge, recursive forecast with predicted lags, weather-prefix and future-target access audits.
- **Verification:** 4 code cells, 2 figures; 2.271 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_24_EXECUTION.md).

<a id="code_122"></a>
### code_122 — Classical forecasting and latent dynamics

- **Book home:** section 24.2.
- **Notebook:** [122_Chapter_24_02_classical_forecasts_and_filtered_dynamics.ipynb](notebooks/122_Chapter_24_02_classical_forecasts_and_filtered_dynamics.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** native seasonal exponential smoothing, native ARIMA and dynamic regression, lag regression and vector autoregression, native structural state-space filtering, future-sensitive smoothing audit.
- **Verification:** 4 code cells, 2 figures; 3.889 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_24_EXECUTION.md).

<a id="code_123"></a>
### code_123 — Machine learning and neural forecasting

- **Book home:** section 24.3.
- **Notebook:** [123_Chapter_24_03_lag_boosting_and_neural_multi_horizon_forecasts.ipynb](notebooks/123_Chapter_24_03_lag_boosting_and_neural_multi_horizon_forecasts.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** native lag-feature histogram boosting, actual GRU causal TCN and attention forecasts, actual nonoverlapping patch tokens, common multi-horizon information budget, development checkpoint and horizon-specific errors.
- **Verification:** 4 code cells, 2 figures; 15.948 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_24_EXECUTION.md).

<a id="code_124"></a>
### code_124 — Irregular signals and event sequences

- **Book home:** section 24.4.
- **Notebook:** [124_Chapter_24_04_sampling_irregular_observations_and_alarm_intensity.ipynb](notebooks/124_Chapter_24_04_sampling_irregular_observations_and_alarm_intensity.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual polyphase anti-alias filtering, offline interpolation versus causal previous hold, exposure-weighted Poisson intensity fit, actual event-time likelihood with censored tail, time-rescaled event-gap diagnostics.
- **Verification:** 4 code cells, 2 figures; 2.460 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_24_EXECUTION.md).

<a id="code_125"></a>
### code_125 — Spatial and spatiotemporal dependencies

- **Book home:** section 24.5.
- **Notebook:** [125_Chapter_24_05_shared_temporal_models_and_held_region.ipynb](notebooks/125_Chapter_24_05_shared_temporal_models_and_held_region.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** native spatial Gaussian-process reference, actual shared GRU and graph-GRU forecasts, known geometry versus unavailable regional measurements, common forecast origins and planned moving loads, source and regional horizon assessment.
- **Verification:** 4 code cells, 2 figures; 6.554 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_24_EXECUTION.md).

<a id="code_126"></a>
### code_126 — Probabilistic, hierarchical and regime-aware forecasts

- **Book home:** section 24.6.
- **Notebook:** [126_Chapter_24_06_coherent_trajectories_quantiles_and_regimes.ipynb](notebooks/126_Chapter_24_06_coherent_trajectories_quantiles_and_regimes.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual all-level forecast reconciliation, calibration-only shrinkage covariance, whole-origin multi-horizon residual scenarios, coherent draws versus nonadditive marginal quantiles, coverage pinball width by regime horizon and level.
- **Verification:** 4 code cells, 2 figures; 2.137 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_24_EXECUTION.md).

<!-- CHAPTER_25_ENTRIES -->

## Chapter 25: Physics-informed and hybrid learning

Use the [concept guide](CHAPTER_25_GUIDE.md) and [actual execution evidence](CHAPTER_25_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_127"></a>
### code_127 — Forward, inverse and hybrid scientific tasks

- **Book home:** section 25.1.
- **Notebook:** [127_Chapter_25_01_forward_inverse_and_identifiability.ipynb](notebooks/127_Chapter_25_01_forward_inverse_and_identifiability.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** native beam boundary-value solver, sparse observation operator, known-load stiffness recovery, joint load-stiffness nonidentifiability, reference refinement and sensitivity rank.
- **Verification:** 4 code cells, 2 figures; 2.199 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_25_EXECUTION.md).

<a id="code_128"></a>
### code_128 — Physics-informed neural network objectives

- **Book home:** section 25.2.
- **Notebook:** [128_Chapter_25_02_pinn_objectives_and_derivatives.ipynb](notebooks/128_Chapter_25_02_pinn_objectives_and_derivatives.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual fourth-order autograd beam residual, separate data equation and boundary terms, dimensionless residual scaling, fixed weight candidates and independent development grid, dense off-collocation validation.
- **Verification:** 4 code cells, 2 figures; 5.655 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_25_EXECUTION.md).

<a id="code_129"></a>
### code_129 — Constraints, conservation and architecture

- **Book home:** section 25.3.
- **Notebook:** [129_Chapter_25_03_hard_constraints_and_conservation.ipynb](notebooks/129_Chapter_25_03_hard_constraints_and_conservation.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual soft versus hard displacement boundary fits, independent differential residual checks, learned positive edge conductances, differentiable conservative finite-volume solve, boundary flux and interior balance identities.
- **Verification:** 4 code cells, 2 figures; 2.996 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_25_EXECUTION.md).

<a id="code_130"></a>
### code_130 — Neural differential equations and structured dynamics

- **Book home:** section 25.4.
- **Notebook:** [130_Chapter_25_04_neural_dynamics_and_solver_contracts.ipynb](notebooks/130_Chapter_25_04_neural_dynamics_and_solver_contracts.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual learned neural ODE vector field, positive mechanical stiffness and damping, differentiable RK4 and finite-difference gradient, controlled input-path integration, neural drift SDE with shared Brownian refinement.
- **Verification:** 4 code cells, 2 figures; 2.560 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_25_EXECUTION.md).

<a id="code_131"></a>
### code_131 — Mechanistic hybrids and multifidelity learning

- **Book home:** section 25.5.
- **Notebook:** [131_Chapter_25_05_hybrid_and_multifidelity_learning.ipynb](notebooks/131_Chapter_25_05_hybrid_and_multifidelity_learning.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** native coarse and fine mechanical solves, actual residual-correction Ridge, data-only comparison with matched case selection, differentiable positive-conductance closure, whole-case and changed-support assessment.
- **Verification:** 4 code cells, 2 figures; 3.286 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_25_EXECUTION.md).

<a id="code_132"></a>
### code_132 — PINN failures, validation and model choice

- **Book home:** section 25.6.
- **Notebook:** [132_Chapter_25_06_pinn_failure_and_validation_audits.ipynb](notebooks/132_Chapter_25_06_pinn_failure_and_validation_audits.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual low and high frequency PINN fits, matched-budget data-only references, off-collocation adversarial witness, missing-boundary nonuniqueness, native refined numerical reference.
- **Verification:** 4 code cells, 2 figures; 4.054 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_25_EXECUTION.md).

<!-- CHAPTER_26_ENTRIES -->

## Chapter 26: Neural operators and learned simulation

Use the [concept guide](CHAPTER_26_GUIDE.md) and [actual execution evidence](CHAPTER_26_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_133"></a>
### code_133 — From finite-dimensional maps to operators

- **Book home:** section 26.1.
- **Notebook:** [133_Chapter_26_01_operator_datasets_and_discretization.ipynb](notebooks/133_Chapter_26_01_operator_datasets_and_discretization.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual variable-coefficient solution family, whole-problem fitting and assessment, finite-grid Ridge operator reference, independent mesh refinement, input-sensor alias nonidentifiability.
- **Verification:** 4 code cells, 2 figures; 2.261 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_26_EXECUTION.md).

<a id="code_134"></a>
### code_134 — DeepONet and branch--trunk representations

- **Book home:** section 26.2.
- **Notebook:** [134_Chapter_26_02_deeponet_and_operator_objectives.ipynb](notebooks/134_Chapter_26_02_deeponet_and_operator_objectives.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual native branch-trunk inner-product network, fixed input sensors and variable output queries, supervised versus discrete physics operator objectives, whole-function development selection, higher-frequency input-support assessment.
- **Verification:** 4 code cells, 2 figures; 3.405 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_26_EXECUTION.md).

<a id="code_135"></a>
### code_135 — Fourier and spectral neural operators

- **Book home:** section 26.3.
- **Notebook:** [135_Chapter_26_03_fourier_operator_and_resolution_checks.ipynb](notebooks/135_Chapter_26_03_fourier_operator_and_resolution_checks.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual native complex spectral convolution, lifting local paths and projection, same-function grid transfer without refitting, retained-mode and FFT identity checks, nonlinear aliasing and changed spectral support.
- **Verification:** 4 code cells, 2 figures; 8.784 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_26_EXECUTION.md).

<a id="code_136"></a>
### code_136 — Graph and geometry-aware operators

- **Book home:** section 26.4.
- **Notebook:** [136_Chapter_26_04_geometry_graph_operator_and_mesh_transfer.ipynb](notebooks/136_Chapter_26_04_geometry_graph_operator_and_mesh_transfer.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** native triangular finite-element problem family, actual quadrature-weighted learned graph kernel, whole-mesh geometry assessment, node-permutation identity, new mesh resolution and notched domain.
- **Verification:** 4 code cells, 2 figures; 5.540 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_26_EXECUTION.md).

<a id="code_137"></a>
### code_137 — Surrogates, rollouts and inverse design

- **Book home:** section 26.5.
- **Notebook:** [137_Chapter_26_05_surrogate_rollouts_and_inverse_design.ipynb](notebooks/137_Chapter_26_05_surrogate_rollouts_and_inverse_design.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual repeated learned heat-step rollout, mass-preserving projection audit, surrogate design optimization with analytic gradients, independent refined solver verification, bootstrap disagreement and actual solve counts.
- **Verification:** 4 code cells, 2 figures; 2.300 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 20 October 2026. [Run evidence](CHAPTER_26_EXECUTION.md).

<!-- CHAPTER_27_ENTRIES -->

## Chapter 27: Generative models for structured data

Use the [concept guide](CHAPTER_27_GUIDE.md) and [actual execution evidence](CHAPTER_27_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_138"></a>
### code_138 — Generative tasks and evaluation targets

- **Book home:** section 27.1.
- **Notebook:** [138_Chapter_27_01_generative_tasks_and_evidence_contracts.ipynb](notebooks/138_Chapter_27_01_generative_tasks_and_evidence_contracts.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual joint and conditional mixture sampling, independent-marginal reference, conditional Gaussian-mixture imputation, generated relational keys and temporal constraints, whole-building evidence boundaries.
- **Verification:** 4 code cells, 2 figures; 2.943 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content revision verified. Checked 21 October 2026. [Run evidence](CHAPTER_27_EXECUTION.md).

<a id="code_139"></a>
### code_139 — Latent-variable models and variational learning

- **Book home:** section 27.2.
- **Notebook:** [139_Chapter_27_02_conditional_vae_and_mixed_likelihoods.ipynb](notebooks/139_Chapter_27_02_conditional_vae_and_mixed_likelihoods.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual reparameterized conditional VAE, Gaussian Bernoulli and Poisson decoder heads, common development ELBO comparison, per-latent KL and decoder sensitivity, conditional tail and type-valid generation.
- **Verification:** 4 code cells, 2 figures; 3.511 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content revision verified. Checked 21 October 2026. [Run evidence](CHAPTER_27_EXECUTION.md).

<a id="code_140"></a>
### code_140 — Adversarial models and training dynamics

- **Book home:** section 27.3.
- **Notebook:** [140_Chapter_27_03_conditional_gan_and_training_dynamics.ipynb](notebooks/140_Chapter_27_03_conditional_gan_and_training_dynamics.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual conditional GAN and Wasserstein gradient penalty, controlled aggressive generator candidate, development selected generative checkpoints, conditional mode coverage and resampling references, actual rare-class augmentation assessment.
- **Verification:** 4 code cells, 2 figures; 4.415 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content revision verified. Checked 21 October 2026. [Run evidence](CHAPTER_27_EXECUTION.md).

<a id="code_141"></a>
### code_141 — Autoregressive, flow and energy models

- **Book home:** section 27.4.
- **Notebook:** [141_Chapter_27_04_autoregressive_flow_and_energy_models.ipynb](notebooks/141_Chapter_27_04_autoregressive_flow_and_energy_models.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** normalized mixed-type autoregressive factorization, native affine-coupling flow with inverse and Jacobian checks, native persistent-negative-phase energy learning, Langevin mixing and unnormalized score limits, independent reference assessment.
- **Verification:** 4 code cells, 2 figures; 5.831 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content revision verified. Checked 21 October 2026. [Run evidence](CHAPTER_27_EXECUTION.md).

<a id="code_142"></a>
### code_142 — Diffusion and flow matching

- **Book home:** section 27.5.
- **Notebook:** [142_Chapter_27_05_diffusion_and_flow_matching.ipynb](notebooks/142_Chapter_27_05_diffusion_and_flow_matching.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual conditional DDPM epsilon prediction and ancestral sampling, native straight-path conditional flow matching, separate development objectives and fixed training budgets, ODE refinement with shared initial noise, mechanism alignment and trajectory distribution assessment.
- **Verification:** 4 code cells, 2 figures; 3.371 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content revision verified. Checked 21 October 2026. [Run evidence](CHAPTER_27_EXECUTION.md).

<a id="code_143"></a>
### code_143 — Utility, validity, leakage and privacy

- **Book home:** section 27.6.
- **Notebook:** [143_Chapter_27_06_synthetic_data_acceptance_and_disclosure.ipynb](notebooks/143_Chapter_27_06_synthetic_data_acceptance_and_disclosure.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** separate fidelity utility schema and disclosure evidence, actual source-only synthetic-only and augmented classifiers, development-calibrated proximity membership attack on generated data, deliberate source canary and exact-copy audits, relational and derived-field acceptance checks without DP claims.
- **Verification:** 4 code cells, 2 figures; 2.674 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content revision verified. Checked 21 October 2026. [Run evidence](CHAPTER_27_EXECUTION.md).

<!-- CHAPTER_28_ENTRIES -->

## Chapter 28: Tabular and relational foundation models

Use the [concept guide](CHAPTER_28_GUIDE.md) and [actual execution evidence](CHAPTER_28_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_144"></a>
### code_144 — What makes a reusable tabular model

- **Book home:** section 28.1.
- **Notebook:** [144_Chapter_28_01_reusable_predictor_pretraining_and_context.ipynb](notebooks/144_Chapter_28_01_reusable_predictor_pretraining_and_context.ipynb).
- **Data/dependencies:** locally generated task inputs; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual cross-task synthetic pretraining, separate frozen labelled-context inference, heterogeneous feature-count masks, task-level development and assessment, parameter invariance and context permutation checks.
- **Verification:** 4 code cells, 2 figures; 4.601 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_28_EXECUTION.md).

<a id="code_145"></a>
### code_145 — The TabPFN family and prior-data learning

- **Book home:** section 28.2.
- **Notebook:** [145_Chapter_28_02_pinned_tabpfn_and_grouped_comparison.ipynb](notebooks/145_Chapter_28_02_pinned_tabpfn_and_grouped_comparison.ipynb).
- **Data/dependencies:** locally generated task inputs; explicit one-time public checkpoint acquisition, then offline CPU inference; [assets and licences](CHAPTER_28_ASSETS.md); [pinned environment](requirements-lock.txt).
- **Scope:** actual pinned TabPFN v2 CPU inference, explicit offline checkpoint hash verification, whole-building development selection versus final assessment, native missing-value handling and fixed tree controls, unchanged pretrained weights with labelled context.
- **Verification:** 4 code cells, 2 figures; 5.132 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_28_EXECUTION.md).

<a id="code_146"></a>
### code_146 — TabICL, TabFM and cross-table approaches

- **Book home:** section 28.3.
- **Notebook:** [146_Chapter_28_03_tabicl_tasks_and_checkpoint_contracts.ipynb](notebooks/146_Chapter_28_03_tabicl_tasks_and_checkpoint_contracts.ipynb).
- **Data/dependencies:** locally generated task inputs; explicit one-time public checkpoint acquisition, then offline CPU inference; [assets and licences](CHAPTER_28_ASSETS.md); [pinned environment](requirements-lock.txt).
- **Scope:** actual pinned TabICLv2 classifier and regressor, separate labelled-context task heads, checkpoint and source-package identity audit, development-selected native ensemble and tree controls, regression quantile assessment without calibration guarantee.
- **Verification:** 4 code cells, 2 figures; 5.138 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_28_EXECUTION.md).

<a id="code_147"></a>
### code_147 — Relational foundation models

- **Book home:** section 28.4.
- **Notebook:** [147_Chapter_28_04_relational_pretraining_and_historical_queries.ipynb](notebooks/147_Chapter_28_04_relational_pretraining_and_historical_queries.ipynb).
- **Data/dependencies:** locally generated task inputs; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual own cross-database relational pretraining, historical event messages and parent-key gathers, frozen labelled-context prediction on new databases, per-database neural and flat-feature controls, future-row intervention with invariant admitted predictions.
- **Verification:** 4 code cells, 2 figures; 4.142 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_28_EXECUTION.md).

<a id="code_148"></a>
### code_148 — Adaptation, input handling and resource limits

- **Book home:** section 28.5.
- **Notebook:** [148_Chapter_28_05_context_caches_inputs_and_distillation.ipynb](notebooks/148_Chapter_28_05_context_caches_inputs_and_distillation.ipynb).
- **Data/dependencies:** locally generated task inputs; explicit one-time public checkpoint acquisition, then offline CPU inference; [assets and licences](CHAPTER_28_ASSETS.md); [pinned environment](requirements-lock.txt).
- **Scope:** actual native mixed-type and missing-value handling, labelled-context size selection, native KV-cache numerical and storage audit, measured CPU fit and repeat-prediction observations, actual teacher-probability distillation with held-out evaluation.
- **Verification:** 4 code cells, 2 figures; 5.376 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_28_EXECUTION.md).

<a id="code_149"></a>
### code_149 — Benchmark evidence and applicability limits

- **Book home:** section 28.6.
- **Notebook:** [149_Chapter_28_06_benchmark_provenance_and_applicability.ipynb](notebooks/149_Chapter_28_06_benchmark_provenance_and_applicability.ipynb).
- **Data/dependencies:** bundled public reference tables and locally generated tasks; explicit one-time public checkpoint acquisition, then offline CPU inference; [assets and licences](CHAPTER_28_ASSETS.md); [pinned environment](requirements-lock.txt).
- **Scope:** actual pinned native model and tree comparisons across public and generated tables, separate random-row versus whole-entity assessment, equal explicit candidate counts without lifetime-compute claims, table-level paired uncertainty with named task families, actual final-label context leakage fixture and overlap hashes.
- **Verification:** 4 code cells, 2 figures; 15.564 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_28_EXECUTION.md).

<!-- CHAPTER_29_ENTRIES -->

## Chapter 29: Temporal and scientific foundation models

Use the [concept guide](CHAPTER_29_GUIDE.md) and [actual execution evidence](CHAPTER_29_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_150"></a>
### code_150 — Pretraining for time series

- **Book home:** section 29.1.
- **Notebook:** [150_Chapter_29_01_cross_series_pretraining_and_context.ipynb](notebooks/150_Chapter_29_01_cross_series_pretraining_and_context.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual shared forecasting pretraining across independent generated series, context-only normalization and patch representation, whole-series model selection and final assessment, frozen checkpoint versus local autoregression and seasonal controls, scale quantization and causal context interventions.
- **Verification:** 4 code cells, 2 figures; 2.533 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_29_EXECUTION.md).

<a id="code_151"></a>
### code_151 — Representative forecasting model families

- **Book home:** section 29.2.
- **Notebook:** [151_Chapter_29_02_native_forecasting_families_and_backtests.ipynb](notebooks/151_Chapter_29_02_native_forecasting_families_and_backtests.ipynb).
- **Data/dependencies:** task inputs generated locally; explicit one-time public checkpoint acquisition then offline CPU inference; [assets and notices](CHAPTER_29_ASSETS.md); [pinned environment](requirements-lock.txt).
- **Scope:** actual pinned TimesFM2.5 and ChronosBoltTiny CPU inference, explicit model/config byte hashes and offline loading, multiple origins kept within independent generated series, seasonal local autoregression and lagged-tree controls, native quantile shape coverage and immutable checkpoint parameters.
- **Verification:** 4 code cells, 2 figures; 7.059 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_29_EXECUTION.md).

<a id="code_152"></a>
### code_152 — Adaptation and evaluation across domains

- **Book home:** section 29.3.
- **Notebook:** [152_Chapter_29_03_forecast_adaptation_and_target_budgets.ipynb](notebooks/152_Chapter_29_03_forecast_adaptation_and_target_budgets.ipynb).
- **Data/dependencies:** task inputs generated locally; explicit one-time public checkpoint acquisition then offline CPU inference; [assets and notices](CHAPTER_29_ASSETS.md); [pinned environment](requirements-lock.txt).
- **Scope:** actual frozen ChronosBolt forecast across cadence regimes, causal historical imputation and input contracts, target-label residual adaptation with separate selection and assessment, independent-series uncertainty for label-budget comparisons, temporal overlap and future-covariate availability interventions.
- **Verification:** 4 code cells, 2 figures; 3.137 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_29_EXECUTION.md).

<a id="code_153"></a>
### code_153 — Scientific and physical foundation models

- **Book home:** section 29.4.
- **Notebook:** [153_Chapter_29_04_scientific_pretraining_and_operator_adaptation.ipynb](notebooks/153_Chapter_29_04_scientific_pretraining_and_operator_adaptation.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual original spectral solution-operator pretraining across equation parameters, analytic periodic advection diffusion reaction references, whole-case development and downstream parameter updates, warm-start versus scratch operators with equal downstream budgets, physical support and semigroup consistency checks without named-model substitution.
- **Verification:** 4 code cells, 2 figures; 2.604 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_29_EXECUTION.md).

<a id="code_154"></a>
### code_154 — Validity, scale and responsible reuse

- **Book home:** section 29.5.
- **Notebook:** [154_Chapter_29_05_physical_validity_mesh_and_boundary_tests.ipynb](notebooks/154_Chapter_29_05_physical_validity_mesh_and_boundary_tests.ipynb).
- **Data/dependencies:** generated locally; no ordinary-run files, network, credentials or GPU; [pinned environment](requirements-lock.txt).
- **Scope:** actual shared learned diffusion stencil with disclosed observation bias, new-mesh physical scaling and deliberate wrong-grid fixture, independent converged sparse numerical references and analytic checks, periodic conservation projection versus invalid Dirichlet mass constraint, boundary values rollout stability and field errors checked separately.
- **Verification:** 4 code cells, 2 figures; 2.492 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content tree verified. Checked 21 October 2026. [Run evidence](CHAPTER_29_EXECUTION.md).

<!-- CHAPTER_30_ENTRIES -->

## Chapter 30: LLMs and typed decision models

Use the [concept guide](CHAPTER_30_GUIDE.md) and [actual execution evidence](CHAPTER_30_EXECUTION.md). Generated teaching mechanisms retain the information, task and interpretation limits declared in each notebook.

<a id="code_155"></a>
### code_155 — LLMs for structured and scientific tasks

- **Book home:** section 30.1.
- **Notebook:** [155_Chapter_30_01_structured_records_and_native_language_prediction.ipynb](notebooks/155_Chapter_30_01_structured_records_and_native_language_prediction.ipynb).
- **Data/dependencies:** task inputs generated locally; [dedicated Python3.12 runtime](CHAPTER_30_RUNTIME.md); explicit [checkpoint acquisition](CHAPTER_30_ASSETS.md) where declared, then offline CPU inference.
- **Scope:** actual pinned instruction-LLM prediction from bounded generated states, units and explicit choice-rule serialization, free generation versus conditional allowed-label projection, syntax correctness and probability mass measured separately, frozen weights and evidence-only field handling.
- **Verification:** 4 code cells, 2 figures; 7.621 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 21 October 2026. [Run evidence](CHAPTER_30_EXECUTION.md).

<a id="code_156"></a>
### code_156 — Prompting, context and adaptation

- **Book home:** section 30.2.
- **Notebook:** [156_Chapter_30_02_prompt_context_and_source_example_policies.ipynb](notebooks/156_Chapter_30_02_prompt_context_and_source_example_policies.ipynb).
- **Data/dependencies:** task inputs generated locally; [dedicated Python3.12 runtime](CHAPTER_30_RUNTIME.md); explicit [checkpoint acquisition](CHAPTER_30_ASSETS.md) where declared, then offline CPU inference.
- **Scope:** actual fixed-checkpoint prompt comparison on unseen building groups, equivalent JSON and prose measurement representations, zero-example random-example and source-only nearest-example policies, source-fitted retrieval scale and explicit label-access audit, weight invariance and prompt-token budgets without native fine-tuning claims.
- **Verification:** 4 code cells, 2 figures; 18.891 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 21 October 2026. [Run evidence](CHAPTER_30_EXECUTION.md).

<a id="code_157"></a>
### code_157 — Typed decisions and System One terminology

- **Book home:** section 30.3.
- **Notebook:** [157_Chapter_30_03_typed_heads_schema_and_action_policy.ipynb](notebooks/157_Chapter_30_03_typed_heads_schema_and_action_policy.ipynb).
- **Data/dependencies:** task inputs generated locally; [dedicated Python3.12 runtime](CHAPTER_30_RUNTIME.md); explicit [checkpoint acquisition](CHAPTER_30_ASSETS.md) where declared, then offline CPU inference.
- **Scope:** actual own multihead neural prediction from structured generated states, separate choice ordinal-score and yes-no output contracts, whole-building training and development selection, schema-valid yet incorrect counterexample and rejected invalid fixtures, deterministic software policy separated from model judgment.
- **Verification:** 4 code cells, 2 figures; 2.328 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 21 October 2026. [Run evidence](CHAPTER_30_EXECUTION.md).

<a id="code_158"></a>
### code_158 — Jev, Laya and Kev as concrete families

- **Book home:** section 30.4.
- **Notebook:** [158_Chapter_30_04_native_laya_kev_and_documented_jev.ipynb](notebooks/158_Chapter_30_04_native_laya_kev_and_documented_jev.ipynb).
- **Data/dependencies:** task inputs generated locally; [dedicated Python3.12 runtime](CHAPTER_30_RUNTIME.md); explicit [checkpoint acquisition](CHAPTER_30_ASSETS.md) where declared, then offline CPU inference.
- **Scope:** actual pinned Laya and Kev CPU inference with required Qwen base, native choice ordinal-score and noul output contracts, same generated states and literal questions across executed families, unused dummy label metadata verified absent from predictive inputs, documented unexecuted Jev and explicitly bounded developer claims.
- **Verification:** 4 code cells, 2 figures; 29.000 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 21 October 2026. [Run evidence](CHAPTER_30_EXECUTION.md).

<a id="code_159"></a>
### code_159 — Evaluation, calibration and deferral

- **Book home:** section 30.5.
- **Notebook:** [159_Chapter_30_05_calibration_and_validation_chosen_deferral.ipynb](notebooks/159_Chapter_30_05_calibration_and_validation_chosen_deferral.ipynb).
- **Data/dependencies:** task inputs generated locally; [dedicated Python3.12 runtime](CHAPTER_30_RUNTIME.md); explicit [checkpoint acquisition](CHAPTER_30_ASSETS.md) where declared, then offline CPU inference.
- **Scope:** actual native Laya probabilities versus a fitted numeric tree control, whole-building source calibration development and final evidence roles, calibration-only temperature selection and development-only deferral, option-order and missing-evidence diagnostics, returned confidence separated from observed correctness and policy authority.
- **Verification:** 4 code cells, 2 figures; 37.964 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 21 October 2026. [Run evidence](CHAPTER_30_EXECUTION.md).

<a id="code_160"></a>
### code_160 — Scientific workflows and security boundaries

- **Book home:** section 30.6.
- **Notebook:** [160_Chapter_30_06_verified_scientific_tools_and_security_boundaries.ipynb](notebooks/160_Chapter_30_06_verified_scientific_tools_and_security_boundaries.ipynb).
- **Data/dependencies:** task inputs generated locally; [dedicated Python3.12 runtime](CHAPTER_30_RUNTIME.md); explicit [checkpoint acquisition](CHAPTER_30_ASSETS.md) where declared, then offline CPU inference.
- **Scope:** actual small language model proposes bounded mechanical tool choices, typed whitelist and evidence consistency gate separate from model text, independent Euler-Bernoulli finite-element verification of exact formulas, generated adversarial note diagnostic and private-field minimization, auditable numeric inputs without arbitrary code or external actions.
- **Verification:** 4 code cells, 2 figures; 6.354 seconds incl. fresh-kernel lifecycle, Darwin arm64 CPU.
- **Status:** published and executed; remote content verified. Checked 21 October 2026. [Run evidence](CHAPTER_30_EXECUTION.md).
