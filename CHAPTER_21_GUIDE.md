# Chapter 21: Building and training neural networks — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_21_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 21.1 · Feedforward networks and output heads

- [Inputs and outputs are different objects](notebooks/103_Chapter_21_01_mixed_features_and_heads.ipynb#head-contract)
- [Losses express the head contracts](notebooks/103_Chapter_21_01_mixed_features_and_heads.ipynb#loss-meaning)

Declared mechanisms: continuous and categorical inputs, shared feedforward torso, Gaussian and classification heads, output-shape and unknown-category contracts.

```bash
python scripts/run_notebook.py notebooks/103_Chapter_21_01_mixed_features_and_heads.ipynb
```

## 21.2 · Automatic differentiation and backpropagation

- [A complete tiny deflection computation](notebooks/104_Chapter_21_02_autodiff_and_gradient_checks.ipynb#graph)
- [A derivative is local evidence](notebooks/104_Chapter_21_02_autodiff_and_gradient_checks.ipynb#checks)

Declared mechanisms: explicit computational graph, manual reverse-mode derivatives, finite differences and gradcheck, gradient accumulation and updates.

```bash
python scripts/run_notebook.py notebooks/104_Chapter_21_02_autodiff_and_gradient_checks.ipynb
```

## 21.3 · Initialization and activation behaviour

- [Hold the computation fixed before comparing initializers](notebooks/105_Chapter_21_03_initialization_and_activations.ipynb#propagation)
- [Diagnose the obstruction before changing the model](notebooks/105_Chapter_21_03_initialization_and_activations.ipynb#diagnostic-limits)

Declared mechanisms: activation and gradient propagation, Xavier and Kaiming controls, dead ReLU units, finite-depth initialization diagnostics.

```bash
python scripts/run_notebook.py notebooks/105_Chapter_21_03_initialization_and_activations.ipynb
```

## 21.4 · Normalization, optimization and regularization

- [Change one declared part of the recipe](notebooks/106_Chapter_21_04_normalization_and_training_health.ipynb#recipe)
- [Training mode is an inference contract](notebooks/106_Chapter_21_04_normalization_and_training_health.ipynb#health)

Declared mechanisms: actual AdamW/SGD ablations, batch and layer normalization, dropout train/eval contracts, development early stopping, controlled instability dashboard.

```bash
python scripts/run_notebook.py notebooks/106_Chapter_21_04_normalization_and_training_health.ipynb
```

## 21.5 · Debugging, batching and computational resources

- [A payload target and a recording shortcut](notebooks/107_Chapter_21_05_debugging_padding_and_resources.ipynb#padding)
- [Measure native CPU process resources honestly](notebooks/107_Chapter_21_05_debugging_padding_and_resources.ipynb#resources)
- [Observation, accounting and deployment are different claims](notebooks/107_Chapter_21_05_debugging_padding_and_resources.ipynb#resource-interpretation)

Declared mechanisms: padding shortcut and explicit masking, tiny-set overfitting, weighted microbatch gradients, checkpoint exact next step, actual process peak RSS and CPU timing.

```bash
python scripts/run_notebook.py notebooks/107_Chapter_21_05_debugging_padding_and_resources.ipynb
```

## Interpretation and boundaries

Five self-contained CPU laboratories103–107use seeds2203–2207,21code cells and10inline figures. Dependencies are unchanged from20: Python3.14.3/NumPy2.4.4/SciPy1.17.1/pandas3.0.3/Matplotlib3.11.0/sklearn1.9.0/PyTorch2.14.1; numerical pools andTorchuseoneCPUthread. Main neural fits usefloat64,explicitseeds/deterministicalgorithms;the separate resource children declarefloat32. Ordinary notebookexecution needs no input files, network, credentials orGPU. All examples generate their inputs/helpers internally. Original105launch used an incorrect pre-registration filename offset and failed before opening a kernel; correcting the builder offset and renaming only the new103–105files repaired the path. The107embedded-child script needed a pre-execution indentation repair, caught by source compilation. All final kernels complete assertions without errors or stderr warnings. Layout-only103/105reruns retain exact deterministic result dictionaries. The103diagram now matches the actual categorical index tensor shapeN, rather than implying an unsqueezedN×1lookup;105labels were shortened for the book column.

103generates60buildings×6members,train40/dev10/final10(240/60/60). Inputs loaduniform.2–2,slendernessnormal1/.2,3physicaltypes;6%randommissingrecordedtype maps to supportedtoken3,unknown4rejectedbyadmissionwrapper. Training-onlycontinuousStd,Embedding5×2,concat4→12ReLUsharedtorso;Gaussianhead2(mean,softplusvariance+1e-4),independentBernoullihead2logits,exclusivehead3logits. Stored161parameters includeunusedunsupportedcategoryrow. Response mean1+.6load+.4slender+typeoffset[0,.2,-.1],heteroscedasticSD.08+.1load;2Bernoulliprobs and3exclusiveGumbelstates have explicitgeneration. Fixed500AdamWsteps/.02/decay.001/unitweightedfullGaussianNLL+BCEWithLogits+CrossEntropy. DevelopmentMSE.0526213/GaussianNLL.0924697/binaryBrier.2470665/exclusiveCE1.1128788/accuracy.416667;final.0498244/-.00354856/.2081116/1.1538845/.466667. NegativecontinuousNLLisvaliddensityscoreinitsunits. Headshapeandprobabilitysumassertionspass,notcalibrationproof. Unknownlookupallocationdoesnotcreatevalidatedsupport. Finalconfusioncounts[[5,8,0],[3,18,3],[6,12,5]]sum60;smallbinarybindiagnosticsnotpopulationcalibrationguarantee.

104fixedinput[-.7,1.2],theta[.4,-.2,.1,.5,.05,-.1,.8,-.6,.2],target.3,twohiddenTanh. z[-.47,.43],h[-.4381993,.4053213],prediction-.393752237,half-squareloss.240646083. Manualreverse/autodiffparameterderivativesagree1e-12,gradcheckeps1e-6atol1e-5rtol1e-3passes. CentralFDsteps.1through1e-8infloat64/32;64relativeerror.0046915at.1,min3.9207e-11at1e-6,4.3817e-9at1e-8;32minimum2.7236e-5at.001anderror1at1e-8. Repeatedbackwardsaccumulatetwicegradientunlesscleared,expectedfullydetachedbackwardRuntimeErrorcaught. Parameterstep.1reducesloss.107120474. Graphnodeadjointsarederivativeswithrespecttohiddenoutputs(-.555002/.416251),notpreactivationderivatives(-.448431/.347867). Finitechecksverifylocalcomputation,notphysicsorglobalconvergence;nonsmooth/randomdiagnosticlimitsdisclosed.

105same128normal32Dinputs,twelvehid32layers,sixactivation/initializerconditions×3seeds,meansquaredfinalactivationdiagnosticloss,nooptimizationorlabeldriveninitializerselection. SigmoidweightsSD2;ReLUSD.001/2;ReLUKaimingfan_in;deadReLUSD.01/bias-5;TanhXaviergaincalculate_gain. SignalSD/weightgradientRMSperdepth,ReLUzeroorSigmoidoutside[.01,.99]/Tanhabs>.99fractions explicit. LastmeanSD ReLUtiny7.6937e-30,large3.15133e10,Kaiming.458580(first.807835),Tanh.648452(first.749198). LargeReLUlastgradient1.18687e19/tiny1.41486e-57;lossitselfchangeswithoutputscales,notfairfixedtaskperformancecomparison. Deadcasealloutputs/gradients0,plottedfloor1e-60explicitnotmeasuredpositive. PositiveweightrescalingspreservepairedReLUactivepatterns(firstinactive.496501,last.472982)despitedrasticgradientdifferences. Sigmoidlastsaturatedfraction.533285butgradientnotzero(.00175995),retainedratherthanassertingallSigmoidlearningfails. Tanhlastsaturated.015381. Three-seeddescriptivemeansnotpopulationCIorexactvarianceguarantee. 72aggregated/216individualprofilesretained.

106fortybuildings×8sensorrecords,train24/dev8/final8(192/64/64),trainingScaler,2hidden32ReLUregression. SixfixedrecipesstartcompatibleweightsfromsameTorchseed/shareprecomputedbatchorders;batch32,max120epochs,developmentMSEpatience15,deepcopybestcheckpointrestored. AdamWlr.01/decay.01base/LN/BN/LNdrop.2/CosineTmax120;momentumSGDlr.05/momentum.9/decay.01base. Bestepoch/runepochs/devMSE/finalMSE: Base9/24/.122136/.187939;LN38/53/.150077/.202729;BN8/23/.135010/.204270;LNdrop25/40/.126994/.193323;SGD17/32/.120325/.157452;Cos9/24/.122288/.187604. SGD'sactualadvantagehereisretained,nouniversaloptimizerclaim. BNclonequerytraincontextdifference1.502284,eval1.665e-16;LNevaldifference0;dropouttrainingrepeatnormdifference1.799883,evaluationidentical. Diagnosticsdon'talterfittedBNrunningstats/checkpoints. IndependentSGDlr20fullbatchfrombaselineinitializationtrainloss.866326→16163.3006→1.178906e12,gradnorm1.11453→10862.426→4.98698e11,devMSE.678447→17996.939→1.369989e12;stopatdeclared1e8losslimitafter2updates,finitehistorynotconcealedNaN. Dashboardstablemini-batchepochversusunstablefullbatchupdateunitsdistinct,noefficiencycomparison.

107independentbalancedtrain200/dev80/final200sequences,paddedwidth32,payloadmean1/1.12withSD.2. Train/devlabel0length8,label1length24;finalreversed. Maskfromknowncount,numericalzerosnotautomaticallymissing. Training-onlyseparateStandardScalers,fixednn.Linear1→1/BCEAdam.1/600stepsperfeature. Unmaskedtrain/devaccuracy1/1,final0/Brier.99183464;maskedtrain.815/dev.95/final.885/Brier.09316936. Thisisadeliberatelyconstructedrecordingshift,notestimatedprevalence. Appending32paddingpositionspreservesmaskedfeature/predictionexactmaxdiff0,changesunmasked. Tiny8arbitrarylabelMLP2→32Tanh→1,1000Adam.05steps,accuracy1/loss1.41781e-5checksplumbingnotgeneralization. Unequalmicrobatch3/3/2record-countweightedmeanmatchesfullgradientmax1.11e-16. Loader8input/7targetmismatchcaught. Gradientnorm1,566,941.272→.99999999999936byclip1. Model/Adamstate/TorchRNGinmemoryBytesIOcheckpointloadweights_onlyTrue/mapcpu→exactnextstepafterrestore;notuniversalpipeline-stateguarantee. Arithmetic[1e8,1,-1e8]sumfloat32=0,float64=1;device/dtypeassertionsCPU64main.

107actualCPUprofilinglaunchesninefreshsubprocesseswithsameinterpreter,inlinecode/model/inputs;batch8/32/128×3repeats,T128,F16,pointwise16→128ReLU→128ReLU→128ReLU→1,float32,1CPUthread,AdamW.001,onewarmup/fivetimedupdates. OSgetrusageSELFhighwaterRSSincludesruntime/libraries/allocator/training,notGPUortensor-onlymemory. LocalDarwinBSDmanualconfirmsbytes;LinuxmanualconfirmsKiBconversion. Exactinputtensorbytes65536/262144/1048576areseparatefrommeasuredpeaks. OriginalmedianpeakRSS302.28125/310.015625/341.015625MiB;medianseconds/update.0005996416/.0014469916/.005438325,individualobservationsandmin/maxrangesretained. BaselineafterTorchimport~203.4–203.9MiB;notclaimthatpeakminusbaselineisexacttensorallocation. Observationsarenondeterministicandlivesummarykeyresource_observations,outsideRESULTS. FigureproducerexplicitlyskipsRESOURCE_MEASUREMENT_CELL,replaysoriginalfreshkernelobservationsforvectorplot,andrerunsallothercodecheckingexactRESULTS. Ordinarynotebookrunsprofilefreshwithnoexternalmeasurementfile. Thisexceptionpreservesactualmeasureddata,notabitwiseclaimaboutelapsedtimes/RSS.

Tenoriginalvectorfiguresimplementbothoriginalbriefs: annotatedforward/reversecomputationandstable/unstabletraininghealth. Five numbered equations andtwelveexercisescoverfiveexactscopes. Primarysourcesinspected20October2026:PyTorch2.14GaussianNLL/CrossEntropy/autograd/gradcheck/init/BN/LN/AdamW/Dropoutandserialization;Glorot/Bengio2010PMLR;Pythonresource3.14.8maintenanceversusexecuted3.14.3;localDarwinBSDgetrusageandLinuxman-pagesforunits. TheimplementationusespinnedPyTorch2.14.1. CPUmeasurementsdon'tcertifyanotherdevice'smemory,throughput,fieldvalidityorliteraturecompleteness.
