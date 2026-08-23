import csv
from pathlib import Path

csv.field_size_limit(10_000_000)
DATA = Path(r"docs/doge/data")
NOW = "2026-08-25T03:35:00Z"
TICK = 1802
EID = "nv_sps_fin"
GID = "gap_spsfin_omzet_1_58m_dividend_0_40m_lt_loans_1_92m_l5"
CID = "comm_spsfin_jr2025_omzet_1_58m"
LID = "lb_spsfin_omzet_1_58m_dividend_0_40m_debt_3_24m_l5"
SRC = "src_spsfin_jr2025_nbb"


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
        "title": "SPS FIN NV NBB VKT-kap YE2025 deposit 2026-00305818",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00305818.pdf",
        "publisher": "NBB / SPS FIN NV",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1802; KBO 0811.365.903; AV 13.07.2026; BDO/Defauw oordeel zonder voorbehoud; assets 5157946 omzet 1578352 dividend 400054; Zefier dual 22.87pct + IKA + Infrabel",
    },
    {
        "source_id": "src_spsfin_kbo",
        "title": "KBO SPS FIN NV 0811.365.903",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0811365903",
        "publisher": "FPS Economy KBO",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1802; NV; zetel Neringsweg 2 9820 Merelbeke-Melle; Infrabel + Enve + IKA + Zefier aandeelhouders",
    },
    {
        "source_id": "src_spsfin_zefier_peerdsbos",
        "title": "Zefier SPS FIN / Peerdsbos leftover dual context",
        "url": "https://jaarverslag.zefier.be/",
        "publisher": "Zefier cv",
        "accessed_date": "2026-08-25",
        "source_class": "primary_official",
        "notes": "tick1802; leftover Zefier dual after Storm Geraardsbergen; Peerdsbos / municipal renewable stack; Zefier 22.87pct",
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
    "tick1802 leftover Zefier dual after StormG; KBO 0811.365.903 Actief; NV; "
    "official NBB VKT-kap YE2025 deposit 2026-00305818 CDN 200 29p; AV 13.07.2026; BDO/Kevin Defauw oordeel zonder voorbehoud "
    "(na eerder verslag van niet-bevinding 11.06.2026); aandeelhouders Enve NV in vereffening 49.53pct / IKA DV 22.87pct / "
    "Zefier CV 22.87pct / Solfund in faling 3.15pct / Infrabel 1.58pct; Infrabel bestuurder (publiek recht); "
    "sourced euros assets 5157946 equity 1701795 debt 3244521 MVA 4195075 omzet 1578352 bruto 1391493 "
    "afschr 791145 expl 569552 fin opbr kapsubs 86059 fin kosten 232194 pnl 423413 tax 3 dividend 400054 "
    "cash 811061 JUMP LT overige leningen 1924682 ST binnen jaar 864231 kapsubs BS 456129 voorzieningen onderhoud 211630 "
    "gage overige leningen 1871080 hypotheek inschrijving 11635562 pand andere 947692 commissaris 6115 VTE 0; FOI ready; NOT every-10 (next 1810)"
)
if not any(r.get("entity_id") == EID for r in rows):
    rows.append(
        {
            "entity_id": EID,
            "name_nl": "SPS FIN NV (leftover Zefier dual / Peerdsbos; NOT StormG / EGPF / W4F / Zo-Fier / PortFineco)",
            "name_fr": "SPS FIN SA (dual Zefier residuel / Peerdsbos)",
            "name_en": "SPS FIN NV leftover Zefier dual Peerdsbos renewable project company",
            "level": "other",
            "parent_id": "cv_zefier",
            "community_language": "nl",
            "website": "https://jaarverslag.zefier.be/",
            "foi_email": "info@zefier.be",
            "foi_postal": "Neringsweg 2 9820 Merelbeke-Melle",
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
    ("bud_spsfin_assets_2025", 5157946, "Assets YE2025 5157946; tick1802"),
    ("bud_spsfin_equity_2025", 1701795, "Equity 1701795 DROP; tick1802"),
    ("bud_spsfin_debt_2025", 3244521, "Debt 3244521; tick1802"),
    ("bud_spsfin_mva_2025", 4195075, "MVA installaties 4195075; tick1802"),
    ("bud_spsfin_omzet_2025", 1578352, "Omzet 1578352; tick1802"),
    ("bud_spsfin_bruto_2025", 1391493, "Brutomarge 1391493; tick1802"),
    ("bud_spsfin_afschr_2025", 791145, "Afschrijvingen 791145; tick1802"),
    ("bud_spsfin_expl_2025", 569552, "Bedrijfswinst 569552; tick1802"),
    ("bud_spsfin_kapsubs_2025", 86059, "Kapitaal- en interestsubsidies 86059 recurrent; tick1802"),
    ("bud_spsfin_fin_kosten_2025", 232194, "Financiele kosten 232194; tick1802"),
    ("bud_spsfin_pnl_2025", 423413, "PnL 423413; tick1802"),
    ("bud_spsfin_dividend_2025", 400054, "Dividend / uit te keren winst 400054; tick1802"),
    ("bud_spsfin_cash_2025", 811061, "Cash 811061 JUMP from 468299; tick1802"),
    ("bud_spsfin_lt_other_loans_2025", 1924682, "Overige leningen LT 1924682; tick1802"),
    ("bud_spsfin_kapsubs_bs_2025", 456129, "Kapitaalsubsidies BS 456129; tick1802"),
    ("bud_spsfin_prov_onderhoud_2025", 211630, "Voorzieningen grote herstellingen 211630; tick1802"),
    ("bud_spsfin_gage_2025", 1871080, "Gage overige leningen 1871080; tick1802"),
    ("bud_spsfin_hypotheek_inschrijving_2025", 11635562, "Hypotheek inschrijving 11635562 on MVA 4195075; tick1802"),
    ("bud_spsfin_commissaris_2025", 6115, "Bezoldiging commissaris BDO 6115; tick1802"),
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
            "title": "SPS FIN JR2025 leftover Zefier dual (omzet 1.58m / dividend 0.40m / LT loans 1.92m)",
            "entity_id": EID,
            "beneficiary": "Zefier 22.87pct / IKA DV 22.87pct / Enve in vereffening 49.53pct / Infrabel 1.58pct",
            "legal_basis": "WVV NV; Bestuursdecreet openbaarheid; municipal renewable dual via Zefier + IKA + Infrabel",
            "decision_date": "2026-07-13",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": "1578352",
            "cash_by_year": "2025:1578352",
            "remaining_eur": "",
            "status": "active",
            "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00305818.pdf",
            "stated_goal": "Local leftover Zefier SPS FIN / Peerdsbos map — dividend payout + LT loans FOI",
            "cut_option": "Publish omzet L5 + dividend recipients (Enve in vereffening?) + LT other loans 1.92m counterparties + kapsubs path",
            "source_id": SRC,
            "confidence": "strong",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>SPS_FIN>JR2025_L5",
            "notes": "tick1802; YE2025; assets 5157946 omzet 1578352 dividend 400054 debt 3244521; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; not TE-additive of 348bn",
        }
    )
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
if not any(r.get("item_id") == LID for r in rows):
    rows.append(
        {
            "item_id": LID,
            "name": "SPS FIN 2025: omzet 1.58m / dividend 0.40m / LT loans 1.92m (Zefier+IKA+Infrabel dual)",
            "level": "L5",
            "type": "igs_energy_project_dual",
            "hierarchy_path": "Vlaanderen>IGS>Zefier>SPS_FIN",
            "annual_cost_eur": "1578352",
            "total_cost_eur": "3244521",
            "tco_notes": "Envelope=omzet 1.58m; dividend 400054 (majority Enve in vereffening 49.53pct); LT other loans 1.92m gage 1.87m hypotheek inschrijving 11.64m; kapsubs 86k/yr; not pure waste — opacity on payout recipients + loan counterparties + Enve liquidation control",
            "confidence": "strong",
            "source_id": SRC,
            "beneficiaries": "Enve 49.53pct + IKA 22.87pct + Zefier 22.87pct + Infrabel 1.58pct",
            "stated_goal": "Local renewable / Peerdsbos via Zefier + intercommunal + Infrabel",
            "measured_outcome": "Profit 0.42m; pays almost all as 0.40m dividend; controlling shareholder in liquidation",
            "absurdity_score": "6",
            "cost_score": "4",
            "difficulty": "5",
            "priority_index": "4.9",
            "cut_proposal": "FOI dividend recipients under Enve vereffening + LT loans 1.92m + kapsubs 86k path + hypotheek 11.6m rationale",
            "status": "open",
            "struck_reason": "",
            "notes": "tick1802 leftover Zefier dual; strong NBB; not TE-additive; not pure-waste top10",
        }
    )
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
if not any(r.get("gap_id") == GID for r in rows):
    rows.append(
        {
            "gap_id": GID,
            "hierarchy_path": "Vlaanderen>IGS>Zefier>SPS_FIN>JR2025_L5",
            "entity_id": EID,
            "what_is_missing": "Omzet L5-uitsplitsing achter 1578352; ontvangers dividend 400054 bij Enve NV in vereffening 49.53pct + IKA/Zefier/Infrabel; tegenpartijen overige leningen LT 1924682 + gage 1871080; path kapitaalsubsidies 86059 recurrent / BS 456129; hypotheek inschrijving 11635562 op MVA 4195075; AV-termijn + BS-publicatie herbenoemingen (commissaris remark)",
            "why_it_matters": "Zefier dual Peerdsbos projectco pays 0.40m dividend while controlling shareholder Enve is in liquidation and Infrabel (public) sits on board — residual opacity after StormG",
            "priority": "8",
            "recipient_body": "SPS FIN NV / Zefier cv / IKA DV / Infrabel",
            "recipient_email": "info@zefier.be",
            "recipient_postal": "Neringsweg 2 9820 Merelbeke-Melle",
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
            "notes": "tick1802; human-send only; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; closes deferred SPS FIN CDN live",
        }
    )
write("foi_queue.csv", fields, rows)
print("foi_queue", len(rows))

fields, rows = read("research_queue.csv")
for r in rows:
    if r.get("task_id") == "rq_1802":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = NOW
        r["notes"] = "tick1802 SPS FIN NV Zefier dual; KBO 0811.365.903; NBB 2026-00305818; omzet 1578352 dividend 400054 debt 3244521; FOI ready; every-10 1810"
        r["blocked_gap_id"] = GID
if not any(r.get("task_id") == "rq_1803" for r in rows):
    rows.append(
        {
            "task_id": "rq_1803",
            "title": "Leftover dual residual hole-fill after SPS FIN (AGB/NSZ/Bosgroep/FARO/IGS)",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "Belgique>LeftoverDual>Residual",
            "entity_id": "",
            "instructions": "Tick 1803 after 1802 SPS FIN. Prefer leftover AGB/APB of mined cities if PDF live, else Bosgroep / IOED / Dijk92 if CDN 200 / FARO NBB YE2025 if live / Storm Wielsbeke/Zandvliet/Terranova or other unused Zefier if CDN 200 / OP-TIL/VI.BE if unused live / other HVZ if JR2025 euros newly live / other IGS. Skip already-done. Next every-10 1810.",
            "blocked_gap_id": "",
            "created_utc": NOW,
            "updated_utc": NOW,
            "notes": "spawned after tick1802; NEXT residual dual; Zefier CDN sister+StormG+SPS FIN closed; every-10 1810",
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
        r["last_unit_id"] = "rq_1802"
        r["ticks_completed"] = str(TICK)
        r["paused"] = "no"
        r["notes"] = (
            "tick1802 leftover SPS FIN NV Zefier dual Peerdsbos; KBO 0811.365.903; NBB 2026-00305818; assets 5157946 "
            "omzet 1578352 dividend 400054 debt 3244521 Enve vereffening 49.53pct Infrabel board; FOI ready; "
            "AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; NOT every-10 (next 1810); next rq_1803 residual dual; continuous hole_fill"
        )
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE")
