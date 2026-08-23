import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
DATA = Path(r"docs/doge/data")
NOW = "2026-08-25T02:15:00Z"
TICK = 1798
EID = "nv_portfineco"
GID = "gap_portfineco_fva_3_81m_dividend_0_70m_fin_opbr_drop_2_78m_l5"
CID = "comm_portfineco_jr2025_dividend_0_70m"
LID = "lb_portfineco_fva_3_81m_dividend_0_70m_fin_opbr_drop_l5"
SRC = "src_portfineco_jr2025_nbb"


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
        "title": "PortFineco NV NBB VOL-kap YE2025 deposit 2026-00119667",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00119667.pdf",
        "publisher": "NBB / PortFineco NV",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1798; KBO 0837.729.216; AV 19.05.2026; BDO/Delbeke oordeel zonder voorbehoud; assets 6234606 FVA 3811484 dividend 700000; Zefier 50pct + POAB 50pct",
    },
    {
        "source_id": "src_portfineco_kbo",
        "title": "KBO PortFineco NV 0837.729.216",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0837729216",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1798; NV; zetel Isabellalaan 1 8380 Zeebrugge",
    },
    {
        "source_id": "src_portfineco_zefier_sector_2025",
        "title": "Zefier rekeningsector Portfineco per vennoot boekjaar 2025",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/698ee988f2ea0a3cee10dd77_Portfineco.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1798; dual residual after W4F 1797; Zefier+POAB haven Brugge-Zeebrugge",
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
    "tick1798 leftover Zefier dual renewable harbour holding after W4F 1797; KBO 0837.729.216 Actief; NV; "
    "official NBB VOL-kap YE2025 deposit 2026-00119667 CDN 200 44p; AV 19.05.2026; BDO/Michael Delbeke oordeel zonder voorbehoud; "
    "aandeelhouders Zefier 50pct + Haven van Antwerpen-Brugge POAB 50pct; FVA Libeccio I / Seagull I / ICO Windpark; "
    "sourced euros assets 6234606 equity 5530192 debt 704414 FVA 3811484 cash 2170 DROP ST recv 2415372 "
    "fin opbr 577490 DROP from 2784204 pnl 528902 dividend 700000 diensten 48033 VTE 0; FOI ready; NOT every-10 (next 1800)"
)
if not any(r.get("entity_id") == EID for r in rows):
    rows.append(
        {
            "entity_id": EID,
            "name_nl": "PortFineco NV (leftover Zefier dual / haven Brugge-Zeebrugge hernieuwbare holding; NOT W4F / Zo-Fier / EGPF)",
            "name_fr": "PortFineco SA (dual Zefier residuel / holding renouvelable port Bruges-Zeebrugge)",
            "name_en": "PortFineco NV leftover Zefier dual harbour renewable holding",
            "level": "other",
            "parent_id": "cv_zefier",
            "community_language": "nl",
            "website": "https://jaarverslag.zefier.be/overlay-pages/portfineco-nv",
            "foi_email": "info@zefier.be",
            "foi_postal": "Isabellalaan 1 8380 Zeebrugge",
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
    ("bud_portfineco_assets_2025", 6234606, "Assets YE2025 6234606; tick1798"),
    ("bud_portfineco_equity_2025", 5530192, "Equity 5530192; tick1798"),
    ("bud_portfineco_debt_2025", 704414, "Debt 704414 DROP; tick1798"),
    ("bud_portfineco_fva_2025", 3811484, "FVA deelnemingen Libeccio/Seagull/ICO 3811484 flat; tick1798"),
    ("bud_portfineco_cash_2025", 2170, "Cash 2170 DROP from 30651; tick1798"),
    ("bud_portfineco_st_recv_2025", 2415372, "Overige vorderingen ST 2415372 DROP from 3848602; tick1798"),
    ("bud_portfineco_diensten_2025", 48033, "Diensten diverse goederen 48033; tick1798"),
    ("bud_portfineco_expl_2025", -48218, "Bedrijfsverlies -48218; tick1798"),
    ("bud_portfineco_fin_opbr_2025", 577490, "Financiele opbrengsten 577490 DROP from 2784204; tick1798"),
    ("bud_portfineco_pnl_2025", 528902, "PnL 528902 tax 0; tick1798"),
    ("bud_portfineco_dividend_2025", 700000, "Uit te keren dividend 700000; tick1798"),
    ("bud_portfineco_st_other_2025", 700000, "Overige schulden ST 700000 (=dividend payable); tick1798"),
    ("bud_portfineco_commissaris_2025", 5158, "Bezoldiging commissaris BDO 5158; tick1798"),
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
            "title": "PortFineco JR2025 leftover Zefier+POAB dual (dividend 0.70m / FVA 3.81m / fin opbr DROP 2.78m)",
            "entity_id": EID,
            "beneficiary": "Zefier 50pct / Haven van Antwerpen-Brugge POAB 50pct / Libeccio Seagull ICO wind",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal+port renewable dual via Zefier",
            "decision_date": "2026-05-19",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "700000",
            "cash_by_year": "2025:700000",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00119667.pdf",
            "stated_goal": "Local leftover Zefier/POAB harbour renewable holding — dividend 0.70m; FOI fin opbr DROP",
            "cut_option": "Publish filial dividend DROP path + ST recv counterparties + POAB/Zefier split of 0.70m",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>PortFineco>JR2025_L5",
            "notes": "tick1798; YE2025; assets 6234606 FVA 3811484 pnl 528902 dividend 700000 fin opbr DROP 2784204 to 577490 cash 2170 VTE 0; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; EGPF CDN live deferred; not TE-additive of 348bn",
        }
    )
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
if not any(r.get("item_id") == LID for r in rows):
    rows.append(
        {
            "item_id": LID,
            "name": "PortFineco 2025: FVA 3.81m / dividend 0.70m / fin opbr DROP 2.78m to 0.58m (Zefier+POAB dual)",
            "level": "L5",
            "type": "igs_energy_holding_dual",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>PortFineco",
            "annual_cost_eur": "700000",
            "total_cost_eur": "3811484",
            "tco_notes": "Envelope=dividend 700000; FVA 3811484 in Libeccio/Seagull/ICO; fin opbr DROP 2.78m to 0.58m; cash 2170; VTE 0 shell; 50/50 Zefier+POAB; not pure waste — opacity on filial income collapse",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Zefier municipalities + Haven Antwerpen-Brugge + Eneco project stack",
            "stated_goal": "Harbour renewable project holding Brugge-Zeebrugge via Zefier sector B",
            "measured_outcome": "PnL 0.53m (tax 0); dividend 0.70m; fin income crater vs 2024",
            "absurdity_score": "4",
            "cost_score": "4",
            "difficulty": "5",
            "priority_index": "4.4",
            "cut_proposal": "FOI filial dividend DROP drivers + ST recv 2.42m counterparties + POAB/Zefier dividend split",
            "status": "open",
            "struck_reason": "",
            "notes": "tick1798 leftover Zefier dual; strong NBB; not TE-additive; not pure-waste top10",
        }
    )
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
if not any(r.get("gap_id") == GID for r in rows):
    rows.append(
        {
            "gap_id": GID,
            "hierarchy_path": "Vlaanderen>IGS>Zefier>PortFineco>JR2025_L5",
            "entity_id": EID,
            "what_is_missing": "Oorzaken fin opbr DROP 2784204 naar 577490 (Libeccio/Seagull/ICO dividendmatrix); tegenpartijen ST overige vorderingen 2415372; uitsplitsing dividend 700000 Zefier vs POAB; cash DROP 30651 naar 2170; AV 19.05.2026 niet-gepersonaliseerd",
            "why_it_matters": "Zefier+POAB harbour renewable holding with dividend 0.70m but fin income crater 2.78m to 0.58m and cash near-zero — residual opacity after W4F tick1797",
            "priority": "8",
            "recipient_body": "PortFineco NV / Zefier cv / Haven van Antwerpen-Brugge",
            "recipient_email": "info@zefier.be",
            "recipient_postal": "Isabellalaan 1 8380 Zeebrugge",
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
            "notes": "tick1798; human-send only; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; EGPF 2026-00206406 live deferred",
        }
    )
write("foi_queue.csv", fields, rows)
print("foi_queue", len(rows))

fields, rows = read("research_queue.csv")
for r in rows:
    if r.get("task_id") == "rq_1798":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = NOW
        r["notes"] = "tick1798 PortFineco NV Zefier+POAB dual; KBO 0837.729.216; NBB 2026-00119667; FVA 3811484 dividend 700000 fin opbr DROP; FOI ready; every-10 1800"
        r["blocked_gap_id"] = GID
if not any(r.get("task_id") == "rq_1799" for r in rows):
    rows.append(
        {
            "task_id": "rq_1799",
            "title": "Leftover dual residual hole-fill after PortFineco (AGB/NSZ/Bosgroep/EGPF-if-200/IGS)",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "Belgique>LeftoverDual>Residual",
            "entity_id": "",
            "instructions": "Tick 1799 after 1798 PortFineco. Prefer leftover AGB/APB of mined cities if PDF live, else Bosgroep / IOED / Dijk92 if CDN 200 / FARO NBB YE2025 if live / EGPF 2026-00206406 if unused live / other HVZ if JR2025 euros newly live / other IGS. Skip already-done. Next every-10 MUST 1800.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick1798; NEXT residual dual; EGPF CDN live deferred; every-10 MUST 1800",
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
        r["last_unit_id"] = "rq_1798"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = (
            "tick1798 leftover PortFineco NV Zefier+POAB dual; KBO 0837.729.216; NBB 2026-00119667; assets 6234606 "
            "FVA 3811484 dividend 700000 pnl 528902 fin opbr DROP 2784204 to 577490 cash 2170 VTE 0; FOI filial DROP; "
            "EGPF CDN live deferred; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; NOT every-10 (next 1800 MUST); "
            "next rq_1799 residual dual; continuous hole_fill"
        )
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE")
