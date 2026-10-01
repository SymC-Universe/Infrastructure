# GRID_INPUT_GEOMETRY_v0.1_FAILURE_AND_v0.2_DELTA_20261001.md

**Status:** v0.1 SCALAR ENTRY PROMOTION REFUSED / v0.2 INPUT-ONLY DELTA FROZEN  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Recovery outcomes opened:** NO

## 1. v0.1 result

All seven development grids produced finite K1 residual and correctly scaled mHz/s derivative coordinates.

Shrinkage-Mahalanobis covariance was numerically admissible in all seven grids:
- effective rank 2;
- condition numbers approximately 1.33–1.71.

Therefore the failure was not numerical degeneracy.

Under the frozen v0.1 sample-adequacy rule:
- D_A failed;
- D_MAX failed;
- D_E failed;
- D_M failed;
- D_R alone passed at q=0.995.

The mechanical v0.1 selector therefore returned D_R.

**That promotion is refused.**

## 2. Why D_R is refused despite passing the mechanical rule

The component structure is strongly grid-dependent.

At q=0.995:

- MALLORCA D_MAX entries were ~99.25% rate-only.
- ICELAND D_MAX entries were ~88.89% rate-only.
- BALTIC D_MAX entries were ~77.63% rate-only.
- GREAT_BRITAIN D_MAX entries were ~67.21% rate-only.
- CONTINENTAL_EUROPE was mixed (~38.60% displacement-only, ~60.56% rate-only).
- WESTERN_INTERCONNECTION was mixed (~26.39% displacement-only, ~73.61% rate-only).
- NORDIC surviving D_MAX entries were 100% displacement-only.

Thus a rate-only event trigger would erase a perturbation morphology that is present in at least one development grid.

The broader program explicitly requires scalar refusal when compression removes qualified structure. Therefore D_R cannot be promoted merely because it satisfies the event-count heuristic.

## 3. Why D_MAX / D_E / D_M failed the v0.1 adequacy gate

The combined-coordinate training tail is dominated by different native components in different grids.

This changes the scalar threshold itself:
- a heavy rate tail can set the joint threshold and suppress displacement events;
- a heavy displacement tail can set the joint threshold and suppress rate events.

Example:
NORDIC q=0.995:
- D_A threshold 4.22095; 4 eval runs;
- D_R threshold 2.94516; 27 eval runs;
- D_MAX threshold 4.22095; 4 eval runs.

Here D_MAX inherited the displacement-tail threshold and effectively discarded the rate-event sample.

MALLORCA shows the converse morphology: D_MAX entries were overwhelmingly rate-driven.

This is evidence against a single empirical-tail scalar threshold, not evidence that one component is universally privileged.

## 4. v0.2 representation

Preserve the native component vector:

[
P_t = (D_A(t), D_R(t))
=
(|z_r(t)|, |z_v(t)|).
]

Define separate training-only component thresholds:

[
T_A(q)=Q_q[D_A]_{mathrm{train}},
qquad
T_R(q)=Q_q[D_R]_{mathrm{train}}.
]

Candidate perturbation entry is the logical union:

[
E_q(t)
=
[D_A(t)>T_A(q)]
;lor;
[D_R(t)>T_R(q)].
]

This is denoted **D_OR** for bookkeeping only.

D_OR is not a new scalar state coordinate. It is a two-channel event-entry rule.

Every event retains:
- displacement severity D_A;
- rate severity D_R;
- entry attribution: AMP_ONLY, RATE_ONLY, BOTH.

## 5. Fresh confirmation firewall

The 0–10% geometry-calibration slice has already been inspected.

It may be used to fit T_A and T_R, but not to confirm v0.2.

Create a fresh input-only confirmation slice:
- 10–15% of QI=0 valid time = EVENT_GEOMETRY_CONFIRMATION.
- 15–60% = RECOVERY_MODEL_DEVELOPMENT.
- 60–80% = INTERNAL_VALIDATION.
- 80–100% = TEMPORAL_HOLDOUT.

No recovery outcomes are opened in the 10–15% slice.

## 6. v0.2 q grid and selection

Use the same frozen q grid:
- 0.995
- 0.999
- 0.9995
- 0.9999

Thresholds T_A and T_R are estimated from the original 0–10% geometry-calibration METRIC_TRAIN only.

Evaluate D_OR on the fresh 10–15% confirmation slice.

Choose the highest q satisfying across all seven development grids:

1. at least 10 D_OR exceedance runs per grid;
2. median at least 30 runs per grid;
3. finite component thresholds;
4. zero candidate entries created by QI-invalid / timestamp-gap crossings after the 101-second warmup;
5. event attribution remains recorded rather than collapsed.

If no q passes, return EVENT_GEOMETRY_REFUSED.

## 7. No balance requirement

The method does **not** require every grid to have the same AMP_ONLY / RATE_ONLY / BOTH fractions.

Different grids may genuinely have different perturbation morphology.

The scientific requirement is only that the representation does not erase either native component before the recovery question is asked.

## 8. Consequence for later recovery modeling

Recovery models must condition on at least:
- D_A at entry;
- D_R at entry;
- entry attribution;
- pre-event native state/noise context.

Perturbation magnitude is therefore vector-valued at the first real-data stage.

Any later scalar severity score requires a separate qualification.

## 9. v0.1 disposition

- K1 baseline: remains synthetic-qualified.
- Correct mHz/s derivative construction: retained.
- D_A and D_R native components: retained.
- D_R as sole event coordinate: REFUSED.
- D_MAX/D_E/D_M as universal scalar entry coordinates: not promoted.
- D_OR component-wise union: enters fresh input-only confirmation.
