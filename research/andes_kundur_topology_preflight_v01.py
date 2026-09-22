from __future__ import annotations

import json
from pathlib import Path

import andes
import pandas as pd

OUT = Path("research/andes_kundur_topology_preflight_v01.json")


def records(model):
    if model is None:
        return []
    df = model.as_df()
    # Keep only source/model data. This preflight does not run PFlow, EIG, or TDS.
    return json.loads(df.to_json(orient="records"))


def subset(rows, keys):
    out = []
    for row in rows:
        out.append({k: row.get(k) for k in keys if k in row})
    return out


def main():
    case = andes.get_case("kundur/kundur_full.xlsx")
    ss = andes.load(case, no_output=True)

    bus = records(ss.Bus)
    line = records(ss.Line)
    genrou = records(ss.GENROU)
    toggle = records(ss.Toggle)
    area = records(getattr(ss, "Area", None))

    bus_small = subset(bus, ["idx", "name", "area", "zone", "u"])
    line_small = subset(
        line,
        ["idx", "name", "bus1", "bus2", "r", "x", "b1", "b2", "Sn", "u"],
    )
    gen_small = subset(
        genrou,
        ["idx", "name", "bus", "M", "D", "Sn", "u"],
    )
    toggle_small = subset(
        toggle,
        ["idx", "name", "model", "dev", "t", "u"],
    )
    area_small = subset(area, ["idx", "name", "u"])

    bus_area = {str(r.get("idx")): r.get("area") for r in bus_small}
    cross_area_lines = []
    for r in line_small:
        a1 = bus_area.get(str(r.get("bus1")))
        a2 = bus_area.get(str(r.get("bus2")))
        if a1 is not None and a2 is not None and str(a1) != str(a2):
            cross_area_lines.append({
                **r,
                "area1": a1,
                "area2": a2,
            })

    out = {
        "schema": "SYMC_ANDES_KUNDUR_TOPOLOGY_PREFLIGHT_V01",
        "status": "PASS",
        "andes_version": getattr(andes, "__version__", None),
        "case": str(case),
        "outcome_routines_run": {
            "PFlow": False,
            "EIG": False,
            "TDS": False,
        },
        "counts": {
            "bus": len(bus_small),
            "line": len(line_small),
            "genrou": len(gen_small),
            "toggle": len(toggle_small),
            "area": len(area_small),
            "cross_area_lines": len(cross_area_lines),
        },
        "areas": area_small,
        "buses": bus_small,
        "lines": line_small,
        "genrou": gen_small,
        "toggles": toggle_small,
        "cross_area_lines_by_bus_area": cross_area_lines,
        "selection_rule_for_next_gate": (
            "Choose intervention only from native cross-area/tie structure and source "
            "disturbance definitions. Do not inspect PFlow, eigenvalues, damping, or TDS "
            "responses before freezing the intervention."
        ),
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
