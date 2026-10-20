# Chapter 18: Trees and ensemble learning — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_18_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## Preserved original tree-control laboratory

[code_001: full constructor/pruning guide](notebooks/001_Chapter_18_01_Decision_Tree.ipynb#mechanism) remains the permanent primary companion for18.1, alongside the new087supplement below. Its notebook and historical manifest bytes are preserved. A current fresh-kernel rerun produced21cells/19figures with identical final metrics; [original publication evidence](EXECUTION_REPORT.md) and current Chapter18execution report distinguish the two runs.

## 18.1 · Decision trees and recursive partitioning

- [Supplement the preserved code_001 laboratory](notebooks/087_Chapter_18_01_Paths_Routes_And_Instability.ipynb#path)
- [Missing is a fitted route; an unseen category is a contract choice](notebooks/087_Chapter_18_01_Paths_Routes_And_Instability.ipynb#missing)

Declared mechanisms: weighted impurity and actual decision paths, small label perturbation and root instability, missing routes versus unknown categories, linked original tree-control laboratory.

```bash
python scripts/run_notebook.py notebooks/087_Chapter_18_01_Paths_Routes_And_Instability.ipynb
```

## 18.2 · Bagging, random forests and extra trees

- [Average varied fits, then check what varied](notebooks/088_Chapter_18_02_Aggregation_Diversity_And_OOB_Limits.ipynb#forests)
- [A row can be out of bag while its building remains in memory](notebooks/088_Chapter_18_02_Aggregation_Diversity_And_OOB_Limits.ipynb#oob)

Declared mechanisms: bootstrap and randomized threshold ensembles, prediction instability and covariance, out-of-bag rows versus new entities, correlated measurements and fixed held-out comparison.

```bash
python scripts/run_notebook.py notebooks/088_Chapter_18_02_Aggregation_Diversity_And_OOB_Limits.ipynb
```

## 18.3 · Boosting and additive correction

- [Follow a baseline and two residual learners](notebooks/089_Chapter_18_03_Residual_Steps_And_Reweighting.ipynb#correction)
- [Weight hard cases; choose a stage budget before final assessment](notebooks/089_Chapter_18_03_Residual_Steps_And_Reweighting.ipynb#selection)

Declared mechanisms: manual squared-error residual correction, loss gradients versus ordinary residuals, AdaBoost weight updates, development-selected stage count.

```bash
python scripts/run_notebook.py notebooks/089_Chapter_18_03_Residual_Steps_And_Reweighting.ipynb
```

## 18.4 · Modern boosted-tree implementations

- [Execute all three libraries on the same evidence boundary](notebooks/090_Chapter_18_04_Native_Boosters_Identical_Group_Protocol.ipynb#protocol)
- [Verify inference representations explicitly](notebooks/090_Chapter_18_04_Native_Boosters_Identical_Group_Protocol.ipynb#contracts)

Declared mechanisms: actual XGBoost LightGBM and CatBoost execution, common group splits and equal candidate count, native categorical and numeric missing contracts, growth and leaf-count resource boundaries.

```bash
python scripts/run_notebook.py notebooks/090_Chapter_18_04_Native_Boosters_Identical_Group_Protocol.ipynb
```

## 18.5 · Stacking, blending and hybrid ensembles

- [Train a meta-model on predictions made without each target](notebooks/091_Chapter_18_05_OOF_Tree_Linear_Neural_Stack.ipynb#stack)
- [A soft-routing candidate needs its own evidence](notebooks/091_Chapter_18_05_OOF_Tree_Linear_Neural_Stack.ipynb#soft)

Declared mechanisms: entire-pipeline out-of-fold base predictions, boosted tree ridge and trained neural base learners, honest holdout blending versus full-memory deployment, soft-routing candidate as a scoped mechanism.

```bash
python scripts/run_notebook.py notebooks/091_Chapter_18_05_OOF_Tree_Linear_Neural_Stack.ipynb
```

## 18.6 · Constraints, distributions and practical tradeoffs

- [Compare targets and constraints on their own losses](notebooks/092_Chapter_18_06_Monotone_Quantiles_And_Cost_Audit.ipynb#quantiles)
- [Check constraints and a defined stored-array budget](notebooks/092_Chapter_18_06_Monotone_Quantiles_And_Cost_Audit.ipynb#audit)

Declared mechanisms: monotonic and additive interaction constraints, separate mean and quantile loss targets, coverage crossings and support challenges, version-specific tree-array resource ledger.

```bash
python scripts/run_notebook.py notebooks/092_Chapter_18_06_Monotone_Quantiles_And_Cost_Audit.ipynb
```

## Interpretation and boundaries

Chapter18 has six original numbered sections, not five. The original code_001 notebook and its manifest record remain byte-for-byte unchanged. It reran independently into ignored build/chapter18-original001.executed.ipynb:21code cells/19inline figures,3.010s including kernel lifecycle, same selected depth6/minleaf20 and identical final metrics (balanced accuracy.933333, Brier.0550442,logloss.635775 on360final cases). The preserved manifest retains its historical3.011s publication evidence; the new rerun is reported separately rather than rewriting an old record.

Six new self-contained laboratories087–092 use seeds1887–1892,24code cells and12inline figures. Together the seven chapter notebooks supply45executed cells/31figures. The core Python3.14.3/NumPy2.4.4/SciPy1.17.1/pandas3.0.3/Matplotlib3.11.0/sklearn1.9.0 versions are unchanged. The native comparison adds pinned CPU XGBoost3.4.1,LightGBM4.7.0 andCatBoost1.2.10; graphviz.21 andplotly7.1.0 are their added dependencies. Existing threadpoolctl3.7.0 limits loaded numerical thread pools; native library thread controls are explicitly1. All inputs/helpers are internal and ordinary runs are offline. Package installation is a setup step, not a notebook cell. Initial087–091runs passed.092first failed an unmatched-parenthesis syntax error; after repair its actual monotonicity assertion failed for raw quantile predictions. That behavioral failure is retained and the final explicitly projected algorithm is described below.091reran to shorten diagram text after book-vector review found spill beyond boxes.092reran after projection/coverage naming clarified the actual fitted target. No warning is suppressed; final outputs contain no solver warnings or error outputs. Numerical result dictionaries stay identical across layout-only reruns; the092coverage-key rename is an explicitly semantic metadata change.

087supplements the complete original constructor/pruning lab. It generates320training/200final Bernoulli records with correlated load measurements and resistance. Fixed depth2/minleaf12 query[.7,.7,.3] follows load threshold.654788 and resistance.292261 toleaf6with75training rows and class-one fraction1/3. Weighted-mass root impurity decrease.0499680 is verified, along with actual path/leaf probabilities. Final Brier.170151 is a fixed-model diagnostic. Forty prescribed perturbations each flip8training labels; root-feature counts[24,16,0], query probabilities.290909–.625 and root thresholds.497744–.654788. No perturbation selects another deployed model. Separate numeric-missing fixture learns the right branch with probability1; a training-only one-hot material encoder maps unseenpolymer toallzeros. These are different contracts and do not imply native categorical support or physical validity. The versioned missing_go_to_left field is disclosed as internal storage.

088independent member fixture train240/dev120(diagnostic only)/final240has six descriptors and correlated firsttwo(.998675). Fixed deep tree/bag80/RF80/Extra80 final MSE .258810/.152220/.142916/.133614. Forest and Extra use max_features.5; bag/forest bootstrap, Extra doesnot. Direct constituent average equals bag prediction. Mean within-bag pair prediction correlation across queries.848997 is not substituted for fixed-query repeated-fit correlation. A separate24bootstrap-refit sensitivity audit gives mean query variance .115604single vs.0246683bag30. Bag80/RF80 OOB MSE .156174/.149110 is appropriate to the independent-row fixture. Deliberately dependent30buildings×8rows share random building labels and an asset-coordinate identity proxy: OOB accuracy.908333 vs20new-building accuracy.43125; all7050omitted-row/tree pairs retain a training sibling. This is a counterexample to an unseen-entity interpretation, not realistic failure evidence.

089thirty-point toy starts mean.345900, then fits two depth1residual corrections with rate.5; training MSE .409355→.183625→.112740. Residual-update identity and a logistic negative-gradient finite difference(.331812) pass. Separate manually specified binary exponential-loss AdaBoost rounds use weighted errors.125/.190476, alpha.972955/.723459 and normalized error mass.5each. This is not a coefficient-normalization claim for every library variant. Independent regression train160/dev100/final200selects200of[20,80,200]stages by development MSE, fixed depth2/minleaf5/rate.1. Development.0713936/final.0638595. Final is not reused to extend the endpoint grid.

090executes all three native libraries on exactly the same60building×8row fixture.45development buildings360rows and15final buildings120rows are disjoint; the same3GroupKFold masks each hold out15buildings120rows from30buildings240rows. Each library gets2depth candidates[3,5]×3fold fits+1full-development selected refit,80rounds/rate.1/thread1/noearlystop. Predeclared materials steel/concrete/timber/missing/unknown retain semantic identities;92development numeric load readings areNaN. Group ID is excluded from features. XGBhist/depthwise/reg_lambda1, LGBleafwise/maxdepth/numleaves2**depth/minchild10/reg_lambda1, CatBoostOrdered/SymmetricTree/l2_leaf_reg1 are executed, with other interface defaults preserved. Equal candidate count is not equal wall time, effective regularization or exhaustive tuning. All selectdepth3. Final XGB/LGB/Cat logloss .624030/.630004/.612130;Brier .216987/.220302/.212960;accuracy.65/.641667/.65.80trees each have536/503/524terminal leaves, not measured latency. Target-free ordinary/missingload/unseenmaterial-mapped-unknown probes all predict finitely and differently; unknown has no training examples. No universal ranking or field probability validity follows. Live XGBdocs3.4.2 vs execution3.4.1 and sklearndocs1.9.1 vs1.9.0 are disclosed; LGB4.7.0 matches inspected documentation.

091generates train180/dev80/final200, four normal features with nonlinear response. Base learners HGB60rounds/leaf7/minleaf10, standardized Ridge1, standardized trained MLP12tanh/LBFGS/alpha.1/maxiter2000 are fixed. Five folds fit entire pipelines inside144memory/36query boundaries; each target gets exactly one OOFprediction row, overlap0. Meta Ridge[.1,1,10] is chosen by development, with head fitting on OOFfeatures only; full bases refit180training cases for deployment. Selected meta10coeff[.097178,.064612,.908408],intercept-.061435. Final boosted/Ridge/neural MSE .319915/1.210945/.0723998, uniform mean.193206, OOFstack.0706745. The small improvement over neural is finite evidence, not a dominance guarantee. Neural in-sample MSE.0236907 vs OOF.194787 exposes invalid meta-training optimism. Full neural fit723iterations with no optimizer warning. Honestblend uses120base/60head disjoint records and retains120-case bases at deployment, finalMSE.180447. Separate original softstump uses fixed sigmoid4x0, only twoleafvalues fit; derivative/prediction identities pass but finalMSE1.262113. No trained deep differentiable forest is claimed.

092train500/dev160/final400/future60uses y=5+3load+sin2piT+NormalSD(.2+.8load), source load/T[0,1], future load[1.2,1.6]. Unrestricted mean, native constrained mean and explicit projected q.1/.9 each selectleaf7of[7,15]using their own devMSE/pinball,120rounds/rate.08/minleaf15/earlystopFalse. Constrained base fits request monotone[1,0]/interaction[{0},{1}]. Actual raw quantile monotonicity fails in pinned1.9.0; selected201point-grid minimum increments-.00417704/-.10078409 are reported. Installed/versioned _update_leaves_values source re-estimates non-smooth-loss leaves; direct prediction checks, not parameter names, supply the failed-behavior evidence. No claim that every version fails is made. Final quantile wrapper projects fixed201load-grid model predictions attemperature.5 with increasing isotonic interpolation/out-of-bounds clipping, then adds the base's additive temperature component anchored atload.5. It uses model predictions only, no dev/final targets, and is applied to every candidate BEFOREdevpinballselection. Additive form establishes the wrapper's interaction restriction; increasing interpolation establishes load monotonicity. Finite81point×5temperature and four-corner checks verify implementation. Native constrained mean passes without projection. This explicit output transformation changes the raw quantile estimate; it is not called native monotonic quantile success.

092final unrestricted/constrained mean MSE .469840/.446708. Projected q.1/.9pinball .113289/.119848; fractionsbelow .1375/.8575, central projected interval coverage.72, upper exceedance.1425, crossings0. There is no final-outcome interval repair/calibration. Future meanMSE3.634464/3.471480, upperpinball.715713 shows unsupported extension despite monotonicity. A separately frozen80recordtemperature.25slice supplies plotted observations at the same conditioning value. Each fitted base has120prediction trees. Version-specific node arrays count1560/1560/1488/1524nodes,840/840/804/822leaves,87360/87360/83328/85344bytes plus0/0/944/1008isotonic threshold-array bytes. Other model arrays, Python/binning/workspaces/processRSS are excluded. This is not full model memory or a timing benchmark.

Twelve original vector figure sets implement both original briefs: actual tree path then varied-tree averaging; baseline plus two residual corrections contrasted with out-of-fold stacking information arrows. Four numbered equations and twelve exercises cover the six exact scopes. Primary official tree/forest/boosting/HGB and XGB/LightGBM/CatBoost documentation, plus pinned1.9.0 leaf-update source, were inspected20October2026. Mechanism correctness, empirical prediction loss, output constraints, uncertainty evidence and defined computation costs remain separate claims.
