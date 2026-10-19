# Chapter 9: concept-to-code guide

Permanent IDs code_042–code_046 correspond to sections 9.1–9.5. Restart and run all cells; imports, helpers and synthetic inputs are inside each notebook. Ordinary runs need no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_09_EXECUTION.md).

These are scoped exploration laboratories. The final laboratory alone fits competing predictive models; earlier OLS slopes are descriptive summaries. The hypothesis comparison uses training-only fits, development selection and one independent final building cohort. No causal, field-reliability or exhaustive estimator API claim follows.

## 9.1 · Distributions, scale and support

- [support](notebooks/042_Chapter_09_01_Distributions_Scale_And_Support.ipynb#support): Physical/observed support, raw source units, real zeros and separate review fixtures.
- [distributions](notebooks/042_Chapter_09_01_Distributions_Scale_And_Support.ipynb#distributions): Pooled/material distributions on common bins with counts and units.
- [transforms](notebooks/042_Chapter_09_01_Distributions_Scale_And_Support.ipynb#transforms): ECDFs, logarithm domains, physical references and unobserved categories.
- [exercises](notebooks/042_Chapter_09_01_Distributions_Scale_And_Support.ipynb#exercises): Bin choices, source review, signed forces and reference scales.

```bash
python scripts/run_notebook.py notebooks/042_Chapter_09_01_Distributions_Scale_And_Support.ipynb
```

## 9.2 · Dependencies and confounding patterns

- [conditional](notebooks/043_Chapter_09_02_Dependencies_And_Confounding.ipynb#conditional): Pooled positive slope beside negative material-specific slopes and unsupported age gaps.
- [decomposition](notebooks/043_Chapter_09_02_Dependencies_And_Confounding.ipynb#decomposition): Exact within/between covariance identity and redundant age units.
- [nonlinear](notebooks/043_Chapter_09_02_Dependencies_And_Confounding.ipynb#nonlinear): Symmetric square with zero correlation but exact dependence, contrasted with a monotone exponential.
- [exercises](notebooks/043_Chapter_09_02_Dependencies_And_Confounding.ipynb#exercises): Group mixture, conditional support, measurement offsets and leakage.

```bash
python scripts/run_notebook.py notebooks/043_Chapter_09_02_Dependencies_And_Confounding.ipynb
```

## 9.3 · Subgroups, rare cases and coverage

- [counts](notebooks/044_Chapter_09_03_Subgroups_Rare_Cases_And_Coverage.ipynb#counts): Distinct cohort prevalence and miss-rate denominators across prespecified groups.
- [intervals](notebooks/044_Chapter_09_03_Subgroups_Rare_Cases_And_Coverage.ipynb#intervals): Actual Wilson intervals and a separate zero-of-six counterexample.
- [coverage](notebooks/044_Chapter_09_03_Subgroups_Rare_Cases_And_Coverage.ipynb#coverage): Invalid row duplication narrows an interval without new independent structures.
- [exercises](notebooks/044_Chapter_09_03_Subgroups_Rare_Cases_And_Coverage.ipynb#exercises): Decision consequences, unknown labels, group weights and acquisition questions.

```bash
python scripts/run_notebook.py notebooks/044_Chapter_09_03_Subgroups_Rare_Cases_And_Coverage.ipynb
```

## 9.4 · Temporal, spatial and relational patterns

- [time](notebooks/045_Chapter_09_04_Temporal_Spatial_And_Relational_Patterns.ipynb#time): Generated cycle plus stationary AR residual and specified sample ACF.
- [scales](notebooks/045_Chapter_09_04_Temporal_Spatial_And_Relational_Patterns.ipynb#scales): Spatial covariance, nearby sensor correlations, physical components and cross-split edges.
- [independent](notebooks/045_Chapter_09_04_Temporal_Spatial_And_Relational_Patterns.ipynb#independent): Derived cluster mean variance and a 3,000-dataset Monte Carlo check.
- [exercises](notebooks/045_Chapter_09_04_Temporal_Spatial_And_Relational_Patterns.ipynb#exercises): Cycle removal, dependence scales, components and extra readings versus buildings.

```bash
python scripts/run_notebook.py notebooks/045_Chapter_09_04_Temporal_Spatial_And_Relational_Patterns.ipynb
```

## 9.5 · Exploration as a recorded hypothesis process

- [contract](notebooks/046_Chapter_09_05_Recorded_Hypotheses_And_Confirmation.ipynb#contract): Whole-building roles, training-only OLS and two disclosed candidate procedures.
- [ledger](notebooks/046_Chapter_09_05_Recorded_Hypotheses_And_Confirmation.ipynb#ledger): Development residual pattern, alternative explanations and frozen selection.
- [final](notebooks/046_Chapter_09_05_Recorded_Hypotheses_And_Confirmation.ipynb#final): One paired final building assessment, all gains and a 2,000-replicate bootstrap.
- [exercises](notebooks/046_Chapter_09_05_Recorded_Hypotheses_And_Confirmation.ipynb#exercises): Null results, extra search, fresh final cohorts and causal interpretation limits.

```bash
python scripts/run_notebook.py notebooks/046_Chapter_09_05_Recorded_Hypotheses_And_Confirmation.ipynb
```

## Controls and questions

| Laboratory | Disclosed control | Predict before changing it |
| --- | --- | --- |
| Support | Common 20-kN bins, physical unit conversion, logarithm reference | Does the change preserve units, zeros and represented cases? |
| Association | Material proportions/ranges, conditional slope, nonlinear shape | Can pooling reverse a trend or zero correlation hide dependence? |
| Subgroups | Independent denominators, prespecified slices, 95% Wilson method | Does the interval reflect structures or repeated rows? |
| Dependence | AR phi .75, 24-day cycle, spatial length 1.2 m, cluster rho .8 | Which estimator and deployment question determine effective evidence? |
| Hypotheses | Two OLS feature sets, 72/24/24 buildings, fixed .005 mm² threshold | Does a positive mean gain establish precision or improve every building? |

Observed support is not physical support. Unit review differs from outlier deletion. Conditional association is not causal identification. Subgroup prevalence, conditional miss probability, zero events and no denominator have different meanings. Effective sample size is specific to the estimator and dependence assumptions. A recorded hypothesis does not erase development adaptivity; redesign after the final check requires new final evidence.
