# Chapter 39 execution evidence

**Date:** 22 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_206 | 39.1 | 4 | 2 | 1.641 |
| code_207 | 39.2 | 4 | 2 | 1.674 |
| code_208 | 39.3 | 4 | 2 | 1.758 |
| code_209 | 39.4 | 4 | 2 | 2.343 |
| code_210 | 39.5 | 4 | 2 | 1.424 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

# Chapter 39 mechanisms, controls and interpretation

Five original laboratories retain all five scopes and both visual briefs. They execute 20 code cells with ten inline figures. Ordinary execution is self-contained, offline and CPU-only; no file, credential, dependency or model/dataset asset is added. Runtime remains CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and threadpoolctl 3.7.0. Source access/execution date: 22 October 2026, Australia/Melbourne; literature cutoff: 18 October 2026.

- **206 / shift identification:** Source 1,600 independent load/material records; fixed 100-iteration HGB. Four 800-record final domains: familiar, covariate prevalence/load shift with unchanged conditional law, unsupported higher loads, and an exactly identical familiar input array with reversed load effect. Familiar/conditional Brier 0.145137/0.484303 and error 0.19875/0.70125. Every deterministic input diagnostic is unchanged for the conditional control. Unsupported Brier 0.025781 with 0.975 positive prevalence is retained: novelty is not proof of numerical failure, and this favourable finite score is not unrestricted validity. Separate exact label-first generator holds Normal(-1,1)/Normal(1,1) class-conditional sensor laws fixed while prior changes 0.3→0.7. Source logistic on 2,000 records, 1,000 independent target observations; explicitly oracle prior correction improves Brier 0.142056→0.099574. No unlabeled prior-estimation claim. Visual A contrasts source envelope/domain changes with response-law changes.
- **207 / measurement faults:** Independent 1,200 source/500 final eight-step AR(0.8) trajectories, two noisy scaled sensors. Current/previous measurements predict current latent state plus noise. Native HGB clean fit versus clean plus three source-only augmentation copies (4,800 rows total): noise SD 0.2, channel-one bias up to 0.3, 15% whole-channel dropout. Final three-level tests distinguish noise amplitude, fraction with missing channel, calibration bias and fraction delayed by two steps. Complete dropout RMSE clean/augmented 0.389845/0.096916; strongest bias 0.319945/0.151963; all delayed 0.272672/0.138070. Strongest added noise worsens slightly with augmentation: 0.290728/0.304240. Current targets stay unchanged under stale packets; NaN is explicit missingness, not zero. Known milli-unit conversion actually restores original features: clean RMSE 0.452190 uncorrected→0.090553 converted; augmented 0.247341→0.082086. Disjoint metadata fixtures reject 50 unknown units, 50 stale records and ten infinities; 390 accepted, 110 unresolved rejects. Accepted RMSE is separate from service obligations. Validators do not identify in-range bias or hidden conditional changes.
- **208 / structural axes:** Actual complex dynamic chain solver (K−omega²I+i0.04omegaI)u=f. Source 1,000 independent chains, n=3–6, positive EA5–8, length0.8–1.2, load0.5–1.5, frequency0–0.1 in declared reference units. Actual 100-iteration HGB on five raw fields; separate known-physics response with fitted nonnegative scale 1.000109 is privileged correct-model information. Independent 200 entities per axis. Raw RMSE familiar 0.032913, graph size 0.770266, length 0.650269, material 2.660664, load 1.854571, frequency 3.247854; physical-scaling RMSE about 0.01 throughout while equations remain correct. Higher-frequency response reaches 16.719668. Separate added tip-to-ground spring changes boundary mechanism without visible feature change: raw/assumed-free-tip/metadata-informed oracle RMSE 0.622510/0.621596/0.010385. Oracle is a consistency comparator, not an adapted learner. Exact force scaling and independent new-entity semantics are checked.
- **209 / validity board:** Actual 2D rotated positive anisotropic stiffness, known force and free displacement, fixed node0. Source 1,200 elements with narrow angle support; source StandardScaler, degree-two PolynomialFeatures and Ridge alpha1. Familiar 300-element RMSE 0.061766 mm, force residual RMS 0.119105 kN. Joint geometry/force ninety-degree rotation keeps exact solver covariance but learned RMSE 19.820527 mm, force residual RMS 41.038519 kN, covariance error 19.815292 mm. Severe polynomial extrapolation failure retained. Seven first-query fixtures separate measured-force and simulator-true-force audits, rotated prediction, zero field, changed clamp with old solution, and correct constrained solution. Zero field passes original support and nonnegative energy but residual 0.494205 kN. Old equilibrium solution passes the remaining free equation but violates new clamp by 0.123727 mm; constrained solver passes both. Missing force is rejected before inference. Visual B aligns all faults with their specific checks; energy/support/equilibrium are not interchangeable acceptance certificates. Board uses a symmetric-log residual axis so the smaller nonzero defects remain visible.
- **210 / adaptation:** Source 400 standard-normal inputs, target pool 200 Normal(1,1), nonlinear common response x²+0.4x plus noise0.2; fixed linear family intentionally misspecified. Actual empirical regression; known simulator density ratio exp(x−0.5) capped at ten (ESS168.045615); true convex group-max epigraph regression with L2 penalty0.01 and two source sign groups, successful SLSQP/constraint slack about2e−14; unlabeled mean alignment with shift1.173417; random versus high-input target acquisition of forty labels each, selected before labels, same hidden pool outcomes and equal source/selected-target aggregate weight. Final 800 familiar/800 target records are independent and never select a route. Target RMSE source2.851772/weighted1.625031/groupmax2.739477/alignment3.092172/random40 1.701665/targeted40 1.954459. Acquisition targeting and mean alignment are not automatically beneficial; familiar-population tradeoffs remain in outputs. A changed-response stress adds4 above x=1 using the exact same target inputs. Frozen source1–99% envelope[−2.118505,2.253442] accepts709/800 target and defers91, identically under changed law. Accepted source-model RMSE1.460477→3.986199; deferrals are unresolved, not counted as correct. No universal OOD, adaptive-release or fallback-correctness guarantee.

Initial job launcher mistakenly resolved the virtual-environment Python symlink to base Python and failed on its missing nbformat import before any notebook ran. The corrected launcher uses sys.executable inside the existing environment; all fresh kernels pass. A notebook syntax error was caught by builder compilation and repaired before209 execution.210 was rerun after coupling acquisition strategies to the same hidden pool outcomes;209 was rerun for the board's residual-axis readability. Markdown guide links were corrected to Chapter39 without changing executed code. All final source code and numerical RESULT dictionaries are rerun during isolated vector export and agree exactly. Ten original SVG/vector-PDF/PNG sets and actual inline versions are reviewed during delivery. All assertions pass and current notebooks contain no errors or stderr. Primary PDFs for WILDS, covariate-weighted validation and group DRO were inspected; these original teaching mechanisms do not reproduce their datasets, algorithms in full or benchmark improvements. Chapters40–43 and the whole-book audit remain required.

## Successful result dictionaries

### code_206

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8006.

```json
{
  "conditional_inputs_byte_identical": true,
  "conditional_shift_observable_from_inputs_alone": false,
  "domain_scores": {
    "Conditional": {
      "Brier": 0.48430330830123713,
      "error": 0.70125,
      "n": 800,
      "outside_declared_range": 0.0,
      "prevalence": 0.4125
    },
    "Covariate": {
      "Brier": 0.1787268696846705,
      "error": 0.245,
      "n": 800,
      "outside_declared_range": 0.0,
      "prevalence": 0.72
    },
    "Familiar": {
      "Brier": 0.14513740658926064,
      "error": 0.19875,
      "n": 800,
      "outside_declared_range": 0.0,
      "prevalence": 0.425
    },
    "Unsupported": {
      "Brier": 0.025781129352213824,
      "error": 0.025,
      "n": 800,
      "outside_declared_range": 1.0,
      "prevalence": 0.975
    }
  },
  "label_shift_scores": {
    "Oracle target prior": {
      "Brier": 0.09957402713960439,
      "mean_probability": 0.6888122478491082
    },
    "Source prior": {
      "Brier": 0.14205602732936523,
      "mean_probability": 0.5043131118272569
    }
  },
  "label_shift_source_prior": 0.3,
  "label_shift_target_empirical_prevalence": 0.669,
  "label_shift_target_prior": 0.7,
  "prior_correction_uses_oracle_simulator_prior": true,
  "source_records": 1600
}
```

### code_207

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8007.

```json
{
  "accepted_packet_RMSE": {
    "Augmented fit": 0.08235533574614459,
    "Clean fit": 0.08866252910871224
  },
  "augmentation_source_rows": 4800,
  "challenge_RMSE": {
    "Calibration bias 0": {
      "Augmented fit": 0.08208632850158316,
      "Clean fit": 0.09055321068090352
    },
    "Calibration bias 0.5": {
      "Augmented fit": 0.11321992749271766,
      "Clean fit": 0.18376604907725888
    },
    "Calibration bias 1": {
      "Augmented fit": 0.15196343707982685,
      "Clean fit": 0.319944601143324
    },
    "Delayed packet 0": {
      "Augmented fit": 0.08208632850158316,
      "Clean fit": 0.09055321068090352
    },
    "Delayed packet 0.5": {
      "Augmented fit": 0.11112432406000071,
      "Clean fit": 0.19470117119100422
    },
    "Delayed packet 1": {
      "Augmented fit": 0.13807020822113206,
      "Clean fit": 0.2726722278386174
    },
    "Missing channel 0": {
      "Augmented fit": 0.08208632850158316,
      "Clean fit": 0.09055321068090352
    },
    "Missing channel 0.5": {
      "Augmented fit": 0.08950719717269656,
      "Clean fit": 0.2882586067460133
    },
    "Missing channel 1": {
      "Augmented fit": 0.09691590884050431,
      "Clean fit": 0.3898453619171724
    },
    "Noise 0": {
      "Augmented fit": 0.08208632850158316,
      "Clean fit": 0.09055321068090352
    },
    "Noise 0.5": {
      "Augmented fit": 0.168340082789479,
      "Clean fit": 0.167770903596004
    },
    "Noise 1": {
      "Augmented fit": 0.3042398286072513,
      "Clean fit": 0.29072754511891774
    }
  },
  "delayed_channel_steps": 2,
  "final_outcomes_select_augmentation": false,
  "final_sequences": 500,
  "packet_validation": {
    "accepted": 390,
    "infinite_values": 10,
    "rejected": 110,
    "stale_packets": 50,
    "unknown_units": 50
  },
  "source_sequences": 1200,
  "unit_scale_challenge": {
    "Augmented fit": {
      "converted_RMSE": 0.08208632850158316,
      "uncorrected_RMSE": 0.24734102733451327
    },
    "Clean fit": {
      "converted_RMSE": 0.09055321068090352,
      "uncorrected_RMSE": 0.4521896666595894
    }
  },
  "validator_does_not_identify_hidden_conditional_shift": true
}
```

### code_208

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8008.

```json
{
  "axis_challenge_scores": {
    "Familiar": {
      "entities": 200,
      "physical_scaling_RMSE": 0.010179451199069293,
      "raw_RMSE": 0.03291299374355887,
      "true_tip_range": [
        0.17258687551017587,
        1.9722826428612268
      ]
    },
    "Frequency": {
      "entities": 200,
      "physical_scaling_RMSE": 0.010159823920644394,
      "raw_RMSE": 3.2478536719872966,
      "true_tip_range": [
        0.32947434004853604,
        16.71966840882771
      ]
    },
    "Geometry": {
      "entities": 200,
      "physical_scaling_RMSE": 0.010215114580141248,
      "raw_RMSE": 0.6502689436869811,
      "true_tip_range": [
        0.5340442201670573,
        3.100325965673381
      ]
    },
    "Graph size": {
      "entities": 200,
      "physical_scaling_RMSE": 0.009985433178322359,
      "raw_RMSE": 0.770265828550878,
      "true_tip_range": [
        0.5705779567337996,
        3.2782993076264466
      ]
    },
    "Load": {
      "entities": 200,
      "physical_scaling_RMSE": 0.009664178043850955,
      "raw_RMSE": 1.854570931928897,
      "true_tip_range": [
        1.00211641169526,
        5.208238376517976
      ]
    },
    "Material": {
      "entities": 200,
      "physical_scaling_RMSE": 0.009648999965103083,
      "raw_RMSE": 2.6606637127482315,
      "true_tip_range": [
        0.7696483798503292,
        8.935981569577788
      ]
    }
  },
  "changed_support_RMSE": {
    "Assumed free tip physics": 0.6215960796466303,
    "Raw-feature boost": 0.6225097372906803,
    "Support-informed oracle physics": 0.010385239461216372
  },
  "changed_support_oracle_is_not_adapted_model": true,
  "extra_support_omitted_from_predictor_inputs": true,
  "learned_physical_scale": 1.000109186994295,
  "linear_force_scaling_checked": true,
  "solver_is_privileged_known_equation": true,
  "source_entities": 1000,
  "source_graph_sizes": [
    3,
    6
  ]
}
```

### code_209

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8009.

```json
{
  "coordinate_model_not_equivariant": true,
  "energy_nonnegative_does_not_ensure_equilibrium": true,
  "exact_solver_rotation_covariance": true,
  "final_elements": 300,
  "geometry_scores": {
    "Familiar": {
      "RMSE_mm": 0.06176607086112501,
      "force_residual_RMS_kN": 0.1191045310126586
    },
    "Rotated": {
      "RMSE_mm": 19.820527132017833,
      "force_residual_RMS_kN": 41.03851916754654
    }
  },
  "learned_rotation_covariance_RMSE_mm": 19.815292349885553,
  "missing_force_rejected": true,
  "physical_stress_board": [
    {
      "displacement_error_mm": 0.04146112621102369,
      "fixture": "Familiar learned",
      "free_equation_residual_kN": 0.0737480038260572,
      "strain_energy_kN_mm": 0.09174437668252751,
      "support_residual_mm": 0.0
    },
    {
      "displacement_error_mm": 0.05417937653073305,
      "fixture": "Noisy measured force",
      "free_equation_residual_kN": 0.08593668519218711,
      "strain_energy_kN_mm": 0.10344543133607965,
      "support_residual_mm": 0.0
    },
    {
      "displacement_error_mm": 0.16908147953992228,
      "fixture": "Noisy true force audit",
      "free_equation_residual_kN": 0.180930250471535,
      "strain_energy_kN_mm": 0.10344543133607965,
      "support_residual_mm": 0.0
    },
    {
      "displacement_error_mm": 18.242142957144527,
      "fixture": "Rotated learned",
      "free_equation_residual_kN": 31.663702477886343,
      "strain_energy_kN_mm": 278.2292196102535,
      "support_residual_mm": 0.0
    },
    {
      "displacement_error_mm": 0.2853848256908004,
      "fixture": "Zero displacement",
      "free_equation_residual_kN": 0.49420501997393523,
      "strain_energy_kN_mm": 0.0,
      "support_residual_mm": 0.0
    },
    {
      "displacement_error_mm": 0.12397131875546225,
      "fixture": "Changed support old solve",
      "free_equation_residual_kN": 0.0,
      "strain_energy_kN_mm": 0.07007308835626587,
      "support_residual_mm": 0.12372675301886105
    },
    {
      "displacement_error_mm": 0.0,
      "fixture": "Changed support correct",
      "free_equation_residual_kN": 0.0,
      "strain_energy_kN_mm": 0.061812337563615455,
      "support_residual_mm": 0.0
    }
  ],
  "solver_force_scaling_checked": true,
  "source_elements": 1200
}
```

### code_210

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8010.

```json
{
  "adaptation_family": "fixed linear intercept+slope",
  "conditional_change_keeps_same_inputs": true,
  "deferred_cases_counted_as_correct": false,
  "final_RMSE": {
    "Group max": {
      "Changed response": 5.187456065637795,
      "Covariate target": 2.739477373854633,
      "Familiar": 1.5878243122403308
    },
    "Mean alignment": {
      "Changed response": 5.635282480552143,
      "Covariate target": 3.0921720858257573,
      "Familiar": 1.5895935250850495
    },
    "Random 40 labels": {
      "Changed response": 3.435994427616863,
      "Covariate target": 1.701664828570896,
      "Familiar": 2.0528493396062104
    },
    "Ratio weighted": {
      "Changed response": 3.6831972734358374,
      "Covariate target": 1.625030616920053,
      "Familiar": 2.2557502967093557
    },
    "Source ERM": {
      "Changed response": 5.314919439228573,
      "Covariate target": 2.8517717586966547,
      "Familiar": 1.5895935250850495
    },
    "Targeted 40 labels": {
      "Changed response": 2.64836431733067,
      "Covariate target": 1.9544587081253595,
      "Familiar": 2.51757415109495
    }
  },
  "final_scores_select_route": false,
  "group_max_coefficients": [
    0.899791467979574,
    0.5183192788214817
  ],
  "group_max_constraint_slacks": [
    2.0650148258027912e-14,
    1.6653345369377348e-14
  ],
  "group_max_optimizer_success": true,
  "known_density_ratio_is_simulator_oracle": true,
  "random_indices": [
    20,
    46,
    29,
    132,
    141,
    23,
    117,
    57,
    75,
    15,
    150,
    131,
    101,
    98,
    119,
    158,
    7,
    94,
    175,
    32,
    168,
    36,
    121,
    10,
    192,
    41,
    3,
    35,
    4,
    16,
    54,
    142,
    111,
    147,
    173,
    56,
    120,
    87,
    27,
    62
  ],
  "ratio_clipping": 10,
  "ratio_effective_sample_size": 168.04561539825795,
  "source_acceptance_envelope": [
    -2.1185049029816505,
    2.253441859635752
  ],
  "source_predictor_gate_results": {
    "Changed response": {
      "accepted": 709,
      "accepted_RMSE": 3.9861987025519654,
      "coverage": 0.88625,
      "deferred": 91
    },
    "Covariate target": {
      "accepted": 709,
      "accepted_RMSE": 1.460477096155378,
      "coverage": 0.88625,
      "deferred": 91
    },
    "Familiar": {
      "accepted": 775,
      "accepted_RMSE": 1.0443286942607957,
      "coverage": 0.96875,
      "deferred": 25
    }
  },
  "source_records": 400,
  "target_label_budget_each": 40,
  "target_unlabelled_pool": 200,
  "targeted_indices": [
    123,
    140,
    180,
    55,
    114,
    192,
    9,
    191,
    7,
    53,
    23,
    2,
    40,
    30,
    79,
    187,
    50,
    156,
    121,
    68,
    27,
    103,
    171,
    199,
    153,
    16,
    116,
    195,
    11,
    173,
    181,
    147,
    64,
    12,
    42,
    47,
    189,
    32,
    158,
    43
  ],
  "targeted_selection_uses_labels": false,
  "unlabelled_alignment_shift": 1.173417214040519
}
```

