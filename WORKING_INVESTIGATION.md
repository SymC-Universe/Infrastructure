# WORKING_INVESTIGATION.md

## Power Grid Revalidation / Native-Grid Reconstruction

**Status:** ACTIVE — P0-N PRIOR-ART / P0-D HISTORICAL CLAIM RECONSTRUCTION  
**Date opened:** 2026-10-01  
**Authoritative research branch:** `grid-revalidation-2026-10-01`  
**Base branch:** `main`  
**Base commit:** `f088b2db1dd8aa6a2971396979b94c68bfc09f4d`  
**Repository:** `SymC-Universe/Infrastructure`  
**Program authority:** SymC General Operations Manual v1.0, 27 September 2026, plus the active Continuity Hardening Addendum and standing Conversation/Paper Formatting Guide.

## 1. Scientific question

Reconstruct the power-grid investigation from native power-system dynamics and the preserved historical SymC materials, determine claim-by-claim what is mathematically correct, empirically supported, overstated, contradicted, non-identifiable, or still worth testing, and only then define any new exploratory or confirmatory program.

The rebuild is not a defense of the 2025 manuscript. Historical material is a hypothesis/evidence inventory.

## 2. Rule of engagement

1. Truth over continuity. A historical claim may be narrowed, refused, or discarded without penalty.
2. Native-grid-first chain:
   native observables -> native dynamics -> measurable observables -> stability representation -> chi-related construction -> SymC interpretation.
3. Preserve the three construction levels:
   - scalar/local/modal coordinate: `χ_i` where a native mode supports it;
   - capital `Χ`: resolved modal/vector architecture;
   - `Χ_arc`: broader system/conglomerate organization and Stability Arc representation.
   No level may be silently substituted for another.
4. A local damping ratio does not automatically define a bus, region, or whole-grid scalar.
5. Mathematical identities, simulation results, retrospective field reconstructions, and prospective field evidence remain separate evidence classes.
6. No historical threshold, tier, lead time, recovery claim, or operational action is promoted without source-identifiable data, native comparators, frozen rules, independent evidence, and the applicable GOM/MFR-14 gates.
7. No operational control recommendation is inferred from a descriptive association.
8. Synthetic and field evidence remain explicitly separated.
9. Failures, anomalies, and outliers are retained and investigated for root cause and distributional status.
10. Forced oscillations, natural ringdowns, changing operating state, controller action, topology, loading, inertia, system strength, and measurement artifacts must be separated before interpreting modal damping.
11. Prior art is reconstructed before new hypothesis-directed confirmation. Existing power-system methods are the baseline, not a straw comparator.
12. Exploration remains open. Negative, narrowed, event-specific, non-identifiable, or refusal outcomes are valid results.

## 3. Canonical historical sources recovered

### Main manuscript
- `SymC_GridCon.tex`
- blob SHA: `445925df72cbf5b18bae7ea6c0c529a1b98ec2db`
- dated 20 December 2025

### Supplement
- `SymC_GridConSupmats.tex`
- blob SHA: `5cd0e54346592fc0ba3d519e88662bda2cf256b6`

### September 2026 correction/rebuild records
- `governance/GRID_GOM_V083_REBUILD_PLAN_20260921.md`
- `governance/GRID_CLAIM_RECONSTRUCTION_LEDGER_GOM_V083_20260921.md`
- `governance/GRID_HISTORICAL_SOURCE_AUDIT_GOM_V083_20260921.md`
- repository `README.md` correction notice

Those records remain scientifically useful but their cited GOM version is superseded by v1.0.

## 4. Historical claim families recovered

The prior source audit identifies these twelve top-level families:

1. whole-grid universal `χ ≈ 1` independent of topology/size/generation mix;
2. field/electron-scale inheritance of that boundary through transmission, generation, controls, and markets;
3. bus/regional `χ` as a direct substrate-degradation measure;
4. 60–100+ minute degradation/precursor lead time;
5. electron-scale precursor propagation into grid-scale failure;
6. cross-timescale `Δχ` divergence as a direct degradation signature;
7. baseline decay as irreversible damage;
8. `χ`-defined Tiers 0–4 as operational intervention states;
9. fixed threshold bands as operationally valid;
10. early intervention restores elasticity whereas late intervention leaves permanent damage;
11. dynamic redundancy maintains stability indefinitely;
12. standard monitoring misses information uniquely captured by SymC.

These are claim families only. The current audit must decompose them into atomic mathematical, empirical, mechanistic, predictive, and operational claims.

## 5. Initial defects/failures found on 2026-10-01

### F-001 — lifecycle duration inconsistency
The supplement describes a single **83-hour** lifecycle run while scheduling major events through `t = 8900 min`. Eighty-three hours is 4,980 minutes; 8,900 minutes is about 148.3 hours. The simulation description is internally inconsistent and cannot be treated as reproduced evidence until source code/output resolves the discrepancy.

### F-002 — bibliography/DOI misattribution
The main manuscript cites Weckesser/Rohden/Beck/Witthaut, “Early warning signals for critical transitions in power systems,” as *Physical Review E* 87, 042909 (2013), DOI `10.1103/PhysRevE.87.042909`. That DOI resolves to a different article, “Driving-induced bistability in coupled chaotic attractors,” by Agrawal/Prasad/Ramaswamy. The verified paper titled “Early warning signals for critical transitions in power systems” found in the present audit is Ren & Watts, *Electric Power Systems Research* 124 (2015) 173–180, DOI `10.1016/j.epsr.2015.03.009`. Full bibliography source matching is therefore mandatory.

### F-003 — field/simulation evidence boundary unclear
The supplement reports numerical performance claims including stable/event means, ROC thresholds, UK field snapshots/events, sensitivity, specificity, lead time, and permanent shifts, but the preserved text does not by itself establish raw-data identity, immutable windows, source lineage, code identity, or independent evaluation status. These values remain UNVERIFIED pending provenance reconstruction.

### F-004 — participation-factor formula requires native audit
The supplement defines participation using normalized squared right-eigenvector magnitudes. Conventional small-signal participation factors are ordinarily defined using both left and right eigenvectors. The historical expression may be a mode-shape/observability weighting rather than a true participation factor. Resolve from native theory before reuse.

### F-005 — sign and symbol convention requires audit
The supplement writes `χ_i = σ_i / |λ_i|`. This is correct only under a convention where `σ_i` is the positive decay rate in `λ_i = -σ_i ± jω_{d,i}`. If `σ_i = Re(λ_i)`, the sign must reverse. Every historical numerical value must be traced to the implemented convention.

### F-006 — scope promotion problem
The manuscript repeatedly promotes properties of an ideal second-order oscillator to whole-grid, cross-scale, mechanistic, predictive, and operational conclusions without separately establishing the required evidence at each level. Each promotion step must be audited independently.

## 6. Native facts already provisionally retained

These are starting points, not SymC validation:

- Small-signal electromechanical modes can be represented by complex eigenvalues and assigned native modal frequency/damping measures.
- Prony/ringdown methods can estimate modal frequency, damping, strength, and phase from suitable transient responses.
- PMUs/synchrophasor systems measure synchronized voltage/current phasors, frequency, and ROCOF; they do not directly measure an electron-scale state.
- Network stability is multidimensional and includes more than one stability class and more than one timescale.
- SCR is a context-dependent system-strength screening metric, especially for inverter interconnections; it is not a universal whole-grid stiffness scalar.
- N-1/planning-contingency practice is a reliability/security criterion, not a theorem of perfect elastic recovery.

Each item will receive primary/native citations in the prior-art ledger.

## 7. Claim-status vocabulary for this rebuild

- `NATIVE_ESTABLISHED`
- `MODEL_IDENTITY_SCOPE_LIMITED`
- `EMPIRICALLY_SUPPORTED_CURRENT_SCOPE`
- `RETROSPECTIVE_UNVERIFIED`
- `OVERSTATED`
- `CONTRADICTED_OR_WRONG`
- `HYPOTHESIS_TESTABLE`
- `NON_IDENTIFIABLE_WITH_CURRENT_DATA`
- `REFUSED`
- `PENDING_SOURCE_AUDIT`

No claim is promoted by confidence language alone.

## 8. Current work lanes

### Lane A — historical atomic claim ledger
Decompose main manuscript and supplement line-by-line into atomic claims, equations, numerical results, mechanistic interpretations, predictions, and operational prescriptions.

### Lane B — bibliography/source audit
Resolve every cited source by title/authors/venue/year/DOI and record whether it actually supports the attached claim.

### Lane C — native mathematical audit
Audit swing-equation reduction, modal damping, eigenvalue/EP language, participation factors, aperiodic-mode formulae, aggregation rules, inertia, SCR, inverter/GFM/VSM equations, thresholds, and dimensional/sign conventions.

### Lane D — evidence/provenance audit
Locate raw data, code, figure-generation sources, event identities/windows, simulation configurations, UK/FNET/PMU provenance, and immutable hashes. Do not treat reported summary statistics as reproduced evidence before this lane succeeds.

### Lane E — prior-art / comparator map
Reconstruct accepted modal monitoring, oscillation detection, transient/dynamic security, frequency stability, weak-grid/IBR metrics, early-warning literature, forced-oscillation methods, recovery/resilience measures, and current grid-forming controls.

### Lane F — residual SymC question
Only after A–E: determine whether `χ_i`, modal/vector `Χ`, and system organization `Χ_arc` add information, compression, prediction, or mechanistic clarity beyond native grid quantities.

## 9. Frozen prohibitions until evidence reconstruction

Do not use as priors or operational rules:
- universal `χ = 1` or `χ = 0.8–1.0` grid optimum;
- Tier 0–4 threshold bands;
- `|Δχ| > 0.2` for >5 min;
- `χ = 0.60` early-warning threshold;
- 60–100+ min or 127 min lead-time claims;
- 89% sensitivity / 98% specificity;
- irreversible 1–3% baseline-shift claim;
- electron-scale precursor mechanism;
- indefinite redundancy claim;
- universal inertia or SCR safe/yellow/red bands.

They remain historical hypotheses/results to audit, not inputs to independent evaluation.

## 10. Next exact actions

1. Complete atomic claim extraction from both TeX sources.
2. Complete bibliography identity/support audit for every cited source.
3. Search repository history and bundles for raw data/code/figure sources and reconstruct evidence identity.
4. Build the native prior-art matrix and direct comparators.
5. Adjudicate every historical atomic claim into the status vocabulary above.
6. Only then decide which residual questions enter P0-D exploration, P0-Q qualification, or are refused.
7. Before any P1 test, freeze estimators, preprocessing, windows, comparators, thresholds/endpoints, refusal rules, and independent evidence under GOM v1.0 and MFR-14.

## 11. Continuity state

**Authoritative lane:** this branch and this working record.  
**Current scientific state:** ACTIVE, no scientific gate requiring user action.  
**Last genuine advancement:** recovery of canonical historical sources, September rebuild records, and initial source/method defects; branch opened under GOM v1.0.  
**Next advancement criterion:** atomic claim ledger + source identity matrix materially expanded from historical family-level triage.
