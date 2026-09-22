# SymC chi <-> capital-Chi grid transport G1: synchronized Continental Europe freeze

**Date:** 2026-09-22  
**Status:** P0-D PRE-RESULT TRANSPORT FREEZE  
**Promotion effect:** NONE  
**Purpose:** transport the already calibrated joint-information protocol into a real engineered network using a source-native local damping coordinate and explicitly synchronized external system state.

## Scientific question

For a focal location inside one synchronous power area, does contemporaneous modal state measured elsewhere in the same synchronous area improve held-out prediction of the focal local damping coordinate at the next non-overlapping 300 s window beyond:

1. focal scalar chi plus focal forcing; and
2. the richer focal modal state itself?

This is an information/sufficiency test. It is not a claim that remote measurements causally control the focal site.

## Why the old global aggregate is not the test object

The preserved 15-minute "global" stability table contains 63,154 bins but never more than three systems per bin:

- 1 system: 8,583 bins;
- 2 systems: 48,265 bins;
- 3 systems: 6,306 bins.

Among the 100 previously preserved per-system event selections, 99 map to a 15-minute aggregate bin:

- 1 system: 23 event bins;
- 2 systems: 59 event bins;
- 3 systems: 17 event bins.

Therefore that table is not licensed as a whole-grid capital-Chi state. In one-system bins it collapses to local information, and in two/three-system bins it does not preserve which external systems contribute to the aggregate.

The whole-grid scalar route remains refused.

## Frozen empirical source

Google Drive source:

- title: `chi_dataset_300s.csv`
- Drive file ID: `1_StEQ5NV0DUnwvjpTEWd3IX_ccFTmmWy`
- stored size: 20,979,636 bytes
- modified: 2026-03-11T05:49:38.317Z
- parsed data rows: 103,549
- source columns:
  `station_code,file_path,freq_col,window_seconds,step_seconds,window_id,time_start,n_samples,max_abs_dfdt_mhzps,qi_nonzero_fraction,chi,sigma_mean,omega_mean,n_modes`
- `window_seconds = step_seconds = 300` for this analysis, so adjacent accepted windows do not overlap by construction.

No values from the historical GridCon manuscript are used as outcome thresholds.

## Pre-outcome source selection

The transport subset is selected by source structure and grid-domain eligibility, not by predictive performance:

`/content/drive/MyDrive/FrequencyData_extracted/sync01/SYNC01.csv`

It contains four co-recorded frequency streams:

1. `f50_DE_KA`
2. `f50_DE_OL`
3. `f50_PT`
4. `f50_TR`

All four belong to the Continental Europe synchronous system during the July-August 2019 observation interval. ENTSO-E defines a synchronous area as electrically tied systems operating at synchronized frequency, and official records place Germany and Portugal within Continental Europe and Türkiye in permanent synchronous operation with Continental Europe following the 2015 long-term agreement.

This four-stream source is therefore preferred over timestamp pooling across unrelated synchronous areas.

## Availability gate fixed before outcome analysis

Exact simultaneous accepted 300 s windows across all four streams:

`n = 458`

observation interval:

`2019-07-10 12:50:00` through `2019-08-07 15:35:00`.

For each focal stream, an eligible row at time `t` requires:

- all four streams accepted at exactly `t`;
- focal stream accepted at exactly `t + 5 min`.

Frozen eligible one-step counts:

- DE_KA: 196
- DE_OL: 219
- PT: 154
- TR: 454

All four focal sites are analyzed coequally. No site may be dropped because of its result.

## Representation hierarchy

### S: scalar-local model

Target:

`y_i(t) = chi_i(t + 5 min)`

Predictors:

- intercept;
- `chi_i(t)`;
- `log1p(max_abs_dfdt_mhzps_i(t))`.

This is the scalar sufficiency branch with forcing control.

### L: local-modal model

Add the native modal decomposition already used to construct the focal coordinate:

- `sigma_mean_i(t)`;
- `omega_mean_i(t)`.

Thus L asks whether the richer local mode contains useful information beyond scalar chi plus forcing.

### J: joint local + partial-system model

Add, separately for each of the other three synchronized streams:

- `chi_j(t)`;
- `sigma_mean_j(t)`;
- `omega_mean_j(t)`;
- `log1p(max_abs_dfdt_mhzps_j(t))`.

Remote stream identities are preserved. They are not averaged into a master scalar.

The J representation is explicitly:

`partial capital-Chi_grid(t)`

not a complete capital-Chi reconstruction. The data do not contain mode shapes, generator participation factors, line topology, inertia distribution or controller state.

## Estimator and split

For each focal site independently:

1. sort eligible observations by time;
2. first 70% = training block;
3. final 30% = untouched chronological test block;
4. standardize predictor columns using training-block mean and standard deviation only;
5. fit ordinary least squares with an intercept;
6. require full column rank for each fitted design;
7. no regularization or hyperparameter tuning;
8. no random shuffle split.

If a required design loses full column rank, that model/site is reported as `REFUSE_ILL_CONDITIONED`; no outcome-informed feature removal is permitted.

## Frozen metrics

For the final chronological test block report:

- persistence SSE, with `chi_hat(t+5)=chi(t)`;
- S scalar-local SSE;
- L local-modal SSE;
- J joint SSE;
- test R2 for S, L and J;
- `modal_increment = 1 - SSE_L / SSE_S`;
- `system_increment = 1 - SSE_J / SSE_L`;
- fraction of test rows with lower squared error under J than L.

## System-alignment null

The contextual block containing all three external streams is shifted as one object, preserving contemporaneous covariance among remote sites while breaking its alignment to the focal site.

Use deterministic nonzero circular shifts:

`k = 1..19`

applied separately inside the training and test blocks. The focal predictors and target remain unshifted.

For every shift, refit J and compute:

`null_system_increment = 1 - SSE_J_shifted / SSE_L`.

Exploratory alignment statistic:

`p_alignment = (1 + count(null_increment >= observed_system_increment)) / 20`.

The null is deliberately conservative with respect to temporal autocorrelation because small shifts are retained rather than excluded.

## Per-site outcome classes

- `PARTIAL_SYSTEM_CONTEXT_ADDS_BEYOND_LOCAL_MODAL`: system_increment > 0, J beats persistence, and p_alignment <= 0.10.
- `CONTEXT_INCREMENT_UNRESOLVED`: system_increment > 0 but the alignment screen is not cleared.
- `LOCAL_MODAL_SUFFICIENT_FOR_THIS_TASK`: system_increment <= 0 and L beats persistence.
- `BOTH_LOCAL_AND_JOINT_INADEQUATE`: neither L nor J beats persistence.
- `REFUSE_ILL_CONDITIONED`: required design loses full rank.

Scalar adequacy is reported separately from the system-context label using `modal_increment`; no universal scalar-adequacy threshold is imposed in this P0-D transport.

## Cross-site disposition

- same material context label at all four sites -> retain that common label;
- otherwise -> `SITE_DEPENDENT / REPRESENTATION_DEPENDENT`.

No favorable site may stand in for the four-site conclusion.

## Native-method ceiling

S, L and J are ordinary linear state predictors. J is therefore a standard multivariate autoregressive-style comparator using the same information that the partial capital-Chi interpretation receives.

A positive J increment can support only:

> synchronized external grid state contains conditional predictive information about focal next-window damping beyond the tested local representation.

It cannot establish a uniquely SymC predictive algorithm. If standard multivariate modeling fully contains the effect, the correct program-level classification is `STANDARD_TOOLKIT_SUBSUMES`.

## Falsifiers / stop rules

The real-data transport fails or narrows if:

- J adds no held-out information over L;
- any gain vanishes under the alignment null;
- conclusions differ materially by focal site;
- persistence outperforms both fitted models;
- full-rank requirements fail;
- the source-native modal representation proves numerically unstable;
- the observed effect is fully described by ordinary multivariate autoregression.

No topology, mode-shape, or causal-embedding claim may be inferred from this dataset.

## Next gate

Execute exactly this frozen four-site challenge on the bound 300 s source. Preserve every site result. Only after adjudication may a controlled grid simulation be used to test topology/participation causally.
