import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
DATA = Path(r"docs/doge/data")
NOW = "2026-08-25T02:35:00Z"
TICK = 1799
EID = "nv_egpf"
GID = "gap_egpf_omzet_4_44m_loss_0_88m_mva_15_02m_prov_2_12m_l5"
CID = "comm_egpf_jr2025_omzet_4_44m"
LID = "lb_egpf_omzet_4_44m_loss_0_88m_mva_15_02m_l5"
SRC = "src_egpf_jr2025_nbb"


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
        "title": "Electrabel Green Projects Flanders NV NBB VOL-kap YE2025 deposit 2026-00206406",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00206406.pdf",
        "publisher": "NBB / EGPF NV",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1799; KBO 0465.399.763; AV 16.06.2026; Deloitte/Van Baelen oordeel zonder voorbehoud; assets 18629714 omzet 4441174 pnl -881205 MVA 15023352; Zefier dual 24.42pct; closes Zefier CDN sister batch",
    },
    {
        "source_id": "src_egpf_kbo",
        "title": "KBO Electrabel Green Projects Flanders NV 0465.399.763",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465399763",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1799; NV; zetel Simon Bolivarlaan 36 1000 Brussel",
    },
    {
        "source_id": "src_egpf_zefier_sector_2025",
        "title": "Zefier rekeningsector EGPF per vennoot boekjaar 2025",
        "url": "https://cdn.prod.website-files.com/67b43e8425285b6d3a0f29b9/698ee9881305252ad09b14ac_EGPF.pdf",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1799; dual residual after PortFineco 1798; Zefier sector A",
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
    "tick1799 leftover Zefier dual renewable opco after PortFineco 1798; KBO 0465.399.763 Actief; NV; "
    "official NBB VOL-kap YE2025 deposit 2026-00206406 CDN 200 40p; AV 16.06.2026; Deloitte/Jo Van Baelen oordeel zonder voorbehoud; "
    "Zefier 24.42pct; closes deferred Zefier CDN sister batch Zo-Fier/W4F/PortFineco/EGPF; "
    "sourced euros assets 18629714 equity 15408750 debt 1102764 MVA 15023352 omzet 4441174 "
    "(elektriciteit 4253208 GSC 187965) diensten 2836792 afschr 2650090 expl -934776 pnl -881205 "
    "voorzieningen 2118200 ST other recv JUMP 2209362 cash 0 VTE 0 dividend 0; FOI ready; NOT every-10 (next 1800 MUST)"
)
if not any(r.get("entity_id") == EID for r in rows):
    rows.append(
        {
            "entity_id": EID,
            "name_nl": "Electrabel Green Projects Flanders NV / EGPF (leftover Zefier dual / wind opco; NOT W4F / Zo-Fier / PortFineco)",
            "name_fr": "Electrabel Green Projects Flanders SA (dual Zefier residuel / opco eolien)",
            "name_en": "EGPF NV leftover Zefier dual wind operating company",
            "level": "other",
            "parent_id": "cv_zefier",
            "community_language": "nl",
            "website": "https://jaarverslag.zefier.be/overlay-pages/electrabel-green-projects-flanders-nv",
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
    ("bud_egpf_assets_2025", 18629714, "Assets YE2025 18629714; tick1799"),
    ("bud_egpf_equity_2025", 15408750, "Equity 15408750 DROP; tick1799"),
    ("bud_egpf_debt_2025", 1102764, "Debt 1102764; tick1799"),
    ("bud_egpf_mva_2025", 15023352, "MVA installaties 15023352 DROP; tick1799"),
    ("bud_egpf_omzet_2025", 4441174, "Omzet 4441174 (elek 4253208 GSC 187965); tick1799"),
    ("bud_egpf_opbr_2025", 4485381, "Bedrijfsopbrengsten 4485381; tick1799"),
    ("bud_egpf_diensten_2025", 2836792, "Diensten diverse goederen 2836792; tick1799"),
    ("bud_egpf_afschr_2025", 2650090, "Afschrijvingen 2650090; tick1799"),
    ("bud_egpf_expl_2025", -934776, "Bedrijfsverlies -934776 deepening; tick1799"),
    ("bud_egpf_pnl_2025", -881205, "PnL LOSS -881205; tick1799"),
    ("bud_egpf_prov_2025", 2118200, "Voorzieningen overige risico 2118200; tick1799"),
    ("bud_egpf_st_recv_other_2025", 2209362, "Overige vorderingen ST 2209362 JUMP from 401606; tick1799"),
    ("bud_egpf_trade_st_2025", 1015044, "Handelsschulden ST 1015044 JUMP; tick1799"),
    ("bud_egpf_kapsubs_2025", 37058, "Kapitaalsubsidies 37058 DROP; tick1799"),
    ("bud_egpf_commissaris_2025", 13923, "Bezoldiging commissaris Deloitte 13923; tick1799"),
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
            "title": "EGPF JR2025 leftover Zefier dual (omzet 4.44m / loss 0.88m / MVA 15.02m / prov 2.12m)",
            "entity_id": EID,
            "beneficiary": "Zefier 24.42pct / ENGIE-Electrabel / municipal sector A / green electricity buyers",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal renewable dual via Zefier",
            "decision_date": "2026-06-16",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "4441174",
            "cash_by_year": "2025:4441174",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00206406.pdf",
            "stated_goal": "Local leftover Zefier EGPF wind opco map — omzet 4.44m / loss 0.88m; FOI prov+recv",
            "cut_option": "Publish voorzieningen 2.12m composition + ST other recv JUMP 2.21m + VTE0 ops model vs diensten 2.84m",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>EGPF>JR2025_L5",
            "notes": "tick1799; YE2025; assets 18629714 omzet 4441174 pnl -881205 MVA 15023352 prov 2118200 dividend 0 cash 0 VTE 0; closes Zefier CDN sister batch; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; not TE-additive of 348bn",
        }
    )
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
if not any(r.get("item_id") == LID for r in rows):
    rows.append(
        {
            "item_id": LID,
            "name": "EGPF 2025: omzet 4.44m / loss 0.88m / MVA 15.02m / provisions 2.12m (Zefier dual wind opco)",
            "level": "L5",
            "type": "igs_energy_opco_dual",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>EGPF",
            "annual_cost_eur": "4441174",
            "total_cost_eur": "15023352",
            "tco_notes": "Envelope=omzet 4441174; loss deepening -881205; MVA turbines 15023352; voorzieningen 2118200; diensten 2836792 VTE 0; cash 0; dividend 0 (prior 1.29m); not pure waste — opacity on loss path + provisions",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Zefier municipalities 24.42pct + ENGIE Electrabel stack",
            "stated_goal": "Operate wind/GSC assets for municipal co-op sector A via Zefier",
            "measured_outcome": "Omzet DROP; expl loss deepens to -0.93m; no dividend YE2025",
            "absurdity_score": "5",
            "cost_score": "5",
            "difficulty": "6",
            "priority_index": "5.2",
            "cut_proposal": "FOI provisions 2.12m + ST recv JUMP 2.21m + VTE0 vs diensten 2.84m + GSC vs power price path",
            "status": "open",
            "struck_reason": "",
            "notes": "tick1799 leftover Zefier dual; strong NBB; closes CDN sister batch; not TE-additive; not pure-waste top10",
        }
    )
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
if not any(r.get("gap_id") == GID for r in rows):
    rows.append(
        {
            "gap_id": GID,
            "hierarchy_path": "Vlaanderen>IGS>Zefier>EGPF>JR2025_L5",
            "entity_id": EID,
            "what_is_missing": "Samenstelling voorzieningen overige risico 2118200; tegenpartijen ST overige vorderingen JUMP 2209362; VTE 0 ops model vs diensten 2836792; oorzaken omzet DROP + loss deepening vs prior dividend 1288089; AV 16.06.2026 niet-gepersonaliseerd",
            "why_it_matters": "Zefier dual wind opco with 4.44m omzet still deepens LOSS to 0.88m, holds 2.12m provisions, zero cash/VTE — residual opacity closing Zefier CDN sister batch",
            "priority": "8",
            "recipient_body": "Electrabel Green Projects Flanders NV / Zefier cv",
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
            "notes": "tick1799; human-send only; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; closes Zo-Fier/W4F/PortFineco/EGPF CDN batch",
        }
    )
write("foi_queue.csv", fields, rows)
print("foi_queue", len(rows))

fields, rows = read("research_queue.csv")
for r in rows:
    if r.get("task_id") == "rq_1799":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = NOW
        r["notes"] = "tick1799 EGPF NV Zefier dual; KBO 0465.399.763; NBB 2026-00206406; omzet 4441174 pnl -881205 MVA 15023352; FOI ready; closes Zefier CDN batch; every-10 MUST 1800"
        r["blocked_gap_id"] = GID
if not any(r.get("task_id") == "rq_1800" for r in rows):
    rows.append(
        {
            "task_id": "rq_1800",
            "title": "EVERY-10 progress coverage % + waste top10 (MUST)",
            "sprint": "hole_fill",
            "priority": "9",
            "status": "open",
            "hierarchy_target": "Belgique>Progress>Every10",
            "entity_id": "",
            "instructions": "Tick 1800 MUST every-10: refresh progress_every_10_ticks.md (layers A-E % of EUR347.956bn TE) and doge_waste_top10_current.md (top 10 by priority_index). Note Zefier dual continuum Zo-Fier/W4F/PortFineco/EGPF. Then spawn rq_1801 residual dual. Skip inventing euros.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick1799; MUST every-10 progress; next residual after 1800",
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
        r["last_unit_id"] = "rq_1799"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = (
            "tick1799 leftover EGPF NV Zefier dual; KBO 0465.399.763; NBB 2026-00206406; assets 18629714 omzet 4441174 "
            "pnl -881205 MVA 15023352 prov 2118200 cash 0 VTE 0 dividend 0; FOI prov/recv; closes Zefier CDN sister batch "
            "Zo-Fier/W4F/PortFineco/EGPF; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; next rq_1800 MUST every-10; continuous hole_fill"
        )
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE")
