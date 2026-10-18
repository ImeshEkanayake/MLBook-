# Chapter 4 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** all five executed; publication verification pending.

Every code cell executed in order in a fresh kernel using the unchanged runner and pinned environment. These five runs were launched concurrently; wall times include kernel lifecycle and are observations rather than performance promises. All imports, generated inputs, algorithms and helpers are inside each notebook. Ordinary runs need no data files, downloads, API keys, GPU or private project modules. No dependency was added. CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0 and scikit-learn 1.9.0 were printed by every kernel; Darwin arm64 CPU. Full pins remain in requirements-lock.txt; pip check passes.

| Example | Section | Code cells | Inline figures | Wall seconds incl. kernel lifecycle |
| --- | --- | ---: | ---: | ---: |
| [code_017](CODE_EXAMPLES.md#code_017) | 4.1 | 7 | 1 | 2.277 |
| [code_018](CODE_EXAMPLES.md#code_018) | 4.2 | 6 | 2 | 2.618 |
| [code_019](CODE_EXAMPLES.md#code_019) | 4.3 | 6 | 1 | 2.362 |
| [code_020](CODE_EXAMPLES.md#code_020) | 4.4 | 7 | 2 | 2.504 |
| [code_021](CODE_EXAMPLES.md#code_021) | 4.5 | 6 | 2 | 2.427 |

Total: **32 new code cells and eight inline figures**. Seed, actual numeric results and inside-kernel elapsed time are printed in each notebook's final summary. Source notebooks are committed with executed outputs.

## Actual outputs and independent checks

- **code_017:** disjoint 144/48/48 member partitions are fixed before fitting. Coefficients are [1.7574679731, .1744371290] mm; training half MSE .00504706035 mm² and gradient norm 1.30e-16 mm. Final MAE is .0883451235 mm versus .4504293754 mm for the training-mean baseline. A separate one-example update changes prediction .5 to .75 mm and half squared loss .125 to .03125 mm². Reference-load conversion preserves physical predictions.
- **code_018:** fixed mean/median/.9-quantile and logistic fits use 540 training members, with disjoint 180 development and 180 final members. Final mean MSE is .0441701211 mm², median MAE .1528755015 mm, quantile pinball loss .0495468119 mm and empirical quantile coverage .944444. Separate binary-event log loss is .6506375342. Different metrics/units are not ranked against one another. Pinball asymmetry and stable score-space binary loss pass; extreme logits +/-1000 give finite losses. The .944444 coverage is retained rather than tuning the nominal level to match the spent assessment.
- **code_019:** exact initial gradient [-3.75,-2.25] mm gives weights [.375,.225] mm after rate .1; initial half MSE is 4.875 mm². Finite differences agree. At fixed parameters, observed batch-gradient variance traces track covariance/B for independent uniform replacement draws. After 120 updates, full/B8/B1 objectives are .0149854464/.0150306049/.0167283890 mm² versus least-squares minimum .0149775509. Exposure budgets are 14400/960/120 examples respectively, so this is not a fair throughput benchmark. Full-batch monotonicity at the declared stable rate and stochastic increases are checked.
- **code_020:** stored scaler/model state survives an in-memory JSON round trip and a query's prediction is invariant to batch companions. The wrong refit-on-batch representation differs as intended. Actual encoder/decoder reconstruction pretraining reduces source objective .509250464 to .0114971274. A disjoint downstream head fit leaves encoder weights unchanged and has final synthetic MAE .0660897386. A separate episodic kernel predictor learns bandwidth .218664524, reducing training query objective .106890180 to .0431406770. Its analytic bandwidth gradient agrees with finite differences. Shifting every new support label by one changes predictions by one to within 6.67e-16, with exactly unchanged learned bandwidth. This is a tiny real contextual pretraining mechanism, not a foundation model or a general transfer claim.
- **code_021:** zero step size leaves a nonzero gradient norm .774453610; the deliberately zeroed gradient report fails comparison with finite differences. Corrected updates reach half MSE 4.00e-11. An affine capacity floor .0344866599 remains at a stationary optimum for a quadratic target, while quadratic features fit to about 1.39e-31. Tiny polynomial training errors are below 2.3e-14 for both original and permuted targets, demonstrating why tiny-set fitting cannot validate target identity. A future-result feature is rejected by its availability ledger, and mm-to-m target scaling changes squared loss by 1e-6 rather than demonstrating better physical accuracy.

## Scope and verification

The task/state ledger separates trainable coefficients, hyperparameters, fitted statistics, schema, seeds and predictions. Output links distinguish mean, median, quantile and probability; range validity does not imply calibration. Estimator settings are fixed and disclosed as partial controls, with full constructor labs deferred to later model chapters.

Main fitted examples keep training/calibration and final outcomes separate. Pure gradients, numerical identities and deliberate training failures do not claim population evaluation. Encoder source data, downstream calibration/assessment and contextual task training are distinct generators with declared roles. Frozen-state comparisons use exact saved arrays/scalars; context labels enter the predictor's inputs, not its parameter update. No downloaded pretrained model or hidden external service is involved.

All eight figures are visually inspected, with numeric/textual explanations, units and grayscale line/marker distinctions. Notebook schemas, sequential execution, absence of error outputs, meaningful assertions, self-contained source, guide anchors, local links and output-summary/manifest agreement are checked using scripts/check_chapter04.py. The prior sixteen notebooks and manifest records remain unchanged. Only companion notebooks/docs are published; local manuscript sources and book figures remain separate.

No empirical structural validity, causal effect, universal quantile calibration, optimizer superiority or pretraining benefit is inferred beyond these declared mechanisms. Final outcomes already read here must be treated as spent when designing extensions; use development evidence and genuinely fresh final observations for subsequent choices.
