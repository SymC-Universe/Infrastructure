# GRID_RECOVERABILITY_PRIOR_ART_COLLISION_v0.1_20261001.md

**Status:** P0-N CLOSEST-PRIOR-ART COLLISION COMPLETE FOR FIRST RECOVERABILITY PASS  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** governance/GRID_RECOVERABILITY_CENTRAL_HYPOTHESIS_v0.1_20261001.md

## 1. Scope

This pass asks a narrow question:

> Has power-system research already implemented and validated the exact program of matched perturbations, causal moving-baseline separation, first-versus-sustained recovery, interruption by a new perturbation, repeated-event history dependence, and prospective classification of normal versus abnormal recoverability?

The answer from the first large literature pass is: **adjacent components are well occupied; the exact integrated protocol was not found.**

This is not yet a promoted novelty claim. It is the current collision result to be challenged by later searches and full-text review.

## 2. Occupied territory that the new study may not claim as novel

### Utility resilience and outage/restore curves
Power-system resilience curves, outage/restore statistics, recovery duration and event-level trend analysis are established.

Key sources:
- [Car20b] — utility-data extraction of resilience metrics;
- [Dob22] — event duration and utility-driven resilience metrics;
- [She18b] — statistical trend testing for power-system resilience;
- [Afs21] — large-scale data analytics of recovery from power failures;
- [Li23] — resilience-curve clustering/properties.

Implication: "measure recovery after disruption" is not novel.

### Sequential and repeated hazards
Sequential-hazard and repeated-event frameworks already show that incomplete restoration and antecedent condition can matter.

Key sources:
- [Kon18b];
- [Kon19];
- [Nas22].

Implication: "the previous event can matter" is not novel as a generic concept.

### Recovery coupling and outage-cluster structure
Recovery dependencies and interactions across outage clusters/networks are established.

Key sources:
- [Dan20];
- [Wu22];
- [Qi21].

Implication: network recovery is already known to be coupled and path dependent in some settings.

### PMU/event/frequency recovery tools
Operational and near-operational PMU tools already monitor frequency response, voltage recovery, oscillations and event signatures.

Key sources:
- [Pin23];
- [Pin24];
- [Bus25];
- [Liu21d];
- [Yam22];
- [Fol24].

Implication: a practical detector cannot claim novelty simply because it uses synchrophasors or classifies events.

### Moving operating conditions and modal drift
Grid dynamics are known to depend on operating point, topology and generation/load composition.

Key sources:
- [Kru23];
- [She19];
- [Wan17g];
- [Fol21d];
- [Ahm21];
- [Bis24b].

Implication: "the baseline/operating point moves" is not novel.

### Disturbance-recovery conditions
Formal computation of disturbance recovery conditions exists.

Key source:
- [Fis25].

Implication: "there is a boundary between recoverable and nonrecoverable disturbances" is not novel by itself.

## 3. Closest unresolved intersection

The first-pass search did not find a power-grid study that simultaneously does all of the following on matched real events:

1. estimates a causal moving reference state separately from recovery dynamics;
2. conditions on current state and disturbance magnitude/type;
3. distinguishes first reclaim from sustained reclaim;
4. treats a new disturbance before recovery as a competing/interruption event rather than ordinary censoring;
5. distinguishes stable operating-point migration/reorganization from degraded recovery;
6. tests whether prior perturbation/recovery history adds out-of-sample information about current recovery beyond current-state sufficiency;
7. allows deterioration, no history effect, and strengthening/adaptation symmetrically;
8. evaluates a frozen normal-recovery envelope on untouched events;
9. reports false alarms/misses relative to monitored time or event prevalence;
10. tests whether modal/vector organization adds incremental value beyond the strongest native recovery comparators.

That intersection is the present clean-sheet target.

## 4. Specific hypotheses that remain alive

### H1 — current-state sufficiency versus history
After conditioning on current native state, event size/type, operating context, baseline motion, noise and identifiable forcing, does prior perturbation/recovery history improve prediction of finite-time sustained recovery?

### H2 — baseline migration versus recovery-law change
Can a causal method distinguish a benign changing operating point from a changed local recovery law?

### H3 — first versus sustained reclaim
Does distinguishing first return from sustained recovery materially change event classification?

### H4 — interruption
Do re-perturbations before sustained recovery explain cases that would otherwise be mislabeled as failed recovery?

### H5 — recovery architecture
Where richer PMU/model data exist, does modal/vector reorganization provide incremental information beyond native scalar recovery metrics?

### H6 — practical discrimination
Can a frozen conditional recovery model distinguish ordinary from abnormal recovery prospectively and outperform same-outcome native baselines?

## 5. Falsifiers of the proposed scientific gap

The central recoverability contribution is weakened or eliminated if later full-text review finds a prior study that already performs the integrated protocol above with comparable field validation.

The scientific hypothesis is also weakened if:
- current state and event magnitude fully explain recovery;
- prior recovery history adds no out-of-sample value;
- baseline migration explains apparent deterioration;
- first-versus-sustained separation adds no information;
- the resulting classifier does not transport;
- native same-outcome comparators match or outperform the proposed architecture.

## 6. Comparator hierarchy frozen for planning

### Same-outcome comparators
- voltage/frequency recovery-duration and threshold methods;
- settling/establishment time;
- PMU voltage-recovery tools;
- disturbance recovery-condition methods;
- trajectory-based post-fault classifiers where endpoint matches.

### Event-context comparators
- event signature libraries;
- PMU anomaly/event classifiers;
- oscillation alarms and RMS-energy detectors;
- frequency nadir and ROCOF.

### Mechanism/state comparators
- native modal damping;
- state-matrix/modal tracking;
- operating-point covariates;
- nonstationary frequency models;
- non-normal/transient-growth metrics where appropriate.

### Service-restoration comparators
Outage/restore resilience curves remain important adjacent comparators but must not be treated as identical to short-timescale electrical-state recovery.

## 7. Current novelty posture

**NOT PROMOTED.**

Provisional gap statement only:

> The literature located so far contains the major component methods separately, but has not yet yielded a field-validated, matched-event, history-conditioned finite-time recoverability framework that separates moving baseline, sustained reclaim, re-perturbation, stable reorganization and recovery-law change, then prospectively distinguishes ordinary from abnormal recovery.

This statement remains subject to full-text collision review.
