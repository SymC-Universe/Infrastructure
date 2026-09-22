# SymC chi <-> capital-Chi grid transport G1: post-result audit

**Date:** 2026-09-22  
**Status:** P0-D POST-RESULT AUDIT  
**Promotion effect:** NONE  
**Freeze commits:** `d3c199bc95ec0795d8b188cf071418909ad97c69`, source-hash binding `aa826fa69fef70cdd91e4fc2c2afd311ca787ee6`  
**Source SHA-256:** `f0136df899c26706843b45cf186fb09b7422f934f4407e61e82d3a2156fa7b93`  
**Independent arithmetic check:** sklearn LinearRegression reproduces S/L/J test SSE values to < 3.3e-14 absolute difference.

## Result

All four predeclared focal sites completed without numerical refusal.

| Focal | n | modal increment L vs S | system increment J vs L | alignment p | frozen context label |
| --- | ---: | ---: | ---: | ---: | --- |
| DE_KA | 196 | +0.158733 | -0.197064 | 0.75 | LOCAL_MODAL_SUFFICIENT_FOR_THIS_TASK |
| DE_OL | 219 | +0.100764 | -0.301149 | 1.00 | LOCAL_MODAL_SUFFICIENT_FOR_THIS_TASK |
| PT | 154 | -0.090028 | -0.179331 | 0.60 | LOCAL_MODAL_SUFFICIENT_FOR_THIS_TASK |
| TR | 454 | +0.085104 | -0.135273 | 0.60 | LOCAL_MODAL_SUFFICIENT_FOR_THIS_TASK |

Cross-site disposition:

`LOCAL_MODAL_SUFFICIENT_FOR_THIS_TASK`

For this frozen 5-minute-ahead task, adding synchronized measurements from the other three Continental-Europe streams worsened held-out focal prediction at every site.

The broader contextual representation therefore does **not** earn an information increment here.

## Absolute predictive adequacy

The frozen label above is comparative, not a claim that the local fitted model is universally strong.

Local-modal test R2:

- DE_KA: -0.112843
- DE_OL: -0.353134
- PT: -0.194357
- TR: +0.170785

Thus three of four fitted local-modal models have negative R2 relative to the test-block mean. They nevertheless beat the frozen persistence baseline and outperform the joint contextual model, which is why the predeclared context label is local-modal sufficient *for this comparison*.

No stronger forecast-performance claim is allowed.

## Scalar chi versus richer local mode

The scalar/local-modal branch itself is not universal.

- DE_KA: local modal reduces scalar-model SSE by 15.9%.
- DE_OL: local modal reduces scalar-model SSE by 10.1%.
- TR: local modal reduces scalar-model SSE by 8.5%.
- PT: local modal increases scalar-model SSE by 9.0%.

Therefore scalar adequacy remains site/representation dependent. The result does not justify replacing local modal state with scalar chi everywhere.

## Capital-Chi consequence

This result is an important limit case for the joint architecture.

Mechanical known-truth calibration showed that broader embedding can add information when the governing equations contain a strong coupling effect. The brain known-truth source showed state/network dependence with measurement dependence. SCC25 showed direction- and representation-dependent local/system information.

In contrast, the present real-grid transport shows:

`synchronized external modal state does not automatically improve local chi prediction`

even when all sites are in one synchronous power area.

That is evidence against treating capital-Chi as a mandatory improvement over local coordinates.

It supports the stronger GOM interpretation that the investigation must determine **when** local reduction is sufficient and **when** embedded organization matters, rather than assuming the answer in advance.

## What this does not test

The dataset does not contain:

- line topology changes;
- generator participation factors;
- mode shapes;
- inertia distribution;
- controller states;
- known disturbance injection location;
- controlled interventions.

Therefore the result cannot falsify topology/participation effects established in native power-system theory and experiments. It falsifies only the tested claim that contemporaneous external modal summaries add held-out information at this horizon under this representation.

## Native-method disposition

`STANDARD_TOOLKIT_EQUIVALENCE_BY_CONSTRUCTION`

The joint predictor is ordinary multivariate linear state prediction. No SymC-specific algorithmic advantage is claimed.

## Next gate

Do not tune the empirical grid representation to rescue capital-Chi.

Proceed to the predeclared controlled network test, where topology/coupling and disturbance location are manipulated under known truth while focal local parameters can be held or matched.

A suitable native execution engine is ANDES, which supports time-domain simulation and eigenvalue analysis and ships standard power-system dynamic cases. The simulation must be frozen as a causal topology/participation test before opening intervention outcomes.
