# Chapter 27: Generative models for structured data — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_27_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 27.1 · Generative tasks and evaluation targets

- [Joint generation, conditioning and completion ask different questions](notebooks/138_Chapter_27_01_generative_tasks_and_evidence_contracts.ipynb#generation-contract)
- [A valid record is not automatically a useful dataset](notebooks/138_Chapter_27_01_generative_tasks_and_evidence_contracts.ipynb#completion-relations-and-use)

Declared mechanisms: actual joint and conditional mixture sampling, independent-marginal reference, conditional Gaussian-mixture imputation, generated relational keys and temporal constraints, whole-building evidence boundaries.

```bash
python scripts/run_notebook.py notebooks/138_Chapter_27_01_generative_tasks_and_evidence_contracts.ipynb
```

## 27.2 · Latent-variable models and variational learning

- [A likelihood must match each output type](notebooks/139_Chapter_27_02_conditional_vae_and_mixed_likelihoods.ipynb#conditional-vae-contract)
- [Type-valid sampling is only one acceptance check](notebooks/139_Chapter_27_02_conditional_vae_and_mixed_likelihoods.ipynb#mixed-generation-and-collapse)

Declared mechanisms: actual reparameterized conditional VAE, Gaussian Bernoulli and Poisson decoder heads, common development ELBO comparison, per-latent KL and decoder sensitivity, conditional tail and type-valid generation.

```bash
python scripts/run_notebook.py notebooks/139_Chapter_27_02_conditional_vae_and_mixed_likelihoods.ipynb
```

## 27.3 · Adversarial models and training dynamics

- [A discriminator loss is not a distributional certificate](notebooks/140_Chapter_27_03_conditional_gan_and_training_dynamics.ipynb#adversarial-contract)
- [Track modes, fitting dynamics and downstream use separately](notebooks/140_Chapter_27_03_conditional_gan_and_training_dynamics.ipynb#adversarial-assessment)

Declared mechanisms: actual conditional GAN and Wasserstein gradient penalty, controlled aggressive generator candidate, development selected generative checkpoints, conditional mode coverage and resampling references, actual rare-class augmentation assessment.

```bash
python scripts/run_notebook.py notebooks/140_Chapter_27_03_conditional_gan_and_training_dynamics.ipynb
```

## 27.4 · Autoregressive, flow and energy models

- [Three mechanisms need different evidence](notebooks/141_Chapter_27_04_autoregressive_flow_and_energy_models.ipynb#factorization-and-measure)
- [Inversion and a tractable Jacobian do not diagnose coverage](notebooks/141_Chapter_27_04_autoregressive_flow_and_energy_models.ipynb#sampling-and-density-limits)

Declared mechanisms: normalized mixed-type autoregressive factorization, native affine-coupling flow with inverse and Jacobian checks, native persistent-negative-phase energy learning, Langevin mixing and unnormalized score limits, independent reference assessment.

```bash
python scripts/run_notebook.py notebooks/141_Chapter_27_04_autoregressive_flow_and_energy_models.ipynb
```

## 27.5 · Diffusion and flow matching

- [Share a task without equating distinct objectives](notebooks/142_Chapter_27_05_diffusion_and_flow_matching.ipynb#diffusion-and-transport-contract)
- [Sampling accuracy and distributional accuracy remain separate](notebooks/142_Chapter_27_05_diffusion_and_flow_matching.ipynb#sampling-and-refinement)

Declared mechanisms: actual conditional DDPM epsilon prediction and ancestral sampling, native straight-path conditional flow matching, separate development objectives and fixed training budgets, ODE refinement with shared initial noise, mechanism alignment and trajectory distribution assessment.

```bash
python scripts/run_notebook.py notebooks/142_Chapter_27_05_diffusion_and_flow_matching.ipynb
```

## 27.6 · Utility, validity, leakage and privacy

- [A generator needs an acceptance contract, not one quality number](notebooks/143_Chapter_27_06_synthetic_data_acceptance_and_disclosure.ipynb#acceptance-evidence-contract)
- [Novel rows and failed attacks are incomplete privacy evidence](notebooks/143_Chapter_27_06_synthetic_data_acceptance_and_disclosure.ipynb#privacy-and-acceptance-limits)

Declared mechanisms: separate fidelity utility schema and disclosure evidence, actual source-only synthetic-only and augmented classifiers, development-calibrated proximity membership attack on generated data, deliberate source canary and exact-copy audits, relational and derived-field acceptance checks without DP claims.

```bash
python scripts/run_notebook.py notebooks/143_Chapter_27_06_synthetic_data_acceptance_and_disclosure.ipynb
```

## Interpretation and boundaries

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

