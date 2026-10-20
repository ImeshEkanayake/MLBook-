# Chapter 19 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_093 | 19.1 | 4 | 2 | 1.773 |
| code_094 | 19.2 | 4 | 2 | 1.660 |
| code_095 | 19.3 | 4 | 2 | 1.860 |
| code_096 | 19.4 | 4 | 2 | 1.765 |
| code_097 | 19.5 | 4 | 2 | 1.667 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

Five self-contained CPU laboratories093–097use seeds1993–1997,20code cells and10inline figures. Core Python3.14.3/NumPy2.4.4/SciPy1.17.1/pandas3.0.3/Matplotlib3.11.0/sklearn1.9.0 versions and dependencies are unchanged from Chapter18. Already-pinned threadpoolctl3.7.0 explicitly limits numerical pools toone thread; native sklearnHDBSCAN needs no additional package. All numerical records are generated internally; ordinary execution is offline without files, credentials or GPU. Initial093–096runs passed, with a094FutureWarning about the upcoming HDBSCANcopy default. Its final explicit copy=True preserves inputs and removes that warning without suppression. Initial097computed its experiments but failed its summary because a plotting variable namedtime shadowed the timing module; renaming itminutes and rerunning the entire notebook repaired the execution. Visual review then shortened clipped axis labels in093/095/097, simplified094boundary labels to four examples while retaining eight in the results, and separated density tick labels. Layout-only reruns preserve exact numerical result dictionaries. Final outputs contain no errors or solver warnings. Synthetic annotations make validity and event audits possible here; field completeness and physical or causal interpretation are not asserted.

093generates independent train240/development80/final200from2Gaussian components with means[-2,0]/[2,.5],covariances[[2,1.25],[1.25,1]]/[[1,-.65],[-.65,1.5]],prior.5. Fixed2groups compare objectives rather than selecting count from final annotations. Training-onlyStandardScaler precedes KMeans20starts, full/sphericalGaussianMixture5starts/regcov1e-4, and manually specified alternatingEuclideanmedoids12starts. The medoid heuristic is local, not a global PAM solver; selected medoids are actual training IDs64/68. Selected medoid distance history359.908→215.388→206.955→202.553 is nonincreasing; kmeans squared-distance sum244.744 is a different objective. Final generator-component ARI KMeans.369334/medoids.433019/fullmixture.791060/sphericalmixture.134189. Full/spherical final mean logdensity -2.319978/-2.772793 in standardized coordinates, development -2.196694/-2.629759. Densities are not attached to centroid/medoid objectives. Responsibilities sumtoone, meanmax.964159 and fractionmax<.8 .065; not verified operating truth. All12single-startkmeans seeds reach the same objective244.743614 and same partition: retain this absence of observed initialization instability. Raw storage scaling[1000,1]versus standardized partition ARI.794191; consistently trained scaling after unit conversion restoresARI1. Fitted ellipses are one-covariance contours, not mean confidence intervals.

094uses exactly260transductive analysis points:180densemoonnoiseSD.04/60sparsemoonnoiseSD.08/20uniformbackground. Declared original dimensionless coordinate geometry is fixed, no target-driven parameter search. KMeans2/Ward2/singlelinkage2/DBSCANeps.18,min_samples7/nativeHDBSCANminsize20,min_samples7,copyTrue/spectral2denseRBFgamma8precomputedcluster_qr use the samepointset. Counts clusters/noise respectively2/0,2/0,2/0,6/17,2/24,2/0. ARI on known moon records .163408/.231146/0/.895463/.957673/.374844; all-record ARI also reported. Sparse/background provenance is not identical to algorithmic noise. Fixed spectral performance is retained, not retuned to a desired picture. DBSCANeps.12/.18/.30 gives3/6/3clusters and noise fractions.211538/.065385/.030769;HDBminsize12/20/40 gives3/2/2clusters and.042308/.092308/.092308noise. NativeHDBminimum samples counts itself, not asserted equivalent to contrib defaults. Twentycoordinate-jitterSD.025DBSCANrefits have meanARI.973249/min.948183;case213/231clustered10of20 despite highaggregateagreement. Eightboundary-sensitive IDs anddenominators are retained;fourlabelledillustrations avoid collisions. No new-query contract is claimed for all transductive methods.

095generates train300/dev100/final200,3operatingGaussianregimes and4redundant noisy sensors with separately generated Bernoulli fault targets. Training-onlyScaler/KMeansK2/3/5 uses no targets. FixedC1logistic fits raw sensors orrawplusclusterindicators; developmentBrier selectsK3. K2/3/5training silhouette .471428/.629582/.431422 and generator-regimeARI .583047/.961994/.696761 are separate audits. Final raw-baselineBrier .143206/logloss.441282;cluster-augmentedK2/3/5Brier .145857/.146014/.145397,logloss.447203/.448492/.450705. Thus the selected stable/regime-matching clusters do not improve the final fault predictor in this realization. No final retuning occurs. Twenty completeScaler/KMeanssensor-noiseSD.15refits perK preserve case IDs; meanARI .990610/.986421/.796752,min .973238/.950625/.559064. Selected training cluster×generatorregime contingency[[3,95,0],[94,1,0],[0,0,107]]retains300counts. ClusterlabelpermutationARI1asserts identityinvariance. No physical fault mechanism or independent review interpretation is inferred from generator agreement.

096admitted reference480centralrho.95bivariateGaussian+20rarevalidnear[5,5],independentcal240central+10rarevalid(same4%fraction). Final diagnostic cohorts200central/20rarevalid/20isolated-loadnear[4.5,0]/20unusual-combinationnear[1.8,-1.8]have declared provenance, not population-prevalence estimates. Training-onlystandardization precedes marginalmedian/MAD,maxabsolutez;robustMinCovDetMahalanobis(supportfraction.85);IsolationForest100;LOF20noveltyTrue;OneClassSVMnu.05/gammascale;GMM2full5starts/regcov1e-4neglogdensity. Scores are orientedhigh=unusual, not anomaly probabilities. LOFscore_samples is called onlyonnewcal/final, neverfittingrecords. Each independent250recordcal95thpercentile threshold has strict empiricalalarmfraction.052(13/250), not an exact5%guarantee. Finalcentral/rarevalid/isolated/joint alarm counts: MAD2/20/20/0;robustcov5/20/20/20;isolation1/17/19/1;LOF9/0/20/20;oneclass11/8/20/20;mixture8/6/20/20. Denominators200/20/20/20remainvisible. Rare valid rejection exposes reference/score assumptions; lowdensity is not automatically error or damage. Density coordinates and nonuniform task definitions are disclosed. No method is crowned universally best.

097uses ring10connections with row-normalized symmetric neighborweights.5.80admitted reference/80independentcal/120finalsteps arefive minutes apart; readings2commonload+nodeoffset+commonambient+.03independentnoise. Finalconnection4has+.3implantsteps50–59atload.8;validcommonload1.5steps80–89raisesall10sensors. Contemporaneous neighbor readings are assumed available; no future reading enters point scores. Clean-referenceglobalrawz/graphcontrastz/PCA1reconstructionresidualz use independentcal99thpercentile across800sensorchecks. These are not800independentepisodes. Over1190normalfinalsensorchecks and10operatinghours, clean global/graph/PCA detect8/10/10of10eventpoints with103/41/24falsepointflags,10.3/4.1/2.4falseflags/hour. Validextremewindow flags100/2/1of100checks. Graph flags can spread to adjacentconnections. Snapshotstep55rawmean1.695839,max|contextz|8.725923;step85validhighermean2.919871,max1.946249. Grayscale signedz/nodeIDs/star4make the distinction explicit.

097contamination injects+.3intonode4in30of80reference steps, refits only declared scorers and recalibrates on the same clean calibration. Allthree then detect0of10eventpoints;falsepointflags106/21/21 and validextremewindow100/2/2. Fewerfalseflags undergraph/PCA accompanies complete masking, not improvement. A clean-reference one-sidedCUSUMnode4 usesdrift.5,h=max(5,maxcalunresetstat)=5,resetonalarmand skipsnext5steps. Alerts50/56bothinevent, firstdelay0minutes at5-minute resolution, nofalsealerts inthisfinite10hwindow;no long-run rate orinstantaneousguarantee. Pointflag, sequentialalert andoperatingepisode denominators remain different. Selectivereview sorts51clean graph flagsbyscoreandreviews everysecond:26reviewed,oracle5true/21false,25unreviewedunknown,reviewedprecision.192308. Unknowns never become assumed true negatives, and reviewfeedback doesnotretunethisassessment.

Ten original vector figure sets implement both original briefs: same-point centroid/density/connectivity partitions, and a locally inconsistent connection versus a globally extreme valid common-load regime. Six numbered equations andtwelveexercises cover the five exact scopes. Official clustering/mixture/HDBSCAN/spectral/novelty references and NIST's CUSUM handbook were inspected20October2026. Live sklearn1.9.1 documentation differs from executed1.9.0. No literature completeness, field validity, causal diagnosis or universal false-alarm control is asserted.

## Successful result dictionaries

### code_093

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1993.

```json
{
  "mixture_densities": {
    "density_coordinates": "training-standardized descriptors",
    "final_fraction_max_responsibility_below_08": 0.065,
    "final_mean_max_responsibility": 0.9641588173668584,
    "full_development_mean_log_density": -2.1966936170350144,
    "full_final_mean_log_density": -2.319977579935062,
    "spherical_development_mean_log_density": -2.6297590836922344,
    "spherical_final_mean_log_density": -2.772793081792603
  },
  "objectives": {
    "comparisons": [
      {
        "final_component_ARI": 0.36933365019389475,
        "model": "KMeans",
        "training_component_ARI": 0.5733161842473165
      },
      {
        "final_component_ARI": 0.43301946359096755,
        "model": "Medoids",
        "training_component_ARI": 0.5860742046039426
      },
      {
        "final_component_ARI": 0.7910604469776511,
        "model": "Full mixture",
        "training_component_ARI": 0.8243358431042703
      },
      {
        "final_component_ARI": 0.1341886268441495,
        "model": "Spherical mixture",
        "training_component_ARI": 0.2642215303452215
      }
    ],
    "kmeans_training_squared_distance_sum": 244.74361417958158,
    "medoid_starts": 12,
    "medoid_training_distance_sum": 202.55333856207534,
    "medoid_training_record_ids": [
      64,
      68
    ],
    "selected_medoid_cost_history": [
      359.9081854070819,
      215.38845522602736,
      206.9549517537722,
      202.55333856207534
    ]
  },
  "roles": {
    "component_count_fixed": 2,
    "development_diagnostic": 80,
    "final": 200,
    "training": 240
  },
  "sensitivity": {
    "consistently_standardized_unit_conversion_ARI": 1.0,
    "raw_unit_changed_vs_standardized_partition_ARI": 0.7941912369563172,
    "single_random_start_fits": [
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 1993
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 1994
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 1995
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 1996
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 1997
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 1998
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 1999
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 2000
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 2001
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 2002
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 2003
      },
      {
        "ARI_with_twenty_start_partition": 1.0,
        "inertia": 244.74361417958158,
        "seed": 2004
      }
    ]
  }
}
```

### code_094

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1994.

```json
{
  "analysis_contract": {
    "HDBSCAN_min_samples_includes_self": true,
    "dense_moon": 180,
    "geometry": "declared original dimensionless descriptors",
    "new_query_predictor_claimed": false,
    "sparse_moon": 60,
    "spectral_RBF_gamma": 8,
    "transductive_records": 260,
    "uniform_background": 20
  },
  "parameter_diagnostics": [
    {
      "clusters": 3,
      "method": "DBSCAN",
      "noise_fraction": 0.21153846153846154,
      "parameter": 0.12
    },
    {
      "clusters": 6,
      "method": "DBSCAN",
      "noise_fraction": 0.06538461538461539,
      "parameter": 0.18
    },
    {
      "clusters": 3,
      "method": "DBSCAN",
      "noise_fraction": 0.03076923076923077,
      "parameter": 0.3
    },
    {
      "clusters": 3,
      "method": "HDBSCAN",
      "noise_fraction": 0.04230769230769231,
      "parameter": 12
    },
    {
      "clusters": 2,
      "method": "HDBSCAN",
      "noise_fraction": 0.09230769230769231,
      "parameter": 20
    },
    {
      "clusters": 2,
      "method": "HDBSCAN",
      "noise_fraction": 0.09230769230769231,
      "parameter": 40
    }
  ],
  "partitions": [
    {
      "all_record_generator_ARI": 0.1379900942232203,
      "clusters_excluding_noise": 2,
      "known_moon_record_ARI": 0.16340807180120592,
      "method": "KMeans",
      "noise_rows": 0
    },
    {
      "all_record_generator_ARI": 0.19597879453716974,
      "clusters_excluding_noise": 2,
      "known_moon_record_ARI": 0.23114566584386706,
      "method": "Ward hierarchy",
      "noise_rows": 0
    },
    {
      "all_record_generator_ARI": 0.015365900505794224,
      "clusters_excluding_noise": 2,
      "known_moon_record_ARI": 0.0,
      "method": "Single linkage",
      "noise_rows": 0
    },
    {
      "all_record_generator_ARI": 0.8399880305680877,
      "clusters_excluding_noise": 6,
      "known_moon_record_ARI": 0.8954627526179337,
      "method": "DBSCAN",
      "noise_rows": 17
    },
    {
      "all_record_generator_ARI": 0.8723011175320959,
      "clusters_excluding_noise": 2,
      "known_moon_record_ARI": 0.9576728947135393,
      "method": "HDBSCAN",
      "noise_rows": 24
    },
    {
      "all_record_generator_ARI": 0.3229506642433475,
      "clusters_excluding_noise": 2,
      "known_moon_record_ARI": 0.3748436256112817,
      "method": "Spectral graph",
      "noise_rows": 0
    }
  ],
  "sensor_jitter": {
    "boundary_records": [
      {
        "background_generator_annotation": false,
        "clustered_count": 10,
        "clustered_fraction": 0.5,
        "original_id": 213,
        "reruns": 20
      },
      {
        "background_generator_annotation": false,
        "clustered_count": 10,
        "clustered_fraction": 0.5,
        "original_id": 231,
        "reruns": 20
      },
      {
        "background_generator_annotation": true,
        "clustered_count": 11,
        "clustered_fraction": 0.55,
        "original_id": 258,
        "reruns": 20
      },
      {
        "background_generator_annotation": false,
        "clustered_count": 8,
        "clustered_fraction": 0.4,
        "original_id": 196,
        "reruns": 20
      },
      {
        "background_generator_annotation": false,
        "clustered_count": 13,
        "clustered_fraction": 0.65,
        "original_id": 198,
        "reruns": 20
      },
      {
        "background_generator_annotation": false,
        "clustered_count": 13,
        "clustered_fraction": 0.65,
        "original_id": 201,
        "reruns": 20
      },
      {
        "background_generator_annotation": false,
        "clustered_count": 7,
        "clustered_fraction": 0.35,
        "original_id": 223,
        "reruns": 20
      },
      {
        "background_generator_annotation": false,
        "clustered_count": 13,
        "clustered_fraction": 0.65,
        "original_id": 232,
        "reruns": 20
      }
    ],
    "coordinate_noise_SD": 0.025,
    "partition_ARI_mean": 0.9732486616075496,
    "partition_ARI_min": 0.948182580136571,
    "reruns": 20
  }
}
```

### code_095

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1995.

```json
{
  "arbitrary_label_permutation_ARI": 1.0,
  "candidates": [
    {
      "development_brier": 0.14046796202113151,
      "final_brier": 0.14585692078591722,
      "final_log_loss": 0.4472031549829282,
      "k": 2,
      "training_generator_regime_ARI": 0.5830470344652239,
      "training_silhouette": 0.4714283429677616
    },
    {
      "development_brier": 0.1393186348673421,
      "final_brier": 0.14601357141117086,
      "final_log_loss": 0.44849161675057914,
      "k": 3,
      "training_generator_regime_ARI": 0.961994444346516,
      "training_silhouette": 0.6295820157518648
    },
    {
      "development_brier": 0.13994995852980568,
      "final_brier": 0.14539703493103975,
      "final_log_loss": 0.4507053742301881,
      "k": 5,
      "training_generator_regime_ARI": 0.6967607381882451,
      "training_silhouette": 0.43142198631778966
    }
  ],
  "raw_sensor_baseline": {
    "development_brier": 0.14124082131462748,
    "final_brier": 0.14320639587282188,
    "final_log_loss": 0.4412816201536072
  },
  "roles": {
    "development": 100,
    "final": 200,
    "selection_metric": "downstream development Brier",
    "targets_used_to_fit_clusters": false,
    "training": 300
  },
  "selected_k": 3,
  "selected_training_contingency": {
    "columns": "generator regime0/1/2",
    "counts": [
      [
        3,
        95,
        0
      ],
      [
        94,
        1,
        0
      ],
      [
        0,
        0,
        107
      ]
    ],
    "independent_interpretation_claimed": false,
    "rows": "arbitrary selected cluster IDs"
  },
  "sensor_resampling": [
    {
      "k": 2,
      "maximum_ARI": 1.0,
      "mean_ARI": 0.9906100167892055,
      "minimum_ARI": 0.9732382120263898,
      "reruns": 20
    },
    {
      "k": 3,
      "maximum_ARI": 1.0,
      "mean_ARI": 0.9864209378478301,
      "minimum_ARI": 0.9506246536748723,
      "reruns": 20
    },
    {
      "k": 5,
      "maximum_ARI": 0.9150906007056077,
      "mean_ARI": 0.7967515838066785,
      "minimum_ARI": 0.5590639844236901,
      "reruns": 20
    }
  ]
}
```

### code_096

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1996.

```json
{
  "reference_contract": {
    "LOF_fitting_rows_scored_as_novelty": false,
    "calibration_central": 240,
    "calibration_rare_valid": 10,
    "density_units": "training-standardized descriptor coordinates",
    "final_cohort_counts": {
      "Isolated load": 20,
      "Rare valid": 20,
      "Unusual combination": 20,
      "Valid central": 200
    },
    "fit_central": 480,
    "fit_rare_valid": 20,
    "rare_valid_reference_fraction": 0.04,
    "scores_are_anomaly_probabilities": false,
    "threshold_quantile": 0.95
  },
  "scores": [
    {
      "calibration_alarm_fraction_strict_greater": 0.052,
      "calibration_rows": 250,
      "calibration_threshold": 2.4963515724933214,
      "final_cohorts": [
        {
          "alarm_fraction": 0.01,
          "alarms": 2,
          "cohort": "Valid central",
          "rows": 200
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Rare valid",
          "rows": 20
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Isolated load",
          "rows": 20
        },
        {
          "alarm_fraction": 0.0,
          "alarms": 0,
          "cohort": "Unusual combination",
          "rows": 20
        }
      ],
      "method": "Marginal MAD"
    },
    {
      "calibration_alarm_fraction_strict_greater": 0.052,
      "calibration_rows": 250,
      "calibration_threshold": 7.792450118331392,
      "final_cohorts": [
        {
          "alarm_fraction": 0.025,
          "alarms": 5,
          "cohort": "Valid central",
          "rows": 200
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Rare valid",
          "rows": 20
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Isolated load",
          "rows": 20
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Unusual combination",
          "rows": 20
        }
      ],
      "method": "Robust covariance"
    },
    {
      "calibration_alarm_fraction_strict_greater": 0.052,
      "calibration_rows": 250,
      "calibration_threshold": 0.6377249885524471,
      "final_cohorts": [
        {
          "alarm_fraction": 0.005,
          "alarms": 1,
          "cohort": "Valid central",
          "rows": 200
        },
        {
          "alarm_fraction": 0.85,
          "alarms": 17,
          "cohort": "Rare valid",
          "rows": 20
        },
        {
          "alarm_fraction": 0.95,
          "alarms": 19,
          "cohort": "Isolated load",
          "rows": 20
        },
        {
          "alarm_fraction": 0.05,
          "alarms": 1,
          "cohort": "Unusual combination",
          "rows": 20
        }
      ],
      "method": "Isolation forest"
    },
    {
      "calibration_alarm_fraction_strict_greater": 0.052,
      "calibration_rows": 250,
      "calibration_threshold": 1.3419543055036711,
      "final_cohorts": [
        {
          "alarm_fraction": 0.045,
          "alarms": 9,
          "cohort": "Valid central",
          "rows": 200
        },
        {
          "alarm_fraction": 0.0,
          "alarms": 0,
          "cohort": "Rare valid",
          "rows": 20
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Isolated load",
          "rows": 20
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Unusual combination",
          "rows": 20
        }
      ],
      "method": "LOF novelty"
    },
    {
      "calibration_alarm_fraction_strict_greater": 0.052,
      "calibration_rows": 250,
      "calibration_threshold": -5.853401838022919,
      "final_cohorts": [
        {
          "alarm_fraction": 0.055,
          "alarms": 11,
          "cohort": "Valid central",
          "rows": 200
        },
        {
          "alarm_fraction": 0.4,
          "alarms": 8,
          "cohort": "Rare valid",
          "rows": 20
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Isolated load",
          "rows": 20
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Unusual combination",
          "rows": 20
        }
      ],
      "method": "One-class SVM"
    },
    {
      "calibration_alarm_fraction_strict_greater": 0.052,
      "calibration_rows": 250,
      "calibration_threshold": 3.258289959830523,
      "final_cohorts": [
        {
          "alarm_fraction": 0.04,
          "alarms": 8,
          "cohort": "Valid central",
          "rows": 200
        },
        {
          "alarm_fraction": 0.3,
          "alarms": 6,
          "cohort": "Rare valid",
          "rows": 20
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Isolated load",
          "rows": 20
        },
        {
          "alarm_fraction": 1.0,
          "alarms": 20,
          "cohort": "Unusual combination",
          "rows": 20
        }
      ],
      "method": "Mixture density"
    }
  ]
}
```

### code_097

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1997.

```json
{
  "contract": {
    "calibration_sensor_checks": 800,
    "calibration_steps": 80,
    "connections": 10,
    "contaminated_reference_steps": 30,
    "contemporaneous_neighbors_available": true,
    "event_connection_zero_based": 4,
    "event_steps_inclusive": [
      50,
      59
    ],
    "final_operating_hours": 10.0,
    "final_steps": 120,
    "flags_are_independent_events": false,
    "future_readings_used_for_point_scores": false,
    "minutes_per_step": 5,
    "point_threshold_quantile": 0.99,
    "reference_steps": 80,
    "valid_commonload_extreme_steps_inclusive": [
      80,
      89
    ]
  },
  "illustrated_snapshots": [
    {
      "max_abs_context_z": 8.725923422567888,
      "raw_mean": 1.6958393269308132,
      "step": 55
    },
    {
      "max_abs_context_z": 1.946249345523678,
      "raw_mean": 2.919871060248269,
      "step": 85
    }
  ],
  "point_alarms": [
    {
      "calibration_threshold": 2.069247510682708,
      "event_point_denominator": 10,
      "false_flags_per_1000_normal_checks": 86.5546218487395,
      "false_point_flags": 103,
      "false_point_flags_per_operating_hour": 10.3,
      "normal_sensor_checks": 1190,
      "reference": "Admitted clean",
      "score": "Global raw",
      "true_event_point_flags": 8,
      "valid_extreme_window_flags": 100
    },
    {
      "calibration_threshold": 2.560658067712572,
      "event_point_denominator": 10,
      "false_flags_per_1000_normal_checks": 34.45378151260504,
      "false_point_flags": 41,
      "false_point_flags_per_operating_hour": 4.1,
      "normal_sensor_checks": 1190,
      "reference": "Admitted clean",
      "score": "Graph context",
      "true_event_point_flags": 10,
      "valid_extreme_window_flags": 2
    },
    {
      "calibration_threshold": 2.8254729616762657,
      "event_point_denominator": 10,
      "false_flags_per_1000_normal_checks": 20.168067226890756,
      "false_point_flags": 24,
      "false_point_flags_per_operating_hour": 2.4,
      "normal_sensor_checks": 1190,
      "reference": "Admitted clean",
      "score": "PCA reconstruction",
      "true_event_point_flags": 10,
      "valid_extreme_window_flags": 1
    },
    {
      "calibration_threshold": 2.03673164951919,
      "event_point_denominator": 10,
      "false_flags_per_1000_normal_checks": 89.07563025210084,
      "false_point_flags": 106,
      "false_point_flags_per_operating_hour": 10.6,
      "normal_sensor_checks": 1190,
      "reference": "Contaminated reference",
      "score": "Global raw",
      "true_event_point_flags": 0,
      "valid_extreme_window_flags": 100
    },
    {
      "calibration_threshold": 2.4285828488876313,
      "event_point_denominator": 10,
      "false_flags_per_1000_normal_checks": 17.647058823529413,
      "false_point_flags": 21,
      "false_point_flags_per_operating_hour": 2.1,
      "normal_sensor_checks": 1190,
      "reference": "Contaminated reference",
      "score": "Graph context",
      "true_event_point_flags": 0,
      "valid_extreme_window_flags": 2
    },
    {
      "calibration_threshold": 2.5677550098945883,
      "event_point_denominator": 10,
      "false_flags_per_1000_normal_checks": 17.647058823529413,
      "false_point_flags": 21,
      "false_point_flags_per_operating_hour": 2.1,
      "normal_sensor_checks": 1190,
      "reference": "Contaminated reference",
      "score": "PCA reconstruction",
      "true_event_point_flags": 0,
      "valid_extreme_window_flags": 2
    }
  ],
  "review_ledger": {
    "feedback_used_to_retune_final": false,
    "graph_point_flags": 51,
    "reviewed": 26,
    "reviewed_oracle_false": 21,
    "reviewed_oracle_true": 5,
    "selectively_reviewed_precision": 0.19230769230769232,
    "unknown_counted_as_true_negative": false,
    "unreviewed_status_unknown": 25
  },
  "sequence_alerts": {
    "CUSUM_drift": 0.5,
    "alert_steps": [
      50,
      56
    ],
    "connection": 4,
    "event_alert_steps": [
      50,
      56
    ],
    "false_alert_steps": [],
    "false_alerts_per_operating_hour": 0.0,
    "final_threshold_changed": false,
    "first_event_delay_minutes": 0,
    "refractory_skipped_steps": 5,
    "threshold": 5.0,
    "threshold_rule": "max(5,maximum unreset calibration statistic)"
  }
}
```

