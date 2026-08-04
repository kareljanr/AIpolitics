import csv

cp = "docs/doge/data/commitments.csv"
with open(cp, encoding="utf-8", newline="") as f:
    rdr = csv.DictReader(f)
    cf = rdr.fieldnames
    crows = list(rdr)

cids = {r["commitment_id"] for r in crows}
cid = "cmt_bda_portfolio_implicit_cost_2025"
if cid in cids:
    print("commitment exists")
else:
    row = {k: "" for k in cf}
    row.update(
        {
            "commitment_id": cid,
            "title": "Federal debt portfolio implicit cost 2.01pct YE2025 + new LT 3.12pct",
            "entity_id": "fed_debt_agency",
            "beneficiary": "Federal treasury / bondholders",
            "legal_basis": "Debt Agency organic rules + OLO programme",
            "decision_date": "2025-12-31",
            "start_year": "2025",
            "end_year": "2026",
            "total_envelope_eur": "",
            "cash_json": '{"implicit_cost_pct_ye2025":2.01,"new_lt_issuance_avg_pct_2025":3.12,"avg_life_y":9.98,"duration_y":7.27,"olo_stock_bn_class":462.3}',
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://www.debtagency.be/sites/default/files/content/download/files/review_outlook_2025_2026_0.pdf",
            "stated_goal": "Transparent federal debt cost of capital",
            "cut_option": "Instrument L5 FOI residual; dual Entity II",
            "source_id": "src_bda_review_outlook_2025_2026_tick411",
            "confidence": "strong",
            "hierarchy_path": "Federal>Debt>portfolio_implicit_rate",
            "notes": "sweep2026-08-05 partial fill gap_debt_interest_implicit_rate_l5; rate not cash stock; dual tick411",
        }
    )
    crows.append(row)
    with open(cp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cf)
        w.writeheader()
        w.writerows(crows)
    print("commitment added")
