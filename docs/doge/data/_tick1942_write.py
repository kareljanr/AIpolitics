# tick 1942 — Synatom YE2025 Medium CW (rq_1942; 1941 Atrias already closed)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-27T18:15:00Z"
csv.field_size_limit(10**7)


def append_csv(path, rows):
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        for r in rows:
            w.writerow(r)


def update_csv_rows(path, key, updates_by_key):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        k = row[key]
        if k in updates_by_key:
            row.update(updates_by_key[k])
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


sources_new = [
    {
        "source_id": "src_synatom_jr2025_cw",
        "title": "Companyweb Synatom YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0406820671/synatom",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": "tick1942; neerlegging 09.07.2026; YE 31.12.2025; omzet 299812250 JUMP +18.43pct; pnl 20547928 JUMP >1000pct; equity 15591563 +7.07pct; bruto NEG -283664871 DROP -91.59pct; FTE 22.1; assets Unknown",
    },
    {
        "source_id": "src_synatom_kbo_1942",
        "title": "KBO Synatom 0406.820.671 Belgian nuclear fuel / provisions NV",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406820671",
        "publisher": "KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": "tick1942; Actief NV; Simon Bolivarlaan 36 1000 Brussel; web www.engie.com in KBO; afkorting Synatom; NACE 24.460; email empty",
    },
    {
        "source_id": "src_synatom_ar_page_1942",
        "title": "Synatom annual reports page (statutory from YE2025 via NBB)",
        "url": "https://www.synatom.be/en/annual-reports/",
        "publisher": "Synatom",
        "accessed_date": "2026-08-27",
        "source_class": "official_org",
        "notes": "tick1942; YE2025 statutory accounts directed to NBB; activity report 2024 PDF live; contact form only",
    },
]
append_csv(DATA / "sources.csv", sources_new)

budgets_new = [
    {
        "budget_id": "bud_synatom_omzet_jr2025",
        "entity_id": "synatom",
        "year": "2025",
        "amount_eur": "299812250",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet",
        "source_id": "src_synatom_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1942; YE2025 omzet 299812250 JUMP +18.43pct vs 253146506",
    },
    {
        "budget_id": "bud_synatom_pnl_jr2025",
        "entity_id": "synatom",
        "year": "2025",
        "amount_eur": "20547928",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived 9904",
        "source_id": "src_synatom_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1942; YE2025 pnl 20547928 JUMP >1000pct vs 797135",
    },
    {
        "budget_id": "bud_synatom_equity_jr2025",
        "entity_id": "synatom",
        "year": "2025",
        "amount_eur": "15591563",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived 10/15",
        "source_id": "src_synatom_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1942; YE2025 equity 15591563 +7.07pct vs 14562015",
    },
    {
        "budget_id": "bud_synatom_bruto_jr2025",
        "entity_id": "synatom",
        "year": "2025",
        "amount_eur": "-283664871",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived 9900",
        "source_id": "src_synatom_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1942; YE2025 bruto NEG -283664871 DROP -91.59pct vs -148057503",
    },
    {
        "budget_id": "bud_synatom_fte_jr2025",
        "entity_id": "synatom",
        "year": "2025",
        "amount_eur": "22",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived FTE 22.1",
        "source_id": "src_synatom_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1942; YE2025 FTE 22.1 (stored 22)",
    },
]
append_csv(DATA / "budgets.csv", budgets_new)

comm = {
    "commitment_id": "comm_synatom_jr2025_omzet",
    "title": "Synatom YE2025 leftover nuclear provisions dual (omzet JUMP 299.8m / pnl JUMP 20.5m / bruto NEG 283.7m)",
    "entity_id": "synatom",
    "beneficiary": "Hedera CAP / NIRAS / CPN / Electrabel-ENGIE path / nuclear liability taxpayers",
    "legal_basis": "WVV NV; nuclear provisions law; NBB neerlegging; dual Hedera CAP / CPN oversight",
    "decision_date": "2026-07-09",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "299812250",
    "cash_by_year": "2025:omzet=299812250;pnl=20547928;equity=15591563;bruto=-283664871;fte=22.1;assets=Unknown",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0406820671/synatom",
    "stated_goal": "Belgian nuclear fuel company / nuclear provisions management (dual Hedera CAP)",
    "cut_option": "FOI NBB PDF + assets/debt + provisions/CAP portfolio eoy2025 + Hedera/Electrabel flows",
    "source_id": "src_synatom_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Federal>Nuclear>Synatom>JR2025_L5",
    "notes": "tick1942; Medium CW; preferred AGB Bornem JR2024 / Dijk92 CDN 403 / FARO YE2024; do not redo RESA/Atrias/Sibelga/ORES/Fluxys*/ETB/Elia/Enodia/BNO/Pipelink/Publi-T/Publigas/Interfin; NON-Eneco (ENGIE nuclear path distinct); double-count vs Hedera CAP 15bn possible",
}
append_csv(DATA / "commitments.csv", [comm])

# priority_index = 0.55*7.5 + 0.35*7.0 + 0.10*(10-3.5) = 4.125+2.45+0.65 = 7.225 -> 7.2
lb = {
    "item_id": "lb_synatom_omzet_jump_299_8m_pnl_jump_20_5m_bruto_neg_283_7m_jr2025",
    "name": "Synatom omzet JUMP 299.8m / pnl JUMP 20.5m / bruto NEG 283.7m (nuclear provisions YE2025)",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Federal>Nuclear>Synatom>JR2025_L5",
    "annual_cost_eur": "299812250",
    "total_cost_eur": "299812250",
    "tco_notes": "omzet 299812250 JUMP pnl 20547928 JUMP equity 15591563 bruto NEG -283664871 FTE 22.1; assets/CAP portfolio Unknown; dual Hedera CAP ~15bn",
    "confidence": "medium",
    "source_id": "src_synatom_jr2025_cw",
    "beneficiaries": "Hedera / NIRAS / CPN / ENGIE-Electrabel path",
    "stated_goal": "Nuclear fuel + provisions management dual Hedera CAP",
    "measured_outcome": "PnL JUMP >1000pct with bruto NEG 284m and equity only 15.6m; CAP assets opaque; NBB PDF unresolved",
    "absurdity_score": "7.0",
    "cost_score": "7.5",
    "difficulty": "3.5",
    "priority_index": "7.2",
    "cut_proposal": "Publish NBB PDF + assets/debt + CAP/provisions eoy2025 + Hedera/Electrabel flow recon",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1942; Medium CW; leftover after Atrias; not TE-additive; double-count vs Hedera CAP possible",
}
append_csv(DATA / "leaderboard.csv", [lb])

update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "synatom": {
            "website": "https://www.synatom.be",
            "foi_email": "",
            "foi_postal": "Simon Bolivarlaan 36 1000 Brussel (contact form https://www.synatom.be/en/contact/)",
            "notes": (
                "Belgian nuclear provisioning company; tick288 CAP dual Hedera; "
                "tick1942 YE2025 Medium CW KBO 0406.820.671 Actief NV; omzet 299.8m JUMP pnl 20.5m JUMP "
                "equity 15.6m bruto NEG 283.7m FTE 22.1 assets Unknown; NBB PDF FOI; dual Hedera CAP"
            ),
        }
    },
)

foi = {
    "gap_id": "gap_synatom_nbb_pdf_assets_provisions_cap_l5",
    "hierarchy_path": "Federal>Nuclear>Synatom>nbb_assets_provisions_cap_L5",
    "entity_id": "synatom",
    "what_is_missing": "NBB deposit id + full JR2025 PDF (assets/debt/cash/provisions exact); CAP portfolio eoy2025 (liquidated+residual) recon vs Hedera; explanation bruto NEG 283.7m with pnl JUMP 20.5m; Electrabel/ENGIE related-party flows; aandeelhouders %",
    "why_it_matters": "Nuclear provisions dual Hedera CAP ~15bn — 300m omzet / pnl JUMP 20.5m with bruto NEG 284m and equity only 15.6m hides true public nuclear liability money after Atrias/RESA mined",
    "priority": "8",
    "recipient_body": "Synatom NV",
    "recipient_email": "",
    "recipient_postal": "Simon Bolivarlaan 36 1000 Brussel (cc Hedera / CPN / FOD Economie; contact form synatom.be)",
    "draft_letter_path": "docs/doge/foi/drafts/gap_synatom_nbb_pdf_assets_provisions_cap_l5.md",
    "status": "ready",
    "date_ready": "2026-08-27",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_synatom_jr2025_omzet",
    "linked_leaderboard_id": "lb_synatom_omzet_jump_299_8m_pnl_jump_20_5m_bruto_neg_283_7m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1942; human-send only; Medium CW; Upswitch miss; AGB Bornem JR2024; Dijk92 CDN 403; FARO YE2024; next every-10 1950",
}
append_csv(DATA / "foi_queue.csv", [foi])

update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1942": {
            "status": "done",
            "entity_id": "synatom",
            "instructions": (
                "Completed: Synatom NV leftover nuclear provisions dual after Atrias; KBO 0406.820.671 Actief NV; "
                "YE2025 Medium Companyweb; sourced euros omzet 299812250 JUMP pnl 20547928 JUMP equity 15591563 "
                "bruto NEG -283664871 FTE 22.1 assets Unknown; FOI ready gap_synatom_nbb_pdf_assets_provisions_cap_l5; "
                "NOT RESA/Atrias/Sibelga/ORES/Fluxys*/ETB/Elia/Enodia/BNO/Pipelink/Publi-T/Publigas/Interfin"
            ),
            "blocked_gap_id": "gap_synatom_nbb_pdf_assets_provisions_cap_l5",
            "updated_utc": TS,
            "notes": (
                "tick1942 Synatom leftover after Atrias; KBO 0406.820.671; YE2025 Medium CW "
                "(omzet JUMP 299.8m pnl JUMP 20.5m bruto NEG 283.7m equity 15.6m); FOI ready not sent; "
                "AGB Bornem JR2024; Dijk92 CDN 403; FARO YE2024; next rq_1943; next every-10 1950"
            ),
        }
    },
)

rq1943 = {
    "task_id": "rq_1943",
    "title": "Leftover dual residual hole-fill after Synatom (AGB/Dijk92-if-200 / FARO-if-YE2025 / otherHVZ-IGS-if-live)",
    "sprint": "hole_fill",
    "priority": "8",
    "status": "open",
    "hierarchy_target": "Vlaanderen>leftover_dual",
    "entity_id": "",
    "instructions": (
        "Tick 1943 after 1942 Synatom. Prefer leftover AGB/APB if PDF live, else Dijk92 if CDN 200, else FARO if "
        "TRUE NBB YE2025, else other HVZ/IGS/energy holding if unused live YE2025 euros. Do NOT redo BNO, "
        "Fluxys holding/LNG/c-grid/c-grid Antwerp/hydrogen, ETB, Elia Group, Pipelink, Enodia, RESA, Atrias, "
        "Sibelga, ORES, Publi-T, Publigas, Interfin, Synatom."
    ),
    "blocked_gap_id": "",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "spawned after tick1942; next every-10 1950",
}
append_csv(DATA / "research_queue.csv", [rq1943])

with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_1942",
            "ticks_completed": "1942",
            "paused": "no",
            "notes": (
                "tick1942 leftover Synatom 0406.820.671 Medium CW (omzet JUMP 299.8m pnl JUMP 20.5m "
                "bruto NEG 283.7m equity 15.6m FTE 22.1 assets Unknown); NBB PDF+CAP/provisions FOI; "
                "AGB Bornem JR2024; Dijk92 CDN 403; FARO YE2024; next rq_1943; next every-10 1950; continuous hole_fill"
            ),
        }
    )

log_block = """

## Tick 1942 - 2026-08-27T18:15:00Z - rq_1942 Synatom (omzet JUMP 299.8m / pnl JUMP 20.5m / Medium)

- Unit: **rq_1942** leftover dual after concurrent closed **rq_1941 Atrias**. Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; Dijk92 CDN **403**; FARO YE2024. Took leftover **Synatom NV** (KBO **0406.820.671**; Simon Bolivarlaan 36 Brussel; Belgian nuclear fuel/provisions holding dual Hedera CAP; ENGIE path; only YE2024 CAP figures mined at tick288). Do not redo RESA/Atrias/Sibelga/ORES/Fluxys*/ETB/Elia/Enodia/BNO/Pipelink/Publi-T/Publigas/Interfin.
- Primary hunt: NBB deposit PDF unresolved; Upswitch miss this tick. **Medium** euros from [Companyweb](https://www.companyweb.be/nl/0406820671/synatom) + KBO (neerlegging **09.07.2026**; YE **31.12.2025**): omzet **EUR299,812,250** (**JUMP +18.43%**); PnL **EUR20,547,928** (**JUMP >1000%**); equity **EUR15,591,563** (**+7.07%**); bruto **NEG EUR-283,664,871** (**DROP -91.59%**); FTE **22.1**; assets **Unknown**.
- Wrote: sources (+3); budgets (+5); commitments (+1); leaderboard (+1); entities (updated synatom); foi + draft gap_synatom_nbb_pdf_assets_provisions_cap_l5; rq_1942=done + rq_1943 open; loop_state ticks=1942.
- FOI opened: NBB PDF + assets/debt + CAP/provisions recon (**ready**, human-send only; postal/contact-form — KBO email empty).
- NOT every-10 (**next every-10 is 1950**). Next: rq_1943 (AGB/Dijk92-if-200 / FARO-if-YE2025 / otherHVZ-IGS).
"""
with (ROOT / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1942 write OK")
