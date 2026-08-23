# tick 1939 — Enodia YE2025 Medium CW (rq_1939; 1938 already closed by concurrent)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # repo root
DATA = Path(__file__).resolve().parent
TS = "2026-08-27T16:45:00Z"
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
        "source_id": "src_enodia_jr2025_cw",
        "title": "Companyweb Enodia (TECTEO) YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0204245277/enodia",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-27",
        "source_class": "secondary_aggregator",
        "notes": "tick1939; neerlegging 24.07.2026; YE 31.12.2025; pnl 29600993 DROP -18.22pct; equity 1190324008 flat -0.21pct; bruto 19846904 DROP -2.41pct; FTE 170.9; omzet empty; assets Unknown",
    },
    {
        "source_id": "src_enodia_kbo",
        "title": "KBO Enodia / TECTEO 0204.245.277 Walloon public energy CV",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0204245277",
        "publisher": "KBO",
        "accessed_date": "2026-08-27",
        "source_class": "official_register",
        "notes": "tick1939; Actief CV; Boulevard Piercot 46 4000 Liege; email officiel.ic-enodia@enodia.net; web www.enodia.net; afkorting TECTEO; parent path of Nethys/Elicio",
    },
    {
        "source_id": "src_enodia_foi_contact",
        "title": "Enodia FOI channel (officiel.ic-enodia@enodia.net)",
        "url": "https://www.enodia.net/",
        "publisher": "Enodia / KBO",
        "accessed_date": "2026-08-27",
        "source_class": "foi_contact",
        "notes": "tick1939; KBO email officiel.ic-enodia@enodia.net; zetel Boulevard Piercot 46 4000 Liege; FOI ready not sent",
    },
]
append_csv(DATA / "sources.csv", sources_new)

budgets_new = [
    {
        "budget_id": "bud_enodia_pnl_jr2025",
        "entity_id": "cv_enodia",
        "year": "2025",
        "amount_eur": "29600993",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived 9904",
        "source_id": "src_enodia_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1939; YE2025 pnl 29600993 DROP -18.22pct",
    },
    {
        "budget_id": "bud_enodia_equity_jr2025",
        "entity_id": "cv_enodia",
        "year": "2025",
        "amount_eur": "1190324008",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived 10/15",
        "source_id": "src_enodia_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1939; YE2025 equity 1190324008 flat -0.21pct vs 1192817810 YE2024",
    },
    {
        "budget_id": "bud_enodia_bruto_jr2025",
        "entity_id": "cv_enodia",
        "year": "2025",
        "amount_eur": "19846904",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived 9900",
        "source_id": "src_enodia_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1939; YE2025 bruto 19846904 DROP -2.41pct",
    },
    {
        "budget_id": "bud_enodia_fte_jr2025",
        "entity_id": "cv_enodia",
        "year": "2025",
        "amount_eur": "171",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived FTE 170.9",
        "source_id": "src_enodia_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1939; YE2025 FTE 170.9 (stored 171)",
    },
]
append_csv(DATA / "budgets.csv", budgets_new)

comm = {
    "commitment_id": "comm_enodia_jr2025_equity",
    "title": "Enodia YE2025 leftover Walloon public energy holding dual (equity 1.19bn / pnl DROP 29.6m)",
    "entity_id": "cv_enodia",
    "beneficiary": "Walloon municipalities / Nethys / Elicio / Orange path / energy+telecom users",
    "legal_basis": "WVV CV; NBB neerlegging; Bestuursdecreet / openbaarheid; Walloon public intercommunale path (ex-TECTEO)",
    "decision_date": "2026-07-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1190324008",
    "cash_by_year": "2025:pnl=29600993;equity=1190324008;bruto=19846904;fte=170.9;omzet=empty;assets=Unknown",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0204245277/enodia",
    "stated_goal": "Walloon public energy/telecom group holding (parent of Nethys)",
    "cut_option": "FOI NBB PDF + assets/debt + Nethys/Elicio share % / FVA path explaining pnl DROP vs thin bruto",
    "source_id": "src_enodia_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Liege>Enodia>JR2025_L5",
    "notes": "tick1939; Medium CW; assets Unknown Upswitch YE2024-only; preferred AGB Bornem JR2024 / Dijk92 CDN 403 / FARO YE2024; do not redo BNO/Fluxys holding/LNG/c-grid/c-grid Antwerp/ETB/Elia Group/Pipelink/Nethys; NON-Eneco; double-count vs Nethys/Elicio possible",
}
append_csv(DATA / "commitments.csv", [comm])

lb = {
    "item_id": "lb_enodia_equity_1_19bn_pnl_drop_29_6m_jr2025",
    "name": "Enodia equity 1.19bn / pnl DROP 29.6m / thin bruto (Walloon public energy holding)",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Wallonie>Liege>Enodia>JR2025_L5",
    "annual_cost_eur": "29600993",
    "total_cost_eur": "1190324008",
    "tco_notes": "pnl 29600993 DROP -18pct equity 1190324008 flat bruto 19846904 FTE 170.9 omzet empty assets Unknown; NBB PDF unresolved",
    "confidence": "medium",
    "source_id": "src_enodia_jr2025_cw",
    "beneficiaries": "Walloon municipalities / Nethys / Elicio / telecom-energy users",
    "stated_goal": "Walloon public energy/telecom group holding (ex-TECTEO)",
    "measured_outcome": "Equity stuck ~1.19bn with pnl DROP -18pct and thin bruto; assets/omzet unpublished; NBB PDF unresolved",
    "absurdity_score": "6.5",
    "cost_score": "9.0",
    "difficulty": "3.5",
    "priority_index": "7.2",
    "cut_proposal": "Publish NBB PDF + assets/debt + Nethys/Elicio share % + FVA/dividend recon",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1939; Medium CW; leftover after Fluxys c-grid Antwerp; not TE-additive; NON-Eneco; double-count vs Nethys/Elicio possible",
}
append_csv(DATA / "leaderboard.csv", [lb])

ent = {
    "entity_id": "cv_enodia",
    "name_nl": "Enodia CV (ex-TECTEO; leftover Walloon public energy holding dual)",
    "name_fr": "Enodia SC (ex-TECTEO; holding energie public wallon residuel)",
    "name_en": "Enodia CV leftover Walloon public energy/telecom holding dual",
    "level": "other",
    "parent_id": "sec_wallonia",
    "community_language": "fr",
    "website": "https://www.enodia.net/",
    "foi_email": "officiel.ic-enodia@enodia.net",
    "foi_postal": "Boulevard Piercot 46 4000 Liège",
    "notes": "tick1939 leftover after Fluxys c-grid Antwerp; KBO 0204.245.277 Actief CV afkorting TECTEO; YE2025 Medium pnl DROP 29.6m equity 1.19bn bruto 19.8m FTE 170.9 omzet empty assets Unknown; parent of Nethys; NBB PDF FOI; NOT Fluxys chain / BNO / Pipelink",
}
append_csv(DATA / "entities.csv", [ent])

foi = {
    "gap_id": "gap_enodia_nbb_pdf_assets_share_fva_l5",
    "hierarchy_path": "Wallonie>Liege>Enodia>nbb_assets_share_fva_L5",
    "entity_id": "cv_enodia",
    "what_is_missing": "NBB deposit id + full JR2025 PDF (assets/cash/debt/FVA exact; VTE detail); aandeelhouders % (gemeenten / other); Nethys/Elicio/Orange stake map; FVA and dividend path explaining pnl DROP 29.6m with thin bruto 19.8m and empty omzet; related-party flows",
    "why_it_matters": "Walloon public energy holding — equity 1.19bn / pnl DROP 29.6m hides municipal energy+telecom money after Nethys mined; assets/omzet still Unknown on free aggregators",
    "priority": "8",
    "recipient_body": "Enodia CV (ex-TECTEO)",
    "recipient_email": "officiel.ic-enodia@enodia.net",
    "recipient_postal": "Boulevard Piercot 46 4000 Liège (cc Nethys)",
    "draft_letter_path": "docs/doge/foi/drafts/gap_enodia_nbb_pdf_assets_share_fva_l5.md",
    "status": "ready",
    "date_ready": "2026-08-27",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_enodia_jr2025_equity",
    "linked_leaderboard_id": "lb_enodia_equity_1_19bn_pnl_drop_29_6m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1939; human-send only; Medium CW; assets Unknown; AGB Bornem JR2024; Dijk92 CDN 403; FARO YE2024; next every-10 1940",
}
append_csv(DATA / "foi_queue.csv", [foi])

update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1939": {
            "status": "done",
            "entity_id": "cv_enodia",
            "instructions": (
                "Completed: Enodia CV leftover Walloon public energy holding dual after Fluxys c-grid Antwerp; "
                "KBO 0204.245.277 Actief CV (TECTEO); YE2025 Medium Companyweb; sourced euros pnl 29600993 equity "
                "1190324008 bruto 19846904 FTE 170.9; omzet/assets Unknown; FOI ready gap_enodia_nbb_pdf_assets_share_fva_l5; "
                "NOT BNO / Fluxys holding/LNG/c-grid/c-grid Antwerp / ETB / Elia Group / Pipelink / Nethys"
            ),
            "blocked_gap_id": "gap_enodia_nbb_pdf_assets_share_fva_l5",
            "updated_utc": TS,
            "notes": (
                "tick1939 Enodia leftover after Fluxys c-grid Antwerp; KBO 0204.245.277; YE2025 Medium CW "
                "(pnl DROP 29.6m equity 1.19bn bruto 19.8m FTE 170.9 omzet/assets Unknown); FOI ready not sent; "
                "AGB Bornem JR2024; Dijk92 CDN 403; FARO YE2024; do not redo BNO/Fluxys holding/LNG/c-grid/c-grid "
                "Antwerp/ETB/Elia Group/Pipelink/Nethys; next rq_1940 EVERY-10"
            ),
        }
    },
)

rq1940 = {
    "task_id": "rq_1940",
    "title": "EVERY-10 + leftover dual residual hole-fill after Enodia (AGB/Dijk92-if-200 / FARO-if-YE2025 / otherHVZ-IGS-if-live)",
    "sprint": "hole_fill",
    "priority": "8",
    "status": "open",
    "hierarchy_target": "Vlaanderen>leftover_dual",
    "entity_id": "",
    "instructions": (
        "Tick 1940 MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md then hole-fill. "
        "Prefer leftover AGB/APB if PDF live, else Dijk92 if CDN 200, else FARO if TRUE NBB YE2025, else "
        "Fluxys hydrogen / RESA YE2025 / Fluxys Belgium statutory / other HVZ/IGS if unused live YE2025 euros. "
        "Do NOT redo BNO, Fluxys holding/LNG/c-grid/c-grid Antwerp, ETB, Elia Group, Pipelink, Enodia, Nethys."
    ),
    "blocked_gap_id": "",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "spawned after tick1939; EVERY-10 required; next every-10 after this is 1950",
}
append_csv(DATA / "research_queue.csv", [rq1940])

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
            "last_unit_id": "rq_1939",
            "ticks_completed": "1939",
            "paused": "no",
            "notes": (
                "tick1939 leftover Enodia 0204.245.277 Medium CW (pnl DROP 29.6m equity 1.19bn bruto 19.8m "
                "FTE 170.9 omzet/assets Unknown); NBB PDF+share/FVA FOI; AGB Bornem JR2024; Dijk92 CDN 403; "
                "FARO YE2024; next rq_1940 EVERY-10; continuous hole_fill"
            ),
        }
    )

log_block = """

## Tick 1939 - 2026-08-27T16:45:00Z - rq_1939 Enodia (equity 1.19bn / pnl DROP 29.6m / Medium)

- Unit: **rq_1939** leftover dual after Fluxys c-grid Antwerp (1938 concurrent already closed). Prefer NON-Eneco live. Hunt: AGB Bornem still **JR2024-only**; Dijk92 CDN **2026-00377886 still 403**; FARO NBB still **YE2024**. Took leftover **Enodia CV** (KBO **0204.245.277**; Boulevard Piercot 46 Liège; ex-TECTEO Walloon public energy/telecom holding; parent of mined Nethys; NON-Eneco). Do not redo BNO/Fluxys holding/LNG/c-grid/c-grid Antwerp/ETB/Elia Group/Pipelink/Nethys.
- Primary hunt: NBB deposit PDF unresolved; Upswitch YE2024-only for assets. **Medium** euros from [Companyweb](https://www.companyweb.be/nl/0204245277/enodia) + **Strong** KBO contact (neerlegging **24.07.2026**; YE **31.12.2025**): omzet **empty**; bruto **EUR19,846,904** (**DROP -2.41%**); PnL **EUR29,600,993** (**DROP -18.22%**); equity **EUR1,190,324,008** (flat **-0.21%**); FTE **170.9**; assets **Unknown** (not invented).
- Wrote: sources (+3); budgets (+4); commitments (+1); leaderboard (+1); entities (+1); foi + draft gap_enodia_nbb_pdf_assets_share_fva_l5; rq_1939=done + rq_1940 open (EVERY-10); loop_state ticks=1939.
- FOI opened: NBB PDF + assets/share % / FVA (**ready**, human-send only).
- NOT every-10 (**next every-10 is 1940**). Next: rq_1940 MUST refresh progress+waste top10 then hole-fill.
"""

with (ROOT / "docs/doge/loop_log.md").open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1939 write OK")
