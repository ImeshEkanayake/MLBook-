# Chapter 20: Representation learning and dimensionality reduction — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_20_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 20.1 · Linear factorization and latent components

- [Four objectives, one information boundary](notebooks/098_Chapter_20_01_factorization_and_lost_signal.ipynb#contracts)
- [Reconstruction is not target sufficiency](notebooks/098_Chapter_20_01_factorization_and_lost_signal.ipynb#interpretation)

Declared mechanisms: centered PCA/SVD identity, nonnegative factorization, independent components, small-signal attenuation.

```bash
python scripts/run_notebook.py notebooks/098_Chapter_20_01_factorization_and_lost_signal.ipynb
```

## 20.2 · Manifolds and nonlinear visualization

- [One transductive display cohort](notebooks/099_Chapter_20_02_manifold_displays.ipynb#display-contract)
- [Attractive geometry is not a validation set](notebooks/099_Chapter_20_02_manifold_displays.ipynb#diagnostics)

Declared mechanisms: actual t-SNE and UMAP, neighborhood diagnostics, transductive visualization, new-query transforms.

```bash
python scripts/run_notebook.py notebooks/099_Chapter_20_02_manifold_displays.ipynb
```

## 20.3 · Embeddings for entities and relationships

- [A row lookup cannot invent an unseen entity](notebooks/100_Chapter_20_03_entity_and_graph_embeddings.ipynb#entities)
- [Graph coordinates identify a relation, not a universal axis](notebooks/100_Chapter_20_03_entity_and_graph_embeddings.ipynb#graph-contract)

Declared mechanisms: masked matrix factorization, whole-entity holdout, inductive descriptor mapping, transductive graph coordinates.

```bash
python scripts/run_notebook.py notebooks/100_Chapter_20_03_entity_and_graph_embeddings.ipynb
```

## 20.4 · Autoencoders and reconstruction learning

- [Fit compression to admitted vibration windows](notebooks/101_Chapter_20_04_autoencoders_and_reconstruction.ipynb#bottleneck)
- [What the losses can certify](notebooks/101_Chapter_20_04_autoencoders_and_reconstruction.ipynb#limits)

Declared mechanisms: actual CPU autoencoder training, denoising measurement targets, bottleneck versus identity, analytic Gaussian KL connection.

```bash
python scripts/run_notebook.py notebooks/101_Chapter_20_04_autoencoders_and_reconstruction.ipynb
```

## 20.5 · Evaluating and transferring representations

- [A new-building task with a small signed signal](notebooks/102_Chapter_20_05_representation_transfer.ipynb#boundaries)
- [Keep the label information visible](notebooks/102_Chapter_20_05_representation_transfer.ipynb#sufficiency)

Declared mechanisms: whole-building representation assessment, frozen linear probes, actual encoder fine-tuning, invariance can remove task information.

```bash
python scripts/run_notebook.py notebooks/102_Chapter_20_05_representation_transfer.ipynb
```

## Interpretation and boundaries

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
