# GRID_RECOVERABILITY_METHOD_QUALIFICATION_PLAN_v0.1_20261001.md

**Status:** P0-Q SYNTHETIC METHOD QUALIFICATION — NO REAL RECOVERY OUTCOMES OPEN  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** governance/GRID_RECOVERABILITY_CENTRAL_HYPOTHESIS_v0.1_20261001.md  
**Governance:** SymC GOM v1.0 + Continuity Hardening Addendum

## 1. Purpose

Qualify the minimum causal machinery needed to distinguish:
- ordinary perturbation + ordinary recovery;
- delayed but ordinary recovery;
- baseline migration with unchanged recovery law;
- changed recovery law with little baseline migration;
- interruption by a new perturbation;
- stable reorganization;
- transient amplification with eventual normal recovery;
- history-dependent erosion;
- history-dependent strengthening;
- measurement/data-quality artifacts.

No real grid event may be labeled NORMAL or ABNORMAL during this stage.

## 2. Nearest-prior-art collision result

The dedicated literature searches found strong adjacent work but no exact matched-event protocol combining moving-baseline separation, sustained recovery, interruption, and incremental history dependence.

Closest occupied territories include:
- power-system resilience trend and outage/restore analysis: Shen et al. 2018, DOI 10.1016/J.RESS.2018.05.006; Afsharinejad et al. 2021, DOI 10.1016/j.joule.2021.07.006;
- sequential/major-event resilience with pre-event condition: Nassif et al. 2022, DOI 10.1109/PESGM48719.2022.9916682;
- PMU frequency-response evaluation: Zhang et al. 2023, DOI 10.1109/GTD49768.2023.00049;
- operational synchrophasor voltage-recovery assessment: Pinzon et al. 2023, DOI 10.1109/ISGT-LA56058.2023.10328255;
- synchrophasor frequency performance indicators: Pinzon 2024, DOI 10.1109/GTDLA61236.2024.10913829;
- empirical PMU event classification and signature libraries: Liu et al., DOI 10.1109/JIOT.2022.3177686; Yamashita et al. 2022, DOI 10.1109/ACCESS.2022.3205321;
- operating-point/nonstationary dynamics: Kruse et al. 2023, DOI 10.1103/prxenergy.2.043003; Sheng & Wang, DOI 10.1109/TSG.2019.2917672; Wang, Bialek & Turitsyn, DOI 10.1109/TPWRS.2017.2712762;
- recovery-condition computation: Fisher & Hiskens 2025, DOI 10.1109/TPWRS.2025.3600275.

Current novelty ceiling:
the new work may investigate **conditional repeated-perturbation recoverability**; it may not claim novelty for resilience curves, recovery time, PMU event classification, moving operating points, modal tracking, or disturbance-recovery analysis generically.

## 3. Qualification objects

### Native synthetic state
Use generic state (Z_t), not chi-derived quantities.

### Candidate baseline operators
K1 — causal trailing robust location:
- past-only rolling median / robust location;
- fixed window;
- no outcome use.

K2 — causal local-trend baseline:
- past-only local linear trend fit;
- fixed lookback;
- predicts the current baseline from prior samples;
- no outcome use.

The purpose is not to prove either operator universally correct. It is to test whether either can distinguish baseline motion from recovery-law change under known truths.

### Conditional-noise object
Estimate a separate past-only robust scale (Sigma_t). Baseline location and noise scale must not be the same estimand.

### Perturbation coordinate
For synthetic qualification only:
[
d_t = |Z_t-B_t|/Sigma_t.
]
No real-data threshold is inherited from this expression.

## 4. Known-truth scenarios

S01 stationary baseline + fixed recovery + isolated shock.  
Expected: no recovery-law change.

S02 stationary baseline + larger shock + same recovery.  
Expected: larger excursion, same conditional recovery law.

S03 drifting baseline + fixed recovery.  
Expected: baseline migration, no recovery-law change.

S04 noise variance increase only.  
Expected: noise-state change, no recovery-law change.

S05 true recovery slowing after a change point.  
Expected: detect recovery-law deterioration without requiring baseline movement.

S06 true recovery strengthening after a change point.  
Expected: detect adaptation/strengthening.

S07 repeated shocks with unchanged recovery law.  
Expected: no false history-dependence claim.

S08 cumulative-burden erosion: recovery rate decreases with prior perturbation burden.  
Expected: history adds information beyond current shock size/state.

S09 cumulative-burden strengthening: recovery rate increases with prior perturbation history.  
Expected: opposite-direction history effect is detected.

S10 second shock before sustained return.  
Expected: INTERRUPTED_BY_NEW_PERTURBATION, not ordinary right censoring and not automatic failed recovery.

S11 stable baseline/set-point shift after a shock with unchanged local recovery around the new state.  
Expected: STABLE_REORGANIZATION, not deterioration.

S12 stable non-normal two-dimensional system with transient amplification.  
Expected: high (A_{transient}) may coexist with normal asymptotic recovery.

S13 missing/stale/zero-filled measurement artifact.  
Expected: refuse or artifact flag, not abnormal recovery.

S14 mixed scenario: drifting baseline + heteroskedastic noise + repeated shocks + no recovery-law change.  
Expected: no false deterioration after conditioning.

## 5. Recovery measurements to qualify

Per synthetic event:
- (T_{first}): first reclaim;
- (T_{sustain}): sustained reclaim;
- (A_{transient}): max amplification relative to entry;
- (I_{burden}): integrated normalized displacement;
- (D_{dwell}): recovered-side dwell;
- (E_H): residual displacement at frozen horizon;
- (Delta B): baseline migration;
- interruption indicator;
- known recovery-rate truth where defined.

No one-number recovery score is used for qualification.

## 6. Primary qualification questions

Q-A: Which baseline operator has lower normalized baseline-location error without inventing recovery-law changes in S01-S04/S07/S11-S14?

Q-B: Can the machinery distinguish S03/S11 baseline migration from S05 recovery deterioration?

Q-C: Does perturbation size alone falsely drive the recovery label in S02?

Q-D: Are interrupted events in S10 kept separate from non-recovery?

Q-E: Is transient amplification in S12 kept separate from asymptotic recovery failure?

Q-F: Can the method detect both erosion S08 and strengthening S09?

## 7. Selection rule

1. K1 and K2 must both pass numerical/causal checks.
2. Any operator that falsely labels S03, S04, S11, S13, or S14 as recovery deterioration is ineligible.
3. Any operator that fails to detect the known recovery-law change in S05 is ineligible.
4. If one operator remains, it becomes the candidate primary baseline operator.
5. If both remain, choose the lower median normalized baseline-location error across S01-S14.
6. If neither remains, return BASELINE_OPERATOR_REFUSED and revise before real data.

This rule is frozen before real recovery outcomes.

## 8. MFR-style falsification floor

The method must be able to fail under:
1. moving baseline;
2. changing noise;
3. large normal shock;
4. small abnormal recovery;
5. repeated normal shocks;
6. history-dependent erosion;
7. history-dependent strengthening;
8. overlapping shocks;
9. stable reorganization;
10. non-normal transient amplification;
11. missingness;
12. zero-fill/staleness;
13. sparse data;
14. wrong sampling interval / timestamp gap.

## 9. Real-data gate after synthetic qualification

Only after the synthetic stage:
- apply source QI;
- preserve native mHz units;
- construct causal local baselines;
- derive event candidates using outcome-blind input geometry;
- hold back untouched systems/time blocks;
- estimate normal conditional recovery envelopes on development data;
- compare current-state-only versus current-state+history models;
- freeze all thresholds/model forms;
- evaluate untouched events.

No chi/Χ/Χ_arc term is required for the first real recovery lane.

## 10. Failure outcomes

Valid outcomes include:
- BASELINE_OPERATOR_REFUSED;
- RECOVERY_NOT_IDENTIFIABLE;
- HISTORY_ADDS_NO_VALUE;
- EVENT_MAGNITUDE_EXPLAINS_RECOVERY;
- BASELINE_MIGRATION_EXPLAINS_APPARENT_CHANGE;
- MEASUREMENT_ARTIFACT;
- NATIVE_MODEL_SUFFICIENT;
- RECOVERABILITY_HYPOTHESIS_SUPPORTED_WITHIN_SCOPE.

No negative result is overridden by the historical paper.
