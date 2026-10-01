# GRID_HISTORY_MODEL_QUALIFICATION_PLAN_v0.1_20261001.md

**Status:** FROZEN BEFORE REAL HISTORY-MODEL FITTING  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Validation / transport holdouts:** SEALED

## 1. Primary question

Does prior perturbation/recovery burden add out-of-sample information about finite-time sustained pre-event recovery after controlling for:

- current perturbation geometry;
- current native frequency state;
- baseline motion/noise;
- ordinary exposure/event count;
- recent event clustering;
- time-of-day and identifiable scheduled forcing;
- grid identity?

The primary comparison is M2 versus M0.

Coefficient sign alone cannot support history dependence.

## 2. Scientific unit

One **recovery episode** is one initiating perturbation plus all re-excitations before sustained pre-event return.

Trigger runs inside one recovery episode are not independent history observations.

Canonical development table:
GRID_RECOVERY_DEVELOPMENT_EPISODES_v01.csv
SHA-256:
0b32b5f5bbbd7a7fa0ea233c58ffee2e7ee5af9ab73e058284c5ef7cd842224c

## 3. Primary outcomes

For H in {60, 300, 900} seconds:

[
Y_H=1
]

if sustained pre-event return occurs by H seconds from episode initiation.

Otherwise:

[
Y_H=0
]

provided the episode remains observable through H.

If DATA_QUALITY_CENSOR occurs before H and no earlier sustained return occurred, that episode is excluded from the H-specific score.

Re-excitation inside an episode is not censoring; it is part of the observed recovery trajectory.

Returns after H do not retroactively change Y_H.

## 4. M0 current-state/native comparator

Continuous/current perturbation terms:
- log1p(first_entry_D_A);
- log1p(first_entry_D_R);
- entry morphology one-hot;
- pre_noise_ratio_300;
- pre_rate_rms60_norm;
- baseline_velocity_60_norm;
- baseline_velocity_300_norm;
- within-grid standardized B0_mhz.

Exposure/clustering controls:
- log1p(prior_episode_count);
- log1p(max(time_since_prev_episode_end_s,0)+1);
- number of prior episode starts in the previous 900 s;
- elapsed fraction through the 25–60% development segment.

Clock/forcing controls:
- sin/cos UTC hour;
- distance to nearest half-hour boundary scaled to [0,1];
- indicator within 10 s of a half-hour boundary;
- indicator within 30 s of a half-hour boundary;
- GB-specific 10-s and 30-s boundary interactions.

Structural control:
- grid identity one-hot.

Including episode count/time in M0 is intentional. M2 must improve beyond simple exposure/time accumulation.

## 5. M2 burden-history extension

M2 = M0 plus:

- log1p(prior_cum_amp_input);
- log1p(prior_cum_rate_input);
- log1p(prior_cum_outside_pre_return_s);
- log1p(prior_incomplete_episode_count).

These variables use only episodes completed before the current episode.

They are not named damage, fatigue, memory, or adaptation in the statistical object.

## 6. Secondary history blocks

M1 ordinal:
- M0 + prior_episode_count only as the focal history term.
Because prior_episode_count already enters M0 as a nuisance/exposure control, M1 is descriptive and not an alternative success route.

M3 incomplete-recovery alternative:
- M0 + prior incomplete count + prior mean outside-return burden + previous episode final cause.
M3 is used to test whether any apparent M2 signal is specifically explained by unresolved/incomplete prior recovery.

No M4 flexible memory kernel is opened in this cycle.

## 7. Learner

Primary learner:
L2-regularized logistic regression with training-only preprocessing.

For each H:
- continuous variables median-imputed from training only;
- continuous variables standardized from training only;
- categorical variables one-hot encoded from training only;
- L2 logistic regression, C=1.0, max_iter=2000;
- no outcome-dependent hyperparameter tuning.

Same learner and preprocessing are used for M0 and M2.

A flexible nonlinear adversarial comparator may be added later, but cannot rescue a failed primary M2 test.

## 8. Grid weighting

Training sample weights are chosen so each grid contributes equal total weight within each training fold.

Primary scoring is macro:
1. compute Brier score within each grid;
2. average equally across grids;
3. average equally across H={60,300,900}.

Mallorca therefore cannot dominate the primary score by event count.

## 9. Forward-development evaluation

The 25–60% development episodes in each grid are ordered chronologically and divided into four equal-count blocks.

Two rolling forward folds:

- Fold A: train blocks 1–2; test block 3.
- Fold B: train blocks 1–3; test block 4.

No future episode enters training for an earlier test block.

The primary development score is the mean macro Brier score across both folds and all three horizons.

## 10. Primary M2 admission rule

Define:

[
Delta B =
Brier(M0)-Brier(M2).
]

Positive ΔB favors history.

M2 can receive DEVELOPMENT_SUPPORT only if all conditions hold:

1. mean macro ΔB > 0;
2. ΔB > 0 separately in Fold A and Fold B;
3. leave-one-grid-out macro ΔB remains >0 for all seven leave-one-grid-out aggregations;
4. at least 5 of 7 grids have nonnegative grid-level macro ΔB;
5. a paired hierarchical bootstrap over grid × forward-fold cells gives a two-sided 95% interval for mean ΔB whose lower bound is >0;
6. the history block also passes the synthetic known-truth gate below.

Failure of any item prevents history promotion.

No minimum arbitrary Brier magnitude is imposed beyond positive robust incremental information.

## 11. Direction classification

Only after M2 admission:

- erosion-direction if larger frozen history burden is associated with lower predicted recovery probability across the prespecified burden contrast;
- adaptation-direction if larger burden is associated with higher recovery probability;
- mixed/direction-dependent if the direction changes materially by grid or burden component.

Direction is secondary to predictive admission.

No fatigue label is used.

## 12. Synthetic known-truth gate

Before fitting real development outcomes, the exact pipeline must pass:

### S-H1 current-state sufficient
Recovery depends on M0 only; synthetic history is correlated with time/event count but has no causal/predictive effect.
Required: M2 not admitted.

### S-H2 clustering confound
Frequent recent episodes slow recovery; M0 clustering terms explain it.
Required: M2 not admitted.

### S-H3 cumulative-burden erosion
Recovery probability decreases with prior cumulative burden beyond M0.
Required: M2 admitted; erosion direction.

### S-H4 adaptation/strengthening
Recovery probability increases with prior burden.
Required: M2 admitted; adaptation direction.

### S-H5 moving baseline / clock forcing
Recovery depends on baseline motion and scheduled clock forcing that are correlated with cumulative history.
Required: M2 not admitted when M0 forcing/state terms are present.

### S-H6 incomplete-recovery alternative
Only prior incomplete recovery drives the effect.
Required: M2 may improve, but M3 must identify incomplete recovery as the narrower explanation.

### S-H7 grid heterogeneity
One high-volume grid contains a history signal while six do not.
Required: macro/leave-one-grid rules prevent a program-wide history promotion.

### S-H8 opposite grid directions
Some grids erode and others adapt.
Required: no universal erosion/adaptation label; mixed disposition.

## 13. Synthetic gate success criterion

Across 50 independently seeded replications of each synthetic world:

- S-H1, S-H2, S-H5: false M2 admission <=5%;
- S-H3, S-H4: correct admission and direction >=90%;
- S-H6: incomplete-recovery alternative correctly identified >=90%;
- S-H7: no program-wide promotion >=95%;
- S-H8: mixed-direction disposition >=90%.

If these are not met, the estimator/promotion rule is revised prospectively before fitting real recovery outcomes.

## 14. Development-only dispositions

Allowed after real M0/M2 analysis:

- HISTORY_ADDS_EROSION_DIRECTION_P0D
- HISTORY_ADDS_ADAPTATION_DIRECTION_P0D
- HISTORY_ADDS_MIXED_OR_DIRECTION_DEPENDENT_P0D
- NATIVE_CURRENT_STATE_SUFFICIENT_P0D
- INCOMPLETE_RECOVERY_EXPLAINS_APPARENT_HISTORY_P0D
- CLUSTERING_EXPLAINS_APPARENT_HISTORY_P0D
- SCHEDULED_FORCING_EXPLAINS_APPARENT_HISTORY_P0D
- RECOVERY_NOT_IDENTIFIABLE
- INSUFFICIENT_EPISODES

No validation/transport claim is allowed from development.

## 15. Validation firewall

Only after a development disposition is frozen:
- open 60–80% internal validation;
- apply the unchanged pipeline once;
- then within-grid replication holdouts;
- then external grid transport holdouts.

Any method change after validation exposure invalidates that validation set for confirmation.
