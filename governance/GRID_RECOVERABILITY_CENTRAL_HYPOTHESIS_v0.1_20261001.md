# GRID_RECOVERABILITY_CENTRAL_HYPOTHESIS_v0.1_20261001.md

**Status:** CENTRAL P0-N / P0-D SCIENTIFIC LANE — NOT PREREGISTERED  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Program authority:** SymC GOM v1.0  
**Parent:** WORKING_INVESTIGATION.md

## 1. Why this lane is central

The clean-sheet grid investigation will center on **recoverability under perturbation**, not on spike amplitude, fixed chi thresholds, or retrospective labels of damage.

The transferable scientific lesson from the market Q040 program is structural:

- perturbation magnitude is not recovery ability;
- first return is not sustained recovery;
- slower recovery is not automatically reduced basin resilience;
- baseline migration is not automatically recovery failure;
- transient amplification is not automatically instability;
- repeated perturbations may cause deterioration, no change, or adaptation/strengthening;
- return of one observable does not prove restoration of the original system architecture.

The grid program will test these distinctions directly using power-system-native observables and models.

## 2. Central hypothesis

### GRH — Grid Recoverability Hypothesis

Conditional on the pre-perturbation native grid state, perturbation class/magnitude/direction, operating context, measurement quality, and identifiable forcing, ordinary recoverable disturbances occupy a reproducible family of finite-time response-and-recovery trajectories.

If grid recoverability changes, at least one of the following may change beyond the matched normal envelope:

1. resistance to displacement;
2. transient amplification;
3. time to first reclaim;
4. time to sustained reclaim;
5. probability of sustained recovery within a frozen horizon;
6. integrated displacement/recovery burden;
7. residual offset at a frozen horizon;
8. baseline/set-point migration;
9. modal/vector reorganization;
10. history dependence under repeated perturbations;
11. cross-timescale propagation of altered recovery behavior.

The hypothesis is **not** that all of these must worsen together.

A valid result may show:
- normal recovery;
- delayed but normal recovery;
- interrupted recovery caused by a new perturbation;
- stable reorganization;
- deteriorating recoverability;
- strengthening/adaptation;
- transition/failure;
- or non-identifiability/refusal.

## 3. Claim ladder

The investigation separates four scientific levels before any tool-level claim.

### G-R0 — trajectory heterogeneity
Matched grid perturbations exhibit measurably different finite-time recovery trajectories.

This is descriptive and does not establish changed recoverability.

### G-R1 — state/history dependence
After conditioning on current native grid state, event magnitude/class, operating conditions, baseline motion, noise, forcing, and measurement quality, prior perturbation/recovery history adds out-of-sample information about the current recovery trajectory.

This is the direct analogue of the market Q040 within-scale history question.

### G-R2 — recoverability change
The probability/distribution of finite-time sustained recovery changes under matched perturbations in a way not explained by current state, perturbation size, baseline migration, or measurement artifacts.

This is the key scientific hypothesis.

### G-R3 — architecture reorganization
Changes in recovery are associated with a separately qualified reorganization of modal/vector or broader grid organization.

This may involve Χ and, only if independently earned, Χ_arc. G-R2 does not imply G-R3.

### G-R4 — prospective discrimination/tool claim
A frozen recovery-state method distinguishes ordinary perturbations with ordinary recovery from abnormal/deteriorating/reorganized recovery on untouched events, with incremental value over strong native comparators.

No tool claim is allowed before G-R0 through G-R3 are adjudicated as applicable.

## 4. Native state first

At each admitted scale S, begin from a native state:

Z_S(t).

Candidate ingredients depend on dataset capability and may include:
- frequency deviation;
- ROCOF with correct units;
- voltage magnitude/angle where available;
- active/reactive power where available;
- PMU phasors;
- frequency coherence across synchronized locations;
- oscillatory spectral content;
- native modal estimates;
- topology/dispatch/load/generation context where available;
- IBR/GFM/GFL composition where available;
- data-quality and observability state.

No chi, Χ, or Χ_arc term is mandatory.

Scalar chi_i may enter only when a local/modal dynamical reduction independently earns it.

## 5. Baseline and reference state

The user's market interpretation transfers directly as a testable grid principle:

> Baseline should be scale-local and causal, then compared hierarchically across slower scales; recovery failure must be distinguished from baseline migration.

For grid scale S define a causal local reference state:

B_S^Z(t).

Recovery toward the pre-event state B_S^Z(t0) is measured separately from subsequent baseline motion.

Required distinctions:
- recovery toward stable pre-event baseline;
- incomplete recovery with stable baseline;
- moving baseline with unchanged recovery law;
- changed recovery law with little baseline movement;
- stable migration/reorganization to a new operating state;
- multiscale coordinated baseline migration.

The baseline estimator may not be selected using recovery outcomes.

## 6. Perturbation definition

A grid perturbation is not defined by one historical threshold.

For each dataset/scale qualify a metric family D_S from outcome-blind criteria.

Possible native event coordinates include:
- standardized frequency/voltage displacement;
- correctly scaled ROCOF;
- multichannel distance from local state;
- spectral/modal displacement;
- state-space/subspace distance;
- event labels from trusted operator/public event records.

The decisive analysis must freeze:
- event entry;
- event magnitude;
- event direction/type where meaningful;
- return set;
- sustain rule;
- timeout/censoring horizon;
- minimum event separation;
- overlap/merge rule;
- interruption by a new event.

No old 0.60, 0.70, 0.80, Δchi, ROC, or lead-time threshold is inherited.

## 7. Recovery vector

For event j at scale S define a candidate recovery vector:

R_(S,j) =
(
T_first,
T_sustain,
P_sustain(H),
A_transient,
I_burden,
D_dwell,
E_H,
Delta_B,
Delta_X,
H_hist
).

Where:

- T_first: time to first reclaim of the return set;
- T_sustain: time to sustained reclaim;
- P_sustain(H): sustained-return probability within frozen horizon H;
- A_transient: maximum transient amplification relative to entry displacement;
- I_burden: integrated normalized displacement over the recovery interval;
- D_dwell: recovered-side dwell after reclaim;
- E_H: residual displacement at horizon H;
- Delta_B: baseline migration/change;
- Delta_X: change in admitted modal/vector organization, only where Χ is independently licensed;
- H_hist: frozen perturbation-history summary.

No universal one-number recovery score is assumed.

## 8. Event states

After perturbation entry, the primary event-state machine should distinguish at least:

1. OUTSIDE_RETURN_SET;
2. FIRST_RECLAIM;
3. SUSTAINED_RECOVERY;
4. INTERRUPTED_BY_NEW_PERTURBATION;
5. STABLE_REORGANIZATION;
6. INCOMPLETE_RECOVERY_AT_HORIZON;
7. TRANSITION_OR_FAILURE;
8. REFUSED_OR_NON_IDENTIFIABLE.

A large spike may still be NORMAL_RECOVERABLE if its conditional recovery trajectory lies inside the matched normal envelope.

A small spike may be ABNORMAL if recovery is persistently delayed, repeatedly fails to sustain, carries abnormal residual burden, or is followed by qualified reorganization after controlling for context.

## 9. Repeated-perturbation hypothesis

For matched perturbations, test whether cumulative perturbation/recovery history changes future recoverability.

Competing outcomes are symmetric:

- erosion/fatigue;
- no material history effect;
- adaptation/strengthening;
- state-dependent mixed effects.

Do not hard-code the old intuition that repeated shocks must weaken the system.

Candidate history variables may include:
- number of prior qualifying disturbances;
- cumulative displacement burden;
- cumulative incomplete-recovery burden;
- time since prior disturbance;
- prior recovery duration;
- prior residual offset;
- direction/type sequence;
- modal/vector reorganization history where admitted.

History must add value beyond current-state sufficiency to support G-R1/G-R2.

## 10. Normal versus abnormal perturbation

The eventual tool is not primarily a spike detector.

It is a conditional **recovery classifier**.

A perturbation is provisionally "ordinary recoverable" when, relative to matched state/event context:
- transient amplification is within the learned normal envelope;
- first and sustained reclaim occur within calibrated distributions;
- recovery burden is not anomalous;
- residual displacement is compatible with baseline behavior;
- any baseline shift is stable/expected rather than unexplained drift;
- admitted modal/vector structure returns or reorganizes within a qualified normal family;
- recent perturbation history does not indicate abnormal degradation.

A perturbation is provisionally "abnormal recovery" when one or more recovery dimensions lie outside the frozen conditional envelope and the deviation is not explained by:
- event magnitude/type;
- operating point;
- forcing;
- measurement artifact;
- missingness/staleness;
- ordinary baseline migration;
- known control action;
- new perturbation interruption.

The first tool should return structured states, not only NORMAL/ABNORMAL.

## 11. Native comparator floor

Any recovery method must be compared with the strongest fair grid-native alternatives for the same task, including as applicable:
- frequency nadir and ROCOF;
- settling/recovery time;
- voltage recovery indices;
- modal damping estimates;
- oscillation alarms;
- event/change-point detection;
- dynamic/transient security metrics;
- critical-slowing indicators;
- trajectory-based voltage/frequency stability indices;
- resilience/event restoration metrics;
- non-normal/transient-growth measures;
- PMU multivariate/subspace methods.

Incremental value, not re-labeling, is the promotion criterion.

## 12. Literature support and collision

Relevant power-system literature already supports:
- multidimensional stability taxonomies;
- early-warning indicators and their limitations;
- PMU event/oscillation detection;
- trajectory-based monitoring;
- resilience/recovery metrics;
- modal estimation;
- non-normal transient amplification.

Representative sources already recovered in the literature atlas include:
- Sanchez, Hines & Danforth 2012, DOI 10.1109/TSG.2012.2213848;
- Ghanavati et al., DOI 10.1109/TCSI.2014.2332246 and 10.1109/TPWRS.2015.2412115;
- Xie, Chen & Kumar 2014, DOI 10.1109/TPWRS.2014.2316476;
- Carrington, Dobson & Wang, DOI 10.1109/TPWRS.2021.3074898;
- Stankovic et al. 2023, DOI 10.1109/TPWRS.2022.3212688;
- Dobson 2023, DOI 10.1109/TPWRS.2023.3300125;
- Almomani, Sarwar & Ajjarapu 2026, DOI 10.48550/arXiv.2604.07051.

Therefore novelty cannot be "grids recover after perturbations" or "slower recovery may precede instability."

The residual target is the conditional, repeated-perturbation, multiscale relationship between:
- current native state;
- perturbation;
- finite-time recovery trajectory;
- recovery history;
- modal/vector organization;
- baseline migration/reorganization;
- and prospective discrimination of ordinary versus abnormal recovery.

## 13. Data strategy

### KIT/OSF frequency corpus
Useful for:
- ordinary frequency perturbation distributions;
- corrected ROCOF;
- finite-time return trajectories;
- recovery burden;
- repeated-event history;
- multiscale local baseline behavior;
- cross-grid transport of frequency-only recovery laws.

Limitations:
- no direct bus-state participation factors;
- no full network topology;
- no voltage/current phasor architecture for most streams;
- no direct impedance or controller-state observables.

### Rich PMU/model datasets
Required for:
- modal/vector recovery;
- spatial mode shape recovery;
- network reorganization;
- topology/control-conditioned analysis;
- stronger Χ/Χ_arc tests.

Frequency-only and rich-PMU lanes must remain separate evidence classes.

## 14. Immediate scientific sequence

1. Complete the recovery-specific literature pass and nearest-prior-art collision map.
2. Reconstruct clean raw frequency data with correct units and quality flags.
3. Build the outcome-blind local baseline/event/return machinery.
4. Establish the normal conditional recovery envelope on development data.
5. Test repeated-perturbation history against current-state-only native baselines.
6. Add modal/vector recovery only where the data independently support it.
7. Stress with synthetic known truths for:
   - large normal spike + fast normal recovery;
   - small spike + slow/incomplete recovery;
   - moving baseline with unchanged recovery law;
   - transient non-normal amplification with eventual normal recovery;
   - new-event interruption;
   - stable reorganization;
   - history-driven erosion;
   - history-driven strengthening;
   - measurement artifacts.
8. Freeze the qualified method.
9. Evaluate untouched real events.
10. Only after the scientific result, decide whether a practical grid recovery tool is warranted and what outputs it may legitimately emit.

## 15. Failure conditions for the central hypothesis

The hypothesis is weakened or refused if:
- recovery trajectories add no information beyond standard event magnitude/state descriptors;
- apparent recovery changes vanish after correcting baseline motion/noise/forcing;
- perturbation history adds no out-of-sample value beyond current state;
- derived abnormal-recovery labels fail transport across grids/events;
- richer Χ/Χ_arc representations add no value over native modal/subspace methods;
- the data cannot identify recovery separately from moving operating conditions;
- or prospective discrimination fails on untouched events.

A negative result is a completed scientific result, not a failed project.
