# Chapter 22 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_108 | 22.1 | 4 | 2 | 3.985 |
| code_109 | 22.2 | 4 | 2 | 4.404 |
| code_110 | 22.3 | 4 | 2 | 2.856 |
| code_111 | 22.4 | 4 | 2 | 3.231 |
| code_112 | 22.5 | 5 | 2 | 21.375 |
| code_113 | 22.6 | 4 | 2 | 2.442 |
| code_114 | 22.7 | 4 | 2 | 3.789 |

Total: **29 executed code cells and 14 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

# Chapter 22 mechanisms, evidence and boundaries

Seven independently executable CPU notebooks use generated records with explicit building/machine or episode boundaries. Actual Torch operations implement the neural mechanisms; named full research systems are comparison context, not falsely claimed library executions. No dependency was added. Core runtime remains Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0, threadpoolctl 3.7.0 and CPU PyTorch 2.14.1. Thread count one, seeds 2308–2314 and deterministic Torch algorithms are explicit. All neural calculations use float64 except the declared float32 state/attention benchmark and its resource children in code_112.

## Experiments and actual conclusions

- **108 — tabular computation:** sixty buildings × six records; train/development/final identities 40/10/10; four continuous plus three one-hot inputs, training-only scale. Ordinary MLP (817 parameters), residual network (2617) and original four-member BatchEnsemble-style fast-weight network (1380); three initializations × two rates × 200 update limits, own development checkpoints. Effective Hadamard matrices independently match vectorized predictions. Ensemble means beat their own individual members but do not consistently beat the ordinary MLP. Residual mean error is lower here with greater capacity. Repeat SD is not a deployment interval. A separate six-training-quantile-knot numerical basis passes partition/reconstruction checks; it is not silently substituted into one fitted comparison. FT-Transformer, TabNet, RealMLP and TabM are located with primary papers, not executed full methods.
- **109 — temporal locality:** sixty machines × four 64-sample windows, 100 Hz; 40/10/10 machine split. An 8-Hz then 12-Hz window versus its exact reversal isolates lost ordering in global power. Fixed logistic global/half-window spectral baselines versus a genuine four-block causal Conv1d model, dilations 1/2/4/8, two rates and 200 updates, own development checkpoints. Final Brier losses 0.251424849, 0.000294110 and 9.00164254e-8; accuracies 0.475/1/1. Receptive span 31 samples, 0.30 seconds, all positions reachable. Future perturbations preserve earlier outputs and fitted last-logit derivatives are zero outside support. Classification uses a completed window, not an unobserved future target. Fixed training-cohort scaling preserves causality.
- **110 — recurrent contracts:** fifty independent building episodes; 30/10/10 identities, source 24–40 events; additional independent final-identity episodes 80–96 events. Explicit elapsed days, observed indicator, and separate valid-padding mask; generator decays by 0.95 raised to elapsed days. Native RNN/GRU/LSTM width eight and GRU truncated every eight events; 120 AdamW update limits, own development checkpoints, valid-count-weighted loss. Truncated training still takes one optimizer update per full batch. Native GRU and LSTM first-step formulas are independently checked, including PyTorch's reset-after-hidden-affine GRU convention. Source MSE 0.0010673/0.00024295/0.00045487/0.00025212, long MSE 0.00485014/0.00139522/0.00200079/0.00143069. Streaming/full frozen predictions agree to rounding. Same forward values with detached chunks cut final-output/first-event gradient from 0.000445505 to zero. Carrying another independent episode's state alters early predictions by about 0.11627. Gate comparisons have different parameter counts.
- **111 — attention access:** independent manual scaled-QKV/native-primitive identity and mask checks. Own pre-normalized width-eight, two-head, feedforward-width-sixteen transformer block. Table task: 30 buildings × six, 20/5/5 split, four numerical field-specific embeddings, categorical and summary tokens, final MSE 0.151710408. Separate causal next-state forecast: fifty episodes, 30/10/10 identities, 48 events, currently observed state/load, final MSE 0.010172543 versus persistence 0.037192204. Both fits use 250 updates with development-only checkpoint selection. Future changes from time 24 leave earlier masked predictions unchanged; removing the same frozen model's mask changes earlier predictions by up to 0.342500907. The latter is an availability audit, not a trained unmasked comparator. Content-only permutation equivariance, positional perturbation, excluded padded keys and unchanged valid-query outputs are checked. Materialized score bytes are accounting, not RSS; MHA true forbids access, while the native primitive identity uses additive zero/negative-infinity masks.
- **112 — selective state and length shift:** own input-dependent diagonal exact zero-order-hold recurrence (627 parameters) versus own materialized causal attention (633), common 633-parameter ceiling, two rates × 120 updates and development checkpoints. Static-control width-48 ablation has 339 parameters, so it is not capacity matched. Marked amplitudes with background distractors; 48/24 train/dev episodes length 32, same 48 final episodes evaluated at prefixes 32/128/512, marker within first sixteen. Last-query MSE selective 0.018865546/0.380159348/0.534933984; attention 0.006982041/0.702159941/1.001933336; static 0.077328995/0.521417797/0.512821436. All-query losses are also retained. Both fitted models fail longer distractor suffixes; static even slightly beats selective at 512. Known marker-copy rule is zero by construction, not learned. Exact constant-control subdivision, streamed/full values and input-dependent controls are verified. An untrained periodic-summary attention fixture verifies causal access only, with no accuracy claim. These references are not S4 or full Mamba 1/2/3 executions. Primary chronology: S4 first 31 Oct 2021, Mamba 1 Dec 2023, Mamba-2 31 May 2024, Mamba-3 16 Mar 2026; all precede the book cutoff.
- **113 — sparse experts:** sixty buildings × ten mixed-regime records, 40/10/10 split. Top-one learned router, selected probability times selected expert, no gradient-through-argmax claim. Actual selected-row execution checked against explicit calculation and forward-hook row counts. Both sparse three-expert and dense candidates use 30 linear MAC/record; softmax, biases, nonlinearities, indexing and dispatch costs are excluded, and no equal-latency claim is made. Sparse/dense stored parameters 108/41, one-path parameters 42/41. Two dense rates and two balance coefficients × 400 updates/own development checkpoints. Dense final MSE 0.044502802; experts balance 0 gives 0.037039745, balance 0.1 gives 0.048347665. Development selects 0.1, retaining its worse final assessment. Loads 33/38/29 are more uniform than 15/65/20, without guaranteeing lower final error or regime recovery. Capacity factor 1 allows 34 per expert, four fallback records and MSE 0.063248946. Factors 1.25/2 permit 42/67 and no overflow, retaining MSE 0.048347665. Input-order admission, explicit centered-zero/raw-training-mean fallback and all-query denominator. Queue permutation at factor 1.25 changes zero flags because no overflow occurs; no observed order effect is claimed.
- **114 — functions and geometry:** actual differentiable cubic Cox–de Boor basis, eleven functions, independent SciPy design-matrix max error 1.110223e-16, nonnegativity/partition checks and interior gradcheck. Own fixed-grid spline-plus-SiLU edge network 2→4→1 (149 parameters), not complete adaptive-grid KAN. Smooth interaction target, source train/dev/final 500/160/300 in [-1,1]²; locked 200-point outside test first coordinate [1.05,1.8]. Additive spline Ridge (23 parameters) versus tensor-product spline Ridge (122), MLP (97), edge network (149), two candidates each/own development selection; neural 400-update limits. Final source MSE 0.312029487/0.001080590/0.002134610/0.001070859; outside MSE 0.941846722/0.375514439/0.260425285/0.345446403. Tensor interactions nearly close the edge model's source advantage over additive splines; MLP extrapolates best here. Clamped spline basis does not make the edge's SiLU-augmented total extrapolation constant. Separate isotropic squared-radius disk task: raw coordinate MLP rotation RMS 0.036368914 versus radial-feature head 7.355637e-17 under angle 0.7; final MSE 0.002717962 versus 4.853367e-6. That symmetry is not imposed on the orientation-dependent interaction target; no graph network is claimed.

## Resource evidence, repairs and reproducibility

Code_112 launches eighteen fresh child CPU processes: two fitted models × three lengths × three repetitions, batch four, float32, one warmup and five inference forwards. Inputs/model state travel in memory to the same interpreter; OS RSS units are explicitly converted for Darwin bytes versus Linux KiB. Peak RSS includes the interpreter/libraries/allocator and is not state-only or GPU memory. The 768-byte recurrent state excludes inputs, returned predictions and training intermediates. The scan uses less process peak memory at length 512 but its Python loop is slower than the small attention reference. Exact observations are recorded below in the execution report, outside deterministic RESULTS. Book figure generation skips the explicitly marked measurement cell, injects its original observations, and reruns every other cell with exact RESULTS checks. It does not claim bit-identical resource timing or silently measure again for the book plot.

All initial kernels passed. The 109 backward receptive-field diagram initially expanded dilation layers in forward order; the diagram loop was corrected to reverse layer order and a fresh run preserved exact results. A tensor-product spline baseline was subsequently added to 114 to separate interaction representation from network choice; all earlier family and geometry results remained exactly unchanged. Visual review then improved 108's residual/matrix layout and common grayscale, clarified 114's diagram labels, and replaced crowded logarithmic context ticks in 111/112. Four fresh kernels reran those current sources; deterministic RESULTS remained exactly identical. The latest 112 run measures its resource observations anew and those current actual observations are retained. No execution warnings are suppressed. Seven notebook sources contain 29 executed code cells and 14 inline figures, all reviewed alongside fourteen original vector book figures.

Primary research papers supply mechanism/chronology context; all numerical results and teaching data mechanisms are original scoped experiments. Documentation accessed 20 October 2026 can identify a newer maintenance patch than the executed pins (notably SciPy live 1.18.0 versus 1.17.1). Named systems' reported benchmark speedups or field claims are not transferred to these references. Literature completeness, operational validity and universal architecture rankings are not asserted.

## Successful result dictionaries

### code_108

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2308.

```json
{
  "candidates": [
    {
      "architecture": "MLP",
      "best_step": 200,
      "development_MSE": 0.22431811987925557,
      "learning_rate": 0.005,
      "replicate": 0
    },
    {
      "architecture": "MLP",
      "best_step": 125,
      "development_MSE": 0.25085964628617163,
      "learning_rate": 0.01,
      "replicate": 0
    },
    {
      "architecture": "MLP",
      "best_step": 200,
      "development_MSE": 0.18472150755483785,
      "learning_rate": 0.005,
      "replicate": 1
    },
    {
      "architecture": "MLP",
      "best_step": 195,
      "development_MSE": 0.2122262060278942,
      "learning_rate": 0.01,
      "replicate": 1
    },
    {
      "architecture": "MLP",
      "best_step": 200,
      "development_MSE": 0.3151370591577223,
      "learning_rate": 0.005,
      "replicate": 2
    },
    {
      "architecture": "MLP",
      "best_step": 200,
      "development_MSE": 0.29978793815759097,
      "learning_rate": 0.01,
      "replicate": 2
    },
    {
      "architecture": "Residual",
      "best_step": 200,
      "development_MSE": 0.21903374810857493,
      "learning_rate": 0.005,
      "replicate": 0
    },
    {
      "architecture": "Residual",
      "best_step": 140,
      "development_MSE": 0.2681242732754587,
      "learning_rate": 0.01,
      "replicate": 0
    },
    {
      "architecture": "Residual",
      "best_step": 200,
      "development_MSE": 0.161966674787578,
      "learning_rate": 0.005,
      "replicate": 1
    },
    {
      "architecture": "Residual",
      "best_step": 175,
      "development_MSE": 0.2020380461093433,
      "learning_rate": 0.01,
      "replicate": 1
    },
    {
      "architecture": "Residual",
      "best_step": 200,
      "development_MSE": 0.21941551743563956,
      "learning_rate": 0.005,
      "replicate": 2
    },
    {
      "architecture": "Residual",
      "best_step": 200,
      "development_MSE": 0.23127084711796642,
      "learning_rate": 0.01,
      "replicate": 2
    },
    {
      "architecture": "Fast ensemble",
      "best_step": 200,
      "development_MSE": 0.2665093003507939,
      "learning_rate": 0.005,
      "replicate": 0
    },
    {
      "architecture": "Fast ensemble",
      "best_step": 195,
      "development_MSE": 0.25047193221317815,
      "learning_rate": 0.01,
      "replicate": 0
    },
    {
      "architecture": "Fast ensemble",
      "best_step": 200,
      "development_MSE": 0.2992676055809452,
      "learning_rate": 0.005,
      "replicate": 1
    },
    {
      "architecture": "Fast ensemble",
      "best_step": 200,
      "development_MSE": 0.25263280431503043,
      "learning_rate": 0.01,
      "replicate": 1
    },
    {
      "architecture": "Fast ensemble",
      "best_step": 200,
      "development_MSE": 0.24788213149691427,
      "learning_rate": 0.005,
      "replicate": 2
    },
    {
      "architecture": "Fast ensemble",
      "best_step": 200,
      "development_MSE": 0.23732338778990636,
      "learning_rate": 0.01,
      "replicate": 2
    }
  ],
  "comparisons": [
    {
      "architecture": "MLP",
      "best_step": 200,
      "development_MSE": 0.22431811987925557,
      "final_MSE": 0.16419410804606474,
      "predictions_per_record": 1,
      "replicate": 0,
      "selected_rate": 0.005,
      "stored_parameters": 817
    },
    {
      "architecture": "MLP",
      "best_step": 200,
      "development_MSE": 0.18472150755483785,
      "final_MSE": 0.14176810941532095,
      "predictions_per_record": 1,
      "replicate": 1,
      "selected_rate": 0.005,
      "stored_parameters": 817
    },
    {
      "architecture": "MLP",
      "best_step": 200,
      "development_MSE": 0.29978793815759097,
      "final_MSE": 0.14714305918980788,
      "predictions_per_record": 1,
      "replicate": 2,
      "selected_rate": 0.01,
      "stored_parameters": 817
    },
    {
      "architecture": "Residual",
      "best_step": 200,
      "development_MSE": 0.21903374810857493,
      "final_MSE": 0.13217076182418125,
      "predictions_per_record": 1,
      "replicate": 0,
      "selected_rate": 0.005,
      "stored_parameters": 2617
    },
    {
      "architecture": "Residual",
      "best_step": 200,
      "development_MSE": 0.161966674787578,
      "final_MSE": 0.15981730186356552,
      "predictions_per_record": 1,
      "replicate": 1,
      "selected_rate": 0.005,
      "stored_parameters": 2617
    },
    {
      "architecture": "Residual",
      "best_step": 200,
      "development_MSE": 0.21941551743563956,
      "final_MSE": 0.13323135118548265,
      "predictions_per_record": 1,
      "replicate": 2,
      "selected_rate": 0.005,
      "stored_parameters": 2617
    },
    {
      "architecture": "Fast ensemble",
      "best_step": 195,
      "development_MSE": 0.25047193221317815,
      "final_MSE": 0.16549916111265447,
      "individual_member_MSE": [
        0.2294579833718197,
        0.23732511968384665,
        0.16667661741253822,
        0.21930525658106148
      ],
      "mean_query_member_SD": 0.19091900186356106,
      "predictions_per_record": 4,
      "replicate": 0,
      "selected_rate": 0.01,
      "stored_parameters": 1380
    },
    {
      "architecture": "Fast ensemble",
      "best_step": 200,
      "development_MSE": 0.25263280431503043,
      "final_MSE": 0.14924394261577859,
      "individual_member_MSE": [
        0.2163662775765786,
        0.1832863984205582,
        0.22058514729157233,
        0.16206396623206792
      ],
      "mean_query_member_SD": 0.1859090106587705,
      "predictions_per_record": 4,
      "replicate": 1,
      "selected_rate": 0.01,
      "stored_parameters": 1380
    },
    {
      "architecture": "Fast ensemble",
      "best_step": 200,
      "development_MSE": 0.23732338778990636,
      "final_MSE": 0.14119579851472105,
      "individual_member_MSE": [
        0.18516596991796563,
        0.15602646649935237,
        0.16171971681813363,
        0.1940017429136964
      ],
      "mean_query_member_SD": 0.15662757202147212,
      "predictions_per_record": 4,
      "replicate": 2,
      "selected_rate": 0.01,
      "stored_parameters": 1380
    }
  ],
  "fast_weight_identity_checked": true,
  "numerical_basis_clipped_final_count": 0,
  "numerical_basis_shape": [
    60,
    6
  ],
  "shared_features": 7,
  "split_buildings": [
    40,
    10,
    10
  ],
  "update_budget_per_candidate": 200
}
```

### code_109

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2309.

```json
{
  "TCN_candidates": [
    {
      "best_step": 200,
      "development_Brier": 1.927355265762106e-06,
      "rate": 0.005
    },
    {
      "best_step": 200,
      "development_Brier": 1.1420725860554361e-11,
      "rate": 0.01
    }
  ],
  "TCN_parameters": 825,
  "first_structurally_reachable_sample": 33,
  "future_prefix_max_difference": 0.0,
  "global_power_reversal_max_difference": 5.551115123125783e-17,
  "metrics": [
    {
      "development_Brier": 0.24418927932623732,
      "final_Brier": 0.2514248494910469,
      "final_accuracy": 0.475,
      "method": "Global powers"
    },
    {
      "development_Brier": 0.00045283885372521016,
      "final_Brier": 0.0002941100413354398,
      "final_accuracy": 1.0,
      "method": "Half-window powers"
    },
    {
      "development_Brier": 1.1420725860554361e-11,
      "final_Brier": 9.0016425430809e-08,
      "final_accuracy": 1.0,
      "method": "Causal TCN"
    }
  ],
  "receptive_field_samples": 31,
  "sample_interval_seconds": 0.01,
  "selected_TCN_rate": 0.01,
  "selected_TCN_step": 200,
  "split_machines": [
    40,
    10,
    10
  ],
  "trained_input_gradient": [
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.11596386506565716,
    0.12008385334704158,
    0.3727228836085237,
    0.07011230857785031,
    0.0012806403387645372,
    -0.046836514247043284,
    -0.49674198542327924,
    -0.2317385412764581,
    -1.1194835444089148,
    -0.9463499309373358,
    -1.7014316193337127,
    0.32066692232302796,
    0.28838287534669615,
    0.37731550359524213,
    3.2509074987818356,
    -0.07793917329301525,
    -1.8686420891387652,
    -2.0384733884170054,
    -5.556889569578293,
    -0.5684642467792203,
    0.3683381225465962,
    0.3897397733031033,
    0.9843623148445412,
    -0.0035418883744694546,
    -0.634069399342526,
    -1.3483635670618057,
    -4.133199348790134,
    -1.3854867015287953,
    -1.681682814715316,
    0.11502513379281783,
    0.5152888845547335
  ]
}
```

### code_110

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2310.

```json
{
  "GRU_first_reset_gate": [
    0.6053136634652837,
    0.38309667689725446,
    0.6175189817562359,
    0.6527573383785739,
    0.45112054381750555,
    0.43438906563754104,
    0.4032557216317348,
    0.7653163247948293
  ],
  "GRU_first_update_gate": [
    0.752554893149598,
    0.7017785128434131,
    0.5724813699752727,
    0.3936913374969174,
    0.5053694874328859,
    0.6349769383593311,
    0.7142826365323944,
    0.48025907835608367
  ],
  "comparisons": [
    {
      "best_update": 115,
      "development_MSE": 0.0013886447426676276,
      "final_long_episode_MSE": 0.00485013575605835,
      "final_source_length_MSE": 0.001067300937370796,
      "model": "RNN",
      "parameters": 113
    },
    {
      "best_update": 120,
      "development_MSE": 0.0002969402235129684,
      "final_long_episode_MSE": 0.001395222197314509,
      "final_source_length_MSE": 0.00024294956068701362,
      "model": "GRU",
      "parameters": 321
    },
    {
      "best_update": 110,
      "development_MSE": 0.0005165326967927965,
      "final_long_episode_MSE": 0.0020007882701330126,
      "final_source_length_MSE": 0.0004548715455990279,
      "model": "LSTM",
      "parameters": 425
    },
    {
      "best_update": 120,
      "development_MSE": 0.00026216393837599663,
      "final_long_episode_MSE": 0.001430689091477824,
      "final_source_length_MSE": 0.00025211891034593824,
      "model": "Truncated GRU",
      "parameters": 321
    }
  ],
  "detached_first_event_gradient": 0.0,
  "full_first_event_gradient": 0.00044550543286659913,
  "histories": {
    "GRU": [
      {
        "development_MSE": 0.03238846874161034,
        "optimizer_update": 5
      },
      {
        "development_MSE": 0.02718409312169999,
        "optimizer_update": 10
      },
      {
        "development_MSE": 0.01947968095067298,
        "optimizer_update": 15
      },
      {
        "development_MSE": 0.01372319293246199,
        "optimizer_update": 20
      },
      {
        "development_MSE": 0.0063508823734002295,
        "optimizer_update": 25
      },
      {
        "development_MSE": 0.0024543739514333524,
        "optimizer_update": 30
      },
      {
        "development_MSE": 0.0027235502602868957,
        "optimizer_update": 35
      },
      {
        "development_MSE": 0.002562760833676209,
        "optimizer_update": 40
      },
      {
        "development_MSE": 0.0014116939359891442,
        "optimizer_update": 45
      },
      {
        "development_MSE": 0.001072729749907898,
        "optimizer_update": 50
      },
      {
        "development_MSE": 0.0010839952786341675,
        "optimizer_update": 55
      },
      {
        "development_MSE": 0.0010453262602705864,
        "optimizer_update": 60
      },
      {
        "development_MSE": 0.0006930193267276522,
        "optimizer_update": 65
      },
      {
        "development_MSE": 0.0006439693677805762,
        "optimizer_update": 70
      },
      {
        "development_MSE": 0.0006610136903908544,
        "optimizer_update": 75
      },
      {
        "development_MSE": 0.0005815952747870281,
        "optimizer_update": 80
      },
      {
        "development_MSE": 0.0005248518566232581,
        "optimizer_update": 85
      },
      {
        "development_MSE": 0.0004809856938852942,
        "optimizer_update": 90
      },
      {
        "development_MSE": 0.0004462337181601794,
        "optimizer_update": 95
      },
      {
        "development_MSE": 0.0004278328968775363,
        "optimizer_update": 100
      },
      {
        "development_MSE": 0.00037570562469590367,
        "optimizer_update": 105
      },
      {
        "development_MSE": 0.00033898495771920377,
        "optimizer_update": 110
      },
      {
        "development_MSE": 0.00032709305729932455,
        "optimizer_update": 115
      },
      {
        "development_MSE": 0.0002969402235129684,
        "optimizer_update": 120
      }
    ],
    "LSTM": [
      {
        "development_MSE": 0.040665005668870415,
        "optimizer_update": 5
      },
      {
        "development_MSE": 0.02195806791455729,
        "optimizer_update": 10
      },
      {
        "development_MSE": 0.0064847186749968245,
        "optimizer_update": 15
      },
      {
        "development_MSE": 0.005240496375591048,
        "optimizer_update": 20
      },
      {
        "development_MSE": 0.006972790161344925,
        "optimizer_update": 25
      },
      {
        "development_MSE": 0.0026884320468871935,
        "optimizer_update": 30
      },
      {
        "development_MSE": 0.0028719063656295323,
        "optimizer_update": 35
      },
      {
        "development_MSE": 0.0032424174755312013,
        "optimizer_update": 40
      },
      {
        "development_MSE": 0.0017960600113902296,
        "optimizer_update": 45
      },
      {
        "development_MSE": 0.0018521525521120175,
        "optimizer_update": 50
      },
      {
        "development_MSE": 0.0017117811107137686,
        "optimizer_update": 55
      },
      {
        "development_MSE": 0.0013392051484517262,
        "optimizer_update": 60
      },
      {
        "development_MSE": 0.0013195068105238527,
        "optimizer_update": 65
      },
      {
        "development_MSE": 0.0009710153644851457,
        "optimizer_update": 70
      },
      {
        "development_MSE": 0.0010253118880139203,
        "optimizer_update": 75
      },
      {
        "development_MSE": 0.000838387833333798,
        "optimizer_update": 80
      },
      {
        "development_MSE": 0.0008040770113308636,
        "optimizer_update": 85
      },
      {
        "development_MSE": 0.0006812046014772055,
        "optimizer_update": 90
      },
      {
        "development_MSE": 0.0006495411462678676,
        "optimizer_update": 95
      },
      {
        "development_MSE": 0.0005570515968025775,
        "optimizer_update": 100
      },
      {
        "development_MSE": 0.0011111657131676325,
        "optimizer_update": 105
      },
      {
        "development_MSE": 0.0005165326967927965,
        "optimizer_update": 110
      },
      {
        "development_MSE": 0.000572142496763151,
        "optimizer_update": 115
      },
      {
        "development_MSE": 0.0005442967554587064,
        "optimizer_update": 120
      }
    ],
    "RNN": [
      {
        "development_MSE": 0.03372140264616278,
        "optimizer_update": 5
      },
      {
        "development_MSE": 0.02071824807066599,
        "optimizer_update": 10
      },
      {
        "development_MSE": 0.007329979158149237,
        "optimizer_update": 15
      },
      {
        "development_MSE": 0.010663609951173995,
        "optimizer_update": 20
      },
      {
        "development_MSE": 0.0086640731074244,
        "optimizer_update": 25
      },
      {
        "development_MSE": 0.005080703239188617,
        "optimizer_update": 30
      },
      {
        "development_MSE": 0.005873501539422048,
        "optimizer_update": 35
      },
      {
        "development_MSE": 0.004001856900353511,
        "optimizer_update": 40
      },
      {
        "development_MSE": 0.004126214810115182,
        "optimizer_update": 45
      },
      {
        "development_MSE": 0.0033109623412854432,
        "optimizer_update": 50
      },
      {
        "development_MSE": 0.003138742623937779,
        "optimizer_update": 55
      },
      {
        "development_MSE": 0.002687982498975261,
        "optimizer_update": 60
      },
      {
        "development_MSE": 0.0026396276570509565,
        "optimizer_update": 65
      },
      {
        "development_MSE": 0.0022664182938740224,
        "optimizer_update": 70
      },
      {
        "development_MSE": 0.0022431161776001046,
        "optimizer_update": 75
      },
      {
        "development_MSE": 0.0019845042882790796,
        "optimizer_update": 80
      },
      {
        "development_MSE": 0.0018582368291946369,
        "optimizer_update": 85
      },
      {
        "development_MSE": 0.001824790439777555,
        "optimizer_update": 90
      },
      {
        "development_MSE": 0.001892740297104955,
        "optimizer_update": 95
      },
      {
        "development_MSE": 0.001958930333320442,
        "optimizer_update": 100
      },
      {
        "development_MSE": 0.0017477932626490443,
        "optimizer_update": 105
      },
      {
        "development_MSE": 0.0016833221441814113,
        "optimizer_update": 110
      },
      {
        "development_MSE": 0.0013886447426676276,
        "optimizer_update": 115
      },
      {
        "development_MSE": 0.0014593603208383186,
        "optimizer_update": 120
      }
    ],
    "Truncated GRU": [
      {
        "development_MSE": 0.03255964386936028,
        "optimizer_update": 5
      },
      {
        "development_MSE": 0.027808025274020615,
        "optimizer_update": 10
      },
      {
        "development_MSE": 0.02048494575042901,
        "optimizer_update": 15
      },
      {
        "development_MSE": 0.015492677517917339,
        "optimizer_update": 20
      },
      {
        "development_MSE": 0.00923222659033876,
        "optimizer_update": 25
      },
      {
        "development_MSE": 0.004925279314468973,
        "optimizer_update": 30
      },
      {
        "development_MSE": 0.001961288202974148,
        "optimizer_update": 35
      },
      {
        "development_MSE": 0.0018539418472317756,
        "optimizer_update": 40
      },
      {
        "development_MSE": 0.0014949002394129478,
        "optimizer_update": 45
      },
      {
        "development_MSE": 0.0011884506022205223,
        "optimizer_update": 50
      },
      {
        "development_MSE": 0.0008178405645126857,
        "optimizer_update": 55
      },
      {
        "development_MSE": 0.000710417638754875,
        "optimizer_update": 60
      },
      {
        "development_MSE": 0.0007018245266258915,
        "optimizer_update": 65
      },
      {
        "development_MSE": 0.0005879726783218391,
        "optimizer_update": 70
      },
      {
        "development_MSE": 0.0005622425991638659,
        "optimizer_update": 75
      },
      {
        "development_MSE": 0.0005157649935278104,
        "optimizer_update": 80
      },
      {
        "development_MSE": 0.0004287436073566188,
        "optimizer_update": 85
      },
      {
        "development_MSE": 0.000371583423458299,
        "optimizer_update": 90
      },
      {
        "development_MSE": 0.000365779863941045,
        "optimizer_update": 95
      },
      {
        "development_MSE": 0.0003552665716408184,
        "optimizer_update": 100
      },
      {
        "development_MSE": 0.00032146454207530634,
        "optimizer_update": 105
      },
      {
        "development_MSE": 0.000295724913834001,
        "optimizer_update": 110
      },
      {
        "development_MSE": 0.00027801784384593007,
        "optimizer_update": 115
      },
      {
        "development_MSE": 0.00026216393837599663,
        "optimizer_update": 120
      }
    ]
  },
  "long_episode_lengths": [
    80,
    85,
    81,
    87,
    88,
    89,
    91,
    89,
    89,
    95
  ],
  "native_gate_checks": true,
  "optimizer_updates_per_candidate": 120,
  "other_episode_carried_state_prefix_difference": 0.11627095479187738,
  "split_buildings": [
    30,
    10,
    10
  ],
  "state_shapes": {
    "GRU": [
      1,
      1,
      8
    ],
    "LSTM": [
      [
        1,
        1,
        8
      ],
      [
        1,
        1,
        8
      ]
    ],
    "RNN": [
      1,
      1,
      8
    ],
    "Truncated GRU": [
      1,
      1,
      8
    ]
  },
  "stream_max_errors": {
    "GRU": 0.0,
    "LSTM": 0.0,
    "RNN": 2.498001805406602e-16,
    "Truncated GRU": 0.0
  },
  "training_lengths": [
    39,
    37,
    29,
    24,
    37,
    34,
    33,
    36,
    34,
    25,
    37,
    35,
    38,
    30,
    27,
    35,
    32,
    25,
    33,
    25,
    28,
    34,
    30,
    30,
    33,
    25,
    35,
    32,
    32,
    30,
    32,
    28,
    32,
    32,
    28,
    25,
    34,
    31,
    28,
    39,
    35,
    39,
    37,
    38,
    33,
    36,
    39,
    36,
    40,
    27
  ]
}
```

### code_111

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2311.

```json
{
  "causal_prefix_max_difference": 0.0,
  "feature_attention_shape": [
    30,
    2,
    6,
    6
  ],
  "manual_attention": [
    [
      [
        1.0,
        0.0
      ],
      [
        0.33023845067334306,
        1.3395230986533138
      ],
      [
        1.7587246087113846,
        1.0
      ]
    ]
  ],
  "materialized_score_bytes": [
    {
      "batch": 1,
      "float64_bytes": 16384,
      "heads": 2,
      "length": 32
    },
    {
      "batch": 1,
      "float64_bytes": 262144,
      "heads": 2,
      "length": 128
    },
    {
      "batch": 1,
      "float64_bytes": 4194304,
      "heads": 2,
      "length": 512
    }
  ],
  "padding_valid_query_max_difference": 0.0,
  "persistence_final_MSE": 0.037192203709195557,
  "position_content_permutation_difference": 1.716878836374487,
  "table_best_step": 250,
  "table_development_MSE": 0.04504705466703456,
  "table_final_MSE": 0.15171040761103277,
  "table_split_buildings": [
    20,
    5,
    5
  ],
  "temporal_best_step": 220,
  "temporal_development_MSE": 0.010550628290364758,
  "temporal_final_MSE": 0.010172542691388434,
  "temporal_split_buildings": [
    30,
    10,
    10
  ],
  "time_attention_shape": [
    10,
    2,
    48,
    48
  ],
  "unmasked_prefix_max_difference": 0.3425009071401382
}
```

### code_112

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2312.

```json
{
  "comparisons": [
    {
      "all_query_MSE": 0.0071017262525856495,
      "best_step": 120,
      "last_query_MSE": 0.018865546211600304,
      "length": 32,
      "model": "Selective scan",
      "parameters": 627,
      "selected_rate": 0.01
    },
    {
      "all_query_MSE": 0.1567832976579666,
      "best_step": 120,
      "last_query_MSE": 0.3801593482494354,
      "length": 128,
      "model": "Selective scan",
      "parameters": 627,
      "selected_rate": 0.01
    },
    {
      "all_query_MSE": 0.4256622791290283,
      "best_step": 120,
      "last_query_MSE": 0.5349339842796326,
      "length": 512,
      "model": "Selective scan",
      "parameters": 627,
      "selected_rate": 0.01
    },
    {
      "all_query_MSE": 0.00485842302441597,
      "best_step": 120,
      "last_query_MSE": 0.00698204105719924,
      "length": 32,
      "model": "Reference attention",
      "parameters": 633,
      "selected_rate": 0.01
    },
    {
      "all_query_MSE": 0.25976064801216125,
      "best_step": 120,
      "last_query_MSE": 0.7021599411964417,
      "length": 128,
      "model": "Reference attention",
      "parameters": 633,
      "selected_rate": 0.01
    },
    {
      "all_query_MSE": 0.5088492035865784,
      "best_step": 120,
      "last_query_MSE": 1.0019333362579346,
      "length": 512,
      "model": "Reference attention",
      "parameters": 633,
      "selected_rate": 0.01
    },
    {
      "all_query_MSE": 0.026916757225990295,
      "best_step": 120,
      "last_query_MSE": 0.07732899487018585,
      "length": 32,
      "model": "Static scan",
      "parameters": 339,
      "selected_rate": 0.01
    },
    {
      "all_query_MSE": 0.25241169333457947,
      "best_step": 120,
      "last_query_MSE": 0.5214177966117859,
      "length": 128,
      "model": "Static scan",
      "parameters": 339,
      "selected_rate": 0.01
    },
    {
      "all_query_MSE": 0.474029541015625,
      "best_step": 120,
      "last_query_MSE": 0.5128214359283447,
      "length": 512,
      "model": "Static scan",
      "parameters": 339,
      "selected_rate": 0.01
    }
  ],
  "delta_marker_control_difference": 0.29835084080696106,
  "diagonal_subdivision_identity_checked": true,
  "exact_marker_rule_MSE": 0.0,
  "fit_length": 32,
  "hybrid_prefix_max_difference": 0.0,
  "hybrid_summary_indices": [
    3,
    7,
    11,
    15
  ],
  "hybrid_untrained_parameters": 1628,
  "materialized_attention_score_bytes": [
    {
      "bytes": 32768,
      "length": 32
    },
    {
      "bytes": 524288,
      "length": 128
    },
    {
      "bytes": 8388608,
      "length": 512
    }
  ],
  "paired_final_lengths": [
    32,
    128,
    512
  ],
  "profile_batch": 4,
  "profile_dtype": "float32",
  "recurrent_state_bytes": 768,
  "selection": [
    {
      "best_step": 120,
      "development_MSE": 0.008636387065052986,
      "model": "Selective scan",
      "rate": 0.005
    },
    {
      "best_step": 120,
      "development_MSE": 0.004317216109484434,
      "model": "Selective scan",
      "rate": 0.01
    },
    {
      "best_step": 120,
      "development_MSE": 0.010491267777979374,
      "model": "Reference attention",
      "rate": 0.005
    },
    {
      "best_step": 120,
      "development_MSE": 0.004043726250529289,
      "model": "Reference attention",
      "rate": 0.01
    },
    {
      "best_step": 120,
      "development_MSE": 0.11277445405721664,
      "model": "Static scan",
      "rate": 0.005
    },
    {
      "best_step": 120,
      "development_MSE": 0.019254017621278763,
      "model": "Static scan",
      "rate": 0.01
    }
  ],
  "source_episode_counts": [
    48,
    24,
    48
  ],
  "streaming_max_difference": 0.0
}
```

### code_113

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2313.

```json
{
  "activated_parameters_per_record": {
    "Dense": 41,
    "MoE": 42
  },
  "candidates": [
    {
      "balance_weight": 0.0,
      "best_step": 400,
      "development_MSE": 0.07005317348500308,
      "family": "Dense",
      "rate": 0.005
    },
    {
      "balance_weight": 0.0,
      "best_step": 400,
      "development_MSE": 0.05565071234539649,
      "family": "Dense",
      "rate": 0.01
    },
    {
      "balance_weight": 0.0,
      "best_step": 400,
      "development_MSE": 0.037286898960384576,
      "family": "MoE",
      "rate": 0.01
    },
    {
      "balance_weight": 0.1,
      "best_step": 310,
      "development_MSE": 0.027001110773952244,
      "family": "MoE",
      "rate": 0.01
    }
  ],
  "capacity": [
    {
      "capacity_factor": 1.0,
      "expert_rows_computed": 96,
      "fallback_count": 4,
      "final_MSE_including_mean_fallback": 0.06324894568883678,
      "per_expert_capacity": 34
    },
    {
      "capacity_factor": 1.25,
      "expert_rows_computed": 100,
      "fallback_count": 0,
      "final_MSE_including_mean_fallback": 0.04834766549382981,
      "per_expert_capacity": 42
    },
    {
      "capacity_factor": 2.0,
      "expert_rows_computed": 100,
      "fallback_count": 0,
      "final_MSE_including_mean_fallback": 0.04834766549382981,
      "per_expert_capacity": 67
    }
  ],
  "capacity_priority": "input order within expert queue",
  "comparisons": [
    {
      "best_step": 400,
      "development_MSE": 0.05565071234539649,
      "final_MSE": 0.04450280194444476,
      "linear_MACs_per_record": 30,
      "model": "Dense",
      "selected_rate": 0.01,
      "stored_parameters": 41
    },
    {
      "balance_weight": 0.0,
      "best_step": 400,
      "development_MSE": 0.037286898960384576,
      "final_MSE": 0.037039745236267185,
      "final_route_loads": [
        15,
        65,
        20
      ],
      "linear_MACs_per_record": 30,
      "model": "MoE balance 0",
      "route_generator_ARI": 0.3216122628756541,
      "stored_parameters": 108
    },
    {
      "balance_weight": 0.1,
      "best_step": 310,
      "development_MSE": 0.027001110773952244,
      "final_MSE": 0.04834766549382981,
      "final_route_loads": [
        33,
        38,
        29
      ],
      "linear_MACs_per_record": 30,
      "model": "MoE balance 0.1",
      "route_generator_ARI": 0.23358199662557033,
      "stored_parameters": 108
    }
  ],
  "dense_equivalent_expert_rows": 300,
  "fallback_raw_response": -0.22150669080341567,
  "linear_MACs_per_record": {
    "Dense": 30,
    "MoE": 30
  },
  "queue_order_changed_fallback_flags": 0,
  "queue_permuted_capacity_MSE": 0.04834766549382981,
  "selected_balance": 0.1,
  "selected_final_loads": [
    33,
    38,
    29
  ],
  "sparse_expert_rows": 100,
  "split_buildings": [
    40,
    10,
    10
  ]
}
```

### code_114

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2314.

```json
{
  "basis_SciPy_max_error": 1.1102230246251565e-16,
  "basis_count": 11,
  "candidates": [
    {
      "alpha": 0.01,
      "development_MSE": 0.29089192781154144,
      "model": "Additive spline"
    },
    {
      "alpha": 1.0,
      "development_MSE": 0.278218923813495,
      "model": "Additive spline"
    },
    {
      "alpha": 0.01,
      "development_MSE": 0.0011724709671943286,
      "model": "Tensor spline"
    },
    {
      "alpha": 1.0,
      "development_MSE": 0.01184125788094893,
      "model": "Tensor spline"
    },
    {
      "best_step": 400,
      "development_MSE": 0.002397650313599454,
      "model": "MLP",
      "rate": 0.005
    },
    {
      "best_step": 400,
      "development_MSE": 0.002049115005245906,
      "model": "MLP",
      "rate": 0.01
    },
    {
      "best_step": 400,
      "development_MSE": 0.0011381128193373885,
      "model": "KAN-style",
      "rate": 0.005
    },
    {
      "best_step": 400,
      "development_MSE": 0.0011983943210614792,
      "model": "KAN-style",
      "rate": 0.01
    }
  ],
  "cohort_sizes": [
    500,
    160,
    300,
    200
  ],
  "comparisons": [
    {
      "development_MSE": 0.278218923813495,
      "final_extrapolation_MSE": 0.9418467221800948,
      "final_source_MSE": 0.31202948714585166,
      "model": "Additive spline",
      "parameters": 23,
      "selected_alpha": 1.0
    },
    {
      "development_MSE": 0.0011724709671943286,
      "final_extrapolation_MSE": 0.37551443893395714,
      "final_source_MSE": 0.001080589848059934,
      "model": "Tensor spline",
      "parameters": 122,
      "selected_alpha": 0.01
    },
    {
      "best_step": 400,
      "development_MSE": 0.002049115005245906,
      "final_extrapolation_MSE": 0.2604252848527289,
      "final_source_MSE": 0.002134610308576436,
      "model": "MLP",
      "parameters": 97,
      "selected_rate": 0.01
    },
    {
      "best_step": 400,
      "development_MSE": 0.0011381128193373885,
      "final_extrapolation_MSE": 0.34544640256610615,
      "final_source_MSE": 0.00107085929206601,
      "model": "KAN-style",
      "parameters": 149,
      "selected_rate": 0.005
    }
  ],
  "fixed_grid_ranges": {
    "first": [
      -1,
      1
    ],
    "hidden": [
      -3,
      3
    ]
  },
  "geometry_contract": [
    {
      "final_radial_response_MSE": 0.002717962445006639,
      "model": "Raw coordinates",
      "rotation_prediction_RMS_difference": 0.03636891439548427
    },
    {
      "final_radial_response_MSE": 4.853367145814617e-06,
      "model": "Radial feature",
      "rotation_prediction_RMS_difference": 7.35563665965861e-17
    }
  ],
  "geometry_rotation_angle": 0.7,
  "interior_basis_gradcheck": true,
  "outside_first_coordinate_range": [
    1.05,
    1.8
  ]
}
```


## Actual code_112 fresh-process resource observations

These measured observations are outside deterministic RESULTS; the vector resource plot replays these exact recorded values. New ordinary notebook runs measure anew.

```json
[
  {
    "baseline_RSS_bytes": 299892736,
    "batch": 4,
    "dtype": "float32",
    "length": 32,
    "model": "Selective scan",
    "parameters": 627,
    "peak_RSS_bytes": 303398912,
    "platform": "Darwin",
    "replicate": 0,
    "seconds_per_forward": 0.0005938334012171254,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299941888,
    "batch": 4,
    "dtype": "float32",
    "length": 32,
    "model": "Selective scan",
    "parameters": 627,
    "peak_RSS_bytes": 303415296,
    "platform": "Darwin",
    "replicate": 1,
    "seconds_per_forward": 0.0005901833996176719,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299843584,
    "batch": 4,
    "dtype": "float32",
    "length": 32,
    "model": "Selective scan",
    "parameters": 627,
    "peak_RSS_bytes": 303284224,
    "platform": "Darwin",
    "replicate": 2,
    "seconds_per_forward": 0.0006251165992580354,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299565056,
    "batch": 4,
    "dtype": "float32",
    "length": 128,
    "model": "Selective scan",
    "parameters": 627,
    "peak_RSS_bytes": 303120384,
    "platform": "Darwin",
    "replicate": 0,
    "seconds_per_forward": 0.00239840840222314,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299778048,
    "batch": 4,
    "dtype": "float32",
    "length": 128,
    "model": "Selective scan",
    "parameters": 627,
    "peak_RSS_bytes": 303366144,
    "platform": "Darwin",
    "replicate": 1,
    "seconds_per_forward": 0.0023993999988306315,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299925504,
    "batch": 4,
    "dtype": "float32",
    "length": 128,
    "model": "Selective scan",
    "parameters": 627,
    "peak_RSS_bytes": 303497216,
    "platform": "Darwin",
    "replicate": 2,
    "seconds_per_forward": 0.0024220834020525217,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299843584,
    "batch": 4,
    "dtype": "float32",
    "length": 512,
    "model": "Selective scan",
    "parameters": 627,
    "peak_RSS_bytes": 303710208,
    "platform": "Darwin",
    "replicate": 0,
    "seconds_per_forward": 0.009614350000629202,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299941888,
    "batch": 4,
    "dtype": "float32",
    "length": 512,
    "model": "Selective scan",
    "parameters": 627,
    "peak_RSS_bytes": 303775744,
    "platform": "Darwin",
    "replicate": 1,
    "seconds_per_forward": 0.009392191798542626,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299565056,
    "batch": 4,
    "dtype": "float32",
    "length": 512,
    "model": "Selective scan",
    "parameters": 627,
    "peak_RSS_bytes": 303382528,
    "platform": "Darwin",
    "replicate": 2,
    "seconds_per_forward": 0.009690525001497008,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299958272,
    "batch": 4,
    "dtype": "float32",
    "length": 32,
    "model": "Reference attention",
    "parameters": 633,
    "peak_RSS_bytes": 304103424,
    "platform": "Darwin",
    "replicate": 0,
    "seconds_per_forward": 9.459159919060767e-05,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299827200,
    "batch": 4,
    "dtype": "float32",
    "length": 32,
    "model": "Reference attention",
    "parameters": 633,
    "peak_RSS_bytes": 303972352,
    "platform": "Darwin",
    "replicate": 1,
    "seconds_per_forward": 9.673339955043047e-05,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299728896,
    "batch": 4,
    "dtype": "float32",
    "length": 32,
    "model": "Reference attention",
    "parameters": 633,
    "peak_RSS_bytes": 303874048,
    "platform": "Darwin",
    "replicate": 2,
    "seconds_per_forward": 9.725000127218664e-05,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299859968,
    "batch": 4,
    "dtype": "float32",
    "length": 128,
    "model": "Reference attention",
    "parameters": 633,
    "peak_RSS_bytes": 304005120,
    "platform": "Darwin",
    "replicate": 0,
    "seconds_per_forward": 0.00030521680018864573,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299728896,
    "batch": 4,
    "dtype": "float32",
    "length": 128,
    "model": "Reference attention",
    "parameters": 633,
    "peak_RSS_bytes": 303841280,
    "platform": "Darwin",
    "replicate": 1,
    "seconds_per_forward": 0.00031858339789323507,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299696128,
    "batch": 4,
    "dtype": "float32",
    "length": 128,
    "model": "Reference attention",
    "parameters": 633,
    "peak_RSS_bytes": 303808512,
    "platform": "Darwin",
    "replicate": 2,
    "seconds_per_forward": 0.00030060840072110295,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299679744,
    "batch": 4,
    "dtype": "float32",
    "length": 512,
    "model": "Reference attention",
    "parameters": 633,
    "peak_RSS_bytes": 328974336,
    "platform": "Darwin",
    "replicate": 0,
    "seconds_per_forward": 0.003298049999284558,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299941888,
    "batch": 4,
    "dtype": "float32",
    "length": 512,
    "model": "Reference attention",
    "parameters": 633,
    "peak_RSS_bytes": 329138176,
    "platform": "Darwin",
    "replicate": 1,
    "seconds_per_forward": 0.003318425000179559,
    "threads": 1,
    "timed_forwards": 5
  },
  {
    "baseline_RSS_bytes": 299679744,
    "batch": 4,
    "dtype": "float32",
    "length": 512,
    "model": "Reference attention",
    "parameters": 633,
    "peak_RSS_bytes": 328908800,
    "platform": "Darwin",
    "replicate": 2,
    "seconds_per_forward": 0.003477283401298337,
    "threads": 1,
    "timed_forwards": 5
  }
]
```

## Publication verification

At content verification, commit `9e54c89c6718bed04da3d382b07558b9154ae54f` matched remote main and all 188 file blobs with a clean working tree. Final metadata and all seven notebooks are separately verified through commit-addressed raw files in the local delivery evidence. Only companion artifacts are published.
