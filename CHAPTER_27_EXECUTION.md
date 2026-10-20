# Chapter 27 execution evidence

**Date:** 21 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content revision verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_138 | 27.1 | 4 | 2 | 2.943 |
| code_139 | 27.2 | 4 | 2 | 3.511 |
| code_140 | 27.3 | 4 | 2 | 4.415 |
| code_141 | 27.4 | 4 | 2 | 5.831 |
| code_142 | 27.5 | 4 | 2 | 3.371 |
| code_143 | 27.6 | 4 | 2 | 2.674 |

Total: **24 executed code cells and 12 inline figures**. Current outputs contain no errors and all assertions pass. All twelve inline figures and twelve reproduced book figures were visually inspected during the book delivery review.

## Actual mechanisms and boundaries

## Mechanisms, controls and limits

All cohorts are generated locally. Source/development/final entities remain whole groups; generated draws are not new independent observed entities. Existing native Torch 2.14.1 CPU float 64 and numerical dependencies are unchanged. Seeds 3338–3343, deterministic Torch operations and one-thread limits are printed. Ordinary runs need no files, downloads, keys or GPU. No resource-profile exception is used: book figure generation reruns every current code cell and requires exact deterministic RESULTS agreement.

- **138 · generation contracts.** Sixty buildings × 20 records split 40/10/10 (800/200/200). Positive load/stiffness are exponentiated joint log summaries; their ratio is a declared scalar teaching rule, not a beam law. Independent Gaussian marginals, a joint full-covariance GMM and regime-conditional GMMs retain candidates 1/2/4, two initializations and convergence checks. Development log density chooses joint 1 and conditional 4/1 components. Reported conditional density concerns the continuous pair given regime and omits its common scenario prior. Two thousand draws per generator; final correlations 0.841 reference versus−0.001/0.757/0.764. Conditional-mean completion on 50 final records preserves observed coordinates exactly, MSE 0.1526 versus 0.2469. Linked tables 20 parents/83 members/83 inspections have zero structural violations; the retained independent fixture has 18 orphan inspections and 41 reports before events. No row-independent confidence intervals are claimed.
- **139 · mixed-output conditional VAE.** Eighty buildings × 16 split 50/15/15 (800/240/240); source rare condition 115 records, final 32. Actual 846-parameter encoder/decoder, two Gaussian latent coordinates, four continuous Gaussian heads, Bernoulli alarm and Poisson count. Continuous-only source scaling and log Jacobian−1.53838 keep reported scores in original log-summary units; all normalization constants/factorials remain. Beta 0.1/1/8 each 1400 updates at 0.003, identical minibatch orders and reset initialization. Every 50 updates, a common beta-one development ELBO with four fixed noise draws selects checkpoints 500/1050/1050; weight 1 wins. Final Monte Carlo uses fresh separate noise panels for each candidate, not common random numbers. Final common negative ELBO 4.6767/3.7648/6.3008; weight 8 KL≈0.000097/0.001407 and weak measured decoder sensitivity support collapse-like behavior. Type-valid draws 1000 percondition/recipe still miss a rare continuous tail:0.085/0.122/0.153 versus 0.28125 in 32 reference records. Binary/count types are sampled rather than rounded. A zero-KL prior identity adds a meaningful nonrandom check; it leaves fitted results unchanged.
- **140 · native conditional adversaries.** Ninety buildings × 12 split 60/15/15 (720/180/180); source/final failure counts 60/12. Own 1250-parameter generator/1217-parameter discriminator or critic, no complete CTGAN implementation. Balanced conditional minibatches are scenario weighting, not the historical prevalence. Three fixed 1000-generator-update recipes: logistic cGAN 0.001, aggressive generator 0.03/discriminator 0.001, and WGAN-GP 0.001 with 3000 critic updates/penalty 10. Sixteen-direction, equal-condition development projected Wasserstein and fixed noise choose checkpoints 1000/800/600. All recipes remain; aggressive generator produces no positive-mode records in either class. Bootstrap and fitted conditional Gaussian controls remain. Each adds 360 failure records to the same logistic classifier, moving training prevalence 0.0833→0.3889. Source Brier 0.05608; all augmented recipes worsen it (0.07884–0.14940), with average precision retained separately. An initial unpublished implementation computed an unused, incorrectly weighted interpolation before overwriting it with the correct convex pair. The unused calculation was removed; actual GP always used the correct second interpolation. This cleanup changes the WGAN random-number stream, selected checkpoint and metrics; no budget, learning rate or final-tuned selection changed. The old snapshot is retained locally as tmp/chapter27/140-before-interpolation-cleanup.json. Assertions check convex bounds and gradient shape/finiteness. All current scatter panels use condition 1 and shared axes, so rare reference size and collapse remain visible.
- **141 · three actual mechanisms.** Ninety entities × 10 split 60/15/15. The explicit mixed autoregression fits regime frequency, Gaussian first-coordinate conditionals, polynomial Gaussian response and Poisson count MLE with convergence checked. Mixed joint final log likelihood−3.0643 and generated/reference count mean 1.5725/1.14 remain. Own 4632-parameter continuous flow has six alternating affine-coupling blocks, bounded log scales, Gaussian base, analytic inverse/log determinants and source-unit Jacobian. Round trips and an autograd-Jacobian determinant are independently checked.1200 Adam updates 0.003, development every 100 selects 800; final continuous NLL 1.62253. This two-coordinate marginal is not ranked against the mixed joint score. Own 1185-parameter bounded tanh energy plus quadratic tail has an integrable ideal density but an uncomputed partition function.500 updates 0.001, persistent 256 negatives with 20 Langevin steps/update at 0.04, separate fixed 150-step development panels select 400; final generation 400 steps. Initialization sensitivity remains: common-noise zero/three chain means differ by 0.1736 after 400 steps. Final projected distances 0.09043/0.12724/0.14808. No equilibrium, exact EBM likelihood or original-paper benchmark reproduction is claimed.
- **142 · diffusion and flow matching.** Eighty entities × 10 split 48/16/16 (480/160/160), four physical sensor-time coordinates. Source-only scaling. Each own 4932-parameter method gets rates 0.001/0.003 × 1200 updates, common source minibatches, fixed development noise/time panels and checkpoints every 100. Each selects rate 0.003; DDPM 1200, flow matching 1100. Their own development objectives are not shared likelihoods. Actual DDPM epsilon training uses 60 linear beta steps 0.001→0.15, terminal signal fraction 0.0084178, declared posterior reverse variance and 60 network evaluations. Separate independent-Gaussian/data straight-path velocity regression samples through midpoint ODE 20/80 steps (40/160 evaluations); common-noise standardized refinement RMS 0.001726/0.001787 acrossconditions. Condition 0/1 reference counts 131/29. Final projected distances DDPM 0.07399/0.10700, FM 0.12314/0.08536; covariance and positive-level modes remain. No speedup or dataset-level optimal coupling is claimed, and this straight path is not equated with the DDPM probability-flow ODE. First execution exposed a local tensor called time shadowing the runtime module only at summary serialization; it was renamed step_time and the whole notebook rerun without changing training controls. Visual A aligns a conceptual conditional sensor request across mechanisms; earlier notebooks use different tasks, and 141's flow is unconditional. Training corruption/path arrows, condition routes and fit objectives are distinct.
- **143 · acceptance and disclosure.** One hundred entities × 8 split 60/20/20 (480/160/160). All data and the conspicuous source-only [8,8] canary are generated. Bootstrap, independent marginal resampling and conditional GMM 1/2 candidates produce 3000 diagnostic records each; both conditional mixtures select 2 bydevelopment. The first 480 draws give equal-size synthetic-only or augmented classifiers, with fixed source scaling/LogisticRegression C 1. Source Brier 0.09647; conditional synthetic-only 0.09674 and independent synthetic-only 0.14686. No precise improvement claim from single-seed differences. Independent marginals miss correlation (−0.0505 vs 0.8355 reference). Valid constraints have zero failures; invalid fixture 15 inspectionFK/47 chronology/3000 ratio violations. The ratio is scalar algebra, not mechanics. Validity uses a disclosed symlog count axis to keep small failures visible beside 3000 ratio failures. Membership thresholds calibrate on source members 1:240 (canary excluded) and development nonmembers, then test 240 other members/160 final nonmembers. This is an assumed known-membership attack, not shadow-model or universal adversary coverage. Bootstrap AUC 0.99836/copyfraction 1/canarycopies 2. Conditional mixture AUC 0.48471/no exact copies, yet canary proximity 0.001004 in source-standardized distance. Independent marginals copy 0.001667 of whole source rows despite independently resampling fields. Initial brute-force nearest-neighbor distances suffered cancellation at identical rows and failed the exact-copy assertion; the corrected source uses native coordinate-based KD-tree distances, then reruns all code. The tolerance remains 1 e−12; no assertion or requirement was weakened. Attack failure and novel rows do not supply a DP guarantee. No DP mechanism/accountant is implemented.

## Sources and review boundaries

Primary records for VAE, GAN, WGAN-GP, CTGAN, MADE, Real NVP, neural energy learning, DDPM, flow matching, membership inference and Dwork/Roth's privacy definition/postprocessing are cited directly. Publication dates and author lists were checked; current access 20–21 October 2026 does not change the 18 October 2026 literature cutoff. Own implementations are distinguished from complete named packages and original benchmark results. All negative outcomes and numerical/sampler limitations remain. The prose also derives the score interpretation and scalar-noise probability-flow equation from Song et al. (2011.13456 v 2), with matched-marginal assumptions and no claim to execute a continuous score-SDE sampler. Author list, submission 26 November 2020/revision 10 February 2021 and method equations verified 21 October 2026. Nineteen exercises and the six-scope code map connect evidence to use. No private-data, formal-privacy, causal or field-engineering claim follows from these generated examples.

## Successful result dictionaries

### code_138

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3338.

```json
{
  "building_counts": [
    40,
    10,
    10
  ],
  "comparisons": [
    {
      "final_conditional_log_density": -1.631999521232751,
      "generated_records": 2000,
      "generator": "Independent fields",
      "log_field_correlation": -0.0010620053503199234,
      "regime_load_log_mean_difference": 0.04396399795452899,
      "response_mean": 4.304316737439849,
      "response_q95": 11.402392970130693
    },
    {
      "final_conditional_log_density": -1.1986267781504398,
      "generated_records": 2000,
      "generator": "Joint mixture",
      "log_field_correlation": 0.7568673718989509,
      "regime_load_log_mean_difference": -0.09702442580812853,
      "response_mean": 3.6300735225837863,
      "response_q95": 6.204926113610462
    },
    {
      "final_conditional_log_density": -1.1625506347036532,
      "generated_records": 2000,
      "generator": "Conditional mixture",
      "log_field_correlation": 0.7638263560820585,
      "regime_load_log_mean_difference": 0.29257298634844586,
      "response_mean": 3.5386647824709763,
      "response_q95": 6.1367292707174315
    }
  ],
  "conditional_completion_MSE": 0.1525850635984643,
  "final_log_field_correlation": 0.8407952923529949,
  "final_regime_load_log_mean_difference": 0.27383552159047886,
  "independent_table_audit": {
    "orphan_inspections": 18,
    "orphan_members": 0,
    "reports_before_events": 41
  },
  "linked_table_counts": [
    20,
    83,
    83
  ],
  "mixture_candidates": [
    {
      "components": 1,
      "development_mean_log_density": -0.9478619979416841,
      "scope": "Joint"
    },
    {
      "components": 2,
      "development_mean_log_density": -0.9570116884658084,
      "scope": "Joint"
    },
    {
      "components": 4,
      "development_mean_log_density": -0.9712947867353698,
      "scope": "Joint"
    },
    {
      "components": 1,
      "development_mean_log_density": -0.9643067602235887,
      "scope": "Condition 0"
    },
    {
      "components": 2,
      "development_mean_log_density": -0.959092349287834,
      "scope": "Condition 0"
    },
    {
      "components": 4,
      "development_mean_log_density": -0.9584023301824103,
      "scope": "Condition 0"
    },
    {
      "components": 1,
      "development_mean_log_density": -0.7717012279646392,
      "scope": "Condition 1"
    },
    {
      "components": 2,
      "development_mean_log_density": -0.7781146313070039,
      "scope": "Condition 1"
    },
    {
      "components": 4,
      "development_mean_log_density": -0.8230336622695211,
      "scope": "Condition 1"
    }
  ],
  "record_counts": [
    800,
    200,
    200
  ],
  "selected_conditional_components": {
    "0": 4,
    "1": 1
  },
  "selected_joint_components": 1,
  "source_regime_prevalence": 0.1925,
  "unconditional_completion_MSE": 0.24685642382189443,
  "valid_table_audit": {
    "orphan_inspections": 0,
    "orphan_members": 0,
    "reports_before_events": 0
  }
}
```

### code_139

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3339.

```json
{
  "building_counts": [
    50,
    15,
    15
  ],
  "comparisons": [
    {
      "best_update": 500,
      "beta": 0.1,
      "decoder_latent_mean_variance_condition1": 0.5911475266049133,
      "development_negative_ELBO_common_beta1": 4.613809717678315,
      "final_KL_per_latent": [
        3.0005026384639404,
        3.459203520110447
      ],
      "final_negative_ELBO_common_beta1": 4.676657247346858,
      "parameters": 846
    },
    {
      "best_update": 1050,
      "beta": 1.0,
      "decoder_latent_mean_variance_condition1": 0.8120883306590796,
      "development_negative_ELBO_common_beta1": 3.692331197327659,
      "final_KL_per_latent": [
        0.9734334138278707,
        2.1198767555877036
      ],
      "final_negative_ELBO_common_beta1": 3.7647639894767484,
      "parameters": 846
    },
    {
      "best_update": 1050,
      "beta": 8.0,
      "decoder_latent_mean_variance_condition1": 0.011501437392197047,
      "development_negative_ELBO_common_beta1": 6.160236460281421,
      "final_KL_per_latent": [
        9.704663376960133e-05,
        0.0014074060702904928
      ],
      "final_negative_ELBO_common_beta1": 6.300766811532737,
      "parameters": 846
    }
  ],
  "conditional_generation": [
    {
      "beta": 0.1,
      "condition": 0,
      "generated_alarm_rate": 0.44,
      "generated_count_mean": 1.653,
      "generated_first_log_summary_tail_gt2_5": 0.018,
      "generated_records": 1000,
      "reference_alarm_rate": 0.33653846153846156,
      "reference_count_mean": 1.5336538461538463,
      "reference_records": 208,
      "reference_tail_gt2_5": 0.028846153846153848
    },
    {
      "beta": 0.1,
      "condition": 1,
      "generated_alarm_rate": 0.738,
      "generated_count_mean": 2.505,
      "generated_first_log_summary_tail_gt2_5": 0.085,
      "generated_records": 1000,
      "reference_alarm_rate": 0.75,
      "reference_count_mean": 3.09375,
      "reference_records": 32,
      "reference_tail_gt2_5": 0.28125
    },
    {
      "beta": 1.0,
      "condition": 0,
      "generated_alarm_rate": 0.368,
      "generated_count_mean": 1.504,
      "generated_first_log_summary_tail_gt2_5": 0.014,
      "generated_records": 1000,
      "reference_alarm_rate": 0.33653846153846156,
      "reference_count_mean": 1.5336538461538463,
      "reference_records": 208,
      "reference_tail_gt2_5": 0.028846153846153848
    },
    {
      "beta": 1.0,
      "condition": 1,
      "generated_alarm_rate": 0.75,
      "generated_count_mean": 2.585,
      "generated_first_log_summary_tail_gt2_5": 0.122,
      "generated_records": 1000,
      "reference_alarm_rate": 0.75,
      "reference_count_mean": 3.09375,
      "reference_records": 32,
      "reference_tail_gt2_5": 0.28125
    },
    {
      "beta": 8.0,
      "condition": 0,
      "generated_alarm_rate": 0.338,
      "generated_count_mean": 1.54,
      "generated_first_log_summary_tail_gt2_5": 0.012,
      "generated_records": 1000,
      "reference_alarm_rate": 0.33653846153846156,
      "reference_count_mean": 1.5336538461538463,
      "reference_records": 208,
      "reference_tail_gt2_5": 0.028846153846153848
    },
    {
      "beta": 8.0,
      "condition": 1,
      "generated_alarm_rate": 0.726,
      "generated_count_mean": 2.748,
      "generated_first_log_summary_tail_gt2_5": 0.153,
      "generated_records": 1000,
      "reference_alarm_rate": 0.75,
      "reference_count_mean": 3.09375,
      "reference_records": 32,
      "reference_tail_gt2_5": 0.28125
    }
  ],
  "continuous_source_log_jacobian": -1.5383786689801684,
  "final_rare_condition_records": 32,
  "latent_dimensions": 2,
  "record_counts": [
    800,
    240,
    240
  ],
  "selected_beta": 1.0,
  "source_rare_condition_records": 115,
  "updates_per_beta": 1400
}
```

### code_140

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3340.

```json
{
  "added_failure_records_per_recipe": 360,
  "augmentation": [
    {
      "final_Brier": 0.056077619410624065,
      "final_average_precision": 0.27994768417810034,
      "training": "Source only",
      "training_failure_fraction": 0.08333333333333333,
      "training_records": 720
    },
    {
      "final_Brier": 0.11750473692059961,
      "final_average_precision": 0.27690573886884445,
      "training": "Bootstrap augmentation",
      "training_failure_fraction": 0.3888888888888889,
      "training_records": 1080
    },
    {
      "final_Brier": 0.11766374009761718,
      "final_average_precision": 0.2790408553945492,
      "training": "Conditional Gaussian augmentation",
      "training_failure_fraction": 0.3888888888888889,
      "training_records": 1080
    },
    {
      "final_Brier": 0.11418551602910727,
      "final_average_precision": 0.2529245987226822,
      "training": "Conditional GAN augmentation",
      "training_failure_fraction": 0.3888888888888889,
      "training_records": 1080
    },
    {
      "final_Brier": 0.07884266936085392,
      "final_average_precision": 0.2604961227286739,
      "training": "Aggressive generator augmentation",
      "training_failure_fraction": 0.3888888888888889,
      "training_records": 1080
    },
    {
      "final_Brier": 0.14940226123707184,
      "final_average_precision": 0.2798905462827994,
      "training": "Wasserstein GP augmentation",
      "training_failure_fraction": 0.3888888888888889,
      "training_records": 1080
    }
  ],
  "building_counts": [
    60,
    15,
    15
  ],
  "conditional_generation": [
    {
      "condition": 0,
      "final_projected_Wasserstein": 0.11076570974361742,
      "generated_positive_mode_fraction": 0.495,
      "generated_records": 1000,
      "model": "Bootstrap",
      "reference_positive_mode_fraction": 0.4880952380952381,
      "reference_records": 168
    },
    {
      "condition": 1,
      "final_projected_Wasserstein": 0.34634549824406624,
      "generated_positive_mode_fraction": 0.212,
      "generated_records": 1000,
      "model": "Bootstrap",
      "reference_positive_mode_fraction": 0.16666666666666666,
      "reference_records": 12
    },
    {
      "condition": 0,
      "final_projected_Wasserstein": 0.24720094224668865,
      "generated_positive_mode_fraction": 0.506,
      "generated_records": 1000,
      "model": "Conditional Gaussian",
      "reference_positive_mode_fraction": 0.4880952380952381,
      "reference_records": 168
    },
    {
      "condition": 1,
      "final_projected_Wasserstein": 0.4121316532272975,
      "generated_positive_mode_fraction": 0.238,
      "generated_records": 1000,
      "model": "Conditional Gaussian",
      "reference_positive_mode_fraction": 0.16666666666666666,
      "reference_records": 12
    },
    {
      "condition": 0,
      "final_projected_Wasserstein": 0.18958881572137276,
      "generated_positive_mode_fraction": 0.508,
      "generated_records": 1000,
      "model": "Conditional GAN",
      "reference_positive_mode_fraction": 0.4880952380952381,
      "reference_records": 168
    },
    {
      "condition": 1,
      "final_projected_Wasserstein": 0.4959236991568709,
      "generated_positive_mode_fraction": 0.258,
      "generated_records": 1000,
      "model": "Conditional GAN",
      "reference_positive_mode_fraction": 0.16666666666666666,
      "reference_records": 12
    },
    {
      "condition": 0,
      "final_projected_Wasserstein": 0.9076621374575327,
      "generated_positive_mode_fraction": 0.0,
      "generated_records": 1000,
      "model": "Aggressive generator",
      "reference_positive_mode_fraction": 0.4880952380952381,
      "reference_records": 168
    },
    {
      "condition": 1,
      "final_projected_Wasserstein": 0.9220556360517257,
      "generated_positive_mode_fraction": 0.0,
      "generated_records": 1000,
      "model": "Aggressive generator",
      "reference_positive_mode_fraction": 0.16666666666666666,
      "reference_records": 12
    },
    {
      "condition": 0,
      "final_projected_Wasserstein": 0.5111248638741008,
      "generated_positive_mode_fraction": 0.653,
      "generated_records": 1000,
      "model": "Wasserstein GP",
      "reference_positive_mode_fraction": 0.4880952380952381,
      "reference_records": 168
    },
    {
      "condition": 1,
      "final_projected_Wasserstein": 0.4823965823375271,
      "generated_positive_mode_fraction": 0.347,
      "generated_records": 1000,
      "model": "Wasserstein GP",
      "reference_positive_mode_fraction": 0.16666666666666666,
      "reference_records": 12
    }
  ],
  "development_directions": 16,
  "final_failure_records": 12,
  "fitting": [
    {
      "best_generator_update": 1000,
      "critic_parameters": 1217,
      "critic_updates": 1000,
      "development_equal_condition_distance": 0.22569461124398973,
      "generator_parameters": 1250,
      "generator_rate": 0.001,
      "generator_updates": 1000,
      "model": "Conditional GAN"
    },
    {
      "best_generator_update": 800,
      "critic_parameters": 1217,
      "critic_updates": 1000,
      "development_equal_condition_distance": 0.6694037096254732,
      "generator_parameters": 1250,
      "generator_rate": 0.03,
      "generator_updates": 1000,
      "model": "Aggressive generator"
    },
    {
      "best_generator_update": 600,
      "critic_parameters": 1217,
      "critic_updates": 3000,
      "development_equal_condition_distance": 0.5910889872277401,
      "generator_parameters": 1250,
      "generator_rate": 0.001,
      "generator_updates": 1000,
      "model": "Wasserstein GP"
    }
  ],
  "source_failure_records": 60
}
```

### code_141

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3341.

```json
{
  "autoregressive_count_generated_mean": 1.5725,
  "autoregressive_count_reference_mean": 1.14,
  "building_counts": [
    60,
    15,
    15
  ],
  "comparisons": [
    {
      "final_projected_Wasserstein": 0.09043162221452913,
      "generated_log_summary_correlation": 0.6900668708027331,
      "model": "Autoregressive"
    },
    {
      "final_projected_Wasserstein": 0.12723915724322946,
      "generated_log_summary_correlation": 0.6942313459956098,
      "model": "Coupling flow"
    },
    {
      "final_projected_Wasserstein": 0.14807850441131545,
      "generated_log_summary_correlation": 0.646854163652462,
      "model": "Energy + Langevin"
    }
  ],
  "energy_common_noise_initialization_mean_gap": 0.17359736337703863,
  "energy_final_sampling_steps": 400,
  "energy_langevin_step_size": 0.04,
  "energy_parameters": 1185,
  "energy_selected_update": 400,
  "energy_training_langevin_steps_per_update": 20,
  "energy_updates": 500,
  "flow_final_continuous_negative_log_likelihood": 1.6225286198905322,
  "flow_parameters": 4632,
  "flow_selected_update": 800,
  "flow_updates": 1200,
  "mixed_autoregressive_final_mean_log_likelihood": -3.064335796405325,
  "record_counts": [
    600,
    150,
    150
  ]
}
```

### code_142

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3342.

```json
{
  "building_counts": [
    48,
    16,
    16
  ],
  "conditional_assessment": [
    {
      "condition": 0,
      "covariance_Frobenius_error": 0.08419977717100394,
      "field_evaluations_per_sample": 60,
      "final_projected_Wasserstein": 0.07398827105474226,
      "generated_positive_level_fraction": 0.237,
      "generated_records": 1000,
      "method": "DDPM",
      "reference_positive_level_fraction": 0.21374045801526717,
      "reference_records": 131
    },
    {
      "condition": 0,
      "covariance_Frobenius_error": 0.15957420774558578,
      "field_evaluations_per_sample": 160,
      "final_projected_Wasserstein": 0.12314414933748694,
      "generated_positive_level_fraction": 0.264,
      "generated_records": 1000,
      "method": "Flow matching",
      "reference_positive_level_fraction": 0.21374045801526717,
      "reference_records": 131
    },
    {
      "condition": 1,
      "covariance_Frobenius_error": 0.3271994834045741,
      "field_evaluations_per_sample": 60,
      "final_projected_Wasserstein": 0.10699839909518855,
      "generated_positive_level_fraction": 0.595,
      "generated_records": 1000,
      "method": "DDPM",
      "reference_positive_level_fraction": 0.5517241379310345,
      "reference_records": 29
    },
    {
      "condition": 1,
      "covariance_Frobenius_error": 0.13949472500709842,
      "field_evaluations_per_sample": 160,
      "final_projected_Wasserstein": 0.0853608310764105,
      "generated_positive_level_fraction": 0.585,
      "generated_records": 1000,
      "method": "Flow matching",
      "reference_positive_level_fraction": 0.5517241379310345,
      "reference_records": 29
    }
  ],
  "ddpm_beta_endpoints": [
    0.001,
    0.15
  ],
  "ddpm_steps": 60,
  "ddpm_terminal_signal_fraction": 0.008417784900786684,
  "fitting": [
    {
      "development_own_objective": 0.1664333503392354,
      "method": "DDPM",
      "parameters": 4932,
      "rate": 0.001,
      "selected_update": 1200,
      "updates": 1200
    },
    {
      "development_own_objective": 0.161529162575162,
      "method": "DDPM",
      "parameters": 4932,
      "rate": 0.003,
      "selected_update": 1200,
      "updates": 1200
    },
    {
      "development_own_objective": 0.8064248702747157,
      "method": "Flow matching",
      "parameters": 4932,
      "rate": 0.001,
      "selected_update": 1200,
      "updates": 1200
    },
    {
      "development_own_objective": 0.7761595768070892,
      "method": "Flow matching",
      "parameters": 4932,
      "rate": 0.003,
      "selected_update": 1100,
      "updates": 1200
    }
  ],
  "flow_common_initial_noise_RMS_refinement_by_condition": [
    0.0017259839341319438,
    0.0017865601312137306
  ],
  "flow_field_evaluations": [
    40,
    160
  ],
  "flow_midpoint_steps": [
    20,
    80
  ],
  "record_counts": [
    480,
    160,
    160
  ]
}
```

### code_143

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3343.

```json
{
  "building_counts": [
    60,
    20,
    20
  ],
  "canary_original_log_coordinates": [
    8.0,
    8.0
  ],
  "deliberately_invalid_constraints": {
    "orphan_inspections": 15,
    "orphan_parents": 0,
    "report_before_event": 47,
    "response_ratio_violations": 3000
  },
  "disclosure": [
    {
      "attack_test_members": 240,
      "attack_test_nonmembers": 160,
      "calibrated_distance_threshold": 0.0,
      "canary_exact_copies": 2,
      "canary_nearest_distance": 0.0,
      "generated_exact_source_copy_fraction": 1.0,
      "generator": "Source bootstrap",
      "held_out_membership_AUC": 0.9983593749999999,
      "held_out_membership_balanced_accuracy": 0.9979166666666667
    },
    {
      "attack_test_members": 240,
      "attack_test_nonmembers": 160,
      "calibrated_distance_threshold": 0.01827473729165511,
      "canary_exact_copies": 0,
      "canary_nearest_distance": 8.163522642619442,
      "generated_exact_source_copy_fraction": 0.0016666666666666668,
      "generator": "Independent marginals",
      "held_out_membership_AUC": 0.5379947916666666,
      "held_out_membership_balanced_accuracy": 0.525
    },
    {
      "attack_test_members": 240,
      "attack_test_nonmembers": 160,
      "calibrated_distance_threshold": 0.038961794525174655,
      "canary_exact_copies": 0,
      "canary_nearest_distance": 0.0010043351852313722,
      "generated_exact_source_copy_fraction": 0.0,
      "generator": "Conditional mixture",
      "held_out_membership_AUC": 0.4847135416666666,
      "held_out_membership_balanced_accuracy": 0.5010416666666666
    }
  ],
  "fidelity": [
    {
      "generated_correlation": 0.8190440475288907,
      "generated_rare_tail_fraction_logload_gt2": 0.076,
      "generator": "Source bootstrap",
      "mean_marginal_Wasserstein": 0.09878205117114777,
      "reference_correlation": 0.835465679682193,
      "reference_rare_tail_fraction": 0.09375
    },
    {
      "generated_correlation": -0.050527974469805614,
      "generated_rare_tail_fraction_logload_gt2": 0.07766666666666666,
      "generator": "Independent marginals",
      "mean_marginal_Wasserstein": 0.11396827211094193,
      "reference_correlation": 0.835465679682193,
      "reference_rare_tail_fraction": 0.09375
    },
    {
      "generated_correlation": 0.8442551380378556,
      "generated_rare_tail_fraction_logload_gt2": 0.07233333333333333,
      "generator": "Conditional mixture",
      "mean_marginal_Wasserstein": 0.11613389735340889,
      "reference_correlation": 0.835465679682193,
      "reference_rare_tail_fraction": 0.09375
    }
  ],
  "generated_records_per_recipe": 3000,
  "mixture_selection": [
    {
      "components": 1,
      "condition": 0,
      "development_log_density": -2.1650758446988734
    },
    {
      "components": 2,
      "condition": 0,
      "development_log_density": -2.1162469909212436
    },
    {
      "components": 1,
      "condition": 1,
      "development_log_density": -2.585132032276114
    },
    {
      "components": 2,
      "condition": 1,
      "development_log_density": -2.3924361827196483
    }
  ],
  "record_counts": [
    480,
    160,
    160
  ],
  "selected_components": {
    "0": 2,
    "1": 2
  },
  "source_label_prevalence": 0.16041666666666668,
  "synthetic_classifier_records": 480,
  "utility": [
    {
      "final_Brier": 0.09647209266228615,
      "final_average_precision": 0.6645724507440222,
      "records": 480,
      "training": "Source only",
      "training_risk_fraction": 0.16041666666666668
    },
    {
      "final_Brier": 0.09501678960188409,
      "final_average_precision": 0.6638034742947049,
      "records": 480,
      "training": "Source bootstrap synthetic only",
      "training_risk_fraction": 0.16666666666666666
    },
    {
      "final_Brier": 0.09578789717835826,
      "final_average_precision": 0.6680633811415726,
      "records": 960,
      "training": "Source bootstrap augmented",
      "training_risk_fraction": 0.16354166666666667
    },
    {
      "final_Brier": 0.14685634006696058,
      "final_average_precision": 0.10206206096541949,
      "records": 480,
      "training": "Independent marginals synthetic only",
      "training_risk_fraction": 0.17708333333333334
    },
    {
      "final_Brier": 0.10844388927720339,
      "final_average_precision": 0.6609864631820183,
      "records": 960,
      "training": "Independent marginals augmented",
      "training_risk_fraction": 0.16875
    },
    {
      "final_Brier": 0.09673908797643074,
      "final_average_precision": 0.6680633811415726,
      "records": 480,
      "training": "Conditional mixture synthetic only",
      "training_risk_fraction": 0.14166666666666666
    },
    {
      "final_Brier": 0.09687126255739349,
      "final_average_precision": 0.6657980776246897,
      "records": 960,
      "training": "Conditional mixture augmented",
      "training_risk_fraction": 0.15104166666666666
    }
  ],
  "valid_constraints": {
    "orphan_inspections": 0,
    "orphan_parents": 0,
    "report_before_event": 0,
    "response_ratio_violations": 0
  }
}
```


## Publication and visual evidence

Content revision: `a59a1ded114584fde53f58a7c3fd0ddd0e7e629f`. Remote main and all 232 tree blobs match. All six current notebooks pass fresh-kernel execution, their 24 code cells and twelve inline figures are reviewed, and book figure generation reruns every current cell with exact RESULTS agreement. The final 454-page manuscript layout (kept local) was visually reviewed with PDF SHA-256 `b9548e8966a31ca04e041a85d1e6351cb3266535b796236f4015ead993b02f06`. Final publication metadata and commit-addressed raw files are verified separately; no manuscript is published in this repository.
