# Chapter 16: Probabilistic and Bayesian models — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_16_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 16.1 · Naive Bayes and generative classification

- [A duplicated alarm is not independent evidence](notebooks/077_Chapter_16_01_Alarm_Dependence_And_Naive_Bayes.ipynb#posterior)
- [Normalize scores, then check their probability meaning](notebooks/077_Chapter_16_01_Alarm_Dependence_And_Naive_Bayes.ipynb#calibration)

Declared mechanisms: Bernoulli class prior and likelihood score, Laplace smoothing and absent indicators, duplicate conditional dependence, classification versus probability calibration.

```bash
python scripts/run_notebook.py notebooks/077_Chapter_16_01_Alarm_Dependence_And_Naive_Bayes.ipynb
```

## 16.2 · Bayesian estimation and hierarchical models

- [Share information through explicit hyperparameters](notebooks/078_Chapter_16_02_Hierarchical_Building_Rates.ipynb#hierarchy)
- [Prediction integrates rate uncertainty and future sampling](notebooks/078_Chapter_16_02_Hierarchical_Building_Rates.ipynb#prediction)

Declared mechanisms: prior likelihood posterior and prediction, full hyperparameter grid integration, unequal group partial pooling, prior predictive versus future evidence.

```bash
python scripts/run_notebook.py notebooks/078_Chapter_16_02_Hierarchical_Building_Rates.ipynb
```

## 16.3 · Posterior computation and model checking

- [Compare computations for one declared posterior](notebooks/079_Chapter_16_03_Grid_MCMC_Variational_And_Checks.ipynb#computation)
- [Sampling diagnostics and model criticism ask different questions](notebooks/079_Chapter_16_03_Grid_MCMC_Variational_And_Checks.ipynb#criticism)

Declared mechanisms: conjugate conditional and joint grid reference, transformed random-walk MCMC with Jacobian, classical split Rhat and simple ESS, mean-field grid approximation and predictive criticism.

```bash
python scripts/run_notebook.py notebooks/079_Chapter_16_03_Grid_MCMC_Variational_And_Checks.ipynb
```

## 16.4 · Gaussian processes and scalable approximations

- [A fixed covariance defines what spatial interpolation assumes](notebooks/080_Chapter_16_04_Temperature_GP_And_Low_Rank_Prior.ipynb#conditioning)
- [A naive low-rank prior can erase uncertainty away from its basis](notebooks/080_Chapter_16_04_Temperature_GP_And_Low_Rank_Prior.ipynb#approximation)

Declared mechanisms: fixed covariance and Gaussian conditioning, latent versus observation intervals, away-from-support conditional uncertainty, low-rank prior approximation and variance loss.

```bash
python scripts/run_notebook.py notebooks/080_Chapter_16_04_Temperature_GP_And_Low_Rank_Prior.ipynb
```

## 16.5 · Graphical models and latent states

- [Known probabilistic states are inferred from noisy measurements](notebooks/081_Chapter_16_05_Regime_HMM_And_Probability_Graphs.ipynb#states)
- [A probability graph factorizes a distribution](notebooks/081_Chapter_16_05_Regime_HMM_And_Probability_Graphs.ipynb#graphs)

Declared mechanisms: directed probability factorization and latent regimes, forward filtering versus offline smoothing and Viterbi, exact enumeration and undirected conditional independence, continuous Gaussian state-space filtering.

```bash
python scripts/run_notebook.py notebooks/081_Chapter_16_05_Regime_HMM_And_Probability_Graphs.ipynb
```

## Interpretation and boundaries

Five self-contained CPU laboratories use seeds 1677–1681 and the unchanged Python 3.14.3 / NumPy 2.4.4 / SciPy 1.17.1 / pandas 3.0.3 / Matplotlib 3.11.0 / scikit-learn 1.9.0 environment. Initial kernels all passed without error outputs or solver warnings. Notebooks 078/079 reran after adding a 121-point-per-axis quadrature refinement and clarifying prior-predictive wording. Notebooks 077/081 reran for distinct calibration markers and observation labels matching the book; their numerical result dictionaries remain exactly unchanged. Notebook079 also reran to enlarge the joint-contour region with explicit zoom axes; result dictionaries remain exactly identical to the registered evidence. No dependency was added and ordinary execution is offline. Declared inspection/failure counts in 078/079 are teaching fixtures, not random field samples; other numerical observations are generated under explicit models.

Bernoulli class models train on 600 and assess 3000 independent records, with generated class 1 prior .2. AlarmA probabilities are .15/.8 by class, and independent conditional alarmB .25/.6. An extra exact copy ofA violates the naive conditional likelihood factorization. Fixed alpha 1 Bernoulli fits use empirical training class priors, present and absent indicators, with manual log-sum-exp probability agreement. Deduplicated final Brier/log loss/accuracy is .092829/.309573/.875667, compared with duplicated .121427/.405040/.844333. Pattern A 1 B 0 has known posterior .415584, fitted deduplicated .446721, duplicated .802816 and final observed frequency .395089 among 448 records. Four-pattern calibration counts remain visible. Smoothing gives finite unseen-indicator probabilities but cannot repair dependence; no final tuning occurs.

The hierarchy has n=[4,8,12,20,40,80,160,320], s=[0,1,3,1,5,9,10,30]. Group rates have Beta(m*k,(1-m)*k) distributions, with truncated hyperpriors m~Beta(2,8) on[.01,.6] and log(k)~Normal(log 20,.8) on[0,log 100]. Full hyperparameter uncertainty is integrated on a 61×61 trapezoid grid, not a plug-in empirical-Bayes fit. A 121×121 refinement changes group posterior means by at most 3.96269e-6. Complete-pooling rate is .0916149, population posterior mean .1144995 and mean concentration 39.3629. Smallest-group raw 0 becomes .1001315; largest raw .09375 becomes .0955137. Five thousand mixture draws supply marginal credible intervals. Prior-predictive mean total failures is 129.1824 versus declared observed 59, with .233 of prior replications having some observed group rate above half; no prior is silently revised. Separate twenty-inspection future draws use oracle rates solely to generate an illustrative future outcome; building 8 has six failures above its displayed upper intervalfive. Eight realizations do not establish predictive coverage. Marginal posterior curves condition on all groups, so displayed local likelihood/prior alone do not reproduce them.

The computation laboratory repeats those counts/priors internally. A numerical grid, iid grid draws, continuous transformed random-walk Metropolis and mean-field categorical grid approximation target declared bounded distributions. Metropolis includes the logit-mean Jacobian, four fixed chains,1000 warmup and 3000 retained steps per chain, proposal SDs[.3,.3]. Acceptance fractions are[.58975,.59525,.61275,.6015]; classical split Rhat is[1.00210,1.00402], and the explicitly simple within-chain ESS is[1121.60,424.01]. These are not modern rank-normalized/folded/tail diagnostics or a proof of convergence. Grid mean(m,logk)=[.1144995,3.5128897], MCMC=[.1153996,3.4771608]. Mean-field coordinate updates stabilize in 14 iterations; SDs[.023983,.552829] are smaller than joint-grid[.027608,.589720]. Posterior mass in the last concentration column is .008441; bounds remain part of the model. Posterior predictive variance of observed group rates retains Binomial sampling at unequal n. Observed .00540109 compares with replicated mean .00890677 and tail fraction .6154 across 5000 draws. This reuses data intentionally for criticism, not independent predictive assessment or a probability that the model is true.

The temperature GP uses 16 sensors on[.2,3.5]m, mean 20 Celsius, fixed RBF variance4 C²/length.8 m and known reading SD.15 C. Manual Cholesky posterior mean/latent variance matches sklearn with optimizerNone and centered targets to 1e-10. Forty inside/far independent readings have MSE .019973/.456526 and conditional pointwise future-interval coverage .975/1.0; these finite outcomes are not nominal-coverage guarantees. Latent intervals exclude reading noise and future intervals add it. A deliberately incomplete rank-five prior feature covariance loses the omitted K-Q component: at 10 m full latent variance is 4 versus approximately 2.11058e-30 for the low-rank prior. This is a failure demonstration, not a complete sparse/variational inducing-point method or a claim that all sparse GPs collapse away from support. No kernel or noise parameter is selected on assessment.

The known-parameter three-state HMM has 120 steps, transition rows[[.95,.05,0],[.01,.94,.05],[0,0,1]], emission means[0,1,3], SDs[.4,.6,.7], initial healthy. Generated state counts are[16,28,76]. Forward filtering is online; smoothing and Viterbi use all observations. Five-step exhaustive enumeration of 243 paths agrees with likelihood, smoothed marginals and joint MAP path. Full-trajectory marginal filtering/smoothing accuracy .991667/.991667 and Viterbi .983333 are retained rather than forcing an offline improvement. No transition/emission parameters are fitted. An eight-state positive undirected binary chain verifies A independent ofC givenB. A separate sixty-step scalar Kalman fixture uses AR.95, process SD.2 and reading SD.5, giving filter MSE .067354 versus raw .186486. These are inference audits, not field degradation, causal, GNN or remaining-life validation.

Ten original vector figure sets implement both planned briefs, with six equations and nine exercises. Primary GPML Chapters 2/8, Rabiner's author-hosted 1989 tutorial (forward/backward pages 262–263 visually read), and official Naive Bayes/Stan predictive/diagnostic documentation were inspected 20 October 2026. Stan is a documentary source only; its runtime and modern diagnostic implementation are not executed. Live sklearn 1.9.1 versus executed 1.9.0 is disclosed. Every probability and interval remains conditional on its stated observation model, priors, fitting role and approximation.
