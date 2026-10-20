# Chapter 21 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_103 | 21.1 | 4 | 2 | 2.284 |
| code_104 | 21.2 | 4 | 2 | 2.172 |
| code_105 | 21.3 | 4 | 2 | 2.457 |
| code_106 | 21.4 | 4 | 2 | 2.332 |
| code_107 | 21.5 | 5 | 2 | 9.869 |

Total: **21 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. All ten inline notebook figures and ten book figure sets were visually inspected, alongside the exact compiled chapter and front/reference pages. The resource vector plot replays the original measured CPU observations; deterministic experiment results reproduce exactly.

## Actual mechanisms and boundaries

Five self-contained CPU laboratories103–107use seeds2203–2207,21code cells and10inline figures. Dependencies are unchanged from20: Python3.14.3/NumPy2.4.4/SciPy1.17.1/pandas3.0.3/Matplotlib3.11.0/sklearn1.9.0/PyTorch2.14.1; numerical pools andTorchuseoneCPUthread. Main neural fits usefloat64,explicitseeds/deterministicalgorithms;the separate resource children declarefloat32. Ordinary notebookexecution needs no input files, network, credentials orGPU. All examples generate their inputs/helpers internally. Original105launch used an incorrect pre-registration filename offset and failed before opening a kernel; correcting the builder offset and renaming only the new103–105files repaired the path. The107embedded-child script needed a pre-execution indentation repair, caught by source compilation. All final kernels complete assertions without errors or stderr warnings. Layout-only103/105reruns retain exact deterministic result dictionaries. The103diagram now matches the actual categorical index tensor shapeN, rather than implying an unsqueezedN×1lookup;105labels were shortened for the book column.

103generates60buildings×6members,train40/dev10/final10(240/60/60). Inputs loaduniform.2–2,slendernessnormal1/.2,3physicaltypes;6%randommissingrecordedtype maps to supportedtoken3,unknown4rejectedbyadmissionwrapper. Training-onlycontinuousStd,Embedding5×2,concat4→12ReLUsharedtorso;Gaussianhead2(mean,softplusvariance+1e-4),independentBernoullihead2logits,exclusivehead3logits. Stored161parameters includeunusedunsupportedcategoryrow. Response mean1+.6load+.4slender+typeoffset[0,.2,-.1],heteroscedasticSD.08+.1load;2Bernoulliprobs and3exclusiveGumbelstates have explicitgeneration. Fixed500AdamWsteps/.02/decay.001/unitweightedfullGaussianNLL+BCEWithLogits+CrossEntropy. DevelopmentMSE.0526213/GaussianNLL.0924697/binaryBrier.2470665/exclusiveCE1.1128788/accuracy.416667;final.0498244/-.00354856/.2081116/1.1538845/.466667. NegativecontinuousNLLisvaliddensityscoreinitsunits. Headshapeandprobabilitysumassertionspass,notcalibrationproof. Unknownlookupallocationdoesnotcreatevalidatedsupport. Finalconfusioncounts[[5,8,0],[3,18,3],[6,12,5]]sum60;smallbinarybindiagnosticsnotpopulationcalibrationguarantee.

104fixedinput[-.7,1.2],theta[.4,-.2,.1,.5,.05,-.1,.8,-.6,.2],target.3,twohiddenTanh. z[-.47,.43],h[-.4381993,.4053213],prediction-.393752237,half-squareloss.240646083. Manualreverse/autodiffparameterderivativesagree1e-12,gradcheckeps1e-6atol1e-5rtol1e-3passes. CentralFDsteps.1through1e-8infloat64/32;64relativeerror.0046915at.1,min3.9207e-11at1e-6,4.3817e-9at1e-8;32minimum2.7236e-5at.001anderror1at1e-8. Repeatedbackwardsaccumulatetwicegradientunlesscleared,expectedfullydetachedbackwardRuntimeErrorcaught. Parameterstep.1reducesloss.107120474. Graphnodeadjointsarederivativeswithrespecttohiddenoutputs(-.555002/.416251),notpreactivationderivatives(-.448431/.347867). Finitechecksverifylocalcomputation,notphysicsorglobalconvergence;nonsmooth/randomdiagnosticlimitsdisclosed.

105same128normal32Dinputs,twelvehid32layers,sixactivation/initializerconditions×3seeds,meansquaredfinalactivationdiagnosticloss,nooptimizationorlabeldriveninitializerselection. SigmoidweightsSD2;ReLUSD.001/2;ReLUKaimingfan_in;deadReLUSD.01/bias-5;TanhXaviergaincalculate_gain. SignalSD/weightgradientRMSperdepth,ReLUzeroorSigmoidoutside[.01,.99]/Tanhabs>.99fractions explicit. LastmeanSD ReLUtiny7.6937e-30,large3.15133e10,Kaiming.458580(first.807835),Tanh.648452(first.749198). LargeReLUlastgradient1.18687e19/tiny1.41486e-57;lossitselfchangeswithoutputscales,notfairfixedtaskperformancecomparison. Deadcasealloutputs/gradients0,plottedfloor1e-60explicitnotmeasuredpositive. PositiveweightrescalingspreservepairedReLUactivepatterns(firstinactive.496501,last.472982)despitedrasticgradientdifferences. Sigmoidlastsaturatedfraction.533285butgradientnotzero(.00175995),retainedratherthanassertingallSigmoidlearningfails. Tanhlastsaturated.015381. Three-seeddescriptivemeansnotpopulationCIorexactvarianceguarantee. 72aggregated/216individualprofilesretained.

106fortybuildings×8sensorrecords,train24/dev8/final8(192/64/64),trainingScaler,2hidden32ReLUregression. SixfixedrecipesstartcompatibleweightsfromsameTorchseed/shareprecomputedbatchorders;batch32,max120epochs,developmentMSEpatience15,deepcopybestcheckpointrestored. AdamWlr.01/decay.01base/LN/BN/LNdrop.2/CosineTmax120;momentumSGDlr.05/momentum.9/decay.01base. Bestepoch/runepochs/devMSE/finalMSE: Base9/24/.122136/.187939;LN38/53/.150077/.202729;BN8/23/.135010/.204270;LNdrop25/40/.126994/.193323;SGD17/32/.120325/.157452;Cos9/24/.122288/.187604. SGD'sactualadvantagehereisretained,nouniversaloptimizerclaim. BNclonequerytraincontextdifference1.502284,eval1.665e-16;LNevaldifference0;dropouttrainingrepeatnormdifference1.799883,evaluationidentical. Diagnosticsdon'talterfittedBNrunningstats/checkpoints. IndependentSGDlr20fullbatchfrombaselineinitializationtrainloss.866326→16163.3006→1.178906e12,gradnorm1.11453→10862.426→4.98698e11,devMSE.678447→17996.939→1.369989e12;stopatdeclared1e8losslimitafter2updates,finitehistorynotconcealedNaN. Dashboardstablemini-batchepochversusunstablefullbatchupdateunitsdistinct,noefficiencycomparison.

107independentbalancedtrain200/dev80/final200sequences,paddedwidth32,payloadmean1/1.12withSD.2. Train/devlabel0length8,label1length24;finalreversed. Maskfromknowncount,numericalzerosnotautomaticallymissing. Training-onlyseparateStandardScalers,fixednn.Linear1→1/BCEAdam.1/600stepsperfeature. Unmaskedtrain/devaccuracy1/1,final0/Brier.99183464;maskedtrain.815/dev.95/final.885/Brier.09316936. Thisisadeliberatelyconstructedrecordingshift,notestimatedprevalence. Appending32paddingpositionspreservesmaskedfeature/predictionexactmaxdiff0,changesunmasked. Tiny8arbitrarylabelMLP2→32Tanh→1,1000Adam.05steps,accuracy1/loss1.41781e-5checksplumbingnotgeneralization. Unequalmicrobatch3/3/2record-countweightedmeanmatchesfullgradientmax1.11e-16. Loader8input/7targetmismatchcaught. Gradientnorm1,566,941.272→.99999999999936byclip1. Model/Adamstate/TorchRNGinmemoryBytesIOcheckpointloadweights_onlyTrue/mapcpu→exactnextstepafterrestore;notuniversalpipeline-stateguarantee. Arithmetic[1e8,1,-1e8]sumfloat32=0,float64=1;device/dtypeassertionsCPU64main.

107actualCPUprofilinglaunchesninefreshsubprocesseswithsameinterpreter,inlinecode/model/inputs;batch8/32/128×3repeats,T128,F16,pointwise16→128ReLU→128ReLU→128ReLU→1,float32,1CPUthread,AdamW.001,onewarmup/fivetimedupdates. OSgetrusageSELFhighwaterRSSincludesruntime/libraries/allocator/training,notGPUortensor-onlymemory. LocalDarwinBSDmanualconfirmsbytes;LinuxmanualconfirmsKiBconversion. Exactinputtensorbytes65536/262144/1048576areseparatefrommeasuredpeaks. OriginalmedianpeakRSS302.28125/310.015625/341.015625MiB;medianseconds/update.0005996416/.0014469916/.005438325,individualobservationsandmin/maxrangesretained. BaselineafterTorchimport~203.4–203.9MiB;notclaimthatpeakminusbaselineisexacttensorallocation. Observationsarenondeterministicandlivesummarykeyresource_observations,outsideRESULTS. FigureproducerexplicitlyskipsRESOURCE_MEASUREMENT_CELL,replaysoriginalfreshkernelobservationsforvectorplot,andrerunsallothercodecheckingexactRESULTS. Ordinarynotebookrunsprofilefreshwithnoexternalmeasurementfile. Thisexceptionpreservesactualmeasureddata,notabitwiseclaimaboutelapsedtimes/RSS.

Tenoriginalvectorfiguresimplementbothoriginalbriefs: annotatedforward/reversecomputationandstable/unstabletraininghealth. Five numbered equations andtwelveexercisescoverfiveexactscopes. Primarysourcesinspected20October2026:PyTorch2.14GaussianNLL/CrossEntropy/autograd/gradcheck/init/BN/LN/AdamW/Dropoutandserialization;Glorot/Bengio2010PMLR;Pythonresource3.14.8maintenanceversusexecuted3.14.3;localDarwinBSDgetrusageandLinuxman-pagesforunits. TheimplementationusespinnedPyTorch2.14.1. CPUmeasurementsdon'tcertifyanotherdevice'smemory,throughput,fieldvalidityorliteraturecompleteness.

## Successful result dictionaries

### code_103

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2203.

```json
{
  "development": {
    "Gaussian_NLL": 0.09246967637009487,
    "MSE": 0.05262131293718684,
    "binary_Brier": 0.24706653436365447,
    "exclusive_accuracy": 0.4166666666666667,
    "exclusive_cross_entropy": 1.1128787942333527
  },
  "final": {
    "Gaussian_NLL": -0.0035485595411644125,
    "MSE": 0.049824395150531525,
    "binary_Brier": 0.2081116059488231,
    "exclusive_accuracy": 0.4666666666666667,
    "exclusive_cross_entropy": 1.1538845291582753
  },
  "head_shapes": {
    "binary_logits": [
      60,
      2
    ],
    "exclusive_logits": [
      60,
      3
    ],
    "mean": [
      60
    ],
    "variance": [
      60
    ]
  },
  "parameter_count": 161,
  "split_buildings": [
    40,
    10,
    10
  ],
  "training_losses": [
    [
      0,
      5.818278663535724,
      0.7380839854986394,
      1.1323469553686571
    ],
    [
      25,
      1.335782083108304,
      0.6416932581399486,
      1.0084971507274934
    ],
    [
      50,
      0.7899855943197617,
      0.6312715208989274,
      0.9807128348830038
    ],
    [
      75,
      -0.09454799752916827,
      0.6316584073756982,
      0.9717469772194726
    ],
    [
      100,
      -0.2514449035455604,
      0.6312687981118575,
      0.9613085172266718
    ],
    [
      125,
      -0.28840522375794253,
      0.6308445624728551,
      0.956065232556866
    ],
    [
      150,
      -0.3058912121613984,
      0.6303774853125306,
      0.953146074403741
    ],
    [
      175,
      -0.31453523821363155,
      0.6302296851245127,
      0.9502411272209558
    ],
    [
      200,
      -0.3221654470500241,
      0.6300600943439091,
      0.9476391066003251
    ],
    [
      225,
      -0.3256165510834459,
      0.6297015113236639,
      0.9461805131095709
    ],
    [
      250,
      -0.32179667592457156,
      0.6293588362765521,
      0.9452036891738224
    ],
    [
      275,
      -0.3306208567643452,
      0.6289319357212361,
      0.9441100903443153
    ],
    [
      300,
      -0.3325878993638425,
      0.6285323265940281,
      0.9428715410067997
    ],
    [
      325,
      -0.329767807434364,
      0.6282108832687371,
      0.9424745650636093
    ],
    [
      350,
      -0.3357167872888533,
      0.6278065528483254,
      0.9420829957083875
    ],
    [
      375,
      -0.3339741722873771,
      0.6274223803083768,
      0.9418504816891867
    ],
    [
      400,
      -0.33761254604043633,
      0.6270252611639933,
      0.9411916312776447
    ],
    [
      425,
      -0.3412170810573882,
      0.6268714555735462,
      0.9406749681657491
    ],
    [
      450,
      -0.3432095754802637,
      0.626610574304769,
      0.9405149716491561
    ],
    [
      475,
      -0.3420930422199614,
      0.6264376114765736,
      0.9404733122661909
    ]
  ],
  "training_steps": 500,
  "unknown_type_rejected": true
}
```

### code_104

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2204.

```json
{
  "automatic_gradient": [
    0.31390177075707465,
    -0.5381173212978423,
    -0.24350713749032066,
    0.417440807126264,
    -0.4484311010815352,
    0.3478673392718867,
    0.3040017549521085,
    -0.28119256463946446,
    -0.693752237079892
  ],
  "detached_graph_rejected": true,
  "finite_difference": [
    {
      "dtype": "torch.float64",
      "epsilon": 0.1,
      "relative_gradient_error": 0.00469150167751583
    },
    {
      "dtype": "torch.float64",
      "epsilon": 0.01,
      "relative_gradient_error": 4.7168826964138646e-05
    },
    {
      "dtype": "torch.float64",
      "epsilon": 0.001,
      "relative_gradient_error": 4.7171371206802574e-07
    },
    {
      "dtype": "torch.float64",
      "epsilon": 0.0001,
      "relative_gradient_error": 4.717193882732605e-09
    },
    {
      "dtype": "torch.float64",
      "epsilon": 1e-05,
      "relative_gradient_error": 4.8471084135616566e-11
    },
    {
      "dtype": "torch.float64",
      "epsilon": 1e-06,
      "relative_gradient_error": 3.920737095483309e-11
    },
    {
      "dtype": "torch.float64",
      "epsilon": 1e-07,
      "relative_gradient_error": 6.254721919964258e-10
    },
    {
      "dtype": "torch.float64",
      "epsilon": 1e-08,
      "relative_gradient_error": 4.381693744945685e-09
    },
    {
      "dtype": "torch.float32",
      "epsilon": 0.1,
      "relative_gradient_error": 0.004691338142733932
    },
    {
      "dtype": "torch.float32",
      "epsilon": 0.01,
      "relative_gradient_error": 4.736755223734331e-05
    },
    {
      "dtype": "torch.float32",
      "epsilon": 0.001,
      "relative_gradient_error": 2.7235732610629574e-05
    },
    {
      "dtype": "torch.float32",
      "epsilon": 0.0001,
      "relative_gradient_error": 0.0004598346523993244
    },
    {
      "dtype": "torch.float32",
      "epsilon": 1e-05,
      "relative_gradient_error": 0.002543357456005712
    },
    {
      "dtype": "torch.float32",
      "epsilon": 1e-06,
      "relative_gradient_error": 0.024795025020756485
    },
    {
      "dtype": "torch.float32",
      "epsilon": 1e-07,
      "relative_gradient_error": 0.35368488321944797
    },
    {
      "dtype": "torch.float32",
      "epsilon": 1e-08,
      "relative_gradient_error": 1.0
    }
  ],
  "gradcheck_passed": true,
  "gradient_accumulation_factor": 2,
  "hidden_values": [
    -0.43819931483276775,
    0.40532130868946303
  ],
  "loss_after_update": 0.10712047414899839,
  "loss_before": 0.24064608322667733,
  "manual_gradient": [
    0.31390177075707465,
    -0.5381173212978423,
    -0.24350713749032066,
    0.417440807126264,
    -0.4484311010815353,
    0.3478673392718867,
    0.3040017549521085,
    -0.28119256463946446,
    -0.693752237079892
  ],
  "preactivations": [
    -0.47000000000000003,
    0.43000000000000005
  ],
  "prediction": -0.393752237079892
}
```

### code_105

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2205.

```json
{
  "depth": 12,
  "individual_profiles": [
    {
      "activation_SD": 0.4618794521469733,
      "condition": "Sigmoid large",
      "depth": 1,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.00037185087933768227,
      "inactive_or_saturated_fraction": 0.67138671875,
      "replicate": 0
    },
    {
      "activation_SD": 0.4504633552389273,
      "condition": "Sigmoid large",
      "depth": 2,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.0002913516341710464,
      "inactive_or_saturated_fraction": 0.579345703125,
      "replicate": 0
    },
    {
      "activation_SD": 0.43290734210712095,
      "condition": "Sigmoid large",
      "depth": 3,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.00037424665048754307,
      "inactive_or_saturated_fraction": 0.4951171875,
      "replicate": 0
    },
    {
      "activation_SD": 0.44382389029975544,
      "condition": "Sigmoid large",
      "depth": 4,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.00043737916232681643,
      "inactive_or_saturated_fraction": 0.54736328125,
      "replicate": 0
    },
    {
      "activation_SD": 0.4416113858311175,
      "condition": "Sigmoid large",
      "depth": 5,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.0007539765305031127,
      "inactive_or_saturated_fraction": 0.603515625,
      "replicate": 0
    },
    {
      "activation_SD": 0.4407341197837154,
      "condition": "Sigmoid large",
      "depth": 6,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.0006420652310295268,
      "inactive_or_saturated_fraction": 0.557373046875,
      "replicate": 0
    },
    {
      "activation_SD": 0.43029466649945086,
      "condition": "Sigmoid large",
      "depth": 7,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.0008972065433924262,
      "inactive_or_saturated_fraction": 0.502197265625,
      "replicate": 0
    },
    {
      "activation_SD": 0.4170597855935713,
      "condition": "Sigmoid large",
      "depth": 8,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.0009834811826776486,
      "inactive_or_saturated_fraction": 0.422607421875,
      "replicate": 0
    },
    {
      "activation_SD": 0.43170902822095175,
      "condition": "Sigmoid large",
      "depth": 9,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.000883959988653753,
      "inactive_or_saturated_fraction": 0.4794921875,
      "replicate": 0
    },
    {
      "activation_SD": 0.43189075470992755,
      "condition": "Sigmoid large",
      "depth": 10,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.0011807227177607807,
      "inactive_or_saturated_fraction": 0.452392578125,
      "replicate": 0
    },
    {
      "activation_SD": 0.4537122803585937,
      "condition": "Sigmoid large",
      "depth": 11,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.0015202462408641516,
      "inactive_or_saturated_fraction": 0.564453125,
      "replicate": 0
    },
    {
      "activation_SD": 0.4405066827160076,
      "condition": "Sigmoid large",
      "depth": 12,
      "final_loss": 0.49845214845568264,
      "gradient_RMS": 0.0019223088170455792,
      "inactive_or_saturated_fraction": 0.54150390625,
      "replicate": 0
    },
    {
      "activation_SD": 0.4606617857920438,
      "condition": "Sigmoid large",
      "depth": 1,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0006001500749075618,
      "inactive_or_saturated_fraction": 0.656494140625,
      "replicate": 1
    },
    {
      "activation_SD": 0.44790515068167497,
      "condition": "Sigmoid large",
      "depth": 2,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0005671416782300123,
      "inactive_or_saturated_fraction": 0.564208984375,
      "replicate": 1
    },
    {
      "activation_SD": 0.4332014450434925,
      "condition": "Sigmoid large",
      "depth": 3,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0005048943270360492,
      "inactive_or_saturated_fraction": 0.462646484375,
      "replicate": 1
    },
    {
      "activation_SD": 0.4518852034340019,
      "condition": "Sigmoid large",
      "depth": 4,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0005177622672139973,
      "inactive_or_saturated_fraction": 0.587158203125,
      "replicate": 1
    },
    {
      "activation_SD": 0.42334365875823093,
      "condition": "Sigmoid large",
      "depth": 5,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0009453932078510985,
      "inactive_or_saturated_fraction": 0.4443359375,
      "replicate": 1
    },
    {
      "activation_SD": 0.4323912888388557,
      "condition": "Sigmoid large",
      "depth": 6,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0007214009058597314,
      "inactive_or_saturated_fraction": 0.502685546875,
      "replicate": 1
    },
    {
      "activation_SD": 0.4488882430568456,
      "condition": "Sigmoid large",
      "depth": 7,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.000763775543992216,
      "inactive_or_saturated_fraction": 0.57177734375,
      "replicate": 1
    },
    {
      "activation_SD": 0.42973975598418507,
      "condition": "Sigmoid large",
      "depth": 8,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.000563644990291899,
      "inactive_or_saturated_fraction": 0.528076171875,
      "replicate": 1
    },
    {
      "activation_SD": 0.4603777016151596,
      "condition": "Sigmoid large",
      "depth": 9,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0009360181528318734,
      "inactive_or_saturated_fraction": 0.615234375,
      "replicate": 1
    },
    {
      "activation_SD": 0.4412888565440437,
      "condition": "Sigmoid large",
      "depth": 10,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0013546824028225722,
      "inactive_or_saturated_fraction": 0.54833984375,
      "replicate": 1
    },
    {
      "activation_SD": 0.4215604337670155,
      "condition": "Sigmoid large",
      "depth": 11,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0016203675482066064,
      "inactive_or_saturated_fraction": 0.552001953125,
      "replicate": 1
    },
    {
      "activation_SD": 0.44528321846876967,
      "condition": "Sigmoid large",
      "depth": 12,
      "final_loss": 0.4503579043284759,
      "gradient_RMS": 0.0013227357763856424,
      "inactive_or_saturated_fraction": 0.446044921875,
      "replicate": 1
    },
    {
      "activation_SD": 0.46307203071611325,
      "condition": "Sigmoid large",
      "depth": 1,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.00013340279220209987,
      "inactive_or_saturated_fraction": 0.674072265625,
      "replicate": 2
    },
    {
      "activation_SD": 0.4346110213268085,
      "condition": "Sigmoid large",
      "depth": 2,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.00012054267419854862,
      "inactive_or_saturated_fraction": 0.469482421875,
      "replicate": 2
    },
    {
      "activation_SD": 0.43401350958868584,
      "condition": "Sigmoid large",
      "depth": 3,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.0001423840446701398,
      "inactive_or_saturated_fraction": 0.499755859375,
      "replicate": 2
    },
    {
      "activation_SD": 0.43767512972145944,
      "condition": "Sigmoid large",
      "depth": 4,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.00014860367563680982,
      "inactive_or_saturated_fraction": 0.53271484375,
      "replicate": 2
    },
    {
      "activation_SD": 0.42973007832946375,
      "condition": "Sigmoid large",
      "depth": 5,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.0001843293099453042,
      "inactive_or_saturated_fraction": 0.59765625,
      "replicate": 2
    },
    {
      "activation_SD": 0.4200444234638663,
      "condition": "Sigmoid large",
      "depth": 6,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.00020619271648552464,
      "inactive_or_saturated_fraction": 0.382080078125,
      "replicate": 2
    },
    {
      "activation_SD": 0.43601496975529774,
      "condition": "Sigmoid large",
      "depth": 7,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.0002477418725898735,
      "inactive_or_saturated_fraction": 0.560546875,
      "replicate": 2
    },
    {
      "activation_SD": 0.38865578097772874,
      "condition": "Sigmoid large",
      "depth": 8,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.0003434996877673132,
      "inactive_or_saturated_fraction": 0.374755859375,
      "replicate": 2
    },
    {
      "activation_SD": 0.4465945763044076,
      "condition": "Sigmoid large",
      "depth": 9,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.0002572367487085983,
      "inactive_or_saturated_fraction": 0.563720703125,
      "replicate": 2
    },
    {
      "activation_SD": 0.4470464486166762,
      "condition": "Sigmoid large",
      "depth": 10,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.0003702224416184138,
      "inactive_or_saturated_fraction": 0.670166015625,
      "replicate": 2
    },
    {
      "activation_SD": 0.47027549752980985,
      "condition": "Sigmoid large",
      "depth": 11,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.001294365059270343,
      "inactive_or_saturated_fraction": 0.76904296875,
      "replicate": 2
    },
    {
      "activation_SD": 0.45653873011713175,
      "condition": "Sigmoid large",
      "depth": 12,
      "final_loss": 0.48275201460796846,
      "gradient_RMS": 0.002034809445199936,
      "inactive_or_saturated_fraction": 0.6123046875,
      "replicate": 2
    },
    {
      "activation_SD": 0.0033252236331559413,
      "condition": "ReLU tiny",
      "depth": 1,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 4.36390268720747e-58,
      "inactive_or_saturated_fraction": 0.487548828125,
      "replicate": 0
    },
    {
      "activation_SD": 1.4197009879103972e-05,
      "condition": "ReLU tiny",
      "depth": 2,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 8.914154779558117e-58,
      "inactive_or_saturated_fraction": 0.48046875,
      "replicate": 0
    },
    {
      "activation_SD": 5.3602528721183785e-08,
      "condition": "ReLU tiny",
      "depth": 3,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 1.3572985810507281e-57,
      "inactive_or_saturated_fraction": 0.450927734375,
      "replicate": 0
    },
    {
      "activation_SD": 2.1015969013068147e-10,
      "condition": "ReLU tiny",
      "depth": 4,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 1.357359585601491e-57,
      "inactive_or_saturated_fraction": 0.450927734375,
      "replicate": 0
    },
    {
      "activation_SD": 8.524162431451904e-13,
      "condition": "ReLU tiny",
      "depth": 5,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 1.9121160858232772e-57,
      "inactive_or_saturated_fraction": 0.584228515625,
      "replicate": 0
    },
    {
      "activation_SD": 3.076174249202455e-15,
      "condition": "ReLU tiny",
      "depth": 6,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 2.569945838818005e-57,
      "inactive_or_saturated_fraction": 0.5341796875,
      "replicate": 0
    },
    {
      "activation_SD": 9.950839070656184e-18,
      "condition": "ReLU tiny",
      "depth": 7,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 2.9532394023306715e-57,
      "inactive_or_saturated_fraction": 0.504150390625,
      "replicate": 0
    },
    {
      "activation_SD": 3.5520307992588304e-20,
      "condition": "ReLU tiny",
      "depth": 8,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 3.378720646645568e-57,
      "inactive_or_saturated_fraction": 0.541015625,
      "replicate": 0
    },
    {
      "activation_SD": 1.1893230946007288e-22,
      "condition": "ReLU tiny",
      "depth": 9,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 2.6929928108284224e-57,
      "inactive_or_saturated_fraction": 0.528564453125,
      "replicate": 0
    },
    {
      "activation_SD": 4.737117577999084e-25,
      "condition": "ReLU tiny",
      "depth": 10,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 1.887104161162954e-57,
      "inactive_or_saturated_fraction": 0.49267578125,
      "replicate": 0
    },
    {
      "activation_SD": 1.5200838875712067e-27,
      "condition": "ReLU tiny",
      "depth": 11,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 1.5579187287930935e-57,
      "inactive_or_saturated_fraction": 0.529052734375,
      "replicate": 0
    },
    {
      "activation_SD": 7.094628678537647e-30,
      "condition": "ReLU tiny",
      "depth": 12,
      "final_loss": 6.942820418466818e-59,
      "gradient_RMS": 8.286219716274016e-58,
      "inactive_or_saturated_fraction": 0.51708984375,
      "replicate": 0
    },
    {
      "activation_SD": 0.003171991244164124,
      "condition": "ReLU tiny",
      "depth": 1,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 6.229373722226337e-58,
      "inactive_or_saturated_fraction": 0.49609375,
      "replicate": 1
    },
    {
      "activation_SD": 1.2258544268053717e-05,
      "condition": "ReLU tiny",
      "depth": 2,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.0237101754747643e-57,
      "inactive_or_saturated_fraction": 0.535400390625,
      "replicate": 1
    },
    {
      "activation_SD": 4.745982752817338e-08,
      "condition": "ReLU tiny",
      "depth": 3,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.8124465130100825e-57,
      "inactive_or_saturated_fraction": 0.460205078125,
      "replicate": 1
    },
    {
      "activation_SD": 1.7741855283367373e-10,
      "condition": "ReLU tiny",
      "depth": 4,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.6275391515691457e-57,
      "inactive_or_saturated_fraction": 0.5380859375,
      "replicate": 1
    },
    {
      "activation_SD": 4.989962086887249e-13,
      "condition": "ReLU tiny",
      "depth": 5,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.8119761934989913e-57,
      "inactive_or_saturated_fraction": 0.536865234375,
      "replicate": 1
    },
    {
      "activation_SD": 1.965559507425777e-15,
      "condition": "ReLU tiny",
      "depth": 6,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.2672566676906423e-57,
      "inactive_or_saturated_fraction": 0.4658203125,
      "replicate": 1
    },
    {
      "activation_SD": 8.143212881223142e-18,
      "condition": "ReLU tiny",
      "depth": 7,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.1099857187938506e-57,
      "inactive_or_saturated_fraction": 0.547607421875,
      "replicate": 1
    },
    {
      "activation_SD": 4.2880201139030763e-20,
      "condition": "ReLU tiny",
      "depth": 8,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.0622634012412707e-57,
      "inactive_or_saturated_fraction": 0.380859375,
      "replicate": 1
    },
    {
      "activation_SD": 1.4544221145307857e-22,
      "condition": "ReLU tiny",
      "depth": 9,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.3245750253110442e-57,
      "inactive_or_saturated_fraction": 0.5908203125,
      "replicate": 1
    },
    {
      "activation_SD": 7.769856185937781e-25,
      "condition": "ReLU tiny",
      "depth": 10,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.0360943351933987e-57,
      "inactive_or_saturated_fraction": 0.497314453125,
      "replicate": 1
    },
    {
      "activation_SD": 2.0821025081464195e-27,
      "condition": "ReLU tiny",
      "depth": 11,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.8398630154019043e-57,
      "inactive_or_saturated_fraction": 0.524169921875,
      "replicate": 1
    },
    {
      "activation_SD": 6.631155899746713e-30,
      "condition": "ReLU tiny",
      "depth": 12,
      "final_loss": 6.493753531332998e-59,
      "gradient_RMS": 1.1087445470056699e-57,
      "inactive_or_saturated_fraction": 0.44677734375,
      "replicate": 1
    },
    {
      "activation_SD": 0.0031968096214962443,
      "condition": "ReLU tiny",
      "depth": 1,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 7.976956818911583e-58,
      "inactive_or_saturated_fraction": 0.505859375,
      "replicate": 2
    },
    {
      "activation_SD": 1.1248340143294839e-05,
      "condition": "ReLU tiny",
      "depth": 2,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 1.9309645790607683e-57,
      "inactive_or_saturated_fraction": 0.5244140625,
      "replicate": 2
    },
    {
      "activation_SD": 4.433816360635451e-08,
      "condition": "ReLU tiny",
      "depth": 3,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 2.127453143049501e-57,
      "inactive_or_saturated_fraction": 0.4521484375,
      "replicate": 2
    },
    {
      "activation_SD": 2.0143304977949176e-10,
      "condition": "ReLU tiny",
      "depth": 4,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 2.152768316882297e-57,
      "inactive_or_saturated_fraction": 0.430908203125,
      "replicate": 2
    },
    {
      "activation_SD": 7.725368640285935e-13,
      "condition": "ReLU tiny",
      "depth": 5,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 2.884746371892218e-57,
      "inactive_or_saturated_fraction": 0.633056640625,
      "replicate": 2
    },
    {
      "activation_SD": 2.3554492918285387e-15,
      "condition": "ReLU tiny",
      "depth": 6,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 3.6286412654467356e-57,
      "inactive_or_saturated_fraction": 0.481689453125,
      "replicate": 2
    },
    {
      "activation_SD": 1.0341971773198628e-17,
      "condition": "ReLU tiny",
      "depth": 7,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 3.296345878178607e-57,
      "inactive_or_saturated_fraction": 0.415283203125,
      "replicate": 2
    },
    {
      "activation_SD": 3.851410999541877e-20,
      "condition": "ReLU tiny",
      "depth": 8,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 2.914643766436679e-57,
      "inactive_or_saturated_fraction": 0.502685546875,
      "replicate": 2
    },
    {
      "activation_SD": 1.5797658212556754e-22,
      "condition": "ReLU tiny",
      "depth": 9,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 2.273577192318978e-57,
      "inactive_or_saturated_fraction": 0.5791015625,
      "replicate": 2
    },
    {
      "activation_SD": 7.073438566359485e-25,
      "condition": "ReLU tiny",
      "depth": 10,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 2.574350503422988e-57,
      "inactive_or_saturated_fraction": 0.412841796875,
      "replicate": 2
    },
    {
      "activation_SD": 2.8874818603463317e-27,
      "condition": "ReLU tiny",
      "depth": 11,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 2.5411811662326227e-57,
      "inactive_or_saturated_fraction": 0.527587890625,
      "replicate": 2
    },
    {
      "activation_SD": 9.355279133163535e-30,
      "condition": "ReLU tiny",
      "depth": 12,
      "final_loss": 1.2394400314673682e-58,
      "gradient_RMS": 2.3072200381113065e-57,
      "inactive_or_saturated_fraction": 0.455078125,
      "replicate": 2
    },
    {
      "activation_SD": 6.650447266311772,
      "condition": "ReLU large",
      "depth": 1,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 3.6607068993130056e+18,
      "inactive_or_saturated_fraction": 0.487548828125,
      "replicate": 0
    },
    {
      "activation_SD": 56.7880395164174,
      "condition": "ReLU large",
      "depth": 2,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 7.47773500970394e+18,
      "inactive_or_saturated_fraction": 0.48046875,
      "replicate": 0
    },
    {
      "activation_SD": 428.8202297694658,
      "condition": "ReLU large",
      "depth": 3,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 1.1385845735390777e+19,
      "inactive_or_saturated_fraction": 0.450927734375,
      "replicate": 0
    },
    {
      "activation_SD": 3362.5550420909335,
      "condition": "ReLU large",
      "depth": 4,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 1.1386357478653342e+19,
      "inactive_or_saturated_fraction": 0.450927734375,
      "replicate": 0
    },
    {
      "activation_SD": 27277.319780646034,
      "condition": "ReLU large",
      "depth": 5,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 1.6039992294465817e+19,
      "inactive_or_saturated_fraction": 0.584228515625,
      "replicate": 0
    },
    {
      "activation_SD": 196875.15194895474,
      "condition": "ReLU large",
      "depth": 6,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 2.1558268223075414e+19,
      "inactive_or_saturated_fraction": 0.5341796875,
      "replicate": 0
    },
    {
      "activation_SD": 1273707.4010440109,
      "condition": "ReLU large",
      "depth": 7,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 2.4773567676306272e+19,
      "inactive_or_saturated_fraction": 0.504150390625,
      "replicate": 0
    },
    {
      "activation_SD": 9093198.846102715,
      "condition": "ReLU large",
      "depth": 8,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 2.8342763046216163e+19,
      "inactive_or_saturated_fraction": 0.541015625,
      "replicate": 0
    },
    {
      "activation_SD": 60893342.44355943,
      "condition": "ReLU large",
      "depth": 9,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 2.259046103685778e+19,
      "inactive_or_saturated_fraction": 0.528564453125,
      "replicate": 0
    },
    {
      "activation_SD": 485080839.98711944,
      "condition": "ReLU large",
      "depth": 10,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 1.5830177063164834e+19,
      "inactive_or_saturated_fraction": 0.49267578125,
      "replicate": 0
    },
    {
      "activation_SD": 3113131801.7458224,
      "condition": "ReLU large",
      "depth": 11,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 1.3068769511703568e+19,
      "inactive_or_saturated_fraction": 0.529052734375,
      "replicate": 0
    },
    {
      "activation_SD": 29059599067.28936,
      "condition": "ReLU large",
      "depth": 12,
      "final_loss": 1.164811978098281e+21,
      "gradient_RMS": 6.950984900169389e+18,
      "inactive_or_saturated_fraction": 0.51708984375,
      "replicate": 0
    },
    {
      "activation_SD": 6.343982488328268,
      "condition": "ReLU large",
      "depth": 1,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 5.225577424125762e+18,
      "inactive_or_saturated_fraction": 0.49609375,
      "replicate": 1
    },
    {
      "activation_SD": 49.03417707221507,
      "condition": "ReLU large",
      "depth": 2,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 8.587503367669008e+18,
      "inactive_or_saturated_fraction": 0.535400390625,
      "replicate": 1
    },
    {
      "activation_SD": 379.6786202253939,
      "condition": "ReLU large",
      "depth": 3,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 1.5203903318608478e+19,
      "inactive_or_saturated_fraction": 0.460205078125,
      "replicate": 1
    },
    {
      "activation_SD": 2838.696845338755,
      "condition": "ReLU large",
      "depth": 4,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 1.3652787947166142e+19,
      "inactive_or_saturated_fraction": 0.5380859375,
      "replicate": 1
    },
    {
      "activation_SD": 15967.878678038724,
      "condition": "ReLU large",
      "depth": 5,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 1.519995799259518e+19,
      "inactive_or_saturated_fraction": 0.536865234375,
      "replicate": 1
    },
    {
      "activation_SD": 125795.80847524974,
      "condition": "ReLU large",
      "depth": 6,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 1.063051942064306e+19,
      "inactive_or_saturated_fraction": 0.4658203125,
      "replicate": 1
    },
    {
      "activation_SD": 1042331.2487965687,
      "condition": "ReLU large",
      "depth": 7,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 9.311235080559841e+18,
      "inactive_or_saturated_fraction": 0.547607421875,
      "replicate": 1
    },
    {
      "activation_SD": 10977331.49159179,
      "condition": "ReLU large",
      "depth": 8,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 8.91091126575973e+18,
      "inactive_or_saturated_fraction": 0.380859375,
      "replicate": 1
    },
    {
      "activation_SD": 74466412.26397704,
      "condition": "ReLU large",
      "depth": 9,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 1.1111340653924426e+19,
      "inactive_or_saturated_fraction": 0.5908203125,
      "replicate": 1
    },
    {
      "activation_SD": 795633273.4400208,
      "condition": "ReLU large",
      "depth": 10,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 8.691389228958026e+18,
      "inactive_or_saturated_fraction": 0.497314453125,
      "replicate": 1
    },
    {
      "activation_SD": 4264145936.6839247,
      "condition": "ReLU large",
      "depth": 11,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 1.5433889609904531e+19,
      "inactive_or_saturated_fraction": 0.524169921875,
      "replicate": 1
    },
    {
      "activation_SD": 27161214565.362892,
      "condition": "ReLU large",
      "depth": 12,
      "final_loss": 1.0894710564593643e+21,
      "gradient_RMS": 9.300823376968137e+18,
      "inactive_or_saturated_fraction": 0.44677734375,
      "replicate": 1
    },
    {
      "activation_SD": 6.393619242992317,
      "condition": "ReLU large",
      "depth": 1,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 6.691556378677623e+18,
      "inactive_or_saturated_fraction": 0.505859375,
      "replicate": 2
    },
    {
      "activation_SD": 44.99336057318,
      "condition": "ReLU large",
      "depth": 2,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 1.6198104915625783e+19,
      "inactive_or_saturated_fraction": 0.5244140625,
      "replicate": 2
    },
    {
      "activation_SD": 354.70530885083997,
      "condition": "ReLU large",
      "depth": 3,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 1.7846370455410178e+19,
      "inactive_or_saturated_fraction": 0.4521484375,
      "replicate": 2
    },
    {
      "activation_SD": 3222.9287964719733,
      "condition": "ReLU large",
      "depth": 4,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 1.805872952514536e+19,
      "inactive_or_saturated_fraction": 0.430908203125,
      "replicate": 2
    },
    {
      "activation_SD": 24721.17964891561,
      "condition": "ReLU large",
      "depth": 5,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 2.4199006493226025e+19,
      "inactive_or_saturated_fraction": 0.633056640625,
      "replicate": 2
    },
    {
      "activation_SD": 150748.75467702554,
      "condition": "ReLU large",
      "depth": 6,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 3.0439249148456595e+19,
      "inactive_or_saturated_fraction": 0.481689453125,
      "replicate": 2
    },
    {
      "activation_SD": 1323772.386969414,
      "condition": "ReLU large",
      "depth": 7,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 2.7651753404456075e+19,
      "inactive_or_saturated_fraction": 0.415283203125,
      "replicate": 2
    },
    {
      "activation_SD": 9859612.158827126,
      "condition": "ReLU large",
      "depth": 8,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 2.4449804016280842e+19,
      "inactive_or_saturated_fraction": 0.502685546875,
      "replicate": 2
    },
    {
      "activation_SD": 80884010.04829198,
      "condition": "ReLU large",
      "depth": 9,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 1.9072147824104505e+19,
      "inactive_or_saturated_fraction": 0.5791015625,
      "replicate": 2
    },
    {
      "activation_SD": 724320109.1952088,
      "condition": "ReLU large",
      "depth": 10,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 2.1595217227818095e+19,
      "inactive_or_saturated_fraction": 0.412841796875,
      "replicate": 2
    },
    {
      "activation_SD": 5913562849.989242,
      "condition": "ReLU large",
      "depth": 11,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 2.13169726605083e+19,
      "inactive_or_saturated_fraction": 0.527587890625,
      "replicate": 2
    },
    {
      "activation_SD": 38319223329.43823,
      "condition": "ReLU large",
      "depth": 12,
      "final_loss": 2.0794353126974827e+21,
      "gradient_RMS": 1.9354364469460804e+19,
      "inactive_or_saturated_fraction": 0.455078125,
      "replicate": 2
    },
    {
      "activation_SD": 0.8313059082889716,
      "condition": "ReLU Kaiming",
      "depth": 1,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.006201478707918493,
      "inactive_or_saturated_fraction": 0.487548828125,
      "replicate": 0
    },
    {
      "activation_SD": 0.8873131174440219,
      "condition": "ReLU Kaiming",
      "depth": 2,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.012667775848112385,
      "inactive_or_saturated_fraction": 0.48046875,
      "replicate": 0
    },
    {
      "activation_SD": 0.8375395112684879,
      "condition": "ReLU Kaiming",
      "depth": 3,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.019288372940461714,
      "inactive_or_saturated_fraction": 0.450927734375,
      "replicate": 0
    },
    {
      "activation_SD": 0.8209362895729818,
      "condition": "ReLU Kaiming",
      "depth": 4,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.01928923986726957,
      "inactive_or_saturated_fraction": 0.450927734375,
      "replicate": 0
    },
    {
      "activation_SD": 0.8324377374464732,
      "condition": "ReLU Kaiming",
      "depth": 5,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.027172803894235296,
      "inactive_or_saturated_fraction": 0.584228515625,
      "replicate": 0
    },
    {
      "activation_SD": 0.751019103809184,
      "condition": "ReLU Kaiming",
      "depth": 6,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.03652112694138059,
      "inactive_or_saturated_fraction": 0.5341796875,
      "replicate": 0
    },
    {
      "activation_SD": 0.6073510174961142,
      "condition": "ReLU Kaiming",
      "depth": 7,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.04196805608573114,
      "inactive_or_saturated_fraction": 0.504150390625,
      "replicate": 0
    },
    {
      "activation_SD": 0.5419968870939442,
      "condition": "ReLU Kaiming",
      "depth": 8,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.0480145082327335,
      "inactive_or_saturated_fraction": 0.541015625,
      "replicate": 0
    },
    {
      "activation_SD": 0.4536907556918221,
      "condition": "ReLU Kaiming",
      "depth": 9,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.03826972958376616,
      "inactive_or_saturated_fraction": 0.528564453125,
      "replicate": 0
    },
    {
      "activation_SD": 0.45176673679344304,
      "condition": "ReLU Kaiming",
      "depth": 10,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.026817363066739867,
      "inactive_or_saturated_fraction": 0.49267578125,
      "replicate": 0
    },
    {
      "activation_SD": 0.36241624058990535,
      "condition": "ReLU Kaiming",
      "depth": 11,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.022139356712970834,
      "inactive_or_saturated_fraction": 0.529052734375,
      "replicate": 0
    },
    {
      "activation_SD": 0.4228728221975232,
      "condition": "ReLU Kaiming",
      "depth": 12,
      "final_loss": 0.24665853070142463,
      "gradient_RMS": 0.011775426452621232,
      "inactive_or_saturated_fraction": 0.51708984375,
      "replicate": 0
    },
    {
      "activation_SD": 0.7929978110410335,
      "condition": "ReLU Kaiming",
      "depth": 1,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.008852472493325558,
      "inactive_or_saturated_fraction": 0.49609375,
      "replicate": 1
    },
    {
      "activation_SD": 0.7661590167533605,
      "condition": "ReLU Kaiming",
      "depth": 2,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.01454779657414582,
      "inactive_or_saturated_fraction": 0.535400390625,
      "replicate": 1
    },
    {
      "activation_SD": 0.7415598051277225,
      "condition": "ReLU Kaiming",
      "depth": 3,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.025756414075460754,
      "inactive_or_saturated_fraction": 0.460205078125,
      "replicate": 1
    },
    {
      "activation_SD": 0.693041222006532,
      "condition": "ReLU Kaiming",
      "depth": 4,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.023128722426252253,
      "inactive_or_saturated_fraction": 0.5380859375,
      "replicate": 1
    },
    {
      "activation_SD": 0.48730098504756847,
      "condition": "ReLU Kaiming",
      "depth": 5,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.025749730433218907,
      "inactive_or_saturated_fraction": 0.536865234375,
      "replicate": 1
    },
    {
      "activation_SD": 0.4798729266176214,
      "condition": "ReLU Kaiming",
      "depth": 6,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.018008800391422736,
      "inactive_or_saturated_fraction": 0.4658203125,
      "replicate": 1
    },
    {
      "activation_SD": 0.4970222705824703,
      "condition": "ReLU Kaiming",
      "depth": 7,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.01577384578572847,
      "inactive_or_saturated_fraction": 0.547607421875,
      "replicate": 1
    },
    {
      "activation_SD": 0.6542999441380376,
      "condition": "ReLU Kaiming",
      "depth": 8,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.015095670864316024,
      "inactive_or_saturated_fraction": 0.380859375,
      "replicate": 1
    },
    {
      "activation_SD": 0.5548180063365179,
      "condition": "ReLU Kaiming",
      "depth": 9,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.018823343244080262,
      "inactive_or_saturated_fraction": 0.5908203125,
      "replicate": 1
    },
    {
      "activation_SD": 0.7409912286699012,
      "condition": "ReLU Kaiming",
      "depth": 10,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.014723786068677195,
      "inactive_or_saturated_fraction": 0.497314453125,
      "replicate": 1
    },
    {
      "activation_SD": 0.4964119215360755,
      "condition": "ReLU Kaiming",
      "depth": 11,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.026146026007749918,
      "inactive_or_saturated_fraction": 0.524169921875,
      "replicate": 1
    },
    {
      "activation_SD": 0.3952476918546438,
      "condition": "ReLU Kaiming",
      "depth": 12,
      "final_loss": 0.2307044699752579,
      "gradient_RMS": 0.01575620767377003,
      "inactive_or_saturated_fraction": 0.44677734375,
      "replicate": 1
    },
    {
      "activation_SD": 0.7992024053740396,
      "condition": "ReLU Kaiming",
      "depth": 1,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.01133593744229924,
      "inactive_or_saturated_fraction": 0.505859375,
      "replicate": 2
    },
    {
      "activation_SD": 0.7030212589559375,
      "condition": "ReLU Kaiming",
      "depth": 2,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.027440657093233754,
      "inactive_or_saturated_fraction": 0.5244140625,
      "replicate": 2
    },
    {
      "activation_SD": 0.6927838063492968,
      "condition": "ReLU Kaiming",
      "depth": 3,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.030232927529276307,
      "inactive_or_saturated_fraction": 0.4521484375,
      "replicate": 2
    },
    {
      "activation_SD": 0.7868478507011654,
      "condition": "ReLU Kaiming",
      "depth": 4,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.030592677786704253,
      "inactive_or_saturated_fraction": 0.430908203125,
      "replicate": 2
    },
    {
      "activation_SD": 0.7544305312779422,
      "condition": "ReLU Kaiming",
      "depth": 5,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.04099471158116638,
      "inactive_or_saturated_fraction": 0.633056640625,
      "replicate": 2
    },
    {
      "activation_SD": 0.5750608622628233,
      "condition": "ReLU Kaiming",
      "depth": 6,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.051566093836850284,
      "inactive_or_saturated_fraction": 0.481689453125,
      "replicate": 2
    },
    {
      "activation_SD": 0.6312238631102629,
      "condition": "ReLU Kaiming",
      "depth": 7,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.046843892365851125,
      "inactive_or_saturated_fraction": 0.415283203125,
      "replicate": 2
    },
    {
      "activation_SD": 0.5876786803500131,
      "condition": "ReLU Kaiming",
      "depth": 8,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.04141957911140078,
      "inactive_or_saturated_fraction": 0.502685546875,
      "replicate": 2
    },
    {
      "activation_SD": 0.6026328358671962,
      "condition": "ReLU Kaiming",
      "depth": 9,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.03230947516384186,
      "inactive_or_saturated_fraction": 0.5791015625,
      "replicate": 2
    },
    {
      "activation_SD": 0.6745756689414464,
      "condition": "ReLU Kaiming",
      "depth": 10,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.036583720990151204,
      "inactive_or_saturated_fraction": 0.412841796875,
      "replicate": 2
    },
    {
      "activation_SD": 0.6884293223253034,
      "condition": "ReLU Kaiming",
      "depth": 11,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.03611235635833938,
      "inactive_or_saturated_fraction": 0.527587890625,
      "replicate": 2
    },
    {
      "activation_SD": 0.5576180895068426,
      "condition": "ReLU Kaiming",
      "depth": 12,
      "final_loss": 0.4403375553847041,
      "gradient_RMS": 0.032787568757602595,
      "inactive_or_saturated_fraction": 0.455078125,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 1,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 2,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 3,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 4,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 5,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 6,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 7,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 8,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 9,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 10,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 11,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 12,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 0
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 1,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 2,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 3,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 4,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 5,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 6,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 7,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 8,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 9,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 10,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 11,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 12,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 1
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 1,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 2,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 3,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 4,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 5,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 6,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 7,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 8,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 9,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 10,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 11,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.0,
      "condition": "ReLU dead",
      "depth": 12,
      "final_loss": 0.0,
      "gradient_RMS": 0.0,
      "inactive_or_saturated_fraction": 1.0,
      "replicate": 2
    },
    {
      "activation_SD": 0.7522317473198511,
      "condition": "Tanh Xavier",
      "depth": 1,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.004043780089942958,
      "inactive_or_saturated_fraction": 0.103271484375,
      "replicate": 0
    },
    {
      "activation_SD": 0.6958541739481793,
      "condition": "Tanh Xavier",
      "depth": 2,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.0032903092160079376,
      "inactive_or_saturated_fraction": 0.0400390625,
      "replicate": 0
    },
    {
      "activation_SD": 0.6663451968117646,
      "condition": "Tanh Xavier",
      "depth": 3,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.003036272656384649,
      "inactive_or_saturated_fraction": 0.018310546875,
      "replicate": 0
    },
    {
      "activation_SD": 0.6671470731278154,
      "condition": "Tanh Xavier",
      "depth": 4,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.0027680309812911615,
      "inactive_or_saturated_fraction": 0.018310546875,
      "replicate": 0
    },
    {
      "activation_SD": 0.6475217039007467,
      "condition": "Tanh Xavier",
      "depth": 5,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.0028385552442788424,
      "inactive_or_saturated_fraction": 0.0185546875,
      "replicate": 0
    },
    {
      "activation_SD": 0.6406670391758988,
      "condition": "Tanh Xavier",
      "depth": 6,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.0025699280408491313,
      "inactive_or_saturated_fraction": 0.010986328125,
      "replicate": 0
    },
    {
      "activation_SD": 0.6549362388788678,
      "condition": "Tanh Xavier",
      "depth": 7,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.003057991173097428,
      "inactive_or_saturated_fraction": 0.024169921875,
      "replicate": 0
    },
    {
      "activation_SD": 0.6358077500548998,
      "condition": "Tanh Xavier",
      "depth": 8,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.00321219273843114,
      "inactive_or_saturated_fraction": 0.013916015625,
      "replicate": 0
    },
    {
      "activation_SD": 0.635163524485751,
      "condition": "Tanh Xavier",
      "depth": 9,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.003385942472573791,
      "inactive_or_saturated_fraction": 0.012939453125,
      "replicate": 0
    },
    {
      "activation_SD": 0.6678549094837755,
      "condition": "Tanh Xavier",
      "depth": 10,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.003226690538621077,
      "inactive_or_saturated_fraction": 0.008544921875,
      "replicate": 0
    },
    {
      "activation_SD": 0.690155034535473,
      "condition": "Tanh Xavier",
      "depth": 11,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.0033172252040711736,
      "inactive_or_saturated_fraction": 0.017333984375,
      "replicate": 0
    },
    {
      "activation_SD": 0.6757197760078695,
      "condition": "Tanh Xavier",
      "depth": 12,
      "final_loss": 0.45661191446864746,
      "gradient_RMS": 0.003943769221285698,
      "inactive_or_saturated_fraction": 0.023193359375,
      "replicate": 0
    },
    {
      "activation_SD": 0.7404885282313522,
      "condition": "Tanh Xavier",
      "depth": 1,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.0034268121766405364,
      "inactive_or_saturated_fraction": 0.093017578125,
      "replicate": 1
    },
    {
      "activation_SD": 0.6874159948782216,
      "condition": "Tanh Xavier",
      "depth": 2,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.002827528292168597,
      "inactive_or_saturated_fraction": 0.030517578125,
      "replicate": 1
    },
    {
      "activation_SD": 0.6810033783521832,
      "condition": "Tanh Xavier",
      "depth": 3,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.002508658039590848,
      "inactive_or_saturated_fraction": 0.02685546875,
      "replicate": 1
    },
    {
      "activation_SD": 0.6598982958061906,
      "condition": "Tanh Xavier",
      "depth": 4,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.002221890427190906,
      "inactive_or_saturated_fraction": 0.02001953125,
      "replicate": 1
    },
    {
      "activation_SD": 0.6704542998037067,
      "condition": "Tanh Xavier",
      "depth": 5,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.002113606360973576,
      "inactive_or_saturated_fraction": 0.02099609375,
      "replicate": 1
    },
    {
      "activation_SD": 0.6735955539710209,
      "condition": "Tanh Xavier",
      "depth": 6,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.0021993610579431827,
      "inactive_or_saturated_fraction": 0.020263671875,
      "replicate": 1
    },
    {
      "activation_SD": 0.6448999808648196,
      "condition": "Tanh Xavier",
      "depth": 7,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.0023800533998672045,
      "inactive_or_saturated_fraction": 0.01513671875,
      "replicate": 1
    },
    {
      "activation_SD": 0.6718857310369436,
      "condition": "Tanh Xavier",
      "depth": 8,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.0027019387789378358,
      "inactive_or_saturated_fraction": 0.01513671875,
      "replicate": 1
    },
    {
      "activation_SD": 0.6860464330478176,
      "condition": "Tanh Xavier",
      "depth": 9,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.002584262332068833,
      "inactive_or_saturated_fraction": 0.029052734375,
      "replicate": 1
    },
    {
      "activation_SD": 0.6574676827743557,
      "condition": "Tanh Xavier",
      "depth": 10,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.003263461760087641,
      "inactive_or_saturated_fraction": 0.00634765625,
      "replicate": 1
    },
    {
      "activation_SD": 0.6528325984684308,
      "condition": "Tanh Xavier",
      "depth": 11,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.003473750472163665,
      "inactive_or_saturated_fraction": 0.014404296875,
      "replicate": 1
    },
    {
      "activation_SD": 0.6353377676402365,
      "condition": "Tanh Xavier",
      "depth": 12,
      "final_loss": 0.4036953308809399,
      "gradient_RMS": 0.003364915330014196,
      "inactive_or_saturated_fraction": 0.01708984375,
      "replicate": 1
    },
    {
      "activation_SD": 0.754873520050036,
      "condition": "Tanh Xavier",
      "depth": 1,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.00301607824733335,
      "inactive_or_saturated_fraction": 0.10498046875,
      "replicate": 2
    },
    {
      "activation_SD": 0.6858737688160608,
      "condition": "Tanh Xavier",
      "depth": 2,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.002806319301356032,
      "inactive_or_saturated_fraction": 0.031494140625,
      "replicate": 2
    },
    {
      "activation_SD": 0.6619664178891089,
      "condition": "Tanh Xavier",
      "depth": 3,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.002464652909860479,
      "inactive_or_saturated_fraction": 0.018310546875,
      "replicate": 2
    },
    {
      "activation_SD": 0.6621116605711331,
      "condition": "Tanh Xavier",
      "depth": 4,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.002500219271571064,
      "inactive_or_saturated_fraction": 0.02294921875,
      "replicate": 2
    },
    {
      "activation_SD": 0.6450979255889651,
      "condition": "Tanh Xavier",
      "depth": 5,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.0025238334173707886,
      "inactive_or_saturated_fraction": 0.015625,
      "replicate": 2
    },
    {
      "activation_SD": 0.654989537124042,
      "condition": "Tanh Xavier",
      "depth": 6,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.002764189019300819,
      "inactive_or_saturated_fraction": 0.02490234375,
      "replicate": 2
    },
    {
      "activation_SD": 0.6576568788103312,
      "condition": "Tanh Xavier",
      "depth": 7,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.002548981795169871,
      "inactive_or_saturated_fraction": 0.009521484375,
      "replicate": 2
    },
    {
      "activation_SD": 0.6540567693936901,
      "condition": "Tanh Xavier",
      "depth": 8,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.002945823346593042,
      "inactive_or_saturated_fraction": 0.01611328125,
      "replicate": 2
    },
    {
      "activation_SD": 0.6415933167232365,
      "condition": "Tanh Xavier",
      "depth": 9,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.003172595434362759,
      "inactive_or_saturated_fraction": 0.015380859375,
      "replicate": 2
    },
    {
      "activation_SD": 0.6240972943307657,
      "condition": "Tanh Xavier",
      "depth": 10,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.003083311298896987,
      "inactive_or_saturated_fraction": 0.013427734375,
      "replicate": 2
    },
    {
      "activation_SD": 0.6482660033342355,
      "condition": "Tanh Xavier",
      "depth": 11,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.003225862071806407,
      "inactive_or_saturated_fraction": 0.014404296875,
      "replicate": 2
    },
    {
      "activation_SD": 0.6342986820706473,
      "condition": "Tanh Xavier",
      "depth": 12,
      "final_loss": 0.4023474594690518,
      "gradient_RMS": 0.0036438499638981802,
      "inactive_or_saturated_fraction": 0.005859375,
      "replicate": 2
    }
  ],
  "loss_contract": "mean square of final hidden activations",
  "profiles": [
    {
      "condition": "ReLU Kaiming",
      "depth": 1,
      "mean_activation_SD": 0.8078353749013484,
      "mean_gradient_RMS": 0.008796629547847762,
      "mean_inactive_or_saturated_fraction": 0.4965006510416667
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 2,
      "mean_activation_SD": 0.7854977977177734,
      "mean_gradient_RMS": 0.018218743171830653,
      "mean_inactive_or_saturated_fraction": 0.513427734375
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 3,
      "mean_activation_SD": 0.7572943742485023,
      "mean_gradient_RMS": 0.025092571515066258,
      "mean_inactive_or_saturated_fraction": 0.4544270833333333
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 4,
      "mean_activation_SD": 0.766941787426893,
      "mean_gradient_RMS": 0.024336880026742027,
      "mean_inactive_or_saturated_fraction": 0.4733072916666667
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 5,
      "mean_activation_SD": 0.6913897512573279,
      "mean_gradient_RMS": 0.03130574863620686,
      "mean_inactive_or_saturated_fraction": 0.584716796875
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 6,
      "mean_activation_SD": 0.6019842975632096,
      "mean_gradient_RMS": 0.035365340389884536,
      "mean_inactive_or_saturated_fraction": 0.493896484375
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 7,
      "mean_activation_SD": 0.5785323837296158,
      "mean_gradient_RMS": 0.03486193141243691,
      "mean_inactive_or_saturated_fraction": 0.489013671875
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 8,
      "mean_activation_SD": 0.594658503860665,
      "mean_gradient_RMS": 0.034843252736150104,
      "mean_inactive_or_saturated_fraction": 0.474853515625
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 9,
      "mean_activation_SD": 0.5370471992985121,
      "mean_gradient_RMS": 0.029800849330562762,
      "mean_inactive_or_saturated_fraction": 0.566162109375
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 10,
      "mean_activation_SD": 0.6224445448015968,
      "mean_gradient_RMS": 0.02604162337518942,
      "mean_inactive_or_saturated_fraction": 0.4676106770833333
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 11,
      "mean_activation_SD": 0.5157524948170947,
      "mean_gradient_RMS": 0.02813257969302004,
      "mean_inactive_or_saturated_fraction": 0.5269368489583334
    },
    {
      "condition": "ReLU Kaiming",
      "depth": 12,
      "mean_activation_SD": 0.4585795345196699,
      "mean_gradient_RMS": 0.020106400961331285,
      "mean_inactive_or_saturated_fraction": 0.4729817708333333
    },
    {
      "condition": "ReLU dead",
      "depth": 1,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 2,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 3,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 4,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 5,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 6,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 7,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 8,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 9,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 10,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 11,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU dead",
      "depth": 12,
      "mean_activation_SD": 0.0,
      "mean_gradient_RMS": 0.0,
      "mean_inactive_or_saturated_fraction": 1.0
    },
    {
      "condition": "ReLU large",
      "depth": 1,
      "mean_activation_SD": 6.462682999210787,
      "mean_gradient_RMS": 5.192613567372129e+18,
      "mean_inactive_or_saturated_fraction": 0.4965006510416667
    },
    {
      "condition": "ReLU large",
      "depth": 2,
      "mean_activation_SD": 50.2718590539375,
      "mean_gradient_RMS": 1.075444776433291e+19,
      "mean_inactive_or_saturated_fraction": 0.513427734375
    },
    {
      "condition": "ReLU large",
      "depth": 3,
      "mean_activation_SD": 387.7347196152332,
      "mean_gradient_RMS": 1.4812039836469811e+19,
      "mean_inactive_or_saturated_fraction": 0.4544270833333333
    },
    {
      "condition": "ReLU large",
      "depth": 4,
      "mean_activation_SD": 3141.3935613005538,
      "mean_gradient_RMS": 1.4365958316988283e+19,
      "mean_inactive_or_saturated_fraction": 0.4733072916666667
    },
    {
      "condition": "ReLU large",
      "depth": 5,
      "mean_activation_SD": 22655.45936920012,
      "mean_gradient_RMS": 1.8479652260095672e+19,
      "mean_inactive_or_saturated_fraction": 0.584716796875
    },
    {
      "condition": "ReLU large",
      "depth": 6,
      "mean_activation_SD": 157806.57170041002,
      "mean_gradient_RMS": 2.0876012264058356e+19,
      "mean_inactive_or_saturated_fraction": 0.493896484375
    },
    {
      "condition": "ReLU large",
      "depth": 7,
      "mean_activation_SD": 1213270.3456033312,
      "mean_gradient_RMS": 2.057885205377406e+19,
      "mean_inactive_or_saturated_fraction": 0.489013671875
    },
    {
      "condition": "ReLU large",
      "depth": 8,
      "mean_activation_SD": 9976714.16550721,
      "mean_gradient_RMS": 2.0567826109418914e+19,
      "mean_inactive_or_saturated_fraction": 0.474853515625
    },
    {
      "condition": "ReLU large",
      "depth": 9,
      "mean_activation_SD": 72081254.91860949,
      "mean_gradient_RMS": 1.7591316504962236e+19,
      "mean_inactive_or_saturated_fraction": 0.566162109375
    },
    {
      "condition": "ReLU large",
      "depth": 10,
      "mean_activation_SD": 668344740.8741163,
      "mean_gradient_RMS": 1.537226117331365e+19,
      "mean_inactive_or_saturated_fraction": 0.4676106770833333
    },
    {
      "condition": "ReLU large",
      "depth": 11,
      "mean_activation_SD": 4430280196.139663,
      "mean_gradient_RMS": 1.660654392737213e+19,
      "mean_inactive_or_saturated_fraction": 0.5269368489583334
    },
    {
      "condition": "ReLU large",
      "depth": 12,
      "mean_activation_SD": 31513345654.030163,
      "mean_gradient_RMS": 1.186872424886611e+19,
      "mean_inactive_or_saturated_fraction": 0.4729817708333333
    },
    {
      "condition": "ReLU tiny",
      "depth": 1,
      "mean_activation_SD": 0.003231341499605437,
      "mean_gradient_RMS": 6.1900777427817964e-58,
      "mean_inactive_or_saturated_fraction": 0.4965006510416667
    },
    {
      "condition": "ReLU tiny",
      "depth": 2,
      "mean_activation_SD": 1.2567964763484174e-05,
      "mean_gradient_RMS": 1.282030077497115e-57,
      "mean_inactive_or_saturated_fraction": 0.513427734375
    },
    {
      "condition": "ReLU tiny",
      "depth": 3,
      "mean_activation_SD": 4.846683995190389e-08,
      "mean_gradient_RMS": 1.7657327457034373e-57,
      "mean_inactive_or_saturated_fraction": 0.4544270833333333
    },
    {
      "condition": "ReLU tiny",
      "depth": 4,
      "mean_activation_SD": 1.9633709758128232e-10,
      "mean_gradient_RMS": 1.7125556846843115e-57,
      "mean_inactive_or_saturated_fraction": 0.4733072916666667
    },
    {
      "condition": "ReLU tiny",
      "depth": 5,
      "mean_activation_SD": 7.079831052875029e-13,
      "mean_gradient_RMS": 2.2029462170714956e-57,
      "mean_inactive_or_saturated_fraction": 0.584716796875
    },
    {
      "condition": "ReLU tiny",
      "depth": 6,
      "mean_activation_SD": 2.4657276828189234e-15,
      "mean_gradient_RMS": 2.4886145906517945e-57,
      "mean_inactive_or_saturated_fraction": 0.493896484375
    },
    {
      "condition": "ReLU tiny",
      "depth": 7,
      "mean_activation_SD": 9.478674575025986e-18,
      "mean_gradient_RMS": 2.4531903331010429e-57,
      "mean_inactive_or_saturated_fraction": 0.489013671875
    },
    {
      "condition": "ReLU tiny",
      "depth": 8,
      "mean_activation_SD": 3.8971539709012617e-20,
      "mean_gradient_RMS": 2.4518759381078388e-57,
      "mean_inactive_or_saturated_fraction": 0.474853515625
    },
    {
      "condition": "ReLU tiny",
      "depth": 9,
      "mean_activation_SD": 1.4078370101290633e-22,
      "mean_gradient_RMS": 2.0970483428194815e-57,
      "mean_inactive_or_saturated_fraction": 0.566162109375
    },
    {
      "condition": "ReLU tiny",
      "depth": 10,
      "mean_activation_SD": 6.526804110098783e-25,
      "mean_gradient_RMS": 1.83251633325978e-57,
      "mean_inactive_or_saturated_fraction": 0.4676106770833333
    },
    {
      "condition": "ReLU tiny",
      "depth": 11,
      "mean_activation_SD": 2.1632227520213194e-27,
      "mean_gradient_RMS": 1.9796543034758735e-57,
      "mean_inactive_or_saturated_fraction": 0.5269368489583334
    },
    {
      "condition": "ReLU tiny",
      "depth": 12,
      "mean_activation_SD": 7.693687903815966e-30,
      "mean_gradient_RMS": 1.4148621855814596e-57,
      "mean_inactive_or_saturated_fraction": 0.4729817708333333
    },
    {
      "condition": "Sigmoid large",
      "depth": 1,
      "mean_activation_SD": 0.46187108955171013,
      "mean_gradient_RMS": 0.000368467915482448,
      "mean_inactive_or_saturated_fraction": 0.6673177083333334
    },
    {
      "condition": "Sigmoid large",
      "depth": 2,
      "mean_activation_SD": 0.44432650908247023,
      "mean_gradient_RMS": 0.00032634532886653575,
      "mean_inactive_or_saturated_fraction": 0.5376790364583334
    },
    {
      "condition": "Sigmoid large",
      "depth": 3,
      "mean_activation_SD": 0.4333740989130998,
      "mean_gradient_RMS": 0.000340508340731244,
      "mean_inactive_or_saturated_fraction": 0.48583984375
    },
    {
      "condition": "Sigmoid large",
      "depth": 4,
      "mean_activation_SD": 0.44446140781840554,
      "mean_gradient_RMS": 0.0003679150350592079,
      "mean_inactive_or_saturated_fraction": 0.5557454427083334
    },
    {
      "condition": "Sigmoid large",
      "depth": 5,
      "mean_activation_SD": 0.43156170763960405,
      "mean_gradient_RMS": 0.0006278996827665051,
      "mean_inactive_or_saturated_fraction": 0.5485026041666666
    },
    {
      "condition": "Sigmoid large",
      "depth": 6,
      "mean_activation_SD": 0.4310566106954791,
      "mean_gradient_RMS": 0.0005232196177915943,
      "mean_inactive_or_saturated_fraction": 0.480712890625
    },
    {
      "condition": "Sigmoid large",
      "depth": 7,
      "mean_activation_SD": 0.4383992931038647,
      "mean_gradient_RMS": 0.0006362413199915053,
      "mean_inactive_or_saturated_fraction": 0.5448404947916666
    },
    {
      "condition": "Sigmoid large",
      "depth": 8,
      "mean_activation_SD": 0.4118184408518284,
      "mean_gradient_RMS": 0.0006302086202456203,
      "mean_inactive_or_saturated_fraction": 0.4418131510416667
    },
    {
      "condition": "Sigmoid large",
      "depth": 9,
      "mean_activation_SD": 0.44622710204683963,
      "mean_gradient_RMS": 0.0006924049633980749,
      "mean_inactive_or_saturated_fraction": 0.5528157552083334
    },
    {
      "condition": "Sigmoid large",
      "depth": 10,
      "mean_activation_SD": 0.4400753532902158,
      "mean_gradient_RMS": 0.0009685425207339222,
      "mean_inactive_or_saturated_fraction": 0.5569661458333334
    },
    {
      "condition": "Sigmoid large",
      "depth": 11,
      "mean_activation_SD": 0.4485160705518063,
      "mean_gradient_RMS": 0.0014783262827803671,
      "mean_inactive_or_saturated_fraction": 0.6284993489583334
    },
    {
      "condition": "Sigmoid large",
      "depth": 12,
      "mean_activation_SD": 0.4474428771006364,
      "mean_gradient_RMS": 0.001759951346210386,
      "mean_inactive_or_saturated_fraction": 0.5332845052083334
    },
    {
      "condition": "Tanh Xavier",
      "depth": 1,
      "mean_activation_SD": 0.7491979318670797,
      "mean_gradient_RMS": 0.0034955568379722818,
      "mean_inactive_or_saturated_fraction": 0.10042317708333333
    },
    {
      "condition": "Tanh Xavier",
      "depth": 2,
      "mean_activation_SD": 0.6897146458808207,
      "mean_gradient_RMS": 0.0029747189365108557,
      "mean_inactive_or_saturated_fraction": 0.034016927083333336
    },
    {
      "condition": "Tanh Xavier",
      "depth": 3,
      "mean_activation_SD": 0.6697716643510189,
      "mean_gradient_RMS": 0.0026698612019453254,
      "mean_inactive_or_saturated_fraction": 0.021158854166666668
    },
    {
      "condition": "Tanh Xavier",
      "depth": 4,
      "mean_activation_SD": 0.6630523431683798,
      "mean_gradient_RMS": 0.0024967135600177104,
      "mean_inactive_or_saturated_fraction": 0.020426432291666668
    },
    {
      "condition": "Tanh Xavier",
      "depth": 5,
      "mean_activation_SD": 0.6543579764311395,
      "mean_gradient_RMS": 0.0024919983408744025,
      "mean_inactive_or_saturated_fraction": 0.018391927083333332
    },
    {
      "condition": "Tanh Xavier",
      "depth": 6,
      "mean_activation_SD": 0.6564173767569873,
      "mean_gradient_RMS": 0.002511159372697711,
      "mean_inactive_or_saturated_fraction": 0.018717447916666668
    },
    {
      "condition": "Tanh Xavier",
      "depth": 7,
      "mean_activation_SD": 0.6524976995180062,
      "mean_gradient_RMS": 0.002662342122711501,
      "mean_inactive_or_saturated_fraction": 0.016276041666666668
    },
    {
      "condition": "Tanh Xavier",
      "depth": 8,
      "mean_activation_SD": 0.6539167501618445,
      "mean_gradient_RMS": 0.0029533182879873388,
      "mean_inactive_or_saturated_fraction": 0.015055338541666666
    },
    {
      "condition": "Tanh Xavier",
      "depth": 9,
      "mean_activation_SD": 0.6542677580856017,
      "mean_gradient_RMS": 0.0030476000796684608,
      "mean_inactive_or_saturated_fraction": 0.019124348958333332
    },
    {
      "condition": "Tanh Xavier",
      "depth": 10,
      "mean_activation_SD": 0.6498066288629657,
      "mean_gradient_RMS": 0.003191154532535235,
      "mean_inactive_or_saturated_fraction": 0.009440104166666666
    },
    {
      "condition": "Tanh Xavier",
      "depth": 11,
      "mean_activation_SD": 0.6637512121127132,
      "mean_gradient_RMS": 0.0033389459160137486,
      "mean_inactive_or_saturated_fraction": 0.015380859375
    },
    {
      "condition": "Tanh Xavier",
      "depth": 12,
      "mean_activation_SD": 0.6484520752395845,
      "mean_gradient_RMS": 0.0036508448383993585,
      "mean_inactive_or_saturated_fraction": 0.015380859375
    }
  ],
  "replicates": 3,
  "width": 32
}
```

### code_106

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2206.

```json
{
  "batchnorm_eval_context_difference": 1.6653345369377348e-16,
  "batchnorm_train_context_difference": 1.502284438646759,
  "dropout_train_repeat_difference": 1.7998832817958124,
  "histories": {
    "BN": [
      {
        "development_MSE": 0.4414772558501253,
        "epoch": 1,
        "learning_rate": 0.01,
        "mean_gradient_norm": 2.3082565011634277,
        "train_MSE": 0.6888453410695708
      },
      {
        "development_MSE": 0.39410820705332267,
        "epoch": 2,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.8438029483003053,
        "train_MSE": 0.41790285917567155
      },
      {
        "development_MSE": 0.26781587940845086,
        "epoch": 3,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.5767097335547196,
        "train_MSE": 0.30130694015649856
      },
      {
        "development_MSE": 0.1794958133064934,
        "epoch": 4,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.2705949305589996,
        "train_MSE": 0.22039620850637118
      },
      {
        "development_MSE": 0.1624742314197128,
        "epoch": 5,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.176588858859719,
        "train_MSE": 0.16182009796081406
      },
      {
        "development_MSE": 0.20906808969986407,
        "epoch": 6,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.0485288371034003,
        "train_MSE": 0.14837953000095638
      },
      {
        "development_MSE": 0.19847245130859442,
        "epoch": 7,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8919754650643323,
        "train_MSE": 0.11219464321098525
      },
      {
        "development_MSE": 0.1350102110248415,
        "epoch": 8,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.2350642167458161,
        "train_MSE": 0.15058050302511486
      },
      {
        "development_MSE": 0.15212190400249556,
        "epoch": 9,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.02433949215692,
        "train_MSE": 0.12175863686855108
      },
      {
        "development_MSE": 0.1514981536966282,
        "epoch": 10,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9528641368360008,
        "train_MSE": 0.11998104456248608
      },
      {
        "development_MSE": 0.17091676974806658,
        "epoch": 11,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.1852003457325326,
        "train_MSE": 0.13431370377181304
      },
      {
        "development_MSE": 0.15017473478904186,
        "epoch": 12,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8464763954210026,
        "train_MSE": 0.09139263149783816
      },
      {
        "development_MSE": 0.16703314396302701,
        "epoch": 13,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.0018218693207563,
        "train_MSE": 0.10466622418661592
      },
      {
        "development_MSE": 0.1910584402938264,
        "epoch": 14,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.216922118403307,
        "train_MSE": 0.13494966615577672
      },
      {
        "development_MSE": 0.18713150855584965,
        "epoch": 15,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.917700800299538,
        "train_MSE": 0.09345617526470561
      },
      {
        "development_MSE": 0.16690213223764114,
        "epoch": 16,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8974247577949589,
        "train_MSE": 0.09723916298406265
      },
      {
        "development_MSE": 0.16996274637547365,
        "epoch": 17,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.057963922706028,
        "train_MSE": 0.1170341357421631
      },
      {
        "development_MSE": 0.15472094465249975,
        "epoch": 18,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8472409478482871,
        "train_MSE": 0.0911056539470364
      },
      {
        "development_MSE": 0.13641653415588992,
        "epoch": 19,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.2611356433231566,
        "train_MSE": 0.1162529389310032
      },
      {
        "development_MSE": 0.18101823719922733,
        "epoch": 20,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.200206396327613,
        "train_MSE": 0.1315186019381475
      },
      {
        "development_MSE": 0.18167004830688183,
        "epoch": 21,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.920594016175346,
        "train_MSE": 0.07544032699652314
      },
      {
        "development_MSE": 0.15907451306456283,
        "epoch": 22,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8728351039370179,
        "train_MSE": 0.06953856514756918
      },
      {
        "development_MSE": 0.18909421921532726,
        "epoch": 23,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8783202223380634,
        "train_MSE": 0.08326198355684779
      }
    ],
    "Base": [
      {
        "development_MSE": 0.3801445111330918,
        "epoch": 1,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9611883626312556,
        "train_MSE": 0.7718081204120791
      },
      {
        "development_MSE": 0.3220231319966782,
        "epoch": 2,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7872706051406727,
        "train_MSE": 0.541331728560784
      },
      {
        "development_MSE": 0.2910257459904322,
        "epoch": 3,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9731480493241699,
        "train_MSE": 0.45127096271797434
      },
      {
        "development_MSE": 0.30643396376961274,
        "epoch": 4,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7062496362221955,
        "train_MSE": 0.34838481517124115
      },
      {
        "development_MSE": 0.19923168170784944,
        "epoch": 5,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.6591025583864344,
        "train_MSE": 0.27347325238035125
      },
      {
        "development_MSE": 0.1831980094359375,
        "epoch": 6,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5730068872452753,
        "train_MSE": 0.19186714597511842
      },
      {
        "development_MSE": 0.1512467466149312,
        "epoch": 7,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5807984703602368,
        "train_MSE": 0.146185645615621
      },
      {
        "development_MSE": 0.12973193814681977,
        "epoch": 8,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.47034867495166166,
        "train_MSE": 0.11391611820422604
      },
      {
        "development_MSE": 0.12213551119765254,
        "epoch": 9,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.45958803293768463,
        "train_MSE": 0.1006388546527967
      },
      {
        "development_MSE": 0.12382638965648977,
        "epoch": 10,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5543331923001199,
        "train_MSE": 0.09162886594194604
      },
      {
        "development_MSE": 0.12711937108467078,
        "epoch": 11,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5001359911372881,
        "train_MSE": 0.08233128199978944
      },
      {
        "development_MSE": 0.12542701120225425,
        "epoch": 12,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.460310434090971,
        "train_MSE": 0.07116003317022306
      },
      {
        "development_MSE": 0.131992391353636,
        "epoch": 13,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.3681509857515055,
        "train_MSE": 0.0599730933831459
      },
      {
        "development_MSE": 0.13008877174405203,
        "epoch": 14,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.36879279928342584,
        "train_MSE": 0.05570147465275512
      },
      {
        "development_MSE": 0.1350819933461165,
        "epoch": 15,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.46753987515405376,
        "train_MSE": 0.05139502838940452
      },
      {
        "development_MSE": 0.15509959106224575,
        "epoch": 16,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4378279713208268,
        "train_MSE": 0.04814107573998646
      },
      {
        "development_MSE": 0.14068145231233944,
        "epoch": 17,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.41481734231827794,
        "train_MSE": 0.04639919067119715
      },
      {
        "development_MSE": 0.13752203162920096,
        "epoch": 18,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.340506769357983,
        "train_MSE": 0.040433535817706805
      },
      {
        "development_MSE": 0.13884210090817056,
        "epoch": 19,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.31203884941050647,
        "train_MSE": 0.03525752825757571
      },
      {
        "development_MSE": 0.15576440946068387,
        "epoch": 20,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.3240820666593613,
        "train_MSE": 0.03251799258777024
      },
      {
        "development_MSE": 0.1516649712587413,
        "epoch": 21,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.40072786141366495,
        "train_MSE": 0.03247151929732453
      },
      {
        "development_MSE": 0.1547203236802917,
        "epoch": 22,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.3630384492544918,
        "train_MSE": 0.029510091319136178
      },
      {
        "development_MSE": 0.14950441719862068,
        "epoch": 23,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.32988673532033586,
        "train_MSE": 0.02822043367896447
      },
      {
        "development_MSE": 0.15310014899627594,
        "epoch": 24,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.3053265554580267,
        "train_MSE": 0.02390854742078528
      }
    ],
    "Cosine": [
      {
        "development_MSE": 0.3801445111330918,
        "epoch": 1,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9611883626312556,
        "train_MSE": 0.7718081204120791
      },
      {
        "development_MSE": 0.32201596018018663,
        "epoch": 2,
        "learning_rate": 0.009998286624877785,
        "mean_gradient_norm": 0.7872579897354276,
        "train_MSE": 0.5413342565078413
      },
      {
        "development_MSE": 0.29101797395958184,
        "epoch": 3,
        "learning_rate": 0.009993147673772868,
        "mean_gradient_norm": 0.9729589091474607,
        "train_MSE": 0.45127024236436597
      },
      {
        "development_MSE": 0.30643020435888146,
        "epoch": 4,
        "learning_rate": 0.00998458666866564,
        "mean_gradient_norm": 0.7060526794984137,
        "train_MSE": 0.3484241853898575
      },
      {
        "development_MSE": 0.19928978362095387,
        "epoch": 5,
        "learning_rate": 0.009972609476841365,
        "mean_gradient_norm": 0.6586193184931733,
        "train_MSE": 0.2735931801298105
      },
      {
        "development_MSE": 0.18321268117591866,
        "epoch": 6,
        "learning_rate": 0.009957224306869052,
        "mean_gradient_norm": 0.5722563203745605,
        "train_MSE": 0.1921108772100106
      },
      {
        "development_MSE": 0.15148044700480426,
        "epoch": 7,
        "learning_rate": 0.009938441702975689,
        "mean_gradient_norm": 0.5785220278112387,
        "train_MSE": 0.14631507101822502
      },
      {
        "development_MSE": 0.13032425863354924,
        "epoch": 8,
        "learning_rate": 0.009916274537819774,
        "mean_gradient_norm": 0.4698272236270474,
        "train_MSE": 0.11404777263955933
      },
      {
        "development_MSE": 0.12228799081942285,
        "epoch": 9,
        "learning_rate": 0.009890738003669028,
        "mean_gradient_norm": 0.45671815445740416,
        "train_MSE": 0.10069149084692251
      },
      {
        "development_MSE": 0.12383234129822147,
        "epoch": 10,
        "learning_rate": 0.009861849601988382,
        "mean_gradient_norm": 0.5556179630249991,
        "train_MSE": 0.0918329672461236
      },
      {
        "development_MSE": 0.12692484536982918,
        "epoch": 11,
        "learning_rate": 0.00982962913144534,
        "mean_gradient_norm": 0.4941246098617573,
        "train_MSE": 0.08210659685983826
      },
      {
        "development_MSE": 0.12595330362675827,
        "epoch": 12,
        "learning_rate": 0.009794098674340964,
        "mean_gradient_norm": 0.4458922177433417,
        "train_MSE": 0.07062835456939272
      },
      {
        "development_MSE": 0.1322506998688297,
        "epoch": 13,
        "learning_rate": 0.009755282581475767,
        "mean_gradient_norm": 0.3590981139809069,
        "train_MSE": 0.05990581444180401
      },
      {
        "development_MSE": 0.1302239658018,
        "epoch": 14,
        "learning_rate": 0.009713207455460893,
        "mean_gradient_norm": 0.3736244071067447,
        "train_MSE": 0.05612854623912807
      },
      {
        "development_MSE": 0.1326968965816998,
        "epoch": 15,
        "learning_rate": 0.009667902132486009,
        "mean_gradient_norm": 0.4721349200041789,
        "train_MSE": 0.0516250832347022
      },
      {
        "development_MSE": 0.1506277010448457,
        "epoch": 16,
        "learning_rate": 0.009619397662556435,
        "mean_gradient_norm": 0.4182519167838283,
        "train_MSE": 0.04732666676797001
      },
      {
        "development_MSE": 0.13864019715873643,
        "epoch": 17,
        "learning_rate": 0.009567727288213005,
        "mean_gradient_norm": 0.39730210229040547,
        "train_MSE": 0.04600645159919418
      },
      {
        "development_MSE": 0.13574562538720475,
        "epoch": 18,
        "learning_rate": 0.009512926421749305,
        "mean_gradient_norm": 0.32744166430107585,
        "train_MSE": 0.040319626397194844
      },
      {
        "development_MSE": 0.1363054729129352,
        "epoch": 19,
        "learning_rate": 0.009455032620941842,
        "mean_gradient_norm": 0.31645678234709124,
        "train_MSE": 0.03581007587917897
      },
      {
        "development_MSE": 0.14998582973494143,
        "epoch": 20,
        "learning_rate": 0.00939408556330983,
        "mean_gradient_norm": 0.3231491602341637,
        "train_MSE": 0.03302692821710296
      },
      {
        "development_MSE": 0.1476802499170546,
        "epoch": 21,
        "learning_rate": 0.009330127018922196,
        "mean_gradient_norm": 0.3771922314167632,
        "train_MSE": 0.03156623820528299
      },
      {
        "development_MSE": 0.14778985100885805,
        "epoch": 22,
        "learning_rate": 0.009263200821770463,
        "mean_gradient_norm": 0.3464086546541602,
        "train_MSE": 0.029161218313613475
      },
      {
        "development_MSE": 0.14414243852801978,
        "epoch": 23,
        "learning_rate": 0.009193352839727123,
        "mean_gradient_norm": 0.30302724593041963,
        "train_MSE": 0.02737677849191771
      },
      {
        "development_MSE": 0.14608070946184548,
        "epoch": 24,
        "learning_rate": 0.00912063094311008,
        "mean_gradient_norm": 0.28962914567930753,
        "train_MSE": 0.02358054776321088
      }
    ],
    "LN": [
      {
        "development_MSE": 0.3335377874951823,
        "epoch": 1,
        "learning_rate": 0.01,
        "mean_gradient_norm": 2.8557623340952714,
        "train_MSE": 0.7877978238701746
      },
      {
        "development_MSE": 0.28412561191635166,
        "epoch": 2,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.6248104657130298,
        "train_MSE": 0.478268211181299
      },
      {
        "development_MSE": 0.2846621910070728,
        "epoch": 3,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.58976890517038,
        "train_MSE": 0.39266301346697263
      },
      {
        "development_MSE": 0.24293128346018872,
        "epoch": 4,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.2898352023431296,
        "train_MSE": 0.3103546075028215
      },
      {
        "development_MSE": 0.18159354587884657,
        "epoch": 5,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.1339457253814798,
        "train_MSE": 0.22802405306479234
      },
      {
        "development_MSE": 0.2020161906778315,
        "epoch": 6,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8197806265311375,
        "train_MSE": 0.16627358654279675
      },
      {
        "development_MSE": 0.17729168391772054,
        "epoch": 7,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.0783050375661352,
        "train_MSE": 0.15153253823124002
      },
      {
        "development_MSE": 0.16169865227849745,
        "epoch": 8,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7507130104543737,
        "train_MSE": 0.11538889620890709
      },
      {
        "development_MSE": 0.16944403994386786,
        "epoch": 9,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5980222672690528,
        "train_MSE": 0.09624395232217016
      },
      {
        "development_MSE": 0.16554035432088804,
        "epoch": 10,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.6707506017789987,
        "train_MSE": 0.08196476812163388
      },
      {
        "development_MSE": 0.1568775177019922,
        "epoch": 11,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8993341417857135,
        "train_MSE": 0.07823642067121984
      },
      {
        "development_MSE": 0.16286434240862735,
        "epoch": 12,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7185814249720729,
        "train_MSE": 0.06186296516407972
      },
      {
        "development_MSE": 0.17830908059614387,
        "epoch": 13,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8324928030083014,
        "train_MSE": 0.058644155802455356
      },
      {
        "development_MSE": 0.17425520487326013,
        "epoch": 14,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7278815360786893,
        "train_MSE": 0.04880176098405089
      },
      {
        "development_MSE": 0.1641813928169889,
        "epoch": 15,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.0469112291055975,
        "train_MSE": 0.0529502930033931
      },
      {
        "development_MSE": 0.1645141007570239,
        "epoch": 16,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7949645543750101,
        "train_MSE": 0.04311956353707392
      },
      {
        "development_MSE": 0.20186672765343106,
        "epoch": 17,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.898276021394315,
        "train_MSE": 0.03978286841095593
      },
      {
        "development_MSE": 0.17844197380702442,
        "epoch": 18,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.6691001536788063,
        "train_MSE": 0.03521067418808026
      },
      {
        "development_MSE": 0.1776928890293355,
        "epoch": 19,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.6043053142815582,
        "train_MSE": 0.026933954961796874
      },
      {
        "development_MSE": 0.16487536731052746,
        "epoch": 20,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.3638030080969071,
        "train_MSE": 0.019851420367253944
      },
      {
        "development_MSE": 0.16861443625473455,
        "epoch": 21,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4707955017541385,
        "train_MSE": 0.020591248306343003
      },
      {
        "development_MSE": 0.1904276014536387,
        "epoch": 22,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.44710646789991787,
        "train_MSE": 0.020323788360241655
      },
      {
        "development_MSE": 0.15950790627945594,
        "epoch": 23,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5355202549877113,
        "train_MSE": 0.018769275690930173
      },
      {
        "development_MSE": 0.15797418557887954,
        "epoch": 24,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.43938163685021964,
        "train_MSE": 0.0147538895397864
      },
      {
        "development_MSE": 0.15434627806902035,
        "epoch": 25,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.39199896842835197,
        "train_MSE": 0.01331981783012943
      },
      {
        "development_MSE": 0.1621732666133857,
        "epoch": 26,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4604617221561773,
        "train_MSE": 0.013209623987119787
      },
      {
        "development_MSE": 0.16037540220762092,
        "epoch": 27,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.3842040654158314,
        "train_MSE": 0.012771484076457992
      },
      {
        "development_MSE": 0.17630870800561924,
        "epoch": 28,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.37195908556132146,
        "train_MSE": 0.009991222095355442
      },
      {
        "development_MSE": 0.1773499361932817,
        "epoch": 29,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5211317327310913,
        "train_MSE": 0.012675681889837753
      },
      {
        "development_MSE": 0.1847776263430489,
        "epoch": 30,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4978390178989331,
        "train_MSE": 0.011977062671280425
      },
      {
        "development_MSE": 0.16762348829123327,
        "epoch": 31,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4931088037902443,
        "train_MSE": 0.013324052132760755
      },
      {
        "development_MSE": 0.1770481345496155,
        "epoch": 32,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5054745898001411,
        "train_MSE": 0.013163461781247826
      },
      {
        "development_MSE": 0.1845117466660819,
        "epoch": 33,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5060448569656079,
        "train_MSE": 0.012913799042166253
      },
      {
        "development_MSE": 0.19010442523636456,
        "epoch": 34,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4550896966929168,
        "train_MSE": 0.012634358327202437
      },
      {
        "development_MSE": 0.18432069522837896,
        "epoch": 35,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.46692960848530524,
        "train_MSE": 0.014032811111479792
      },
      {
        "development_MSE": 0.16477180860209384,
        "epoch": 36,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.420432439244963,
        "train_MSE": 0.014238795735523245
      },
      {
        "development_MSE": 0.19464405658345507,
        "epoch": 37,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.43564300614562784,
        "train_MSE": 0.012248257091430561
      },
      {
        "development_MSE": 0.15007719116450327,
        "epoch": 38,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.3244841091459045,
        "train_MSE": 0.007409032734878325
      },
      {
        "development_MSE": 0.1831347761104421,
        "epoch": 39,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.48073542840376177,
        "train_MSE": 0.009301564785636084
      },
      {
        "development_MSE": 0.17130196977563728,
        "epoch": 40,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.42806155876149293,
        "train_MSE": 0.009303535523928671
      },
      {
        "development_MSE": 0.1686617082862717,
        "epoch": 41,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4471086309257508,
        "train_MSE": 0.011343974572950548
      },
      {
        "development_MSE": 0.1734208778784926,
        "epoch": 42,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5235199784710628,
        "train_MSE": 0.014024223444501402
      },
      {
        "development_MSE": 0.1992922107450264,
        "epoch": 43,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4133655464886739,
        "train_MSE": 0.010828097203972995
      },
      {
        "development_MSE": 0.1674495187794986,
        "epoch": 44,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.45720788590498734,
        "train_MSE": 0.011700826510262642
      },
      {
        "development_MSE": 0.17316637080283703,
        "epoch": 45,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4260944746905995,
        "train_MSE": 0.01074427981823439
      },
      {
        "development_MSE": 0.17878587797859535,
        "epoch": 46,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.451410021253805,
        "train_MSE": 0.009217016271814283
      },
      {
        "development_MSE": 0.17287917266512692,
        "epoch": 47,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.33954844663723077,
        "train_MSE": 0.0093901416125944
      },
      {
        "development_MSE": 0.1691530903956821,
        "epoch": 48,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.468606731929178,
        "train_MSE": 0.008971145266214087
      },
      {
        "development_MSE": 0.18079789876759073,
        "epoch": 49,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.5024982783159025,
        "train_MSE": 0.01068187360978447
      },
      {
        "development_MSE": 0.17117397463132666,
        "epoch": 50,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.4835038310443523,
        "train_MSE": 0.013856431171526637
      },
      {
        "development_MSE": 0.1813040893013666,
        "epoch": 51,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.3415299828230265,
        "train_MSE": 0.008231061233146477
      },
      {
        "development_MSE": 0.17531980999681357,
        "epoch": 52,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.35010449998398313,
        "train_MSE": 0.009015089085325261
      },
      {
        "development_MSE": 0.18280196641738572,
        "epoch": 53,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.3370144974464279,
        "train_MSE": 0.009588998684813218
      }
    ],
    "LN+drop": [
      {
        "development_MSE": 0.32762807222251744,
        "epoch": 1,
        "learning_rate": 0.01,
        "mean_gradient_norm": 3.2605095983908434,
        "train_MSE": 0.8950350983589511
      },
      {
        "development_MSE": 0.30544749213377437,
        "epoch": 2,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.772959664353131,
        "train_MSE": 0.552772511567674
      },
      {
        "development_MSE": 0.30430563642743835,
        "epoch": 3,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.6156714594984587,
        "train_MSE": 0.4769364106881672
      },
      {
        "development_MSE": 0.3047089150252631,
        "epoch": 4,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.1907197879644515,
        "train_MSE": 0.43077255655801167
      },
      {
        "development_MSE": 0.2229978170127759,
        "epoch": 5,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.2638491488369639,
        "train_MSE": 0.43519890543045187
      },
      {
        "development_MSE": 0.20315046914494966,
        "epoch": 6,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.2406528102769137,
        "train_MSE": 0.3467079481449547
      },
      {
        "development_MSE": 0.2119471288464713,
        "epoch": 7,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.0684202110338752,
        "train_MSE": 0.32356327323913897
      },
      {
        "development_MSE": 0.20290726716751117,
        "epoch": 8,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.1346633300811684,
        "train_MSE": 0.29544129892269333
      },
      {
        "development_MSE": 0.19491732012854746,
        "epoch": 9,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9988866700322395,
        "train_MSE": 0.31055129363502204
      },
      {
        "development_MSE": 0.19235695491809257,
        "epoch": 10,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.944709119435133,
        "train_MSE": 0.2812752045466339
      },
      {
        "development_MSE": 0.17472808581069343,
        "epoch": 11,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.0210333786735404,
        "train_MSE": 0.23390768441420307
      },
      {
        "development_MSE": 0.15456256960600506,
        "epoch": 12,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9620733444796955,
        "train_MSE": 0.21864169805588007
      },
      {
        "development_MSE": 0.14414581186409836,
        "epoch": 13,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9492172885849451,
        "train_MSE": 0.23002486486782456
      },
      {
        "development_MSE": 0.13300221885074476,
        "epoch": 14,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.0521689354715724,
        "train_MSE": 0.23348383055376098
      },
      {
        "development_MSE": 0.1685886155105874,
        "epoch": 15,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9943940866348667,
        "train_MSE": 0.2336701620851304
      },
      {
        "development_MSE": 0.16572264774174972,
        "epoch": 16,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9313500330448438,
        "train_MSE": 0.22586851122307702
      },
      {
        "development_MSE": 0.16101445574413098,
        "epoch": 17,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9446975034143997,
        "train_MSE": 0.23822597179500374
      },
      {
        "development_MSE": 0.17370186982981006,
        "epoch": 18,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9572057420828332,
        "train_MSE": 0.20040421987845355
      },
      {
        "development_MSE": 0.18070731364629283,
        "epoch": 19,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9153223828932155,
        "train_MSE": 0.24659210962420083
      },
      {
        "development_MSE": 0.1643163843479324,
        "epoch": 20,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8499543705163749,
        "train_MSE": 0.20181155379676766
      },
      {
        "development_MSE": 0.16260696172100111,
        "epoch": 21,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8640697005408845,
        "train_MSE": 0.20325516442786898
      },
      {
        "development_MSE": 0.1534913350365178,
        "epoch": 22,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7302489108242375,
        "train_MSE": 0.20889168442764686
      },
      {
        "development_MSE": 0.1502944210396698,
        "epoch": 23,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.0855306704085255,
        "train_MSE": 0.20577924528609012
      },
      {
        "development_MSE": 0.137294923993448,
        "epoch": 24,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8452519974749843,
        "train_MSE": 0.19307496645019706
      },
      {
        "development_MSE": 0.1269936600148886,
        "epoch": 25,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8200355837244926,
        "train_MSE": 0.21150141863454083
      },
      {
        "development_MSE": 0.13285889797626327,
        "epoch": 26,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.0181085696310703,
        "train_MSE": 0.20982822453843353
      },
      {
        "development_MSE": 0.14126363553529192,
        "epoch": 27,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.887627348053203,
        "train_MSE": 0.21261146461758904
      },
      {
        "development_MSE": 0.14587236214886862,
        "epoch": 28,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.791577944150526,
        "train_MSE": 0.20071837391304823
      },
      {
        "development_MSE": 0.14691770238930252,
        "epoch": 29,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7500463381168005,
        "train_MSE": 0.16795694366669392
      },
      {
        "development_MSE": 0.13789340401343225,
        "epoch": 30,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8746367377748744,
        "train_MSE": 0.18904315129794877
      },
      {
        "development_MSE": 0.1597861435606338,
        "epoch": 31,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8565497217153704,
        "train_MSE": 0.1869851330815754
      },
      {
        "development_MSE": 0.15515630651104834,
        "epoch": 32,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8440799333485165,
        "train_MSE": 0.17291729977565787
      },
      {
        "development_MSE": 0.15531110867076486,
        "epoch": 33,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.6971640265046722,
        "train_MSE": 0.15741826232033596
      },
      {
        "development_MSE": 0.14737192638566765,
        "epoch": 34,
        "learning_rate": 0.01,
        "mean_gradient_norm": 1.015305665913637,
        "train_MSE": 0.19990732288151447
      },
      {
        "development_MSE": 0.17315420459597186,
        "epoch": 35,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8448106706975297,
        "train_MSE": 0.17968908307350154
      },
      {
        "development_MSE": 0.20562917089659222,
        "epoch": 36,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7595358647146613,
        "train_MSE": 0.1587655947880571
      },
      {
        "development_MSE": 0.2133267967039055,
        "epoch": 37,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.7077988121629044,
        "train_MSE": 0.14990034666895877
      },
      {
        "development_MSE": 0.17680190465682033,
        "epoch": 38,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.8176490304452044,
        "train_MSE": 0.15150212709853506
      },
      {
        "development_MSE": 0.1656078484615403,
        "epoch": 39,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9170605155553483,
        "train_MSE": 0.1939937234692174
      },
      {
        "development_MSE": 0.14824100554837086,
        "epoch": 40,
        "learning_rate": 0.01,
        "mean_gradient_norm": 0.9748350212435982,
        "train_MSE": 0.17033282611314618
      }
    ],
    "SGD": [
      {
        "development_MSE": 0.45661231855345763,
        "epoch": 1,
        "learning_rate": 0.05,
        "mean_gradient_norm": 1.1129415091453618,
        "train_MSE": 0.8290447468515807
      },
      {
        "development_MSE": 0.35244380404825004,
        "epoch": 2,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.7875415396853679,
        "train_MSE": 0.6487512951285377
      },
      {
        "development_MSE": 0.3445138199228982,
        "epoch": 3,
        "learning_rate": 0.05,
        "mean_gradient_norm": 1.286455697351373,
        "train_MSE": 0.566908835439626
      },
      {
        "development_MSE": 0.3074192841958452,
        "epoch": 4,
        "learning_rate": 0.05,
        "mean_gradient_norm": 1.0440078206965266,
        "train_MSE": 0.46669292524281597
      },
      {
        "development_MSE": 0.3277964861128048,
        "epoch": 5,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.9935709699499133,
        "train_MSE": 0.35847012074154133
      },
      {
        "development_MSE": 0.2461141754148882,
        "epoch": 6,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.9219120645584359,
        "train_MSE": 0.26798160458519826
      },
      {
        "development_MSE": 0.24129252767064052,
        "epoch": 7,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.840030603295364,
        "train_MSE": 0.19126441841092176
      },
      {
        "development_MSE": 0.17000959537146113,
        "epoch": 8,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.8661773584922609,
        "train_MSE": 0.14945536092907577
      },
      {
        "development_MSE": 0.15741852540101325,
        "epoch": 9,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.7680599089829142,
        "train_MSE": 0.12525881875365805
      },
      {
        "development_MSE": 0.14723004661219233,
        "epoch": 10,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.5925446420835828,
        "train_MSE": 0.10700370986339199
      },
      {
        "development_MSE": 0.13930701197738593,
        "epoch": 11,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.44568198985678853,
        "train_MSE": 0.08193193989061226
      },
      {
        "development_MSE": 0.13074136414118004,
        "epoch": 12,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.44081408442115183,
        "train_MSE": 0.07943662039600145
      },
      {
        "development_MSE": 0.1354015494891445,
        "epoch": 13,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.44866148193776034,
        "train_MSE": 0.07321443676949325
      },
      {
        "development_MSE": 0.1330948962331528,
        "epoch": 14,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.4694942840796483,
        "train_MSE": 0.06896410499161575
      },
      {
        "development_MSE": 0.13066080719629372,
        "epoch": 15,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.48724808905141676,
        "train_MSE": 0.06494214008937277
      },
      {
        "development_MSE": 0.13921952465676543,
        "epoch": 16,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.39302887699012573,
        "train_MSE": 0.060645605878596874
      },
      {
        "development_MSE": 0.12032538937838963,
        "epoch": 17,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.37852531840017073,
        "train_MSE": 0.05534277583873956
      },
      {
        "development_MSE": 0.1387366913461174,
        "epoch": 18,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.3754934508443675,
        "train_MSE": 0.05468897310627061
      },
      {
        "development_MSE": 0.1235313800249166,
        "epoch": 19,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.40939601504770357,
        "train_MSE": 0.052770004438015085
      },
      {
        "development_MSE": 0.130308904614084,
        "epoch": 20,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.4581910775358846,
        "train_MSE": 0.05327546443027039
      },
      {
        "development_MSE": 0.134197414940451,
        "epoch": 21,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.433334206987858,
        "train_MSE": 0.05006242542744812
      },
      {
        "development_MSE": 0.13292052144901265,
        "epoch": 22,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.45127735802441654,
        "train_MSE": 0.0495886659961435
      },
      {
        "development_MSE": 0.12163589832740246,
        "epoch": 23,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.3774776151461538,
        "train_MSE": 0.04564374001137519
      },
      {
        "development_MSE": 0.1250772945549338,
        "epoch": 24,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.37419996909822784,
        "train_MSE": 0.040884047554580825
      },
      {
        "development_MSE": 0.1379642828900973,
        "epoch": 25,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.4065901367983238,
        "train_MSE": 0.04361911355073525
      },
      {
        "development_MSE": 0.12682758943435107,
        "epoch": 26,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.49911003496591233,
        "train_MSE": 0.046131858592282166
      },
      {
        "development_MSE": 0.12797052304500928,
        "epoch": 27,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.4714839490321105,
        "train_MSE": 0.04551758773048844
      },
      {
        "development_MSE": 0.12064639922670127,
        "epoch": 28,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.48327713457957544,
        "train_MSE": 0.04207300554328714
      },
      {
        "development_MSE": 0.13769578937564192,
        "epoch": 29,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.4724464793247843,
        "train_MSE": 0.03824109941124431
      },
      {
        "development_MSE": 0.1583334484962688,
        "epoch": 30,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.4917880881308813,
        "train_MSE": 0.041456620607526105
      },
      {
        "development_MSE": 0.127333249764038,
        "epoch": 31,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.659804283873015,
        "train_MSE": 0.05198528981766245
      },
      {
        "development_MSE": 0.12668049172640464,
        "epoch": 32,
        "learning_rate": 0.05,
        "mean_gradient_norm": 0.43619149969277676,
        "train_MSE": 0.04024531547434362
      }
    ]
  },
  "layernorm_eval_context_difference": 0.0,
  "recipes": [
    {
      "best_development_MSE": 0.12213551119765254,
      "best_epoch": 9,
      "epochs_run": 24,
      "final_MSE": 0.1879392190760363,
      "recipe": "Base"
    },
    {
      "best_development_MSE": 0.15007719116450327,
      "best_epoch": 38,
      "epochs_run": 53,
      "final_MSE": 0.2027289709266696,
      "recipe": "LN"
    },
    {
      "best_development_MSE": 0.1350102110248415,
      "best_epoch": 8,
      "epochs_run": 23,
      "final_MSE": 0.2042702680463325,
      "recipe": "BN"
    },
    {
      "best_development_MSE": 0.1269936600148886,
      "best_epoch": 25,
      "epochs_run": 40,
      "final_MSE": 0.19332299270833722,
      "recipe": "LN+drop"
    },
    {
      "best_development_MSE": 0.12032538937838963,
      "best_epoch": 17,
      "epochs_run": 32,
      "final_MSE": 0.15745246605532137,
      "recipe": "SGD"
    },
    {
      "best_development_MSE": 0.12228799081942285,
      "best_epoch": 9,
      "epochs_run": 24,
      "final_MSE": 0.18760398875834242,
      "recipe": "Cosine"
    }
  ],
  "split_buildings": [
    24,
    8,
    8
  ],
  "unstable_history": [
    {
      "development_MSE": 0.6784470222608918,
      "gradient_norm": 1.1145303585901019,
      "train_MSE": 0.866326463290713,
      "update": 0
    },
    {
      "development_MSE": 17996.939397545728,
      "gradient_norm": 10862.425963198406,
      "train_MSE": 16163.300603953297,
      "update": 1
    },
    {
      "development_MSE": 1369989169627.212,
      "gradient_norm": 498698021574.1536,
      "train_MSE": 1178905809530.587,
      "update": 2
    }
  ],
  "unstable_stop": "loss exceeds declared 1e8 health limit"
}
```

### code_107

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2207.

```json
{
  "checkpoint_next_step_exact": true,
  "data_loader_mismatch_caught": true,
  "gradient_norm_after_clip": 0.9999999999993617,
  "gradient_norm_before_clip": 1566941.2720391648,
  "masked_padding_probability_max_difference": 0.0,
  "microbatch_gradient_max_error": 1.1102230246251565e-16,
  "padding_metrics": [
    {
      "development_accuracy": 1.0,
      "feature": "Unmasked",
      "final_Brier": 0.9918346444556835,
      "final_accuracy": 0.0,
      "train_accuracy": 1.0
    },
    {
      "development_accuracy": 0.95,
      "feature": "Masked",
      "final_Brier": 0.09316936116731546,
      "final_accuracy": 0.885,
      "train_accuracy": 0.815
    }
  ],
  "precision_sums": {
    "torch.float32": 0.0,
    "torch.float64": 1.0
  },
  "resource_batch_shapes": [
    [
      8,
      128,
      16
    ],
    [
      32,
      128,
      16
    ],
    [
      128,
      128,
      16
    ]
  ],
  "resource_input_tensor_bytes": [
    65536,
    262144,
    1048576
  ],
  "tiny_set_accuracy": 1.0,
  "tiny_set_final_loss": 1.4178126420924895e-05
}
```


## Original CPU resource observations

These nine actual fresh-process observations belong to the code_107 kernel. Timings and OS process high-water RSS vary across runs and are kept outside deterministic RESULT assertions. The vector figure replays these original observations.

```json
[
  {
    "baseline_RSS_bytes": 213778432,
    "batch": 8,
    "dtype": "float32",
    "peak_RSS_bytes": 316981248,
    "platform": "Darwin",
    "replicate": 0,
    "seconds_per_update": 0.0006036083999788388,
    "threads": 1,
    "timed_updates": 5,
    "torch": "2.14.1"
  },
  {
    "baseline_RSS_bytes": 213532672,
    "batch": 8,
    "dtype": "float32",
    "peak_RSS_bytes": 316964864,
    "platform": "Darwin",
    "replicate": 1,
    "seconds_per_update": 0.0005996416002744809,
    "threads": 1,
    "timed_updates": 5,
    "torch": "2.14.1"
  },
  {
    "baseline_RSS_bytes": 213385216,
    "batch": 8,
    "dtype": "float32",
    "peak_RSS_bytes": 316751872,
    "platform": "Darwin",
    "replicate": 2,
    "seconds_per_update": 0.0005972499988274649,
    "threads": 1,
    "timed_updates": 5,
    "torch": "2.14.1"
  },
  {
    "baseline_RSS_bytes": 213450752,
    "batch": 32,
    "dtype": "float32",
    "peak_RSS_bytes": 325107712,
    "platform": "Darwin",
    "replicate": 0,
    "seconds_per_update": 0.001458766800351441,
    "threads": 1,
    "timed_updates": 5,
    "torch": "2.14.1"
  },
  {
    "baseline_RSS_bytes": 213417984,
    "batch": 32,
    "dtype": "float32",
    "peak_RSS_bytes": 324812800,
    "platform": "Darwin",
    "replicate": 1,
    "seconds_per_update": 0.0014469916000962257,
    "threads": 1,
    "timed_updates": 5,
    "torch": "2.14.1"
  },
  {
    "baseline_RSS_bytes": 213499904,
    "batch": 32,
    "dtype": "float32",
    "peak_RSS_bytes": 325074944,
    "platform": "Darwin",
    "replicate": 2,
    "seconds_per_update": 0.0013946000020951034,
    "threads": 1,
    "timed_updates": 5,
    "torch": "2.14.1"
  },
  {
    "baseline_RSS_bytes": 213499904,
    "batch": 128,
    "dtype": "float32",
    "peak_RSS_bytes": 357761024,
    "platform": "Darwin",
    "replicate": 0,
    "seconds_per_update": 0.005243049998534843,
    "threads": 1,
    "timed_updates": 5,
    "torch": "2.14.1"
  },
  {
    "baseline_RSS_bytes": 213565440,
    "batch": 128,
    "dtype": "float32",
    "peak_RSS_bytes": 357580800,
    "platform": "Darwin",
    "replicate": 1,
    "seconds_per_update": 0.005442166799912229,
    "threads": 1,
    "timed_updates": 5,
    "torch": "2.14.1"
  },
  {
    "baseline_RSS_bytes": 213237760,
    "batch": 128,
    "dtype": "float32",
    "peak_RSS_bytes": 357269504,
    "platform": "Darwin",
    "replicate": 2,
    "seconds_per_update": 0.0054383249982493,
    "threads": 1,
    "timed_updates": 5,
    "torch": "2.14.1"
  }
]
```

## Publication verification

At content verification, commit `8c5f8fd6b513cf6b35078669fee6036e054c4781` matched remote main and all 178 file blobs with a clean working tree. Final metadata and all five notebooks are separately verified through commit-addressed raw files in the local delivery evidence. Only companion artifacts are published.
