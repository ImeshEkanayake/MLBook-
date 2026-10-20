# Chapter 22: Neural architecture families — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_22_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 22.1 · MLPs, residual networks and tabular architectures

- [Common data, explicit architectures](notebooks/108_Chapter_22_01_residual_and_efficient_tabular_models.ipynb#architecture-contract)
- [Weight sharing is not free inference](notebooks/108_Chapter_22_01_residual_and_efficient_tabular_models.ipynb#comparison-limits)

Declared mechanisms: whole-building tabular comparison, residual computation, actual rank-one fast-weight ensemble, numerical basis contract, named-model implementation boundaries.

```bash
python scripts/run_notebook.py notebooks/108_Chapter_22_01_residual_and_efficient_tabular_models.ipynb
```

## 22.2 · Convolutions for signals and structured fields

- [Frequency content and temporal order](notebooks/109_Chapter_22_02_causal_convolutions_and_spectral_features.ipynb#signal-contract)
- [Audit availability separately from predictive performance](notebooks/109_Chapter_22_02_causal_convolutions_and_spectral_features.ipynb#receptive-field)

Declared mechanisms: actual causal Conv1d model, dilation and receptive field, spectral order invariance, whole-machine holdout, future-input perturbation audit.

```bash
python scripts/run_notebook.py notebooks/109_Chapter_22_02_causal_convolutions_and_spectral_features.ipynb
```

## 22.3 · Recurrent and gated architectures

- [State follows an episode, not a row counter](notebooks/110_Chapter_22_03_recurrent_state_and_truncated_training.ipynb#state-contract)
- [Valid observations, carried state and derivative history](notebooks/110_Chapter_22_03_recurrent_state_and_truncated_training.ipynb#history-boundary)

Declared mechanisms: actual RNN GRU and LSTM, irregular-time input contract, masked losses, truncated derivative history, streaming state and entity resets.

```bash
python scripts/run_notebook.py notebooks/110_Chapter_22_03_recurrent_state_and_truncated_training.ipynb
```

## 22.4 · Attention and transformers

- [Token meaning precedes the attention matrix](notebooks/111_Chapter_22_04_attention_tokens_and_access.ipynb#token-contract)
- [Access is a model contract](notebooks/111_Chapter_22_04_attention_tokens_and_access.ipynb#attention-limits)

Declared mechanisms: scaled dot-product attention identity, actual multihead transformer blocks, feature versus time tokens, position and padding contracts, causal future-perturbation test.

```bash
python scripts/run_notebook.py notebooks/111_Chapter_22_04_attention_tokens_and_access.ipynb
```

## 22.5 · State-space and recurrent-attention hybrids

- [A bounded reference experiment, not a full Mamba benchmark](notebooks/112_Chapter_22_05_selective_state_and_reference_attention.ipynb#state-space-contract)
- [Profile the declared reference implementations](notebooks/112_Chapter_22_05_selective_state_and_reference_attention.ipynb#matched-profile)
- [State storage and process peak memory answer different questions](notebooks/112_Chapter_22_05_selective_state_and_reference_attention.ipynb#state-interpretation)

Declared mechanisms: actual input-dependent diagonal state model, exact diagonal discretization, paired context-length assessment, reference attention comparison, untrained summary-attention hybrid contract, measured CPU inference resources.

```bash
python scripts/run_notebook.py notebooks/112_Chapter_22_05_selective_state_and_reference_attention.ipynb
```

## 22.6 · Mixture-of-experts and conditional computation

- [Stored experts and activated computations](notebooks/113_Chapter_22_06_conditional_experts_and_capacity.ipynb#routing-contract)
- [Capacity is a separate serving policy](notebooks/113_Chapter_22_06_conditional_experts_and_capacity.ipynb#capacity-contract)

Declared mechanisms: actual selected-row expert execution, learned top-one routing, load-balance ablation, declared linear-MAC budget, capacity fallback and queue order.

```bash
python scripts/run_notebook.py notebooks/113_Chapter_22_06_conditional_experts_and_capacity.ipynb
```

## 22.7 · Emerging function and geometry-aware designs

- [Approximation is not a learning guarantee](notebooks/114_Chapter_22_07_spline_edge_functions_and_geometry.ipynb#function-contract)
- [State the grid, interaction and symmetry assumptions](notebooks/114_Chapter_22_07_spline_edge_functions_and_geometry.ipynb#function-limits)

Declared mechanisms: actual differentiable cubic edge splines, SciPy basis and gradient checks, additive spline versus composed functions, locked extrapolation test, separate rotation-invariant task.

```bash
python scripts/run_notebook.py notebooks/114_Chapter_22_07_spline_edge_functions_and_geometry.ipynb
```

## Interpretation and boundaries

# Chapter 22 mechanisms, evidence and boundaries

Seven independently executable CPU notebooks use generated records with explicit building/machine or episode boundaries. Actual Torch operations implement the neural mechanisms; named full research systems are comparison context, not falsely claimed library executions. No dependency was added. Core runtime remains Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0, threadpoolctl 3.7.0 and CPU PyTorch 2.14.1. Thread count one, seeds 2308–2314 and deterministic Torch algorithms are explicit. All neural calculations use float64 except the declared float32 state/attention benchmark and its resource children in code_112.

## Experiments and actual conclusions

- **108 — tabular computation:** sixty buildings × six records; train/development/final identities 40/10/10; four continuous plus three one-hot inputs, training-only scale. Ordinary MLP (817 parameters), residual network (2617) and original four-member BatchEnsemble-style fast-weight network (1380); three initializations × two rates × 200 update limits, own development checkpoints. Effective Hadamard matrices independently match vectorized predictions. Ensemble means beat their own individual members but do not consistently beat the ordinary MLP. Residual mean error is lower here with greater capacity. Repeat SD is not a deployment interval. A separate six-training-quantile-knot numerical basis passes partition/reconstruction checks; it is not silently substituted into one fitted comparison. FT-Transformer, TabNet, RealMLP and TabM are located with primary papers, not executed full methods.
- **109 — temporal locality:** sixty machines × four 64-sample windows, 100 Hz; 40/10/10 machine split. An 8-Hz then 12-Hz window versus its exact reversal isolates lost ordering in global power. Fixed logistic global/half-window spectral baselines versus a genuine four-block causal Conv1d model, dilations 1/2/4/8, two rates and 200 updates, own development checkpoints. Final Brier losses 0.251424849, 0.000294110 and 9.00164254e-8; accuracies 0.475/1/1. Receptive span 31 samples, 0.30 seconds, all positions reachable. Future perturbations preserve earlier outputs and fitted last-logit derivatives are zero outside support. Classification uses a completed window, not an unobserved future target. Fixed training-cohort scaling preserves causality.
- **110 — recurrent contracts:** fifty independent building episodes; 30/10/10 identities, source 24–40 events; additional independent final-identity episodes 80–96 events. Explicit elapsed days, observed indicator, and separate valid-padding mask; generator decays by 0.95 raised to elapsed days. Native RNN/GRU/LSTM width eight and GRU truncated every eight events; 120 AdamW update limits, own development checkpoints, valid-count-weighted loss. Truncated training still takes one optimizer update per full batch. Native GRU and LSTM first-step formulas are independently checked, including PyTorch's reset-after-hidden-affine GRU convention. Source MSE 0.0010673/0.00024295/0.00045487/0.00025212, long MSE 0.00485014/0.00139522/0.00200079/0.00143069. Streaming/full frozen predictions agree to rounding. Same forward values with detached chunks cut final-output/first-event gradient from 0.000445505 to zero. Carrying another independent episode's state alters early predictions by about 0.11627. Gate comparisons have different parameter counts.
- **111 — attention access:** independent manual scaled-QKV/native-primitive identity and mask checks. Own pre-normalized width-eight, two-head, feedforward-width-sixteen transformer block. Table task: 30 buildings × six, 20/5/5 split, four numerical field-specific embeddings, categorical and summary tokens, final MSE 0.151710408. Separate causal next-state forecast: fifty episodes, 30/10/10 identities, 48 events, currently observed state/load, final MSE 0.010172543 versus persistence 0.037192204. Both fits use 250 updates with development-only checkpoint selection. Future changes from time 24 leave earlier masked predictions unchanged; removing the same frozen model's mask changes earlier predictions by up to 0.342500907. The latter is an availability audit, not a trained unmasked comparator. Content-only permutation equivariance, positional perturbation, excluded padded keys and unchanged valid-query outputs are checked. Materialized score bytes are accounting, not RSS; MHA true forbids access, while the native primitive identity uses additive zero/negative-infinity masks.
- **112 — selective state and length shift:** own input-dependent diagonal exact zero-order-hold recurrence (627 parameters) versus own materialized causal attention (633), common 633-parameter ceiling, two rates × 120 updates and development checkpoints. Static-control width-48 ablation has 339 parameters, so it is not capacity matched. Marked amplitudes with background distractors; 48/24 train/dev episodes length 32, same 48 final episodes evaluated at prefixes 32/128/512, marker within first sixteen. Last-query MSE selective 0.018865546/0.380159348/0.534933984; attention 0.006982041/0.702159941/1.001933336; static 0.077328995/0.521417797/0.512821436. All-query losses are also retained. Both fitted models fail longer distractor suffixes; static even slightly beats selective at 512. Known marker-copy rule is zero by construction, not learned. Exact constant-control subdivision, streamed/full values and input-dependent controls are verified. An untrained periodic-summary attention fixture verifies causal access only, with no accuracy claim. These references are not S4 or full Mamba 1/2/3 executions. Primary chronology: S4 first 31 Oct 2021, Mamba 1 Dec 2023, Mamba-2 31 May 2024, Mamba-3 16 Mar 2026; all precede the book cutoff.
- **113 — sparse experts:** sixty buildings × ten mixed-regime records, 40/10/10 split. Top-one learned router, selected probability times selected expert, no gradient-through-argmax claim. Actual selected-row execution checked against explicit calculation and forward-hook row counts. Both sparse three-expert and dense candidates use 30 linear MAC/record; softmax, biases, nonlinearities, indexing and dispatch costs are excluded, and no equal-latency claim is made. Sparse/dense stored parameters 108/41, one-path parameters 42/41. Two dense rates and two balance coefficients × 400 updates/own development checkpoints. Dense final MSE 0.044502802; experts balance 0 gives 0.037039745, balance 0.1 gives 0.048347665. Development selects 0.1, retaining its worse final assessment. Loads 33/38/29 are more uniform than 15/65/20, without guaranteeing lower final error or regime recovery. Capacity factor 1 allows 34 per expert, four fallback records and MSE 0.063248946. Factors 1.25/2 permit 42/67 and no overflow, retaining MSE 0.048347665. Input-order admission, explicit centered-zero/raw-training-mean fallback and all-query denominator. Queue permutation at factor 1.25 changes zero flags because no overflow occurs; no observed order effect is claimed.
- **114 — functions and geometry:** actual differentiable cubic Cox–de Boor basis, eleven functions, independent SciPy design-matrix max error 1.110223e-16, nonnegativity/partition checks and interior gradcheck. Own fixed-grid spline-plus-SiLU edge network 2→4→1 (149 parameters), not complete adaptive-grid KAN. Smooth interaction target, source train/dev/final 500/160/300 in [-1,1]²; locked 200-point outside test first coordinate [1.05,1.8]. Additive spline Ridge (23 parameters) versus tensor-product spline Ridge (122), MLP (97), edge network (149), two candidates each/own development selection; neural 400-update limits. Final source MSE 0.312029487/0.001080590/0.002134610/0.001070859; outside MSE 0.941846722/0.375514439/0.260425285/0.345446403. Tensor interactions nearly close the edge model's source advantage over additive splines; MLP extrapolates best here. Clamped spline basis does not make the edge's SiLU-augmented total extrapolation constant. Separate isotropic squared-radius disk task: raw coordinate MLP rotation RMS 0.036368914 versus radial-feature head 7.355637e-17 under angle 0.7; final MSE 0.002717962 versus 4.853367e-6. That symmetry is not imposed on the orientation-dependent interaction target; no graph network is claimed.

## Resource evidence, repairs and reproducibility

Code_112 launches eighteen fresh child CPU processes: two fitted models × three lengths × three repetitions, batch four, float32, one warmup and five inference forwards. Inputs/model state travel in memory to the same interpreter; OS RSS units are explicitly converted for Darwin bytes versus Linux KiB. Peak RSS includes the interpreter/libraries/allocator and is not state-only or GPU memory. The 768-byte recurrent state excludes inputs, returned predictions and training intermediates. The scan uses less process peak memory at length 512 but its Python loop is slower than the small attention reference. Exact observations are recorded below in the execution report, outside deterministic RESULTS. Book figure generation skips the explicitly marked measurement cell, injects its original observations, and reruns every other cell with exact RESULTS checks. It does not claim bit-identical resource timing or silently measure again for the book plot.

All initial kernels passed. The 109 backward receptive-field diagram initially expanded dilation layers in forward order; the diagram loop was corrected to reverse layer order and a fresh run preserved exact results. A tensor-product spline baseline was subsequently added to 114 to separate interaction representation from network choice; all earlier family and geometry results remained exactly unchanged. Visual review then improved 108's residual/matrix layout and common grayscale, clarified 114's diagram labels, and replaced crowded logarithmic context ticks in 111/112. Four fresh kernels reran those current sources; deterministic RESULTS remained exactly identical. The latest 112 run measures its resource observations anew and those current actual observations are retained. No execution warnings are suppressed. Seven notebook sources contain 29 executed code cells and 14 inline figures, all reviewed alongside fourteen original vector book figures.

Primary research papers supply mechanism/chronology context; all numerical results and teaching data mechanisms are original scoped experiments. Documentation accessed 20 October 2026 can identify a newer maintenance patch than the executed pins (notably SciPy live 1.18.0 versus 1.17.1). Named systems' reported benchmark speedups or field claims are not transferred to these references. Literature completeness, operational validity and universal architecture rankings are not asserted.
