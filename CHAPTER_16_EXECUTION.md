# Chapter 16 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verification passed.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_077 | 16.1 | 4 | 2 | 1.322 |
| code_078 | 16.2 | 4 | 2 | 1.489 |
| code_079 | 16.3 | 4 | 2 | 1.987 |
| code_080 | 16.4 | 4 | 2 | 1.867 |
| code_081 | 16.5 | 4 | 2 | 1.304 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. All ten inline figures have been visually reviewed. Pooling intervals, explicit contour zoom, sensor-support bands and probability-graph labels are clear.

## Actual mechanisms and boundaries

Five self-contained CPU laboratories use seeds 1677–1681 and the unchanged Python 3.14.3 / NumPy 2.4.4 / SciPy 1.17.1 / pandas 3.0.3 / Matplotlib 3.11.0 / scikit-learn 1.9.0 environment. Initial kernels all passed without error outputs or solver warnings. Notebooks 078/079 reran after adding a 121-point-per-axis quadrature refinement and clarifying prior-predictive wording. Notebooks 077/081 reran for distinct calibration markers and observation labels matching the book; their numerical result dictionaries remain exactly unchanged. Notebook079 also reran to enlarge the joint-contour region with explicit zoom axes; result dictionaries remain exactly identical to the registered evidence. No dependency was added and ordinary execution is offline. Declared inspection/failure counts in 078/079 are teaching fixtures, not random field samples; other numerical observations are generated under explicit models.

Bernoulli class models train on 600 and assess 3000 independent records, with generated class 1 prior .2. AlarmA probabilities are .15/.8 by class, and independent conditional alarmB .25/.6. An extra exact copy ofA violates the naive conditional likelihood factorization. Fixed alpha 1 Bernoulli fits use empirical training class priors, present and absent indicators, with manual log-sum-exp probability agreement. Deduplicated final Brier/log loss/accuracy is .092829/.309573/.875667, compared with duplicated .121427/.405040/.844333. Pattern A 1 B 0 has known posterior .415584, fitted deduplicated .446721, duplicated .802816 and final observed frequency .395089 among 448 records. Four-pattern calibration counts remain visible. Smoothing gives finite unseen-indicator probabilities but cannot repair dependence; no final tuning occurs.

The hierarchy has n=[4,8,12,20,40,80,160,320], s=[0,1,3,1,5,9,10,30]. Group rates have Beta(m*k,(1-m)*k) distributions, with truncated hyperpriors m~Beta(2,8) on[.01,.6] and log(k)~Normal(log 20,.8) on[0,log 100]. Full hyperparameter uncertainty is integrated on a 61×61 trapezoid grid, not a plug-in empirical-Bayes fit. A 121×121 refinement changes group posterior means by at most 3.96269e-6. Complete-pooling rate is .0916149, population posterior mean .1144995 and mean concentration 39.3629. Smallest-group raw 0 becomes .1001315; largest raw .09375 becomes .0955137. Five thousand mixture draws supply marginal credible intervals. Prior-predictive mean total failures is 129.1824 versus declared observed 59, with .233 of prior replications having some observed group rate above half; no prior is silently revised. Separate twenty-inspection future draws use oracle rates solely to generate an illustrative future outcome; building 8 has six failures above its displayed upper intervalfive. Eight realizations do not establish predictive coverage. Marginal posterior curves condition on all groups, so displayed local likelihood/prior alone do not reproduce them.

The computation laboratory repeats those counts/priors internally. A numerical grid, iid grid draws, continuous transformed random-walk Metropolis and mean-field categorical grid approximation target declared bounded distributions. Metropolis includes the logit-mean Jacobian, four fixed chains,1000 warmup and 3000 retained steps per chain, proposal SDs[.3,.3]. Acceptance fractions are[.58975,.59525,.61275,.6015]; classical split Rhat is[1.00210,1.00402], and the explicitly simple within-chain ESS is[1121.60,424.01]. These are not modern rank-normalized/folded/tail diagnostics or a proof of convergence. Grid mean(m,logk)=[.1144995,3.5128897], MCMC=[.1153996,3.4771608]. Mean-field coordinate updates stabilize in 14 iterations; SDs[.023983,.552829] are smaller than joint-grid[.027608,.589720]. Posterior mass in the last concentration column is .008441; bounds remain part of the model. Posterior predictive variance of observed group rates retains Binomial sampling at unequal n. Observed .00540109 compares with replicated mean .00890677 and tail fraction .6154 across 5000 draws. This reuses data intentionally for criticism, not independent predictive assessment or a probability that the model is true.

The temperature GP uses 16 sensors on[.2,3.5]m, mean 20 Celsius, fixed RBF variance4 C²/length.8 m and known reading SD.15 C. Manual Cholesky posterior mean/latent variance matches sklearn with optimizerNone and centered targets to 1e-10. Forty inside/far independent readings have MSE .019973/.456526 and conditional pointwise future-interval coverage .975/1.0; these finite outcomes are not nominal-coverage guarantees. Latent intervals exclude reading noise and future intervals add it. A deliberately incomplete rank-five prior feature covariance loses the omitted K-Q component: at 10 m full latent variance is 4 versus approximately 2.11058e-30 for the low-rank prior. This is a failure demonstration, not a complete sparse/variational inducing-point method or a claim that all sparse GPs collapse away from support. No kernel or noise parameter is selected on assessment.

The known-parameter three-state HMM has 120 steps, transition rows[[.95,.05,0],[.01,.94,.05],[0,0,1]], emission means[0,1,3], SDs[.4,.6,.7], initial healthy. Generated state counts are[16,28,76]. Forward filtering is online; smoothing and Viterbi use all observations. Five-step exhaustive enumeration of 243 paths agrees with likelihood, smoothed marginals and joint MAP path. Full-trajectory marginal filtering/smoothing accuracy .991667/.991667 and Viterbi .983333 are retained rather than forcing an offline improvement. No transition/emission parameters are fitted. An eight-state positive undirected binary chain verifies A independent ofC givenB. A separate sixty-step scalar Kalman fixture uses AR.95, process SD.2 and reading SD.5, giving filter MSE .067354 versus raw .186486. These are inference audits, not field degradation, causal, GNN or remaining-life validation.

Ten original vector figure sets implement both planned briefs, with six equations and nine exercises. Primary GPML Chapters 2/8, Rabiner's author-hosted 1989 tutorial (forward/backward pages 262–263 visually read), and official Naive Bayes/Stan predictive/diagnostic documentation were inspected 20 October 2026. Stan is a documentary source only; its runtime and modern diagnostic implementation are not executed. Live sklearn 1.9.1 versus executed 1.9.0 is disclosed. Every probability and interval remains conditional on its stated observation model, priors, fitting role and approximation.

## Successful result dictionaries

### code_077

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1677.

```json
{
  "calibration_by_distinct_score": [
    {
      "model": "Deduplicated",
      "predicted_observed_count": [
        [
          0.03721307712452384,
          0.0341047503045067,
          1642
        ],
        [
          0.11538825030919683,
          0.1079136690647482,
          556
        ],
        [
          0.4467214075013207,
          0.3950892857142857,
          448
        ],
        [
          0.7315300018112155,
          0.7740112994350282,
          354
        ]
      ]
    },
    {
      "model": "Duplicated",
      "predicted_observed_count": [
        [
          0.009243939369107753,
          0.0341047503045067,
          1642
        ],
        [
          0.03052600690591308,
          0.1079136690647482,
          556
        ],
        [
          0.802816364321768,
          0.3950892857142857,
          448
        ],
        [
          0.9321577003507677,
          0.7740112994350282,
          354
        ]
      ]
    }
  ],
  "fits": [
    {
      "final_accuracy_at_half": 0.8756666666666667,
      "final_brier": 0.09282850147029599,
      "final_log_loss": 0.3095730316148787,
      "model": "Deduplicated"
    },
    {
      "final_accuracy_at_half": 0.8443333333333334,
      "final_brier": 0.12142661465822555,
      "final_log_loss": 0.4050396125508621,
      "model": "Duplicated"
    }
  ],
  "pattern_probabilities": {
    "deduplicated_fitted": [
      0.03721307712452384,
      0.11538825030919683,
      0.4467214075013207,
      0.7315300018112155
    ],
    "duplicated_fitted": [
      0.009243939369107753,
      0.03052600690591308,
      0.802816364321768,
      0.9321577003507677
    ],
    "known_generator_class1_posterior": [
      0.030418250950570335,
      0.12371134020618553,
      0.4155844155844156,
      0.7619047619047619
    ],
    "patterns_A_B": [
      [
        0,
        0
      ],
      [
        0,
        1
      ],
      [
        1,
        0
      ],
      [
        1,
        1
      ]
    ]
  },
  "roles": {
    "fixed_smoothing_alpha": 1,
    "independent_final": 3000,
    "selection": false,
    "train": 600
  },
  "smoothing_toy_unobserved_feature_finite": true
}
```

### code_078

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1678.

```json
{
  "future_prediction": {
    "future_data_used_in_fit": false,
    "inspections_per_building": 20,
    "predictive_lower": [
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    "predictive_mean": [
      2.0026308317424646,
      2.3141830760360644,
      3.0189958752546557,
      1.7720705421965988,
      2.377689685019615,
      2.241350654611228,
      1.431535947954803,
      1.910274279037213
    ],
    "predictive_upper": [
      6.0,
      6.0,
      8.0,
      5.0,
      6.0,
      6.0,
      4.0,
      5.0
    ],
    "separate_future_counts": [
      0,
      1,
      4,
      1,
      4,
      0,
      1,
      6
    ],
    "separate_oracle_rates": [
      0.02,
      0.08,
      0.18,
      0.06,
      0.12,
      0.09,
      0.07,
      0.1
    ]
  },
  "grid_refinement": {
    "coarse_points_per_axis": 61,
    "fine_points_per_axis": 121,
    "max_group_posterior_mean_difference": 3.962686708908203e-06,
    "posterior_continuous_integration_exact": false
  },
  "posterior": {
    "complete_pooling_rate": 0.09161490683229814,
    "failure_counts": [
      0,
      1,
      3,
      1,
      5,
      9,
      10,
      30
    ],
    "group_draws": 5000,
    "inspection_counts": [
      4,
      8,
      12,
      20,
      40,
      80,
      160,
      320
    ],
    "mixture_credible_95_lower": [
      0.01641130176748799,
      0.030218691742928662,
      0.05979990859726921,
      0.02316630656871206,
      0.054389181987390574,
      0.05920245473635754,
      0.03791772375537018,
      0.06702229605380543
    ],
    "mixture_credible_95_upper": [
      0.23791885025745604,
      0.24752456319313176,
      0.294330441636388,
      0.18548050575519975,
      0.21172672366311113,
      0.18000809776821725,
      0.11241940899837015,
      0.12847129342557098
    ],
    "partial_pooling_means": [
      0.10013154158712323,
      0.11570915380180322,
      0.1509497937627328,
      0.08860352710982994,
      0.11888448425098075,
      0.1120675327305614,
      0.07157679739774016,
      0.09551371395186065
    ],
    "posterior_hyper_mean_k": 39.362889520640415,
    "posterior_hyper_mean_m": 0.1144995083644458,
    "quadrature_grid": [
      61,
      61
    ],
    "raw_rates": [
      0.0,
      0.125,
      0.25,
      0.05,
      0.125,
      0.1125,
      0.0625,
      0.09375
    ],
    "truncated_hyperprior_ranges": {
      "log_k": [
        0,
        4.605170185988092
      ],
      "m": [
        0.01,
        0.6
      ]
    }
  },
  "prior_predictive": {
    "draws": 5000,
    "group_expected_rate": 0.19904525804395307,
    "mean_total_failures": 129.1824,
    "probability_any_group_rate_above_half": 0.233
  }
}
```

### code_079

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1679.

```json
{
  "computation": {
    "chain_acceptance": [
      0.58975,
      0.59525,
      0.61275,
      0.6015
    ],
    "classical_split_Rhat": [
      1.0020965472343628,
      1.0040228137294058
    ],
    "iid_grid_draw_mean": [
      0.11483726388888965,
      3.510470064221086
    ],
    "mcmc_mean_m_logk": [
      0.1153996171504399,
      3.4771607556958974
    ],
    "mean_field_iterations": 14,
    "mean_field_mean_m_logk": [
      0.11157594538246068,
      3.538782668482428
    ],
    "mean_field_sd_m_logk": [
      0.02398312115434151,
      0.5528290880329282
    ],
    "posterior_last_concentration_grid_column_mass": 0.008441130578302106,
    "reference_mean_m_logk": [
      0.1144995083644458,
      3.512889743597202
    ],
    "reference_sd_m_logk": [
      0.02760820719345163,
      0.5897203796974916
    ],
    "retained_per_chain": 3000,
    "simple_within_chain_ESS": [
      1121.6049646325832,
      424.01400693134366
    ],
    "warmup_per_chain": 1000
  },
  "grid_refinement": {
    "coarse_points_per_axis": 61,
    "fine_points_per_axis": 121,
    "max_group_posterior_mean_difference": 3.962686708908203e-06,
    "posterior_continuous_integration_exact": false
  },
  "posterior_predictive_check": {
    "draws": 5000,
    "independent_assessment": false,
    "observed": 0.005401088169642856,
    "replicated_2_5_97_5": [
      0.0017447064112103177,
      0.02813667999751981
    ],
    "replicated_fraction_ge_observed": 0.6154,
    "replicated_mean": 0.008906774076915923,
    "statistic": "unweighted variance of group observed rates"
  }
}
```

### code_080

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1680.

```json
{
  "GP": {
    "RBF_variance_C2": 4.0,
    "assessment": [
      {
        "cohort": "inside",
        "mean_latent_variance_C2": 0.008645341201899137,
        "pointwise_future_interval_coverage": 0.975,
        "readings": 40,
        "squared_error_mean_C2": 0.019972833604827996
      },
      {
        "cohort": "far",
        "mean_latent_variance_C2": 3.4845973814508917,
        "pointwise_future_interval_coverage": 1.0,
        "readings": 40,
        "squared_error_mean_C2": 0.45652552864528156
      }
    ],
    "hyperparameter_selection": false,
    "length_m": 0.8,
    "manual_library_agreement": true,
    "mean_C": 20.0,
    "noise_SD_C": 0.15,
    "sensors": 16
  },
  "low_rank_prior": {
    "at_10m_full_latent_variance_C2": 4.0,
    "at_10m_low_rank_latent_variance_C2": 2.1105807608149698e-30,
    "grid_mean_prediction_difference_C": 0.1720138162804691,
    "inducing_locations_m": [
      0.2,
      1.025,
      1.8499999999999999,
      2.675,
      3.5
    ],
    "omitted_component": "K-Q prior residual; this is not a complete sparse GP method",
    "rank": 5
  }
}
```

### code_081

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1681.

```json
{
  "HMM": {
    "emission_SD": [
      0.4,
      0.6,
      0.7
    ],
    "emission_means": [
      0.0,
      1.0,
      3.0
    ],
    "filter_marginal_argmax_accuracy": 0.9916666666666667,
    "five_step_enumeration_passed": true,
    "log_likelihood": -125.39832437277302,
    "offline_Viterbi_path_accuracy": 0.9833333333333333,
    "offline_smooth_marginal_argmax_accuracy": 0.9916666666666667,
    "parameters_fitted": false,
    "state_counts": [
      16,
      28,
      76
    ],
    "steps": 120,
    "transition": [
      [
        0.95,
        0.05,
        0.0
      ],
      [
        0.01,
        0.94,
        0.05
      ],
      [
        0.0,
        0.0,
        1.0
      ]
    ]
  },
  "continuous_state_filter": {
    "AR": 0.95,
    "filter_MSE": 0.0673537922366018,
    "final_conditional_variance": 0.0754761346655404,
    "measurement_SD": 0.5,
    "parameters_fitted": false,
    "process_SD": 0.2,
    "raw_measurement_MSE": 0.18648621429320453,
    "steps": 60
  },
  "probability_graphs": {
    "GNN_computation_executed": false,
    "conditional_independence_checked": true,
    "positive_undirected_chain_states": 8
  }
}
```


## Remote content verification

Content commit [2fac2b2c982ada3646fb8e7b78dc89297880ea0d](https://github.com/ImeshEkanayake/MLBook-/commit/2fac2b2c982ada3646fb8e7b78dc89297880ea0d) is published on main. All 137 remote blobs match the local tree and the earlier 76 manifest records remain unchanged. Final metadata is independently checked in the local book delivery evidence, including commit-addressed raw bytes.
