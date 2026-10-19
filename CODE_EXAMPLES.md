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
