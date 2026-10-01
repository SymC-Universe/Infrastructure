# GRID_RECOVERABILITY_SYNTHETIC_QUALIFICATION_v0.2_RESULT_20261001.md

**Status:** SYNTHETIC QUALIFICATION PASSED / REAL-GRID RECOVERY OUTCOMES STILL SEALED  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Plan delta:** governance/GRID_RECOVERABILITY_SYNTHETIC_v0.1_FAILURE_AND_v0.2_PLAN_DELTA_20261001.md  
**Executable:** Popstop research_audit/grid_recoverability_synthetic_qualification_v02.py  
**Replications:** 200 fresh replications per scenario; v0.1 seeds not reused.

## 1. Outcome

Both prespecified baseline operators passed all mandatory v0.2 synthetic known-truth criteria.

K1 was selected as the **synthetic-qualified candidate primary baseline operator** because both were eligible and K1 had the lower median normalized baseline-location error.

This does not qualify K1 on real grid data and does not authorize a real-world NORMAL/ABNORMAL threshold.

## 2. Operator summary

### K1 — causal trailing robust location
- eligible: YES
- median normalized baseline-location error: **0.5904**

### K2 — causal local-trend baseline
- eligible: YES
- median normalized baseline-location error: **0.9585**

Selection rule therefore chooses **K1**.

## 3. K1 mandatory known-truth results

Null / no-recovery-law-change scenarios all passed the frozen ensemble criterion:

- S01 stationary: mean late-minus-early recovery coefficient change = -0.00135; 95% CI [-0.00388, +0.00119].
- S02 larger shocks, same recovery: +0.00375; 95% CI [+0.00102, +0.00649].
- S03 moving baseline, same recovery: -0.00104; 95% CI [-0.00347, +0.00139].
- S04 changing noise only: -0.00261; 95% CI [-0.00647, +0.00125].
- S07 repeated shocks, unchanged recovery: -0.00112; 95% CI [-0.00364, +0.00140].
- S11 stable baseline reorganization, unchanged recovery: -0.00252; 95% CI [-0.00513, +0.00009].
- S14 mixed moving-baseline + heteroskedastic-noise null: -0.00066; 95% CI [-0.00399, +0.00266].

True recovery-law changes also passed:

- S05 slowing: mean change +0.07786; 95% CI [+0.07585, +0.07986].
- S06 strengthening: mean change -0.11836; 95% CI [-0.12074, -0.11597].
- S08 history erosion: median event-index/recovery-coefficient Spearman rho = +1.0; positive in 100% of replications.
- S09 history strengthening: median rho = -1.0; negative in 100% of replications.

Competing-event and reorganization controls passed:

- S10 overlapping shock: 100% of the targeted pre-recovery second-shock episodes were classified as INTERRUPTED_BY_NEW_PERTURBATION.
- S11 estimated stable baseline shift: median absolute recovered shift = 3.0057 for true shift 3.0.

## 4. Non-normal transient control

Synthetic 2D stable matrix:
- spectral radius: 0.92;
- initial norm: 1.0;
- maximum norm: 1.6093;
- eventual norm after 80 steps: 0.00581.

Disposition: transient amplification occurred despite asymptotic stability and eventual decay.

This control supports retaining (A_{transient}) separately from failed recoverability.

## 5. Measurement-artifact control

Injected long zero-fill and missing-data segments were detected:
- zero-run detected: YES;
- missing fraction: 0.03;
- required disposition: artifact/refusal before scientific recovery classification.

PASS.

## 6. What this result licenses

It licenses only the following next step:

> Apply K1 as the candidate causal baseline operator to **outcome-blind real-data preprocessing and input-geometry qualification**, while preserving a real-data refusal path.

It does not license:
- a real event threshold;
- a recovery threshold;
- a normal/abnormal classifier;
- history dependence in the real grid;
- chi/Χ/Χ_arc interpretation;
- an operational tool;
- a paper claim.

## 7. Real-data gate

Before opening real recovery outcomes:

1. freeze source stream identity and quality-indicator mapping;
2. remove/flag invalid and zero-filled source states according to source QI;
3. preserve native mHz frequency-deviation units;
4. freeze sampling/gap rules;
5. remove duplicate/reference-stream pseudo-replication;
6. create development and untouched holdout partitions without recovery-outcome inspection;
7. qualify the event-coordinate/input geometry from training inputs only;
8. freeze event entry, return-set, sustain, overlap and horizon rules;
9. only then expose recovery outcomes.

## 8. Caveat

The synthetic model is deliberately controlled and simpler than a real grid. Passing it demonstrates that the machinery can distinguish the prespecified known truths; it does not show that the same decomposition is identifiable in field data.

A real-data refusal remains a fully valid outcome.
