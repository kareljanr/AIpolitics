import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
DATA = Path(r"docs/doge/data")
NOW = "2026-08-25T01:15:00Z"
TICK = 1795
EID = "cv_zefier"
GID = "gap_zefier_dividend_1_73m_guaranteed_debt_17_82m_fva_24_01m_l5"
CID = "comm_zefier_jr2025_dividend_1_73m"
LID = "lb_zefier_dividend_1_73m_fva_24_01m_guaranteed_17_82m_l5"


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
        "source_id": "src_zefier_jr2025_official",
        "title": "Zefier cv jaarrekening 2025 (VKT-inb / official jaarverslag bijlage)",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/69bd2442316b81d50017e484_Bijlage%202-jaarrekening%202025.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1795; KBO 0680.832.904; VKT-inb 25p; Grant Thornton / Elie Janssens; assets 39932242 equity 20276744 debt 19655498 FVA 24009023 dividend 1734822 VTE 1.8",
    },
    {
        "source_id": "src_zefier_jv2025_site",
        "title": "Zefier Jaarverslag 2025 (achtste boekjaar) — official site",
        "url": "https://jaarverslag.zefier.be/2024",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1795; 160 vennoten; 121 windturbines 365.63 MW; 72408 solar 20897.71 kWp; guaranteed debt narrative",
    },
    {
        "source_id": "src_zefier_totaal_vennoten_2025",
        "title": "Zefier Resultaten per rekeningsector en per vennoot boekjaar 2025 (Totaal)",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/699c52d6eef8e193e4cf50de_totaal_boekjaar2025.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1795; Totaal dividend -1734821.79 matches JR; municipal matrix",
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
    "tick1795 leftover residual IGS dual of mined VL cities after AGB/NSZ/Dijk92/FARO/Vivalto-holding closed; "
    "KBO 0680.832.904 Actief; CV sinds 01.01.2024; zetel Koning Albert II-laan 37 1030 Schaarbeek; 160 vennoten; "
    "official JR2025 VKT-inb live; sourced euros assets 39932242 equity 20276744 debt 19655498 FVA 24009023 "
    "LT recv 14493895 cash 145654 fin opbr 3150279 staff 434044 VTE 1.8 pnl 2212031 dividend 1734822 "
    "gewaarborgde schuld BE overheid 17818678; FOI ready; NOT every-10 (next 1800)"
)
if not any(r.get("entity_id") == EID for r in rows):
    rows.append(
        {
            "entity_id": EID,
            "name_nl": "Zefier cv (leftover IGS / gemeentelijke hernieuwbare-energie coöperatie van mined Vlaamse gemeenten; NOT Fluvius / Publi-T / Publigas / Vivalto)",
            "name_fr": "Zefier SC (IGS residuel / cooperative energie renouvelable des communes flamandes)",
            "name_en": "Zefier CV leftover municipal renewable-energy cooperative IGS of mined Flemish municipalities",
            "level": "other",
            "parent_id": "sec_flanders",
            "community_language": "nl",
            "website": "https://www.zefier.be",
            "foi_email": "info@zefier.be",
            "foi_postal": "Koning Albert II-laan 37 1030 Schaarbeek",
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
    ("bud_zefier_assets_2025", 39932242, "Assets YE2025 39932242; tick1795"),
    ("bud_zefier_equity_2025", 20276744, "Equity 20276744; tick1795"),
    ("bud_zefier_debt_2025", 19655498, "Debt 19655498; tick1795"),
    ("bud_zefier_fva_2025", 24009023, "FVA participaties 24009023 flat; tick1795"),
    ("bud_zefier_lt_recv_2025", 14493895, "Overige vorderingen LT 14493895; tick1795"),
    ("bud_zefier_st_recv_2025", 1211693, "Overige vorderingen ST 1211693 JUMP; tick1795"),
    ("bud_zefier_cash_2025", 145654, "Liquide middelen 145654; tick1795"),
    ("bud_zefier_bruto_2025", -80969, "Brutomarge NEG -80969; tick1795"),
    ("bud_zefier_staff_2025", 434044, "Personeelskosten 434044 / VTE 1.8; tick1795"),
    ("bud_zefier_expl_2025", -519504, "Bedrijfsverlies -519504; tick1795"),
    ("bud_zefier_fin_opbr_2025", 3150279, "Financiele opbrengsten 3150279; tick1795"),
    ("bud_zefier_fin_kosten_2025", 404511, "Financiele kosten 404511; tick1795"),
    ("bud_zefier_pnl_2025", 2212031, "PnL na belasting 2212031; tick1795"),
    ("bud_zefier_dividend_2025", 1734822, "Uit te keren winst / vergoeding inbreng 1734822 naar 160 gemeenten; tick1795"),
    ("bud_zefier_guaranteed_debt_2025", 17818678, "Door BE overheidsinstellingen gewaarborgde schulden 17818678; tick1795"),
    ("bud_zefier_st_other_loans_2025", 8980000, "Overige leningen ST 8980000 (thesaurie/cashpool class); tick1795"),
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
            "source_id": "src_zefier_jr2025_official",
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
            "title": "Zefier JR2025 leftover IGS dual (dividend 1.73m / FVA 24.01m / guaranteed debt 17.82m)",
            "entity_id": EID,
            "beneficiary": "160 Vlaamse gemeenten-vennoten / hernieuwbare energie projectvennootschappen",
            "legal_basis": "WVV CV; Bestuursdecreet openbaarheid; municipal shareholding dual",
            "decision_date": "2026-06-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "1734822",
            "cash_by_year": "2025:1734822",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/69bd2442316b81d50017e484_Bijlage%202-jaarrekening%202025.pdf",
            "stated_goal": "Local leftover IGS renewable co-op map — dividend 1.73m to cities; FOI guarantee matrix",
            "cut_option": "Publish per-gemeente guarantee schedule + thesauriebewijzen outstanding + FVA mark-to-market vs flat 24.01m",
            "source_id": "src_zefier_jr2025_official",
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>JR2025_L5",
            "notes": "tick1795; YE2025; assets 39932242 equity 20276744 debt 19655498 FVA 24009023 pnl 2212031 dividend 1734822 guaranteed 17818678 VTE 1.8; 160 vennoten; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; not TE-additive of 348bn",
        }
    )
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
if not any(r.get("item_id") == LID for r in rows):
    rows.append(
        {
            "item_id": LID,
            "name": "Zefier 2025: dividend 1.73m / FVA 24.01m / guaranteed debt 17.82m (municipal renewable co-op dual)",
            "level": "L5",
            "type": "igs_energy_coop_dual",
            "hierarchy_path": "Vlaanderen>IGS>Zefier",
            "annual_cost_eur": "1734822",
            "total_cost_eur": "17818678",
            "tco_notes": "Envelope=dividend 1734822 to 160 cities; FVA 24009023 flat; municipal-guaranteed debt 17818678; assets 39932242; PnL 2212031; staff 434044 VTE 1.8; not pure waste — opacity on guarantee matrix + thesaurie",
            "confidence": "strong",
            "source_id": "src_zefier_jr2025_official",
            "beneficiaries": "160 VL municipalities + EGPF/W4F/Zo-Fier/Portfineco/Storm projectcos",
            "stated_goal": "Municipal renewable production shareholding via tracking sectors",
            "measured_outcome": "121 turbines 365.63 MW + 72408 panels 20.9 MWp; dividend 1.73m YE2025",
            "absurdity_score": "4",
            "cost_score": "5",
            "difficulty": "6",
            "priority_index": "4.8",
            "cut_proposal": "FOI full municipal guarantee schedule + outstanding commercial paper + why FVA book flat while W4F equity alone 48.2m at 27pct",
            "status": "open",
            "struck_reason": "",
            "notes": "tick1795 leftover IGS dual; strong JR2025; not TE-additive; not pure-waste top10",
        }
    )
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
if not any(r.get("gap_id") == GID for r in rows):
    rows.append(
        {
            "gap_id": GID,
            "hierarchy_path": "Vlaanderen>IGS>Zefier>JR2025_L5",
            "entity_id": EID,
            "what_is_missing": "Per-gemeente garantie-/borgstellingsmatrix achter door BE overheidsinstellingen gewaarborgde schulden 17818678; outstanding thesauriebewijzen + cashpool debet 8980000 class; FVA 24009023 book vs underlying (W4F 27.09pct equity 48.2m / Zo-Fier 48.49pct / EGPF 24.42pct / Portfineco 50pct); LT overige vorderingen 14493895 tegenpartijen; presentiegelden bestuurders exact 2025",
            "why_it_matters": "Municipal renewable co-op with 1.73m dividend to 160 cities sits on 17.82m publicly guaranteed debt and flat 24.01m FVA — classic dual residual opacity after Vivalto holding closed",
            "priority": "8",
            "recipient_body": "Zefier cv",
            "recipient_email": "info@zefier.be",
            "recipient_postal": "Koning Albert II-laan 37 1030 Schaarbeek",
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
            "notes": "tick1795; human-send only; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403",
        }
    )
write("foi_queue.csv", fields, rows)
print("foi_queue", len(rows))

fields, rows = read("research_queue.csv")
for r in rows:
    if r.get("task_id") == "rq_1795":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = NOW
        r["notes"] = "tick1795 Zefier cv leftover IGS; KBO 0680.832.904; JR2025 assets 39932242 dividend 1734822 guaranteed 17818678; FOI ready; every-10 1800"
        r["blocked_gap_id"] = GID
if not any(r.get("task_id") == "rq_1796" for r in rows):
    rows.append(
        {
            "task_id": "rq_1796",
            "title": "Leftover dual residual hole-fill after Zefier (AGB/NSZ/Bosgroep/FARO/HVZ-if-2025/IGS)",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "Belgique>LeftoverDual>Residual",
            "entity_id": "",
            "instructions": "Tick 1796 after 1795 Zefier. Prefer leftover AGB/APB of mined cities if PDF live, else Bosgroep / other IOED / Dijk92 if CDN 200 / FARO NBB YE2025 if live / other HVZ if official JR2025 euros newly live / other IGS. Skip already-done. Next every-10 1800.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick1795; NEXT residual dual; every-10 1800",
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
        r["last_unit_id"] = "rq_1795"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = (
            "tick1795 leftover Zefier cv IGS dual; KBO 0680.832.904; JR2025 assets 39932242 equity 20276744 debt 19655498 "
            "FVA 24009023 dividend 1734822 guaranteed 17818678 VTE 1.8 pnl 2212031; FOI guarantee/FVA; AGB Bornem JR2024; "
            "NSZ/Dijk92/APEFE still 403; Vivalto holding list closed; NOT every-10 (next 1800); next rq_1796 residual dual; continuous hole_fill"
        )
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE")
