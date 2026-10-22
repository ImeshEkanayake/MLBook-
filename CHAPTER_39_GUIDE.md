# Chapter 39: Robustness and domain validity — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_39_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 39.1 · Distribution shifts and support


Declared mechanisms: source-only classifier assessed on separate covariate and conditional shifts, identical observed inputs with changed response law as an observability control, exact class-conditional label-shift generator and prior correction, source-support map and independent label-dependent diagnostics.

```bash
python scripts/run_notebook.py notebooks/206_Chapter_39_01_shift_types_support_and_observability.ipynb
```

## 39.2 · Corruption and measurement robustness


Declared mechanisms: actual two-channel temporal sensor regression with source-only augmentation, severity tests for noise missing channel calibration bias and delayed packets, unit timestamp and finite-value validators with explicit reject counts, independent clean and corrupted outcomes without challenge-selected repairs.

```bash
python scripts/run_notebook.py notebooks/207_Chapter_39_02_sensor_corruptions_augmentation_and_input_validation.ipynb
```

## 39.3 · Extrapolation and structural generalization


Declared mechanisms: actual frequency-domain elastic chain solver with independent source/final entities, separate graph size member length material load and frequency challenges, learned physical response scaling contrasted with raw feature boosting, changed boundary-condition challenge exposes misspecified physical transfer.

```bash
python scripts/run_notebook.py notebooks/208_Chapter_39_03_dynamic_chain_extrapolation_by_domain_axis.ipynb
```

## 39.4 · Physical and domain validity


Declared mechanisms: actual source-fitted anisotropic vector response and mechanical comparator, rotated geometry force covariance boundary and equilibrium checks, explicit corruption and support-change stress-test board, separate displacement error force residual energy and field constraints.

```bash
python scripts/run_notebook.py notebooks/209_Chapter_39_04_physical_stress_board_symmetry_equilibrium_and_bounds.ipynb
```

## 39.5 · Adaptation, stress testing and fallback


Declared mechanisms: actual clipped density-ratio regression and effective sample size, actual convex group-max epigraph optimization with feasibility checks, unlabelled mean alignment and equal-budget random versus targeted target labels, independent challenge results with frozen source-envelope acceptance and explicit deferrals.

```bash
python scripts/run_notebook.py notebooks/210_Chapter_39_05_adaptation_reweighting_group_robustness_and_targeted_labels.ipynb
```

## Interpretation and boundaries

# Chapter 39 mechanisms, controls and interpretation

Five original laboratories retain all five scopes and both visual briefs. They execute 20 code cells with ten inline figures. Ordinary execution is self-contained, offline and CPU-only; no file, credential, dependency or model/dataset asset is added. Runtime remains CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and threadpoolctl 3.7.0. Source access/execution date: 22 October 2026, Australia/Melbourne; literature cutoff: 18 October 2026.

- **206 / shift identification:** Source 1,600 independent load/material records; fixed 100-iteration HGB. Four 800-record final domains: familiar, covariate prevalence/load shift with unchanged conditional law, unsupported higher loads, and an exactly identical familiar input array with reversed load effect. Familiar/conditional Brier 0.145137/0.484303 and error 0.19875/0.70125. Every deterministic input diagnostic is unchanged for the conditional control. Unsupported Brier 0.025781 with 0.975 positive prevalence is retained: novelty is not proof of numerical failure, and this favourable finite score is not unrestricted validity. Separate exact label-first generator holds Normal(-1,1)/Normal(1,1) class-conditional sensor laws fixed while prior changes 0.3→0.7. Source logistic on 2,000 records, 1,000 independent target observations; explicitly oracle prior correction improves Brier 0.142056→0.099574. No unlabeled prior-estimation claim. Visual A contrasts source envelope/domain changes with response-law changes.
- **207 / measurement faults:** Independent 1,200 source/500 final eight-step AR(0.8) trajectories, two noisy scaled sensors. Current/previous measurements predict current latent state plus noise. Native HGB clean fit versus clean plus three source-only augmentation copies (4,800 rows total): noise SD 0.2, channel-one bias up to 0.3, 15% whole-channel dropout. Final three-level tests distinguish noise amplitude, fraction with missing channel, calibration bias and fraction delayed by two steps. Complete dropout RMSE clean/augmented 0.389845/0.096916; strongest bias 0.319945/0.151963; all delayed 0.272672/0.138070. Strongest added noise worsens slightly with augmentation: 0.290728/0.304240. Current targets stay unchanged under stale packets; NaN is explicit missingness, not zero. Known milli-unit conversion actually restores original features: clean RMSE 0.452190 uncorrected→0.090553 converted; augmented 0.247341→0.082086. Disjoint metadata fixtures reject 50 unknown units, 50 stale records and ten infinities; 390 accepted, 110 unresolved rejects. Accepted RMSE is separate from service obligations. Validators do not identify in-range bias or hidden conditional changes.
- **208 / structural axes:** Actual complex dynamic chain solver (K−omega²I+i0.04omegaI)u=f. Source 1,000 independent chains, n=3–6, positive EA5–8, length0.8–1.2, load0.5–1.5, frequency0–0.1 in declared reference units. Actual 100-iteration HGB on five raw fields; separate known-physics response with fitted nonnegative scale 1.000109 is privileged correct-model information. Independent 200 entities per axis. Raw RMSE familiar 0.032913, graph size 0.770266, length 0.650269, material 2.660664, load 1.854571, frequency 3.247854; physical-scaling RMSE about 0.01 throughout while equations remain correct. Higher-frequency response reaches 16.719668. Separate added tip-to-ground spring changes boundary mechanism without visible feature change: raw/assumed-free-tip/metadata-informed oracle RMSE 0.622510/0.621596/0.010385. Oracle is a consistency comparator, not an adapted learner. Exact force scaling and independent new-entity semantics are checked.
- **209 / validity board:** Actual 2D rotated positive anisotropic stiffness, known force and free displacement, fixed node0. Source 1,200 elements with narrow angle support; source StandardScaler, degree-two PolynomialFeatures and Ridge alpha1. Familiar 300-element RMSE 0.061766 mm, force residual RMS 0.119105 kN. Joint geometry/force ninety-degree rotation keeps exact solver covariance but learned RMSE 19.820527 mm, force residual RMS 41.038519 kN, covariance error 19.815292 mm. Severe polynomial extrapolation failure retained. Seven first-query fixtures separate measured-force and simulator-true-force audits, rotated prediction, zero field, changed clamp with old solution, and correct constrained solution. Zero field passes original support and nonnegative energy but residual 0.494205 kN. Old equilibrium solution passes the remaining free equation but violates new clamp by 0.123727 mm; constrained solver passes both. Missing force is rejected before inference. Visual B aligns all faults with their specific checks; energy/support/equilibrium are not interchangeable acceptance certificates. Board uses a symmetric-log residual axis so the smaller nonzero defects remain visible.
- **210 / adaptation:** Source 400 standard-normal inputs, target pool 200 Normal(1,1), nonlinear common response x²+0.4x plus noise0.2; fixed linear family intentionally misspecified. Actual empirical regression; known simulator density ratio exp(x−0.5) capped at ten (ESS168.045615); true convex group-max epigraph regression with L2 penalty0.01 and two source sign groups, successful SLSQP/constraint slack about2e−14; unlabeled mean alignment with shift1.173417; random versus high-input target acquisition of forty labels each, selected before labels, same hidden pool outcomes and equal source/selected-target aggregate weight. Final 800 familiar/800 target records are independent and never select a route. Target RMSE source2.851772/weighted1.625031/groupmax2.739477/alignment3.092172/random40 1.701665/targeted40 1.954459. Acquisition targeting and mean alignment are not automatically beneficial; familiar-population tradeoffs remain in outputs. A changed-response stress adds4 above x=1 using the exact same target inputs. Frozen source1–99% envelope[−2.118505,2.253442] accepts709/800 target and defers91, identically under changed law. Accepted source-model RMSE1.460477→3.986199; deferrals are unresolved, not counted as correct. No universal OOD, adaptive-release or fallback-correctness guarantee.

Initial job launcher mistakenly resolved the virtual-environment Python symlink to base Python and failed on its missing nbformat import before any notebook ran. The corrected launcher uses sys.executable inside the existing environment; all fresh kernels pass. A notebook syntax error was caught by builder compilation and repaired before209 execution.210 was rerun after coupling acquisition strategies to the same hidden pool outcomes;209 was rerun for the board's residual-axis readability. Markdown guide links were corrected to Chapter39 without changing executed code. All final source code and numerical RESULT dictionaries are rerun during isolated vector export and agree exactly. Ten original SVG/vector-PDF/PNG sets and actual inline versions are reviewed during delivery. All assertions pass and current notebooks contain no errors or stderr. Primary PDFs for WILDS, covariate-weighted validation and group DRO were inspected; these original teaching mechanisms do not reproduce their datasets, algorithms in full or benchmark improvements. Chapters40–43 and the whole-book audit remain required.
