# Chapter 32 execution evidence

**Date:** 21 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_167 | 32.1 | 4 | 2 | 2.059 |
| code_168 | 32.2 | 4 | 2 | 2.832 |
| code_169 | 32.3 | 4 | 2 | 4.091 |
| code_170 | 32.4 | 4 | 2 | 2.188 |
| code_171 | 32.5 | 4 | 2 | 2.070 |
| code_172 | 32.6 | 4 | 2 | 2.177 |

Total: **24 executed code cells and 12 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

### Chapter 32 evidence and runtime

Chapter 32 is added only to `main_2.tex` / `output/pdf/main_2.pdf`. The separate first preview through Chapter 30 remains byte-identical. Chapter 31's source, notebooks and second-preview body pages are preserved. The second preview retains How to use this preview, contents and its own references; the two PDFs remain separate for later human assembly.

All six laboratories use the unchanged main CPython 3.14.3, NumPy 2.4.4 and Torch 2.14.1 CPU environment. Torch uses float64, one thread and deterministic operations. No package, downloaded asset, network request, credential or GPU is required by ordinary execution. The five-tuple control environment is an original Gymnasium-style implementation, not an imported native Gymnasium Env or checker-compliance claim. Each notebook has four executed code cells and two inline figures. Full code is rerun for vector exports and numeric RESULTS must agree exactly with fresh-kernel summaries.

### Mechanisms, controls and actual results

167: real disjoint linear LinUCB with ridge identity initialization and confidence coefficient 0.55, 600 training contexts and one observed chosen-action reward each. Counts 260/229/111. Only selected feedback updates statistics; full potential means remain simulator-only. A separate 400-context assessment freezes the ridge policy and compares conditional expected rewards, without noisy outcomes or final fitting: contextual 0.674175, random 0.253399, fixed first inspection 0.321158, oracle 0.674586. Training expected pseudo-regret is 3.759655. The exact two-step battery chooses wait then discharge for return 1 versus myopic 0.2. A hidden low-future-price regime reverses the first optimal action under the same present observation. The initial NumPy batched solve was repaired to use an explicit singleton right-hand-side dimension, then rerun; no score-selected parameter change was made.

168: explicit three-condition/two-action continuing maintenance MDP, discount 0.9. Value iteration takes 258 iterations and residual below 1e-12. Exact policy wait/repair/repair; exact healthy-wait Q 6.366972 and repair Q 4.348624. Real exploratory Q-learning uses 60,000 transitions, epsilon 0.3 and visit-count power −0.6 steps; all pairs are visited, with highly uneven counts [[41006,7261],[1665,9490],[77,501]]. The initial unjustified assertion that every pair must receive over 100 visits was replaced by the actual coverage assertion and the smaller count is disclosed. No trajectory or fitting setting changed. Tabular maximum Q error 0.038463 / Bellman residual 0.029491. A distinct generative simulator service supplies 6,000 uniformly sampled transitions to a one-hidden-layer 16-unit tanh Q network: 1,600 Adam 0.005 updates, batch 64, target copy every 50; error 0.264276 / residual 0.095868. Both greedy policies match the reference. Separate zero-reward two-state shared-feature counterexample updates only A→B records, gamma 0.95/step 0.1, amplifying weight by 1.09 to 30,987.01575 after 120 updates. It isolates an unsupported bootstrap rather than predicting universal divergence.

169: actual original PPO and SAC mechanisms, explicitly different tasks. PPO uses 30 on-policy batches ×48 episodes ×12 decisions =17,280 interactions, four epochs per batch, 16-unit tanh actor and critic, Monte Carlo returns at gamma 0.95, frozen old probabilities, normalized advantages, clip 0.2, entropy 0.01, critic coefficient 0.5 and gradient norm cap 1. No replay or final selection. Final deterministic argmax assessed on 300 independent matched-noise episodes: undiscounted mean 8.15 versus threshold repair 7.208667 and wait −11.222667; discounted 6.339825/5.737297/−6.542151. The final batch's recorded clip fraction is zero; clipping is implemented but not claimed active on every batch. SAC uses a tanh-Gaussian actor with change-of-variables log density, independent twin 32-unit critics, minimum soft backup, replay and Polyak 0.005 target updates. Fixed temperature 0.1, gamma 0.95, 3,600 transitions/256 uniform warm-up/3,344 batch-64 updates, critic lr 0.003/actor lr 0.001. Actual successor values bootstrap at external 32-step resets. Sixty independent matched-noise trajectories compare deterministic tanh means: undiscounted SAC −0.652905/proportional −0.635059/zero −2.066426; discounted −0.535513/−0.519556/−1.542429. Simple proportional control wins narrowly. Episode SDs are descriptive, not mean confidence intervals; no multiple-seed algorithm ranking is claimed. Discounted results were added explicitly and the current source rerun before publication, without selecting new training settings.

170: 30 generated 24-hour source days yield 690 demand residual pairs, least-squares intercept 0.001898 and coefficient 0.721537. Ten development days are diagnostic only (one-step MAE 0.065137); no selection or final refit. Unit battery/rate 0.25/efficiency 0.92 are known; only demand is learned and actions do not affect demand. Costs explicitly combine price purchases, peak-grid penalty coefficient 2 above 1.1, wear 0.02 and terminal storage coefficient 0.5 toward 0.5. Exhaustive 81 four-action sequences, first action only, state-dependent feasible projection; short-horizon terminal penalty is a declared heuristic. Ten familiar final days: no storage/reactive/persistence MPC/learned MPC costs 4.266641/4.287027/4.138903/4.126396. Ten changed-peak/different-persistence days: 5.800496/5.382552/5.290188/5.284075. Familiar learned one-/three-step MAE 0.060205/0.084425 versus persistence 0.078165/0.165852; changed learned 0.115604/0.181855. Fixed hour-16 rollout differs from future observed demand. No clairvoyant controller or field cost-saving claim. Legend clearance was repaired and both inline and vector figures rerun.

171: 200 fitting and 800 independent evaluation eight-step episodes, behavior wait/repair/overhaul probabilities [0.8,0.2,0] at every state. Training support counts [[824,240,0],[290,72,0],[143,31,0]]. Actual tabular FQI 100 iterations/gamma 0.9 with untouched optimistic unknown Q 5 chooses [wait,overhaul,overhaul]; simple support mask (at least ten state-action records) chooses [wait,repair,repair]. Simulator eight-step returns 0.833331 versus 5.163636. Mask is explicitly not CQL or a theoretical lower-bound implementation. A different fixed supported stochastic policy is evaluated at gamma 1 with model/finite-horizon Q,V fitted only on the 200 training episodes. Exact return 1.678812; trajectory IS 1.431109/episode SD 6.791695 and sequential DR 1.673035/SD 4.333482. Whole-episode 300-resample percentile intervals [1.025387,1.928264] and [1.368150,1.956431]. Weight sum 783.990012/max 4.561395/trajectory ESS 434.392284 out of 800. Evaluation outcomes never fit a nuisance model or select policy. An all-overhaul policy is refused by the support guard; identical logged worlds with overhaul reward −5/+5 give exact values −40/+40. The ambiguity is structural, not an interval-width problem.

172: original reset→(observation,info), step→(observation,reward,terminated,truncated,info). Unit storage evolves without clipping, max action 0.3. Trusted independent storage measurement supplies the shield; separately dropped policy sensor can trigger zero-action fallback. Natural day-24 horizon has observed clock, physical failure terminates, external limit truncates. Forty episodes per controller per scenario (normal/dropout 0.25/demand +0.6/efficiency 0.75). Unshielded fixed price rule fails in all 40 under every scenario, completing only 2–3 physical steps; low observed costs are not success. Nominal 0.92 projection survives familiar operation but fails all 40 at eta 0.75, serving 19/24 steps. Robust projection assumes eta∈[0.7,1.0], completes all tested episodes and passes 612 additional grid cases. Under shifted demand the nominal/robust controllers still exceed the 1.25 grid target on 0.889583/0.890625 of observed steps; storage feasibility does not imply service satisfaction. Dropout robust fallback triggers 222 times. Bootstrap tests retain actual successor state: r=1/gamma=0.9/Vnext=5 produces 5.5 after external truncation and 1 at true termination. The nominal failure trace ends rather than inventing later states. Figure labels and legends were repaired without metric changes and rerun.

### Interpretation and source boundaries

Nine primary records support contextual upper-confidence methods, tabular Q-learning, policy-gradient context, PPO, SAC, learned-model MPC, CQL context, sequential DR and the versioned Gymnasium interface. No author's benchmark gains are assigned to these original generated tasks. The publisher's Q-learning abstract supports the general tabular convergence boundary; no inaccessible full-text result is claimed inspected. PPO's clipped objective, SAC's log-density correction and target updates, and DR's independent-model backward recursion were checked against primary method text. Sources predate the 18 October 2026 cutoff and were accessed on 21 October 2026. Failed author-book fetches are not cited as inspected sources.

All assessment and fitting controls are fixed before final reporting. Final simulator truth diagnoses value error or identifies constructed ambiguity; it is never treated as available historical operational evidence. Controls, rewards, state observability, source support, generative sampling access, independent episodes and actual failures remain explicit. Small single-seed learned-policy comparisons and descriptive episode variability do not establish general algorithm superiority, field safety, a causal claim under arbitrary logs or hardware readiness. Kernel-manager transport notices appear in runner process logs rather than notebook stderr; they are not suppressed or described as learning failures.

## Successful result dictionaries

### code_167

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 5367.

```json
{
  "action_counts": [
    260,
    229,
    111
  ],
  "aliased_first_actions": {
    "high_future_price": 0,
    "low_future_price": 1
  },
  "battery_myopic_return": 0.2,
  "battery_optimal_return": 1.0,
  "battery_trace": [
    {
      "discharge": 0,
      "price": 0.2,
      "reward": 0.0,
      "storage_before": 1,
      "t": 0
    },
    {
      "discharge": 1,
      "price": 1.0,
      "reward": 1.0,
      "storage_before": 1,
      "t": 1
    }
  ],
  "final_contexts": 400,
  "final_expected_reward": {
    "Context oracle": 0.674585935480358,
    "Fixed inspection 0": 0.32115802258857834,
    "Frozen contextual": 0.6741751883279327,
    "Uniform random": 0.25339901421770644
  },
  "final_feedback_used_for_learning": 0,
  "observed_training_rewards": 600,
  "source_action_reward_log": [
    {
      "action": 0,
      "reward": 1.0748291838209516,
      "t": 0
    },
    {
      "action": 0,
      "reward": 0.8846509342362214,
      "t": 1
    },
    {
      "action": 0,
      "reward": 0.1619271728793028,
      "t": 2
    },
    {
      "action": 1,
      "reward": 0.30632215785551453,
      "t": 3
    },
    {
      "action": 2,
      "reward": 0.1992067481047477,
      "t": 4
    }
  ],
  "training_decisions": 600,
  "training_pseudo_regret": 3.7596549718256616,
  "ucb_coefficient": 0.55
}
```

### code_168

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 5368.

```json
{
  "Bellman_residuals": {
    "exact": 7.94031507211912e-13,
    "neural": 0.09586842110199623,
    "tabular": 0.029490566354645864
  },
  "discount": 0.9,
  "exact_Q": [
    [
      6.366972477056289,
      4.348623853203078
    ],
    [
      4.113761467881976,
      4.348623853203078
    ],
    [
      -0.08623853211802368,
      4.348623853203078
    ]
  ],
  "instability_final_weight": 30987.015749194372,
  "instability_growth_factor": 1.09,
  "instability_initial_weight": 1.0,
  "instability_successor_only_states": [
    "B"
  ],
  "instability_true_values": [
    0.0,
    0.0
  ],
  "instability_updated_states": [
    "A"
  ],
  "instability_updates": 120,
  "max_value_errors": {
    "neural": 0.26427576112820184,
    "tabular": 0.03846276796292347
  },
  "neural_Q": [
    [
      6.102696715928087,
      4.136047407427235
    ],
    [
      4.015873190950257,
      4.194756076653444
    ],
    [
      -0.15193131528897522,
      4.216580807902557
    ]
  ],
  "neural_batch": 64,
  "neural_policy": [
    0,
    1,
    1
  ],
  "neural_source_transitions": 6000,
  "neural_updates": 1600,
  "optimal_policy": [
    0,
    1,
    1
  ],
  "tabular_Q": [
    [
      6.377024372356995,
      4.374611524743843
    ],
    [
      4.141180406323575,
      4.357847924468774
    ],
    [
      -0.051611416770557556,
      4.387086621166001
    ]
  ],
  "tabular_policy": [
    0,
    1,
    1
  ],
  "tabular_visits": [
    [
      41006,
      7261
    ],
    [
      1665,
      9490
    ],
    [
      77,
      501
    ]
  ],
  "target_copy_interval": 50,
  "trajectory_transitions": 60000,
  "value_iteration_iterations": 258
}
```

### code_169

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 5369.

```json
{
  "PPO": {
    "clip_epsilon": 0.2,
    "critic_loss_coefficient": 0.5,
    "discount": 0.95,
    "entropy_coefficient": 0.01,
    "epochs_per_batch": 4,
    "evaluation": {
      "Always wait": {
        "episode_SD": 17.19054786820125,
        "mean_discounted_return": -6.542150729739868,
        "mean_undiscounted_return": -11.222666666666667
      },
      "PPO": {
        "episode_SD": 2.3674563350414215,
        "mean_discounted_return": 6.339825161862993,
        "mean_undiscounted_return": 8.15
      },
      "Threshold": {
        "episode_SD": 2.904325839875659,
        "mean_discounted_return": 5.737296633574423,
        "mean_undiscounted_return": 7.208666666666667
      }
    },
    "evaluation_policy": "deterministic argmax",
    "final_batch_clip_fraction": 0.0,
    "final_evaluation_episodes_per_policy": 300,
    "interaction_steps": 17280,
    "training_episodes": 1440
  },
  "SAC": {
    "batch_size": 64,
    "bootstrap_at_external_reset": true,
    "discount": 0.95,
    "evaluation": {
      "Proportional": {
        "episode_SD": 0.39251090361224705,
        "mean_discounted_return": -0.5195555093279911,
        "mean_undiscounted_return": -0.6350594234989112
      },
      "SAC mean": {
        "episode_SD": 0.413731549575385,
        "mean_discounted_return": -0.5355125280116003,
        "mean_undiscounted_return": -0.652904813967378
      },
      "Zero action": {
        "episode_SD": 1.499581408531218,
        "mean_discounted_return": -1.542429067177767,
        "mean_undiscounted_return": -2.066425640349469
      }
    },
    "evaluation_policy": "deterministic tanh mean",
    "external_reset_period": 32,
    "final_evaluation_episodes_per_policy": 60,
    "interaction_steps": 3600,
    "replay_records": 3600,
    "target_polyak": 0.005,
    "temperature": 0.1,
    "uniform_warmup_steps": 256,
    "updates": 3344
  }
}
```

### code_170

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 5370.

```json
{
  "candidate_action_sequences": 81,
  "closed_loop_cost": [
    {
      "controller": "No storage",
      "day_SD": 0.3065159083432039,
      "mean_daily_cost": 4.266641121100917,
      "regime": "Familiar"
    },
    {
      "controller": "Reactive",
      "day_SD": 0.4430530564281684,
      "mean_daily_cost": 4.287026580147959,
      "regime": "Familiar"
    },
    {
      "controller": "Persistence",
      "day_SD": 0.33641445516278834,
      "mean_daily_cost": 4.1389031619297665,
      "regime": "Familiar"
    },
    {
      "controller": "Learned",
      "day_SD": 0.34148059330990493,
      "mean_daily_cost": 4.126396335683179,
      "regime": "Familiar"
    },
    {
      "controller": "No storage",
      "day_SD": 0.23999862460541058,
      "mean_daily_cost": 5.800496321691,
      "regime": "Changed peak"
    },
    {
      "controller": "Reactive",
      "day_SD": 0.24134777774481325,
      "mean_daily_cost": 5.382552019277062,
      "regime": "Changed peak"
    },
    {
      "controller": "Persistence",
      "day_SD": 0.20036118080621518,
      "mean_daily_cost": 5.290188070013088,
      "regime": "Changed peak"
    },
    {
      "controller": "Learned",
      "day_SD": 0.19874131053049543,
      "mean_daily_cost": 5.284075468880252,
      "regime": "Changed peak"
    }
  ],
  "demand_intercept": 0.00189796502278547,
  "demand_residual_coefficient": 0.7215365634596664,
  "development_days": 10,
  "development_one_step_MAE": 0.06513726501947392,
  "development_used_for_selection": false,
  "example_plan_hour": 16,
  "example_planned_actions": [
    -0.25,
    -0.21000000000000002,
    -0.0,
    -0.0
  ],
  "example_planned_storage": [
    0.5,
    0.2282608695652174,
    0.0,
    0.0,
    0.0
  ],
  "example_predicted_demand": [
    1.4042247032464177,
    1.1573297668741507,
    0.9782660465889566,
    0.8718370954738242
  ],
  "final_days_per_regime": 10,
  "final_refits": 0,
  "forecast_errors": [
    {
      "MAE": 0.0781647743271861,
      "model": "Persistence",
      "regime": "Familiar",
      "steps_ahead": 1
    },
    {
      "MAE": 0.06020521368708379,
      "model": "Learned",
      "regime": "Familiar",
      "steps_ahead": 1
    },
    {
      "MAE": 0.12462469729946453,
      "model": "Persistence",
      "regime": "Familiar",
      "steps_ahead": 2
    },
    {
      "MAE": 0.0753574715879831,
      "model": "Learned",
      "regime": "Familiar",
      "steps_ahead": 2
    },
    {
      "MAE": 0.16585174073088682,
      "model": "Persistence",
      "regime": "Familiar",
      "steps_ahead": 3
    },
    {
      "MAE": 0.0844249211639068,
      "model": "Learned",
      "regime": "Familiar",
      "steps_ahead": 3
    },
    {
      "MAE": 0.1227935104097752,
      "model": "Persistence",
      "regime": "Changed peak",
      "steps_ahead": 1
    },
    {
      "MAE": 0.11560417671889302,
      "model": "Learned",
      "regime": "Changed peak",
      "steps_ahead": 1
    },
    {
      "MAE": 0.18259750928054985,
      "model": "Persistence",
      "regime": "Changed peak",
      "steps_ahead": 2
    },
    {
      "MAE": 0.1532930765150541,
      "model": "Learned",
      "regime": "Changed peak",
      "steps_ahead": 2
    },
    {
      "MAE": 0.22530076262281357,
      "model": "Persistence",
      "regime": "Changed peak",
      "steps_ahead": 3
    },
    {
      "MAE": 0.18185454052105782,
      "model": "Learned",
      "regime": "Changed peak",
      "steps_ahead": 3
    }
  ],
  "implemented_actions_per_plan": 1,
  "known_charge_discharge_efficiency": 0.92,
  "planning_horizon": 4,
  "source_days": 30,
  "source_transition_pairs": 690
}
```

### code_171

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 5371.

```json
{
  "behavior_probabilities": [
    [
      0.8,
      0.2,
      0.0
    ],
    [
      0.8,
      0.2,
      0.0
    ],
    [
      0.8,
      0.2,
      0.0
    ]
  ],
  "bootstrap_episode_resamples": 300,
  "candidate_true_finite_return": 1.6788120435003009,
  "compatible_world_unsupported_values": [
    -40.0,
    40.0
  ],
  "evaluation_episodes": 800,
  "evaluation_outcomes_used_for_fitting": 0,
  "fit_discount": 0.9,
  "fit_iterations": 100,
  "horizon": 8,
  "max_trajectory_weight": 4.561394691467285,
  "offline_evaluation": {
    "Sequential DR": {
      "bootstrap_95_percentile": [
        1.3681502052722827,
        1.9564305463972658
      ],
      "episode_SD": 4.333482418606214,
      "mean": 1.6730350400292948
    },
    "Trajectory IS": {
      "bootstrap_95_percentile": [
        1.0253871530927727,
        1.9282637546963994
      ],
      "episode_SD": 6.791695303714117,
      "mean": 1.43110915490985
    }
  },
  "support_constrained_policy": [
    0,
    1,
    1
  ],
  "support_constrained_true_return": 5.163636360000002,
  "support_minimum_count": 10,
  "training_action_counts": [
    [
      824,
      240,
      0
    ],
    [
      290,
      72,
      0
    ],
    [
      143,
      31,
      0
    ]
  ],
  "training_episodes": 200,
  "trajectory_effective_sample_size": 434.39228392046215,
  "trajectory_weight_sum": 783.9900119304657,
  "unrestricted_policy": [
    0,
    2,
    2
  ],
  "unrestricted_true_return": 0.8333311999999999,
  "unsupported_initial_Q": 5.0,
  "unsupported_policy_weighting_refused": true
}
```

### code_172

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 5372.

```json
{
  "bootstrap_test": {
    "discount": 0.9,
    "external_truncation_target": 5.5,
    "incorrect_combined_done_target": 1.0,
    "next_value": 5.0,
    "reward": 1.0,
    "true_terminal_target": 1.0
  },
  "environment_interface": "original Gymnasium-style five-tuple; not native Gymnasium Env",
  "episodes_per_scenario_controller": 40,
  "finite_horizon_clock_observed": true,
  "grid_cap_target": 1.25,
  "physical_failure_terminal": true,
  "robust_efficiency_interval": [
    0.7,
    1.0
  ],
  "robust_projection_grid_cases": 612,
  "stress_metrics": [
    {
      "completed_fraction": 0.0,
      "controller": "Unshielded",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.9625,
      "mean_observed_energy_cost": 0.4006672679710663,
      "scenario": "Normal",
      "sensor_fallbacks": 0,
      "served_step_fraction": 0.08333333333333333,
      "shield_overrides": 0,
      "storage_failures": 40
    },
    {
      "completed_fraction": 1.0,
      "controller": "Nominal shield",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.071875,
      "mean_observed_energy_cost": 4.273437709308599,
      "scenario": "Normal",
      "sensor_fallbacks": 0,
      "served_step_fraction": 1.0,
      "shield_overrides": 320,
      "storage_failures": 0
    },
    {
      "completed_fraction": 1.0,
      "controller": "Robust + fallback",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.06666666666666667,
      "mean_observed_energy_cost": 4.275406820449481,
      "scenario": "Normal",
      "sensor_fallbacks": 0,
      "served_step_fraction": 1.0,
      "shield_overrides": 360,
      "storage_failures": 0
    },
    {
      "completed_fraction": 0.0,
      "controller": "Unshielded",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.9625,
      "mean_observed_energy_cost": 0.4006672679710663,
      "scenario": "Sensor dropout",
      "sensor_fallbacks": 0,
      "served_step_fraction": 0.08333333333333333,
      "shield_overrides": 0,
      "storage_failures": 40
    },
    {
      "completed_fraction": 1.0,
      "controller": "Nominal shield",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.071875,
      "mean_observed_energy_cost": 4.273437709308599,
      "scenario": "Sensor dropout",
      "sensor_fallbacks": 0,
      "served_step_fraction": 1.0,
      "shield_overrides": 320,
      "storage_failures": 0
    },
    {
      "completed_fraction": 1.0,
      "controller": "Robust + fallback",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.0625,
      "mean_observed_energy_cost": 4.293143842678025,
      "scenario": "Sensor dropout",
      "sensor_fallbacks": 222,
      "served_step_fraction": 1.0,
      "shield_overrides": 257,
      "storage_failures": 0
    },
    {
      "completed_fraction": 0.0,
      "controller": "Unshielded",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 1.0,
      "mean_observed_energy_cost": 0.5806672679710663,
      "scenario": "Demand shift",
      "sensor_fallbacks": 0,
      "served_step_fraction": 0.08333333333333333,
      "shield_overrides": 0,
      "storage_failures": 40
    },
    {
      "completed_fraction": 1.0,
      "controller": "Nominal shield",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.8895833333333333,
      "mean_observed_energy_cost": 7.333437709308598,
      "scenario": "Demand shift",
      "sensor_fallbacks": 0,
      "served_step_fraction": 1.0,
      "shield_overrides": 320,
      "storage_failures": 0
    },
    {
      "completed_fraction": 1.0,
      "controller": "Robust + fallback",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.890625,
      "mean_observed_energy_cost": 7.335406820449481,
      "scenario": "Demand shift",
      "sensor_fallbacks": 0,
      "served_step_fraction": 1.0,
      "shield_overrides": 360,
      "storage_failures": 0
    },
    {
      "completed_fraction": 0.0,
      "controller": "Unshielded",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.9666666666666667,
      "mean_observed_energy_cost": 0.6006624912048689,
      "scenario": "Efficiency shift",
      "sensor_fallbacks": 0,
      "served_step_fraction": 0.125,
      "shield_overrides": 0,
      "storage_failures": 40
    },
    {
      "completed_fraction": 0.0,
      "controller": "Nominal shield",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.1,
      "mean_observed_energy_cost": 3.2038140524910106,
      "scenario": "Efficiency shift",
      "sensor_fallbacks": 0,
      "served_step_fraction": 0.7916666666666666,
      "shield_overrides": 280,
      "storage_failures": 40
    },
    {
      "completed_fraction": 1.0,
      "controller": "Robust + fallback",
      "episodes": 40,
      "grid_exceedance_fraction_of_observed_steps": 0.078125,
      "mean_observed_energy_cost": 4.36844519503168,
      "scenario": "Efficiency shift",
      "sensor_fallbacks": 0,
      "served_step_fraction": 1.0,
      "shield_overrides": 360,
      "storage_failures": 0
    }
  ],
  "trusted_independent_storage_sensor_assumed": true
}
```

