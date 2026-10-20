# Chapter 20 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. Added pinned umap-learn 0.5.12, PyTorch 2.14.1 and ipywidgets 8.1.9 with recorded transitive dependencies, while retaining all prior numerical core versions. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_098 | 20.1 | 4 | 2 | 1.561 |
| code_099 | 20.2 | 4 | 2 | 8.489 |
| code_100 | 20.3 | 4 | 2 | 1.435 |
| code_101 | 20.4 | 4 | 2 | 2.773 |
| code_102 | 20.5 | 4 | 2 | 3.256 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. All ten inline notebook figures and ten vector book figure sets were visually inspected, with current-chapter and front/reference page review completed for the accepted PDF revision.

## Actual mechanisms and boundaries

Five self-contained generated-data laboratories098–102use seeds2098–2102,20code cells and10inline figures. CPU execution remains Python3.14.3,NumPy2.4.4,SciPy1.17.1,pandas3.0.3,Matplotlib3.11.0,sklearn1.9.0. Added pinned umap-learn0.5.12,torch2.14.1 and ipywidgets8.1.9 under the previous lock's constraints; the numerical core is unchanged. New transitive pins include numba0.68.0,llvmlite0.50.0,pynndescent0.6.0,tqdm4.70.1 and the PyTorch/widget dependencies in requirements-lock.txt. NumPy numerical pools/Numba/PyTorch use one CPU thread; neural fits use explicit seeds, float64 and deterministic algorithms. No ordinary-run files, network, credentials or GPU. All new source cells passed syntax checking before execution; an initial source-builder quoting error was repaired before notebook099execution.

All five initial kernels completed their experiments and assertions. The initial099run printed a tqdm IProgress warning; installing and pinning ipywidgets repaired its actual missing display dependency, without warning suppression. Figure reproduction caught a roughly1e-9distance-rank-correlation difference from Isomap's automatic eigensolver, not UMAP; explicit eigen_solver='dense' and a full fresh-kernel099rerun removed that discrepancy. Final outputs contain no errors or stderr warnings. Visual review then changed098latent axes to paired displacements in explicitly scaled units, shortened100warm/cold ticks and101model ticks. A second figure review further abbreviated warm/cold and model labels and removed a scientific-offset label collision. A minor TeX line overflow was repaired by rephrasing the current chapter. Layout-only reruns preserve exact numerical RESULT dictionaries. All ten vector figure sets reproduce exact fresh-kernel results, not rounded tolerances. Reproducibility is bounded to this pinned CPU environment, not promised across hardware/releases.

098generates train300/dev80/final200positive three-channel energies: independent exponential sources mixed by[[1,.8,.4],[.2,1,1.3]],offset1,noiseSD.02;independentbinarypattern.1v, vunitorthogonalto mixing rows[.39663665,-.75608862,.52058560]. PCA2fullSVD centers but does not standardize; explicit centeredSVD reconstruction and manualprojection agree. NMF2initnndsvda/tol1e-5/maxiter2000seesuncenteredpositiveoffset, so rank/objective allocation differs;coefficients/basis nonnegative. ICA2unitvariancewhiten/svd/tol1e-5/maxiter2000takes6iterations;NMF421. FinalMSE PCA/ICA.001028964,NMF.004172736,dev.000975521/.004310846. PCAexplainedvariance.999329677. Lockednoiselesscounterfactualpair.1v retainsnormfraction.001735868 afterPCAreconstruction; notexactzero and notfielddamagecausality. ICArotationofsamePCA2subspace hasidentical reconstruction. Nonnegative parts andindependentsource identification assumptions remain distinct; no ranking of physicalinterpretability.

099uses600Swissrollpoints,noise.05,analysis-cohortStandardScaler;declared transductiveexploration,notprospectivevalidation. Intrinsic rollpositiononlygrayscaleannotation. FixedPCA2,Isomap12denseeigensolver,tSNEperplexity10/50(maxiter500,pca-init,learningrateauto),actualUMAPneighbors10/50(min_dist.1,n_epochs200,random_state/transform_seed2099,n_jobs1). Top10inputEuclideanneighborrecall .477833/.366/.798833/.838/.760667/.7595 respectively;trustworthiness .868869/.901342/.997764/.998170/.996968/.996846. Global inputdistance-rankcorrelation assesses999nonidentical pairs drawn beforefits, nothiddengeodesictruth; unrolling can reduce this metric. A fixedper-displayStandardScaler+DBSCANeps.3,min5 gives2/1/3/2/3/3groups,onlyPCAoneof600noise. No finalorannotationdrivenparametersearch;UMAPboth3retained. TwentyseparatenewSwissrollqueries transform throughfittedUMAP10tofinite20×2coordinates. This sklearnTSNE hasno transform. UMAPlive docsheading0.5.8 differs from executed0.5.12;sklearnmaintenance1.9.1 differs fromexecuted1.9.0. No independentclusteroroperatingregimeproof.

100generates50buildings×8membertypes with3descriptors,latentU=descriptors@[[1,.2],[-.3,.8],[.6,-.4]]+noiseSD.15,Vnormal, response3+UV^T+noiseSD.1. First36buildings have exactly4observedcells each (144),144otherwarmcellswithheld;7entiredevelopmentbuildings and7finalcoldbuildings. Maskedrank2ALS80updates,ridge.1,globalmeancoordinateupdate,objective150.163361→5.279290nonincreasing. Response labels fit factors, not unlabeled pretraining. WarmmissingMSE.0288865; coldIDglobalmeanfallback.9009942. Training-onlydescriptorScaler+Ridgeα.1/1/10mapsdescriptorsto fittedU;devMSE.0469774/.0511719/.1282558selects.1,finalcoldMSE.04986697. Alltypesalreadyhavefitcells;notnewtypeassessment. Coldfinalresponse labels neverfitU/mapping. Separate12nodecyclecombinatorialLaplacianusesfirst2nonconstanteigenvectors,allknownnodes/edges;orthogonalrotationGrammaxerror5.55e-17. No rowexistsfornewnode12. Thistransductivelookupdoesnotinheritbuildingmapper'sinductivecontract;factor/graphaxesnotuniquelyphysical.

101generates32samplewindows with2orthonormaldominantsin/cosmodes,normalamplitudesSD1.5,independentbinarypresence.15orthogonalalternatinglocalpattern,measurementnoiseSD.02. Train300/dev80/final200;trainingmeancenteringonly. PCA2,linearAE32→2→32(162params),nonlinearAE32→8tanh→2tanh→8tanh→32(594params),denoisingsamearchitecture. Fixed800fullbatchAdamsteps,rate.01,weightdecay1e-4;denoisingfreshnoiseSD.08targetstheoriginalobservedtrainmeasurement,nothiddennoiselessoracle. Identity usesall32coordinates andzero self-reconstructionloss. FinalmeasurementMSE Identity0/PCA.000553624/linear.000556396/nonlinear.001231921/denoising.001213648. Patternretainednormfractions1/.00300827/.00549687/.14903025/.04828362;notfielddamageproof. IndependentfinalinputcorruptionSD.08againstoriginalmeasurementMSE .00641755/.000995554/.001009783/.002033482/.001670341. DenoisingimprovesitsnonlinearcounterpartbutdoesnotbeatPCAhere. SeparatehiddennoiselessoracleMSE .000399614/.000206030/.000208213/.000865666/.000854960 isgenerator-onlyevidence. GaussianKLanalyticstandardnormal0andunitmeanshift1asserted;noVAE/generativefit. Fixedbudget/finitegradientsdonotcertifyglobaloptimum.

102uses50buildings×8windows,wholebuildingtrain30/dev10/final10(240/80/80records);building-specificdominantsin/cosamplitudespluswithinbuildingnoise, independentbinarylabelpolarity±.15pattern,measurementnoiseSD.02. This signedtargetdiffersfrom101presence. Unlabeledpretraininginputs/mean/PCA/AEsourceonly,novelbuildinginputsnotused. AEarchitecture32→8tanh→2tanh→8tanh→32,800Adamsteps/.01/weightdecay1e-4. Sourceonlyfeaturestandardizersfitraw32/PCA2/frozenAE2/signedfilter/absolute-filter;fixedC1Logisticprobes maxiter1000. Threefixednestedordersof3/10/30wholetrainingbuildings supply24/80/240labelseach,sharedallmethods. Developmentdiagnostic,nocandidateselection;allfixedcandidatesassessed. Actualfine-tuningcopiesencoder+newbinaryhead,400Adamsteps/.01/weightdecay1e-3/BCEWithLogitsLoss;encoderparameterchangesnorm5.12–5.35assertednonzero. Total54candidate/budget/orderassessments. FinalAEreconstructionMSE.001919571/PCA.001120034doesnotpredictprobeutility.

102full240labelmeanBrier PCA.24881786/frozenAE.24880159/raw.00415667/signedfilter.000345954/fine-tune.000149586/absolutefilter.249937875. Accuracies .5/.5/1/1/1/.5125. Fine-tuneall9fitsachievefinite80-caseaccuracy1even24labels;retaineasyconstructedsignal,noextrapolationtofieldreliability. At24labelsmeanBrier raw.114428/signed.0104334/fine-tune.00124571/PCA.272541/frozen.271477/absolute.266863. Matchedsignedfilterknowsgeneratorpattern,aprivilegeddomainprior;absolute-valueinvarianceerasespolarity. RepeatsSDmeasurethreebuildingordersandnewheadseeds,notpopulationCI;fullbudgetfrozenprobesidentical,headseedfine-tunesvary. Nofrom-scratchneuralcomparator,sofine-tuninggaindoesnotprovenecessityofpretraining. Nofoundationmodel,causaldamageorfieldtransferclaim.

Tenoriginalvectorfiguresimplementbothoutlinebriefs: threechannels→two-coordinatecompression→lostsmallpattern,andunlabeledencoder/labeledprobeinformationboundaries. Four numbered equations andtwelveexercisescoverthefiveexactscopes. Primarysourcesinspected20October2026: sklearn1.9decomposition/TSNE,originalvan der Maaten/Hinton2008,UMAPparameters/transform,PyTorch2.14reproducibility/BCEWithLogitsLoss. The manuscript's experiments and diagrams are original; bibliography cites versioned implementation assumptions rather than claiming exhaustive literature coverage.

Final page review moved the label-budget figure after its interpretation, keeping the closing practice material more evenly distributed. References use a readable nine-point size to avoid a single bibliography entry stranded on a separate page. All earlier chapter body pages retain their original layout. The final render and preservation checks use the accepted PDF revision.

## Successful result dictionaries

### code_098

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 2098.

```json
{
  "explained_variance_fraction": 0.999329677432988,
  "ica_iterations": 6,
  "metrics": [
    {
      "development_MSE": 0.0009755213914827486,
      "final_MSE": 0.0010289636611159616,
      "method": "PCA",
      "train_MSE": 0.000986242129132029
    },
    {
      "development_MSE": 0.004310845959388441,
      "final_MSE": 0.004172736393385739,
      "method": "NMF",
      "train_MSE": 0.0033621249875766352
    },
    {
      "development_MSE": 0.0009755213914827463,
      "final_MSE": 0.001028963661115962,
      "method": "ICA",
      "train_MSE": 0.000986242129132029
    }
  ],
  "nmf_iterations": 421,
  "pattern_retained_fraction": 0.0017358678171519022,
  "pattern_vector": [
    0.3966366510671125,
    -0.7560886160966829,
    0.5205856045255848
  ],
  "split_sizes": [
    300,
    80,
    200
  ]
}
```

### code_099

Versions: `{"matplotlib": "3.11.0", "numba": "0.68.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "umap": "0.5.12"}`; Darwin arm64 CPU; seed 2099.

```json
{
  "cohort_size": 600,
  "metrics": [
    {
      "display_groups": 2,
      "display_noise_fraction": 0.0016666666666666668,
      "method": "PCA",
      "neighbor_recall": 0.47783333333333333,
      "pair_rank_correlation": 0.8086182648355413,
      "trustworthiness": 0.8688685486170515
    },
    {
      "display_groups": 1,
      "display_noise_fraction": 0.0,
      "method": "Isomap k=12",
      "neighbor_recall": 0.366,
      "pair_rank_correlation": 0.3533513895860874,
      "trustworthiness": 0.9013416025092672
    },
    {
      "display_groups": 3,
      "display_noise_fraction": 0.0,
      "method": "t-SNE p=10",
      "neighbor_recall": 0.7988333333333333,
      "pair_rank_correlation": 0.36630214623002333,
      "trustworthiness": 0.9977644710578842
    },
    {
      "display_groups": 2,
      "display_noise_fraction": 0.0,
      "method": "t-SNE p=50",
      "neighbor_recall": 0.8380000000000001,
      "pair_rank_correlation": 0.7052699838748968,
      "trustworthiness": 0.9981702309666382
    },
    {
      "display_groups": 3,
      "display_noise_fraction": 0.0,
      "method": "UMAP k=10",
      "neighbor_recall": 0.7606666666666666,
      "pair_rank_correlation": 0.3259783871163154,
      "trustworthiness": 0.9969683490162532
    },
    {
      "display_groups": 3,
      "display_noise_fraction": 0.0,
      "method": "UMAP k=50",
      "neighbor_recall": 0.7595,
      "pair_rank_correlation": 0.6424381452687735,
      "trustworthiness": 0.9968463073852295
    }
  ],
  "new_umap_shape": [
    20,
    2
  ],
  "pair_count": 999
}
```

### code_100

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 2100.

```json
{
  "cold_ID_fallback_MSE": 0.9009941852417638,
  "cold_descriptor_MSE": 0.04986697027046933,
  "development": [
    {
      "alpha": 0.1,
      "development_MSE": 0.046977415284414105
    },
    {
      "alpha": 1.0,
      "development_MSE": 0.05117193173785776
    },
    {
      "alpha": 10.0,
      "development_MSE": 0.12825581795720656
    }
  ],
  "graph_eigenvalues": [
    5.5511151231255886e-17,
    0.26794919243112214,
    0.26794919243112225,
    0.9999999999999996
  ],
  "graph_nodes": 12,
  "objective_final": 5.279290273783243,
  "objective_initial": 150.16336120882713,
  "observed_cells": 144,
  "rotation_gram_max_error": 5.551115123125783e-17,
  "selected_alpha": 0.1,
  "split_buildings": [
    36,
    7,
    7
  ],
  "warm_missing_MSE": 0.028886502376827747,
  "warm_missing_cells": 144
}
```

### code_101

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2101.

```json
{
  "gaussian_KL_shift_example": 1.0,
  "metrics": [
    {
      "corrupted_input_MSE": 0.006417549669590323,
      "development_MSE": 0.0,
      "final_measurement_MSE": 0.0,
      "method": "Identity",
      "noiseless_oracle_MSE": 0.00039961365989749244,
      "pattern_retained_fraction": 1.0
    },
    {
      "corrupted_input_MSE": 0.0009955537459705793,
      "development_MSE": 0.0005342337001933694,
      "final_measurement_MSE": 0.0005536244545914369,
      "method": "PCA",
      "noiseless_oracle_MSE": 0.00020602991637269508,
      "pattern_retained_fraction": 0.0030082680073932216
    },
    {
      "corrupted_input_MSE": 0.0010097826815586954,
      "development_MSE": 0.0005365498864991363,
      "final_measurement_MSE": 0.0005563961224612249,
      "method": "Linear AE",
      "noiseless_oracle_MSE": 0.00020821293439969604,
      "pattern_retained_fraction": 0.005496867608636132
    },
    {
      "corrupted_input_MSE": 0.002033482441993343,
      "development_MSE": 0.0019780221375607417,
      "final_measurement_MSE": 0.0012319211955596214,
      "method": "Nonlinear AE",
      "noiseless_oracle_MSE": 0.0008656657229566495,
      "pattern_retained_fraction": 0.1490302495169994
    },
    {
      "corrupted_input_MSE": 0.0016703408781629642,
      "development_MSE": 0.0019154501601822162,
      "final_measurement_MSE": 0.0012136475550361266,
      "method": "Denoising AE",
      "noiseless_oracle_MSE": 0.0008549602238951451,
      "pattern_retained_fraction": 0.04828362288929928
    }
  ],
  "parameter_counts": {
    "Denoising AE": 594,
    "Linear AE": 162,
    "Nonlinear AE": 594
  },
  "split_sizes": [
    300,
    80,
    200
  ],
  "training_steps": 800
}
```

### code_102

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2102.

```json
{
  "encoder_parameter_changes": [
    5.346457854349838,
    5.130658242586451,
    5.256875916498482,
    5.227090391732023,
    5.306906668002642,
    5.283706870021827,
    5.312715771748238,
    5.3325501863703595,
    5.118777495833457
  ],
  "final_AE_reconstruction_MSE": 0.0019195714587805334,
  "final_PCA_reconstruction_MSE": 0.001120034132266834,
  "fine_tuning_steps": 400,
  "individual_runs": [
    {
      "development_Brier": 0.010846043789495071,
      "final_Brier": 0.009548218155985798,
      "final_accuracy": 1.0,
      "labels": 24,
      "method": "Signed filter",
      "replicate": 0
    },
    {
      "development_Brier": 0.0863966107693471,
      "final_Brier": 0.06332780196676599,
      "final_accuracy": 1.0,
      "labels": 24,
      "method": "Raw window",
      "replicate": 0
    },
    {
      "development_Brier": 0.2667811238485367,
      "final_Brier": 0.25789220946170976,
      "final_accuracy": 0.5125,
      "labels": 24,
      "method": "PCA",
      "replicate": 0
    },
    {
      "development_Brier": 0.26683642351841125,
      "final_Brier": 0.25742825427325233,
      "final_accuracy": 0.5125,
      "labels": 24,
      "method": "Frozen AE",
      "replicate": 0
    },
    {
      "development_Brier": 0.26674823883252535,
      "final_Brier": 0.2716002617847498,
      "final_accuracy": 0.5,
      "labels": 24,
      "method": "Absolute filter",
      "replicate": 0
    },
    {
      "development_Brier": 0.0003162788622552418,
      "final_Brier": 0.00017632249096287262,
      "final_accuracy": 1.0,
      "labels": 24,
      "method": "Fine-tuned AE",
      "replicate": 0
    },
    {
      "development_Brier": 0.0022788284128314154,
      "final_Brier": 0.0018510463144284215,
      "final_accuracy": 1.0,
      "labels": 80,
      "method": "Signed filter",
      "replicate": 0
    },
    {
      "development_Brier": 0.019744638103126627,
      "final_Brier": 0.01776343141524812,
      "final_accuracy": 1.0,
      "labels": 80,
      "method": "Raw window",
      "replicate": 0
    },
    {
      "development_Brier": 0.2608071405732339,
      "final_Brier": 0.2505324743178998,
      "final_accuracy": 0.5125,
      "labels": 80,
      "method": "PCA",
      "replicate": 0
    },
    {
      "development_Brier": 0.26039052999951584,
      "final_Brier": 0.25073563872744337,
      "final_accuracy": 0.5125,
      "labels": 80,
      "method": "Frozen AE",
      "replicate": 0
    },
    {
      "development_Brier": 0.2600124745571314,
      "final_Brier": 0.25289104058424494,
      "final_accuracy": 0.525,
      "labels": 80,
      "method": "Absolute filter",
      "replicate": 0
    },
    {
      "development_Brier": 0.00012632681866973656,
      "final_Brier": 0.00011680175555023327,
      "final_accuracy": 1.0,
      "labels": 80,
      "method": "Fine-tuned AE",
      "replicate": 0
    },
    {
      "development_Brier": 0.0004564862735227664,
      "final_Brier": 0.0003459543988577057,
      "final_accuracy": 1.0,
      "labels": 240,
      "method": "Signed filter",
      "replicate": 0
    },
    {
      "development_Brier": 0.005028494882628354,
      "final_Brier": 0.004156670881214768,
      "final_accuracy": 1.0,
      "labels": 240,
      "method": "Raw window",
      "replicate": 0
    },
    {
      "development_Brier": 0.26399105263120326,
      "final_Brier": 0.24881786001325618,
      "final_accuracy": 0.5,
      "labels": 240,
      "method": "PCA",
      "replicate": 0
    },
    {
      "development_Brier": 0.2637487168786238,
      "final_Brier": 0.2488015887256066,
      "final_accuracy": 0.5,
      "labels": 240,
      "method": "Frozen AE",
      "replicate": 0
    },
    {
      "development_Brier": 0.25311538017162843,
      "final_Brier": 0.24993787455673494,
      "final_accuracy": 0.5125,
      "labels": 240,
      "method": "Absolute filter",
      "replicate": 0
    },
    {
      "development_Brier": 0.00020456525897863688,
      "final_Brier": 0.00019008710097549055,
      "final_accuracy": 1.0,
      "labels": 240,
      "method": "Fine-tuned AE",
      "replicate": 0
    },
    {
      "development_Brier": 0.010343800555675253,
      "final_Brier": 0.009261035198430401,
      "final_accuracy": 1.0,
      "labels": 24,
      "method": "Signed filter",
      "replicate": 1
    },
    {
      "development_Brier": 0.226212864593674,
      "final_Brier": 0.18772000065038905,
      "final_accuracy": 0.7375,
      "labels": 24,
      "method": "Raw window",
      "replicate": 1
    },
    {
      "development_Brier": 0.2899066066348721,
      "final_Brier": 0.2907092275167368,
      "final_accuracy": 0.4625,
      "labels": 24,
      "method": "PCA",
      "replicate": 1
    },
    {
      "development_Brier": 0.28597982100478925,
      "final_Brier": 0.28780386139235714,
      "final_accuracy": 0.4625,
      "labels": 24,
      "method": "Frozen AE",
      "replicate": 1
    },
    {
      "development_Brier": 0.2659454739321276,
      "final_Brier": 0.26487990649766247,
      "final_accuracy": 0.475,
      "labels": 24,
      "method": "Absolute filter",
      "replicate": 1
    },
    {
      "development_Brier": 0.014962157623154126,
      "final_Brier": 0.0034019725797485903,
      "final_accuracy": 1.0,
      "labels": 24,
      "method": "Fine-tuned AE",
      "replicate": 1
    },
    {
      "development_Brier": 0.002068717481917508,
      "final_Brier": 0.0017306153603406937,
      "final_accuracy": 1.0,
      "labels": 80,
      "method": "Signed filter",
      "replicate": 1
    },
    {
      "development_Brier": 0.01934627635851841,
      "final_Brier": 0.016873038956935878,
      "final_accuracy": 1.0,
      "labels": 80,
      "method": "Raw window",
      "replicate": 1
    },
    {
      "development_Brier": 0.25864917006488997,
      "final_Brier": 0.2478214458631914,
      "final_accuracy": 0.6,
      "labels": 80,
      "method": "PCA",
      "replicate": 1
    },
    {
      "development_Brier": 0.25833049194091495,
      "final_Brier": 0.24728745365048868,
      "final_accuracy": 0.6,
      "labels": 80,
      "method": "Frozen AE",
      "replicate": 1
    },
    {
      "development_Brier": 0.25961481194793795,
      "final_Brier": 0.25872074458079625,
      "final_accuracy": 0.4625,
      "labels": 80,
      "method": "Absolute filter",
      "replicate": 1
    },
    {
      "development_Brier": 0.00017584829415589388,
      "final_Brier": 0.0001654549201006002,
      "final_accuracy": 1.0,
      "labels": 80,
      "method": "Fine-tuned AE",
      "replicate": 1
    },
    {
      "development_Brier": 0.0004564862735227664,
      "final_Brier": 0.0003459543988577057,
      "final_accuracy": 1.0,
      "labels": 240,
      "method": "Signed filter",
      "replicate": 1
    },
    {
      "development_Brier": 0.005028494882628354,
      "final_Brier": 0.004156670881214768,
      "final_accuracy": 1.0,
      "labels": 240,
      "method": "Raw window",
      "replicate": 1
    },
    {
      "development_Brier": 0.26399105263120326,
      "final_Brier": 0.24881786001325618,
      "final_accuracy": 0.5,
      "labels": 240,
      "method": "PCA",
      "replicate": 1
    },
    {
      "development_Brier": 0.2637487168786238,
      "final_Brier": 0.2488015887256066,
      "final_accuracy": 0.5,
      "labels": 240,
      "method": "Frozen AE",
      "replicate": 1
    },
    {
      "development_Brier": 0.25311538017162843,
      "final_Brier": 0.24993787455673494,
      "final_accuracy": 0.5125,
      "labels": 240,
      "method": "Absolute filter",
      "replicate": 1
    },
    {
      "development_Brier": 0.00015146057544443832,
      "final_Brier": 0.00013970506368186897,
      "final_accuracy": 1.0,
      "labels": 240,
      "method": "Fine-tuned AE",
      "replicate": 1
    },
    {
      "development_Brier": 0.014554748538663138,
      "final_Brier": 0.012490917133984047,
      "final_accuracy": 1.0,
      "labels": 24,
      "method": "Signed filter",
      "replicate": 2
    },
    {
      "development_Brier": 0.11730513760114443,
      "final_Brier": 0.09223622605418721,
      "final_accuracy": 0.9625,
      "labels": 24,
      "method": "Raw window",
      "replicate": 2
    },
    {
      "development_Brier": 0.2870486240794963,
      "final_Brier": 0.2690220024287403,
      "final_accuracy": 0.5125,
      "labels": 24,
      "method": "PCA",
      "replicate": 2
    },
    {
      "development_Brier": 0.2871924937157453,
      "final_Brier": 0.26919980353169437,
      "final_accuracy": 0.5125,
      "labels": 24,
      "method": "Frozen AE",
      "replicate": 2
    },
    {
      "development_Brier": 0.280335215216751,
      "final_Brier": 0.26410947740775953,
      "final_accuracy": 0.525,
      "labels": 24,
      "method": "Absolute filter",
      "replicate": 2
    },
    {
      "development_Brier": 0.00018457698069080107,
      "final_Brier": 0.00015884413195329982,
      "final_accuracy": 1.0,
      "labels": 24,
      "method": "Fine-tuned AE",
      "replicate": 2
    },
    {
      "development_Brier": 0.001932875165033339,
      "final_Brier": 0.0015932063772397535,
      "final_accuracy": 1.0,
      "labels": 80,
      "method": "Signed filter",
      "replicate": 2
    },
    {
      "development_Brier": 0.020123376659915686,
      "final_Brier": 0.017745130477381178,
      "final_accuracy": 1.0,
      "labels": 80,
      "method": "Raw window",
      "replicate": 2
    },
    {
      "development_Brier": 0.2612838648320047,
      "final_Brier": 0.2506023364368994,
      "final_accuracy": 0.4875,
      "labels": 80,
      "method": "PCA",
      "replicate": 2
    },
    {
      "development_Brier": 0.26110691550628495,
      "final_Brier": 0.25037505807413407,
      "final_accuracy": 0.475,
      "labels": 80,
      "method": "Frozen AE",
      "replicate": 2
    },
    {
      "development_Brier": 0.25540239479269417,
      "final_Brier": 0.2531590436099128,
      "final_accuracy": 0.4875,
      "labels": 80,
      "method": "Absolute filter",
      "replicate": 2
    },
    {
      "development_Brier": 0.00014395078218854273,
      "final_Brier": 0.00013552571397718732,
      "final_accuracy": 1.0,
      "labels": 80,
      "method": "Fine-tuned AE",
      "replicate": 2
    },
    {
      "development_Brier": 0.0004564862735227664,
      "final_Brier": 0.0003459543988577057,
      "final_accuracy": 1.0,
      "labels": 240,
      "method": "Signed filter",
      "replicate": 2
    },
    {
      "development_Brier": 0.005028494882628354,
      "final_Brier": 0.004156670881214768,
      "final_accuracy": 1.0,
      "labels": 240,
      "method": "Raw window",
      "replicate": 2
    },
    {
      "development_Brier": 0.26399105263120326,
      "final_Brier": 0.24881786001325618,
      "final_accuracy": 0.5,
      "labels": 240,
      "method": "PCA",
      "replicate": 2
    },
    {
      "development_Brier": 0.2637487168786238,
      "final_Brier": 0.2488015887256066,
      "final_accuracy": 0.5,
      "labels": 240,
      "method": "Frozen AE",
      "replicate": 2
    },
    {
      "development_Brier": 0.25311538017162843,
      "final_Brier": 0.24993787455673494,
      "final_accuracy": 0.5125,
      "labels": 240,
      "method": "Absolute filter",
      "replicate": 2
    },
    {
      "development_Brier": 0.0001297143025598214,
      "final_Brier": 0.00011896663637097122,
      "final_accuracy": 1.0,
      "labels": 240,
      "method": "Fine-tuned AE",
      "replicate": 2
    }
  ],
  "pretraining_steps": 800,
  "probes": [
    {
      "SD_Brier": 0.004120448736683343,
      "SD_accuracy": 0.025000000000000022,
      "labels": 24,
      "mean_Brier": 0.26686321523005724,
      "mean_accuracy": 0.5,
      "method": "Absolute filter"
    },
    {
      "SD_Brier": 0.0032911444817545136,
      "SD_accuracy": 0.0314576434802948,
      "labels": 80,
      "mean_Brier": 0.25492360959165133,
      "mean_accuracy": 0.4916666666666667,
      "method": "Absolute filter"
    },
    {
      "SD_Brier": 3.3993498887762956e-17,
      "SD_accuracy": 0.0,
      "labels": 240,
      "mean_Brier": 0.24993787455673497,
      "mean_accuracy": 0.5125,
      "method": "Absolute filter"
    },
    {
      "SD_Brier": 0.0018673959639569423,
      "SD_accuracy": 0.0,
      "labels": 24,
      "mean_Brier": 0.001245713067554921,
      "mean_accuracy": 1.0,
      "method": "Fine-tuned AE"
    },
    {
      "SD_Brier": 2.454069551825131e-05,
      "SD_accuracy": 0.0,
      "labels": 80,
      "mean_Brier": 0.00013926079654267358,
      "mean_accuracy": 1.0,
      "method": "Fine-tuned AE"
    },
    {
      "SD_Brier": 3.6575384561085966e-05,
      "SD_accuracy": 0.0,
      "labels": 240,
      "mean_Brier": 0.00014958626700944358,
      "mean_accuracy": 1.0,
      "method": "Fine-tuned AE"
    },
    {
      "SD_Brier": 0.01531534006957853,
      "SD_accuracy": 0.02886751345948125,
      "labels": 24,
      "mean_Brier": 0.2714773063991013,
      "mean_accuracy": 0.4958333333333333,
      "method": "Frozen AE"
    },
    {
      "SD_Brier": 0.0018953143894610434,
      "SD_accuracy": 0.06414501799308606,
      "labels": 80,
      "mean_Brier": 0.2494660501506887,
      "mean_accuracy": 0.5291666666666667,
      "method": "Frozen AE"
    },
    {
      "SD_Brier": 3.3993498887762956e-17,
      "SD_accuracy": 0.0,
      "labels": 240,
      "mean_Brier": 0.24880158872560662,
      "mean_accuracy": 0.5,
      "method": "Frozen AE"
    },
    {
      "SD_Brier": 0.01668914166721562,
      "SD_accuracy": 0.02886751345948125,
      "labels": 24,
      "mean_Brier": 0.2725411464690623,
      "mean_accuracy": 0.4958333333333333,
      "method": "PCA"
    },
    {
      "SD_Brier": 0.0015857652401310694,
      "SD_accuracy": 0.05907269532815761,
      "labels": 80,
      "mean_Brier": 0.2496520855393302,
      "mean_accuracy": 0.5333333333333333,
      "method": "PCA"
    },
    {
      "SD_Brier": 3.3993498887762956e-17,
      "SD_accuracy": 0.0,
      "labels": 240,
      "mean_Brier": 0.24881786001325615,
      "mean_accuracy": 0.5,
      "method": "PCA"
    },
    {
      "SD_Brier": 0.06509770514094233,
      "SD_accuracy": 0.14197270864500683,
      "labels": 24,
      "mean_Brier": 0.11442800955711407,
      "mean_accuracy": 0.9,
      "method": "Raw window"
    },
    {
      "SD_Brier": 0.0005088675784161539,
      "SD_accuracy": 0.0,
      "labels": 80,
      "mean_Brier": 0.017460533616521723,
      "mean_accuracy": 1.0,
      "method": "Raw window"
    },
    {
      "SD_Brier": 0.0,
      "SD_accuracy": 0.0,
      "labels": 240,
      "mean_Brier": 0.004156670881214768,
      "mean_accuracy": 1.0,
      "method": "Raw window"
    },
    {
      "SD_Brier": 0.001787646900436342,
      "SD_accuracy": 0.0,
      "labels": 24,
      "mean_Brier": 0.010433390162800081,
      "mean_accuracy": 1.0,
      "method": "Signed filter"
    },
    {
      "SD_Brier": 0.00012901309788077792,
      "SD_accuracy": 0.0,
      "labels": 80,
      "mean_Brier": 0.0017249560173362895,
      "mean_accuracy": 1.0,
      "method": "Signed filter"
    },
    {
      "SD_Brier": 0.0,
      "SD_accuracy": 0.0,
      "labels": 240,
      "mean_Brier": 0.0003459543988577057,
      "mean_accuracy": 1.0,
      "method": "Signed filter"
    }
  ],
  "split_buildings": [
    30,
    10,
    10
  ]
}
```


## Publication verification

At content verification, commit `b2e224191f8adf279971b5a856a01d24c149afb8` matched remote main and all 170 file blobs with a clean working tree. Final metadata and all five notebooks are separately verified through commit-addressed raw files in the local delivery evidence. Only companion artifacts are published.
