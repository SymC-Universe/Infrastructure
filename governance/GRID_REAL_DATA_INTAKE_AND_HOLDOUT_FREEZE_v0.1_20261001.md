# GRID_REAL_DATA_INTAKE_AND_HOLDOUT_FREEZE_v0.1_20261001.md

**Status:** FROZEN OUTCOME-BLIND REAL-DATA INTAKE / PARTITION DESIGN  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** governance/GRID_RECOVERABILITY_SYNTHETIC_QUALIFICATION_v0.2_RESULT_20261001.md  
**Real recovery outcomes opened:** NO

## 1. Source contract

Primary first-lane source:
Jumar et al., "Database of Power Grid Frequency Measurements," arXiv:2006.01771, with the associated KIT/OSF frequency corpus.

Source-defined facts:
- timestamps are UTC;
- nominal sampling is one second for the primary frequency files;
- f50_* / f60_* are frequency deviations from nominal in **mHz**;
- QI=0: data OK;
- QI=1: invalid data;
- QI=2: interpolated data;
- unavailable synchronized-campaign entries may be zero-filled and marked QI=1.

Primary decisive recovery analysis will use **QI=0 only**.

QI=2 interpolation may be used only in a separately labeled sensitivity analysis.

QI=1 and zero-filled unavailable states are invalid and may not enter scientific recovery trajectories.

## 2. Independent scientific unit

The primary event unit is:

**synchronous area × disturbance episode**.

Multiple measurement locations observing the same synchronous-area episode are correlated views, not independent events.

Repeated f50_DE_KA reference streams embedded in campaign files are reference/context channels and may not inflate sample size.

The synchronized CE campaign (sync01) is a multichannel spatial object, not four independent grids.

## 3. Synchronous-area map

- BALTIC: EE01
- CONTINENTAL_EUROPE: FR01, HR01, IT01, PL01, PT01, sync01 and associated DE_KA reference channels
- ERCOT: US_TX01, US_TX02
- FAROE_ISLANDS: FO01
- GRAN_CANARIA: ES_GC01, ES_GC02
- GREAT_BRITAIN: GB01, GB02
- ICELAND: IS01
- MALLORCA: ES_PM01, ES_PM02, ES_PM03
- NORDIC: SE01
- RUSSIA: RU01
- SOUTH_AFRICA: ZA01
- WESTERN_INTERCONNECTION: US_UT

## 4. Whole-grid transport eligibility

A synchronous area is eligible for decisive whole-grid transport holdout if at least one campaign has:

- source-reported GoodData >= 75%; and
- source-reported maximum continuous section >= 0.5 day.

This is an input-quality rule only. No recovery outcome enters it.

Under the frozen metadata:
- FAROE_ISLANDS fails the criterion;
- SOUTH_AFRICA fails the GoodData criterion;
- the remaining ten synchronous areas qualify.

Faroe Islands and South Africa are retained as QUALITY_LIMITED_AUXILIARY / refusal-stress data rather than discarded.

## 5. Deterministic whole-grid holdout selection

Selection algorithm:

1. eligible synchronous-area labels are uppercase canonical strings;
2. compute SHA-256 of GRID_RECOVERY_V1_20261001|<GRID_ID>;
3. sort ascending by full hash;
4. first three eligible areas are untouched transport holdouts.

Frozen result:

1. **RUSSIA**
2. **GRAN_CANARIA**
3. **ERCOT**

These grids may not be used for:
- baseline-operator revision;
- event-coordinate selection;
- threshold selection;
- recovery-model selection;
- feature selection;
- history-model selection;
- chi/Χ/Χ_arc construction selection.

They remain sealed until the development methodology is frozen.

## 6. Development synchronous areas

Primary method development/qualification areas:

- BALTIC
- CONTINENTAL_EUROPE
- GREAT_BRITAIN
- ICELAND
- MALLORCA
- NORDIC
- WESTERN_INTERCONNECTION

Quality-limited auxiliary stress:
- FAROE_ISLANDS
- SOUTH_AFRICA

## 7. Within-development temporal partition

For every primary development synchronous area:

- first 60% of chronologically ordered QI=0 valid seconds: DEVELOPMENT;
- next 20%: INTERNAL_VALIDATION;
- final 20%: TEMPORAL_HOLDOUT.

Partitioning is done by valid source time, not row number.

No event or recovery statistic enters the cut.

Before outcome analysis, partition boundaries receive an embargo equal to the maximum causal baseline lookback plus maximum recovery horizon so no episode/window crosses folds.

The exact embargo duration will be filled only after those two quantities are frozen from synthetic/input-only qualification.

## 8. Campaign and channel rules

1. Local source channel is primary for single-location cross-grid work.
2. A simultaneously recorded DE_KA/reference channel is context, not an independent replicate.
3. CE multichannel data may enter a separate spatial-recovery lane after single-stream recovery machinery is frozen.
4. Repeated campaigns from the same synchronous area remain grouped under that area.
5. Event dependence is clustered at minimum by synchronous area and episode.
6. Overlapping station detections of the same disturbance must be merged or modeled jointly before event counting.

## 9. Data-quality refusal

A segment is ineligible for primary recovery analysis if:
- source QI is not 0;
- required causal baseline history is unavailable;
- timestamp continuity fails inside an episode;
- a source zero-fill/invalid period intersects the episode;
- the episode crosses a partition boundary/embargo;
- the frozen recovery horizon cannot be observed;
- the relevant native state is not identifiable.

DATA_QUALITY_REFUSED is a scientific disposition, not an imputation invitation.

## 10. Near-title literature collision clarification

Liu, Zhu & Kekatos (2021), "A Dynamic Response Recovery Framework Using Ambient Synchrophasor Data," arXiv:2104.05614, uses "recovery" to mean **recovering/reconstructing dynamic impulse responses from ambient correlations**.

It is highly relevant to dynamic-response inference and rich-PMU comparison, but it does not test the present hypothesis of changing post-disturbance recoverability or history-conditioned sustained recovery.

## 11. Next gate

Mechanical next action:

1. stream through the raw QI columns;
2. construct valid-time counts and contiguous-run metadata;
3. generate exact 60/20/20 cut timestamps for the seven development grids;
4. verify the three external holdout grids remain untouched beyond metadata/QI intake;
5. write a cryptographically identified partition manifest;
6. then qualify event-coordinate/input geometry using DEVELOPMENT only.

No real recovery trajectory outcome is to be computed before that manifest is frozen.
