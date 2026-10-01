# GRID_EVENT_GEOMETRY_QUALIFICATION_v0.2_RESULT_20261001.md

**Status:** INPUT GEOMETRY QUALIFIED / RECOVERY OUTCOMES STILL SEALED  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent delta:** governance/GRID_INPUT_GEOMETRY_v0.1_FAILURE_AND_v0.2_DELTA_20261001.md

## 1. Qualified representation

The first real-data perturbation representation is **not a scalar severity coordinate**.

Retain the native two-component input vector:

[
P_t=(D_A(t),D_R(t))
]

where:

- (D_A=|z_r|): robust-standardized displacement from the causal K1 baseline;
- (D_R=|z_v|): robust-standardized correctly scaled rate component in mHz/s.

Episode entry uses the component-wise union rule:

[
E(t)=
[D_A(t)>T_A]
lor
[D_R(t)>T_R].
]

This bookkeeping trigger is called D_OR.

No chi/Χ/Χ_arc object is involved.

## 2. Fresh confirmation design

The revised rule was not confirmed on the 0–10% slice that motivated it.

Fresh confirmation used QI-valid time from 10–15% of each primary development campaign.

The original 0–10% geometry calibration remained the sole source for:
- K1 robust component scales;
- T_A(q);
- T_R(q).

No recovery trajectory was calculated.

## 3. Frozen q test

Fresh confirmation results:

| q | Minimum runs across 7 grids | Median runs | Finite all grids | Gap/QI artifact free | Pass |
|---:|---:|---:|---|---|---|
| 0.995 | 40 | 270 | yes | yes | yes |
| 0.999 | 12 | 88 | yes | yes | **yes** |
| 0.9995 | 5 | 60 | yes | yes | no |
| 0.9999 | 2 | 35 | yes | yes | no |

The frozen rule selects the **highest passing q**.

Therefore:

[
oxed{q_{mathrm{entry}}=0.999}
]

for separate component thresholds.

## 4. Grid-specific calibration thresholds at q=0.999

These are robust standardized input thresholds learned from each development campaign's calibration slice, not universal physical constants.

| Grid | T_A | T_R |
|---|---:|---:|
| BALTIC | 3.7824 | 3.3882 |
| CONTINENTAL_EUROPE | 3.8567 | 3.4490 |
| GREAT_BRITAIN | 6.0656 | 5.3638 |
| ICELAND | 3.0333 | 4.3024 |
| MALLORCA | 3.4794 | 5.5662 |
| NORDIC | 5.2936 | 3.3503 |
| WESTERN_INTERCONNECTION | 3.4705 | 3.7879 |

These values show directly why a universal standardized scalar threshold was not promoted.

## 5. Fresh confirmation event morphology at q=0.999

| Grid | Runs | AMP_ONLY | RATE_ONLY | BOTH |
|---|---:|---:|---:|---:|
| BALTIC | 220 | 12.3% | 87.7% | 0.0% |
| CONTINENTAL_EUROPE | 469 | 9.8% | 90.2% | 0.0% |
| GREAT_BRITAIN | 88 | 26.1% | 73.9% | 0.0% |
| ICELAND | 51 | 41.2% | 58.8% | 0.0% |
| MALLORCA | 3,320 | 49.4% | 50.1% | 0.5% |
| NORDIC | 12 | 0.0% | 100.0% | 0.0% |
| WESTERN_INTERCONNECTION | 84 | 29.8% | 67.9% | 2.4% |

The component mix is clearly system-dependent.

This is evidence for preserving perturbation morphology as a vector covariate, not evidence that one component is the universal causal driver.

## 6. What is now licensed

Licensed for RECOVERY_MODEL_DEVELOPMENT only:

- K1 causal local baseline;
- source-unit-correct mHz/s derivative;
- training-only robust component scales;
- grid-calibrated q=0.999 component thresholds;
- D_OR episode entry;
- event severity vector ((D_A,D_R));
- entry morphology AMP_ONLY / RATE_ONLY / BOTH.

Not licensed:

- normal versus abnormal recovery;
- return threshold;
- sustained-return duration;
- recovery horizon;
- history effect;
- scalar severity;
- early warning;
- chi/Χ/Χ_arc interpretation;
- operational tool.

## 7. External transport implication

The q=0.999 **calibration rule** is the transferable object.

The numerical T_A/T_R values above are not assumed to transfer unchanged across grids.

Before external-grid recovery outcomes are opened, the protocol must prespecify whether the primary transport question is:

1. zero-shot transfer of development-derived standardized thresholds; or
2. outcome-blind local input calibration followed by recovery-outcome transport.

Both may be tested, but they are different claims.

## 8. Next gate

Qualify, without opening real recovery outcomes:

- return-set geometry;
- pre-event versus moving-baseline reference frames;
- sustained-return rule;
- competing re-perturbation rule;
- finite recovery horizon.

Use synthetic known truths plus input-only event timing/state geometry from the 15–60% development segment.

Only after those rules are frozen may real recovery trajectories be exposed.
