# Chapter 38: Explainable AI and model interpretation — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_38_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 38.1 · Interpretability goals and transparent models

- [Fit interpretable baselines in a declared representation](notebooks/201_Chapter_38_01_transparent_physical_baselines_and_decision_paths.ipynb#transparent-physical-baselines)
- [Trace one prediction without treating it as an action justification](notebooks/201_Chapter_38_01_transparent_physical_baselines_and_decision_paths.ipynb#local-trace-and-interpretation-goals)

Declared mechanisms: actual raw linear log Lasso small tree and boosted physical response models, source-only transformed coefficient interpretation with nuisance variables, actual local additive log prediction and native tree decision path, independent accuracy and negative physical output diagnostics.

```bash
python scripts/run_notebook.py notebooks/201_Chapter_38_01_transparent_physical_baselines_and_decision_paths.ipynb
```

## 38.2 · Effects, importance and dependent features

- [State which information a permutation removes](notebooks/202_Chapter_38_02_permutation_ICE_partial_dependence_and_ALE.ipynb#permutation-and-dependent-inputs)
- [Compute different curves rather than rename one curve](notebooks/202_Chapter_38_02_permutation_ICE_partial_dependence_and_ALE.ipynb#ICE-PDP-and-local-effects)

Declared mechanisms: actual source fitted models with and without a correlated sensor, marginal joint and within-sensor-bin permutation loss changes, actual individual conditional expectation partial dependence and finite-bin ALE, support diagnostics for feature combinations and noncausal interpretation.

```bash
python scripts/run_notebook.py notebooks/202_Chapter_38_02_permutation_ICE_partial_dependence_and_ALE.ipynb
```

## 38.3 · Local attributions and SHAP

- [Enumerate a declared game instead of treating attribution as a unique property](notebooks/203_Chapter_38_03_exact_SHAP_coalitions_and_background_sensitivity.ipynb#define-the-coalition-game)
- [Test reasonable reference variation and the combinations it creates](notebooks/203_Chapter_38_03_exact_SHAP_coalitions_and_background_sensitivity.ipynb#background-stability-and-supported-combinations)

Declared mechanisms: actual exact three-feature Shapley coalition enumeration for a fitted classifier, two valid empirical background populations with different baselines, conditional background-resample variability separated from model uncertainty, correlated-feature masking support diagnostic and exact efficiency checks.

```bash
python scripts/run_notebook.py notebooks/203_Chapter_38_03_exact_SHAP_coalitions_and_background_sensitivity.ipynb
```

## 38.4 · Counterfactual explanations and recourse

- [Solve an input-edit problem and audit its meaning](notebooks/204_Chapter_38_04_counterfactual_edits_physical_recourse_and_explanation_questions.ipynb#record-edit-versus-physical-action)
- [Give each explanation its own question](notebooks/204_Chapter_38_04_counterfactual_edits_physical_recourse_and_explanation_questions.ipynb#one-prediction-three-questions)

Declared mechanisms: actual source-scaled logistic alarm model on normalized load strain stiffness, analytic closest standardized model-changing edit versus immutable physical constraints, explicit load-action search propagating strain through a declared elastic relation, same-prediction local attribution global effect and feasible-action Visual A.

```bash
python scripts/run_notebook.py notebooks/204_Chapter_38_04_counterfactual_edits_physical_recourse_and_explanation_questions.ipynb
```

## 38.5 · Graph, temporal and scientific explanations


Declared mechanisms: actual graph neural regression and learned sparse edge mask with hard-mask fidelity checks, single-edge model perturbations compared with an independent elastic solver, nodewise displacement error and equilibrium residual maps, actual learned temporal attention and integrated gradients with occlusion and parameter randomization controls.

```bash
python scripts/run_notebook.py notebooks/205_Chapter_38_05_graph_masks_physical_residuals_and_temporal_attribution.ipynb
```

## Interpretation and boundaries

# Chapter 38 mechanisms, controls and interpretation

Five original laboratories retain all five original scopes and both visual briefs: 21 executed code cells and 11 inline figures. All imports, helpers and generated inputs are internal. Ordinary execution is offline and CPU-only, without files, credentials or new dependencies/assets. Main runtime remains CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and threadpoolctl 3.7.0.205 additionally uses existing Torch 2.14.1 CPU, deterministic float64 and one thread. Execution/access date22 October2026 Australia/Melbourne; literature cutoff18 October2026.

- **201 / transparent representations:**1,200 source/600 final independent beams, correlated log load/span, physical cantilever law10qL^4/(8EI)mm with multiplicative lognoiseSD0.05, four irrelevant sensors. Actual raw linear, standardized log Lasso alpha0.01, depth3 tree/minleaf30 and120iteration HGB. Physical log coefficients0.991048/3.959420/−0.907345/−0.978224; all four nuisance coefficients zero. Backtransform is median-like, not automatic conditional-mean correction. Final RMSE14.445465mm(logLasso),199.829829(rawlinear),192.433352(tree),146.641885(boost); negative prediction fractions0/0.208333/0/0.01 respectively. Exact source-centred local log decomposition and actual native tree decision_path for first fixed final beam. Tree path has three L thresholds4.187/3.454/2.942 and leaf32.692mm. Transparent function traces do not establish intervention benefit or scientific discovery from field observations.
- **202 / dependent inputs:**1,000 source/600 final generated records; load/strain correlation0.97, independent sensor. Actual fixed HGB with all features and reduced load/sensor model. Final MSE0.121528/0.118896; no selection. Twenty marginal permutation MSE increases full load4.845486/strain0.007771/sensor0.444891; joint load/strain5.088687; load permuted within ten strain bins0.676104, explicitly approximate conditional diagnostic. Across-permutationSD is Monte Carlo variability, not population uncertainty. Fraction outside three sourceSD of load−strain0.003333→0.615 after marginal load permutation. Actual35point source5–95% grid, five predeclared ICE rows, all-source PDP, ten quantile-bin finite-difference ALE. Midpoint ALE approximation accumulates increments minus half current bin and source-count centres; PDP centres by grid mean. Counts/identities independently asserted. Curves describe fitted response, not causal interventions.
- **203 / exact attribution:** Actual source HGB, three features, fixed query[1.4,1.4,0.4], probability0.802418. Enumerates all eight coalitions and factorial Shapley formula, asserting efficiency. Absent features retain joint empirical background; query-fixed/absent dependence can break. This is a declared finite empirical interventional game, not conditional causal SHAP or a TreeSHAP/package benchmark.120 mixed source background baseline0.316595/loadphi0.458357/strainphi−0.006906/sensorphi0.034371;120 high-load source baseline0.742060/loadphi0.015851/strainphi−0.020920/sensorphi0.065428. Forty within-background bootstrap resamples give conditional central95% ranges, excluding model-refit/causal uncertainty. Mixed-background one-of-load/strain coalitions create off-relation fractions0.816667/0.808333. Exact additivity does not validate reference/support.
- **204 / recourse:**1,200 source normalized load/strain/stiffness states, source StandardScaler and logisticC2; query[8,8,1],p0.887287. Analytic closest standardized Euclidean projection to targetp0.2 changes immutable stiffness+0.148578, physical residual−1.888619;distance1.436053.151 coherent load actions fixedstiffness1/strain=q/k choose largest admissibleq4.68,p0.194343,reduction3.32,distance1.827368,zero relation residual. This is declared relation/grid feasibility, not real intervention effect. VisualA uses same query/model for exact80-background three-feature probability attribution, all-source load PDP and coherent load-action path. Three questions remain distinct; features use normalized reference units rather than literal field strain magnitudes.
- **205 / structured explanation tests:**800source/200final scalar spring networks,6nodes/8edges, support0; known stiffness matrix solves5 free nodal displacements. Actual3layer GNN/16hidden/400Adamupdates has final nodeRMSE0.103923mm/tip0.146841mm. Original frozen-predictor retention+sparsity mask objective is squared original tip deviation+0.01mean sigmoid gate,300updates; no claim to full GNNExplainer MI/feature-mask reproduction. Continuous mask tiperror0.002467mm; hardtop3edges[5,6,1]error1.749138mm. This failed hard extraction is retained. All single-edge removals remain physically solvable; actual model and independent solver tipchanges differ, including learned negative changes for several physically positive ones. Querypredtip0.949693/solvertip0.943815mm; free equilibrium residualL2 0.260212kN despite exact zero support displacement. Separate displacementerror(mm)/forceresidual(kN) maps use schematic drawing coordinates, not truss geometry. Temporal800source/200final AR0.6,length20, noisy last-three target; actual attentionpoolingnet400updates. FinalRMSE0.100866. Source-mean baseline,256midpoint integrated gradients, completenesserror1.32e−8. IGtop3[2,19,18] replacementchange−0.022577;attentiontop3[17,18,19]change−0.032178;20randomthree-positioncontrols retained. Fully reset learnedparameters includingpositions gives IG rankcorrelation0.906767, an unfavourable specificity check retained rather than query-selected away. Neither attention nor IG is claimed causal.

Every current source runs in a fresh kernel with all assertions passing, no notebook errors or stderr. All cells rerun independently during vector export with exact scientific RESULTS equality. Eleven original SVG/PDF/PNG sets and inline versions are reviewed during delivery. Full primary PDFs inspected for ALE(arXivv2/2019), SHAP(2017), integrated gradients(2017), GNNExplainer(arXivv4/2019) and counterfactuals(arXiv2017); no full-PDF inspection of the separately inaccessible saliency-sanity-check paper is claimed or cited. Sources contextualize methods; all numerical results are original generated experiments. Chapters39–43 and whole-book audit remain required.
