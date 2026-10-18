# Chapter 4: how models learn — concept-to-code guide

Five independent laboratories connect a task to a written prediction rule, objective, fitting procedure, reusable state and diagnostic evidence. Each supplies its own setup, generated inputs, helper definitions, prediction prompts, controlled checks, exercises and separate hints. Read the [execution report](CHAPTER_04_EXECUTION.md), use the [pinned environment](requirements-lock.txt), and find permanent IDs in [CODE_EXAMPLES.md](CODE_EXAMPLES.md).

| Manuscript mechanism | Notebook section | Executable evidence or extension |
| --- | --- | --- |
| Operational target, feature availability, units and independent split unit | [code_017: contract](notebooks/017_Chapter_04_01_Parameters_Predictions_And_Objectives.ipynb#contract) | One independent member per row, N/mm conventions, fixed reference load and disjoint 144/48/48 partitions. |
| Parameters, hyperparameters, learned state, predictions and reproducibility controls | [code_017: contract](notebooks/017_Chapter_04_01_Parameters_Predictions_And_Objectives.ipynb#contract) | Explicit role/provenance/unit ledger; optimizer/checkpoint-state exercise. |
| Empirical objective, weighting, baseline, regularization role and non-gradient fitting | [code_017: fit](notebooks/017_Chapter_04_01_Parameters_Predictions_And_Objectives.ipynb#fit) | Half MSE, training-only least squares, stationarity and training-mean baseline; penalty/averaging extensions. |
| Reference coordinates and held-out evidence | [code_017: development](notebooks/017_Chapter_04_01_Parameters_Predictions_And_Objectives.ipynb#development) and [final](notebooks/017_Chapter_04_01_Parameters_Predictions_And_Objectives.ipynb#final) | Physical prediction invariance to reference-load conversion and one fixed-rule final comparison. |
| Predict/compare/adjust arithmetic | [code_017: one step](notebooks/017_Chapter_04_01_Parameters_Predictions_And_Objectives.ipynb#one-step) | Exact separate one-observation update; target unchanged, prediction/loss before and after. |
| Squared/absolute/pinball loss, output summaries and asymmetry | [code_018: losses](notebooks/018_Chapter_04_02_Loss_Functions_And_Output_Meanings.ipynb#losses) | Normalized loss curves and .9/.1 residual slopes; skew-response generator makes mean/median/quantile different. |
| Fixed estimator controls and output meaning | [code_018: contract](notebooks/018_Chapter_04_02_Loss_Functions_And_Output_Meanings.ipynb#contract) | Mean least squares, QuantileRegressor tau=.5/.9, alpha=0, HiGHS; fixed logistic C/solver/iteration budget. Partial mechanism controls, not exhaustive constructors. |
| Probability links, likelihood and numerical stability | [code_018: output links](notebooks/018_Chapter_04_02_Loss_Functions_And_Output_Meanings.ipynb#output-links) | Sigmoid/logit interpretation, finite extreme-score log loss and moderate-score identity; separate binary event. |
| Quantile coverage, probability calibration limits, metrics versus decisions | [code_018: assessment](notebooks/018_Chapter_04_02_Loss_Functions_And_Output_Meanings.ipynb#assessment) and [exercises](notebooks/018_Chapter_04_02_Loss_Functions_And_Output_Meanings.ipynb#exercises) | Fixed final losses/coverage with no retuning; Gaussian-scale, class-weighting, penalty and decision-threshold extensions explicitly distinguished. |
| Chain-rule regression gradient and several hand updates | [code_019: hand update](notebooks/019_Chapter_04_03_Gradients_And_Iterative_Optimization.ipynb#hand-update) | Four exact rows, initial gradient, first weights, five-step trace and finite-difference check. |
| Full/stochastic/minibatch gradients and unbiasedness | [code_019: gradient noise](notebooks/019_Chapter_04_03_Gradients_And_Iterative_Optimization.ipynb#gradient-noise) | Average per-row gradient equals full gradient; uniform independent replacement sampling at fixed parameters. |
| Noise scaling and batching assumptions | [code_019: gradient noise](notebooks/019_Chapter_04_03_Gradients_And_Iterative_Optimization.ipynb#gradient-noise) | Empirical covariance-trace/B agreement; replacement batch of size n distinguished from deterministic full batch; no-replacement correction exercise. |
| Rate, fluctuations, epochs, monitoring quantity and resource budgets | [code_019: trajectories](notebooks/019_Chapter_04_03_Gradients_And_Iterative_Optimization.ipynb#trajectories) and [checks](notebooks/019_Chapter_04_03_Gradients_And_Iterative_Optimization.ipynb#checks) | Full objective after every update, exact optimum, actual exposure counts and quadratic stability bound; fixed-seed rather than best-seed comparison. |
| Training-only fitted preprocessing and inference batch invariance | [code_020: scaler](notebooks/020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb#scaler) | Fitted means/scales, fixed query prediction across companions, deliberate wrong refit-on-batch representation. |
| Reproducible inference state versus resumable training state | [code_020: scaler](notebooks/020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb#scaler) and [exercises](notebooks/020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb#exercises) | In-memory JSON round trip with schema/output meaning; optimizer/RNG continuation checklist. |
| Pretraining as actual reusable model training | [code_020: encoder pretraining](notebooks/020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb#encoder-pretraining) | Separate 1200-row unlabeled source, encoder/decoder reconstruction gradients, derivative check and decreased objective. |
| Frozen representation, downstream fitting and fine-tuning distinction | [code_020: frozen encoder](notebooks/020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb#frozen-encoder) | Disjoint downstream calibration/development/final data, head-only fit, exact unchanged encoder comparison; fine-tuning extension requires new evidence. |
| Real contextual-predictor pretraining across tasks | [code_020: context pretraining](notebooks/020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb#context-pretraining) | Train one kernel bandwidth across 200 support/query tasks, analytic versus numeric gradient and lower query objective; bounded numerical controls disclosed. |
| Conditioning on labels with frozen learned parameters | [code_020: frozen context](notebooks/020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb#frozen-context) | Separate new support/query inputs, +1 support-label shift gives +1 predictions with exactly unchanged bandwidth. Limited kernel mechanism, not a foundation model or general transfer guarantee. |
| Flat loss: zero update versus incorrect zero gradient | [code_021: flat loss](notebooks/021_Chapter_04_05_Learning_Failures_And_Diagnostics.ipynb#flat-loss) | Nonzero true sensitivity with zero rate, explicitly zeroed gradient caught by finite differences, corrected loop agrees with reference fit. |
| Capacity floor versus failed optimization | [code_021: capacity](notebooks/021_Chapter_04_05_Learning_Failures_And_Diagnostics.ipynb#capacity) | Stationary affine least-squares fit retains quadratic residual; adding a known quadratic feature resolves the constructed representational limit. |
| Tiny-data overfit: useful implementation check with limits | [code_021: tiny overfit](notebooks/021_Chapter_04_05_Learning_Failures_And_Diagnostics.ipynb#tiny-overfit) | Degree-seven interpolation fits both original/permuted eight-row targets; passing does not validate IDs or generalization. |
| Data mistakes, unsuitable objective, component scales and next investigations | [code_021: data/objective](notebooks/021_Chapter_04_05_Learning_Failures_And_Diagnostics.ipynb#data-objective) and [exercises](notebooks/021_Chapter_04_05_Learning_Failures_And_Diagnostics.ipynb#exercises) | Availability rejects a future-result feature, target-unit loss ratio and output/objective worksheet; shape/ID/NaN, weighted-loss and monitoring/selection-boundary exercises. |

## What the experiments establish

Data-generating assumptions, fixed unit references, fitted state, trainable parameters, training controls and decision criteria have separate roles. Scaler fitting is learned preprocessing; the encoder and contextual kernel perform real model training for reuse. Frozen-context labels are inputs to an evaluated rule, while updating the learned bandwidth is parameter training. The two small pretraining examples are independent mechanisms rather than one claimed general-purpose system.

Training/calibration evidence is separated from assessment in fitted predictive examples; settings are not retuned on their already-viewed final outcomes. Pure derivative checks, numerical identities and intentionally broken training cases do not need a population assessment split to make their stated implementation claim. Their success cannot establish field validity, causal effects, probability calibration or model transfer. Full model constructor and optimizer-engineering laboratories remain in later chapters.

The B=1/8/full trajectory comparison fixes updates rather than example exposures and discloses the unequal budgets. A flatter or lower curve is not a claim of universal optimizer superiority. Pinball loss and probability/response units are preserved, and a finite penalty is not an exact physical constraint. Keep genuinely fresh final evidence when adapting the examples.

## Run

From the activated pinned environment at repository root:

```bash
python scripts/run_notebook.py notebooks/017_Chapter_04_01_Parameters_Predictions_And_Objectives.ipynb
python scripts/run_notebook.py notebooks/018_Chapter_04_02_Loss_Functions_And_Output_Meanings.ipynb
python scripts/run_notebook.py notebooks/019_Chapter_04_03_Gradients_And_Iterative_Optimization.ipynb
python scripts/run_notebook.py notebooks/020_Chapter_04_04_Training_Inference_And_Reusable_State.ipynb
python scripts/run_notebook.py notebooks/021_Chapter_04_05_Learning_Failures_And_Diagnostics.ipynb
python scripts/check_chapter04.py
```

Default execution writes a separate reference copy under ignored `build/`. Use `--output` with a source notebook path only when intentionally replacing its stored outputs after a full successful run. Restart/run-all after edits; saved outputs do not replace fresh-kernel execution.
