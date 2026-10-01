# GRID_REAL_DATA_PARTITION_MANIFEST_v0.1_20261001.md

**Status:** FROZEN / RECOVERY OUTCOMES SEALED  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Source rule:** governance/GRID_REAL_DATA_INTAKE_AND_HOLDOUT_FREEZE_v0.1_20261001.md

## 1. Manifest identities

Local machine artifacts:
- GRID_QI_CAMPAIGN_MANIFEST_v01.csv
- GRID_TEMPORAL_PARTITION_CUTS_v01.csv
- GRID_QI_PARTITION_SUMMARY_v01.json

SHA-256:
- campaign manifest: **41733f9498090a173c61f61b4003ae0b0fa4dc306aa592af99271e6ba29c18bb**
- temporal cuts: **d71e9e751e2744b58d2f75ecd821262b96be685b4ea537e791fe05e1948e18fc**

No recovery metric, event outcome, chi quantity, or normal/abnormal label was computed to produce these files.

## 2. Primary development campaigns

| Grid | Campaign | Primary channel | QI=0 valid seconds | QI=0 fraction |
|---|---|---|---:|---:|
| BALTIC | EE01 | f50_EE | 1,974,144 | 0.999963 |
| CONTINENTAL_EUROPE | sync01 | f50_DE_KA | 3,542,400 | 1.000000 |
| GREAT_BRITAIN | GB02 | f50_UK | 4,422,918 | 0.984446 |
| ICELAND | IS01 | f50_IS | 367,803 | 0.759575 |
| MALLORCA | ES_PM02 | f50_ES_PM | 26,468,589 | 0.837020 |
| NORDIC | SE01 | f50_SE | 565,853 | 0.978490 |
| WESTERN_INTERCONNECTION | US_UT | f60_US_UT01 | 548,793 | 0.995902 |

Primary campaign selection was determined only by maximum QI=0 valid seconds within each development synchronous area.

## 3. Same-grid replication holdouts

These are not used for method development:

- CONTINENTAL_EUROPE: FR01, HR01, IT01, PL01, PT01
- GREAT_BRITAIN: GB01
- MALLORCA: ES_PM01, ES_PM03

They become available only after the recovery/event method is frozen.

## 4. Whole-grid transport holdouts

Completely sealed beyond source/QI metadata:

### RUSSIA
- RU01 primary holdout
- QI=0 valid seconds: 981,340

### GRAN_CANARIA
- ES_GC01 primary holdout: 557,521 QI=0 seconds
- ES_GC02 replication holdout: 75,946 QI=0 seconds

### ERCOT
- US_TX02 primary holdout: 306,224 QI=0 seconds
- US_TX01 replication holdout: 123,883 QI=0 seconds

## 5. Quality-limited auxiliary/refusal sets

- FAROE_ISLANDS / FO01: 373,288 QI=0 seconds; QI=0 fraction 0.6672.
- SOUTH_AFRICA / ZA01: 546,382 QI=0 seconds; QI=0 fraction 0.6644.

These cannot decide primary transport success. They test refusal/data-quality behavior.

## 6. Frozen temporal cuts in primary development campaigns

| Grid | Development end 60% | Internal-validation end 80% | Temporal holdout end |
|---|---|---|---|
| BALTIC | 2019-04-08 04:11:20 UTC | 2019-04-12 17:52:06 UTC | 2019-04-17 07:32:47 UTC |
| CONTINENTAL_EUROPE | 2019-08-02 14:23:59 UTC | 2019-08-10 19:11:59 UTC | 2019-08-18 23:59:59 UTC |
| GREAT_BRITAIN | 2019-12-11 12:11:47 UTC | 2019-12-21 18:16:30 UTC | 2019-12-31 23:59:59 UTC |
| ICELAND | 2017-10-18 14:43:42 UTC | 2017-10-19 11:10:18 UTC | 2017-10-20 07:54:06 UTC |
| MALLORCA | 2020-07-05 12:59:23 UTC | 2020-10-31 17:15:32 UTC | 2020-12-31 23:59:59 UTC |
| NORDIC | 2019-05-10 14:34:51 UTC | 2019-05-11 22:34:29 UTC | 2019-05-13 06:54:20 UTC |
| WESTERN_INTERCONNECTION | 2019-05-22 22:59:38 UTC | 2019-05-24 05:28:58 UTC | 2019-05-25 11:58:16 UTC |

An embargo equal to the later-frozen maximum causal baseline lookback plus recovery horizon will be applied around the 60% and 80% boundaries before any episode construction.

## 7. Intake observations

The QI scan confirms that source-level "bad data" must be resolved at the channel level. Some campaign-level metadata summaries do not exactly equal the local channel's QI=0 fraction.

Therefore:
- primary eligibility uses the actual selected channel QI;
- source metadata remains provenance/context;
- scientific episodes require QI=0 at the selected channel;
- no source-level GoodData percentage substitutes for channel-level QI.

## 8. Next authorized exposure

Only the **DEVELOPMENT portion** of the seven primary campaigns may now be used for:
- baseline input diagnostics;
- fixed robust scale estimation;
- event-coordinate geometry;
- perturbation-entry calibration;
- gap/artifact refusal testing.

Recovery outcomes remain sealed until event-entry, return-set, sustain, horizon and embargo rules are frozen.
