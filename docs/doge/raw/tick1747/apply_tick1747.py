import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T07:45:00Z"
DATE = "2026-08-24"
EID = "vzw_zusterhof"
GAP = "gap_zusterhof_omzet_12_67m_staff_9_76m_subs_2_58m_l5"
COMM = "comm_zusterhof_jr2025_omzet"
LB = "lb_zusterhof_omzet_12_67m_staff_9_76m_subs_2_58m"


def read(fn):
    with open(base / fn, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return r.fieldnames, list(r)


def write(fn, fields, rows):
    with open(base / fn, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


fields, rows = read("entities.csv")
assert not any(r["entity_id"] == EID for r in rows)
rows.append(
    {
        "entity_id": EID,
        "name_nl": "Zusterhof Woon-en Zorgcentrum VZW (leftover VL WZC Geel local; NOT Vivalto; omzet 12.7m)",
        "name_fr": "Maison de repos Zusterhof asbl (residuelle Geel locale; pas Vivalto)",
        "name_en": "Zusterhof residential care VZW leftover Flemish WZC Geel local not Vivalto",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.zusterhof.be/",
        "foi_email": "info@zusterhof.be",
        "foi_postal": "Gerststraat 67 2440 Geel",
        "notes": "tick1747 leftover local Geel WZC VZW (NOT Vivalto despite earlier queue guess); official NBB VOL-VZW YE2025 deposit 2026-00272840 CDN 200; KBO 0473.762.450; omzet 12672532 staff 9758965 VTE 151.1; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_zusterhof_nbb_ye2025",
        "title": "Zusterhof VZW NBB VOL-VZW YE2025 deposit 2026-00272840",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00272840.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1747; AV 05.06.2026; assets 28530472 omzet 12672532 subs 2580277 staff 9758965 VTE 151.1 pnl 377671 equity 15037745 debt 13492727; commissaris Vanderhaegen fee 5141; audit pages image-only",
    },
    {
        "source_id": "src_zusterhof_kbo",
        "title": "Zusterhof VZW KBO 0473.762.450",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=473762450",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1747; VZW; Gerststraat 67 2440 Geel",
    },
    {
        "source_id": "src_zusterhof_portal",
        "title": "Zusterhof WZC portal",
        "url": "https://www.zusterhof.be/",
        "publisher": "Zusterhof VZW",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1747; WZC Geel; info@zusterhof.be; tel 014 57 97 97",
    },
    {
        "source_id": "src_zusterhof_foi_contact_1747",
        "title": "Zusterhof FOI channel",
        "url": "https://www.zusterhof.be/",
        "publisher": "Zusterhof VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1747; info@zusterhof.be; Gerststraat 67 2440 Geel",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_zusterhof_assets_2025", "2025", "28530472", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB 20/58 assets 28530472 DROP vs 29449648; tick1747"),
    ("bud_zusterhof_va_2025", "2025", "20893000", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB VA 20893000; buildings 19954667; in aanbouw 427058; tick1747"),
    ("bud_zusterhof_vlottend_2025", "2025", "7637472", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB vlottend 7637472 DROP; tick1747"),
    ("bud_zusterhof_cash_2025", "2025", "2401443", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB liquide 2401443 DROP vs 2555796; tick1747"),
    ("bud_zusterhof_lt_recv_2025", "2025", "2082519", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB LT overige vorderingen 2082519 DROP vs 2725505; FOI counterparties; tick1747"),
    ("bud_zusterhof_equity_2025", "2025", "15037745", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB EV 15037745; kapitaalsubsidies 6081249; tick1747"),
    ("bud_zusterhof_debt_2025", "2025", "13492727", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB schulden 13492727 DROP; LT bank 9446051; tick1747"),
    ("bud_zusterhof_omzet_2025", "2025", "12672532", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB omzet 70 WZC 12672532; tick1747"),
    ("bud_zusterhof_subs_2025", "2025", "2580277", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB 733 subsidies 2580277 DROP vs 2744071; FOI split; tick1747"),
    ("bud_zusterhof_bedrijfsopbr_2025", "2025", "15410578", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB bedrijfsopbrengsten 70/76A 15410578; tick1747"),
    ("bud_zusterhof_staff_2025", "2025", "9758965", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB 62 9758965 / VTE 151.1 JUMP vs 145.3; interim 617 440422 DROP vs 1180124; tick1747"),
    ("bud_zusterhof_diensten_2025", "2025", "3094996", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB 61 diensten 3094996 DROP vs 3698737; tick1747"),
    ("bud_zusterhof_expl_2025", "2025", "871860", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 871860 JUMP vs 45680; tick1747"),
    ("bud_zusterhof_pnl_2025", "2025", "377671", "executed", "src_zusterhof_nbb_ye2025", "strong", "NBB PnL 9904 377671 (vs -340335); AV 05.06.2026; tick1747"),
]
for bid, year, amt, basis, sid, conf, notes in budgets:
    assert not any(r["budget_id"] == bid for r in rows)
    rows.append(
        {
            "budget_id": bid,
            "entity_id": EID,
            "year": year,
            "amount_eur": amt,
            "amount_min_eur": "",
            "amount_max_eur": "",
            "basis": basis,
            "source_id": sid,
            "confidence": conf,
            "notes": notes,
        }
    )
write("budgets.csv", fields, rows)
print("budgets", len(rows))

fields, rows = read("commitments.csv")
rows.append(
    {
        "commitment_id": COMM,
        "title": "Zusterhof YE2025 leftover VL WZC Geel (omzet 12.67m / staff 9.76m / subs 2.58m)",
        "entity_id": EID,
        "beneficiary": "WZC residents Geel / local VZW board",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-06-05",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "15410578",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00272840.pdf",
        "stated_goal": "Local leftover Zusterhof WZC Geel map — official NBB YE2025 VOL; FOI subsidy split + LT recv",
        "cut_option": "Publish RIZIV/dagprijs/subsidy split; disclose LT other-recv 2.08m counterparties; publish auditor opinion text; map temp-contract churn",
        "source_id": "src_zusterhof_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Zusterhof>JR2025_L5",
        "notes": "tick1747; YE2025 VOL-VZW; omzet 12.67m subs 2.58m staff 9.76m VTE 151.1 pnl +378k; NOT Vivalto; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Zusterhof YE2025: omzet 12.67m / staff 9.76m / subs 2.58m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Zusterhof>JR2025_L5",
        "annual_cost_eur": "15410578",
        "total_cost_eur": "15410578",
        "tco_notes": "Leftover local Geel Zusterhof WZC VZW YE2025 VOL (NOT Vivalto): omzet WZC 12.67m / subsidies 2.58m DROP / bedrijfsopbr 15.41m / staff 9.76m VTE 151.1 JUMP vs 145.3 / interim cost DROP 1.18m→0.44m / diensten DROP 3.70m→3.09m / expl JUMP 46k→872k / pnl +378k (vs -340k); assets 28.53m / equity 15.04m incl kapitaalsubsidies 6.08m / debt 13.49m LT bank 9.45m / LT other recv 2.08m opaque; high temp churn 112.5 VTE in / 106.4 out; commissaris Vanderhaegen fee 5.1k (audit pages image-only in PDF extract)",
        "confidence": "strong",
        "source_id": "src_zusterhof_nbb_ye2025",
        "beneficiaries": "WZC residents Geel",
        "stated_goal": "Local leftover Zusterhof WZC map — official NBB YE2025 after HofSchoten residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: omzet 12672532 / subs 2580277 / staff 9758965 VTE 151.1 / pnl 377671 / assets 28530472 / equity 15037745 / LT recv 2082519",
        "absurdity_score": "4.8",
        "cost_score": "5.5",
        "difficulty": "2.5",
        "priority_index": "5.2",
        "cut_proposal": "Publish subsidy 2.58m programme split + LT recv 2.08m counterparties; disclose auditor opinion; reduce opaque temp-contract churn without cutting care quality",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1747; leftover after AGB Bornem JR2024-only / HofSchoten done; corrected NOT-Vivalto; Vivalto queue exhausted for CDN trio; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Zusterhof>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-VZW publishes omzet 12672532 / subsidies 2580277 / staff 9758965 VTE 151.1 / pnl 377671 / LT other recv 2082519; subsidy programme split, LT recv counterparties, full auditor opinion text (PDF image pages), and AV notulen 05.06.2026 unpublished",
        "why_it_matters": "Large local Geel WZC with 15.4m operating euros and 2.58m subsidies plus 2.08m opaque LT receivables — need programme and counterparty transparency for public-care euros",
        "priority": "8",
        "recipient_body": "Zusterhof Woon-en Zorgcentrum VZW / Bestuursorgaan",
        "recipient_email": "info@zusterhof.be",
        "recipient_postal": "Gerststraat 67 2440 Geel",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1747; human-send only; local Geel VZW NOT Vivalto; AGB/NSZ/Dijk92/APEFE still blocked preferred path",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1747":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = "Zusterhof WZC Geel JR2025 leftover dual residual"
        r["notes"] = "DONE tick1747: Zusterhof VZW Geel KBO 0473.762.450 NBB YE2025 omzet 12672532 staff 9758965 VTE 151.1 subs 2580277; NOT Vivalto; FOI ready gap_zusterhof_omzet_12_67m_staff_9_76m_subs_2_58m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1748",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1748 after 1747 Zusterhof YE2025. Next every-10 is 1750. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo Zusterhof/HofSchoten/Buitenhof/Familiehof/Akapella/DeVerlosser/VivaltoHomeBE/Prinsenhof/ColiseeBelgium/Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if CDN 200, ABS/POV/BVAS, other IOED/HVZ/IGS/WZC/LSC if unused live JR2025.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1747 Zusterhof; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ/IGS/WZC; Vivalto CDN trio done; next every-10 1750",
    }
)
write("research_queue.csv", fields, rows)
print("rq", len(rows))

fields, rows = read("loop_state.csv")
assert len(rows) == 1
rows[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1747",
        "ticks_completed": "1747",
        "paused": "no",
        "notes": "tick1747 leftover Zusterhof WZC Geel VZW residual; KBO 0473.762.450; official NBB VOL-VZW YE2025 deposit 2026-00272840 CDN 200; sourced euros assets 28530472 omzet 12672532 subs 2580277 bedrijfsopbr 15410578 staff 9758965 VTE 151.1 pnl 377671 equity 15037745 debt 13492727 LT recv 2082519; NOT Vivalto local board; FOI ready; AGB Bornem JR2024-only; NOT every-10 (next 1750); next rq_1748 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/IOED/HVZ; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
