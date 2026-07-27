#!/usr/bin/env python3
"""Recompute pain_tax_fte and pain_net_years on proposals.csv from taxpayer_unit.csv."""
from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
TAX = 19400.0
NET = 29500.0


def load_unit() -> tuple[float, float]:
    p = DATA / "taxpayer_unit.csv"
    if not p.exists():
        return TAX, NET
    with p.open(encoding="utf-8", newline="") as f:
        r = next(csv.DictReader(f))
    return float(r["tax_rounded_eur"]), float(r["net_rounded_eur"])


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
    tax, net = load_unit()
    path = DATA / "proposals.csv"
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys()) if rows else []
    for col in ("pain_tax_fte", "pain_net_years", "pain_basis_eur", "pain_note"):
        if col not in fields:
            fields.append(col)

    for r in rows:
        # savings: fiscal_static positive amount with basis that is a cut → detect via recommendation/notes is fragile
        # Convention: if notes or a new field fiscal_sign; default cost positive.
        # Use pain_note / instrument: if title has saving or we set fiscal_is_saving
        sign = 1.0
        if r.get("fiscal_is_saving", "").lower() in ("yes", "1", "true"):
            sign = -1.0
        m = mid(r.get("fiscal_static_min_eur", ""), r.get("fiscal_static_max_eur", ""))
        if m is None or m == 0 and r.get("fiscal_static_max_eur") in ("", "0", None) and r.get("fiscal_static_min_eur") in ("", "0", None):
            # unknown
            if r.get("fiscal_static_min_eur") in ("", None) and r.get("fiscal_static_max_eur") in ("", None):
                r["pain_tax_fte"] = ""
                r["pain_net_years"] = ""
                r["pain_basis_eur"] = ""
                r["pain_note"] = r.get("pain_note") or "no_quantified_fiscal"
                continue
        basis = sign * (m if m is not None else 0.0)
        # dolphin 0-5m: mid 2.5m
        r["pain_basis_eur"] = f"{basis:.0f}"
        r["pain_tax_fte"] = f"{basis / tax:.1f}"
        r["pain_net_years"] = f"{basis / net:.1f}"
        if not r.get("pain_note"):
            r["pain_note"] = "mid(min,max)*sign; unit be_avg_single_ft v1"

    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"Recomputed pain with tax={tax} net={net} for {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
