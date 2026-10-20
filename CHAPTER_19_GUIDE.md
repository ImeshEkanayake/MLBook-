# Chapter 19: Clustering and anomaly detection — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_19_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 19.1 · Centroid and mixture-based clustering

- [Specify what a group should optimize](notebooks/093_Chapter_19_01_Centroids_Medoids_And_Mixture_Responsibilities.ipynb#objectives)
- [Units and initialization affect the specified objective](notebooks/093_Chapter_19_01_Centroids_Medoids_And_Mixture_Responsibilities.ipynb#sensitivity)

Declared mechanisms: Euclidean centroid versus observed-case medoid objectives, full versus spherical mixture assumptions, unit scaling and initialization sensitivity, model responsibilities versus external regime evidence.

```bash
python scripts/run_notebook.py notebooks/093_Chapter_19_01_Centroids_Medoids_And_Mixture_Responsibilities.ipynb
```

## 19.2 · Hierarchical, density and graph clustering

- [Different cluster definitions on exactly the same records](notebooks/094_Chapter_19_02_Shapes_Densities_And_Connectivity.ipynb#partitions)
- [Density parameters and boundary records remain choices](notebooks/094_Chapter_19_02_Shapes_Densities_And_Connectivity.ipynb#boundaries)

Declared mechanisms: same-point centroid hierarchy density and spectral partitions, native HDBSCAN density hierarchy, noise labels and scale controls, boundary sensitivity without comparing arbitrary label IDs.

```bash
python scripts/run_notebook.py notebooks/094_Chapter_19_02_Shapes_Densities_And_Connectivity.ipynb
```

## 19.3 · Evaluating discovered groups

- [Ask three different evaluation questions](notebooks/095_Chapter_19_03_Stability_Separation_And_Downstream_Utility.ipynb#evaluation)
- [Resample measurements while preserving record identity](notebooks/095_Chapter_19_03_Stability_Separation_And_Downstream_Utility.ipynb#resampling)

Declared mechanisms: internal separation versus external agreement, training-only clustering in downstream prediction, sensor resampling and permutation-invariant stability, development selection without final interpretation tuning.

```bash
python scripts/run_notebook.py notebooks/095_Chapter_19_03_Stability_Separation_And_Downstream_Utility.ipynb
```

## 19.4 · Point anomalies, novelty and density scores

- [A score defines unusualness relative to a reference](notebooks/096_Chapter_19_04_Reference_Scores_And_Valid_Rarity.ipynb#scores)
- [Rarity, invalidity and review labels are different claims](notebooks/096_Chapter_19_04_Reference_Scores_And_Valid_Rarity.ipynb#alarms)

Declared mechanisms: marginal versus joint unusualness, robust covariance isolation local density and one-class boundaries, LOF novelty-only scoring contract, calibration thresholds versus rare valid observations.

```bash
python scripts/run_notebook.py notebooks/096_Chapter_19_04_Reference_Scores_And_Valid_Rarity.ipynb
```

## 19.5 · Contextual and structured anomalies

- [A locally inconsistent connection can be globally ordinary](notebooks/097_Chapter_19_05_Graph_Context_Sequence_And_Alarm_Burden.ipynb#context)
- [Distinguish point flags, sequential alerts and selective review](notebooks/097_Chapter_19_05_Graph_Context_Sequence_And_Alarm_Burden.ipynb#timing)

Declared mechanisms: contemporaneous graph residual versus common-mode extremes, training-only PCA reconstruction and reference contamination, calibration thresholds sequential delay and alarm burden, selective review with unreviewed cases kept unknown.

```bash
python scripts/run_notebook.py notebooks/097_Chapter_19_05_Graph_Context_Sequence_And_Alarm_Burden.ipynb
```

## Interpretation and boundaries

Five self-contained CPU laboratories093–097use seeds1993–1997,20code cells and10inline figures. Core Python3.14.3/NumPy2.4.4/SciPy1.17.1/pandas3.0.3/Matplotlib3.11.0/sklearn1.9.0 versions and dependencies are unchanged from Chapter18. Already-pinned threadpoolctl3.7.0 explicitly limits numerical pools toone thread; native sklearnHDBSCAN needs no additional package. All numerical records are generated internally; ordinary execution is offline without files, credentials or GPU. Initial093–096runs passed, with a094FutureWarning about the upcoming HDBSCANcopy default. Its final explicit copy=True preserves inputs and removes that warning without suppression. Initial097computed its experiments but failed its summary because a plotting variable namedtime shadowed the timing module; renaming itminutes and rerunning the entire notebook repaired the execution. Visual review then shortened clipped axis labels in093/095/097, simplified094boundary labels to four examples while retaining eight in the results, and separated density tick labels. Layout-only reruns preserve exact numerical result dictionaries. Final outputs contain no errors or solver warnings. Synthetic annotations make validity and event audits possible here; field completeness and physical or causal interpretation are not asserted.

093generates independent train240/development80/final200from2Gaussian components with means[-2,0]/[2,.5],covariances[[2,1.25],[1.25,1]]/[[1,-.65],[-.65,1.5]],prior.5. Fixed2groups compare objectives rather than selecting count from final annotations. Training-onlyStandardScaler precedes KMeans20starts, full/sphericalGaussianMixture5starts/regcov1e-4, and manually specified alternatingEuclideanmedoids12starts. The medoid heuristic is local, not a global PAM solver; selected medoids are actual training IDs64/68. Selected medoid distance history359.908→215.388→206.955→202.553 is nonincreasing; kmeans squared-distance sum244.744 is a different objective. Final generator-component ARI KMeans.369334/medoids.433019/fullmixture.791060/sphericalmixture.134189. Full/spherical final mean logdensity -2.319978/-2.772793 in standardized coordinates, development -2.196694/-2.629759. Densities are not attached to centroid/medoid objectives. Responsibilities sumtoone, meanmax.964159 and fractionmax<.8 .065; not verified operating truth. All12single-startkmeans seeds reach the same objective244.743614 and same partition: retain this absence of observed initialization instability. Raw storage scaling[1000,1]versus standardized partition ARI.794191; consistently trained scaling after unit conversion restoresARI1. Fitted ellipses are one-covariance contours, not mean confidence intervals.

094uses exactly260transductive analysis points:180densemoonnoiseSD.04/60sparsemoonnoiseSD.08/20uniformbackground. Declared original dimensionless coordinate geometry is fixed, no target-driven parameter search. KMeans2/Ward2/singlelinkage2/DBSCANeps.18,min_samples7/nativeHDBSCANminsize20,min_samples7,copyTrue/spectral2denseRBFgamma8precomputedcluster_qr use the samepointset. Counts clusters/noise respectively2/0,2/0,2/0,6/17,2/24,2/0. ARI on known moon records .163408/.231146/0/.895463/.957673/.374844; all-record ARI also reported. Sparse/background provenance is not identical to algorithmic noise. Fixed spectral performance is retained, not retuned to a desired picture. DBSCANeps.12/.18/.30 gives3/6/3clusters and noise fractions.211538/.065385/.030769;HDBminsize12/20/40 gives3/2/2clusters and.042308/.092308/.092308noise. NativeHDBminimum samples counts itself, not asserted equivalent to contrib defaults. Twentycoordinate-jitterSD.025DBSCANrefits have meanARI.973249/min.948183;case213/231clustered10of20 despite highaggregateagreement. Eightboundary-sensitive IDs anddenominators are retained;fourlabelledillustrations avoid collisions. No new-query contract is claimed for all transductive methods.

095generates train300/dev100/final200,3operatingGaussianregimes and4redundant noisy sensors with separately generated Bernoulli fault targets. Training-onlyScaler/KMeansK2/3/5 uses no targets. FixedC1logistic fits raw sensors orrawplusclusterindicators; developmentBrier selectsK3. K2/3/5training silhouette .471428/.629582/.431422 and generator-regimeARI .583047/.961994/.696761 are separate audits. Final raw-baselineBrier .143206/logloss.441282;cluster-augmentedK2/3/5Brier .145857/.146014/.145397,logloss.447203/.448492/.450705. Thus the selected stable/regime-matching clusters do not improve the final fault predictor in this realization. No final retuning occurs. Twenty completeScaler/KMeanssensor-noiseSD.15refits perK preserve case IDs; meanARI .990610/.986421/.796752,min .973238/.950625/.559064. Selected training cluster×generatorregime contingency[[3,95,0],[94,1,0],[0,0,107]]retains300counts. ClusterlabelpermutationARI1asserts identityinvariance. No physical fault mechanism or independent review interpretation is inferred from generator agreement.

096admitted reference480centralrho.95bivariateGaussian+20rarevalidnear[5,5],independentcal240central+10rarevalid(same4%fraction). Final diagnostic cohorts200central/20rarevalid/20isolated-loadnear[4.5,0]/20unusual-combinationnear[1.8,-1.8]have declared provenance, not population-prevalence estimates. Training-onlystandardization precedes marginalmedian/MAD,maxabsolutez;robustMinCovDetMahalanobis(supportfraction.85);IsolationForest100;LOF20noveltyTrue;OneClassSVMnu.05/gammascale;GMM2full5starts/regcov1e-4neglogdensity. Scores are orientedhigh=unusual, not anomaly probabilities. LOFscore_samples is called onlyonnewcal/final, neverfittingrecords. Each independent250recordcal95thpercentile threshold has strict empiricalalarmfraction.052(13/250), not an exact5%guarantee. Finalcentral/rarevalid/isolated/joint alarm counts: MAD2/20/20/0;robustcov5/20/20/20;isolation1/17/19/1;LOF9/0/20/20;oneclass11/8/20/20;mixture8/6/20/20. Denominators200/20/20/20remainvisible. Rare valid rejection exposes reference/score assumptions; lowdensity is not automatically error or damage. Density coordinates and nonuniform task definitions are disclosed. No method is crowned universally best.

097uses ring10connections with row-normalized symmetric neighborweights.5.80admitted reference/80independentcal/120finalsteps arefive minutes apart; readings2commonload+nodeoffset+commonambient+.03independentnoise. Finalconnection4has+.3implantsteps50–59atload.8;validcommonload1.5steps80–89raisesall10sensors. Contemporaneous neighbor readings are assumed available; no future reading enters point scores. Clean-referenceglobalrawz/graphcontrastz/PCA1reconstructionresidualz use independentcal99thpercentile across800sensorchecks. These are not800independentepisodes. Over1190normalfinalsensorchecks and10operatinghours, clean global/graph/PCA detect8/10/10of10eventpoints with103/41/24falsepointflags,10.3/4.1/2.4falseflags/hour. Validextremewindow flags100/2/1of100checks. Graph flags can spread to adjacentconnections. Snapshotstep55rawmean1.695839,max|contextz|8.725923;step85validhighermean2.919871,max1.946249. Grayscale signedz/nodeIDs/star4make the distinction explicit.

097contamination injects+.3intonode4in30of80reference steps, refits only declared scorers and recalibrates on the same clean calibration. Allthree then detect0of10eventpoints;falsepointflags106/21/21 and validextremewindow100/2/2. Fewerfalseflags undergraph/PCA accompanies complete masking, not improvement. A clean-reference one-sidedCUSUMnode4 usesdrift.5,h=max(5,maxcalunresetstat)=5,resetonalarmand skipsnext5steps. Alerts50/56bothinevent, firstdelay0minutes at5-minute resolution, nofalsealerts inthisfinite10hwindow;no long-run rate orinstantaneousguarantee. Pointflag, sequentialalert andoperatingepisode denominators remain different. Selectivereview sorts51clean graph flagsbyscoreandreviews everysecond:26reviewed,oracle5true/21false,25unreviewedunknown,reviewedprecision.192308. Unknowns never become assumed true negatives, and reviewfeedback doesnotretunethisassessment.

Ten original vector figure sets implement both original briefs: same-point centroid/density/connectivity partitions, and a locally inconsistent connection versus a globally extreme valid common-load regime. Six numbered equations andtwelveexercises cover the five exact scopes. Official clustering/mixture/HDBSCAN/spectral/novelty references and NIST's CUSUM handbook were inspected20October2026. Live sklearn1.9.1 documentation differs from executed1.9.0. No literature completeness, field validity, causal diagnosis or universal false-alarm control is asserted.
