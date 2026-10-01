# GRID_RETURN_AND_SUSTAIN_QUALIFICATION_PLAN_v0.1_20261001.md

**Status:** FROZEN INPUT/SYNTHETIC QUALIFICATION PLAN — REAL RECOVERY OUTCOMES SEALED  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** governance/GRID_EVENT_GEOMETRY_QUALIFICATION_v0.2_RESULT_20261001.md

## 1. Purpose

Qualify the definitions required to distinguish:

- first reclaim;
- sustained return toward the pre-perturbation state;
- local stabilization around a moving/new baseline;
- re-perturbation/re-excitation before sustained return;
- incomplete recovery at finite reporting horizons.

This stage may use:
- synthetic known truths;
- input-only state occupancy/dwell statistics.

It may not inspect event-specific real recovery outcomes.

## 2. Additional firewall

Use QI-valid time:

- 0–10%: input-geometry calibration;
- 10–15%: event-geometry confirmation;
- 15–20%: return-set/sustain qualification;
- 20–60%: RECOVERY_MODEL_DEVELOPMENT;
- 60–80%: INTERNAL_VALIDATION;
- 80–100%: TEMPORAL_HOLDOUT.

The 15–20% slice is not used to classify recovery after detected perturbations.

## 3. Two reference frames

For an event at time t0, store the pre-event causal baseline:

[
B_0=B(t_0^-).
]

### Pre-event return coordinate

[
A_{mathrm{pre}}(t)
=
|f(t)-B_0|/s_r.
]

This asks whether the measured frequency state returned toward the pre-event reference.

### Local stabilization coordinate

[
A_{mathrm{local}}(t)
=
|f(t)-B(t)|/s_r.
]

This asks whether the system is locally settled around the contemporaneous causal baseline.

Both use the same rate coordinate:

[
R(t)=|v_f(t)|/s_v.
]

A system may locally stabilize without returning to B0. That case is not automatically labeled damage or recovery.

## 4. Return-set candidates

Using the original METRIC_TRAIN portion only, estimate component quantiles at:

- q_return = 0.95
- q_return = 0.975
- q_return = 0.99

For each q define:

[
T_A^{ret}=Q_q[D_A]_{mathrm{train}},
qquad
T_R^{ret}=Q_q[D_R]_{mathrm{train}}.
]

Candidate local return set:

[
mathcal R_{mathrm{local}}
=
[A_{mathrm{local}}le T_A^{ret}]
land
[Rle T_R^{ret}].
]

Candidate pre-event return set replaces A_local with A_pre.

The event-entry threshold remains q_entry=0.999 and is not altered here.

## 5. Input-only return-set adequacy

Evaluate q_return on the 15–20% input-only slice using local coordinates only.

For each grid report:

- joint return-set occupancy;
- number of return-set dwell runs;
- median dwell duration;
- 25th / 75th / 95th percentile dwell duration.

A q_return candidate is eligible if every development grid satisfies:

1. occupancy >= 0.80;
2. occupancy <= 0.995;
3. median dwell >= 10 s;
4. 75th-percentile dwell >= 20 s.

Select the **lowest q_return** satisfying all four conditions across all grids.

If no candidate passes, return RETURN_SET_REFUSED.

The lower passing q is preferred because it is the stricter central-state definition.

## 6. Sustain candidates

Candidate continuous sustain durations:

- 10 s
- 20 s
- 30 s
- 60 s

A duration L is input-adequate if, for the selected return set:

- at least 25% of return-set dwell runs in every grid last >= L;
- median fraction across grids lasting >= L is at least 50%.

## 7. Synthetic oscillatory safeguard

Input adequacy alone cannot choose L because a trajectory can cross the return set during an oscillation and leave again.

Synthetic safeguard includes damped oscillatory responses with periods:

- 1 s
- 2 s
- 5 s
- 10 s

and envelopes chosen so the trajectory crosses the return set before true settling.

For each candidate L, a false sustained return occurs if the algorithm declares sustained recovery and the trajectory subsequently exits the return set because the original oscillation has not settled.

L is synthetically eligible only if false sustained return rate <= 1% across the frozen oscillatory suite.

Select the **shortest L** that passes both:
- input-only dwell adequacy;
- synthetic oscillatory safeguard.

If none pass, return SUSTAIN_RULE_REFUSED.

## 8. State definitions

After a perturbation entry:

### FIRST_RECLAIM_PRE
First entry into the pre-event return set.

### SUSTAINED_RETURN_PRE
First time the pre-event return condition remains continuously true for L seconds.

### FIRST_RECLAIM_LOCAL
First entry into the local return set.

### SUSTAINED_RETURN_LOCAL
First time the local return condition remains continuously true for L seconds.

### REPERTURBATION_OR_REEXCITATION
A new q_entry=0.999 D_OR run begins before SUSTAINED_RETURN_PRE.

No claim of statistical independence is attached to this state.

### INCOMPLETE_RECOVERY
No sustained pre-event return before the reporting/censoring horizon, subject to competing-event handling.

### POSSIBLE_REORGANIZATION
SUSTAINED_RETURN_LOCAL occurs without SUSTAINED_RETURN_PRE and the causal baseline has materially migrated.

No final reorganization label is licensed until baseline-migration thresholds are separately qualified.

## 9. Time-to-event inference

Primary recovery analysis will not depend on one arbitrary horizon.

Use a competing-event time-to-event formulation with:
- sustained pre-event return;
- re-perturbation/re-excitation.

Fixed reporting horizons:

- 60 s
- 300 s
- 900 s

Report cumulative incidence / sustained-return probability at each horizon.

These horizons span immediate, several-minute, and 15-minute recovery behavior and align with the program's multiscale objective.

A later tool may use different operational horizons only after separate validation.

## 10. Why a first crossing is insufficient

Operational literature already uses frequency-establishment and voltage-recovery indicators, and recovery-region theory explicitly distinguishes parameter states that return to the desired operating point from non-recovery.

The present program therefore requires sustained reclaim rather than a single threshold crossing.

## 11. Next gate

If q_return and L qualify:

1. freeze the return/sustain rules;
2. apply q_entry and return definitions to the 20–60% RECOVERY_MODEL_DEVELOPMENT segment;
3. open real development recovery trajectories for the first time;
4. estimate normal conditional recovery envelopes;
5. only then test current-state-only versus current-state-plus-history models.
