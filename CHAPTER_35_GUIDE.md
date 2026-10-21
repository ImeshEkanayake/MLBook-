# Chapter 35: Training strategies, tuning, and AutoML — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution is offline and CPU-only. Laboratory 185 first requires the verified [TabPFN asset](CHAPTER_35_ASSETS.md); laboratory 186 uses the dedicated [Python 3.12 runtime](CHAPTER_35_RUNTIME.md). Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_35_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 35.1 · Hyperparameters and search spaces

- [Draw valid configurations before looking at any development result](notebooks/183_Chapter_35_01_conditional_search_spaces_and_fitted_parameters.ipynb#declare-conditional-spaces)
- [Fit model parameters inside the declared source boundary](notebooks/183_Chapter_35_01_conditional_search_spaces_and_fitted_parameters.ipynb#fitted-transformations-and-final-selection)

Declared mechanisms: actual conditional boosting and neural search configurations, family-specific logarithmic learning-rate and regularization ranges, source-only missing-value and scaling fits, development-only model selection with one final locked assessment, explicit different tree and neural update allocations.

```bash
python scripts/run_notebook.py notebooks/183_Chapter_35_01_conditional_search_spaces_and_fitted_parameters.ipynb
```

## 35.2 · Search, early stopping and resource allocation

- [Fit real candidates at declared resource levels](notebooks/184_Chapter_35_02_bayesian_halving_hyperband_and_population_search.ipynb#static-search-and-fidelity)
- [Train and mutate actual model lineages](notebooks/184_Chapter_35_02_bayesian_halving_hyperband_and_population_search.ipynb#population-weight-transfer)

Declared mechanisms: actual random and Gaussian-process expected-improvement search, actual successive halving and Hyperband bracket allocation, explicit restart cost with a common 432-update ceiling, actual synchronous population weight and optimizer transfer with rate mutation, locked final assessment and actual elimination visual.

```bash
python scripts/run_notebook.py notebooks/184_Chapter_35_02_bayesian_halving_hyperband_and_population_search.ipynb
```

## 35.3 · Model and architecture selection

- [Spend a declared screening stage before expanding a family](notebooks/185_Chapter_35_03_staged_family_architecture_and_foundation_selection.ipynb#screen-families-before-tuning)
- [Expand only the shortlisted families and retain the full attempt record](notebooks/185_Chapter_35_03_staged_family_architecture_and_foundation_selection.ipynb#shortlist-architecture-and-ensemble)

Declared mechanisms: actual linear tree neural and pinned TabPFN v2 family screening, conditional shortlist tuning of representations and architectures, source-only learned preprocessing and frozen pretrained weights, actual development-fitted convex ensemble with locked final assessment, explicit immutable external checkpoint verification and offline inference.

```bash
python scripts/run_notebook.py notebooks/185_Chapter_35_03_staged_family_architecture_and_foundation_selection.ipynb
```

## 35.4 · AutoML and automated workflows

- [Compare actual workflows on the same buildings and assessment boundary](notebooks/186_Chapter_35_04_native_automl_budget_and_auditable_workflow.ipynb#native-automl-and-manual-budget)
- [Audit proposals before they consume a protected role or an unbounded budget](notebooks/186_Chapter_35_04_native_automl_budget_and_auditable_workflow.ipynb#auditable-proposals-and-information-access)

Declared mechanisms: actual native AutoGluon LightGBM random forest neural and weighted ensemble fitting, source-prefitted native feature generator with fit-call audit, same grouped data roles and fifteen-second ceilings for manual and AutoML, freshly measured resource observations outside deterministic scientific results, explicit proposal validator distinguished from an executed language-model agent.

```bash
build/chapter35-runtime/bin/python scripts/run_notebook.py notebooks/186_Chapter_35_04_native_automl_budget_and_auditable_workflow.ipynb
```

## 35.5 · Selection bias, reporting and final refitting

- [Fit inside inner boundaries and assess outside them](notebooks/187_Chapter_35_05_nested_selection_refitting_and_reused_test_bias.ipynb#nested-selection-and-refitting)
- [Repeated assessment reuse can optimize noise](notebooks/187_Chapter_35_05_nested_selection_refitting_and_reused_test_bias.ipynb#reused-assessment-and-attempt-counts)

Declared mechanisms: actual grouped inner selection of depth rate and stopping checkpoint, outer evaluation with source-only preprocessing and executed fixed-budget refits, whole-source inner selection followed by locked independent final assessment, repeated equal-risk predictor selection showing reused-score optimism, nested information-boundary diagram with actual building counts.

```bash
python scripts/run_notebook.py notebooks/187_Chapter_35_05_nested_selection_refitting_and_reused_test_bias.ipynb
```

## Interpretation and boundaries

# Chapter 35 mechanisms, controls and interpretation

Five laboratories preserve all five numbered scopes and both visual briefs. They execute 20 code cells and produce 11 inline figures. All imports, helpers and generated observations are internal. Ordinary runs are offline and CPU-only, but laboratory 185 needs the explicitly acquired, hash-verified TabPFN v2 checkpoint; laboratory 186 needs a dedicated Python environment. Literature cutoff: 18 October 2026. Execution and primary-source access: 22 October 2026 Australia/Melbourne.

## Environments and assets

Laboratories 183–185 and 187 use the unchanged CPython 3.14.3 environment: NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and Torch 2.14.1 CPU; 185 additionally uses already installed TabPFN 9.2.0. The explicit v2 classifier weights are reused from the verified Chapter 28 cache: Prior-Labs/TabPFN-v2-clf revision f851f2a3c941544733b712d8c0f96dfae9b28862, filename tabpfn-v2-classifier-v2_default.ckpt, 29, 009, 539 bytes, SHA 256 cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49. The asset guide, acquisition script and licence notice accompany the notebook. No new model download occurred; missing or different bytes fail explicitly rather than substitute a model.

AutoGluon 1.6.3 excludes Python 3.14. Laboratory 186 therefore uses a separate CPython 3.12.13 environment with AutoGluon tabular/core/features/common1.6.3, Torch 2.14.1 CPU, NumPy 2.5.4, SciPy 1.18.1, pandas 2.3.3, scikit-learn 1.9.1, LightGBM 4.7.0 and Matplotlib 3.11.2. Direct requirements and all 81 installed package pins are published separately. Primary PyPI release metadata verifies all 81 versions were available before 19 OctoberUTC. Both environments pass pip checks; neither the main environment nor the separate Chapter 30 environment is changed. Native fitting imports Torch first, uses float 32 and one CPU thread; the other Torch laboratories use float 64. The runtime guide records exact commands and boundaries.

## Actual mechanisms

- **183 / conditional spaces:**180 buildings with four records each split 108 source/36 development/36 final. Twelve pre-drawn configurations cross six native-missing histogram-boosting recipes and six source-median-imputed neural recipes with StandardScaler or RobustScaler. Tree depth/leaf minimum/rate and neural width/rate/decay/scaler are genuinely conditional. Trees train 60 iterations with automatic stopping disabled; networks train 150 full-batch updates. Assertions independently verify source-fitted transformation statistics. Development RMSE chooses one recipe, refitted using the same source, seed and fixed resources before one final assessment. Trial 11, neural width 8 with standard scaling, scores development 0.7509 and final 0.916687 RMSE. Source scores for all candidates remain descriptive rather than a selection objective.
- **184 / search and scheduling:**A fixed 6→12→1 Tanh network and a declared 64-point log-uniform learning-rate/decay pool support actual random search, Gaussian-process expected improvement, successive halving and Hyperband. Random/GP each fit 16 candidates for 27 updates, spending 432 updates; their first four candidates coincide. The GP uses a fixed Matern kernel and actual untried-pool EI, without a claim to reproduce the paper's full inference scheme. Four halving brackets restart27/9/3/1 candidates at1/3/9/27 updates, each spending 108. Hyperband's four brackets spend108/99/108/108=423 under a432 ceiling, leaving 9 unused. The declared return rule considers full 27-update candidates only; this differs from the original algorithm's minimum over intermediate losses. Actual synchronous population training uses four slots, 108 updates each, development checks every nine updates, 11 weight-and-Adam-state exploit copies and multiplicative clipped rate/decay exploration. Its longer effective horizon differs from static search; sequential CPU execution does not reproduce asynchronous scheduling. Final RMSE random/GP1.463158, halving/Hyperband1.382326, population 1.552595. Final scores never choose among policies. Visual B displays actual resources and eliminations rather than a conceptual learning curve.
- **185 / staged family and architecture choice:**64 buildings split 32 source/16 development/16 final, with five records each. Four actual screening fits are median-imputed scaled logistic, native histogram boosting, a small neural network and frozen TabPFN v2 with 160 source-context labels. Development Brier shortlists TabPFN and linear; predeclared expansion adds a four-member TabPFN prediction ensemble and degree-two polynomial logistic. Other potential expansions are declared but not executed or counted. Six actual fits enter the attempt log. Development chooses the original single-member TabPFN; an independently fitted convex combination of the top two assigns weight 1.0 to it, so the ensemble is honestly degenerate. Final Brier 0.240192 versus source-prevalence0.248008; log loss 0.666231 versus 0.689161. A source-only eight-row warm-up precedes the pretrained-parameter hash: native inference preparation can change dtype/state before that boundary. Subsequent development/final prediction leaves the hashed state unchanged. No final outcome fits any choice.
- **186 / native AutoML:**120 buildings split 72 source/24 development/24 final, four records each, with numerical missing values and categorical zones. Six manual logistic/boosting candidates and native AutoGluon LightGBM 80, random forest 80, NeuralNetTorch 25 and weighted ensemble use the same development-log-loss objective and separate 15-second ceilings. Feature generation is inside each allowance; short finite lists finish well below the ceilings, so measured time is not equal consumption or a portable speed claim. The native SourceOnlyGenerator subclasses AutoMLPipelineFeatureGenerator, fits once on source indices and is passed already fitted; the learner transforms its otherwise combined train/tuning frame. Assertions verify its one fit call and all four native model names. No bagging, GPU, dynamic stacking or threshold calibration. Selected manual HGB final Brier0.272414/log loss 0.755003; native weighted ensemble0.249746/0.692315; prevalence0.247287/0.687712. Automation does not beat the prevalence control here. Resource observations are freshly measured outside deterministic RESULTS and retained in actual kernel/export evidence. Three proposed requests then exercise a deterministic role/budget validator: reject final-role fitting, reject 1000 updates over remaining budget, admit a50-update source request. This last step performs no extra fit and executes no language-model agent; AIDE and auto-sklearn are explained from primary sources, not claimed as installed executions.
- **187 / selection and refit:**160 independent buildings with four records each: 120 source/40 locked final. Three outer grouped folds fit 80 and assess 40 buildings; each has three inner grouped folds. Four boosting recipes cross depth2/5 and rate0.05/0.15; every inner fit actually trains 40 trees and examines staged5/15/40 checkpoints. Source-median imputation is fitted separately within each inner fold. All 48 inner fits, including selection on all 120 source buildings, spend 1920 trees; retrospective checkpoint selection is not early-saving computation. Outer labels assess their own selected procedure without selecting it. Final selection reruns inside all source buildings, refits 480 records at the chosen fixed 40-tree count and assesses final buildings once. Mean outer MSE 0.856796; locked-final MSE 0.715585. Different training sizes and data draws prevent attributing their difference solely to bias. Visual A explicitly encloses inner selection inside outer fitting and keeps final assessment outside. A separate 100-study null experiment considers1/8/64 equal-population-risk predictors, using 40 reused and 200 fresh observations. Mean reused minima1.07015/0.94250/0.86280 improve spuriously while fresh errors1.10167/1.10736/1.10226 stay near the common 1.09 population risk.

## Execution, repairs and figure evidence

All five final notebooks execute in fresh kernels using the unchanged runner; all assertions pass, current outputs have no errors or stderr. The first TabPFN hash assertion preceded native inference preparation; it was moved after an explicitly source-only warm-up and rerun. Explicit median imputation repaired defaults that initially used means in 185 and 187. Manual 186 selection was changed from Brier to log loss to match AutoGluon's declared objective, then rerun. An authoring text edit briefly corrupted the 187 builder tail; recovery from its actual saved notebook preceded fresh186/187 runs. Initial failures and preflight logs are retained locally. An early Torch-enabled preflight produced no result JSON and an empty log; a later shell command's exit does not establish that fit's success. Torch-first native preflight and final laboratory 186 do succeed.

Every current code cell reruns in an isolated exporter process, including the dedicated 3.12 process for 186; deterministic scientific RESULTS match kernel summaries exactly. Resource observations are measured anew and not falsely compared as deterministic results. Eleven SVG/vector-PDF/PNG sets reproduce the experiments. Review corrected wrapped diagram text and long axis labels at book size without changing scientific results. Notebook orientations and chapter prose retain fitted-information boundaries, failed controls, native/original distinctions and limited generated-study claims. Chapters 36–43 and the whole-book audit remain required.
