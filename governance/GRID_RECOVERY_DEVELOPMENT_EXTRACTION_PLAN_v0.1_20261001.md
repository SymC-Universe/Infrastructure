# GRID_RECOVERY_DEVELOPMENT_EXTRACTION_PLAN_v0.1_20261001.md

**Status:** FROZEN BEFORE FIRST REAL RECOVERY OUTCOME EXTRACTION  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01

## 1. Authorized data

Only primary development campaigns and only the 25–60% QI-valid segment.

Still sealed:
- 60–80% internal validation;
- 80–100% temporal holdout;
- within-grid replication holdouts;
- ERCOT;
- Gran Canaria;
- Russia.

Apply the frozen 1001-s partition embargo to event-entry eligibility.

## 2. Frozen input geometry

Entry:
- K1 101-s past-only rolling median baseline;
- q_entry=0.999;
- component-wise D_OR entry;
- 1-s source-unit-correct derivative;
- retain D_A and D_R separately;
- retain AMP_ONLY / RATE_ONLY / BOTH morphology.

## 3. Frozen recovery geometry

Return:
- q_return=0.975;
- amplitude relative to either pre-event B0 or local B(t);
- 5-s rolling RMS of the 1-s derivative;
- 20 continuous seconds for sustained return.

Follow-up:
- maximum 900 s;
- reporting horizons 60, 300, 900 s.

## 4. Competing event

A new D_OR exceedance run beginning before completed SUSTAINED_RETURN_PRE is:

REPERTURBATION_OR_REEXCITATION.

No claim of independence is made.

Primary event endpoint is the earliest of:
1. completed 20-s sustained pre-event return;
2. re-perturbation/re-excitation;
3. 900-s horizon;
4. data/quality censoring.

## 5. Raw event input fields

For every event record:

- grid_id;
- station_dir;
- event_id;
- t_entry;
- entry morphology;
- entry D_A;
- entry D_R;
- entry physical residual in mHz;
- entry 1-s rate in mHz/s;
- entry-run duration;
- peak D_A during entry run;
- peak D_R during entry run;
- amplitude excess area during entry run;
- rate excess area during entry run.

No scalar perturbation-severity score is created.

## 6. Causal pre-event state fields

Record using only information available at/before t_entry:

- B0_mHz;
- baseline velocity over 60 s, normalized by s_r;
- baseline velocity over 300 s, normalized by s_r;
- 300-s residual robust-noise ratio relative to frozen s_r;
- 60-s pre-event RMS 1-s rate relative to frozen s_v;
- UTC hour;
- elapsed seconds since start of campaign-development segment.

These are native current-state comparators, not recovery outcomes.

## 7. Raw recovery outcomes

### Pre-event reference
- T_first_pre_s;
- T_sustain_pre_s;
- sustained_pre_by_60;
- sustained_pre_by_300;
- sustained_pre_by_900.

### Local moving-baseline reference
- T_first_local_s;
- T_sustain_local_s;
- sustained_local_by_60;
- sustained_local_by_300;
- sustained_local_by_900.

### Competing event
- T_reexcitation_s;
- reexcited_by_60;
- reexcited_by_300;
- reexcited_by_900.

### Primary cause
One of:
- SUSTAINED_RETURN_PRE;
- REPERTURBATION_OR_REEXCITATION;
- HORIZON_CENSOR;
- DATA_QUALITY_CENSOR.

## 8. Continuous trajectory summaries

Up to the primary endpoint record:

- max pre-event-normalized displacement;
- max local-baseline-normalized displacement;
- max absolute 1-s rate;
- max 5-s rate energy;
- integrated pre-event displacement burden;
- time outside pre-event return set;
- baseline migration at primary endpoint;
- local-minus-pre reference divergence at endpoint.

At 60/300/900 s, where not contaminated by an earlier competing event, record:
- residual pre-event displacement;
- residual local displacement;
- baseline migration.

A later new event invalidates horizon-specific residual attribution for the earlier event.

## 9. History bookkeeping fields

The first raw table may record only causal bookkeeping, not history-effect conclusions:

- ordinal event number within grid campaign;
- time since previous event entry;
- whether current event began before prior sustained pre-event return;
- previous event primary cause;
- previous event T_sustain_pre if observed.

Do not yet fit or select a history model.

## 10. Predeclared candidate history objects for the next gate

Following the market Q040 structure but translated to grid-native quantities, preserve for later qualification:

N_j: prior event count.

L_A,j and L_R,j: cumulative prior amplitude- and rate-input burdens.

U_j: cumulative prior time outside the pre-event return set.

F_j: prior incomplete-recovery burden built only from already-observed prior outcomes.

C_j: recent event-clustering/re-excitation burden.

No "damage" or "fatigue" label is attached.

The primary history model will be frozen only after the raw development table is quality-audited and before validation data are opened.

## 11. First real-development outputs allowed

Allowed:
- event counts;
- cause counts;
- raw recovery-time distributions;
- burden distributions;
- baseline-migration distributions;
- data-quality/refusal counts;
- current-state descriptive summaries.

Not yet allowed:
- normal/abnormal classifier;
- history-effect promotion;
- threshold retuning;
- validation or holdout scoring;
- chi/Χ/Χ_arc claims;
- early-warning claims.

## 12. Failure conditions

If the qualified event/return rules yield:
- too few independent events;
- overwhelming re-excitation making recovery unidentifiable;
- unstable return definitions in real development data;
- QI/gap contamination;
- or incoherent reference behavior,

return the relevant refusal rather than redefining recovery from the observed outcome.
