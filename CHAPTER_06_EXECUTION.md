# Chapter 6 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** all five published and executed; remote tree verified.

All code cells ran in order in fresh kernels using the unchanged runner. The five jobs ran concurrently; wall times include kernel lifecycle and are observations, not performance guarantees. No dependency was added. Each notebook printed CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0 and scikit-learn 1.9.0 on Darwin arm64 CPU. Every import, helper and generated input is inside its notebook; ordinary execution needs no files, downloads, keys or GPU. Requirements and their lock remain unchanged.

| Example | Section | Code cells | Inline figures | Wall seconds incl. kernel |
| --- | --- | ---: | ---: | ---: |
| [code_027](CODE_EXAMPLES.md#code_027) | 6.1 | 5 | 2 | 1.726 |
| [code_028](CODE_EXAMPLES.md#code_028) | 6.2 | 5 | 2 | 2.019 |
| [code_029](CODE_EXAMPLES.md#code_029) | 6.3 | 7 | 2 | 1.768 |
| [code_030](CODE_EXAMPLES.md#code_030) | 6.4 | 7 | 2 | 1.651 |
| [code_031](CODE_EXAMPLES.md#code_031) | 6.5 | 6 | 2 | 1.705 |

Total: **30 executed code cells and ten inline figures**, with fixed seeds 627–631. All assertions passed. The final summary in each executed notebook contains versions, hardware, actual metrics and elapsed time.

## Actual results and meaningful checks

- **code_027:** label availability excludes twelve day-6 pending labels at the day-3 training cutoff, leaving 348 eligible training members. A day-1 report is unavailable for day-0 prediction even though it exists at training time. Training-only scaler state and disjoint 120-member development/final samples are checked. Final scalar regression RMSE is .0786144164 mm versus .4200415494 mm for a training-mean baseline; finding log loss is .6637549140 versus .6948490363; root mean squared Euclidean vector error is .0566691403 mm versus .3955109882 mm. Output-specific metrics are not ranked across meanings.
- **code_028:** K-means and GMM fit 480 training snapshots without regime or finding labels. Actual nonlinear bottleneck autoencoder training decreases half reconstruction MSE 1.463101291 to .063521978 in standardized reference units squared, with a finite-difference derivative check. Final reconstruction is .058889684 versus 1.556668653 for training-mean reconstruction. External final regime ARI is 1, while independent finding ARI is -.005031800. The grouping does not imply damage meaning. Final mean log density is -1.607569710 and a constructed far-out query has -1166.316639339 in fixed coordinates; this is not a calibrated anomaly decision.
- **code_029:** actual masked source pretraining decreases fixed-mask probe half MSE .506396559 to .127736970. Hidden values are zeroed and mask indicators appended. Paired-view contrastive loss is 2.283481609, while collapsed embeddings give log(48)=3.871201011 exactly; this is objective evaluation using a masked-pretrained encoder, not a contrastively trained encoder. Forty human labels fit a frozen-feature head, a copied encoder/head undergo actual fine-tuning, and 38 training-only pseudo-labels enter a one-pass weighted student. Small-noise probability consistency MSE is 1.8015e-5 and is measured rather than silently optimized as a penalty. Final log losses frozen/fine-tuned/semi-supervised are .551920084/.574939897/.561544917; added adaptation does not improve this sample. A matched scratch comparison is absent, so no pretraining benefit is claimed. Development/final inputs do not enter pretraining.
- **code_030:** 80 source tasks fit a pooled line and actual shared-slope/per-task-intercept rule. An exact linear MAML meta-gradient passes finite differences; the source post-one-step query objective decreases .487593863 to .194758138 mm² under half-squared normalization. A contextual RBF bandwidth is actually pretrained to .270104461, decreasing source query objective .183462333 to .042612664 mm². Shifting every context label by one shifts predictions by one with unchanged learned bandwidth. On 80 independent final tasks, frozen/100-support-updates/meta-one-step/fixed-context query MSE is .602436583/.011478926/.405218475/.105537531 mm². These contracts have different budgets, so this is not an algorithm leaderboard. A separate reversed-slope stress task exposes an inappropriate frozen source rule without claiming a matched negative-transfer benchmark.
- **code_031:** the actual epsilon-greedy contextual bandit collects state-action counts [[1901,123],[100,1876]] and learns policy [0,1]. Independent frozen-policy simulator mean reward is .648855268 versus .089500635/.352261879 for constant-action baselines. Invented utilities are not field inspection costs. A constructed offline log has counts [[98,0],[102,0]], exposing missing action-1 evidence. A separate explicitly known three-state model is solved by planning in 218 iterations, policy [0,1,1], with Bellman discrepancy 8.41e-11. This is not a learned transition model. The four-axis transformer/offline-policy card is an explicit illustrative worksheet; no transformer or offline policy is trained.

## Information and interpretation boundaries

Eligible external labels, data-derived targets, unlabelled training inputs, source-task support/query labels and selected reward feedback have different provenance. Training-only preprocessing and state inventories are checked. Source query labels train the meta/context mechanisms and are not confused with final tasks. Final targets/rewards are accessed only after the declared rules are fixed; subsequent redesign needs genuinely fresh assessment. Masking history does not authorize future measurements, and absent labels/actions are not negative or zero-reward outcomes.

Unsupervised grouping, density and reconstruction have independent objectives and require external usefulness checks. Self-supervision names target construction; semi-supervision combines external labels with unlabelled examples. Frozen features, fine-tuning, multitask heads, meta-initializations and fixed contextual inference change distinct state. A matching loss, equilibrium/Bellman residual or accepted output shape does not establish engineering validity, causal policy benefit or model-family superiority.

All ten inline figures are visually reviewed with textual explanations, units/scales and grayscale styles or markers. Five selected experiment plots are rerun as vector book figures and compared against exact executed result dictionaries; two additional original diagrams show the learning-evidence map and four-axis worksheet. Notebook schemas, sequential execution, no-error outputs, meaningful assertions, self-contained code, local guide anchors and manifest/summary agreement pass scripts/check_chapter06.py. All 26 prior notebooks and manifest records remain unchanged. Only companion artifacts are published, not manuscript or outline.

## Full recorded result dictionaries

These values are copied from the actual fresh-kernel summaries, rather than manually rounded figure labels.

### code_027

```json
{
  "eligible_training_labels": 348,
  "finding_baseline_log_loss": 0.6948490362764715,
  "finding_log_loss": 0.6637549140005726,
  "regression_RMSE_mm": 0.07861441637108232,
  "regression_baseline_RMSE_mm": 0.4200415493552509,
  "vector_RMSE_mm": 0.05666914032888592,
  "vector_baseline_RMSE_mm": 0.3955109881694723
}
```

### code_028

```json
{
  "far_query_log_density": -1166.3166393389438,
  "final_finding_ARI": -0.0050318003708739924,
  "final_half_reconstruction_MSE": 0.05888968402887595,
  "final_mean_log_density": -1.6075697099218778,
  "final_regime_ARI": 1.0,
  "mean_baseline_half_MSE": 1.5566686529077935,
  "training_reconstruction_initial_final": [
    1.4631012907940226,
    0.06352197791931974
  ]
}
```

### code_029

```json
{
  "contrastive_paired_collapsed": [
    2.283481609413014,
    3.871201010907892
  ],
  "embedding_consistency_distance": 0.00953347399825087,
  "final_binary_log_loss": {
    "fine_tuned": 0.5749398969854592,
    "frozen_features": 0.5519200844744722,
    "semi_supervised": 0.5615449171425718
  },
  "masked_probe_initial_final": [
    0.5063965593030453,
    0.12773696963384054
  ],
  "pseudo_labels_selected": 38,
  "teacher_prediction_consistency_MSE": 1.8015000452831338e-05
}
```

### code_030

```json
{
  "context_bandwidth": 0.2701044608492857,
  "context_initial_final_query_half_MSE_mm2": [
    0.1834623332332446,
    0.04261266438929887
  ],
  "final_task_query_MSE_mm2": {
    "fine_tuned_100_steps": 0.011478926460447424,
    "fixed_context_rule": 0.10553753109783251,
    "frozen_pooled": 0.6024365830430506,
    "meta_one_step": 0.4052184751614849
  },
  "meta_initial_final_query_half_MSE_mm2": [
    0.4875938633485949,
    0.19475813841148545
  ],
  "meta_initialization_mm": [
    1.4006001034919817,
    0.09372836756245555
  ],
  "multitask_shared_slope_mm": 1.3824100189944408,
  "pooled_coefficients_mm": [
    1.3088663473498994,
    0.10949298282517456
  ],
  "shift_task_support_MSE_frozen_updated_mm2": [
    4.062983570352172,
    1.4613466650549993e-05
  ]
}
```

### code_031

```json
{
  "Bellman_residual": 8.410161456140486e-11,
  "final_mean_reward": {
    "always_0": 0.08950063502811335,
    "always_1": 0.3522618793414959,
    "learned": 0.6488552676455762
  },
  "learned_policy": [
    0,
    1
  ],
  "learned_reward_means": [
    [
      0.6984046863215989,
      0.11091538448684315
    ],
    [
      -0.5406262221498795,
      0.6019262700330681
    ]
  ],
  "offline_logged_action_counts": [
    [
      98,
      0
    ],
    [
      102,
      0
    ]
  ],
  "planning_iterations": 218,
  "planning_policy": [
    0,
    1,
    1
  ],
  "taxonomy_axes": [
    "architecture",
    "objective",
    "adaptation",
    "task"
  ],
  "training_action_counts": [
    [
      1901,
      123
    ],
    [
      100,
      1876
    ]
  ],
  "transformer_worksheet_only": true
}
```

## Publication evidence

First published content commit: [f1616f36db5ab4bc439b853536d3b7990f8f7e75](https://github.com/ImeshEkanayake/MLBook-/commit/f1616f36db5ab4bc439b853536d3b7990f8f7e75). All 57 remote tracked file blobs matched the local commit tree, including all five executed notebooks and their registry, manifest, guide, evidence and checker. The following metadata commit records this verification. The manuscript handoff records final branch/tree and raw-file comparisons.
