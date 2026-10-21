# Chapter 29: Temporal and scientific foundation models — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Examples150/153/154 generate all inputs internally. Examples151/152 require explicitly acquired, hash-verified public checkpoints before offline CPU inference; see the [asset guide](CHAPTER_29_ASSETS.md). Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_29_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 29.1 · Pretraining for time series

- [Train shared weights on whole source series](notebooks/150_Chapter_29_01_cross_series_pretraining_and_context.ipynb#cross-series-pretraining)
- [Keep the observation clock and information boundary](notebooks/150_Chapter_29_01_cross_series_pretraining_and_context.ipynb#context-and-token-contracts)

Declared mechanisms: actual shared forecasting pretraining across independent generated series, context-only normalization and patch representation, whole-series model selection and final assessment, frozen checkpoint versus local autoregression and seasonal controls, scale quantization and causal context interventions.

```bash
python scripts/run_notebook.py notebooks/150_Chapter_29_01_cross_series_pretraining_and_context.ipynb
```

## 29.2 · Representative forecasting model families

- [Execute named checkpoints on a common bounded task](notebooks/151_Chapter_29_02_native_forecasting_families_and_backtests.ipynb#native-forecasting-backtest)
- [Compare released contracts rather than family names](notebooks/151_Chapter_29_02_native_forecasting_families_and_backtests.ipynb#checkpoint-and-output-constraints)

Declared mechanisms: actual pinned TimesFM2.5 and ChronosBoltTiny CPU inference, explicit model/config byte hashes and offline loading, multiple origins kept within independent generated series, seasonal local autoregression and lagged-tree controls, native quantile shape coverage and immutable checkpoint parameters.

```bash
python scripts/run_notebook.py notebooks/151_Chapter_29_02_native_forecasting_families_and_backtests.ipynb
```

## 29.3 · Adaptation and evaluation across domains

- [Count target labels used by an actual adaptation route](notebooks/152_Chapter_29_03_forecast_adaptation_and_target_budgets.ipynb#adaptation-budget)
- [State the adaptation and confidence boundary](notebooks/152_Chapter_29_03_forecast_adaptation_and_target_budgets.ipynb#clock-and-selection-accounting)

Declared mechanisms: actual frozen ChronosBolt forecast across cadence regimes, causal historical imputation and input contracts, target-label residual adaptation with separate selection and assessment, independent-series uncertainty for label-budget comparisons, temporal overlap and future-covariate availability interventions.

```bash
python scripts/run_notebook.py notebooks/152_Chapter_29_03_forecast_adaptation_and_target_budgets.ipynb
```

## 29.4 · Scientific and physical foundation models

- [Pretrain an actual small solution operator](notebooks/153_Chapter_29_04_scientific_pretraining_and_operator_adaptation.ipynb#scientific-operator-reuse)
- [Keep the scientific family and units visible](notebooks/153_Chapter_29_04_scientific_pretraining_and_operator_adaptation.ipynb#scientific-support-map)

Declared mechanisms: actual original spectral solution-operator pretraining across equation parameters, analytic periodic advection diffusion reaction references, whole-case development and downstream parameter updates, warm-start versus scratch operators with equal downstream budgets, physical support and semigroup consistency checks without named-model substitution.

```bash
python scripts/run_notebook.py notebooks/153_Chapter_29_04_scientific_pretraining_and_operator_adaptation.ipynb
```

## 29.5 · Validity, scale and responsible reuse

- [Reuse a learned operator only with physical checks](notebooks/154_Chapter_29_05_physical_validity_mesh_and_boundary_tests.ipynb#mesh-and-physics-validity)
- [Conservation must match the boundary problem](notebooks/154_Chapter_29_05_physical_validity_mesh_and_boundary_tests.ipynb#physical-acceptance-tests)

Declared mechanisms: actual shared learned diffusion stencil with disclosed observation bias, new-mesh physical scaling and deliberate wrong-grid fixture, independent converged sparse numerical references and analytic checks, periodic conservation projection versus invalid Dirichlet mass constraint, boundary values rollout stability and field errors checked separately.

```bash
python scripts/run_notebook.py notebooks/154_Chapter_29_05_physical_validity_mesh_and_boundary_tests.ipynb
```

## Interpretation and boundaries

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
