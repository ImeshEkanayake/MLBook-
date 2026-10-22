# Chapter 43 execution evidence

**Date:** 22 October 2026 (Australia/Melbourne). **Status:** published and executed; content-tree verification passed.

All current sources ran in fresh kernels using the unchanged runner. Imports, helpers and generated task observations are internal. code_226 and code_228 also require explicitly acquired pinned cached pretrained files; see the [asset guide](CHAPTER_43_ASSETS.md). Ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency or new asset was added; code_226 and code_228 explicitly reuse pinned existing pretrained checkpoints. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_226 | 43.1 | 5 | 3 | 4.145 |
| code_227 | 43.2 | 5 | 3 | 2.545 |
| code_228 | 43.3 | 5 | 3 | 3.770 |
| code_229 | 43.4 | 5 | 3 | 2.842 |
| code_230 | 43.5 | 5 | 3 | 5.231 |

Total: **25 executed code cells and 15 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

# Chapter 43 mechanisms, controls and interpretation

Five complete generated capstones implement the original scopes and both visual briefs: **25 fresh-kernel code cells and 15 embedded figures**. They retain framing, entity/availability contracts, actual baselines, independent evidence and bounded decisions. The five numerical studies are independently generated; common workflow and provenance diagrams do not turn them into one field dataset. Main Python 3.14.3 / NumPy 2.4.4 / SciPy 1.17.1 / pandas 3.0.3 / Matplotlib 3.11.0 / scikit-learn 1.9.0 / Torch 2.14.1 runtime is unchanged. Own neural computations are deterministic float64 on one CPU thread. Native pretrained inference explicitly uses float32. No new dependency or asset is added.

**Asset exception:** 226 requires the previously used pinned TabPFN v2 classifier checkpoint; 228 requires previously used pinned Chronos-BoltTiny README/config/weights. The new explicit acquisition script fetches only these required artifacts, reuses existing cache bytes and verifies every size/SHA. Notebooks verify again before local native loading with Hub offline mode. The other three capstones generate every input internally. No credentials, gated acceptance or GPU is needed; no weights are published. Guides, manifest, exact revisions and existing licence notices accompany the notebooks. Variable resource measurements from kernels and separate vector-export runs are retained separately from deterministic scientific RESULTS. Access/execution: 22 October 2026, Australia/Melbourne; literature cutoff: 18 October 2026.

- **226 — relational risk.** Eighty buildings × six members; source/development/calibration/final buildings 40/10/10/20. Source origins 60/120, development 180, calibration 220, final 270; thirty-day event plus five-day report maturity is checked before the next role. Entity tables and as-of event/availability joins admit 480 member rows and exclude 480 future measurements. Adding 999 to every future measurement changes no feature. Source-fitted logistic, 50-round seven-leaf histogram boosting, own 5–16–1 tanh neural classifier (180 Adam steps, weight decay 0.01) and actual one-estimator TabPFN v2 all use 240 task labels; upstream pretraining differs. A no-relational logistic ablation uses four rather than five features. Historical earlier-to-later source Brier is 0.149808. Development selects logistic at 0.190167 (neural 0.190505, TabPFN 0.197957, boosting 0.206299). Independent calibration uses 60 labels, increasing logit-remapping slope 0.747310. Final native Brier: logistic 0.156156, neural 0.157565, TabPFN 0.157055, boosting 0.171623; no-relational logistic 0.167680. Calibration worsens selected final Brier to 0.160012. Whole-building paired conditional bootstrap difference +0.003855, interval [−0.002364,0.010150], excludes refitting/selection uncertainty. Material groups: n84/36, positives23/12, Brier0.135409/0.217418, error0.178571/0.388889. Twelve fixed highest-score visits capture nine findings; yield is not causal repair benefit or clearance. Actual three-repeat warm120-row profiles compare implementations without equal-pretraining-budget claims. Visual A aligns five independent capstones with their common evidence chain.
- **227 — inductive graph response.** Positive spring incidence stiffness with node0 fixed and positive loads produces reference node displacement, signed edge force and graph maximum. Forty source and ten development six/eight-node chains; final ten matched chains and ten twelve-node chorded structures. Every solve checks positive free stiffness and equilibrium. Inputs: load, mean incident stiffness, normalized position, support flag, node count. One/two-hop full-neighbour mean-aggregation multitask networks each train250 fixed Adam steps; separate learned node/edge/graph heads, characteristic loss scales10/4/10, hard zero-support embedding. Relational controls use boosted node regression on observable one/two-hop summaries, ridge endpoint force and ridge pooled-graph maximum. Development node RMSE1.732462/3.329945 selects one hop. Matched final node RMSE1.408110/3.322074/1.053558 (one/two-hop/relational); changed size/chord5.452484/1.759328/2.931974. Selected larger-regime edge RMSE2.166804, graph absolute error9.164308 and equilibrium residual RMS2.150799 remain explicit failures. No final architecture reselection. Node/edge permutation differences0; graph3.55e−15. Masking the aggregation chord leaves the last-node output unchanged outside the one-hop receptive field; endpoint influence is separately recorded. Features/stiffness/solver are not recomputed, so this is not a physical intervention. Plot errors use declared characteristic scales rather than mixing physical units as a common score. The schematic chord was repaired to meet its endpoint nodes before delivery.
- **228 — temporal/spatial forecast.** Thirty-two independent three-sensor buildings ×280 hourly observations; source12, development4, calibration10, final6. Source origins128/144/160, development180, calibration192/204/216, final228/240/252; outcome index origin+h−1 becomes available one hour later, and maturity checks pass. Historical128-value contexts, lag24 own/spatial views; horizons1/6/12. Altering future suffix changes no origin features/context. Actual seasonal, ridge autoregressive, boosted spatial60-round/seven-leaf, own48–32–3 neural250-step and frozen native Chronos-BoltTiny families; spatial boosting ablation. Native file hashes verified, no fine-tuning/implicit download, median quantile index4. Development MSE selects Bolt0.022365 vs AR0.027303/neural0.030023/seasonal0.048901/boost0.063758. Final Bolt RMSE[0.104020,0.168386,0.160630], AR[0.106312,0.199029,0.171210], neural[0.127048,0.190020,0.169766], seasonal[0.155924,0.183298,0.202836], spatial boost[0.176045,0.252580,0.228224], own-only boost[0.190127,0.253435,0.247308]. Ten calibration whole-building max scores across sensors/origins/horizons use rank10 and half-width0.462732. All six final groups and all individual outputs fall inside; finite evidence and temporal/exchangeability limits remain, no OOD guarantee. Past-only15% missing fill RMSE0.164740; three-hour delayed history0.554330; changed future seasonal amplitude0.554454/coverage0.641975. Leading missing context falls back to first admitted observation without forecast-horizon access. Monitoring records package/cadence/horizons/coverage trigger/maturity; no automatic replacement. Three-repeat actual warm profiles are separate resource observations.
- **229 — physics/inverse/operator.** Dimensionless fixed-end variable-stiffness bar with conservative face fluxes and tridiagonal banded reference. Constant-coefficient manufactured max errors at31/63/127 interior nodes are5.81567e−5/1.45339e−5/3.63315e−6, with refinement ratio>3.8. Known-load three-sensor noisy bounded inverse recoversa0=1.306945 fromtrue1.3; independent sensors/finer solve RMSE0.000578. Doubling both load/stiffness preserves displacement exactly, exposing joint-scale nonidentifiability. Actual hard-boundary x(1−x) PINN800 Adam steps/65 collocation points; excluded257-point field RMSE8.42603e−6, continuous residual RMS0.005026. Original branch16–32–16/trunk1–32–16 operator600 steps on64 source functions/31 interior reference points,16 development functions RMSE0.001725; branch samples eight load/eight stiffness values. Twenty-four untouched functions/new65-point output grid/finer127-interior reference yield field RMSE0.001866, exact endpoints but flux residual RMS0.337065. A source-trained ridge inverse hybrid uses three measured displacements and known load before solving; field RMSE0.000567 has a different information budget from forward prediction with known stiffness. At out-of-range stiffness0.3, operator field RMSE0.157214. Fixed candidate-grid surrogate proposala0=1.85 passes independently refined255/511-interior-node reference: max displacement0.078936≤0.08, mesh difference1.70303e−7. Reference same-grid minimum feasible is1.85; repair route retained. Actual five-repeat24-field operator/reference workloads are measured separately; no universal speedup or field clearance.
- **230 — sequential control.** Explicit24-hour storage simulator, energy0–4/initial-terminal target2/actions−1/0/+1/efficiency0.9. Current observations and known daily means are causal; future noise is excluded. Price-purchase, soft peak and terminal deviation costs; hard capacity/power masks. Actual tabular Q-learning3,000 episodes; fifty independent development episodes select checkpoint3,000 from1,000/2,000/3,000. Frozen Q, fixed price heuristic and actual three-step causal enumerating planner share200 new final disturbances. Mean costs8.433735/10.695318/7.973228; Q-minus-heuristic difference−2.261583, whole-episode paired interval[−2.434983,−2.080574]. Planner superiority retained. Mean peak purchases3.404443/2.693148/3.059157; terminal deviations0/1.715/0; hard violations0. Two unmasked boundary state/action proposals violate capacity; guarded version0. Twenty valid/unsupported/nonfinite price fixtures return ten learned/ten safe-idle fallback dispositions; simulator protection is not device safety. Deterministic heuristic has zero support at2,754 target-Q state/actions encountered in a separate exploratory log. Two hundred positive-action-support behaviour episodes use0.7heuristic+0.3uniform valid actions; all full-trajectory target weights are zero, ESS0 and numerical IS cost0 is explicitly uninformative, not cost-free control or safety evidence. Visual B maps fictional asset B017 schema/provenance keys only; capstone numerical data are independent.

Every current notebook passes independently with no execution errors. Two native advisories are retained and reviewed: TabPFN warns that CPU contexts above 200 rows may be slow; Torch reports that elastic-process redirects are unsupported on macOS. The measured 240-row CPU context completes successfully, and the capstone does not use elastic process redirects. The checker accepts only these scoped messages; other stderr fails. Notebook227 was rerun after adding endpoint mask influence, correcting the chord drawing and normalizing mixed-unit plot diagnostics. Markdown spacing was polished without changing executed code. Independent isolated vector exports reexecute all code and require exact deterministic RESULTS;15 original figure sets and15 actual inline images are reviewed during delivery. Primary PDFs inspected for GraphSAGE arXivv4 (10 September2018), Physics Informed Deep Learning PartI arXivv1 (28 November2017, PDF30 November) and three-author DeepONet arXivv3 (15 April2020), distinguishing later journal metadata. Existing pretrained revisions/licenses and software APIs remain pinned.

All43 chapters are now drafted once this chapter is registered/compiled/reviewed. The whole-book editorial/technical audit remains required before declaring the objective complete. Keep the first and second PDFs separate; preserve the first preview's original bytes.

## Successful result dictionaries

### code_226

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "tabpfn": "9.2.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 8026.

```json
{
  "asof_admitted_feature_rows": 480,
  "bootstrap_conditions_on_fitted_and_selected_state": true,
  "building_roles": [
    40,
    10,
    10,
    20
  ],
  "calibration_logit_slope": 0.7473096189267787,
  "calibration_scalar_labels": 60,
  "development_Brier": {
    "Boosting": 0.20629853034794948,
    "Logistic": 0.19016712896303994,
    "Neural": 0.19050451507528682,
    "TabPFN": 0.1979574882556628
  },
  "development_scalar_labels": 60,
  "development_selected_family": "Logistic",
  "excluded_future_measurements": 480,
  "final_buildings_bootstrap_unit": 20,
  "final_calibrated_selected_Brier": 0.16001179677536598,
  "final_logistic_without_relational_Brier": 0.1676801828272895,
  "final_material_subgroups": [
    {
      "Brier": 0.13540925560130698,
      "error": 0.17857142857142858,
      "material": 0,
      "n": 84,
      "positives": 23
    },
    {
      "Brier": 0.21741772618150357,
      "error": 0.3888888888888889,
      "material": 1,
      "n": 36,
      "positives": 12
    }
  ],
  "final_native_Brier": {
    "Boosting": 0.17162338347017989,
    "Logistic": 0.15615634991180843,
    "Neural": 0.15756462233188842,
    "TabPFN": 0.15705523021787993
  },
  "final_scalar_labels": 120,
  "future_measurement_intervention_difference": 0.0,
  "group_overlap": 0,
  "historical_earlier_to_later_source_Brier": 0.14980818842185253,
  "inspection_budget": 12,
  "inspection_queue_members": [
    448,
    459,
    446,
    447,
    458,
    427,
    460,
    431,
    360,
    449,
    429,
    444
  ],
  "inspection_queue_observed_findings": 9,
  "inspection_yield_is_not_causal_repair_benefit": true,
  "members_per_building": 6,
  "paired_Brier_difference": 0.0038554468635575386,
  "paired_building_bootstrap95": [
    -0.002364353698842238,
    0.01015023144146765
  ],
  "pretrained_parameters_unchanged_after_initialization": true,
  "probability_calibration_labels": 60,
  "source_scalar_labels": 240
}
```

### code_227

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 8027.

```json
{
  "challenge_node_size": 12,
  "development_node_RMSE": {
    "1-hop": 1.7324624658924228,
    "2-hop": 3.3299452821238065
  },
  "development_selected_GNN": "1-hop",
  "development_structures": 10,
  "edge_mask_is_not_physical_intervention": true,
  "edge_target": "signed spring force",
  "final_labels_select_architecture": false,
  "final_matched_chains": 10,
  "final_new_size_chord_structures": 10,
  "final_per_structure_assessments": {
    "1-hop": [
      {
        "chord": false,
        "edge_RMSE": 0.4151264626680363,
        "equilibrium_residual_RMS": 1.4372563999604808,
        "graph_absolute_error": 0.23560752978297828,
        "n": 6,
        "node_RMSE": 1.7581105101769459
      },
      {
        "chord": false,
        "edge_RMSE": 0.4664449143862366,
        "equilibrium_residual_RMS": 1.8170219079064889,
        "graph_absolute_error": 2.1572378980616698,
        "n": 8,
        "node_RMSE": 1.1562861637228574
      },
      {
        "chord": false,
        "edge_RMSE": 0.1737353399236849,
        "equilibrium_residual_RMS": 3.176829369659044,
        "graph_absolute_error": 0.5376425354482777,
        "n": 6,
        "node_RMSE": 0.8088584766329439
      },
      {
        "chord": false,
        "edge_RMSE": 0.324818868707002,
        "equilibrium_residual_RMS": 1.9294205061235263,
        "graph_absolute_error": 0.7887958839152791,
        "n": 8,
        "node_RMSE": 0.8432606025247542
      },
      {
        "chord": false,
        "edge_RMSE": 0.21690323563410005,
        "equilibrium_residual_RMS": 1.766330997508649,
        "graph_absolute_error": 1.4729338572809265,
        "n": 6,
        "node_RMSE": 2.650154778473203
      },
      {
        "chord": false,
        "edge_RMSE": 0.36254983145908437,
        "equilibrium_residual_RMS": 0.9035287624394062,
        "graph_absolute_error": 2.4683445812184868,
        "n": 8,
        "node_RMSE": 1.4251596062561447
      },
      {
        "chord": false,
        "edge_RMSE": 0.09028292071446604,
        "equilibrium_residual_RMS": 2.7386467277923208,
        "graph_absolute_error": 0.09622105990437646,
        "n": 6,
        "node_RMSE": 0.8657083082443667
      },
      {
        "chord": false,
        "edge_RMSE": 0.09774189200415309,
        "equilibrium_residual_RMS": 1.6216029046284566,
        "graph_absolute_error": 0.672281114000528,
        "n": 8,
        "node_RMSE": 0.9947608149945074
      },
      {
        "chord": false,
        "edge_RMSE": 0.5875794300218605,
        "equilibrium_residual_RMS": 2.9820560707685018,
        "graph_absolute_error": 1.5196499923394633,
        "n": 6,
        "node_RMSE": 1.7932492210767272
      },
      {
        "chord": false,
        "edge_RMSE": 0.17021205390752392,
        "equilibrium_residual_RMS": 1.3845006379004987,
        "graph_absolute_error": 1.8241141226526132,
        "n": 8,
        "node_RMSE": 1.7855483985209466
      },
      {
        "chord": true,
        "edge_RMSE": 2.0876589449023863,
        "equilibrium_residual_RMS": 1.9494509072709334,
        "graph_absolute_error": 10.803515869774722,
        "n": 12,
        "node_RMSE": 6.912355207316447
      },
      {
        "chord": true,
        "edge_RMSE": 2.047763323887312,
        "equilibrium_residual_RMS": 2.073158227041913,
        "graph_absolute_error": 8.909134874027593,
        "n": 12,
        "node_RMSE": 4.928894708406519
      },
      {
        "chord": true,
        "edge_RMSE": 2.113788156466578,
        "equilibrium_residual_RMS": 1.6825015779239167,
        "graph_absolute_error": 7.621182232332263,
        "n": 12,
        "node_RMSE": 4.38096729856165
      },
      {
        "chord": true,
        "edge_RMSE": 2.0685553221403006,
        "equilibrium_residual_RMS": 2.389597454812649,
        "graph_absolute_error": 9.155027736998058,
        "n": 12,
        "node_RMSE": 5.650028564935883
      },
      {
        "chord": true,
        "edge_RMSE": 2.2871429329088264,
        "equilibrium_residual_RMS": 2.619265550804409,
        "graph_absolute_error": 9.485445419249194,
        "n": 12,
        "node_RMSE": 6.086209259775213
      },
      {
        "chord": true,
        "edge_RMSE": 2.045043763161546,
        "equilibrium_residual_RMS": 1.6335568434713663,
        "graph_absolute_error": 8.413039449702124,
        "n": 12,
        "node_RMSE": 4.1952276726402715
      },
      {
        "chord": true,
        "edge_RMSE": 2.2661085225881603,
        "equilibrium_residual_RMS": 2.4875079345035167,
        "graph_absolute_error": 9.686459890666708,
        "n": 12,
        "node_RMSE": 5.980055349144346
      },
      {
        "chord": true,
        "edge_RMSE": 2.305913894593312,
        "equilibrium_residual_RMS": 2.41409889539325,
        "graph_absolute_error": 9.265566989136003,
        "n": 12,
        "node_RMSE": 5.506662188222343
      },
      {
        "chord": true,
        "edge_RMSE": 1.9833811228047964,
        "equilibrium_residual_RMS": 1.7698664482378577,
        "graph_absolute_error": 8.777049922182142,
        "n": 12,
        "node_RMSE": 5.050288857821337
      },
      {
        "chord": true,
        "edge_RMSE": 2.4626855172240747,
        "equilibrium_residual_RMS": 2.4889869921730243,
        "graph_absolute_error": 9.526658268661414,
        "n": 12,
        "node_RMSE": 5.834154918854788
      }
    ],
    "2-hop": [
      {
        "chord": false,
        "edge_RMSE": 0.9058897952385339,
        "equilibrium_residual_RMS": 6.227401389295483,
        "graph_absolute_error": 4.575476317792754,
        "n": 6,
        "node_RMSE": 3.9917013837138646
      },
      {
        "chord": false,
        "edge_RMSE": 1.1724375284187185,
        "equilibrium_residual_RMS": 2.892379994033697,
        "graph_absolute_error": 1.3767521222159953,
        "n": 8,
        "node_RMSE": 2.6473791561406927
      },
      {
        "chord": false,
        "edge_RMSE": 0.8129025079542777,
        "equilibrium_residual_RMS": 3.2645321946294814,
        "graph_absolute_error": 2.5329347044306036,
        "n": 6,
        "node_RMSE": 2.683949838237594
      },
      {
        "chord": false,
        "edge_RMSE": 1.2069900441697707,
        "equilibrium_residual_RMS": 3.0407052034826236,
        "graph_absolute_error": 3.233254083002773,
        "n": 8,
        "node_RMSE": 3.529779304982179
      },
      {
        "chord": false,
        "edge_RMSE": 0.9950974703502679,
        "equilibrium_residual_RMS": 4.113637052516117,
        "graph_absolute_error": 4.810028215603994,
        "n": 6,
        "node_RMSE": 3.779748637476779
      },
      {
        "chord": false,
        "edge_RMSE": 1.1726218226474545,
        "equilibrium_residual_RMS": 3.6634825088059735,
        "graph_absolute_error": 1.044395461363381,
        "n": 8,
        "node_RMSE": 2.795357516027484
      },
      {
        "chord": false,
        "edge_RMSE": 0.9274618098046163,
        "equilibrium_residual_RMS": 4.041099931944523,
        "graph_absolute_error": 2.5554676077891543,
        "n": 6,
        "node_RMSE": 2.7819002306398155
      },
      {
        "chord": false,
        "edge_RMSE": 1.2021556631328043,
        "equilibrium_residual_RMS": 3.4201371710194097,
        "graph_absolute_error": 2.6559187613689925,
        "n": 8,
        "node_RMSE": 3.4468078452230997
      },
      {
        "chord": false,
        "edge_RMSE": 1.3019145716041387,
        "equilibrium_residual_RMS": 4.113490084280357,
        "graph_absolute_error": 6.225180223545749,
        "n": 6,
        "node_RMSE": 4.430180428469179
      },
      {
        "chord": false,
        "edge_RMSE": 1.2115056879774448,
        "equilibrium_residual_RMS": 5.096140560384456,
        "graph_absolute_error": 1.2411282458615833,
        "n": 8,
        "node_RMSE": 3.1339336102686137
      },
      {
        "chord": true,
        "edge_RMSE": 2.324076967388581,
        "equilibrium_residual_RMS": 3.3921852237678314,
        "graph_absolute_error": 2.033711920807594,
        "n": 12,
        "node_RMSE": 1.8168674682366321
      },
      {
        "chord": true,
        "edge_RMSE": 2.274382704156399,
        "equilibrium_residual_RMS": 3.017685784640232,
        "graph_absolute_error": 0.5224120730545998,
        "n": 12,
        "node_RMSE": 1.5705332886265613
      },
      {
        "chord": true,
        "edge_RMSE": 2.3175939988739294,
        "equilibrium_residual_RMS": 2.921681281397783,
        "graph_absolute_error": 1.1119837565435287,
        "n": 12,
        "node_RMSE": 2.3045381111975693
      },
      {
        "chord": true,
        "edge_RMSE": 2.283335473899162,
        "equilibrium_residual_RMS": 2.529323009448963,
        "graph_absolute_error": 0.5639823074634212,
        "n": 12,
        "node_RMSE": 1.5462030280152985
      },
      {
        "chord": true,
        "edge_RMSE": 2.54118011894601,
        "equilibrium_residual_RMS": 3.9642250919360786,
        "graph_absolute_error": 0.8410522318673781,
        "n": 12,
        "node_RMSE": 1.715559103200157
      },
      {
        "chord": true,
        "edge_RMSE": 2.329077451146307,
        "equilibrium_residual_RMS": 2.4243999190879504,
        "graph_absolute_error": 0.36034854571254904,
        "n": 12,
        "node_RMSE": 2.026573456649697
      },
      {
        "chord": true,
        "edge_RMSE": 2.5161844580573938,
        "equilibrium_residual_RMS": 4.067449970466266,
        "graph_absolute_error": 0.8760093382945229,
        "n": 12,
        "node_RMSE": 1.6828560661557443
      },
      {
        "chord": true,
        "edge_RMSE": 2.5216347098045184,
        "equilibrium_residual_RMS": 3.4303173582600865,
        "graph_absolute_error": 0.6582706629558555,
        "n": 12,
        "node_RMSE": 1.5249307462027453
      },
      {
        "chord": true,
        "edge_RMSE": 2.1981469037732655,
        "equilibrium_residual_RMS": 2.319040367710901,
        "graph_absolute_error": 0.08697651043964427,
        "n": 12,
        "node_RMSE": 1.780310977012025
      },
      {
        "chord": true,
        "edge_RMSE": 2.655761535569458,
        "equilibrium_residual_RMS": 3.550160901066525,
        "graph_absolute_error": 1.1044042778098362,
        "n": 12,
        "node_RMSE": 1.624911399651591
      }
    ],
    "Relational baseline": [
      {
        "chord": false,
        "edge_RMSE": 0.5043945271798624,
        "equilibrium_residual_RMS": 2.1651753983984072,
        "graph_absolute_error": 0.8391324687773398,
        "n": 6,
        "node_RMSE": 0.5288555368108174
      },
      {
        "chord": false,
        "edge_RMSE": 0.3615513204089677,
        "equilibrium_residual_RMS": 2.166809636723085,
        "graph_absolute_error": 2.034770224438736,
        "n": 8,
        "node_RMSE": 0.9406977781496945
      },
      {
        "chord": false,
        "edge_RMSE": 0.2721211310905435,
        "equilibrium_residual_RMS": 0.7658086737808711,
        "graph_absolute_error": 0.5617208794477033,
        "n": 6,
        "node_RMSE": 0.8082330549539042
      },
      {
        "chord": false,
        "edge_RMSE": 0.27400895060574726,
        "equilibrium_residual_RMS": 2.0326142463912804,
        "graph_absolute_error": 0.20636078473757102,
        "n": 8,
        "node_RMSE": 0.614572613765445
      },
      {
        "chord": false,
        "edge_RMSE": 0.4493753174647125,
        "equilibrium_residual_RMS": 1.8520451973479886,
        "graph_absolute_error": 1.473027668643926,
        "n": 6,
        "node_RMSE": 1.2010320225307485
      },
      {
        "chord": false,
        "edge_RMSE": 0.24185586221534502,
        "equilibrium_residual_RMS": 1.6833544406260528,
        "graph_absolute_error": 2.22873961500758,
        "n": 8,
        "node_RMSE": 1.6018313510736244
      },
      {
        "chord": false,
        "edge_RMSE": 0.16945222683159894,
        "equilibrium_residual_RMS": 0.6412496800960111,
        "graph_absolute_error": 0.48086275470399187,
        "n": 6,
        "node_RMSE": 0.41294636674283136
      },
      {
        "chord": false,
        "edge_RMSE": 0.1901210770645914,
        "equilibrium_residual_RMS": 1.0533608224478714,
        "graph_absolute_error": 0.640186401883291,
        "n": 8,
        "node_RMSE": 1.2259802486587477
      },
      {
        "chord": false,
        "edge_RMSE": 0.7450295668699956,
        "equilibrium_residual_RMS": 1.1223696715783127,
        "graph_absolute_error": 2.3654403689635686,
        "n": 6,
        "node_RMSE": 1.0917292458192809
      },
      {
        "chord": false,
        "edge_RMSE": 0.14241223909099754,
        "equilibrium_residual_RMS": 0.8782033273705886,
        "graph_absolute_error": 1.8287949153436074,
        "n": 8,
        "node_RMSE": 2.109704878373332
      },
      {
        "chord": true,
        "edge_RMSE": 2.8176332092988714,
        "equilibrium_residual_RMS": 4.647754635763695,
        "graph_absolute_error": 18.270556032658682,
        "n": 12,
        "node_RMSE": 3.4392599230154235
      },
      {
        "chord": true,
        "edge_RMSE": 2.6333457211900244,
        "equilibrium_residual_RMS": 4.551846960823641,
        "graph_absolute_error": 16.372007115261983,
        "n": 12,
        "node_RMSE": 2.8981524341277263
      },
      {
        "chord": true,
        "edge_RMSE": 2.6907140392129523,
        "equilibrium_residual_RMS": 3.5688044662599743,
        "graph_absolute_error": 15.146446614709504,
        "n": 12,
        "node_RMSE": 2.963920403840793
      },
      {
        "chord": true,
        "edge_RMSE": 2.801932656918927,
        "equilibrium_residual_RMS": 4.984074007955596,
        "graph_absolute_error": 16.46684512826656,
        "n": 12,
        "node_RMSE": 3.0322623525579546
      },
      {
        "chord": true,
        "edge_RMSE": 2.9539459178964993,
        "equilibrium_residual_RMS": 4.253195517037338,
        "graph_absolute_error": 17.001305091960532,
        "n": 12,
        "node_RMSE": 3.356393649484324
      },
      {
        "chord": true,
        "edge_RMSE": 2.727586225430599,
        "equilibrium_residual_RMS": 4.439865303751291,
        "graph_absolute_error": 15.709034601149403,
        "n": 12,
        "node_RMSE": 2.6641147958813662
      },
      {
        "chord": true,
        "edge_RMSE": 2.8962469894725738,
        "equilibrium_residual_RMS": 3.1483611639904345,
        "graph_absolute_error": 17.067076367651403,
        "n": 12,
        "node_RMSE": 2.900857836321743
      },
      {
        "chord": true,
        "edge_RMSE": 2.986854850287799,
        "equilibrium_residual_RMS": 4.527361388704993,
        "graph_absolute_error": 16.71228376585251,
        "n": 12,
        "node_RMSE": 2.7836317867617177
      },
      {
        "chord": true,
        "edge_RMSE": 2.761256285109501,
        "equilibrium_residual_RMS": 4.080478592368493,
        "graph_absolute_error": 16.161754929343182,
        "n": 12,
        "node_RMSE": 2.9190455060175675
      },
      {
        "chord": true,
        "edge_RMSE": 3.142778979392909,
        "equilibrium_residual_RMS": 5.8305936088565655,
        "graph_absolute_error": 16.869702341116465,
        "n": 12,
        "node_RMSE": 2.362104143717874
      }
    ]
  },
  "final_regime_profiles": [
    {
      "edge_RMSE": 0.2905394949426148,
      "equilibrium_residual_RMS": 1.975719428468737,
      "graph_absolute_error": 1.17728285746046,
      "model": "1-hop",
      "node_RMSE": 1.4081096880623396,
      "regime": "matched chain",
      "structures": 10
    },
    {
      "edge_RMSE": 2.1668041500677293,
      "equilibrium_residual_RMS": 2.1507990831632835,
      "graph_absolute_error": 9.164308065273023,
      "model": "1-hop",
      "node_RMSE": 5.45248440256788,
      "regime": "new size + chord",
      "structures": 10
    },
    {
      "edge_RMSE": 1.0908976901298026,
      "equilibrium_residual_RMS": 3.987300609039212,
      "graph_absolute_error": 3.025053574297498,
      "model": "2-hop",
      "node_RMSE": 3.32207379511793,
      "regime": "matched chain",
      "structures": 10
    },
    {
      "edge_RMSE": 2.396137432161502,
      "equilibrium_residual_RMS": 3.161646890778262,
      "graph_absolute_error": 0.8159151624948929,
      "model": "2-hop",
      "node_RMSE": 1.7593283644948023,
      "regime": "new size + chord",
      "structures": 10
    },
    {
      "edge_RMSE": 0.3350322218822362,
      "equilibrium_residual_RMS": 1.436099109476047,
      "graph_absolute_error": 1.2659036081947315,
      "model": "Relational baseline",
      "node_RMSE": 1.0535583096878427,
      "regime": "matched chain",
      "structures": 10
    },
    {
      "edge_RMSE": 2.8412294874210655,
      "equilibrium_residual_RMS": 4.403233564551202,
      "graph_absolute_error": 16.577701198797023,
      "model": "Relational baseline",
      "node_RMSE": 2.931974283172649,
      "regime": "new size + chord",
      "structures": 10
    }
  ],
  "graph_roles_disjoint": true,
  "graph_target": "maximum reference displacement",
  "masked_chord_endpoint_prediction_change": 0.4153416281492923,
  "masked_chord_last_node_prediction_change": 0.0,
  "network_source_steps": 250,
  "node_target": "fixed-base spring displacement",
  "permutation_edge_max_difference": 0.0,
  "permutation_graph_difference": 3.552713678800501e-15,
  "permutation_node_max_difference": 0.0,
  "physical_reference_is_generated_not_field_truth": true,
  "source_node_sizes": [
    6,
    8
  ],
  "source_structures": 40,
  "support_prediction_exact_zero": true
}
```

### code_228

Versions: `{"accelerate": "1.15.0", "chronos-forecasting": "2.3.2", "matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1", "transformers": "5.20.1"}`; Darwin arm64 CPU; seed 8028.

```json
{
  "building_roles": [
    12,
    4,
    10,
    6
  ],
  "calibration_buildings": 10,
  "calibration_forecast_windows": 90,
  "calibration_max_score_rank": 10,
  "common_interval_half_width": 0.4627316219827673,
  "development_MSE": {
    "AR ridge": 0.027302615920428687,
    "Boosted spatial": 0.06375835921812176,
    "Frozen Bolt": 0.022365109111266053,
    "Neural spatial": 0.030022877635107574,
    "Seasonal": 0.04890079223661921
  },
  "development_forecast_windows": 12,
  "development_selected_family": "Frozen Bolt",
  "final_RMSE_by_horizon": {
    "AR ridge": [
      0.1063120750901899,
      0.1990291835901751,
      0.17120997946119
    ],
    "Boosted spatial": [
      0.17604496741918943,
      0.252580262080838,
      0.22822366044723347
    ],
    "Frozen Bolt": [
      0.10401972682974958,
      0.168386095778671,
      0.1606298466214871
    ],
    "Neural spatial": [
      0.12704845659899033,
      0.19001976476028404,
      0.16976550764996978
    ],
    "Seasonal": [
      0.15592380642813317,
      0.18329792748852666,
      0.20283563132237795
    ]
  },
  "final_boosted_without_spatial_RMSE_by_horizon": [
    0.19012705750593709,
    0.2534345109939249,
    0.24730768277592555
  ],
  "final_building_coverage_flags": [
    true,
    true,
    true,
    true,
    true,
    true
  ],
  "final_forecast_windows": 54,
  "final_marginal_coverage": 1.0,
  "final_whole_building_coverage": 1.0,
  "frozen_pretrained_weights_unchanged": true,
  "future_feature_intervention_difference": 0.0,
  "horizons_hours": [
    1,
    6,
    12
  ],
  "lag_context_hours": 24,
  "monitoring_specification": {
    "cadence": "hourly",
    "horizons_hours": [
      1,
      6,
      12
    ],
    "input_coverage_trigger": 0.9,
    "label_maturity_hours_after_origin": 12,
    "package_version": "forecast-capstone-v1",
    "response": "investigate missingness and mature errors; do not automatically replace"
  },
  "native_context_hours": 128,
  "native_quantile_median_index": 4,
  "neural_source_steps": 250,
  "sensors_per_building": 3,
  "simultaneous_event": "all three sensors origins and horizons within one final building",
  "source_dev_cal_final_outcomes_mature_before_next_role": true,
  "source_forecast_windows": 108,
  "stress_assessments": {
    "changed_amplitude_marginal_interval_coverage": 0.6419753086419753,
    "changed_future_seasonal_amplitude_RMSE": 0.554453691282022,
    "missing_past_15pct_RMSE": 0.16474010131891564,
    "three_hour_delayed_history_RMSE": 0.5543298027687008
  },
  "temporal_or_OOD_coverage_guarantee": false
}
```

### code_229

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 8029.

```json
{
  "PINN_collocation_points": 65,
  "PINN_dense_field_RMSE": 8.426028881206151e-06,
  "PINN_independent_continuous_residual_RMS": 0.005025711052893875,
  "PINN_source_steps": 800,
  "final_operator_field_RMSE": 0.001865930845812077,
  "final_operator_flux_residual_RMS_mean": 0.33706472010350486,
  "final_sensor_assisted_hybrid_field_RMSE": 0.0005668017737916415,
  "hybrid_has_three_measured_displacements": true,
  "independent_final_functions": 24,
  "independent_sensor_RMSE": 0.0005781437519956325,
  "inverse_estimated_a0": 1.3069453196026486,
  "inverse_sensor_positions": [
    0.2,
    0.5,
    0.8
  ],
  "inverse_true_a0": 1.3,
  "joint_load_stiffness_not_identifiable_from_displacement_alone": true,
  "joint_load_stiffness_scale_counterexample_max_difference": 0.0,
  "manufactured_interior_nodes": [
    31,
    63,
    127
  ],
  "manufactured_max_errors": [
    5.815674401622728e-05,
    1.4533931043309023e-05,
    3.633154443419273e-06
  ],
  "operator_assessment_coordinates": 65,
  "operator_boundary_max_abs": 0.0,
  "operator_development_cases": 16,
  "operator_development_field_RMSE": 0.0017252080438372266,
  "operator_is_own_branch_trunk_not_pretrained": true,
  "operator_source_cases": 64,
  "operator_source_interior_nodes": 31,
  "operator_source_steps": 600,
  "out_of_range_a0": 0.3,
  "out_of_range_operator_field_RMSE": 0.15721410620164875,
  "proposal_passes_declared_reference_limit": true,
  "proposal_reference_mesh_difference": 1.703028744970414e-07,
  "proposal_refined_reference_max_displacement": 0.07893577571896275,
  "reference_assessment_interior_nodes": 127,
  "reference_equation": "-(a u_x)_x=f, fixed endpoint displacements",
  "reference_grid_minimum_feasible_a0": 1.85,
  "surrogate_proposed_design_a0": 1.85,
  "verified_design_is_not_field_clearance": true
}
```

### code_230

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 8030.

```json
{
  "actions_energy_units": [
    -1,
    0,
    1
  ],
  "candidate_training_checkpoints": [
    1000,
    2000,
    3000
  ],
  "capacity_energy_units": 4,
  "deterministic_behaviour_zero_support_Q_state_actions": 2754,
  "development_checkpoint_cost": {
    "1000": 8.74547956663189,
    "2000": 8.538973016853582,
    "3000": 8.440028341246155
  },
  "development_episodes": 50,
  "development_selected_training_checkpoint": 3000,
  "efficiency": 0.9,
  "exploratory_logged_episodes": 200,
  "fallback_fixture_dispositions": [
    "learned",
    "learned",
    "fallback_idle",
    "fallback_idle",
    "learned",
    "learned",
    "fallback_idle",
    "fallback_idle",
    "learned",
    "learned",
    "fallback_idle",
    "fallback_idle",
    "learned",
    "learned",
    "fallback_idle",
    "fallback_idle",
    "learned",
    "learned",
    "fallback_idle",
    "fallback_idle"
  ],
  "fallback_fixture_requests": 20,
  "final_outcomes_choose_checkpoint": false,
  "final_policy_profiles": {
    "Causal planner": {
      "cost": 7.973227819764307,
      "peak_purchase": 3.0591573413464666,
      "terminal_deviation": 0.0,
      "violations": 0.0
    },
    "Frozen Q": {
      "cost": 8.433734941027327,
      "peak_purchase": 3.4044434618130492,
      "terminal_deviation": 0.0,
      "violations": 0.0
    },
    "Heuristic": {
      "cost": 10.69531793596055,
      "peak_purchase": 2.693147775739309,
      "terminal_deviation": 1.715,
      "violations": 0.0
    }
  },
  "finite_IS_observation_is_policy_safety_certificate": false,
  "guarded_capacity_violations": 0,
  "hard_constraints": [
    "energy in [0,4]",
    "absolute action at most1"
  ],
  "horizon_hours": 24,
  "independent_shared_final_episodes": 200,
  "initial_and_target_terminal_energy": 2,
  "paired_Q_minus_heuristic_cost": -2.2615829949332245,
  "paired_whole_episode_bootstrap95": [
    -2.434983230511554,
    -2.0805740347265957
  ],
  "peak_purchase_is_soft_cost": true,
  "planner_future_noise_access": false,
  "raw_unmasked_capacity_violations": 2,
  "representation_provenance_crosswalk": {
    "asset_id": "B017",
    "connectivity_key": [
      "asset_id",
      "node_id",
      "topology_version"
    ],
    "decision_log_key": [
      "asset_id",
      "hour",
      "policy_version",
      "action",
      "disposition"
    ],
    "meaning": "schema crosswalk only; numerical capstone datasets are independently generated",
    "member_table_key": [
      "asset_id",
      "member_id",
      "snapshot_day"
    ],
    "physical_field_key": [
      "asset_id",
      "load_case",
      "coordinate",
      "unit_contract"
    ],
    "sensor_history_key": [
      "asset_id",
      "sensor_id",
      "event_hour",
      "available_hour"
    ]
  },
  "reward": "negative purchase plus peak and terminal cost",
  "training_episodes": 3000,
  "trajectory_IS_cost_observation": 0.0,
  "trajectory_importance_ESS": 0.0,
  "trajectory_nonzero_importance_weights": 0
}
```

## Independent resource observations

Fresh-kernel and independent vector-export measurements are separate actual runs. Timings vary and remain outside deterministic RESULTS. Context, precision, training and forward-call boundaries are explicit; no production throughput or current price claim is made.

### code_226 fresh kernel

```json
{
  "warm_forward_profiles": [
    {
      "median_seconds": 8.900000830180943e-05,
      "model": "Logistic",
      "repetitions": 3,
      "request_rows": 120
    },
    {
      "median_seconds": 0.00017512499471195042,
      "model": "Boosting",
      "repetitions": 3,
      "request_rows": 120
    },
    {
      "median_seconds": 6.587497773580253e-05,
      "model": "Neural",
      "repetitions": 3,
      "request_rows": 120
    },
    {
      "median_seconds": 0.11197812500176951,
      "model": "TabPFN",
      "repetitions": 3,
      "request_rows": 120
    }
  ]
}
```

### code_226 independent vector export

```json
{
  "warm_forward_profiles": [
    {
      "model": "Logistic",
      "request_rows": 120,
      "median_seconds": 8.487497689202428e-05,
      "repetitions": 3
    },
    {
      "model": "Boosting",
      "request_rows": 120,
      "median_seconds": 0.00018283299868926406,
      "repetitions": 3
    },
    {
      "model": "Neural",
      "request_rows": 120,
      "median_seconds": 6.787499296478927e-05,
      "repetitions": 3
    },
    {
      "model": "TabPFN",
      "request_rows": 120,
      "median_seconds": 0.11171045800438151,
      "repetitions": 3
    }
  ]
}
```

### code_228 fresh kernel

```json
{
  "warm_forward_profiles": [
    {
      "horizons": 3,
      "median_seconds": 1.7500133253633976e-06,
      "model": "Seasonal",
      "repetitions": 3,
      "windows": 54
    },
    {
      "horizons": 3,
      "median_seconds": 3.0499999411404133e-05,
      "model": "AR ridge",
      "repetitions": 3,
      "windows": 54
    },
    {
      "horizons": 3,
      "median_seconds": 0.0005612499953713268,
      "model": "Boosted spatial",
      "repetitions": 3,
      "windows": 54
    },
    {
      "horizons": 3,
      "median_seconds": 6.741599645465612e-05,
      "model": "Neural spatial",
      "repetitions": 3,
      "windows": 54
    },
    {
      "horizons": 3,
      "median_seconds": 0.006806666991906241,
      "model": "Frozen Bolt",
      "repetitions": 3,
      "windows": 54
    }
  ]
}
```

### code_228 independent vector export

```json
{
  "warm_forward_profiles": [
    {
      "model": "Seasonal",
      "windows": 54,
      "horizons": 3,
      "repetitions": 3,
      "median_seconds": 1.7920101527124643e-06
    },
    {
      "model": "AR ridge",
      "windows": 54,
      "horizons": 3,
      "repetitions": 3,
      "median_seconds": 2.9375019948929548e-05
    },
    {
      "model": "Boosted spatial",
      "windows": 54,
      "horizons": 3,
      "repetitions": 3,
      "median_seconds": 0.0005363339732866734
    },
    {
      "model": "Neural spatial",
      "windows": 54,
      "horizons": 3,
      "repetitions": 3,
      "median_seconds": 6.829199264757335e-05
    },
    {
      "model": "Frozen Bolt",
      "windows": 54,
      "horizons": 3,
      "repetitions": 3,
      "median_seconds": 0.006732834008289501
    }
  ]
}
```

### code_229 fresh kernel

```json
{
  "operator_24_fields": {
    "median_seconds": 0.00022175000049173832,
    "repetitions": 5
  },
  "reference_24_fields_127_interior": {
    "median_seconds": 0.0006730000022798777,
    "repetitions": 5
  }
}
```

### code_229 independent vector export

```json
{
  "operator_24_fields": {
    "median_seconds": 0.0001956670021172613,
    "repetitions": 5
  },
  "reference_24_fields_127_interior": {
    "median_seconds": 0.0005887080042157322,
    "repetitions": 5
  }
}
```



## Layout and publication verification

All fifteen inline figures and fifteen vector book figures were visually inspected. Repairs include category labels, diagram geometry and within-section figure placement. The second preview contains 26 Chapter 43 pages, all reviewed with its six front-matter and ten reference pages. All 224 earlier body pages are pixel-identical after the added contents-page offset. Content revision [2bb3e5a8a08bfe234db264248d83b9eb4dea64f7](https://github.com/ImeshEkanayake/MLBook-/commit/2bb3e5a8a08bfe234db264248d83b9eb4dea64f7) has 394 remote blobs matching the clean local checkout. The subsequent metadata revision is separately checked for full-tree and commit-addressed raw-file equality. Only companion artifacts are published.
