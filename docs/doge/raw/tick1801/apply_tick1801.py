import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
DATA = Path(r"docs/doge/data")
NOW = "2026-08-25T03:15:00Z"
TICK = 1801
EID = "nv_storm_geraardsbergen"
GID = "gap_stormg_bruto_0_46m_loss_0_33m_dividend_0_15m_debt_3_42m_l5"
CID = "comm_stormg_jr2025_bruto_0_46m"
LID = "lb_stormg_bruto_0_46m_loss_0_33m_dividend_0_15m_l5"
SRC = "src_stormg_jr2025_nbb"


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
        "title": "Storm Geraardsbergen NV NBB VKT-kap YE2025 deposit 2026-00155792",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00155792.pdf",
        "publisher": "NBB / Storm Geraardsbergen NV",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1801; KBO 0839.404.940; AV 15.05.2026; Finvision/Nijs oordeel zonder voorbehoud; assets 5727870 bruto 462689 pnl -325767 dividend 150000; Zefier dual 20pct",
    },
    {
        "source_id": "src_stormg_kbo",
        "title": "KBO Storm Geraardsbergen NV 0839.404.940",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0839404940",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1801; NV; zetel Borsbeeksebrug 22 2600 Berchem; Ann Panis schepen Geraardsbergen bestuurder",
    },
    {
        "source_id": "src_stormg_zefier_sector_2025",
        "title": "Zefier rekeningsector Storm Geraardsbergen per vennoot boekjaar 2025",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/698ee98841ee0ef8c001f19f_Storm%20Geraards%C2%AD%C2%ADbergen%20nv.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1801; leftover Zefier sector J after EGPF batch; municipal dual Geraardsbergen",
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
    "tick1801 leftover Zefier dual wind projectco after EGPF/every-10; KBO 0839.404.940 Actief; NV; "
    "official NBB VKT-kap YE2025 deposit 2026-00155792 CDN 200 23p; AV 15.05.2026; Finvision/Karel Nijs oordeel zonder voorbehoud; "
    "Zefier 20pct; Storm Management gedelegeerd; Ann Panis (schepen Geraardsbergen) bestuurder; "
    "sourced euros assets 5727870 equity 2310634 debt 3417236 MVA 4959582 bruto 462689 DROP from 1869314 "
    "afschr 393779 expl 67496 fin kosten 117637 pnl -325767 tax 275625 dividend 150000 despite loss "
    "onttrekking equity 475767 cash 462312 JUMP LT bank 2258524 other loans 623496 gage handelsfonds 2432889; FOI ready; NOT every-10 (next 1810)"
)
if not any(r.get("entity_id") == EID for r in rows):
    rows.append(
        {
            "entity_id": EID,
            "name_nl": "Storm Geraardsbergen NV (leftover Zefier dual / wind projectco; NOT EGPF / W4F / Zo-Fier / PortFineco / SPS FIN)",
            "name_fr": "Storm Geraardsbergen SA (dual Zefier residuel / projet eolien)",
            "name_en": "Storm Geraardsbergen NV leftover Zefier dual wind project company",
            "level": "other",
            "parent_id": "cv_zefier",
            "community_language": "nl",
            "website": "https://jaarverslag.zefier.be/overlay-pages/storm-geraardsbergen",
            "foi_email": "info@zefier.be",
            "foi_postal": "Borsbeeksebrug 22 2600 Berchem (Antwerpen)",
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
    ("bud_stormg_assets_2025", 5727870, "Assets YE2025 5727870; tick1801"),
    ("bud_stormg_equity_2025", 2310634, "Equity 2310634 DROP; tick1801"),
    ("bud_stormg_debt_2025", 3417236, "Debt 3417236; tick1801"),
    ("bud_stormg_mva_2025", 4959582, "MVA installaties 4959582; tick1801"),
    ("bud_stormg_bruto_2025", 462689, "Brutomarge 462689 DROP from 1869314; tick1801"),
    ("bud_stormg_afschr_2025", 393779, "Afschrijvingen 393779; tick1801"),
    ("bud_stormg_expl_2025", 67496, "Bedrijfswinst 67496 DROP; tick1801"),
    ("bud_stormg_fin_kosten_2025", 117637, "Financiele kosten 117637; tick1801"),
    ("bud_stormg_tax_2025", 275625, "Belastingen 275625 despite pre-tax loss; tick1801"),
    ("bud_stormg_pnl_2025", -325767, "PnL LOSS -325767 FLIP from +962589; tick1801"),
    ("bud_stormg_dividend_2025", 150000, "Dividend 150000 despite loss (equity draw 475767); tick1801"),
    ("bud_stormg_cash_2025", 462312, "Cash 462312 JUMP; tick1801"),
    ("bud_stormg_lt_bank_2025", 2258524, "Kredietinstellingen LT 2258524; tick1801"),
    ("bud_stormg_lt_other_loans_2025", 623496, "Overige leningen LT 623496; tick1801"),
    ("bud_stormg_gage_2025", 2432889, "Gage handelsfonds max 2432889; tick1801"),
    ("bud_stormg_commissaris_2025", 4400, "Bezoldiging commissaris Finvision 4400 excl btw; tick1801"),
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
            "title": "Storm Geraardsbergen JR2025 leftover Zefier dual (bruto 0.46m / loss 0.33m / dividend 0.15m)",
            "entity_id": EID,
            "beneficiary": "Zefier 20pct / Storm Management / Stad Geraardsbergen dual / wind offtake",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal renewable dual via Zefier sector J",
            "decision_date": "2026-05-15",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "462689",
            "cash_by_year": "2025:462689",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00155792.pdf",
            "stated_goal": "Local leftover Zefier Storm Geraardsbergen wind map — bruto DROP / loss+dividend FOI",
            "cut_option": "Publish omzet empty split + why dividend 150k on loss 326k + tax 276k on pre-tax loss + other loans 623k",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>StormGeraardsbergen>JR2025_L5",
            "notes": "tick1801; YE2025; assets 5727870 bruto 462689 pnl -325767 dividend 150000 tax 275625 debt 3417236; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; SPS FIN CDN live deferred; not TE-additive of 348bn",
        }
    )
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
if not any(r.get("item_id") == LID for r in rows):
    rows.append(
        {
            "item_id": LID,
            "name": "Storm Geraardsbergen 2025: bruto 0.46m / loss 0.33m / dividend 0.15m despite loss (Zefier dual)",
            "level": "L5",
            "type": "igs_energy_project_dual",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>StormGeraardsbergen",
            "annual_cost_eur": "462689",
            "total_cost_eur": "3417236",
            "tco_notes": "Envelope=bruto 462689 DROP from 1.87m; PnL flip -325767; dividend 150000 + equity draw 475767; tax 275625 on pre-tax loss; debt 3.42m gage 2.43m; not pure waste — opacity on dividend-while-loss + empty omzet",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Zefier 20pct + Storm + Geraardsbergen municipal dual",
            "stated_goal": "Local wind project via Zefier sector J / Storm",
            "measured_outcome": "Bruto crater; loss flip; still pays 150k dividend",
            "absurdity_score": "6",
            "cost_score": "3.5",
            "difficulty": "5",
            "priority_index": "4.7",
            "cut_proposal": "FOI empty omzet + dividend-on-loss rationale + tax 276k path + LT other loans 623k counterparties",
            "status": "open",
            "struck_reason": "",
            "notes": "tick1801 leftover Zefier dual; strong NBB; not TE-additive; not pure-waste top10",
        }
    )
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
if not any(r.get("gap_id") == GID for r in rows):
    rows.append(
        {
            "gap_id": GID,
            "hierarchy_path": "Vlaanderen>IGS>Zefier>StormGeraardsbergen>JR2025_L5",
            "entity_id": EID,
            "what_is_missing": "Omzet empty (VKT) vs bruto DROP 1869314 naar 462689; rechtvaardiging dividend 150000 + equity onttrekking 475767 bij PnL loss 325767; belastingen 275625 bij pre-tax loss 50141; tegenpartijen overige leningen LT 623496; AV 15.05.2026 niet-gepersonaliseerd",
            "why_it_matters": "Zefier dual wind projectco flips to loss 0.33m after bruto crater yet still pays 0.15m dividend and 0.28m tax — residual opacity after EGPF/every-10",
            "priority": "8",
            "recipient_body": "Storm Geraardsbergen NV / Zefier cv / Storm Management NV",
            "recipient_email": "info@zefier.be",
            "recipient_postal": "Borsbeeksebrug 22 2600 Berchem (Antwerpen)",
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
            "notes": "tick1801; human-send only; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; SPS FIN 2026-00305818 live deferred",
        }
    )
write("foi_queue.csv", fields, rows)
print("foi_queue", len(rows))

fields, rows = read("research_queue.csv")
for r in rows:
    if r.get("task_id") == "rq_1801":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = NOW
        r["notes"] = "tick1801 Storm Geraardsbergen NV Zefier dual; KBO 0839.404.940; NBB 2026-00155792; bruto 462689 pnl -325767 dividend 150000; FOI ready; every-10 1810"
        r["blocked_gap_id"] = GID
if not any(r.get("task_id") == "rq_1802" for r in rows):
    rows.append(
        {
            "task_id": "rq_1802",
            "title": "Leftover dual residual hole-fill after StormG (AGB/NSZ/Bosgroep/SPS-FIN-if-200/IGS)",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "Belgique>LeftoverDual>Residual",
            "entity_id": "",
            "instructions": "Tick 1802 after 1801 Storm Geraardsbergen. Prefer leftover AGB/APB of mined cities if PDF live, else Bosgroep / IOED / Dijk92 if CDN 200 / FARO NBB YE2025 if live / SPS FIN 2026-00305818 or Storm Wielsbeke/Zandvliet/Terranova if CDN 200 / other HVZ if JR2025 euros newly live / other IGS. Skip already-done. Next every-10 1810.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick1801; NEXT residual dual; SPS FIN CDN live deferred; every-10 1810",
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
        r["last_unit_id"] = "rq_1801"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = (
            "tick1801 leftover Storm Geraardsbergen NV Zefier dual; KBO 0839.404.940; NBB 2026-00155792; assets 5727870 "
            "bruto 462689 pnl -325767 dividend 150000 tax 275625 debt 3417236; FOI dividend-on-loss; SPS FIN CDN live deferred; "
            "AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; NOT every-10 (next 1810); next rq_1802 residual dual; continuous hole_fill"
        )
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE")
