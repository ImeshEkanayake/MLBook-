# Chapter 29 execution evidence

**Date:** 21 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Task inputs and helpers are internal. Examples151/152 require explicit one-time acquisition and hash verification of two public forecasting checkpoints; ordinary inference then runs offline on CPU. See the [asset guide](CHAPTER_29_ASSETS.md). Actual versions and hardware are printed by every kernel and retained below. Twelve verified pre-cutoff dependencies added; all107prior versions unchanged. Native TimesFM3.0.2/Chronos2.3.2 load explicitly pinned historical checkpoints; no runtime downloads. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_150 | 29.1 | 4 | 2 | 2.533 |
| code_151 | 29.2 | 4 | 2 | 7.059 |
| code_152 | 29.3 | 4 | 2 | 3.137 |
| code_153 | 29.4 | 4 | 2 | 2.604 |
| code_154 | 29.5 | 4 | 2 | 2.492 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

## Models, provenance and controls

Chapter 29 preserves five exact scopes and both visual briefs. Its 150–154 laboratories contain actual shared training, native forecasting, downstream output adaptation, full-weight operator adaptation and numerical validity tests. Original small models are explicitly distinguished from TimesFM, Chronos, Poseidon and Aurora. No absent named checkpoint receives substituted performance.

### Environment and explicit artifacts

The 107 prior installed package versions remain unchanged, including Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and Torch 2.14.1. Twelve pre-cutoff releases were added under the complete prior constraints: TimesFM 3.0.2, chronos-forecasting 2.3.2, Transformers 5.20.1, Accelerate 1.15.0, tokenizers 0.23.3, regex 2026.9.29, typer 0.27.3, annotated-doc 0.0.5, rich 15.0.0, markdown-it-py 4.2.0, mdurl 0.1.2 and shellingham 1.5.4. Release upload evidence is retained locally. The lock now records 119 packages; pip check passes. All neural work is explicit one-thread CPU float32; independent numerical references use float64.

Two ungated historical forecasting checkpoints are acquired explicitly through HF CLI and verified against immutable Hub metadata before offline use. Config, card and safetensors bytes are separately hashed; the manifest and acquisition script retain their contracts. No model weights enter Git.

- Google TimesFM 2.5: repository `google/timesfm-2.5-200m-pytorch`, revision `1d952420fba87f3c6dee4f240de0f1a0fbc790e3`. Weight file 925,181,104 bytes, SHA-256 `2f776efe6245e42b24bc4153ffdf61810140210e4bd3b01fb21f7aa779ab6ce8`. The loaded complete artifact has 231,289,280 parameters, including the head beyond the labelled 200M backbone. Apache-2.0 source/weights; notice retained. Source snapshot `e51928e27119cb17bebc005be2696b75e0a9e688` is 29 September 2026 and already includes TimesFM 3.0. Its separately restricted weights are not acquired or executed; hosted-service permissions are not silently transferred to local weights. The 31 August 2026 primary announcement is separately cited.
- Amazon Chronos-Bolt Tiny: repository `amazon/chronos-bolt-tiny`, revision `a0e552de83495b5c28c14c71c374f3e33280b340`. Weight file 34,622,352 bytes, SHA-256 `75068728d376d2bec670379eeef4bfb4d24c0cfe24d957451f8d19b447030a32`. Actual loaded parameters 8,652,672. Apache-2.0; notice retained. This is direct quantile patch forecasting, not original token-sampling Chronos or multivariate Chronos-2. Source snapshot `1224fafa91e1ecd6674f5204066b159e40b5e4a1`, 5 October 2026, records the distinct releases.

Only151/152 require declared cached files. All task inputs and helpers are internal; ordinary inference sets Hub offline mode, uses local directories and checks every byte hash. A working-directory check supports both fresh kernels in notebooks/ and book figure reproduction from the root without requiring a hidden helper. The first figure-production pass exposed the original notebook-only relative path; it was corrected, and both full native kernels were rerun. Named model imports emit one native Torch distributed-elastic note per native notebook that redirects are unsupported on macOS. These stderr notes remain visible; progress bars alone are disabled. No warning filter suppresses a model advisory. Other notebook stderr is empty.

### Actual experiments and repairs

**150 · shared series pretraining.** Original 6924-parameter patch forecaster: 160 source series, 24 development, 24 familiar final and 24 changed-period final; 64-value contexts, eight-value patches, twelve-step outputs. Eight hundred source windows, 1500 Adam updates at 0.002 and batch32; development selects update700. Whole series define the split. Final origins192/216 remain within each series. Context-only scaling and a horizon-mutation intervention are verified. Familiar MAE: scratch0.76136, frozen0.11202, local ridge AR0.23704, supplied-period seasonal0.14944. Changed periods:0.78497/1.50671/0.23514/0.15830. The severe frozen-model failure remains. A separate33-centre quantization illustration has context reconstruction MAE0.01598 but is not the continuous model's input tokenizer. An introductory description of its embeddings was corrected to match the actual flattened head, then the notebook rerun.

**151 · native families.** Forty-eight generated hourly series:16development and32final, period24, level/scale/drift differences and autocorrelated noise. Each final series has origins192/216/240, context128, horizon12. Fixed native TimesFM2.5/BoltTiny medians use identical admitted history. All local controls were explicitly restricted to the same128observations; calendar features retain absolute clock time. An initial unpublished local control used the longer full history; matching the boundary also required correcting the seasonal slice to local coordinates. Full execution was rerun without changing any native forecasts or tuning final outcomes. Local ridge alpha1; histogram80rounds, rate0.05, leaves7/15, minleaf10, l2=1, no early stopping. Development selects15leaves. Final MAE: seasonal0.189370, AR0.154881, tree0.196702, TimesFM0.168062, Bolt0.148097. Whole-series summaries retain three origins rather than claiming96independent sites. Native middle80coverage0.803819/0.830729, widths0.584283/0.540428. TimesFM's output has auxiliary point plus nine deciles; correct0.1/0.9channels are used. Actual network parameter hashes remain unchanged and a repeated native TimesFM batch matches within1e-6. Native settings use max_context128, compiled output block128, batch8, normalization and continuous quantile head, no sign-flip augmentation or automatic positivity constraint, crossing correction enabled. Bolt uses CPUfloat32 direct quantiles, no target-weight update.

**152 · adaptation.** Two generated domains differ in cadence (hourly/half-hourly) and trend; this is not a causal isolation of cadence. Each has24calibration/8development/8final series. Ten-percent missing-history fixture; forward fill remains inside context, including a disclosed first-observed-value prefix fill. Native frozen Bolt medians feed a ridge residual head using prediction, context-slope extrapolation and lead. Budgets2/8/24whole calibration series correspond24/96/288fitting outcomes. Ninety-six separate development outcomes select alpha0.1/10. Results distinguish budget offered from labels actually used: frozen rows use zero calibration fitting labels, unlike the head and seasonal bias. No native fine-tuning is claimed. Hourly frozen MAE0.154403; head0.159633/0.143298/0.150611. Half-hourly frozen0.364034; head0.599549/0.295307/0.297787; largest-budget seasonal bias0.196652. Harmful low-budget adaptation is preserved. Two thousand paired whole-series bootstrap resamples use only eight final series per domain; wide intervals mostly include zero. Future-horizon mutation leaves admitted imputation unchanged. Actual checkpoint parameter hash is unchanged.

**153 · original scientific operator.** 3474-parameter coefficient-to-complex-multiplier network with nine retained Fourier modes,64periodic nodes,512source/128development cases. Source advection–diffusion–reaction coefficients/time are explicit.1500Adam updates0.002,batch32; source development selects1500. Downstream coefficients lie outside source ranges. Budgets2/8/32cases; warm-start and scratch each receive200updates0.002,16development cases selecting every50updates;64final cases untouched. Frozen relative L2=0.334267. Warm start0.157618/0.063075/0.046384; scratch0.213103/0.093203/0.047779. Equal downstream updates do not equal lifetime learning cost. Adapted mean-law MAE0.002003 and semigroup relative defect0.101283 show that final-field accuracy does not guarantee consistent dynamics. Independent float64 analytic composition and reaction-adjusted mean checks pass1e-12; the half-step reference uses the equation's actual half duration, not an assumed learned law. No Poseidon/Aurora checkpoint was executed.

**154 · validity.** Original four-parameter stencil fitted by least squares across128periodic diffusion cases on32nodes, diffusivity0.01–0.04. Exact source one-step solutions are deliberately biased by+0.001and noiseSD0.0001; the fitted surrogate inherits that evidence. Requested diffusivity0.06, duration0.1, new64/128nodes; explicit diffusion number0.08. At128nodes, raw RMSE1.27142/mean drift1.27123; correctly scaled periodic-mean projection RMSE0.021821/mean error0; invalid old-grid scale RMSE0.136735 despite mean error0. More nodes alone do not fix biased learned dynamics. Periodic native sparse solver versus analytic RMSE decreases0.00026745→0.000066637→0.000016645on64/128/256nodes. Independent256interval Dirichlet reference RMSE0.0000050303. Changed-boundary results: periodic wrapping RMSE0.368529/endpointerror0.651585; zero-endpoint recipe RMSE0.274096/endpointerror0; invalid conserved-mean recipe RMSE0.055784/endpointerror0/meanchange0. The invalid constraint happens to lower scalar error against another biased recipe, but contradicts heat loss. This counterexample is retained rather than tuning it into a simpler story.

### Primary-source and reproduction boundaries

Primary records cover original TimesFM, the pre-cutoff3.0release and historical2.5artifact; original Chronos, Bolt card and Chronos-2; Poseidon report, pinned source and Tiny card; Aurora's21May2025Nature report and official conventions. Poseidon-T metadata is CC BY-NC4.0 and specifies128×128density/two velocities/pressure; only card/configuration were inspected, no weights acquired. Aurora and Poseidon benchmark claims remain author evidence. The original linear PDE operator and stencil are openly identified teaching mechanisms, not reproductions of those scientific checkpoints.

All five notebooks execute independently with four code cells and two inline figures each. All current source cells are rerun by the book figure producer and numeric RESULTS must agree exactly with fresh-kernel summaries. No timing/resource replay exception is used. Elapsed and wall times remain observations outside deterministic results. Actual diagram layouts, numerical assertions, version locks and source assumptions are reviewable. Field validity, universal transfer gains, private-site representativeness and exhaustive estimator API coverage are not asserted.

## Successful result dictionaries

### code_150

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3750.

```json
{
  "changed_series": 24,
  "comparisons": [
    {
      "MAE": 0.761355459690094,
      "cohort": "Source-period family",
      "model": "Scratch shared",
      "origins_per_series": 2,
      "series": 24
    },
    {
      "MAE": 0.11201539635658264,
      "cohort": "Source-period family",
      "model": "Frozen pretrained",
      "origins_per_series": 2,
      "series": 24
    },
    {
      "MAE": 0.23703552478238624,
      "cohort": "Source-period family",
      "model": "Local ridge AR",
      "origins_per_series": 2,
      "series": 24
    },
    {
      "MAE": 0.149443984130509,
      "cohort": "Source-period family",
      "model": "Seasonal repeat",
      "origins_per_series": 2,
      "series": 24
    },
    {
      "MAE": 0.7849719524383545,
      "cohort": "Changed periods",
      "model": "Scratch shared",
      "origins_per_series": 2,
      "series": 24
    },
    {
      "MAE": 1.5067079067230225,
      "cohort": "Changed periods",
      "model": "Frozen pretrained",
      "origins_per_series": 2,
      "series": 24
    },
    {
      "MAE": 0.2351356213895509,
      "cohort": "Changed periods",
      "model": "Local ridge AR",
      "origins_per_series": 2,
      "series": 24
    },
    {
      "MAE": 0.15829645867052022,
      "cohort": "Changed periods",
      "model": "Seasonal repeat",
      "origins_per_series": 2,
      "series": 24
    }
  ],
  "context_quantization_MAE": 0.015978280309354886,
  "development_normalized_MSE": 0.033488526940345764,
  "development_series": 24,
  "final_series": 24,
  "frozen_weights_unchanged": true,
  "future_intervention_max_difference": 0.0,
  "history_length": 64,
  "horizon": 12,
  "learning_rate": 0.002,
  "parameters": 6924,
  "patch_length": 8,
  "pretraining_updates": 1500,
  "selected_update": 700,
  "source_series": 160,
  "source_windows": 800
}
```

### code_151

Versions: `{"accelerate": "1.15.0", "chronos-forecasting": "2.3.2", "matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "timesfm": "3.0.2", "torch": "2.14.1", "transformers": "5.20.1"}`; Darwin arm64 CPU; seed 3751.

```json
{
  "Bolt_input_patch": 16,
  "Bolt_parameters": 8652672,
  "TimesFM_input_patch": 32,
  "TimesFM_total_parameters": 231289280,
  "comparisons": [
    {
      "MAE": 0.1893700369530254,
      "independent_series": 32,
      "median_series_MAE": 0.18833212057749432,
      "model": "Seasonal repeat",
      "origins_per_series": 3
    },
    {
      "MAE": 0.1548809636636671,
      "independent_series": 32,
      "median_series_MAE": 0.15700418841369845,
      "model": "Local ridge AR",
      "origins_per_series": 3
    },
    {
      "MAE": 0.19670160574447298,
      "independent_series": 32,
      "median_series_MAE": 0.1775961353375753,
      "model": "Lagged histogram",
      "origins_per_series": 3
    },
    {
      "MAE": 0.1680622696876526,
      "independent_series": 32,
      "median_series_MAE": 0.16305068135261536,
      "model": "TimesFM2.5 median",
      "origins_per_series": 3
    },
    {
      "MAE": 0.14809709787368774,
      "independent_series": 32,
      "median_series_MAE": 0.15754982829093933,
      "model": "ChronosBoltTiny median",
      "origins_per_series": 3
    }
  ],
  "development_series": 16,
  "final_series": 32,
  "frozen_parameter_hashes_unchanged": true,
  "history": 128,
  "horizon": 12,
  "local_AR_ridge": 1,
  "local_tree_rounds": 80,
  "native_bands": [
    {
      "mean_width": 0.5842829346656799,
      "middle80_coverage": 0.8038194444444444,
      "model": "TimesFM2.5"
    },
    {
      "mean_width": 0.5404284596443176,
      "middle80_coverage": 0.8307291666666666,
      "model": "ChronosBoltTiny"
    }
  ],
  "origins": [
    192,
    216,
    240
  ],
  "selected_tree_leaves": 7,
  "tree_candidates": [
    {
      "MAE": 0.17570223360465023,
      "leaves": 7
    },
    {
      "MAE": 0.1773554862200756,
      "leaves": 15
    }
  ],
  "upstream_task_overlap": "Generated local instances; broader public prior influence is unverified."
}
```

### code_152

Versions: `{"accelerate": "1.15.0", "chronos-forecasting": "2.3.2", "matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1", "transformers": "5.20.1"}`; Darwin arm64 CPU; seed 3752.

```json
{
  "adaptation": "Ridge output residual head; no native checkpoint fine-tuning",
  "budgets": [
    2,
    8,
    24
  ],
  "calibration_series_available": 24,
  "comparisons": [
    {
      "MAE": 0.1544032245874405,
      "cadence_hours": 1.0,
      "calibration_scalar_labels_used": 0,
      "calibration_series_used": 0,
      "domain": "Hourly",
      "final_series": 8,
      "label_budget_series": 2,
      "model": "Frozen Bolt",
      "selection_series": 0
    },
    {
      "MAE": 0.15963274366636243,
      "cadence_hours": 1.0,
      "calibration_scalar_labels_used": 24,
      "calibration_series_used": 2,
      "domain": "Hourly",
      "final_series": 8,
      "label_budget_series": 2,
      "model": "Residual head",
      "selection_series": 8
    },
    {
      "MAE": 0.24993062019348145,
      "cadence_hours": 1.0,
      "calibration_scalar_labels_used": 24,
      "calibration_series_used": 2,
      "domain": "Hourly",
      "final_series": 8,
      "label_budget_series": 2,
      "model": "Seasonal bias",
      "selection_series": 0
    },
    {
      "MAE": 0.1544032245874405,
      "cadence_hours": 1.0,
      "calibration_scalar_labels_used": 0,
      "calibration_series_used": 0,
      "domain": "Hourly",
      "final_series": 8,
      "label_budget_series": 8,
      "model": "Frozen Bolt",
      "selection_series": 0
    },
    {
      "MAE": 0.1432978371744908,
      "cadence_hours": 1.0,
      "calibration_scalar_labels_used": 96,
      "calibration_series_used": 8,
      "domain": "Hourly",
      "final_series": 8,
      "label_budget_series": 8,
      "model": "Residual head",
      "selection_series": 8
    },
    {
      "MAE": 0.1977049857378006,
      "cadence_hours": 1.0,
      "calibration_scalar_labels_used": 96,
      "calibration_series_used": 8,
      "domain": "Hourly",
      "final_series": 8,
      "label_budget_series": 8,
      "model": "Seasonal bias",
      "selection_series": 0
    },
    {
      "MAE": 0.1544032245874405,
      "cadence_hours": 1.0,
      "calibration_scalar_labels_used": 0,
      "calibration_series_used": 0,
      "domain": "Hourly",
      "final_series": 8,
      "label_budget_series": 24,
      "model": "Frozen Bolt",
      "selection_series": 0
    },
    {
      "MAE": 0.15061066375018836,
      "cadence_hours": 1.0,
      "calibration_scalar_labels_used": 288,
      "calibration_series_used": 24,
      "domain": "Hourly",
      "final_series": 8,
      "label_budget_series": 24,
      "model": "Residual head",
      "selection_series": 8
    },
    {
      "MAE": 0.18303506076335907,
      "cadence_hours": 1.0,
      "calibration_scalar_labels_used": 288,
      "calibration_series_used": 24,
      "domain": "Hourly",
      "final_series": 8,
      "label_budget_series": 24,
      "model": "Seasonal bias",
      "selection_series": 0
    },
    {
      "MAE": 0.36403390765190125,
      "cadence_hours": 0.5,
      "calibration_scalar_labels_used": 0,
      "calibration_series_used": 0,
      "domain": "Half-hourly",
      "final_series": 8,
      "label_budget_series": 2,
      "model": "Frozen Bolt",
      "selection_series": 0
    },
    {
      "MAE": 0.5995490254009584,
      "cadence_hours": 0.5,
      "calibration_scalar_labels_used": 24,
      "calibration_series_used": 2,
      "domain": "Half-hourly",
      "final_series": 8,
      "label_budget_series": 2,
      "model": "Residual head",
      "selection_series": 8
    },
    {
      "MAE": 0.22673197090625763,
      "cadence_hours": 0.5,
      "calibration_scalar_labels_used": 24,
      "calibration_series_used": 2,
      "domain": "Half-hourly",
      "final_series": 8,
      "label_budget_series": 2,
      "model": "Seasonal bias",
      "selection_series": 0
    },
    {
      "MAE": 0.36403390765190125,
      "cadence_hours": 0.5,
      "calibration_scalar_labels_used": 0,
      "calibration_series_used": 0,
      "domain": "Half-hourly",
      "final_series": 8,
      "label_budget_series": 8,
      "model": "Frozen Bolt",
      "selection_series": 0
    },
    {
      "MAE": 0.2953074581418415,
      "cadence_hours": 0.5,
      "calibration_scalar_labels_used": 96,
      "calibration_series_used": 8,
      "domain": "Half-hourly",
      "final_series": 8,
      "label_budget_series": 8,
      "model": "Residual head",
      "selection_series": 8
    },
    {
      "MAE": 0.20792584121227264,
      "cadence_hours": 0.5,
      "calibration_scalar_labels_used": 96,
      "calibration_series_used": 8,
      "domain": "Half-hourly",
      "final_series": 8,
      "label_budget_series": 8,
      "model": "Seasonal bias",
      "selection_series": 0
    },
    {
      "MAE": 0.36403390765190125,
      "cadence_hours": 0.5,
      "calibration_scalar_labels_used": 0,
      "calibration_series_used": 0,
      "domain": "Half-hourly",
      "final_series": 8,
      "label_budget_series": 24,
      "model": "Frozen Bolt",
      "selection_series": 0
    },
    {
      "MAE": 0.29778743270188696,
      "cadence_hours": 0.5,
      "calibration_scalar_labels_used": 288,
      "calibration_series_used": 24,
      "domain": "Half-hourly",
      "final_series": 8,
      "label_budget_series": 24,
      "model": "Residual head",
      "selection_series": 8
    },
    {
      "MAE": 0.19665157794952393,
      "cadence_hours": 0.5,
      "calibration_scalar_labels_used": 288,
      "calibration_series_used": 24,
      "domain": "Half-hourly",
      "final_series": 8,
      "label_budget_series": 24,
      "model": "Seasonal bias",
      "selection_series": 0
    }
  ],
  "context": 128,
  "development_series": 8,
  "domains": 2,
  "final_series": 8,
  "frozen_checkpoint_unchanged": true,
  "future_imputation_intervention_difference": 0.0,
  "horizon": 12,
  "missing_probability": 0.1,
  "paired_assessments": [
    {
      "budget": 2,
      "development_MAE": 0.152272009609827,
      "domain": "Hourly",
      "paired_final_MAE_difference": 0.005229506971728462,
      "ridge_strength": 10,
      "series_bootstrap95": [
        -0.02475415623196222,
        0.03922457063493097
      ]
    },
    {
      "budget": 8,
      "development_MAE": 0.15034841577358524,
      "domain": "Hourly",
      "paired_final_MAE_difference": -0.011105399520143165,
      "ridge_strength": 10,
      "series_bootstrap95": [
        -0.02908919141594877,
        0.00544250246641572
      ]
    },
    {
      "budget": 24,
      "development_MAE": 0.14804051092411294,
      "domain": "Hourly",
      "paired_final_MAE_difference": -0.0037925729444455904,
      "ridge_strength": 0.1,
      "series_bootstrap95": [
        -0.01034481769670343,
        0.0029318808907361433
      ]
    },
    {
      "budget": 2,
      "development_MAE": 0.5274458255113218,
      "domain": "Half-hourly",
      "paired_final_MAE_difference": 0.23551512706228298,
      "ridge_strength": 10,
      "series_bootstrap95": [
        0.002015021807076174,
        0.4472474500746802
      ]
    },
    {
      "budget": 8,
      "development_MAE": 0.2343747360190437,
      "domain": "Half-hourly",
      "paired_final_MAE_difference": -0.06872644019683397,
      "ridge_strength": 10,
      "series_bootstrap95": [
        -0.23683461456201207,
        0.12395276449502217
      ]
    },
    {
      "budget": 24,
      "development_MAE": 0.23460425282560238,
      "domain": "Half-hourly",
      "paired_final_MAE_difference": -0.06624646563678856,
      "ridge_strength": 0.1,
      "series_bootstrap95": [
        -0.2110229469757315,
        0.07778506198139762
      ]
    }
  ],
  "ridge_candidates": [
    0.1,
    10
  ],
  "series_per_domain": 40
}
```

### code_153

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3753.

```json
{
  "adaptation": [
    {
      "development_cases": 16,
      "development_relative_L2": 0.18925276398658752,
      "downstream_cases": 2,
      "final_relative_L2": 0.1576175093650818,
      "route": "Warm start",
      "selected_update": 200
    },
    {
      "development_cases": 16,
      "development_relative_L2": 0.2331567406654358,
      "downstream_cases": 2,
      "final_relative_L2": 0.2131032943725586,
      "route": "Scratch",
      "selected_update": 100
    },
    {
      "development_cases": 16,
      "development_relative_L2": 0.06301914155483246,
      "downstream_cases": 8,
      "final_relative_L2": 0.06307488679885864,
      "route": "Warm start",
      "selected_update": 200
    },
    {
      "development_cases": 16,
      "development_relative_L2": 0.08807773143053055,
      "downstream_cases": 8,
      "final_relative_L2": 0.0932026132941246,
      "route": "Scratch",
      "selected_update": 200
    },
    {
      "development_cases": 16,
      "development_relative_L2": 0.05338579788804054,
      "downstream_cases": 32,
      "final_relative_L2": 0.046384431421756744,
      "route": "Warm start",
      "selected_update": 200
    },
    {
      "development_cases": 16,
      "development_relative_L2": 0.05290031433105469,
      "downstream_cases": 32,
      "final_relative_L2": 0.04777868092060089,
      "route": "Scratch",
      "selected_update": 200
    }
  ],
  "adapted_mean_law_MAE": 0.002003015950322151,
  "adapted_semigroup_relative_defect": 0.101282998919487,
  "downstream_available_cases": 32,
  "downstream_development_cases": 16,
  "final_cases": 64,
  "fit_budgets": [
    {
      "budget": 2,
      "learning_rate": 0.002,
      "optimizer_updates": 200,
      "route": "Warm start"
    },
    {
      "budget": 2,
      "learning_rate": 0.002,
      "optimizer_updates": 200,
      "route": "Scratch"
    },
    {
      "budget": 8,
      "learning_rate": 0.002,
      "optimizer_updates": 200,
      "route": "Warm start"
    },
    {
      "budget": 8,
      "learning_rate": 0.002,
      "optimizer_updates": 200,
      "route": "Scratch"
    },
    {
      "budget": 32,
      "learning_rate": 0.002,
      "optimizer_updates": 200,
      "route": "Warm start"
    },
    {
      "budget": 32,
      "learning_rate": 0.002,
      "optimizer_updates": 200,
      "route": "Scratch"
    }
  ],
  "frozen_final_relative_L2": 0.3342665433883667,
  "grid_points": 64,
  "named_scientific_checkpoint_executed": false,
  "parameters": 3474,
  "pretraining_updates": 1500,
  "retained_modes": 9,
  "selected_pretraining_update": 1500,
  "source_cases": 512,
  "source_development_MSE": 0.0005411769379861653,
  "source_development_cases": 128
}
```

### code_154

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3754.

```json
{
  "boundary_comparisons": [
    {
      "RMSE": 0.368528758186009,
      "max_endpoint_error": 0.6515852716998055,
      "mean_change": 0.3039554476756675,
      "recipe": "Periodic wrap reused"
    },
    {
      "RMSE": 0.2740959144863247,
      "max_endpoint_error": 0.0,
      "mean_change": 0.20996183345334984,
      "recipe": "Dirichlet endpoints"
    },
    {
      "RMSE": 0.055784093750348804,
      "max_endpoint_error": 0.0,
      "mean_change": 0.0,
      "recipe": "Invalid conserved mean"
    }
  ],
  "dirichlet_reference_RMSE": 5.030320219844247e-06,
  "learned_intercept": 0.011796565825540823,
  "learned_parameters": 4,
  "learned_stencil": [
    1.0229674967968165,
    -2.0453392155829833,
    1.0230690207137314
  ],
  "named_scientific_checkpoint_executed": false,
  "new_mesh_comparisons": [
    {
      "RMSE": 0.3097123758334309,
      "grid": 64,
      "mean_error": 0.30968663319515555,
      "recipe": "Raw reuse",
      "steps": 308
    },
    {
      "RMSE": 0.003993114653683824,
      "grid": 64,
      "mean_error": 0.0,
      "recipe": "Periodic mean projection",
      "steps": 308
    },
    {
      "RMSE": 0.09342229719579076,
      "grid": 64,
      "mean_error": 0.0,
      "recipe": "Invalid old grid scale",
      "steps": 308
    },
    {
      "RMSE": 1.2714212684902457,
      "grid": 128,
      "mean_error": 1.2712340078367719,
      "recipe": "Raw reuse",
      "steps": 1229
    },
    {
      "RMSE": 0.02182061613711326,
      "grid": 128,
      "mean_error": 0.0,
      "recipe": "Periodic mean projection",
      "steps": 1229
    },
    {
      "RMSE": 0.13673450008878818,
      "grid": 128,
      "mean_error": 0.0,
      "recipe": "Invalid old grid scale",
      "steps": 1229
    }
  ],
  "periodic_reference_refinement": [
    {
      "grid": 64,
      "native_vs_analytic_RMSE": 0.0002674506214629621
    },
    {
      "grid": 128,
      "native_vs_analytic_RMSE": 6.66367384971822e-05
    },
    {
      "grid": 256,
      "native_vs_analytic_RMSE": 1.664506521630154e-05
    }
  ],
  "physical_duration": 0.1,
  "source_cases": 128,
  "source_diffusivity_range": [
    0.01,
    0.04
  ],
  "source_grid": 32,
  "source_observation_bias": 0.001,
  "source_observation_noise_sd": 0.0001,
  "target_diffusivity": 0.06
}
```

