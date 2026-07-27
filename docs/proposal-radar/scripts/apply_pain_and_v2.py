#!/usr/bin/env python3
"""Apply analysis_version=2 metadata + taxpayer pain columns to proposals.csv."""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATA = Path(__file__).resolve().parents[1] / "data"
TAX, NET = 19400.0, 29500.0

META = {
    "prop_2025_unemp_time_limit": dict(saving="", min="", max="", note="saving uncertain; pain blank", ver="2"),
    "prop_2025_cgt_capital_gains": dict(
        saving="", min="", max="", note="revenue instrument; pain blank until outturn", ver="2"
    ),
    "prop_2026_centenindex": dict(
        saving="", min="", max="", note="public bill saving unquantified in sources", ver="2"
    ),
    "prop_2021_company_car_ice_2026": dict(
        saving="yes", min="500000000", max="1200000000", note="TE kill mid saving", ver="2"
    ),
    "prop_2025_hybrid_car_rehab": dict(saving="", min="", max="", note="foregone saving unknown", ver="2"),
    "prop_2026_vl_syntra_49m": dict(saving="no", min="49700000", max="49700000", note="one-off cost", ver="2"),
    "prop_2026_wk_veldrijden_ostend": dict(saving="no", min="350000", max="350000", note="one-off cost", ver="2"),
    "prop_2022_smaakhaven_38m": dict(saving="no", min="38000000", max="38000000", note="envelope cost", ver="2"),
    "prop_2026_dolphin_ban_2036": dict(
        saving="no", min="0", max="5000000", note="speculative public cost range", ver="2"
    ),
    "prop_2026_fwb_budget_cuts_255m": dict(
        saving="yes", min="255000000", max="255000000", note="headline economies if cash-real", ver="2"
    ),
}


def main() -> int:
    path = DATA / "proposals.csv"
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    fields: list[str] = []
    seen: set[str] = set()
    for f in list(rows[0].keys()) + [
        "fiscal_is_saving",
        "pain_basis_eur",
        "pain_tax_fte",
        "pain_net_years",
        "pain_note",
    ]:
        if f not in seen:
            seen.add(f)
            fields.append(f)

    # Prefer pain columns after fiscal_confidence
    preferred = []
    for f in fields:
        if f.startswith("pain_") or f == "fiscal_is_saving":
            continue
        preferred.append(f)
        if f == "fiscal_confidence":
            preferred.extend(
                ["fiscal_is_saving", "pain_basis_eur", "pain_tax_fte", "pain_net_years", "pain_note"]
            )
    for f in fields:
        if f not in preferred:
            preferred.append(f)
    fields = preferred

    for r in rows:
        pid = r["proposal_id"]
        m = META[pid]
        r["analysis_version"] = m["ver"]
        r["updated_utc"] = NOW
        r["fiscal_is_saving"] = m["saving"]
        if m["min"] != "":
            r["fiscal_static_min_eur"] = m["min"]
            r["fiscal_static_max_eur"] = m["max"]
        if m["min"] == "" and m["max"] == "":
            r["pain_basis_eur"] = ""
            r["pain_tax_fte"] = ""
            r["pain_net_years"] = ""
            r["pain_note"] = m["note"]
            continue
        lo, hi = float(m["min"]), float(m["max"])
        mid = (lo + hi) / 2.0
        sign = -1.0 if m["saving"] == "yes" else 1.0
        basis = sign * mid
        r["pain_basis_eur"] = f"{basis:.0f}"
        r["pain_tax_fte"] = f"{basis / TAX:.1f}"
        r["pain_net_years"] = f"{basis / NET:.1f}"
        r["pain_note"] = m["note"] + f"; unit tax={TAX:.0f} net={NET:.0f}"

    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    hpath = DATA / "score_history.csv"
    hfields = [
        "history_id",
        "proposal_id",
        "analysis_version",
        "clownpoints",
        "genius_score",
        "policy_index",
        "score_confidence",
        "changed_reason",
        "recorded_utc",
    ]
    with hpath.open(encoding="utf-8", newline="") as f:
        hist = list(csv.DictReader(f))
    for r in rows:
        hist.append(
            {
                "history_id": f"hist_{r['proposal_id']}_v2_pain",
                "proposal_id": r["proposal_id"],
                "analysis_version": "2",
                "clownpoints": r["clownpoints"],
                "genius_score": r["genius_score"],
                "policy_index": r["policy_index"],
                "score_confidence": r["score_confidence"],
                "changed_reason": "deep_memo_v2_and_or_taxpayer_pain",
                "recorded_utc": NOW,
            }
        )
    with hpath.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=hfields)
        w.writeheader()
        w.writerows(hist)

    for r in rows:
        print(
            f"{r['proposal_id'][:34]:34} "
            f"tax_fte={str(r.get('pain_tax_fte','')):>10} "
            f"net_y={str(r.get('pain_net_years','')):>10} "
            f"save={r.get('fiscal_is_saving')}"
        )
    print("OK", NOW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
