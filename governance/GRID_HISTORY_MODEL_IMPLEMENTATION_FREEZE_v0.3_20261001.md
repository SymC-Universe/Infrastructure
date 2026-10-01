# GRID_HISTORY_MODEL_IMPLEMENTATION_FREEZE_v0.3_20261001.md

**Status:** IMPLEMENTATION FROZEN BEFORE SYNTHETIC AND REAL HISTORY FITTING  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01

This document makes the v0.1 plan plus v0.2 correction executable.

## 1. Episode-derived pre-event controls

Before fitting, derive from the episode table using only earlier episode start/end times:

- recent_episode_count_900: number of earlier episode starts in (t-900 s, t);
- elapsed_grid_fraction: ordinal time from first to last development episode within each grid, scaled to [0,1];
- B0_z: B0_mhz standardized within grid using training-fold mean/SD only;
- hour_sin = sin(2*pi*UTC_hour/24);
- hour_cos = cos(2*pi*UTC_hour/24);
- halfhour_distance_norm = distance_to_halfhour_s / 900;
- near_halfhour_10s;
- near_halfhour_30s;
- GB_x_near10 and GB_x_near30.

## 2. M0 numeric feature block

- log1p(first_entry_D_A)
- log1p(first_entry_D_R)
- pre_noise_ratio_300
- pre_rate_rms60_norm
- baseline_velocity_60_norm
- baseline_velocity_300_norm
- B0_z
- log1p(prior_episode_count)
- log1p(max(time_since_prev_episode_end_s,0)+1)
- recent_episode_count_900
- elapsed_grid_fraction
- hour_sin
- hour_cos
- halfhour_distance_norm
- near_halfhour_10s
- near_halfhour_30s
- GB_x_near10
- GB_x_near30

Categorical M0:
- first_entry_morphology
- grid_id

## 3. M2 primary burden block

Add to M0:

- log1p(prior_cum_amp_input)
- log1p(prior_cum_rate_input)
- log1p(prior_cum_outside_pre_return_s)

No incomplete-recovery flag enters M2.

## 4. M3 incomplete-recovery alternative

Add to M0:

- log1p(prior_incomplete_episode_count)
- prior_mean_outside = prior_cum_outside_pre_return_s / max(prior_episode_count,1)
- previous episode final-cause categorical indicator

M3 is an alternative explanation, not a second primary success route.

## 5. Outcomes

For H = 60, 300, 900 s:

Y_H=1 if T_sustain_pre_episode_s <= H.

Y_H=0 if no sustained pre-event return by H and the episode remains observable to H.

If DATA_QUALITY_CENSOR occurs before H without prior sustained return, the row is omitted for that H.

Episode chains may contain re-excitation; this does not censor Y_H.

## 6. Forward folds

Within each grid, order episodes by t_start and assign equal-count quartiles 1–4.

Fold A:
- train quartiles 1–2
- test quartile 3

Fold B:
- train quartiles 1–3
- test quartile 4

Quartile boundaries are never chosen from outcome values.

## 7. Preprocessing and learner

For each fold/H/model separately:

- training-only median imputation for numeric missingness;
- training-only standardization of numeric features;
- one-hot categorical encoding with unknown categories ignored;
- L2 logistic regression;
- C=1.0;
- solver=lbfgs;
- max_iter=2000;
- no class reweighting by outcome.

Grid sample weights:
each grid receives equal total training weight within the fold/H fit.

The same preprocessing and learner are used for M0, M2 and M3.

## 8. Primary Brier calculation

For each test fold and H:

1. calculate ordinary Brier loss per eligible episode;
2. average within each grid;
3. average the seven grid means equally.

Across horizons:
average H=60,300,900 equally.

Across forward folds:
average Fold A and Fold B equally.

Primary delta:
DeltaB = Brier(M0) - Brier(M2).

Positive favors M2.

## 9. Admission robustness

Aggregate horizon-specific deltas to one delta for each grid x fold cell.

Require:
- overall mean DeltaB > 0;
- Fold A mean >0;
- Fold B mean >0;
- all seven leave-one-grid-out means >0;
- >=5/7 grid means >=0.

Hierarchical paired bootstrap:
- 2,000 bootstrap replicates;
- seed = 20261001;
- sample seven grids with replacement;
- for each sampled grid, sample the two forward-fold cells with replacement;
- average sampled paired DeltaB values.

Require 2.5th percentile > 0.

## 10. Synthetic qualification

Synthetic qualification uses 50 independent seeds per S-H1 through S-H8.

The exact same feature construction, folds, learner, grid weighting and admission function are used.

A synthetic world's truth may alter only the data-generating recovery law, not the fitted-model/admission rules.

## 11. Direction diagnostic

If M2 is admitted, direction is determined by a frozen burden contrast:

- take test episodes;
- hold M0 features fixed;
- set all three M2 burden features to their training-fold 25th percentiles and predict;
- set them to their 75th percentiles and predict;
- average probability difference macro across grids/H/folds.

Higher-burden minus lower-burden recovery probability:
- <0: erosion direction;
- >0: adaptation direction.

For S-H8 or real data, if at least two grids show each sign with absolute grid-level contrast >=0.01, disposition is mixed/direction-dependent rather than universal.

## 12. M3 alternative adjudication

If M2 is admitted, fit M3 under the same folds.

Incomplete-recovery explanation is favored if:
- M3 primary macro Brier improvement over M0 is >= M2 improvement;
- and M2 added to M3 does not produce a positive 95% bootstrap lower bound.

No real validation data are used in this adjudication.
