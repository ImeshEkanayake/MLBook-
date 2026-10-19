# Chapter 11: Choosing preprocessing steps — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_11_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 11.1 · Preprocessing as a learned pipeline

- [Declare the fitting boundary before transforming](notebooks/052_Chapter_11_01_Fold_Fitting_And_Stored_State.ipynb#boundary)
- [Trace fit and transform arrows separately](notebooks/052_Chapter_11_01_Fold_Fitting_And_Stored_State.ipynb#diagram)
- [Keep state fixed across prediction batches](notebooks/052_Chapter_11_01_Fold_Fitting_And_Stored_State.ipynb#inference)

Declared mechanisms: deterministic validation versus learned transforms, fold-only imputation and scaling, paired leakage audit, stored state and batch-invariant inference.

```bash
python scripts/run_notebook.py notebooks/052_Chapter_11_01_Fold_Fitting_And_Stored_State.ipynb
```

## 11.2 · Scaling and numerical conditioning

- [The same physical dataset in two unit systems](notebooks/053_Chapter_11_02_Scaling_Distance_And_Penalties.ipynb#units)
- [Inspect geometry, not only a model score](notebooks/053_Chapter_11_02_Scaling_Distance_And_Penalties.ipynb#geometry)

Declared mechanisms: unit conversion versus learned scaling, distance and ridge penalty geometry, standard robust and row normalization, model-dependent sensitivity and conditioning.

```bash
python scripts/run_notebook.py notebooks/053_Chapter_11_02_Scaling_Distance_And_Penalties.ipynb
```

## 11.3 · Encoding categories and unknown values

- [An integer category code does not supply a physical distance](notebooks/054_Chapter_11_03_Categories_And_Cross_Fitted_Targets.ipynb#vocabulary)
- [Hold whole buildings out of target statistics](notebooks/054_Chapter_11_03_Categories_And_Cross_Fitted_Targets.ipynb#crossfit)
- [Expose the limiting high-cardinality failure](notebooks/054_Chapter_11_03_Categories_And_Cross_Fitted_Targets.ipynb#singleton)

Declared mechanisms: one-hot unknown handling and ordinal assumptions, group-aware target cross-fitting, high-cardinality identifiers and leakage, encoding compatibility and learned embeddings.

```bash
python scripts/run_notebook.py notebooks/054_Chapter_11_03_Categories_And_Cross_Fitted_Targets.ipynb
```

## 11.4 · Imputation and internal missing-value handling

- [A controlled missingness shift with unchanged reference targets](notebooks/055_Chapter_11_04_Imputation_And_Native_Routes.ipynb#mechanism)
- [Assess frozen procedures on each regime](notebooks/055_Chapter_11_04_Imputation_And_Native_Routes.ipynb#assessment)

Declared mechanisms: simple and conditional imputation, posterior-draw predictive averaging, native tree missing-value routes, same-cohort missingness-shift assessment.

```bash
python scripts/run_notebook.py notebooks/055_Chapter_11_04_Imputation_And_Native_Routes.ipynb
```

## 11.5 · Transformations and model input contracts

- [Positive loads and the objective after transformation](notebooks/056_Chapter_11_05_Target_Transforms_And_Input_Contracts.ipynb#target)
- [Fit clipping and power-transform parameters only in training](notebooks/056_Chapter_11_05_Target_Transforms_And_Input_Contracts.ipynb#schema)
- [A documentary contract review is different from executing a foundation model](notebooks/056_Chapter_11_05_Target_Transforms_And_Input_Contracts.ipynb#contracts)

Declared mechanisms: log-target estimands and inverse-transform bias, training-residual smearing and original-unit scoring, clipping and power-transform state, release-pinned documentary input contract.

```bash
python scripts/run_notebook.py notebooks/056_Chapter_11_05_Target_Transforms_And_Input_Contracts.ipynb
```

## Interpretation and boundaries

All five numerical laboratories execute successfully in fresh kernels. The generator creates every numerical input locally; the foundation-model branch is an explicitly labeled documentary review and contributes no downloaded inputs or runtime predictions. A static syntax check caught an unterminated multiline diagram-label string in the initial code_056 source before its first kernel execution; the builder was corrected to construct line breaks explicitly. There were no failed reference kernel runs. All controls, information roles and limitations are retained in the notebooks.

The fold experiment uses 160 independent members, two inputs, 20% first-input dropout and a deliberately broad final block. Identical four-block validation and five-neighbor controls give mean squared error 9.956478941 mm² for fold-only imputation/scaling versus 10.557481933 for invalid all-input statistics. The invalid procedure is worse; score direction does not legalize leakage. Fold statistics match explicit training-only calculations, the independent pipeline CV call agrees, and a three-request batching check preserves predictions and stored state. This is a diagnostic boundary example, not a final performance estimate.

The scaling experiment uses 550 members and 300/100/150 roles, with the same physical data represented in kN or N. All model/transform candidates are predeclared: five neighbors, Ridge alpha=10, histogram boosting 80 iterations/seven leaves/minimum leaf 15/learning rate .1/no early stopping. Standard and robust column scaling preserve predictions under the unit conversion. Raw neighbor final MSE changes .143780387 to .192088485; standardized MSE is .016884561. Tree raw/standard/robust MSE coincides at .013526792. Raw ridge .010324980 slightly beats standardized .010527788, despite centered Gram condition numbers 813017630.861 versus 1.239890. Row normalization changes magnitude/geometry and is poor here; no universal scaling recommendation follows. Robust scaling is not tested under a contamination claim.

The encoding audit preserves an explicit three-category vocabulary, all-zero one-hot unknown fallback and ordinal unknown -1. Seventy-five buildings with six members each split by 50/10/15 buildings. Scikit-learn 1.9.0 TargetEncoder accepts explicit GroupKFold iterable folds, continuous targets and fixed smoothing 5. Training cross-fitted versus invalid same-building MSE is .463718499/.064653842; final new-building MSE is .979827643/1.017786639. New IDs fall back to 2.241868165 mm. Perturbing an entire held-out fold's labels leaves its cross-fitted representation unchanged. Eight singleton IDs expose exact unsmoothed same-row target recovery versus lawful other-fold means. Learned embeddings are explained conceptually, not claimed as an implemented network.

The missingness experiment preserves 450/150/200 member roles. Correlated inputs and a nonlinear target use one training/development acquisition mechanism; identical final reference members receive matched and reversed-dependence masks. Missing fractions are .415556 training, .395 matched and .425 shifted. Matched/shifted final MSE is .756603999/.854855265 for median-indicator Ridge, .581625356/.569484072 for KNN-imputed Ridge, .713605227/.678037783 for a five posterior-draw iterative-imputation mean, .673091982/.682731542 for native histogram boosting and .723850069/.773057954 for median-indicator boosting. All fitting is training-only. The two tree routes share controls; linear/tree comparisons also change family. Posterior imputers use BayesianRidge with ten iterations and separate seeds; reported spread is imputation sensitivity, not Rubin-pooled inference or calibrated predictive uncertainty. The transform draw sequence is explicitly stochastic. A changed acquisition process does not worsen every method on this cohort.

Positive load targets use the declared lognormal mechanism, 350/100/200 roles and three fixed raw/log/smearing fits. Final raw/exp-log/smearing MSE is 42.789361012/43.502081607/41.308347106 kN²; MAE is 4.413402017/4.073622155/4.283623476 kN. Objectives differ. The training smearing factor is 1.184698059 versus the mechanism's mean/median ratio 1.197217363. Yeo–Johnson input parameters fit training only, inverse reconstruction passes, and six final inputs meet learned clipping limits [-.972892215,.965682990]. Wrong unit, infinity and nonpositive log-target fixtures are rejected. No predictive benefit is claimed for clipping/power shape alone.

The foundation input branch records a primary maintainer README at PriorLabs/TabPFN commit `417c9877dbfe657afdbe0aee70af2a05ffe4abba`, inspected 19 October 2026. It documents default TabPFN-3.5, missing-value support and advice against generic external scaling/one-hot conversion. This is a pinned document review, not a foundation-model execution, acceptance test or accuracy benchmark. No checkpoint is downloaded or dependency installed. Earlier-release search results were not treated as the current contract. A tagged v2 landing-page attempt and a documentation-installation URL were unavailable; the immutable primary README was retrieved and inspected instead.

The chapter implements both agreed visual briefs with a fold fit/transform diagram and a model-dependent input-contract diagram, plus four numerical figures. Five numbered equations derive composition, metric/penalty geometry, smoothed encoding and lognormal output meanings. The primary/official source references distinguish live maintenance documentation from the executed 1.9.0 environment. No dependency was added.

The first chapter-checker pass exposed an inherited literal-assert count that ignored numerical NumPy assertion calls. The checker now recognizes both forms. Code_055 also gained explicit pairwise role-separation and training-median audits and was re-executed successfully; all result dictionaries remain unchanged and timings reflect current sources.
