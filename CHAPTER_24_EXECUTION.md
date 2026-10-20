# Chapter 24 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. Added statsmodels 0.15.0, patsy 1.0.3, formulaic 1.2.2, interface-meta 2.0.1 and wrapt 2.5.1; every previously installed distribution version is unchanged. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_121 | 24.1 | 4 | 2 | 2.271 |
| code_122 | 24.2 | 4 | 2 | 3.889 |
| code_123 | 24.3 | 4 | 2 | 15.948 |
| code_124 | 24.4 | 4 | 2 | 2.460 |
| code_125 | 24.5 | 4 | 2 | 6.554 |
| code_126 | 24.6 | 4 | 2 | 2.137 |

Total: **24 executed code cells and 12 inline figures**. Current outputs contain no errors and all assertions pass. All twelve inline figures and twelve vector book figures have been visually reviewed, including repaired labels and spatial edges.

## Actual mechanisms and boundaries

## Evidence and interpretation

Six generated-data laboratories execute independently with seeds 2721–2726. Every issue time admits only its completed context, static attributes, and explicitly preannounced future covariates. The examples test information availability as well as prediction error. They are finite synthetic demonstrations, not field-validated energy, alarm or structural forecasting systems. No neural foundation forecast service or complete PatchTST implementation is claimed.

### Origins, baselines and shared forecasts — code_121

Sixteen building demand series contain 2,160 hourly observations. The 48-hour context and 24-hour output window stay inside their declared fitting, development or final cohort. Origins are the first unobserved index. Source-only transformations, independent development selection and frozen final parameters apply to local/direct, global/direct and global/recursive Ridge forecasts. Future weather is an issued conditional trajectory from the admitted last weather value and declared generator, never subsequently refreshed with realized weather. Poisoning future outcomes or weather leaves admitted inputs unchanged.

Final mean squared errors are persistence 7.993172, daily seasonal 9.304228, weekly seasonal 4.546387, local direct 2.138517, global direct 2.099402 and global recursive 1.836063. The local/direct, global/direct and recursive coefficient-plus-intercept counts are 48,384, 3,408 and 26; these exclude stored preprocessing state. The direct and recursive fits have equal scalar target counts but different context counts. A weekly baseline was added after inspecting completeness against the known weekly generator; all earlier candidates and their results remained unchanged. This authoring correction is not represented as a preregistered untouched-test comparison.

### Classical and latent dynamics — code_122

Native statsmodels Holt–Winters, ARIMA(1,1,1), SARIMAX dynamic regression, VAR(2) and a local-level state-space model run alongside seasonal and lag-Ridge forecasts. Parameters fit on the first 720 hours; later origins can filter or update observed prefixes while preserving fitted parameters. All four numerical maximum-likelihood/smoothing optimizers report convergence. Both fitted VAR coefficient systems have stable roots; that diagnostic does not establish stationarity of their observed inputs.

The initial raw VAR deliberately remains as a failed use on integrated, seasonal demand. Primary-documentation review prompted an additional candidate: source-only regression removes known calendar/occupancy/trend structure, residual demand is differenced, a VAR predicts its differences with ambient level, and forecasts reconstruct from the admitted last residual. This changes both stationarity treatment and availability of known future regression covariates; it is not a one-factor ablation. Earlier family forecasts are unchanged. Mean final errors are seasonal 1.687457, Holt–Winters 0.781457, ARIMA 2.725781, dynamic regression 0.246182, lag Ridge 0.267520, raw VAR 6.385160, differenced VAR 0.177624 and state space 0.262494. Future-observation perturbations leave past filtered states unchanged but change retrospective smoothed states. Generated latent reference states are diagnostic truth, never fitted observations.

### Neural and lag forecasts — code_123

Eight buildings provide source, development and final windows for horizons 1, 6 and 24. Every model receives the same admitted 48-hour multichannel history and issued future covariates. Actual native histogram gradient boosting, GRU, causal dilated convolution, history attention and a four-patch attention encoder fit the data. Each neural model receives two learning rates and 300 updates with shared minibatch indices, its own development checkpoint and frozen final evaluation. Capacities differ: 1,079 GRU, 2,363 convolution, 1,799 history-attention and 2,195 patch-attention parameters. The patch model mixes channels within patches and is not the published channel-independent PatchTST system.

Mean final errors are 0.471902, 0.311283, 0.328307, 0.273926 and 0.331385 respectively. Boosting performs best at the shortest horizon; history attention performs best at 24 hours. Patch attention does not win uniformly. A within-history perturbation verifies the convolution's causal encoder positions. The attention models encode a fully observed past window, so unmasked history attention does not imply future-target leakage.

### Signals and event exposure — code_124

A completed 100-Hz window contains 8- and 30-Hz components. Naive reduction to 25 Hz produces a 5-Hz alias of amplitude 0.700000; native SciPy polyphase filtering reduces it to 0.000134 while retaining amplitude 1.001346 at 8 Hz, after trimming boundary transients. This zero-phase offline filter is explicitly not a causal online processor. A separate irregular-sampling experiment distinguishes retrospectively interpolated windows from previous-observation holding; changing a future value changes interpolation but leaves the causal held value unchanged.

Sixty buildings generate alarm counts, event times and unequal recording exposures, split 40/10/10 by building. Native Poisson regression models rate using exposure weights and known interval covariates. Final ten-building data contain 311 events. Constant versus covariate intensity gives process negative log likelihood per day 0.796220 versus 0.738275 and any-event Brier score 0.227459 versus 0.193561. Complete rescaled gaps have descriptive KS statistics 0.057977 and 0.029981. End-of-record hazard contributes to likelihood but is not misreported as a completed event gap. Complete event recording is an explicit assumption; unrecorded downtime would invalidate these exposure calculations.

### Shared spatial dynamics — code_125

A known twenty-location mesh with planned moving loads supplies 360 hours. The first twelve locations are source sensors; measurements and labels for the right eight locations are withheld from fitting and model selection. Geometry and adjacency are known, making this a known-mesh regional holdout rather than unseen geometry. Source-only scaling, random source measurement dropout and a separate development time cohort apply to a spatial Gaussian process, shared GRU and graph GRU. Poisoning held-region measurements leaves admitted inputs unchanged.

The shared and graph GRUs have 1,051 and 1,483 parameters and each receives two learning rates and 400 updates. Mean final source errors are GP 0.001300, shared GRU 0.001332 and graph GRU 0.002430. Held-region errors are 0.025818, 0.057686 and 0.116564. The graph model's twelve-hour held-region error is 0.265382; its negative extrapolations remain visible. The graph does not automatically supply successful spatial transfer. Visual B shows actual immediate and skip-neighbor edges and separates parameter sharing from message passing.

### Joint trajectories and regime shift — code_126

Nine members, three buildings and one root give thirteen coherent outcome series. Independent node forecasts are intentionally incoherent. Thirty calibration origins supply positive definite, horizon-specific shrunk covariance estimates and pooled or regime-conditioned whole-error-block draws. Each of thirty final origins has 400 joint draws. The reconciliation matrix satisfies its projection and summation identities. Point incoherence falls from 2.811046 to approximately 2.84e-14; every reconciled draw is coherent to 5.68e-14. Marginal quantiles nevertheless have an additivity gap of 3.113967. Positivity in this particular sample is not a nonnegative-reconciliation guarantee.

Calibration has only fifteen origins in each regime. Before the unannounced high-regime shift, nominal 80% member intervals at 24 hours cover 0.603175 using pooled reconciliation and 0.746032 using regime conditioning. After the shift they cover 0.277778 and 0.347222. These represent only seven and eight origin groups respectively, each with nine dependent member outcomes. Regime-conditioned intervals are wider and improve coverage here, but remain badly undercovered after the shift. Coherence is a constraint, not a calibration or universal accuracy guarantee. Later forecasts may use legitimately observed post-shift context while keeping model and calibration parameters frozen.

## Sources, environment and verification

Primary sources include official statsmodels model and stationarity documentation, the original PatchTST paper (first submitted 27 November 2022; ICLR 2023), SciPy's resample_poly documentation, scikit-learn Poisson/boosting documentation, Jakob Gulddahl Rasmussen's 2018 point-process lecture notes, GPML and Wickramasuriya, Athanasopoulos and Hyndman's 2019 JASA MinT paper. Literature is bounded by 18 October 2026; access checks occurred 20 October 2026. Live SciPy documentation is newer than the executed 1.17.1 installation; live scikit-learn maintenance documentation is 1.9.1 while execution uses 1.9.0. Actual installed APIs and outputs are checked directly.

Native classical execution adds statsmodels 0.15.0, patsy 1.0.3, formulaic 1.2.2, interface-meta 2.0.1 and stable wrapt 2.5.1 to both pinned dependency files. Primary release metadata verifies all five releases before the literature cutoff. The candidate prerelease wrapt 2.5.2rc1 was excluded. Every previously installed distribution version remains unchanged and pip check passes. CPU execution uses the existing numerical core and Torch 2.14.1, float64 and explicit thread controls. Each notebook reports actual versions, hardware and seeds.

All six current notebooks pass fresh kernels: 24 executed code cells, twelve inline figures, no errors or stderr warnings. Layout repairs to classical residual panels, sampling titles and the spatial information diagram were rerun in fresh kernels with exact result agreement. The added weekly baseline and differenced VAR are documented authoring additions, with prior family outputs preserved. The book figure producer reruns every current code cell and requires exact deterministic RESULTS agreement; no timing/resource replay exception is used. All twelve inline and twelve vector-book figures have been visually inspected, including final repaired labels and actual graph edges. Composed PDF review and publication verification are recorded separately in the chapter review package.

## Successful result dictionaries

### code_121

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "statsmodels": "0.15.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2721.

```json
{
  "building_count": 16,
  "candidates": [
    {
      "alpha": 1.0,
      "development_MSE": 3.0626338988912583,
      "family": "Local direct"
    },
    {
      "alpha": 100.0,
      "development_MSE": 2.1898655402487077,
      "family": "Local direct"
    },
    {
      "alpha": 1.0,
      "development_MSE": 3.2038091825866735,
      "family": "Global direct"
    },
    {
      "alpha": 100.0,
      "development_MSE": 2.2205293629598413,
      "family": "Global direct"
    },
    {
      "alpha": 1.0,
      "development_MSE": 1.6471032479975674,
      "family": "Global recursive"
    },
    {
      "alpha": 100.0,
      "development_MSE": 1.6705627832870333,
      "family": "Global recursive"
    }
  ],
  "comparisons": [
    {
      "MSE_by_horizon": [
        1.1826834443647314,
        2.476653370767406,
        3.3076054177192358,
        4.526521330533378,
        3.8592140672194777,
        4.334060101738665,
        3.3554328399734668,
        2.8394273562524317,
        13.898239783332748,
        14.365054233434012,
        11.965785489721107,
        10.186411577121676,
        9.553412879663002,
        7.331765494809477,
        8.427619811279117,
        8.745006300547262,
        9.786582318896613,
        11.512290739847748,
        10.052915912353532,
        10.25213841647268,
        9.027078845613296,
        8.991992550038798,
        10.524170856945739,
        11.334058030820389
      ],
      "final_MSE": 7.993171715394416,
      "horizon_1_MSE": 1.182683444364732,
      "horizon_24_MSE": 11.334058030820385,
      "horizon_6_MSE": 4.334060101738669,
      "method": "Persistence"
    },
    {
      "MSE_by_horizon": [
        9.749172689586109,
        10.407796773775116,
        11.767749897643048,
        11.695692870819478,
        10.840139469784814,
        11.421627273353723,
        10.362468865196597,
        10.708857998998328,
        7.225218594860938,
        9.842764351067645,
        8.236548323808972,
        7.179196693203065,
        6.514514828028111,
        6.914285402351408,
        8.937543632000223,
        8.725880750321958,
        6.696417637535859,
        8.363578033369535,
        6.355649934906072,
        7.5092154850967825,
        8.85146093929823,
        11.91409862136225,
        11.747536948788904,
        11.334058030820389
      ],
      "final_MSE": 9.304228085249067,
      "horizon_1_MSE": 9.749172689586107,
      "horizon_24_MSE": 11.334058030820385,
      "horizon_6_MSE": 11.421627273353726,
      "method": "Seasonal naive"
    },
    {
      "MSE_by_horizon": [
        2.4201930937833613,
        2.8224020596248183,
        4.246784693291943,
        5.93967667539247,
        5.464702330601963,
        6.511221801279024,
        5.453415041228819,
        7.2751251711287725,
        6.786931113468419,
        7.149131757154015,
        5.492781732049417,
        4.331199521217999,
        3.044500739438782,
        2.3062487379406074,
        2.970848162348226,
        3.546377051810475,
        4.6445801063235885,
        5.1702342693782075,
        4.608634883088744,
        3.980421796237219,
        3.8470027110425553,
        3.5920709062387446,
        4.1827806194741814,
        3.3260188505281882
      ],
      "final_MSE": 4.546386826002939,
      "horizon_1_MSE": 2.420193093783362,
      "horizon_24_MSE": 3.32601885052819,
      "horizon_6_MSE": 6.511221801279028,
      "method": "Weekly naive"
    },
    {
      "MSE_by_horizon": [
        1.1463675905191657,
        1.4926769719127888,
        1.7514459271372786,
        2.184143110130044,
        1.6924747882798965,
        2.6699462623633026,
        2.005035079946518,
        3.0268569937288357,
        2.5900410634273743,
        3.3018622526068473,
        2.4497975731300072,
        2.2513503470324863,
        1.640586674727607,
        1.3036726196230262,
        2.087896528367545,
        1.9031958601199872,
        1.840293969134712,
        2.157389231952332,
        2.1211266419274137,
        2.0964001819920526,
        2.2093910959329164,
        2.3248336735571495,
        2.458445589414941,
        2.619180128154501
      ],
      "final_MSE": 2.138517089796614,
      "horizon_1_MSE": 1.1463675905191637,
      "horizon_24_MSE": 2.619180128154501,
      "horizon_6_MSE": 2.6699462623633026,
      "method": "Local direct"
    },
    {
      "MSE_by_horizon": [
        1.1280286124582728,
        1.3565018942303129,
        1.459800875702671,
        1.911760393822996,
        1.3271691228123896,
        2.6510923599709475,
        1.9437541075693507,
        3.397377663646381,
        2.3223448745899113,
        3.143285368833419,
        2.4915704083108765,
        2.2908812509382477,
        1.7037171850519277,
        1.2748406560570245,
        2.201704515617743,
        2.3953459005549225,
        1.7619352104668258,
        1.975690337283403,
        2.330735693283807,
        2.1871858175276784,
        2.1034889085623463,
        2.292113800283632,
        2.3205904237002106,
        2.4147376250039883
      ],
      "final_MSE": 2.0994022085949706,
      "horizon_1_MSE": 1.1280286124582732,
      "horizon_24_MSE": 2.4147376250039905,
      "horizon_6_MSE": 2.651092359970951,
      "method": "Global direct"
    },
    {
      "MSE_by_horizon": [
        0.7808531424885922,
        1.3282802188978884,
        1.4301427906290485,
        1.84980748664983,
        1.3575639064523475,
        2.185082135725908,
        1.7728347461589964,
        2.776783213233258,
        2.3570041989453476,
        2.5534571563458646,
        1.849217866327119,
        1.4936580315873471,
        1.4581141590288573,
        1.1035902152169796,
        2.012348598021478,
        1.5141172877985636,
        1.826645617930666,
        1.8948712170267188,
        2.5227296722877153,
        1.8285326783800224,
        1.9297110281177876,
        2.0759692743678118,
        2.183437202155154,
        1.980754392319489
      ],
      "final_MSE": 1.8360627598371995,
      "horizon_1_MSE": 0.780853142488593,
      "horizon_24_MSE": 1.9807543923194888,
      "horizon_6_MSE": 2.185082135725907,
      "method": "Global recursive"
    }
  ],
  "context_hours": 48,
  "cutoffs": {
    "final_begin": 1560,
    "fit_end_exclusive": 1200
  },
  "direct_feature_count": 141,
  "fitted_linear_coefficients_and_intercepts": {
    "Global direct": 3408,
    "Global recursive": 26,
    "Local direct": 48384
  },
  "future_energy_perturbation_changes_frozen_forecast": false,
  "future_weather_perturbation_changes_issued_forecast": false,
  "horizon_hours": 24,
  "hourly_length": 2160,
  "invalid_realized_weather_substitution_prediction_RMS": 0.9101986197634393,
  "origin_counts": {
    "development": 15,
    "final": 25,
    "train": 48
  },
  "recursive_feature_count": 25,
  "recursive_selected_alpha": 1.0,
  "training_counts": {
    "direct_context_rows": 768,
    "direct_scalar_targets": 18432,
    "recursive_context_rows": 18432,
    "recursive_scalar_targets": 18432
  },
  "weather_provider_AR": 0.85
}
```

### code_122

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "statsmodels": "0.15.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2722.

```json
{
  "ARIMA_parameters": {
    "ar.L1": 0.5877199935015383,
    "ma.L1": -0.49061038600582974,
    "sigma2": 0.21894757095953954,
    "x1": 0.0016257132265919347
  },
  "VAR_order": 2,
  "VAR_stable": true,
  "comparisons": [
    {
      "MSE_by_horizon": [
        0.32490614148862945,
        0.22535905224548453,
        0.3035791774414116,
        0.28125749662037947,
        0.23948883103964153,
        0.1387800070048713,
        0.19466186080758768,
        0.2935847218716103,
        0.3789352066741135,
        4.760605951048442,
        3.7709456400809023,
        4.7523084342553945,
        4.405111818406214,
        4.140221525883802,
        3.7324832773103687,
        3.835789062902923,
        3.1767047422448402,
        3.7767997936081033,
        0.261249419968247,
        0.22076348994758263,
        0.2819571901983435,
        0.19594753603451062,
        0.40098964522609715,
        0.4065427107741268
      ],
      "development_MSE": 1.1923942123510964,
      "final_MSE": 1.687457197211818,
      "horizon_1_MSE": 0.32490614148862945,
      "horizon_24_MSE": 0.4065427107741268,
      "model": "Seasonal naive"
    },
    {
      "MSE_by_horizon": [
        0.11350032765242668,
        0.21315337120463637,
        0.22439714733461394,
        0.2594107070795556,
        0.24583341247810683,
        0.19257174971675942,
        0.19296878400709974,
        0.2199701741386876,
        0.24748799510372463,
        1.9670037914357148,
        1.5445315783112874,
        1.875915042584167,
        1.6471415907465097,
        1.6060689527890375,
        1.3274484304087213,
        1.468186440354422,
        1.5184753264308049,
        1.8075474651180035,
        0.3867523457917557,
        0.3349241004068923,
        0.2753530558881086,
        0.29666025950017355,
        0.39074251204018273,
        0.39893455671980466
      ],
      "development_MSE": 0.5342620140526984,
      "final_MSE": 0.7814574632183832,
      "horizon_1_MSE": 0.11350032765242668,
      "horizon_24_MSE": 0.39893455671980466,
      "model": "Holt-Winters"
    },
    {
      "MSE_by_horizon": [
        0.34219588402131595,
        1.009613708767629,
        1.7662170618268997,
        2.9969128898775867,
        3.9409031632951477,
        3.781951062275702,
        3.598207016331157,
        2.9701669394141126,
        1.871606006906927,
        7.855076688192756,
        5.569750428561249,
        3.7114090875116768,
        2.5689198329979437,
        1.5668614989764271,
        1.0685963383392303,
        1.2633237825993477,
        1.5678249282456589,
        1.9704311756605755,
        5.41897412427832,
        4.432732489319345,
        3.1590079032098326,
        1.7020186616737043,
        0.8165448877555495,
        0.46950971467469127
      ],
      "development_MSE": 2.7389746687953456,
      "final_MSE": 2.7257814697796996,
      "horizon_1_MSE": 0.34219588402131595,
      "horizon_24_MSE": 0.46950971467469127,
      "model": "ARIMA"
    },
    {
      "MSE_by_horizon": [
        0.11958840701356344,
        0.14879090589965388,
        0.15240575019781324,
        0.2454313509280266,
        0.2659363161861261,
        0.1936114051362105,
        0.20121199280739716,
        0.2441385719644907,
        0.2818548028550772,
        0.16162660908684598,
        0.19876420486625618,
        0.23693762189067322,
        0.2887098226053832,
        0.2545702012291484,
        0.3346093191524804,
        0.33684025562519504,
        0.24146507663013014,
        0.21874459566596577,
        0.27544725216014554,
        0.22002242709458503,
        0.2259509902549493,
        0.28726254323926814,
        0.4346663306314465,
        0.3397777356122579
      ],
      "development_MSE": 0.1128369839975734,
      "final_MSE": 0.24618185369721207,
      "horizon_1_MSE": 0.11958840701356344,
      "horizon_24_MSE": 0.3397777356122579,
      "model": "Dynamic regression"
    },
    {
      "MSE_by_horizon": [
        0.23626229269512972,
        0.20231132603462676,
        0.1929000913685511,
        0.25672623090972724,
        0.2521798290458599,
        0.17996015859573192,
        0.18407143139509946,
        0.22930524460505794,
        0.2757313972861076,
        0.392053079330781,
        0.1921631611258591,
        0.23885555597032707,
        0.28709850864692765,
        0.26663268634080933,
        0.35255052750191984,
        0.3483021570182042,
        0.24751138495888095,
        0.22151762017874269,
        0.21150943668237526,
        0.250175337040182,
        0.27752266776094703,
        0.3292075711300641,
        0.4551375232013938,
        0.34079093538465954
      ],
      "development_MSE": 0.1256371813603836,
      "final_MSE": 0.2675198397586652,
      "horizon_1_MSE": 0.2362622926951296,
      "horizon_24_MSE": 0.3407909353846595,
      "model": "Lag Ridge"
    },
    {
      "MSE_by_horizon": [
        0.6166849029043181,
        2.1485421254747212,
        4.225729634481354,
        7.0871995015192395,
        9.612927530992504,
        10.387522301371146,
        10.816153205148835,
        10.273890216414127,
        8.630557589138252,
        19.05233587640858,
        15.838483223187874,
        12.311997569873729,
        9.876411095962053,
        6.8921266362061715,
        5.4129586755392225,
        4.549258835401507,
        3.4247036474042845,
        3.3819455939168073,
        0.42853279424604895,
        0.30831509063875334,
        0.3969323808281608,
        1.076164510184796,
        2.5025788684570425,
        3.9918983209428083
      ],
      "development_MSE": 3.424475357602453,
      "final_MSE": 6.38516042194343,
      "horizon_1_MSE": 0.6166849029043181,
      "horizon_24_MSE": 3.9918983209428083,
      "model": "Raw VAR"
    },
    {
      "MSE_by_horizon": [
        0.10984228254105569,
        0.15280445956835825,
        0.1495497304875955,
        0.18359140450473682,
        0.15506803326633944,
        0.1165931321437648,
        0.10229489747187259,
        0.11705524996984717,
        0.18821229401919026,
        0.19287953314819575,
        0.14440485981409468,
        0.20333396611194302,
        0.16726445550193075,
        0.24317046668058095,
        0.214771082461918,
        0.1581850417768636,
        0.2259039779399067,
        0.23466231776962507,
        0.22374383636760525,
        0.1539631072318628,
        0.14206755689290576,
        0.13807672481030425,
        0.2822684754027726,
        0.26328059571163326
      ],
      "development_MSE": 0.10663930505733887,
      "final_MSE": 0.17762447839978762,
      "horizon_1_MSE": 0.10984228254105569,
      "horizon_24_MSE": 0.2632805957116333,
      "model": "Differenced VAR"
    },
    {
      "MSE_by_horizon": [
        0.1267755535894571,
        0.20313349080903484,
        0.20618522268143763,
        0.24433289693740332,
        0.22974150676103985,
        0.16569729470832514,
        0.1637256936406714,
        0.19469884098482346,
        0.22093232991852596,
        0.21145830395739326,
        0.26007707703493577,
        0.2466032243883219,
        0.24663875303555488,
        0.350622882346897,
        0.27836050242992566,
        0.2914993557953106,
        0.3642924087256241,
        0.3639752002355614,
        0.3478886240487128,
        0.29678764252052736,
        0.2584630364809511,
        0.27691426820362547,
        0.37679185922714226,
        0.3742587818569051
      ],
      "development_MSE": 0.1611780409598295,
      "final_MSE": 0.26249394792992115,
      "horizon_1_MSE": 0.1267755535894571,
      "horizon_24_MSE": 0.3742587818569051,
      "model": "Structural state"
    }
  ],
  "development_origins": [
    720,
    744,
    768,
    792,
    816,
    840,
    864,
    888,
    912,
    936
  ],
  "differenced_VAR_order": 2,
  "differenced_VAR_stable": true,
  "dynamic_parameters": {
    "ar.L1": 0.6671090290344155,
    "intercept": -3.019743563137545e-05,
    "ma.L1": 0.014026472896274981,
    "sigma2": 0.023631703692507378,
    "x1": 0.7185582773262346,
    "x2": 0.8900635477363567,
    "x3": 0.22344949248743512,
    "x4": 0.35611972757455884
  },
  "final_origins": [
    960,
    984,
    1008,
    1032,
    1056,
    1080,
    1104,
    1128,
    1152,
    1176,
    1200,
    1224,
    1248,
    1272,
    1296,
    1320,
    1344,
    1368,
    1392,
    1416
  ],
  "future_perturbation_changes_historical_filtered_state": false,
  "future_perturbation_historical_smoothed_level_max_difference": 1.062314537183202,
  "horizon": 24,
  "optimizer_converged": {
    "ARIMA": true,
    "Dynamic regression": true,
    "Holt-Winters": true,
    "Structural state": true
  },
  "prefix_filtered_state_max_error": 0.0,
  "source_hours": 720,
  "source_residual_diagnostics": [
    {
      "lag1_correlation": 0.8008368119865028,
      "lag24_correlation": -0.5161652614756888,
      "model": "Seasonal naive",
      "source_residual_count": 696
    },
    {
      "lag1_correlation": -0.049617195312764296,
      "lag24_correlation": -0.16696894734973608,
      "model": "Holt-Winters",
      "source_residual_count": 672
    },
    {
      "lag1_correlation": -0.00890411919168051,
      "lag24_correlation": 0.6436228935909138,
      "model": "ARIMA",
      "source_residual_count": 672
    },
    {
      "lag1_correlation": 0.007352575912032995,
      "lag24_correlation": 0.013047303778649695,
      "model": "Dynamic regression",
      "source_residual_count": 672
    },
    {
      "lag1_correlation": 0.5026821313311615,
      "lag24_correlation": 0.017497127024555074,
      "model": "Lag Ridge",
      "source_residual_count": 696
    },
    {
      "lag1_correlation": -0.024014147856899145,
      "lag24_correlation": 0.6793664959670893,
      "model": "Raw VAR",
      "source_residual_count": 718
    },
    {
      "lag1_correlation": -0.015500713627405136,
      "lag24_correlation": 0.033639052373729765,
      "model": "Differenced VAR",
      "source_residual_count": 717
    },
    {
      "lag1_correlation": 0.05619622108074628,
      "lag24_correlation": 0.01907517935966742,
      "model": "Structural state",
      "source_residual_count": 672
    }
  ],
  "structural_parameters": {
    "beta.x1": 1.686500849774928,
    "sigma2.irregular": 0.007291382878571143,
    "sigma2.level": 0.014260389154802012
  },
  "total_hours": 1440
}
```

### code_123

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "statsmodels": "0.15.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2723.

```json
{
  "TCN_prefix_max_difference": 0.0,
  "TCN_receptive_span": 63,
  "building_count": 8,
  "candidates": [
    {
      "development_MSE": 0.7243733204053274,
      "family": "Lag boosting",
      "max_leaf_nodes": 7
    },
    {
      "development_MSE": 0.7170210762999332,
      "family": "Lag boosting",
      "max_leaf_nodes": 15
    },
    {
      "best_step": 300,
      "development_MSE": 0.4853945836313141,
      "family": "GRU",
      "rate": 0.003
    },
    {
      "best_step": 240,
      "development_MSE": 0.44908386874360584,
      "family": "GRU",
      "rate": 0.01
    },
    {
      "best_step": 160,
      "development_MSE": 0.47523837967937327,
      "family": "Causal TCN",
      "rate": 0.003
    },
    {
      "best_step": 100,
      "development_MSE": 0.46864399361914455,
      "family": "Causal TCN",
      "rate": 0.01
    },
    {
      "best_step": 150,
      "development_MSE": 0.4779888503249997,
      "family": "History attention",
      "rate": 0.003
    },
    {
      "best_step": 80,
      "development_MSE": 0.4763114349917562,
      "family": "History attention",
      "rate": 0.01
    },
    {
      "best_step": 210,
      "development_MSE": 0.47308510797901987,
      "family": "Patch attention",
      "rate": 0.003
    },
    {
      "best_step": 80,
      "development_MSE": 0.49872877056686293,
      "family": "Patch attention",
      "rate": 0.01
    }
  ],
  "comparisons": [
    {
      "MSE_by_horizon": [
        0.09253000523931146,
        0.6141965216953309,
        0.7089793885775645
      ],
      "development_MSE": 0.7170210762999332,
      "final_MSE": 0.4719019718374023,
      "model": "Lag boosting"
    },
    {
      "MSE_by_horizon": [
        0.14091068621007238,
        0.3840078720514471,
        0.4089311880513694
      ],
      "development_MSE": 0.4490838687436059,
      "final_MSE": 0.311283248770963,
      "model": "GRU"
    },
    {
      "MSE_by_horizon": [
        0.24175053901402918,
        0.3345075079988117,
        0.4086616133593477
      ],
      "development_MSE": 0.4686439936191446,
      "final_MSE": 0.3283065534573962,
      "model": "Causal TCN"
    },
    {
      "MSE_by_horizon": [
        0.11334868724105132,
        0.3722729061729892,
        0.3361553431284828
      ],
      "development_MSE": 0.47631143499175627,
      "final_MSE": 0.2739256455141745,
      "model": "History attention"
    },
    {
      "MSE_by_horizon": [
        0.10972358769056392,
        0.3331106610308974,
        0.5513192718745477
      ],
      "development_MSE": 0.47308510797901987,
      "final_MSE": 0.3313845068653363,
      "model": "Patch attention"
    }
  ],
  "complexity": {
    "Causal TCN": {
      "best_step": 100,
      "minibatch_records": 128,
      "selected_rate": 0.01,
      "trainable_parameters": 2363,
      "update_limit": 300
    },
    "GRU": {
      "best_step": 240,
      "minibatch_records": 128,
      "selected_rate": 0.01,
      "trainable_parameters": 1079,
      "update_limit": 300
    },
    "History attention": {
      "best_step": 80,
      "minibatch_records": 128,
      "selected_rate": 0.01,
      "trainable_parameters": 1799,
      "update_limit": 300
    },
    "Lag boosting": {
      "heads": 3,
      "rounds_per_head": 100,
      "selected_max_leaf_nodes": 15
    },
    "Patch attention": {
      "best_step": 210,
      "minibatch_records": 128,
      "selected_rate": 0.003,
      "trainable_parameters": 2195,
      "update_limit": 300
    }
  },
  "context_hours": 48,
  "history_channels": [
    "demand",
    "observed weather",
    "occupancy"
  ],
  "horizons": [
    1,
    6,
    24
  ],
  "known_future_channels": [
    "hour sine",
    "hour cosine",
    "preannounced occupancy",
    "issued heating-weather feature"
  ],
  "patch_length": 12,
  "patch_tokens": 4,
  "split_context_records": [
    808,
    200,
    200
  ],
  "split_origin_counts": [
    101,
    25,
    25
  ]
}
```

### code_124

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "statsmodels": "0.15.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2724.

```json
{
  "alarm_assessment": [
    {
      "completed_rescaled_gap_count": 311,
      "final_any_event_Brier": 0.22745929481914687,
      "final_process_NLL_per_day": 0.7962200588278789,
      "model": "Constant rate",
      "rescaled_gap_Exp1_KS_statistic": 0.05797668109230572,
      "rescaled_gap_mean": 1.0077815085540553,
      "sum_right_censored_tail_hazard": 18.020079262557527
    },
    {
      "completed_rescaled_gap_count": 311,
      "final_any_event_Brier": 0.1935614512073748,
      "final_process_NLL_per_day": 0.738275417259188,
      "model": "Covariate intensity",
      "rescaled_gap_Exp1_KS_statistic": 0.029981476786988814,
      "rescaled_gap_mean": 1.0281562395154265,
      "sum_right_censored_tail_hazard": 20.34823096065751
    }
  ],
  "candidates": [
    {
      "alpha": 0.0,
      "development_process_NLL_per_day": 0.795190263021122,
      "iterations": 8
    },
    {
      "alpha": 0.1,
      "development_process_NLL_per_day": 0.7944373356385018,
      "iterations": 8
    }
  ],
  "complete_recording_assumed": true,
  "constant_training_events_per_day": 0.4613255075276875,
  "final_event_count": 311,
  "final_exposure_days": 718.451772153476,
  "intensity_coefficients": [
    0.387619312087285,
    0.1531961472991194
  ],
  "intensity_intercept": -0.8527134275080859,
  "intervals_per_building": 40,
  "irregular_signal": {
    "causal_hold_reference_MSE": 0.17296955550083445,
    "future_perturbation_hold_change": 0.0,
    "future_perturbation_offline_interpolation_change": 5.0,
    "offline_interpolation_reference_MSE": 0.010934604264776356,
    "query_time": 5.218463098358823,
    "sample_count": 101
  },
  "right_censored_end_included_in_likelihood": true,
  "selected_alpha": 0.1,
  "signal_sampling": {
    "aliased_30Hz_to": 5.0,
    "filtered_5Hz_amplitude": 0.00013395888164612903,
    "filtered_8Hz_amplitude": 1.0013462174027101,
    "naive_5Hz_amplitude": 0.7000000000000043,
    "original_Hz": 100.0,
    "original_components_Hz": [
      8,
      30
    ],
    "reduced_Hz": 25.0,
    "trimmed_boundary_seconds": 2.0
  },
  "split_buildings": [
    40,
    10,
    10
  ]
}
```

### code_125

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "statsmodels": "0.15.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2725.

```json
{
  "candidates": [
    {
      "development_source_MSE": 0.0016715791598142194,
      "distance_length_scale": 0.12,
      "family": "Spatial GP"
    },
    {
      "development_source_MSE": 0.0019860474684559354,
      "distance_length_scale": 0.25,
      "family": "Spatial GP"
    },
    {
      "best_step": 400,
      "development_source_MSE": 0.002968043868641578,
      "family": "Shared temporal",
      "rate": 0.003
    },
    {
      "best_step": 400,
      "development_source_MSE": 0.001148556576446204,
      "family": "Shared temporal",
      "rate": 0.01
    },
    {
      "best_step": 400,
      "development_source_MSE": 0.0028402315341162646,
      "family": "Graph temporal",
      "rate": 0.003
    },
    {
      "best_step": 390,
      "development_source_MSE": 0.0021721412773248938,
      "family": "Graph temporal",
      "rate": 0.01
    }
  ],
  "comparisons": [
    {
      "MSE_by_horizon": [
        0.0015276548187621321,
        0.001079501355078758,
        0.0012934863740949498
      ],
      "final_MSE": 0.0013002141826452798,
      "location_count": 12,
      "model": "Spatial GP",
      "origin_count": 23,
      "region": "Source locations"
    },
    {
      "MSE_by_horizon": [
        0.023052279414590603,
        0.024286189601856488,
        0.030114460112726154
      ],
      "final_MSE": 0.02581764304305775,
      "location_count": 8,
      "model": "Spatial GP",
      "origin_count": 23,
      "region": "Held region"
    },
    {
      "MSE_by_horizon": [
        0.0003900803406171053,
        0.0010427556739425713,
        0.002563997447269309
      ],
      "final_MSE": 0.0013322778206096618,
      "location_count": 12,
      "model": "Shared temporal",
      "origin_count": 23,
      "region": "Source locations"
    },
    {
      "MSE_by_horizon": [
        0.062064337461231425,
        0.041082545667674955,
        0.06991075347024175
      ],
      "final_MSE": 0.05768587886638271,
      "location_count": 8,
      "model": "Shared temporal",
      "origin_count": 23,
      "region": "Held region"
    },
    {
      "MSE_by_horizon": [
        0.001071961563414453,
        0.002510517323642494,
        0.0037078325473223713
      ],
      "final_MSE": 0.0024301038114597725,
      "location_count": 12,
      "model": "Graph temporal",
      "origin_count": 23,
      "region": "Source locations"
    },
    {
      "MSE_by_horizon": [
        0.036253596670628364,
        0.048056339526190366,
        0.2653817471483363
      ],
      "final_MSE": 0.116563894448385,
      "location_count": 8,
      "model": "Graph temporal",
      "origin_count": 23,
      "region": "Held region"
    }
  ],
  "complexity": {
    "Graph temporal": {
      "best_step": 390,
      "parameters": 1483,
      "selected_rate": 0.01,
      "update_limit": 400
    },
    "Shared temporal": {
      "best_step": 400,
      "parameters": 1051,
      "selected_rate": 0.01,
      "update_limit": 400
    },
    "Spatial GP": {
      "fixed_noise_variance_normalized": 0.005,
      "selected_distance_length_scale": 0.12,
      "source_training_rows": 1656
    }
  },
  "context_steps": 8,
  "forecast_target": "generated moving-load sensor response, not a field-validated PDE solver",
  "held_location_indices": [
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19
  ],
  "horizons": [
    1,
    4,
    12
  ],
  "known_geometry_locations": 20,
  "origin_counts": [
    46,
    13,
    23
  ],
  "region_coordinates_and_topology_known": true,
  "region_measurements_used_as_inputs": false,
  "region_measurements_used_for_fitting": false,
  "source_location_indices": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11
  ],
  "training_input_observation_fraction_on_source": 0.808197463768116,
  "unavailable_region_perturbation_changes_inputs": false
}
```

### code_126

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "statsmodels": "0.15.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2726.

```json
{
  "base_point_coherence_max_error": 2.8110461105395927,
  "calibration_frozen_before_final": true,
  "calibration_origin_counts_by_regime": {
    "0": 15,
    "1": 15
  },
  "draws_per_origin": 400,
  "final_begins_at_hour": 2160,
  "hierarchy": {
    "all_series": 13,
    "bottom_members": 9,
    "buildings": 3,
    "summing_matrix_shape": [
      13,
      9
    ]
  },
  "horizons": [
    1,
    6,
    24
  ],
  "interval_assessment": [
    {
      "case_count": 8,
      "coverage80": 0.875,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.2374639729553135,
      "mean_width": 3.574001869436044,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.875,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.24352936841869655,
      "mean_width": 3.418656630658946,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.75,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.24917002215134146,
      "mean_width": 2.899068915583623,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.37484728395063255,
      "mean_width": 7.678174884196084,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.3631958673577144,
      "mean_width": 7.763011973328615,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.75,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.23008670206211215,
      "mean_width": 2.183980218073671,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 1.0,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.36487096674695246,
      "mean_width": 4.741946436907288,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 1.0,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.3540880189651759,
      "mean_width": 4.881106334023059,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.75,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.3198499804743846,
      "mean_width": 2.2308277381811354,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 24,
      "coverage80": 0.9166666666666666,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.18464376824473247,
      "mean_width": 2.6819955341113846,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.9166666666666666,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.18855468733045383,
      "mean_width": 2.6554948274681016,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.875,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.1396390142507848,
      "mean_width": 1.571764430724792,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.19107594833142247,
      "mean_width": 3.8827010376207665,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.1877748630159546,
      "mean_width": 3.865824378473737,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.7916666666666666,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.1143889229193549,
      "mean_width": 1.2514533220765032,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.9583333333333334,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.16472010414281696,
      "mean_width": 2.4392268476279058,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.9583333333333334,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.16440200006331224,
      "mean_width": 2.4009532136724276,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.75,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.15435677956513708,
      "mean_width": 1.3273968469404156,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 72,
      "coverage80": 0.9166666666666666,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.07629752283236749,
      "mean_width": 1.1260574827810679,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.9305555555555556,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.07594480487112186,
      "mean_width": 1.130312933249378,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.8472222222222222,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.06131626709396731,
      "mean_width": 0.6539715568356079,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.9861111111111112,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.07714309057128556,
      "mean_width": 1.553237401175536,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.9861111111111112,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.0768280835843447,
      "mean_width": 1.5512596893585928,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.7916666666666666,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.05041488141297932,
      "mean_width": 0.49682364813729485,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.9583333333333334,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.07845251288652487,
      "mean_width": 1.2920715356926977,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.9583333333333334,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.07786527249041729,
      "mean_width": 1.2879153645222166,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.7083333333333334,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.0663292132715977,
      "mean_width": 0.5771391748341719,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 8,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 7,
      "coverage80": 0.42857142857142855,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.8847324772117714,
      "mean_width": 3.556115436774643,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.42857142857142855,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.8975145682247556,
      "mean_width": 3.399056153828923,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.7142857142857143,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.7192884119162747,
      "mean_width": 5.893791551442392,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.8571428571428571,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.6257222333140363,
      "mean_width": 7.713010738643691,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.8571428571428571,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.6202573508015051,
      "mean_width": 7.764612826206161,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.7106748167365217,
      "mean_width": 12.033337940169375,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.5714285714285714,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.8137185722891961,
      "mean_width": 4.44697933354984,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.7142857142857143,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.7982222285732581,
      "mean_width": 4.547859923061155,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.7142857142857143,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.7051183193223615,
      "mean_width": 6.777966987847934,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 1
    },
    {
      "case_count": 21,
      "coverage80": 0.47619047619047616,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.5057941600185428,
      "mean_width": 2.678020136843063,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.47619047619047616,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.5011051327298447,
      "mean_width": 2.64527555294315,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.5238095238095238,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.5164832017369438,
      "mean_width": 3.5202470100306016,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.8095238095238095,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.4073848584758735,
      "mean_width": 3.8927641814216623,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.8095238095238095,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.4065220329564473,
      "mean_width": 3.8842382990950646,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.8571428571428571,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.4374908755795015,
      "mean_width": 5.420655633754532,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.6190476190476191,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.4756190330330748,
      "mean_width": 2.509758582856268,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.6190476190476191,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.4730934106373836,
      "mean_width": 2.4728746751382555,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.8095238095238095,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.435282438589292,
      "mean_width": 4.221913663029414,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 3
    },
    {
      "case_count": 63,
      "coverage80": 0.5555555555555556,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.20416996583369684,
      "mean_width": 1.1221529458714583,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.5555555555555556,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.20486688834356998,
      "mean_width": 1.1264762270304158,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.6825396825396826,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.2110716465867069,
      "mean_width": 1.5605800718473286,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.6984126984126984,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.1814670789274189,
      "mean_width": 1.550438131833257,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.6984126984126984,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.18158278999865876,
      "mean_width": 1.5488164267803728,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.8571428571428571,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.17914430241127835,
      "mean_width": 2.170410506361962,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.6031746031746031,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.19211816653770403,
      "mean_width": 1.2814596704854715,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.6031746031746031,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.19293476342293533,
      "mean_width": 1.278090480189232,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.746031746031746,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.1884618358241268,
      "mean_width": 1.7378957731958227,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 7,
      "period": "Before shift",
      "series_count": 9
    },
    {
      "case_count": 7,
      "coverage80": 0.8571428571428571,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.36376557705923473,
      "mean_width": 3.5768975738034805,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.8571428571428571,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.2878584923246378,
      "mean_width": 3.5059490236416133,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.8571428571428571,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.2836122934587374,
      "mean_width": 2.911191769364117,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.8571428571428571,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.5784685994887626,
      "mean_width": 7.767405074370605,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.4399546679332766,
      "mean_width": 7.802287047233217,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.42857142857142855,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.3985684901754543,
      "mean_width": 2.1886097631464634,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.42857142857142855,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.9044639736723299,
      "mean_width": 4.179927020637824,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.5714285714285714,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.7604795742044895,
      "mean_width": 4.3117746022524885,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 7,
      "coverage80": 0.42857142857142855,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 0.8108741273476757,
      "mean_width": 2.258785461289073,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 21,
      "coverage80": 0.7619047619047619,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.30616694433452146,
      "mean_width": 2.729480608169917,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.8571428571428571,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.2159749561929431,
      "mean_width": 2.7068894625412074,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.6666666666666666,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.20424419149048986,
      "mean_width": 1.5870613533477966,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.24832061392166,
      "mean_width": 3.967759851087586,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.2397808351478936,
      "mean_width": 3.942967672975127,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.47619047619047616,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.1950428363950278,
      "mean_width": 1.2507681628054026,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.7619047619047619,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.3528964804555586,
      "mean_width": 2.237940534942238,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.8095238095238095,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.3365347530861788,
      "mean_width": 2.18627024830982,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 21,
      "coverage80": 0.47619047619047616,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 0.33781460574740096,
      "mean_width": 1.3475749841860736,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 63,
      "coverage80": 0.873015873015873,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.09451451094277842,
      "mean_width": 1.1303032578405583,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.8571428571428571,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.0970900897990234,
      "mean_width": 1.137805175287683,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.6349206349206349,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.09117737679879494,
      "mean_width": 0.6628914800498183,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.08795356632410216,
      "mean_width": 1.5841687532339148,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 1.0,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.09045410287573781,
      "mean_width": 1.5838385095375085,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.6349206349206349,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.07291233352335846,
      "mean_width": 0.5007354724462698,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.7936507936507936,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.13430231896350273,
      "mean_width": 1.2858963291065708,
      "method": "Base pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.7777777777777778,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.139898665346643,
      "mean_width": 1.2850818985080863,
      "method": "Reconciled pooled",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 63,
      "coverage80": 0.5238095238095238,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.14079112063562665,
      "mean_width": 0.5807318102518263,
      "method": "Reconciled regime",
      "operating_regime": 0,
      "origin_count": 7,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 8,
      "coverage80": 0.25,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 2.152568692866185,
      "mean_width": 3.5738366887902124,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.25,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 2.146418477232782,
      "mean_width": 3.400102468603034,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.375,
      "horizon": 1,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 1.8385269149852466,
      "mean_width": 5.9318485469644955,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.125,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 3.76985337897298,
      "mean_width": 7.381948953688802,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.125,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 3.737895405124901,
      "mean_width": 7.477967158008141,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.375,
      "horizon": 6,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 3.3592830427592033,
      "mean_width": 12.428570396253827,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.125,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 3.7808503678709022,
      "mean_width": 4.659300709886912,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.125,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 3.806992743107044,
      "mean_width": 4.83084225379822,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 8,
      "coverage80": 0.125,
      "horizon": 24,
      "level": "Grand total",
      "mean_pinball_three_quantiles": 3.512507280249435,
      "mean_width": 6.7779669878479485,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 1
    },
    {
      "case_count": 24,
      "coverage80": 0.125,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 2.048899731921317,
      "mean_width": 2.7949361252956613,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.125,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 2.0561534597558633,
      "mean_width": 2.757476032772317,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.125,
      "horizon": 1,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 2.0890362019782813,
      "mean_width": 3.5435804203853785,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.375,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 1.9526698789044343,
      "mean_width": 3.8227854399164785,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.375,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 1.9533416951637521,
      "mean_width": 3.8207272973058353,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.4583333333333333,
      "horizon": 6,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 1.7831400990571653,
      "mean_width": 5.4269837341545015,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.20833333333333334,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 1.745214052059171,
      "mean_width": 2.408373040718599,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.25,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 1.7631053723327408,
      "mean_width": 2.355066431887033,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 24,
      "coverage80": 0.2916666666666667,
      "horizon": 24,
      "level": "Buildings",
      "mean_pinball_three_quantiles": 1.6330899358348658,
      "mean_width": 4.1959244964430225,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 3
    },
    {
      "case_count": 72,
      "coverage80": 0.19444444444444445,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.704192636992625,
      "mean_width": 1.1028545823219533,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.19444444444444445,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.7024060838725135,
      "mean_width": 1.1123583886880246,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.2916666666666667,
      "horizon": 1,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.7043534915064511,
      "mean_width": 1.5776005056269433,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.3194444444444444,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.6935272573937119,
      "mean_width": 1.5455377358575701,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.3055555555555556,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.6940167361390968,
      "mean_width": 1.5430676654357844,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.4444444444444444,
      "horizon": 6,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.6533734404101028,
      "mean_width": 2.174251859842337,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.2638888888888889,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.6333513580913712,
      "mean_width": 1.3152965788726974,
      "method": "Base pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.2777777777777778,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.6323281518525626,
      "mean_width": 1.3134319852061265,
      "method": "Reconciled pooled",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 9
    },
    {
      "case_count": 72,
      "coverage80": 0.3472222222222222,
      "horizon": 24,
      "level": "Members",
      "mean_pinball_three_quantiles": 0.5965227304159973,
      "mean_width": 1.7232227110785543,
      "method": "Reconciled regime",
      "operating_regime": 1,
      "origin_count": 8,
      "period": "After shift",
      "series_count": 9
    }
  ],
  "minimum_reconciled_scenario_value": 6.1529859354221035,
  "origin_counts": {
    "calibration": 30,
    "final": 30,
    "source": 58
  },
  "point_assessment": [
    {
      "MSE": 4.2000449483264095,
      "horizon": 1,
      "level": "Grand total",
      "method": "Base",
      "period": "Before shift"
    },
    {
      "MSE": 4.186793265428639,
      "horizon": 1,
      "level": "Grand total",
      "method": "Reconciled",
      "period": "Before shift"
    },
    {
      "MSE": 3.049737776871231,
      "horizon": 6,
      "level": "Grand total",
      "method": "Base",
      "period": "Before shift"
    },
    {
      "MSE": 2.94728395183231,
      "horizon": 6,
      "level": "Grand total",
      "method": "Reconciled",
      "period": "Before shift"
    },
    {
      "MSE": 4.556366581187905,
      "horizon": 24,
      "level": "Grand total",
      "method": "Base",
      "period": "Before shift"
    },
    {
      "MSE": 4.272964492143784,
      "horizon": 24,
      "level": "Grand total",
      "method": "Reconciled",
      "period": "Before shift"
    },
    {
      "MSE": 1.7217757986768554,
      "horizon": 1,
      "level": "Buildings",
      "method": "Base",
      "period": "Before shift"
    },
    {
      "MSE": 1.6988163056978263,
      "horizon": 1,
      "level": "Buildings",
      "method": "Reconciled",
      "period": "Before shift"
    },
    {
      "MSE": 1.3027655364928918,
      "horizon": 6,
      "level": "Buildings",
      "method": "Base",
      "period": "Before shift"
    },
    {
      "MSE": 1.289656846899792,
      "horizon": 6,
      "level": "Buildings",
      "method": "Reconciled",
      "period": "Before shift"
    },
    {
      "MSE": 1.5407362402584068,
      "horizon": 24,
      "level": "Buildings",
      "method": "Base",
      "period": "Before shift"
    },
    {
      "MSE": 1.5367520842505034,
      "horizon": 24,
      "level": "Buildings",
      "method": "Reconciled",
      "period": "Before shift"
    },
    {
      "MSE": 0.2821948410618151,
      "horizon": 1,
      "level": "Members",
      "method": "Base",
      "period": "Before shift"
    },
    {
      "MSE": 0.2829887875447589,
      "horizon": 1,
      "level": "Members",
      "method": "Reconciled",
      "period": "Before shift"
    },
    {
      "MSE": 0.2535544065782017,
      "horizon": 6,
      "level": "Members",
      "method": "Base",
      "period": "Before shift"
    },
    {
      "MSE": 0.2537879843203527,
      "horizon": 6,
      "level": "Members",
      "method": "Reconciled",
      "period": "Before shift"
    },
    {
      "MSE": 0.2902236340959085,
      "horizon": 24,
      "level": "Members",
      "method": "Base",
      "period": "Before shift"
    },
    {
      "MSE": 0.29184684853129517,
      "horizon": 24,
      "level": "Members",
      "method": "Reconciled",
      "period": "Before shift"
    },
    {
      "MSE": 22.707899774859925,
      "horizon": 1,
      "level": "Grand total",
      "method": "Base",
      "period": "After shift"
    },
    {
      "MSE": 22.27877558587146,
      "horizon": 1,
      "level": "Grand total",
      "method": "Reconciled",
      "period": "After shift"
    },
    {
      "MSE": 62.543613098576365,
      "horizon": 6,
      "level": "Grand total",
      "method": "Base",
      "period": "After shift"
    },
    {
      "MSE": 60.4425647534604,
      "horizon": 6,
      "level": "Grand total",
      "method": "Reconciled",
      "period": "After shift"
    },
    {
      "MSE": 52.670672243011985,
      "horizon": 24,
      "level": "Grand total",
      "method": "Base",
      "period": "After shift"
    },
    {
      "MSE": 52.631930125761954,
      "horizon": 24,
      "level": "Grand total",
      "method": "Reconciled",
      "period": "After shift"
    },
    {
      "MSE": 16.696768885664827,
      "horizon": 1,
      "level": "Buildings",
      "method": "Base",
      "period": "After shift"
    },
    {
      "MSE": 16.3587850483914,
      "horizon": 1,
      "level": "Buildings",
      "method": "Reconciled",
      "period": "After shift"
    },
    {
      "MSE": 20.15213628106985,
      "horizon": 6,
      "level": "Buildings",
      "method": "Base",
      "period": "After shift"
    },
    {
      "MSE": 20.15455094806832,
      "horizon": 6,
      "level": "Buildings",
      "method": "Reconciled",
      "period": "After shift"
    },
    {
      "MSE": 16.53979784407463,
      "horizon": 24,
      "level": "Buildings",
      "method": "Base",
      "period": "After shift"
    },
    {
      "MSE": 16.366417502178805,
      "horizon": 24,
      "level": "Buildings",
      "method": "Reconciled",
      "period": "After shift"
    },
    {
      "MSE": 2.1707377114231194,
      "horizon": 1,
      "level": "Members",
      "method": "Base",
      "period": "After shift"
    },
    {
      "MSE": 2.173031053033854,
      "horizon": 1,
      "level": "Members",
      "method": "Reconciled",
      "period": "After shift"
    },
    {
      "MSE": 2.769856939493247,
      "horizon": 6,
      "level": "Members",
      "method": "Base",
      "period": "After shift"
    },
    {
      "MSE": 2.7739677129487577,
      "horizon": 6,
      "level": "Members",
      "method": "Reconciled",
      "period": "After shift"
    },
    {
      "MSE": 2.272036542065301,
      "horizon": 24,
      "level": "Members",
      "method": "Base",
      "period": "After shift"
    },
    {
      "MSE": 2.279447310956829,
      "horizon": 24,
      "level": "Members",
      "method": "Reconciled",
      "period": "After shift"
    }
  ],
  "reconciled_marginal_quantile_coherence_max_error": 3.1139668735422674,
  "reconciled_point_coherence_max_error": 2.842170943040401e-14,
  "scenario_coherence_max_errors": {
    "Base pooled": 3.2128812024722286,
    "Reconciled pooled": 5.684341886080802e-14,
    "Reconciled regime": 5.684341886080802e-14
  },
  "shift_begins_at_hour": 2520,
  "source_only_model_fit": true,
  "weight_covariance_minimum_eigenvalues": [
    0.11905562851734766,
    0.18632342129161888,
    0.17166731580887992
  ]
}
```


## Publication verification

At content verification, commit `456f2f7e047cc9854ec23690f8e882c22e8f7da6` matched remote main and all 206 file blobs with a clean working tree. Final metadata and all six notebooks are separately verified through commit-addressed raw files in the local delivery evidence. Only companion artifacts are published.
