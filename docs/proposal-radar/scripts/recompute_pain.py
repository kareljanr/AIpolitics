#!/usr/bin/env python3
"""Recompute all pain_* columns on proposals.csv from taxpayer_unit.csv."""
from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"


def load_unit() -> dict:
    p = DATA / "taxpayer_unit.csv"
    with p.open(encoding="utf-8", newline="") as f:
        return next(csv.DictReader(f))


def mid(a: str, b: str) -> float | None:
    try:
        x = float(a) if a not in ("", None) else None
        y = float(b) if b not in ("", None) else None
    except ValueError:
        return None
    if x is None and y is None:
        return None
    if x is None:
        return y
    if y is None:
        return x
    return (x + y) / 2.0


def main() -> int:
    u = load_unit()
    tax = float(u["tax_rounded_eur"])
    net = float(u["net_rounded_eur"])
    n_emp = float(u["employees_be"])
    work_min = float(u["work_minutes_year"])
    gross = float(u["gross_eur_year"])
    # € per work-minute (gross)
    eur_per_min = gross / work_min

    path = DATA / "proposals.csv"
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    extra = [
        "fiscal_is_saving",
        "pain_basis_eur",
        "pain_tax_fte",
        "pain_net_years",
        "pain_eur_per_employee",
        "pain_work_minutes",
        "pain_note",
    ]
    fields: list[str] = []
    seen: set[str] = set()
    for f in list(rows[0].keys()) + extra:
        if f not in seen:
            seen.add(f)
            fields.append(f)

    # order: after fiscal_confidence
    ordered: list[str] = []
    for f in fields:
        if f in extra:
            continue
        ordered.append(f)
        if f == "fiscal_confidence":
            ordered.extend(extra)
    for f in fields:
        if f not in ordered:
            ordered.append(f)
    fields = ordered

    for r in rows:
        sign = -1.0 if str(r.get("fiscal_is_saving", "")).lower() in ("yes", "1", "true") else 1.0
        m = mid(r.get("fiscal_static_min_eur", ""), r.get("fiscal_static_max_eur", ""))
        if m is None:
            r["pain_basis_eur"] = ""
            r["pain_tax_fte"] = ""
            r["pain_net_years"] = ""
            r["pain_eur_per_employee"] = ""
            r["pain_work_minutes"] = ""
            if not r.get("pain_note"):
                r["pain_note"] = "no_quantified_fiscal"
            continue

        basis = sign * m
        per_emp = basis / n_emp
        minutes = per_emp / eur_per_min

        r["pain_basis_eur"] = f"{basis:.0f}"
        r["pain_tax_fte"] = f"{basis / tax:.1f}"
        r["pain_net_years"] = f"{basis / net:.1f}"
        r["pain_eur_per_employee"] = f"{per_emp:.4f}"
        r["pain_work_minutes"] = f"{minutes:.2f}"
        r["pain_note"] = (
            f"mid*sign; unit v{u.get('unit_version', '?')} "
            f"tax={tax:.0f} net={net:.0f} Nemp={n_emp:.0f} "
            f"min/yr={work_min:.0f} eur/min={eur_per_min:.4f}"
        )

    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    print(f"Unit: tax={tax} net={net} N={n_emp:.0f} eur/min={eur_per_min:.4f}")
    for r in rows:
        print(
            f"{r['proposal_id'][:32]:32} "
            f"fte={str(r.get('pain_tax_fte','')):>10} "
            f"net_y={str(r.get('pain_net_years','')):>10} "
            f"min={str(r.get('pain_work_minutes','')):>8} "
            f"€/emp={str(r.get('pain_eur_per_employee','')):>10}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
