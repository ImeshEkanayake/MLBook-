# Chapter 34 execution evidence

**Date:** 21 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_178 | 34.1 | 5 | 3 | 2.446 |
| code_179 | 34.2 | 4 | 2 | 2.503 |
| code_180 | 34.3 | 5 | 3 | 2.840 |
| code_181 | 34.4 | 5 | 3 | 2.882 |
| code_182 | 34.5 | 5 | 3 | 2.551 |

Total: **24 executed code cells and 14 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

# Chapter 34 mechanisms, controls and interpretation

Five self-contained laboratories preserve all five original scopes and both visual briefs. There are 24 executed code cells and 14 inline figures; all imports/helpers and generated inputs are internal. Ordinary runs are offline, CPU-only and require no files or credentials. CPython 3.14.3; NumPy 2.4.4; SciPy 1.17.1; pandas 3.0.3; Matplotlib 3.11.0; scikit-learn 1.9.0; threadpoolctl 3.7.0; Torch 2.14.1 CPU. Ranking additionally uses installed XGBoost 3.4.1; ordinal fitting uses installed statsmodels 0.15.0. No installation, dependency change, model asset or dataset download occurred. Accessed live sklearn/XGBoost pages identify 1.9.1/3.4.2; execution versions remain separately pinned. Literature cutoff is 18 October 2026; access and execution are 21 October 2026 Australia/Melbourne.

## Actual mechanisms and boundaries

- **178 / survival:** Independent 480 source/120 diagnostic-development/240 final components. Calendar entry 0–3 and administrative cutoff 6; all observed from installation, no delayed-entry claim. Actual lightly penalized Cox partial likelihood on fixed x0/x1², Breslow baseline; original 30-bootstrap-tree depth-four logrank forest with minimum daughter 20, Nelson–Aalen leaf hazards and ensemble hazard averaging; actual six-bin neural survival likelihood, 500 updates. Censoring is independent by construction, exactly at annual endpoints. Source reverse-KM censor weights use left limits appropriate to the administrative atoms; final IPCW Brier and cumulative/dynamic AUC at ages 2/4/5. Final latent failure times are separate audit quantities only. Cox beta 0.725589/0.816669, optimizer successful. At age five Brier KM/Cox/forest/neural 0.188763/0.174703/0.172086/0.175429. This is not a pure calibration score. A separate 1,200-component failure/retirement cohort implements Aalen–Johansen cumulative incidence: failure incidence at age five 0.431728 versus retirement-censored net risk 0.529322. Original timeline Visual A selects two failures, two administrative censors and two retirements from that cohort; its age-three event-free risk count uses all 1,200 records. Installation/service clocks are explicit.
- **179 / ranking:** Whole days stay separate: 180 source/40 development/60 final, ten candidates, capacity three. Identical initialization and 500 identical 32-query batches for pointwise MSE, ordered-pair logistic and top-one ListNet losses. Native XGBRanker rank:ndcg uses 80 depth-three trees and sorted qid. The tree objective is weighted LambdaMART-style pair construction, not ListNet. Fully judged source grades are stronger information than policy feedback. Mean final NDCG@3 point/pair/list/tree/severity is 0.998710/1/0.998034/0.926287/0.894036. Final expected findings are separate simulator audits. In 6,000 diagnostic lists known examination probabilities range 1 to .05; low-severity raw response .043563 versus true mean finding .241809 and weighted estimate .253956. A top-three-only policy leaves 42,000 candidate records without support; full-population recovery is refused. No feedback diagnostic fits rankers. Predicted ranks display from one.
- **180 / recommendation:** 128 warm/24 cold assets, 32 options, 6,000 popularity-biased observed source interactions. Response means acceptance, not maintenance efficacy. Actual 8D MF BPR and original one-hop normalized LightGCN-style propagation/layer average/BPR, identical embeddings and 600 batches of 256 triples. Nonpositive-edge negatives mix unobserved alternatives with observed nonresponses; less-preferred sampling is an assumption. Feature-based 4→16→8 two towers fit observed binary likelihood for 600 updates. Cold ID models have a source-popularity fallback; features are usable for cold tower profiles. Warm expected response popularity/MF/graph/tower .609139/.608717/.639534/.853646; cold fallback .594022 versus tower .839528. Repeated options are permitted; warm assessment targets fresh requests on the fixed finite asset population. Tower candidate pool eight yields top-three recall .989583 warm/.972222 cold, yet fixed native reranking lowers response to .840889/.831105. Independent 2,000 logged requests give 69 matches, ESS35.899; raw .797101, IPS .691118, self-normalized .731919 versus simulator audit .842188. Propensity knowledge does not remove this finite error. A separate fixed-preference 80-round feedback study raises top-five exposure mass to .326852 under reinforcement versus .15625 uniform; it never fits earlier models.
- **181 / joint outputs:** Independent 1,000 source/200 development/400 final assets. Generated spall/corrosion/neither contract allows 001/100/010/110; not a universal physical incompatibility. Actual independent logistic models, native fixed-order ClassifierChain with cv5 upstream predictions, shared 4→24→3 BCE head with 600 updates. Chain greedy outputs are not exhaustive joint MAP or exact posterior marginals. Independent/shared valid-set decoding maximizes product-Bernoulli scores, explicitly an approximation. Independent invalid fraction .135 falls to zero; exact accuracy .470→.5125 while Hamming worsens .289167→.295833. The same assets have correlated displacements with exact fixture u1+u2+u3=0mm. Independent 80-tree forests, native shared-partition 80-tree RF and shared 600-update neural vector head are fitted. Orthogonal mean subtraction enforces this exact relation; independent RMSE .546931→.505112mm, residual .464205mm→rounding. Shared RF residual is already negligible but RMSE .663735mm; shared NN RMSE .373996mm and raw residual .035155mm. Validity differs from accuracy. Visual B orders the same fixed six final assets by a declared sum of marginal damage scores and shows their valid flags and projected signed vectors; rounded displayed components need not sum exactly to zero.
- **182 / special targets:** Native statsmodels proportional-odds ordered likelihood, nominal logistic and rounded ridge on 1,000 source/600 final grades. Ordered accuracy .505/step error .635 versus rounded .451667/.608333; a rounded value gets no invented log score. Repair counts use 1,200 source/300 calibration/300 selection/600 final records with hidden structural states. Actual Poisson and original autodifferentiated NB/ZINB BFGS likelihoods; two fixed ZINB starts selected by source likelihood only; all optimizer gradient norms small and success true. Final NLL 1.132344/.773714/.750682 while mean squared errors near2.14; Poisson predicts zero .617904 vs .823333 observed and tail≥5 .002397 vs .028333. NB dispersion5.9694 absorbs omitted mixture variation; ZINB count dispersion .7341. A mixture does not reveal individual zero state. Rare-event costs FN10/FP1; only four calibration positives/eight selection positives. Fixed .5 and1/11 rules miss all17final positives; independently selected .05 catches2, misses15 and makes10false alarms, cost .266667 vs .283333. No final choice. Separate 1,000 source/500 final continuous burdens fit native HGB quantiles .1/.5/.9,120iterations. Crossing .002; sorting enforces order but 80%coverage remains .728, width1.415051. Slice plot holds x1=0; global scores use all500final records.

## Execution and repairs

The initial saved builder had a missing newline at the notebook writer/call boundary, discovered before any kernel ran and repaired. All five notebooks then executed through the unchanged runner in fresh kernels with all assertions passing and no notebook stderr. Timeline construction was subsequently expanded to include competing retirement and use its actual full cohort risk count; ranking positions were labelled from one and cold fallback panel titles clarified. Affected notebooks178–180 reran in fresh kernels; final stored outputs and summary dictionaries agree.

The first all-notebook vector-export attempt completed178 then aborted with native OpenMP mutex initialization error179 when changing library combinations inside one long-lived process. The exporter was repaired to dispatch a fresh isolated process for each notebook with the same single-thread settings used by the kernel runner. Every current code cell then ran again for vector exports, with exact numeric RESULTS equality to its actual kernel summary; all five child processes exited zero. No resource results were replayed. The initial failure remains in execution history; no notebook runtime failure is hidden by the exporter repair.

Fourteen original vector SVG/PDF/PNG sets reproduce the experiments, including three survival/three recommendation/three structured-output/three special-target and two ranking figures. Notebook markdown and chapter prose disclose role boundaries, objective scales, simulator-only truth, native versus original mechanisms, failed controls and limited assessment claims. No oracle outcomes select a final model, threshold or checkpoint. Future chapter scopes and prior artifacts remain preserved; the complete book still requires Chapters35–43 and the whole-book audit.

## Successful result dictionaries

### code_178

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7578.

```json
{
  "analytic_failure_incidence_age5": 0.4076367097178821,
  "calendar_cutoff": 6,
  "competing_components": 1200,
  "competing_counts": {
    "0": 411,
    "1": 482,
    "2": 307
  },
  "competing_service_age3_risk_set": 580,
  "components_observed_from_installation": true,
  "cox_coefficients": [
    0.7255885132463814,
    0.8166688768117845
  ],
  "cox_gradient_norm": 4.9316733032622444e-11,
  "cox_optimizer_success": true,
  "development_components": 120,
  "development_metrics": [
    {
      "IPCW_Brier": 0.22604166666666672,
      "censor_survival_left": 1.0,
      "horizon": 2.0,
      "model": "KM",
      "oracle_full_time_Brier_for_audit": 0.22604166666666672,
      "weighted_dynamic_AUC": 0.5
    },
    {
      "IPCW_Brier": 0.218978003547885,
      "censor_survival_left": 0.7634854771784232,
      "horizon": 4.0,
      "model": "KM",
      "oracle_full_time_Brier_for_audit": 0.22596527913667858,
      "weighted_dynamic_AUC": 0.5
    },
    {
      "IPCW_Brier": 0.17678151855464178,
      "censor_survival_left": 0.5015598025259714,
      "horizon": 5.0,
      "model": "KM",
      "oracle_full_time_Brier_for_audit": 0.18492734813216227,
      "weighted_dynamic_AUC": 0.5
    },
    {
      "IPCW_Brier": 0.20905411983933972,
      "censor_survival_left": 1.0,
      "horizon": 2.0,
      "model": "Cox",
      "oracle_full_time_Brier_for_audit": 0.20905411983933972,
      "weighted_dynamic_AUC": 0.6606977462179685
    },
    {
      "IPCW_Brier": 0.20397511390520998,
      "censor_survival_left": 0.7634854771784232,
      "horizon": 4.0,
      "model": "Cox",
      "oracle_full_time_Brier_for_audit": 0.20981038658994777,
      "weighted_dynamic_AUC": 0.6675353408323437
    },
    {
      "IPCW_Brier": 0.1727651360490076,
      "censor_survival_left": 0.5015598025259714,
      "horizon": 5.0,
      "model": "Cox",
      "oracle_full_time_Brier_for_audit": 0.17079449068959385,
      "weighted_dynamic_AUC": 0.6463547960673796
    },
    {
      "IPCW_Brier": 0.212907058432752,
      "censor_survival_left": 1.0,
      "horizon": 2.0,
      "model": "Forest",
      "oracle_full_time_Brier_for_audit": 0.212907058432752,
      "weighted_dynamic_AUC": 0.6421735103426983
    },
    {
      "IPCW_Brier": 0.20030354998742608,
      "censor_survival_left": 0.7634854771784232,
      "horizon": 4.0,
      "model": "Forest",
      "oracle_full_time_Brier_for_audit": 0.20479440727887088,
      "weighted_dynamic_AUC": 0.676268660192366
    },
    {
      "IPCW_Brier": 0.16914467514320955,
      "censor_survival_left": 0.5015598025259714,
      "horizon": 5.0,
      "model": "Forest",
      "oracle_full_time_Brier_for_audit": 0.16987225464033787,
      "weighted_dynamic_AUC": 0.6582537574688186
    },
    {
      "IPCW_Brier": 0.2115275075754175,
      "censor_survival_left": 1.0,
      "horizon": 2.0,
      "model": "Neural",
      "oracle_full_time_Brier_for_audit": 0.2115275075754175,
      "weighted_dynamic_AUC": 0.6511268910157456
    },
    {
      "IPCW_Brier": 0.2027207525844813,
      "censor_survival_left": 0.7634854771784232,
      "horizon": 4.0,
      "model": "Neural",
      "oracle_full_time_Brier_for_audit": 0.20830247557063095,
      "weighted_dynamic_AUC": 0.6708609888446402
    },
    {
      "IPCW_Brier": 0.1811463670266048,
      "censor_survival_left": 0.5015598025259714,
      "horizon": 5.0,
      "model": "Neural",
      "oracle_full_time_Brier_for_audit": 0.17852812743001234,
      "weighted_dynamic_AUC": 0.6371396906715635
    }
  ],
  "development_used_for_selection": false,
  "failure_incidence_age5": 0.4317281792281763,
  "final_components": 240,
  "final_latent_failure_times_used_for_fitting": false,
  "final_metrics": [
    {
      "IPCW_Brier": 0.20048611111111106,
      "censor_survival_left": 1.0,
      "horizon": 2.0,
      "model": "KM",
      "oracle_full_time_Brier_for_audit": 0.20048611111111106,
      "weighted_dynamic_AUC": 0.5
    },
    {
      "IPCW_Brier": 0.23405949086002828,
      "censor_survival_left": 0.7634854771784232,
      "horizon": 4.0,
      "model": "KM",
      "oracle_full_time_Brier_for_audit": 0.24383882608716148,
      "weighted_dynamic_AUC": 0.5
    },
    {
      "IPCW_Brier": 0.18876269418698802,
      "censor_survival_left": 0.5015598025259714,
      "horizon": 5.0,
      "model": "KM",
      "oracle_full_time_Brier_for_audit": 0.21212082387692865,
      "weighted_dynamic_AUC": 0.5
    },
    {
      "IPCW_Brier": 0.18384703922322398,
      "censor_survival_left": 1.0,
      "horizon": 2.0,
      "model": "Cox",
      "oracle_full_time_Brier_for_audit": 0.18384703922322398,
      "weighted_dynamic_AUC": 0.69836293974225
    },
    {
      "IPCW_Brier": 0.21542797067291716,
      "censor_survival_left": 0.7634854771784232,
      "horizon": 4.0,
      "model": "Cox",
      "oracle_full_time_Brier_for_audit": 0.22006600759682815,
      "weighted_dynamic_AUC": 0.6685441306233023
    },
    {
      "IPCW_Brier": 0.17470336122665567,
      "censor_survival_left": 0.5015598025259714,
      "horizon": 5.0,
      "model": "Cox",
      "oracle_full_time_Brier_for_audit": 0.18134843063897582,
      "weighted_dynamic_AUC": 0.6850115858655047
    },
    {
      "IPCW_Brier": 0.18564420256958758,
      "censor_survival_left": 1.0,
      "horizon": 2.0,
      "model": "Forest",
      "oracle_full_time_Brier_for_audit": 0.18564420256958758,
      "weighted_dynamic_AUC": 0.6763322884012539
    },
    {
      "IPCW_Brier": 0.21450136992204868,
      "censor_survival_left": 0.7634854771784232,
      "horizon": 4.0,
      "model": "Forest",
      "oracle_full_time_Brier_for_audit": 0.21937007352213778,
      "weighted_dynamic_AUC": 0.6625918336558616
    },
    {
      "IPCW_Brier": 0.17208553133979076,
      "censor_survival_left": 0.5015598025259714,
      "horizon": 5.0,
      "model": "Forest",
      "oracle_full_time_Brier_for_audit": 0.1792201363588763,
      "weighted_dynamic_AUC": 0.6940056043599571
    },
    {
      "IPCW_Brier": 0.18599801785269104,
      "censor_survival_left": 1.0,
      "horizon": 2.0,
      "model": "Neural",
      "oracle_full_time_Brier_for_audit": 0.18599801785269104,
      "weighted_dynamic_AUC": 0.6792058516196449
    },
    {
      "IPCW_Brier": 0.2140067372445148,
      "censor_survival_left": 0.7634854771784232,
      "horizon": 4.0,
      "model": "Neural",
      "oracle_full_time_Brier_for_audit": 0.2196378997320752,
      "weighted_dynamic_AUC": 0.672638047596669
    },
    {
      "IPCW_Brier": 0.17542913507351182,
      "censor_survival_left": 0.5015598025259714,
      "horizon": 5.0,
      "model": "Neural",
      "oracle_full_time_Brier_for_audit": 0.18186521490261726,
      "weighted_dynamic_AUC": 0.6831591985329942
    }
  ],
  "forest_max_depth": 4,
  "forest_min_daughter": 20,
  "forest_trees": 30,
  "illustration_competing_cohort_ids": [
    1,
    2,
    5,
    6,
    0,
    4
  ],
  "left_truncation_claimed": false,
  "neural_annual_intervals": 6,
  "neural_updates": 500,
  "retirement_censored_net_risk_age5": 0.5293224626639648,
  "source_censored": 166,
  "source_components": 480,
  "source_events": 314
}
```

### code_179

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1", "xgboost": "3.4.1"}`; Darwin arm64 CPU; seed 7579.

```json
{
  "batch_days": 32,
  "candidates_per_day": 10,
  "daily_capacity": 3,
  "development_days": 40,
  "development_metrics": [
    {
      "mean_NDCG_at3": 0.9942424951061589,
      "mean_expected_findings_at3": 2.378825886055907,
      "model": "Pointwise"
    },
    {
      "mean_NDCG_at3": 1.0,
      "mean_expected_findings_at3": 2.379488185305359,
      "model": "Pairwise"
    },
    {
      "mean_NDCG_at3": 0.996448785430263,
      "mean_expected_findings_at3": 2.3713405147662505,
      "model": "ListNet"
    },
    {
      "mean_NDCG_at3": 0.9566696023588562,
      "mean_expected_findings_at3": 2.3043537436087376,
      "model": "Tree NDCG"
    },
    {
      "mean_NDCG_at3": 0.8729318745764196,
      "mean_expected_findings_at3": 2.185520421105371,
      "model": "Severity"
    },
    {
      "mean_NDCG_at3": 1.0,
      "mean_expected_findings_at3": 2.3806705601146967,
      "model": "Oracle"
    }
  ],
  "development_used_for_selection": false,
  "diagnostic_feedback_used_for_fitting": 0,
  "examination_probabilities": [
    1.0,
    0.8,
    0.6,
    0.4,
    0.25,
    0.2,
    0.15,
    0.1,
    0.08,
    0.05
  ],
  "final_days": 60,
  "final_metrics": [
    {
      "mean_NDCG_at3": 0.9987096615964762,
      "mean_expected_findings_at3": 2.4025180786271574,
      "model": "Pointwise"
    },
    {
      "mean_NDCG_at3": 1.0,
      "mean_expected_findings_at3": 2.40622325263458,
      "model": "Pairwise"
    },
    {
      "mean_NDCG_at3": 0.9980338868396875,
      "mean_expected_findings_at3": 2.3956346977457588,
      "model": "ListNet"
    },
    {
      "mean_NDCG_at3": 0.9262871170757424,
      "mean_expected_findings_at3": 2.307202944729894,
      "model": "Tree NDCG"
    },
    {
      "mean_NDCG_at3": 0.8940359940836405,
      "mean_expected_findings_at3": 2.2676336626924396,
      "model": "Severity"
    },
    {
      "mean_NDCG_at3": 1.0,
      "mean_expected_findings_at3": 2.4071330473278416,
      "model": "Oracle"
    }
  ],
  "losses_different_units": {
    "ListNet": 1.855056291419409,
    "Pairwise": 0.012123169525006734,
    "Pointwise": 0.08755280489889772
  },
  "native_ranker_trees": 80,
  "neural_updates_per_objective": 500,
  "never_displayed_records_under_top3_only": 42000,
  "position_feedback": [
    {
      "candidate_records": 19948,
      "oracle_expected_finding": 0.24180904256214994,
      "raw_response_rate": 0.04356326448766794,
      "severity_bin": 0,
      "weighted_finding_estimate": 0.2539561192433661
    },
    {
      "candidate_records": 19892,
      "oracle_expected_finding": 0.500337347681383,
      "raw_response_rate": 0.20706816810778203,
      "severity_bin": 1,
      "weighted_finding_estimate": 0.49242157651317114
    },
    {
      "candidate_records": 20160,
      "oracle_expected_finding": 0.7598054262890037,
      "raw_response_rate": 0.5011904761904762,
      "severity_bin": 2,
      "weighted_finding_estimate": 0.7555059523809524
    }
  ],
  "position_feedback_days": 6000,
  "query_role_ids": {
    "development": [
      1000,
      1039
    ],
    "final": [
      2000,
      2059
    ],
    "source": [
      0,
      179
    ]
  },
  "source_days": 180,
  "top3_only_full_population_claim_refused": true
}
```

### code_180

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7580.

```json
{
  "bpr_batch_size": 256,
  "bpr_updates": 600,
  "candidate_pool_size": 8,
  "cold_ID_fallback": "source positive-response popularity",
  "cold_assets": 24,
  "feedback_final_top5_mass": {
    "Reinforce": 0.32685178671918963,
    "Uniform": 0.15625
  },
  "feedback_mean_response": {
    "Reinforce": 0.5259765625,
    "Uniform": 0.499365234375
  },
  "feedback_preferences_fixed": true,
  "feedback_requests_per_round": 256,
  "feedback_rounds": 80,
  "feedback_used_to_fit_prior_models": false,
  "final_population_metrics": [
    {
      "expected_top1_response": 0.6091390371406324,
      "model": "Popularity",
      "population": "Warm",
      "utility_NDCG_at5": 0.6980633765247439
    },
    {
      "expected_top1_response": 0.594022235648539,
      "model": "Popularity",
      "population": "Cold",
      "utility_NDCG_at5": 0.7034720879421918
    },
    {
      "expected_top1_response": 0.6087168199403774,
      "model": "MF",
      "population": "Warm",
      "utility_NDCG_at5": 0.7445335575864009
    },
    {
      "expected_top1_response": 0.594022235648539,
      "model": "MF",
      "population": "Cold",
      "utility_NDCG_at5": 0.7034720879421918
    },
    {
      "expected_top1_response": 0.6395342528309059,
      "model": "Graph",
      "population": "Warm",
      "utility_NDCG_at5": 0.76273767995758
    },
    {
      "expected_top1_response": 0.594022235648539,
      "model": "Graph",
      "population": "Cold",
      "utility_NDCG_at5": 0.7034720879421918
    },
    {
      "expected_top1_response": 0.8536461924898174,
      "model": "Two tower",
      "population": "Warm",
      "utility_NDCG_at5": 0.9894901538841809
    },
    {
      "expected_top1_response": 0.8395282934600807,
      "model": "Two tower",
      "population": "Cold",
      "utility_NDCG_at5": 0.9862473842406763
    }
  ],
  "graph_propagation_layers": 1,
  "independent_logged_policy": {
    "IPS_response": 0.691118015264682,
    "matches": 69,
    "raw_match_response": 0.7971014492753623,
    "requests": 2000,
    "self_normalized_response": 0.7319186159976525,
    "simulator_policy_response_audit": 0.842188159078858,
    "weight_ESS": 35.89927573294769
  },
  "last_BPR_losses": {
    "Graph": 0.14058561569823236,
    "MF": 0.11743491620001605
  },
  "options": 32,
  "oracle_used_for_training": false,
  "positive_edges": 1671,
  "repeat_options_permitted": true,
  "reranker_iterations": 100,
  "reranker_source_requests": 6000,
  "source_option_probabilities": [
    0.004809683818879698,
    0.0052984034608958615,
    0.005836782685014879,
    0.006429867480557852,
    0.007083216567866789,
    0.007802953497721182,
    0.008595824044659405,
    0.009469259432127015,
    0.010431445982033168,
    0.011491401841509536,
    0.012659061505997537,
    0.013945368930861228,
    0.015362380104219671,
    0.01692337604236832,
    0.018642987266845372,
    0.020537330929811318,
    0.02262416187295692,
    0.024923039035747777,
    0.027455508772675875,
    0.030245306797669378,
    0.033318580648396025,
    0.036704134755518945,
    0.04043370041383045,
    0.044542233185583174,
    0.049068240523447895,
    0.054054142683762525,
    0.05954667031275174,
    0.06559730243211652,
    0.07226274892903767,
    0.07960548207275799,
    0.08769432203941188,
    0.09660508193296644
  ],
  "source_requests": 6000,
  "stage_metrics": [
    {
      "candidate_recall_top3_in8": 0.9895833333333333,
      "oracle_expected_top1": 0.8660236466367175,
      "population": "Warm",
      "reranked_expected_top1": 0.840888571529937,
      "tower_expected_top1": 0.8536461924898174
    },
    {
      "candidate_recall_top3_in8": 0.9722222222222222,
      "oracle_expected_top1": 0.851609434671134,
      "population": "Cold",
      "reranked_expected_top1": 0.8311045968393033,
      "tower_expected_top1": 0.8395282934600807
    }
  ],
  "tower_updates": 600,
  "warm_assets": 128
}
```

### code_181

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7581.

```json
{
  "allowed_label_vectors": [
    [
      0,
      0,
      1
    ],
    [
      1,
      0,
      0
    ],
    [
      0,
      1,
      0
    ],
    [
      1,
      1,
      0
    ]
  ],
  "chain_order": [
    0,
    1,
    2
  ],
  "chain_upstream_folds": 5,
  "development_assets": 200,
  "development_label_metrics": [
    {
      "Hamming_loss": 0.305,
      "exact_vector_accuracy": 0.425,
      "invalid_fraction": 0.155,
      "micro_F1": 0.6500956022944551,
      "model": "Independent"
    },
    {
      "Hamming_loss": 0.295,
      "exact_vector_accuracy": 0.445,
      "invalid_fraction": 0.145,
      "micro_F1": 0.6602687140115163,
      "model": "Chain"
    },
    {
      "Hamming_loss": 0.365,
      "exact_vector_accuracy": 0.365,
      "invalid_fraction": 0.09,
      "micro_F1": 0.5875706214689266,
      "model": "Shared"
    },
    {
      "Hamming_loss": 0.30333333333333334,
      "exact_vector_accuracy": 0.48,
      "invalid_fraction": 0.0,
      "micro_F1": 0.6702898550724637,
      "model": "Ind projected"
    },
    {
      "Hamming_loss": 0.3616666666666667,
      "exact_vector_accuracy": 0.395,
      "invalid_fraction": 0.0,
      "micro_F1": 0.6018348623853211,
      "model": "Shared projected"
    }
  ],
  "development_used_for_selection": false,
  "displacement_relation": "u1+u2+u3=0 mm in the declared fixture",
  "final_assets": 400,
  "final_label_metrics": [
    {
      "Hamming_loss": 0.2891666666666667,
      "exact_vector_accuracy": 0.47,
      "invalid_fraction": 0.135,
      "micro_F1": 0.6760037348272643,
      "model": "Independent"
    },
    {
      "Hamming_loss": 0.2891666666666667,
      "exact_vector_accuracy": 0.4625,
      "invalid_fraction": 0.13,
      "micro_F1": 0.6766076421248836,
      "model": "Chain"
    },
    {
      "Hamming_loss": 0.31333333333333335,
      "exact_vector_accuracy": 0.445,
      "invalid_fraction": 0.1025,
      "micro_F1": 0.6485981308411215,
      "model": "Shared"
    },
    {
      "Hamming_loss": 0.29583333333333334,
      "exact_vector_accuracy": 0.5125,
      "invalid_fraction": 0.0,
      "micro_F1": 0.6838824577025824,
      "model": "Ind projected"
    },
    {
      "Hamming_loss": 0.31083333333333335,
      "exact_vector_accuracy": 0.4775,
      "invalid_fraction": 0.0,
      "micro_F1": 0.6624434389140271,
      "model": "Shared projected"
    }
  ],
  "final_vector_metrics": [
    {
      "component_RMSE_mm": 0.5469305506843506,
      "mean_absolute_sum_mm": 0.4642054448516022,
      "model": "Independent RF",
      "state": "Raw"
    },
    {
      "component_RMSE_mm": 0.5051115482276717,
      "mean_absolute_sum_mm": 1.8002960233687304e-16,
      "model": "Independent RF",
      "state": "Projected"
    },
    {
      "component_RMSE_mm": 0.663735230697651,
      "mean_absolute_sum_mm": 8.185379457570363e-16,
      "model": "Joint RF",
      "state": "Raw"
    },
    {
      "component_RMSE_mm": 0.663735230697651,
      "mean_absolute_sum_mm": 1.6727938478844352e-16,
      "model": "Joint RF",
      "state": "Projected"
    },
    {
      "component_RMSE_mm": 0.37399569098738716,
      "mean_absolute_sum_mm": 0.03515531272872042,
      "model": "Shared NN",
      "state": "Raw"
    },
    {
      "component_RMSE_mm": 0.3736059562777425,
      "mean_absolute_sum_mm": 1.4930764957732377e-16,
      "model": "Shared NN",
      "state": "Projected"
    }
  ],
  "forest_depth": 6,
  "forest_trees_each": 80,
  "illustration_damage_flags": [
    [
      1,
      1,
      0
    ],
    [
      1,
      1,
      0
    ],
    [
      0,
      1,
      0
    ],
    [
      0,
      0,
      1
    ],
    [
      0,
      1,
      0
    ],
    [
      0,
      0,
      1
    ]
  ],
  "illustration_displacements_mm": [
    [
      4.001788684020341,
      0.9934810715144243,
      -4.995269755534766
    ],
    [
      2.5748249177867337,
      -0.7246853655621116,
      -1.850139552224622
    ],
    [
      -0.44749763271796233,
      -0.03687343979244737,
      0.4843710725104097
    ],
    [
      -1.9036334157709236,
      0.6431408754715282,
      1.2604925402993954
    ],
    [
      -2.925751815533719,
      0.8573799999919001,
      2.068371815541819
    ],
    [
      -0.31757491803230975,
      4.285395534146667,
      -3.967820616114357
    ]
  ],
  "illustration_final_asset_ids": [
    3,
    0,
    2,
    1,
    5,
    4
  ],
  "illustration_priority_scores": [
    1.4004072570226145,
    1.3527407476145066,
    1.0499371527982713,
    0.8255225797350012,
    0.7740121416164574,
    0.4343753906572184
  ],
  "label_network_updates": 600,
  "shared_RF_preserves_linear_relation": true,
  "source_assets": 1000,
  "vector_network_updates": 600
}
```

### code_182

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "statsmodels": "0.15.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7582.

```json
{
  "NB_optimizer": {
    "dispersion": 5.969429117922576,
    "gradient_norm": 1.6328822334661536e-08,
    "success": true
  },
  "ZINB_optimizer": {
    "dispersion": 0.7340572724020638,
    "gradient_norm": 1.9907519547322847e-08,
    "source_start_losses": [
      0.8252009734595714,
      0.8252009734595368
    ],
    "success": true
  },
  "count_role_sizes": {
    "calibration": 300,
    "final": 600,
    "source": 1200,
    "threshold_selection": 300
  },
  "false_negative_cost": 10,
  "false_positive_cost": 1,
  "final_count_metrics": [
    {
      "count_mean_squared_error": 2.1396125406159725,
      "model": "Poisson",
      "negative_log_probability": 1.1323441162183019,
      "observed_at_least5_fraction": 0.028333333333333332,
      "observed_zero_fraction": 0.8233333333333334,
      "predicted_at_least5_fraction": 0.0023971556161958016,
      "predicted_zero_fraction": 0.617904493955791
    },
    {
      "count_mean_squared_error": 2.1483716362110923,
      "model": "NB",
      "negative_log_probability": 0.7737139766450335,
      "observed_at_least5_fraction": 0.028333333333333332,
      "observed_zero_fraction": 0.8233333333333334,
      "predicted_at_least5_fraction": 0.029565803505266903,
      "predicted_zero_fraction": 0.8026936282768824
    },
    {
      "count_mean_squared_error": 2.1417523121024042,
      "model": "ZINB",
      "negative_log_probability": 0.7506822356044381,
      "observed_at_least5_fraction": 0.028333333333333332,
      "observed_zero_fraction": 0.8233333333333334,
      "predicted_at_least5_fraction": 0.03281925735816537,
      "predicted_zero_fraction": 0.805905739326157
    }
  ],
  "final_grade_metrics": [
    {
      "absolute_grade_step_error": 0.635,
      "accuracy": 0.505,
      "model": "Ordinal",
      "negative_log_probability": 1.0996562901999705
    },
    {
      "absolute_grade_step_error": 0.6366666666666667,
      "accuracy": 0.49833333333333335,
      "model": "Nominal",
      "negative_log_probability": 1.099639028423458
    },
    {
      "absolute_grade_step_error": 0.6083333333333333,
      "accuracy": 0.45166666666666666,
      "model": "Rounded ridge",
      "negative_log_probability": null
    }
  ],
  "final_quantile_metrics": [
    {
      "central80_coverage": 0.728,
      "mean_interval_width": 1.4148651284264988,
      "pinball_losses": [
        0.11696255937319769,
        0.2558225593363592,
        0.119387737695509
      ],
      "state": "Raw"
    },
    {
      "central80_coverage": 0.728,
      "mean_interval_width": 1.4150506796568834,
      "pinball_losses": [
        0.11696255937319769,
        0.255729783721167,
        0.11940629281854745
      ],
      "state": "Sorted"
    }
  ],
  "final_tail_Brier_calibrated": 0.027140898929349563,
  "final_tail_Brier_raw": 0.02674395564136636,
  "final_threshold_metrics": [
    {
      "false_alarms": 0,
      "mean_cost": 0.2833333333333333,
      "missed": 17,
      "positive_count": 17,
      "recall": 0.0,
      "threshold": 0.5,
      "threshold_rule": "Half"
    },
    {
      "false_alarms": 0,
      "mean_cost": 0.2833333333333333,
      "missed": 17,
      "positive_count": 17,
      "recall": 0.0,
      "threshold": 0.09090909090909091,
      "threshold_rule": "Bayes"
    },
    {
      "false_alarms": 10,
      "mean_cost": 0.26666666666666666,
      "missed": 15,
      "positive_count": 17,
      "recall": 0.11764705882352941,
      "threshold": 0.05,
      "threshold_rule": "Selected"
    }
  ],
  "final_used_for_selection": false,
  "fitted_ordered_thresholds": [
    -1.443134663549861,
    1.1018295509428926,
    2.425096707616819
  ],
  "ordinal_final_assets": 600,
  "ordinal_optimizer_converged": true,
  "ordinal_source_assets": 1000,
  "quantile_crossing_fraction": 0.002,
  "quantile_final_size": 500,
  "quantile_source_size": 1000,
  "rare_calibration_positives": 4,
  "rare_final_positives": 17,
  "rare_selection_positives": 8,
  "selected_threshold": 0.05,
  "structural_zero_labels_observed": false
}
```

