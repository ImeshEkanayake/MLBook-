# Chapter 3: probability, statistics and uncertainty traceability

Five independent laboratories accompany the five agreed manuscript sections. Each includes an orientation, declared population/model, prediction prompts, controlled calculations, actual diagnostics, exercises, separate hints and official references. Use permanent IDs in [CODE_EXAMPLES.md](CODE_EXAMPLES.md), [execution evidence](CHAPTER_03_EXECUTION.md) and the unchanged [pinned environment](requirements-lock.txt).

| Manuscript mechanism | Notebook section | Executable evidence or worksheet |
| --- | --- | --- |
| Discrete random variables, joint/marginal distributions and event definitions | [code_012: joint table](notebooks/012_Chapter_03_01_Random_Variables_And_Conditional_Distributions.ipynb#joint-table) | Four material/load strata expanded into eight joint masses; exact count and normalization checks. |
| Conditional probabilities, denominators and reversed conditions | [code_012: conditionals](notebooks/012_Chapter_03_01_Random_Variables_And_Conditional_Distributions.ipynb#conditionals) | 52/200 versus 52/96; total probability and nonfactorizing joint probability; numerator/denominator plot. |
| Mixtures, expectation, variance, independence and causal boundary | [code_012: mixtures](notebooks/012_Chapter_03_01_Random_Variables_And_Conditional_Distributions.ipynb#mixtures) | Reweight load regimes, preserve stratum rates, Bernoulli mean/variance check; zero-correlation/nonindependence exercise and intervention worksheet. |
| Continuous distributions, density units and probability as area | [code_012: continuous](notebooks/012_Chapter_03_01_Random_Variables_And_Conditional_Distributions.ipynb#continuous) | Integrated normal density, CDF interval probability, unit invariance; mean/median loss interpretation. |
| Populations, observation/independent units and repeated sampling | [code_013: design](notebooks/013_Chapter_03_02_Sampling_And_Data_Generating_Processes.ipynb#design) | Equal 10,000-row designs with one versus 100 buildings, full hierarchical generator, derived and empirical variance. |
| Dependence, conditional independence, design effects and effective count limits | [code_013: design](notebooks/013_Chapter_03_02_Sampling_And_Data_Generating_Processes.ipynb#design) | Beta latent-rate variance/correlation identity and design-effect table; unequal-cluster/zero-correlation extensions. |
| Sampling distributions and interval procedure coverage | [code_013: intervals](notebooks/013_Chapter_03_02_Sampling_And_Data_Generating_Processes.ipynb#intervals) | 3000 independent population draws; known-model normal-interval coverage, distinguished from what one cohort can estimate. |
| Selection bias and supported population | [code_013: selection](notebooks/013_Chapter_03_02_Sampling_And_Data_Generating_Processes.ipynb#selection) | Declared selection mechanism, analytic enriched rate and observed fraction; inclusion/overlap limitations. |
| Measurement error, shared bias and information limits | [code_013: measurement](notebooks/013_Chapter_03_02_Sampling_And_Data_Generating_Processes.ipynb#measurement) | Fixed offset plus independent reading noise; checked population-scope worksheet, drift/time-dependence exercises. |
| Probability model versus estimator; likelihood, logs and MLE | [code_014: likelihood](notebooks/014_Chapter_03_03_Estimation_Likelihood_And_Bayesian_Updating.ipynb#likelihood) | Binomial log likelihood, analytic/log-gamma identity and grid maximum; zero-outcome boundary distinction. |
| Priors, conjugate posterior and sequential updating | [code_014: updating](notebooks/014_Chapter_03_03_Estimation_Likelihood_And_Bayesian_Updating.ipynb#updating) | Explicit two-batch beta updates equal pooled update; declared assumptions and prior/posterior plot. |
| Credible interval, posterior summaries and prior sensitivity | [code_014: credible](notebooks/014_Chapter_03_03_Estimation_Likelihood_And_Bayesian_Updating.ipynb#credible) | Equal-tailed CDF/quantile agreement; predeclared uniform/declared-prior table at two sample sizes. |
| Parameter versus future-outcome uncertainty | [code_014: predictive](notebooks/014_Chapter_03_03_Estimation_Likelihood_And_Bayesian_Updating.ipynb#predictive) | Beta-binomial versus plug-in binomial; mass normalization, predictive mean and variance formula. |
| Zero events, Wald failure and interval interpretation | [code_014: zero](notebooks/014_Chapter_03_03_Estimation_Likelihood_And_Bayesian_Updating.ipynb#zero) | Wilson and credible intervals with positive upper endpoints; coverage and imperfect-label extensions. |
| Evaluation contract, paired differences, averaging unit and effect size | [code_015: contract](notebooks/015_Chapter_03_04_Statistical_Comparisons_And_Resampling.ipynb#contract) | Fixed predictors, 40 independent assessment buildings, case pairing, equal-building statistic and predeclared .05 mm margin. |
| Group bootstrap, confidence intervals and percentile limitations | [code_015: bootstrap](notebooks/015_Chapter_03_04_Statistical_Comparisons_And_Resampling.ipynb#bootstrap) | Complete-building versus wrong row resampling, paired-index identity, expected SE comparison; no universal coverage claim. |
| Hypothesis tests, p-values and practical thresholds | [code_015: effect/test](notebooks/015_Chapter_03_04_Statistical_Comparisons_And_Resampling.ipynb#effect-test) | Declared symmetric-null sign-flip Monte Carlo test, effect/interval/margin report; skew-null challenge. |
| Multiple comparisons, selection and familywise control | [code_015: multiplicity](notebooks/015_Chapter_03_04_Statistical_Comparisons_And_Resampling.ipynb#multiplicity) | 2000 searches with 20 valid independent normal-null t tests; observed/theoretical familywise rates and Bonferroni comparison. |
| Outcome variation and parameter-mean uncertainty | [code_016: decomposition](notebooks/016_Chapter_03_05_Kinds_And_Sources_Of_Uncertainty.ipynb#decomposition) | Exact beta/Bernoulli law-of-total-variance identity; concentration extension. |
| Mean confidence versus individual prediction intervals | [code_016: mean/outcome](notebooks/016_Chapter_03_05_Kinds_And_Sources_Of_Uncertainty.ipynb#mean-outcome) | Known-sigma normal half-width curves, repeated coverage, deliberate mean-band misuse; estimated-sigma t extension. |
| Measurement noise, fixed offset and relative irreducibility | [code_016: noise/bias](notebooks/016_Chapter_03_05_Kinds_And_Sources_Of_Uncertainty.ipynb#noise-bias) | Averages tightly estimate the biased measured mean; calibration/domain-knowledge discussion. |
| Misspecification, distribution shift and information boundaries | [code_016: material shift](notebooks/016_Chapter_03_05_Kinds_And_Sources_Of_Uncertainty.ipynb#material-shift) | A-only compliance calibration, fixed A assessment, separate B conditional-response stress test and known-noise interval; no retuning on assessment outcomes. |
| Included/excluded sources and calibration scope | [code_016: ledger](notebooks/016_Chapter_03_05_Kinds_And_Sources_Of_Uncertainty.ipynb#ledger) | Validated five-row uncertainty ledger; coverage/width/group evaluation and new-B-calibration/fresh-assessment exercises. |

## Roles, assumptions and next work

Sampling design and inclusion rules define what population is observed. A likelihood describes observations conditional on parameters; priors and estimation procedures describe how evidence updates those parameters. A bootstrap resampling unit follows dependence and the estimand. Simulation budgets control numerical precision; practical margins are decision criteria. They are not interchangeable model hyperparameters.

Exact finite-population tables, analytic distribution identities and fully declared repeated-population simulations do not require a supervised split. Fixed-predictor error resampling describes assessment uncertainty conditional on those predictors, not retraining or model selection. The fitted compliance uses only A calibration labels; A/B assessment outcomes remain outside fitting and are not reused to choose a better model. Adapting the experiment requires fresh relevant assessment data.

Percentile bootstrap, symmetric sign flips, known-noise normal intervals and common-rate beta updates have stated assumptions and failure conditions. The experiments preserve genuine awkward outcomes rather than choose seeds to make a preferred result significant. No coverage guarantee under unseen materials, causal load effect or empirical structural reliability is inferred.

## Run

From the activated pinned environment at repository root:

```bash
python scripts/run_notebook.py notebooks/012_Chapter_03_01_Random_Variables_And_Conditional_Distributions.ipynb
python scripts/run_notebook.py notebooks/013_Chapter_03_02_Sampling_And_Data_Generating_Processes.ipynb
python scripts/run_notebook.py notebooks/014_Chapter_03_03_Estimation_Likelihood_And_Bayesian_Updating.ipynb
python scripts/run_notebook.py notebooks/015_Chapter_03_04_Statistical_Comparisons_And_Resampling.ipynb
python scripts/run_notebook.py notebooks/016_Chapter_03_05_Kinds_And_Sources_Of_Uncertainty.ipynb
python scripts/check_chapter03.py
```

By default the runner writes a separate executed copy to ignored `build/`. Using `--output` with a source path intentionally replaces that reference after successful execution. Restart and run all cells after code changes; stored outputs do not substitute for a clean-kernel check. All data generation and helpers remain inside each notebook.
