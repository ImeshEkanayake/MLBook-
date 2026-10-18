# Chapter 5: concept-to-code guide

Read each prediction prompt, run the notebook from a fresh kernel, then interpret results before changing controls. Permanent IDs code_022–code_026 map one-to-one to sections 5.1–5.5. Each notebook contains all imports, generated data and helpers; the pinned CPU environment is sufficient. No external files or credentials are needed for ordinary execution. See [run evidence](CHAPTER_05_EXECUTION.md) and the [registry](CODE_EXAMPLES.md).

## 5.1 · Generalization and the target population

- [contract](notebooks/022_Chapter_05_01_Generalization_And_The_Target_Population.ipynb#contract): Target case, available state, grouped boundaries and known/new-site estimands.
- [development](notebooks/022_Chapter_05_01_Generalization_And_The_Target_Population.ipynb#development): Development scores diagnose the two different questions.
- [final](notebooks/022_Chapter_05_01_Generalization_And_The_Target_Population.ipynb#final): Fixed-rule final and equal-site MSE; six independent new sites.
- [support](notebooks/022_Chapter_05_01_Generalization_And_The_Target_Population.ipynb#support): Marginal ranges versus observed joint support; distance is not calibration.
- [exercises](notebooks/022_Chapter_05_01_Generalization_And_The_Target_Population.ipynb#exercises): Unequal-site weights, calibrated-new-site contract and construction-era shift.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/022_Chapter_05_01_Generalization_And_The_Target_Population.ipynb
```

## 5.2 · Capacity, overfitting and bias–variance

- [capacity](notebooks/023_Chapter_05_02_Capacity_Overfitting_And_Bias_Variance.ipynb#capacity): Nested degree families, training/development curves, numerical basis and fixed data.
- [final](notebooks/023_Chapter_05_02_Capacity_Overfitting_And_Bias_Variance.ipynb#final): Development selection followed by frozen-rule final evidence.
- [decomposition](notebooks/023_Chapter_05_02_Capacity_Overfitting_And_Bias_Variance.ipynb#decomposition): Repeated training samples, fixed-input squared bias, variance, noise and exact identity.
- [exercises](notebooks/023_Chapter_05_02_Capacity_Overfitting_And_Bias_Variance.ipynb#exercises): Boundary location, algorithm randomness, other losses and selection variability.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/023_Chapter_05_02_Capacity_Overfitting_And_Bias_Variance.ipynb
```

## 5.3 · Regularization and inductive bias

- [lenses](notebooks/024_Chapter_05_03_Regularization_And_Inductive_Bias.ipynb#lenses): Same-data line/smooth/local/monotone completions and unsupported regions.
- [shrinkage](notebooks/024_Chapter_05_03_Regularization_And_Inductive_Bias.ipynb#shrinkage): Mean-loss ridge objective, intercept convention, stationarity, units/rescaling and stopping.
- [families](notebooks/024_Chapter_05_03_Regularization_And_Inductive_Bias.ipynb#families): Actual smooth additive, constrained monotone and deep neural fits; training-only preprocessing.
- [augmentation](notebooks/024_Chapter_05_03_Regularization_And_Inductive_Bias.ipynb#augmentation): Valid scalar augmentation only under an isotropic symmetry; target types matter.
- [exercises](notebooks/024_Chapter_05_03_Regularization_And_Inductive_Bias.ipynb#exercises): Penalty normalization, units, interaction, post-peak regime and checkpoint selection.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/024_Chapter_05_03_Regularization_And_Inductive_Bias.ipynb
```

## 5.4 · Learning curves and data value

- [size-curve](notebooks/025_Chapter_05_04_Learning_Curves_And_Data_Value.ipynb#size-curve): Nested sizes, repeated pools, fixed development set and descriptive spread.
- [sites](notebooks/025_Chapter_05_04_Learning_Curves_And_Data_Value.ipynb#sites): Known-slope derivation and simulation: independent sites versus repeated readings.
- [coverage](notebooks/025_Chapter_05_04_Learning_Curves_And_Data_Value.ipynb#coverage): Material subgroup coverage and acquisition-cost information required.
- [final](notebooks/025_Chapter_05_04_Learning_Curves_And_Data_Value.ipynb#final): Predeclared n=192 cubic; one fresh final sample; no best replicate.
- [exercises](notebooks/025_Chapter_05_04_Learning_Curves_And_Data_Value.ipynb#exercises): Model floor, wrong assessment population, acquisition costs and changed sensor.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/025_Chapter_05_04_Learning_Curves_And_Data_Value.ipynb
```

## 5.5 · Assumptions as testable commitments

- [ledger](notebooks/026_Chapter_05_05_Assumptions_As_Testable_Commitments.ipynb#ledger): Six assumptions, their observable stress tests and possible actions.
- [response](notebooks/026_Chapter_05_05_Assumptions_As_Testable_Commitments.ipynb#response): Linearity, nonlinear high-load response and declared extrapolation.
- [sampling](notebooks/026_Chapter_05_05_Assumptions_As_Testable_Commitments.ipynb#sampling): Local support, later-window drift, shared-site dependence and exchangeability limits.
- [symmetry](notebooks/026_Chapter_05_05_Assumptions_As_Testable_Commitments.ipynb#symmetry): Physical load rotation versus coordinate equivariance, units, SPD solve and residual limits.
- [exercises](notebooks/026_Chapter_05_05_Assumptions_As_Testable_Commitments.ipynb#exercises): Operational ledger criteria, later-time split, regime grid and incorrect physical models.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/026_Chapter_05_05_Assumptions_As_Testable_Commitments.ipynb
```

## How to extend the evidence

Keep target population, available information, independent unit, split and averaging scheme explicit. Use development evidence to choose model capacity, penalty, checkpoint or representation. After any final outcomes have been consulted, obtain genuinely fresh final evidence for a revised rule. Test simulator identities separately from population performance. A geometric support flag is not a probability, a hard constraint is not a finite penalty, and fitting an equation is not validation against observations.

The model settings are fixed and disclosed as scoped mechanism controls. Later family chapters cover full estimator-constructor studies. The experiments do not supply empirical structural safety, causal benefits of collection, equal-compute model rankings or universal curve shapes. Only the stated ideal isotropic scalar augmentation preserves rotated-force targets; the direction-dependent counterexample requires direction information.
