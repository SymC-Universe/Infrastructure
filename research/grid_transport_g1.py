from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

EXPECTED_SHA256 = "f0136df899c26706843b45cf186fb09b7422f934f4407e61e82d3a2156fa7b93"
SOURCE_SUFFIX = "/sync01/SYNC01.csv"
STREAMS = ["f50_DE_KA", "f50_DE_OL", "f50_PT", "f50_TR"]
NULL_SHIFTS = list(range(1, 20))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fit_ols(xtr, ytr, xte):
    mu = xtr.mean(axis=0)
    sd = xtr.std(axis=0)
    if np.any(~np.isfinite(mu)) or np.any(~np.isfinite(sd)) or np.any(sd <= 0):
        return None
    a = np.column_stack([(xtr - mu) / sd, np.ones(len(xtr))])
    b = np.column_stack([(xte - mu) / sd, np.ones(len(xte))])
    if np.linalg.matrix_rank(a) != a.shape[1]:
        return None
    beta = np.linalg.lstsq(a, ytr, rcond=None)[0]
    return b @ beta


def sse(y, p):
    return float(np.sum((y - p) ** 2))


def r2(y, p):
    den = float(np.sum((y - y.mean()) ** 2))
    return float(1 - sse(y, p) / den) if den > 0 else float("nan")


def records_for(df, focal):
    keyed = {(r.freq_col, r.time_start): r for r in df.itertuples(index=False)}
    common = sorted(set.intersection(*[
        set(df.loc[df.freq_col.eq(s), "time_start"]) for s in STREAMS
    ]))
    remote = [s for s in STREAMS if s != focal]
    out = []
    for t in common:
        tn = t + pd.Timedelta(minutes=5)
        target = keyed.get((focal, tn))
        if target is None:
            continue
        local = keyed[(focal, t)]
        sf = [float(local.chi), float(np.log1p(local.max_abs_dfdt_mhzps))]
        lf = sf + [float(local.sigma_mean), float(local.omega_mean)]
        cf = []
        for s in remote:
            z = keyed[(s, t)]
            cf += [float(z.chi), float(np.log1p(z.max_abs_dfdt_mhzps)),
                   float(z.sigma_mean), float(z.omega_mean)]
        out.append((t, float(target.chi), float(local.chi), sf, lf, cf))
    return out, common


def evaluate(df, focal):
    rec, common = records_for(df, focal)
    n = len(rec)
    nt = int(math.floor(0.70 * n))
    y = np.array([x[1] for x in rec])
    persistence = np.array([x[2] for x in rec])
    xs = np.array([x[3] for x in rec])
    xl = np.array([x[4] for x in rec])
    xc = np.array([x[5] for x in rec])
    xj = np.column_stack([xl, xc])

    if nt < 30 or n - nt < 20:
        return {"focal": focal, "status": "REFUSE_INSUFFICIENT_SAMPLE",
                "n_eligible": n, "n_train": nt, "n_test": n - nt}

    ps = fit_ols(xs[:nt], y[:nt], xs[nt:])
    pl = fit_ols(xl[:nt], y[:nt], xl[nt:])
    pj = fit_ols(xj[:nt], y[:nt], xj[nt:])
    if ps is None or pl is None or pj is None:
        return {"focal": focal, "status": "REFUSE_ILL_CONDITIONED",
                "n_eligible": n, "n_train": nt, "n_test": n - nt}

    yt = y[nt:]
    sp = sse(yt, persistence[nt:])
    ss = sse(yt, ps)
    sl = sse(yt, pl)
    sj = sse(yt, pj)
    modal = 1 - sl / ss
    system = 1 - sj / sl
    wins = float(np.mean((yt - pj) ** 2 < (yt - pl) ** 2))

    null = []
    for k in NULL_SHIFTS:
        jtr = np.column_stack([xl[:nt], np.roll(xc[:nt], k, axis=0)])
        jte = np.column_stack([xl[nt:], np.roll(xc[nt:], k, axis=0)])
        pn = fit_ols(jtr, y[:nt], jte)
        if pn is None:
            return {"focal": focal, "status": "REFUSE_ILL_CONDITIONED",
                    "n_eligible": n, "n_train": nt, "n_test": n - nt}
        null.append(1 - sse(yt, pn) / sl)
    null = np.asarray(null)
    p_align = float((1 + np.sum(null >= system)) / 20)

    if sl >= sp and sj >= sp:
        label = "BOTH_LOCAL_AND_JOINT_INADEQUATE"
    elif system > 0 and sj < sp and p_align <= 0.10:
        label = "PARTIAL_SYSTEM_CONTEXT_ADDS_BEYOND_LOCAL_MODAL"
    elif system > 0:
        label = "CONTEXT_INCREMENT_UNRESOLVED"
    elif system <= 0 and sl < sp:
        label = "LOCAL_MODAL_SUFFICIENT_FOR_THIS_TASK"
    else:
        label = "BOTH_LOCAL_AND_JOINT_INADEQUATE"

    return {
        "focal": focal, "status": "COMPLETE",
        "remote_streams": [s for s in STREAMS if s != focal],
        "n_all_four_context_times": len(common), "n_eligible": n,
        "n_train": nt, "n_test": n - nt,
        "train_start": str(rec[0][0]), "train_end": str(rec[nt-1][0]),
        "test_start": str(rec[nt][0]), "test_end": str(rec[-1][0]),
        "persistence_sse": sp, "scalar_local_sse": ss,
        "local_modal_sse": sl, "joint_sse": sj,
        "scalar_local_r2": r2(yt, ps), "local_modal_r2": r2(yt, pl),
        "joint_r2": r2(yt, pj), "modal_increment": float(modal),
        "system_increment": float(system),
        "joint_vs_local_win_fraction": wins,
        "alignment_null_n": 19,
        "alignment_null_median_increment": float(np.median(null)),
        "alignment_null_max_increment": float(np.max(null)),
        "alignment_null_min_increment": float(np.min(null)),
        "p_alignment": p_align,
        "scalar_relation": ("LOCAL_MODAL_IMPROVES_SCALAR_BRANCH"
                            if modal > 0 else
                            "SCALAR_BRANCH_NOT_WORSE_THAN_LOCAL_MODAL"),
        "context_label": label,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", default="grid_transport_g1_result.json")
    args = ap.parse_args()
    src = Path(args.input)
    obs = sha256_file(src)
    if obs != EXPECTED_SHA256:
        raise SystemExit(f"source SHA mismatch: {obs}")
    df = pd.read_csv(src)
    if len(df) != 103549:
        raise SystemExit(f"unexpected row count: {len(df)}")
    df["time_start"] = pd.to_datetime(df["time_start"])
    sub = df[df.file_path.astype(str).str.endswith(SOURCE_SUFFIX)].copy()
    if sorted(sub.freq_col.unique()) != sorted(STREAMS):
        raise SystemExit("unexpected SYNC01 stream set")
    if not sub.window_seconds.eq(300).all() or not sub.step_seconds.eq(300).all():
        raise SystemExit("non-300/300 windows found")

    results = [evaluate(sub, s) for s in STREAMS]
    complete = all(x["status"] == "COMPLETE" for x in results)
    labels = [x.get("context_label", x["status"]) for x in results]
    cross = labels[0] if complete and len(set(labels)) == 1 else (
        "SITE_DEPENDENT / REPRESENTATION_DEPENDENT" if complete else "REFUSAL_PRESENT"
    )
    out = {
        "schema": "SYMC_CHI_CAPITALCHI_GRID_TRANSPORT_G1_V01",
        "date": "2026-09-22",
        "status": "PASS" if complete else "REFUSE",
        "epistemic_class": "P0_D_REAL_GRID_TRANSPORT",
        "promotion_effect": "NONE",
        "freeze_commit_initial": "d3c199bc95ec0795d8b188cf071418909ad97c69",
        "freeze_commit_source_hash_bound": "aa826fa69fef70cdd91e4fc2c2afd311ca787ee6",
        "source": {"title": src.name, "sha256": obs, "rows": len(df),
                   "sync01_rows": len(sub), "source_suffix": SOURCE_SUFFIX,
                   "streams": STREAMS},
        "per_focal_results": results,
        "cross_site_disposition": cross,
        "native_method_disposition":
            "STANDARD_TOOLKIT_EQUIVALENCE_BY_CONSTRUCTION: J is an ordinary multivariate linear state predictor; any context increment is an information-structure result, not a uniquely SymC algorithmic advantage.",
        "claim_ceiling":
            "Real-data transport within one co-recorded Continental Europe source. Context is partial capital-Chi only; topology, participation, inertia, controller state, causal embedding, and whole-grid capital-Chi are not established."
    }
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
