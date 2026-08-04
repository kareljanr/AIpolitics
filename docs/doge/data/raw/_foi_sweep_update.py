# FOI public-source sweep: status updates for partials found
import csv
from datetime import datetime, timezone

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
PATH = "docs/doge/data/foi_queue.csv"

UPDATES = {
    "gap_fanc_budget_2024_26": {
        "status": "partial",
        "response_summary": (
            "Kamer 1281/023: pers 16.039m ops 7.291m invest 1.864m fees 30.781m "
            "public_rec 3.893m (2026 budgeted); pers outturn 13.860m 2024. Residual: "
            "multi-year outturn 2022-25, FTE, Bel V recovery rules, statutory accounts"
        ),
        "note": "sweep2026-08-05: partial from tick756 Kamer fill",
    },
    "gap_gba_accounts_l5": {
        "status": "partial",
        "response_summary": (
            "AR2024/25 public: werkingskrediet 13.274m(2023)/15.113m(2024)/15.300m(2025); "
            "dotatie 14.002m(2024); toewijzing 12.669m(2025); staff 68/84/96. Residual: "
            "personnel vs ops vs invest, reserve stock path, BA codes"
        ),
        "note": "sweep2026-08-05: status partial (public AR totals tick304)",
    },
    "gap_bbi_bank_collection_l5": {
        "status": "partial",
        "response_summary": (
            "CoA 2026_20: bank investigations 2015-2024 assessed taxes 2.3bn of which "
            "collected only 36m; ~80pct corrections 5th Directorate (preventive). Residual: "
            "cash collection schedule by year 2015-2026; CAP foreign/crypto completeness"
        ),
        "note": "sweep2026-08-05: CoA 2026_20 collected 36m on 2.3bn assessed; residual yearly path",
    },
    "gap_isi_bank_inquiry_collection_l5": {
        "status": "partial",
        "response_summary": (
            "CoA 2026_20 dual: established 2.3bn 2015-2024; collected 36m aggregate. "
            "Residual: established vs collected matrix by year and by direction 2015-2025; "
            "aging open claims; prevented vs cash-collectible share"
        ),
        "note": "sweep2026-08-05: aggregate collect 36m public; year x direction matrix residual",
    },
    "gap_mons_budget_l5": {
        "status": "partial",
        "response_summary": (
            "2025 ord rec 246.2m dep 244.2m named L5 sample; 2026 MB1 ord ~241.8m extra ~63.2m "
            "totals. Residual: full BI2026 named third-party ASBL top20 table"
        ),
        "note": "sweep2026-08-05: reconfirm partial totals; named 2026 L5 still FOI",
    },
}


def main():
    with open(PATH, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    n = 0
    for r in rows:
        gid = r.get("gap_id")
        if gid not in UPDATES:
            continue
        u = UPDATES[gid]
        r["status"] = u["status"]
        r["response_summary"] = u["response_summary"]
        r["updated_utc"] = NOW
        notes = r.get("notes") or ""
        if u["note"] not in notes:
            r["notes"] = (notes + " | " + u["note"]).strip(" |")
        n += 1
        print("updated", gid, "->", u["status"])

    with open(PATH, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print("done", n, "updates;", len(rows), "rows")


if __name__ == "__main__":
    main()
