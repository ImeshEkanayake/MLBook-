# Chapter 24: Time-series and spatiotemporal learning — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_24_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 24.1 · Forecasting tasks, horizons and baselines

- [Every forecast names an origin and information cutoff](notebooks/121_Chapter_24_01_forecast_origins_and_demand_baselines.ipynb#forecast-origin-contract)
- [Direct heads and recursive lags use different fitted rules](notebooks/121_Chapter_24_01_forecast_origins_and_demand_baselines.ipynb#forecast-information-limits)

Declared mechanisms: actual temporal forecast contract, persistence and seasonal references, local versus shared direct Ridge, recursive forecast with predicted lags, weather-prefix and future-target access audits.

```bash
python scripts/run_notebook.py notebooks/121_Chapter_24_01_forecast_origins_and_demand_baselines.ipynb
```

## 24.2 · Classical forecasting and latent dynamics

- [Classical families encode different temporal assumptions](notebooks/122_Chapter_24_02_classical_forecasts_and_filtered_dynamics.ipynb#classical-forecast-contract)
- [State updates are not parameter refits, and smoothing is not online filtering](notebooks/122_Chapter_24_02_classical_forecasts_and_filtered_dynamics.ipynb#classical-model-limits)

Declared mechanisms: native seasonal exponential smoothing, native ARIMA and dynamic regression, lag regression and vector autoregression, native structural state-space filtering, future-sensitive smoothing audit.

```bash
python scripts/run_notebook.py notebooks/122_Chapter_24_02_classical_forecasts_and_filtered_dynamics.ipynb
```

## 24.3 · Machine learning and neural forecasting

- [Share origins and information before comparing model families](notebooks/123_Chapter_24_03_lag_boosting_and_neural_multi_horizon_forecasts.ipynb#neural-forecast-contract)
- [A history encoder does not observe the forecast targets](notebooks/123_Chapter_24_03_lag_boosting_and_neural_multi_horizon_forecasts.ipynb#neural-forecast-limits)

Declared mechanisms: native lag-feature histogram boosting, actual GRU causal TCN and attention forecasts, actual nonoverlapping patch tokens, common multi-horizon information budget, development checkpoint and horizon-specific errors.

```bash
python scripts/run_notebook.py notebooks/123_Chapter_24_03_lag_boosting_and_neural_multi_horizon_forecasts.ipynb
```

## 24.4 · Irregular signals and event sequences

- [A sampled waveform and event arrivals have different targets](notebooks/124_Chapter_24_04_sampling_irregular_observations_and_alarm_intensity.ipynb#observation-process-contract)
- [Availability and event exposure determine the likelihood](notebooks/124_Chapter_24_04_sampling_irregular_observations_and_alarm_intensity.ipynb#signal-event-limits)

Declared mechanisms: actual polyphase anti-alias filtering, offline interpolation versus causal previous hold, exposure-weighted Poisson intensity fit, actual event-time likelihood with censored tail, time-rescaled event-gap diagnostics.

```bash
python scripts/run_notebook.py notebooks/124_Chapter_24_04_sampling_irregular_observations_and_alarm_intensity.ipynb
```

## 24.5 · Spatial and spatiotemporal dependencies

- [A known mesh does not make its missing regional measurements available](notebooks/125_Chapter_24_05_shared_temporal_models_and_held_region.ipynb#spatiotemporal-contract)
- [Known structure, measured support and shared parameters are different resources](notebooks/125_Chapter_24_05_shared_temporal_models_and_held_region.ipynb#regional-forecast-limits)

Declared mechanisms: native spatial Gaussian-process reference, actual shared GRU and graph-GRU forecasts, known geometry versus unavailable regional measurements, common forecast origins and planned moving loads, source and regional horizon assessment.

```bash
python scripts/run_notebook.py notebooks/125_Chapter_24_05_shared_temporal_models_and_held_region.ipynb
```

## 24.6 · Probabilistic, hierarchical and regime-aware forecasts

- [Coherent forecast draws do not make marginal quantiles additive](notebooks/126_Chapter_24_06_coherent_trajectories_quantiles_and_regimes.ipynb#hierarchical-probabilistic-contract)
- [Projection is a coherence calculation, not a coverage guarantee](notebooks/126_Chapter_24_06_coherent_trajectories_quantiles_and_regimes.ipynb#forecast-uncertainty-limits)

Declared mechanisms: actual all-level forecast reconciliation, calibration-only shrinkage covariance, whole-origin multi-horizon residual scenarios, coherent draws versus nonadditive marginal quantiles, coverage pinball width by regime horizon and level.

```bash
python scripts/run_notebook.py notebooks/126_Chapter_24_06_coherent_trajectories_quantiles_and_regimes.ipynb
```

## Interpretation and boundaries

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
