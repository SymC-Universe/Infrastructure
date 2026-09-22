# SymC χ <-> Χ cross-domain experimental expansion: E3 execution state

**Date:** 2026-09-21  
**Status:** P0-D / KNOWN-TRUTH CALIBRATION + SOURCE QUALIFICATION  
**E1:** independent experiment sketches preserved before targeted literature collision  
**E2:** literature collision completed before outcome-bearing SymC analyses

## Mechanical known-truth gate

Execution was performed remotely in the Biomedical repository because that branch already has qualified GitHub Actions execution.

Source:
- repository: `SymC-Universe/Biomedical`
- branch: `gri-chi-bio-conglomerate-v01-20260918`
- workflow: `GRI joint-information mechanical known-truth`
- run: `35652521161`
- head SHA: `e1745988dc4388371f7e740528c0c52f51900356`
- artifact: `GRI_JOINT_INFORMATION_MECHANICAL_KNOWN_TRUTH_V01`
- artifact ID: `10663076712`
- artifact digest: `sha256:5913bb45eed2d3f72c5d2b8bd6df74a65f5c793ec705ff981fb7dc7ab1afa8f1`

Frozen synthetic construction:
- four coupled oscillators;
- isolated focal `χ = 0.15` identical across chain, ring and star topologies;
- local-only predictor receives focal displacement, focal velocity and isolated χ;
- system-augmented predictor adds embedding/coupling state;
- target is focal displacement 1.0 s ahead;
- held-out test split fixed before execution;
- predeclared gate: `Delta R2 >= 0.10`.

Result:

```text
R2_local_only         = 0.5250507702547642
R2_local_plus_system  = 0.7246126021364034
Delta_R2              = 0.19956183188163923
gate                  = PASS
```

Per topology:

```text
chain: local 0.71516 -> joint 0.78221 ; Delta = 0.06705
ring:  local 0.67482 -> joint 0.99356 ; Delta = 0.31875
star:  local -0.54183 -> joint 0.09163 ; Delta = 0.63345
```

### Interpretation ceiling

This is a synthetic known-truth implementation result only. The simulated equations already contain coupling, so the result does not independently discover that system architecture conditions local dynamics.

What it establishes is narrower and important: the proposed held-out comparison can detect conditional system information when it is known to exist, while preserving identical isolated local χ across architectures.

The topology-specific variation is also informative for future Function/Limit mapping: system information was useful in all three topologies but the amount of recoverable increment varied materially. No universality is inferred.

## Brain-stimulation source qualification

A high-value open known-truth source has been identified:

`grabuffo/State_Dependent_Brain_Stimulation`, source commit `84afcf934c3798b2a40dc8da22d0840e60a4b0f9`.

The repository states that it reproduces Rabuffo et al., *Pre-stimulus Brain States Predict and Control Variability in Stimulation Responses*. It links an open OSF source dataset and contains:

- simultaneous SEEG and high-density EEG from 36 patients;
- single-pulse intracortical stimulation;
- pre/post metric extraction across spatial radii;
- out-of-sample prediction notebooks;
- prospective closed-loop state-conditioned stimulation analysis;
- radius-dependence analyses;
- network-dependent predictability analyses;
- surrogate and carryover controls.

### Qualification disposition

`OPEN_KNOWN_TRUTH_TESTBED_CANDIDATE = YES`

`SCALAR_CHI_LICENSED = NO`

`SOURCE_NATIVE_PREDICTIVE_EFFECT_ALREADY_ESTABLISHED = YES`

`SYMC_INCREMENTAL_VALUE = NOT_TESTED`

The first SymC use of this source must therefore be a **reproduction/qualification pass**, not a novelty claim. The source-native metrics and source train/test logic are the baseline to beat or equal. A local χ branch is optional and must be separately licensed from native local oscillatory dynamics rather than created from a generic EEG feature.

## Brain source-native qualification result

The source-native qualification completed successfully in `SymC-Universe/Biomedical`:

- workflow run: `35667947330`;
- head SHA: `7c882cb9221975ae1f1e9b8bb6b4e360ee89a01d`;
- artifact: `GRI_BRAIN_SOURCE_NATIVE_QUALIFICATION_V01`;
- artifact ID: `10669554940`;
- artifact digest: `sha256:0a8ae286220c825381851bb08a71c5246944902ff3bfb17460d63d00c9886610`;
- exact upstream commit and all six predeclared blob identities matched.

The source-native Salience-to-Salience derived table contains 318 sessions from 36 subjects. Without filtering away negative cross-validation results:

```text
mean OOS R2                      = -0.3903626243
median OOS R2                    = -0.1325688419
fraction OOS R2 > 0              = 0.3993710692
mean source null R2              = -0.7746289351
median source null R2            = -0.3791251880
fraction OOS R2 > source null    = 0.7798742138
mean (OOS R2 - source null)      = 0.3842663108
median (OOS R2 - source null)    = 0.3094923758
```

This is an important qualification nuance. The source contains real state-dependent predictive structure relative to its own null, but the unfiltered session-average OOS R2 is negative. Therefore the SymC calibration must **not** inherit the source notebook's later `R2 >= 0` filter as if it were a prospective population-level success criterion. The complete session distribution is the correct starting point for our same-question challenge.

The supplied spatial-radius summary is likewise nontrivial:

```text
5 mm -> 5 mm:     mean correlation = 0.574519
                  mean in-sample R2 = 0.388414
                  mean CV R2        = -2.010048

100 mm -> 100 mm: mean correlation = 0.540243
                  mean in-sample R2 = 0.334969
                  mean CV R2        = -0.390363
```

This supports scale/radius dependence of the measured relation, not a simple claim that the broadest scale is always more predictive.

## Current cross-domain state

```text
mechanical_known_truth_protocol = PASS
mechanical_physical_bench = NOT_YET_RUN
brain_open_data = SOURCE_NATIVE_QUALIFICATION_PASS
SCC25_joint_chi_Chi = DESIGN_PACKET_EXISTS_NOT_FROZEN
grid_transport = LITERATURE_COLLISION_COMPLETE_NOT_RUN
cross_domain_generality = NOT_ESTABLISHED
```

## Next exact actions

1. qualify the brain source's derived files and source-native train/test logic sufficiently to reproduce one published state-dependent prediction result;
2. write the SCC25 joint-meaning prediction freeze without choosing a biological scalar unless scalar admission succeeds;
3. convert the mechanical known-truth into a direct benchtop protocol after the calibration logic is stable;
4. map the existing grid data against the same conditional-information outcome classes.

No cross-domain universality claim is permitted at this stage.


## Update: brain source-native known-truth closed

The source-native brain network-dependence reproduction has now passed in the Biomedical execution environment.

- run: `35671352024`
- head SHA: `885791c4799090c00f7776da4575cbf1f6f0eb6d`
- artifact: `SYMC_BRAIN_STATE_KNOWN_TRUTH_SOURCE_REPRODUCTION_V01`
- artifact ID: `10671395900`
- artifact digest: `sha256:116649a13cef743964857a8902c4c983995ba69d75e0d69ff645b853fb2379e4`

The result reproduces a strong ordered network gradient for SEEG but no monotonic gradient for hdEEG. This is a useful Function/Limit result: system/network organization matters in the source-native evidence, but the form of that dependence is measurement/representation dependent.

No local scalar chi was constructed or inferred from this result.

## Update: SCC25 local-scalar branch narrowed

A separate SCC25 G2 eigenstructure diagnostic has now refused scalar chi for the current R1/A3 weekly representation.

- r=2: no complex-conjugate eigenvalue pair in any required fit;
- r=3: point-fit complex pair exists, but pair existence fails one required representation/refit and the derived continuous-time ratio is branch dependent;
- cross-rank disposition: `REPRESENTATION_DEPENDENT_SCALAR_ELIGIBILITY`.

Therefore the active SCC25 joint-meaning experiment uses a native local/modal discrete-time object `z_local`, not a manufactured scalar chi. This is a direct example of the GOM rule that a joint chi<->Chi investigation continues even when one scalar reduction refuses.

## Updated execution state

```text
mechanical_known_truth_protocol = PASS
brain_source_native_known_truth = PASS
brain_measurement_dependence = OBSERVED_SEEG_VS_HDEEG
SCC25_scalar_chi_current_representation = REFUSED
SCC25_local_modal_object = ADMITTED_FOR_JOINT_DESIGN
SCC25_joint_chi_Chi_outcome_run = NOT_YET_FROZEN
grid_transport = LITERATURE_COLLISION_COMPLETE_NOT_RUN
cross_domain_generality = NOT_ESTABLISHED
```

The next scientific gate is the prospective SCC25 joint-design freeze. No outcome-bearing SCC25 joint computation should begin until its broader-system representation, held-out task and incremental-value/refusal rules are fixed.
