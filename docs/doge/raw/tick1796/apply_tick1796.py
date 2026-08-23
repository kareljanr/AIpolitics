import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
DATA = Path(r"docs/doge/data")
NOW = "2026-08-25T01:35:00Z"
TICK = 1796
EID = "nv_zofier"
GID = "gap_zofier_omzet_2_48m_loss_0_78m_lt_loans_20_96m_l5"
CID = "comm_zofier_jr2025_omzet_2_48m"
LID = "lb_zofier_omzet_2_48m_loss_0_78m_lt_loans_20_96m_l5"
SRC = "src_zofier_jr2025_nbb"


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
        "title": "Zo-Fier NV NBB VOL-kap YE2025 deposit 2026-00135547",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00135547.pdf",
        "publisher": "NBB / Zo-Fier NV",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1796; KBO 0761.723.974; AV 18.05.2026; KPMG/Jorion opinion zonder voorbehoud; assets 30973170 omzet 2478871 pnl -776843 LT loans 20957723; Zefier dual 48.49pct",
    },
    {
        "source_id": "src_zofier_kbo",
        "title": "KBO Zo-Fier NV 0761.723.974",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0761723974",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1796; NV; zetel Koning Albert II-laan 7 1210 Sint-Joost-ten-Node",
    },
    {
        "source_id": "src_zofier_zefier_sector_2025",
        "title": "Zefier rekeningsector Zo-Fier per vennoot boekjaar 2025",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/698ee989aea7b008cffe5c24_Zo-Fier%20nv.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1796; 4 gemeenten Eeklo/Evergem/Gent/Halle; sector dividend 60703; dual residual after Zefier tick1795",
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
    "tick1796 leftover Zefier dual renewable projectco after Zefier cv 1795; KBO 0761.723.974 Actief; NV; "
    "official NBB VOL-kap YE2025 deposit 2026-00135547 CDN 200 46p; AV 18.05.2026; KPMG/Axel Jorion oordeel zonder voorbehoud; "
    "moeder Zefier 48.49pct; 4 gemeenten Eeklo/Evergem/Gent/Halle; sourced euros assets 30973170 equity 8465583 debt 22415804 "
    "MVA 29273427 omzet 2478871 opbr 2667483 diensten 771997 afschr 1553685 expl 282471 fin kosten 1065371 pnl -776843 "
    "LT overige leningen 20957723 cash 0 VTE 0; FOI ready; NOT every-10 (next 1800)"
)
if not any(r.get("entity_id") == EID for r in rows):
    rows.append(
        {
            "entity_id": EID,
            "name_nl": "Zo-Fier NV (leftover Zefier dual / hernieuwbare projectvennootschap; NOT Wind4Flanders / EGPF / Portfineco)",
            "name_fr": "Zo-Fier SA (dual Zefier residuel / projet renouvelable)",
            "name_en": "Zo-Fier NV leftover Zefier dual renewable project company",
            "level": "other",
            "parent_id": "cv_zefier",
            "community_language": "nl",
            "website": "https://jaarverslag.zefier.be/overlay-pages/zo-fier-nv",
            "foi_email": "info@zefier.be",
            "foi_postal": "Koning Albert II-laan 7 1210 Sint-Joost-ten-Node",
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
    ("bud_zofier_assets_2025", 30973170, "Assets YE2025 30973170; tick1796"),
    ("bud_zofier_equity_2025", 8465583, "Equity 8465583 DROP; tick1796"),
    ("bud_zofier_debt_2025", 22415804, "Debt 22415804; tick1796"),
    ("bud_zofier_mva_2025", 29273427, "MVA installaties 29273427; tick1796"),
    ("bud_zofier_omzet_2025", 2478871, "Omzet GSC+elektriciteit 2478871; tick1796"),
    ("bud_zofier_opbr_2025", 2667483, "Bedrijfsopbrengsten 2667483; tick1796"),
    ("bud_zofier_diensten_2025", 771997, "Diensten diverse goederen 771997; tick1796"),
    ("bud_zofier_afschr_2025", 1553685, "Afschrijvingen 1553685; tick1796"),
    ("bud_zofier_expl_2025", 282471, "Bedrijfswinst 282471 FLIP; tick1796"),
    ("bud_zofier_fin_kosten_2025", 1065371, "Financiele kosten 1065371; tick1796"),
    ("bud_zofier_pnl_2025", -776843, "PnL LOSS -776843; tick1796"),
    ("bud_zofier_lt_loans_2025", 20957723, "Overige leningen LT 20957723 (shareholder/Zefier class); tick1796"),
    ("bud_zofier_st_other_2025", 1091775, "Overige schulden ST 1091775; tick1796"),
    ("bud_zofier_trade_st_2025", 216190, "Handelsschulden ST 216190 DROP from 4703412; tick1796"),
    ("bud_zofier_prov_2025", 91783, "Voorzieningen 91783 JUMP; tick1796"),
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
            "title": "Zo-Fier JR2025 leftover Zefier dual (omzet 2.48m / loss 0.78m / LT loans 20.96m)",
            "entity_id": EID,
            "beneficiary": "Zefier / 4 gemeenten Eeklo Evergem Gent Halle / Luminus PPA",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal renewable dual via Zefier",
            "decision_date": "2026-05-18",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "2478871",
            "cash_by_year": "2025:2478871",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00135547.pdf",
            "stated_goal": "Local leftover Zefier projectco map — omzet 2.48m / loss 0.78m / FOI LT loans",
            "cut_option": "Publish LT loan counterparties rates + empty VTE ops model + cash zero path + Luminus PPA euros",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>ZoFier>JR2025_L5",
            "notes": "tick1796; YE2025; assets 30973170 equity 8465583 debt 22415804 omzet 2478871 pnl -776843 LT loans 20957723 VTE 0 cash 0; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; not TE-additive of 348bn",
        }
    )
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
if not any(r.get("item_id") == LID for r in rows):
    rows.append(
        {
            "item_id": LID,
            "name": "Zo-Fier 2025: omzet 2.48m / loss 0.78m / LT loans 20.96m (Zefier dual projectco)",
            "level": "L5",
            "type": "igs_energy_project_dual",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>ZoFier",
            "annual_cost_eur": "2478871",
            "total_cost_eur": "20957723",
            "tco_notes": "Envelope=omzet 2478871; loss 776843; LT other loans 20957723 shareholder/Zefier class; MVA 29273427; cash 0 VTE 0 shell; not pure waste — opacity on loan matrix + ops model",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Zefier 48.49pct + 4 municipalities + Luminus offtake",
            "stated_goal": "Renewable electricity + GSC sales via municipal co-op stack",
            "measured_outcome": "Omzet JUMP 2.48m; expl flip +0.28m; still net LOSS -0.78m on 21m LT loans",
            "absurdity_score": "5",
            "cost_score": "5",
            "difficulty": "6",
            "priority_index": "5.2",
            "cut_proposal": "FOI LT loan lenders/rates + why VTE 0 with 0.77m diensten + cash collapse + Luminus PPA terms",
            "status": "open",
            "struck_reason": "",
            "notes": "tick1796 leftover Zefier dual; strong NBB; not TE-additive; not pure-waste top10",
        }
    )
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
if not any(r.get("gap_id") == GID for r in rows):
    rows.append(
        {
            "gap_id": GID,
            "hierarchy_path": "Vlaanderen>IGS>Zefier>ZoFier>JR2025_L5",
            "entity_id": EID,
            "what_is_missing": "Tegenpartijen/voorwaarden/rente overige leningen LT 20957723 (Zefier/gemeenten vs bank); cash 0 path vs ST overige 1091775; VTE 0 ops model vs diensten 771997; Luminus PPA 2026 euros; uitsplitsing omzet GSC vs elektriciteit; AV 18.05.2026 niet-gepersonaliseerd",
            "why_it_matters": "Zefier dual projectco with 2.48m omzet still deepens LOSS to 0.78m on 21m LT shareholder-class loans and zero cash/VTE — residual opacity after Zefier parent tick1795",
            "priority": "8",
            "recipient_body": "Zo-Fier NV / Zefier cv",
            "recipient_email": "info@zefier.be",
            "recipient_postal": "Koning Albert II-laan 7 1210 Sint-Joost-ten-Node",
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
            "notes": "tick1796; human-send only; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403",
        }
    )
write("foi_queue.csv", fields, rows)
print("foi_queue", len(rows))

fields, rows = read("research_queue.csv")
for r in rows:
    if r.get("task_id") == "rq_1796":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = NOW
        r["notes"] = "tick1796 Zo-Fier NV Zefier dual; KBO 0761.723.974; NBB 2026-00135547; omzet 2478871 pnl -776843 LT loans 20957723; FOI ready; every-10 1800"
        r["blocked_gap_id"] = GID
if not any(r.get("task_id") == "rq_1797" for r in rows):
    rows.append(
        {
            "task_id": "rq_1797",
            "title": "Leftover dual residual hole-fill after Zo-Fier (AGB/NSZ/Bosgroep/FARO/W4F-if-200/IGS)",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "Belgique>LeftoverDual>Residual",
            "entity_id": "",
            "instructions": "Tick 1797 after 1796 Zo-Fier. Prefer leftover AGB/APB of mined cities if PDF live, else Bosgroep / IOED / Dijk92 if CDN 200 / FARO NBB YE2025 if live / Wind4Flanders or Portfineco if CDN 200 / other HVZ if JR2025 euros newly live / other IGS. Skip already-done. Next every-10 1800.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick1796; NEXT residual dual; every-10 1800",
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
        r["last_unit_id"] = "rq_1796"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = (
            "tick1796 leftover Zo-Fier NV Zefier dual; KBO 0761.723.974; NBB 2026-00135547; assets 30973170 omzet 2478871 "
            "pnl -776843 LT loans 20957723 cash 0 VTE 0; FOI loans/PPA; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; "
            "NOT every-10 (next 1800); next rq_1797 residual dual; continuous hole_fill"
        )
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE")
