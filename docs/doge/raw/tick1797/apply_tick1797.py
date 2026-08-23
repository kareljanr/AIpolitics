import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
DATA = Path(r"docs/doge/data")
NOW = "2026-08-25T01:55:00Z"
TICK = 1797
EID = "nv_w4f"
GID = "gap_w4f_fva_48_38m_dividend_3_28m_recv_drop_12_57m_l5"
CID = "comm_w4f_jr2025_dividend_3_28m"
LID = "lb_w4f_fva_48_38m_dividend_3_28m_recv_drop_l5"
SRC = "src_w4f_jr2025_nbb"


def read(fn):
    with (DATA / fn).open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write(fn, fields, rows):
    with (DATA / fn).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": SRC,
        "title": "Wind4Flanders NV NBB VOL-kap YE2025 deposit 2026-00127411",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00127411.pdf",
        "publisher": "NBB / Wind4Flanders NV",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1797; KBO 0628.836.449; AV 19.05.2026; Deloitte/Van Baelen getrouw beeld; assets 53903666 FVA 48380710 dividend 3275357; Zefier dual 27.09pct",
    },
    {
        "source_id": "src_w4f_kbo",
        "title": "KBO Wind4Flanders NV 0628.836.449",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0628836449",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1797; NV; zetel Simon Bolivarlaan 36 1000 Brussel",
    },
    {
        "source_id": "src_w4f_zefier_sector_2025",
        "title": "Zefier rekeningsector Wind4Flanders per vennoot boekjaar 2025",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/698ee98962b24e3ab08331b6_Wind4Flanders%20nv%20(W4F).pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1797; ~117 gemeenten-deelnemers; dual residual after Zo-Fier 1796",
    },
]
ids = {r["source_id"] for r in rows}
for s in new_sources:
    if s["source_id"] not in ids:
        rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("entities.csv")
note = (
    "tick1797 leftover Zefier dual renewable holding after Zo-Fier 1796; KBO 0628.836.449 Actief; NV; "
    "official NBB VOL-kap YE2025 deposit 2026-00127411 CDN 200 36p; AV 19.05.2026; Deloitte/Jo Van Baelen getrouw beeld; "
    "Zefier 27.09pct; FVA Projects1-4/Alfa/Beta 48380710; sourced euros assets 53903666 equity after-distrib 46628514 "
    "pre-distrib equity 49903871 debt 7275152 cash 2178774 JUMP other recv ST 2906101 DROP from 12573528 "
    "fin opbr 1967952 pnl 1698988 dividend 3275357 LT loans 3420637 VTE 0; FOI ready; NOT every-10 (next 1800)"
)
if not any(r.get("entity_id") == EID for r in rows):
    rows.append(
        {
            "entity_id": EID,
            "name_nl": "Wind4Flanders NV / W4F (leftover Zefier dual / hernieuwbare holding; NOT Zo-Fier / EGPF / Portfineco)",
            "name_fr": "Wind4Flanders SA (dual Zefier residuel / holding renouvelable)",
            "name_en": "Wind4Flanders NV leftover Zefier dual renewable holding",
            "level": "other",
            "parent_id": "cv_zefier",
            "community_language": "nl",
            "website": "https://jaarverslag.zefier.be/overlay-pages/wind4flanders-nv",
            "foi_email": "info@zefier.be",
            "foi_postal": "Simon Bolivarlaan 36 1000 Brussel",
            "notes": note,
        }
    )
else:
    for r in rows:
        if r.get("entity_id") == EID:
            r["notes"] = note
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_w4f_assets_2025", 53903666, "Assets YE2025 53903666; tick1797"),
    ("bud_w4f_equity_after_2025", 46628514, "Equity na winstverdeling 46628514; tick1797"),
    ("bud_w4f_equity_pre_2025", 49903871, "Equity voor winstverdeling 49903871 (jaarverslag); tick1797"),
    ("bud_w4f_debt_2025", 7275152, "Debt 7275152 DROP; tick1797"),
    ("bud_w4f_fva_2025", 48380710, "FVA deelnemingen Projects1-4/Alfa/Beta 48380710 flat; tick1797"),
    ("bud_w4f_cash_2025", 2178774, "Cash 2178774 JUMP from 520543; tick1797"),
    ("bud_w4f_st_recv_2025", 2906101, "Overige vorderingen ST 2906101 DROP from 12573528; tick1797"),
    ("bud_w4f_diensten_2025", 61516, "Diensten diverse goederen 61516; tick1797"),
    ("bud_w4f_expl_2025", -62515, "Bedrijfsverlies -62515; tick1797"),
    ("bud_w4f_fin_opbr_2025", 1967952, "Financiele opbrengsten 1967952 (dividenden filialen 1727520); tick1797"),
    ("bud_w4f_fin_kosten_2025", 206449, "Financiele kosten 206449; tick1797"),
    ("bud_w4f_pnl_2025", 1698988, "PnL 1698988 tax 0; tick1797"),
    ("bud_w4f_dividend_2025", 3275357, "Uit te keren dividend 3275357; tick1797"),
    ("bud_w4f_lt_loans_2025", 3420637, "Overige leningen LT 3420637 (vennoten); tick1797"),
    ("bud_w4f_st_other_2025", 3275357, "Overige schulden ST 3275357 (=dividend payable); tick1797"),
    ("bud_w4f_commissaris_2025", 7554, "Bezoldiging commissaris Deloitte 7554; tick1797"),
]
existing = {r["budget_id"] for r in rows}
for bid, amt, notes in budgets:
    if bid in existing:
        continue
    rows.append(
        {
            "budget_id": bid,
            "entity_id": EID,
            "year": "2025",
            "amount_eur": str(amt),
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": "realized",
            "source_id": SRC,
            "confidence": "strong",
            "notes": notes,
        }
    )
write("budgets.csv", fields, rows)
print("budgets", len(rows))

fields, rows = read("commitments.csv")
if not any(r.get("commitment_id") == CID for r in rows):
    rows.append(
        {
            "commitment_id": CID,
            "title": "Wind4Flanders JR2025 leftover Zefier dual (dividend 3.28m / FVA 48.38m / recv DROP 12.57m)",
            "entity_id": EID,
            "beneficiary": "Zefier / ~117 gemeenten / W4F Projects 1-4 Alfa Beta / ENGIE partners",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal renewable holding dual via Zefier",
            "decision_date": "2026-05-19",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "3275357",
            "cash_by_year": "2025:3275357",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00127411.pdf",
            "stated_goal": "Local leftover Zefier W4F holding map — dividend 3.28m; FOI recv DROP + projectco matrix",
            "cut_option": "Publish ST recv 12.57m DROP counterparties + Projects Beta 18.5m reval path + vennoten loan rates",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>Wind4Flanders>JR2025_L5",
            "notes": "tick1797; YE2025; assets 53903666 FVA 48380710 pnl 1698988 dividend 3275357 ST recv DROP 12573528 to 2906101 cash JUMP; VTE 0; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; not TE-additive of 348bn",
        }
    )
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
if not any(r.get("item_id") == LID for r in rows):
    rows.append(
        {
            "item_id": LID,
            "name": "Wind4Flanders 2025: FVA 48.38m / dividend 3.28m / ST recv DROP 12.57m (Zefier dual holding)",
            "level": "L5",
            "type": "igs_energy_holding_dual",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>Wind4Flanders",
            "annual_cost_eur": "3275357",
            "total_cost_eur": "48380710",
            "tco_notes": "Envelope=dividend 3275357; FVA 48380710 in 6 projectcos (Beta alone 18.50m); ST other recv DROP 12.57m to 2.91m; cash JUMP 2.18m; VTE 0 shell holding; not pure waste — opacity on recv collapse + projectco dividends drop",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Zefier 27.09pct + ~117 municipalities + ENGIE/Electrabel stack",
            "stated_goal": "Holding for municipal wind projectcos via Zefier tracking sector H",
            "measured_outcome": "PnL 1.70m (tax 0); filial dividends 1.73m DROP vs 2024; payout 3.28m",
            "absurdity_score": "4",
            "cost_score": "6",
            "difficulty": "6",
            "priority_index": "5.0",
            "cut_proposal": "FOI ST recv DROP 12.57m counterparties + Projects dividend matrix + vennoten LT loan 3.42m rates",
            "status": "open",
            "struck_reason": "",
            "notes": "tick1797 leftover Zefier dual; strong NBB; not TE-additive; not pure-waste top10",
        }
    )
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
if not any(r.get("gap_id") == GID for r in rows):
    rows.append(
        {
            "gap_id": GID,
            "hierarchy_path": "Vlaanderen>IGS>Zefier>Wind4Flanders>JR2025_L5",
            "entity_id": EID,
            "what_is_missing": "Tegenpartijen overige vorderingen ST DROP 12573528 naar 2906101; dividendmatrix Projects1-4/Alfa/Beta (filialdividenden 1727520 vs prior); voorwaarden overige leningen LT 3420637 van W4F-vennoten(groepen); meerwaarden 18400000 path vs book; AV 19.05.2026 niet-gepersonaliseerd",
            "why_it_matters": "Largest Zefier dual holding (FVA 48.4m / dividend 3.28m to cities) with massive ST recv collapse 12.6m and filial dividend DROP — residual opacity after Zo-Fier tick1796",
            "priority": "8",
            "recipient_body": "Wind4Flanders NV / Zefier cv",
            "recipient_email": "info@zefier.be",
            "recipient_postal": "Simon Bolivarlaan 36 1000 Brussel",
            "draft_letter_path": f"docs/doge/foi/drafts/{GID}.md",
            "status": "ready",
            "date_ready": "2026-08-25",
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": CID,
            "linked_leaderboard_id": LID,
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "tick1797; human-send only; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; Portfineco 2026-00119667 / EGPF 2026-00206406 live unused deferred",
        }
    )
write("foi_queue.csv", fields, rows)
print("foi_queue", len(rows))

fields, rows = read("research_queue.csv")
for r in rows:
    if r.get("task_id") == "rq_1797":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = NOW
        r["notes"] = "tick1797 Wind4Flanders NV Zefier dual; KBO 0628.836.449; NBB 2026-00127411; FVA 48380710 dividend 3275357 recv DROP; FOI ready; every-10 1800"
        r["blocked_gap_id"] = GID
if not any(r.get("task_id") == "rq_1798" for r in rows):
    rows.append(
        {
            "task_id": "rq_1798",
            "title": "Leftover dual residual hole-fill after W4F (AGB/NSZ/Bosgroep/Portfineco-if-200/EGPF/IGS)",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "Belgique>LeftoverDual>Residual",
            "entity_id": "",
            "instructions": "Tick 1798 after 1797 W4F. Prefer leftover AGB/APB of mined cities if PDF live, else Bosgroep / IOED / Dijk92 if CDN 200 / FARO NBB YE2025 if live / Portfineco 2026-00119667 or EGPF 2026-00206406 if unused live / other HVZ if JR2025 euros newly live / other IGS. Skip already-done. Next every-10 1800.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick1797; NEXT residual dual; Portfineco+EGPF CDN live deferred; every-10 1800",
        }
    )
write("research_queue.csv", fields, rows)
print("research_queue updated")

fields, rows = read("loop_state.csv")
for r in rows:
    if r.get("state_id") == "main":
        r["mode"] = "continuous"
        r["current_sprint"] = "hole_fill"
        r["last_tick_utc"] = NOW
        r["last_unit_id"] = "rq_1797"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = (
            "tick1797 leftover Wind4Flanders NV Zefier dual; KBO 0628.836.449; NBB 2026-00127411; assets 53903666 "
            "FVA 48380710 dividend 3275357 pnl 1698988 ST recv DROP 12573528 to 2906101 cash JUMP 2178774 VTE 0; "
            "FOI recv/projectcos; Portfineco+EGPF CDN live deferred; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; "
            "NOT every-10 (next 1800); next rq_1798 residual dual; continuous hole_fill"
        )
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE")
