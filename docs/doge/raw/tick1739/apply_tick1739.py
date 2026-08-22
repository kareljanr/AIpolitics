import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T05:05:00Z"
DATE = "2026-08-24"
EID = "vzw_prinsenhof"
GAP = "gap_prinsenhof_opbr_4_90m_equity_neg_0_77m_debt_9_21m_l5"
COMM = "comm_prinsenhof_jr2025_opbr"
LB = "lb_prinsenhof_opbr_4_90m_equity_neg_0_77m_debt_9_21m"


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
        "name_nl": "WZC Prinsenhof VZW (leftover VL WZC Beringen-Koersel / Vivalto Home; dual Molenheide; NOT Colisée/Armonea)",
        "name_fr": "Maison de repos Prinsenhof asbl (residuelle Beringen / Vivalto)",
        "name_en": "Prinsenhof residential care VZW leftover Flemish WZC Beringen Vivalto dual Molenheide",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.vivaltohome.com/nl/maisons/prinsenhof/",
        "foi_email": "prinsenhof@vivaltohome.com",
        "foi_postal": "Heerbaan 375 3582 Koersel",
        "notes": "tick1739 leftover VL WZC after Colisée; official NBB VOL-VZW YE2025 deposit 2026-00176220 CDN 200; KBO 0644.497.395; equity NEG 0.77m + Vivalto comfort letter; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_prinsenhof_nbb_ye2025",
        "title": "WZC Prinsenhof NBB VOL-VZW YE2025 deposit 2026-00176220",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00176220.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1739; AV 22.05.2026; assets 8445494 opbr 4902312 staff 3230598 VTE 59.9 pnl 43669 equity -766800 debt 9212294; Mazars zonder voorbehoud; Vivalto comfort",
    },
    {
        "source_id": "src_prinsenhof_kbo",
        "title": "WZC Prinsenhof KBO 0644.497.395",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=644497395",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1739; VZW; Heerbaan 375 3582 Koersel",
    },
    {
        "source_id": "src_prinsenhof_portal",
        "title": "Prinsenhof Vivalto Home portal",
        "url": "https://www.vivaltohome.com/nl/maisons/prinsenhof/",
        "publisher": "Vivalto Home / WZC Prinsenhof",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1739; WZC Koersel; tel 011/42.06.98",
    },
    {
        "source_id": "src_prinsenhof_foi_contact_1739",
        "title": "Prinsenhof FOI channel",
        "url": "https://www.vivaltohome.com/nl/maisons/prinsenhof/",
        "publisher": "WZC Prinsenhof VZW",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1739; prinsenhof@vivaltohome.com; Heerbaan 375 3582 Koersel",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_prinsenhof_assets_2025", "2025", "8445494", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB 20/58 assets 8445494; tick1739"),
    ("bud_prinsenhof_va_2025", "2025", "6240159", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB VA 6240159; tick1739"),
    ("bud_prinsenhof_leasing_mva_2025", "2025", "5844871", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB leasing MVA 5844871; tick1739"),
    ("bud_prinsenhof_vlottend_2025", "2025", "2205335", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB vlottend 2205335; tick1739"),
    ("bud_prinsenhof_cash_2025", "2025", "430498", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB liquide 430498 JUMP vs 61455; tick1739"),
    ("bud_prinsenhof_equity_2025", "2025", "-766800", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB EV -766800 NEG (improved vs -2215469); Vivalto comfort; tick1739"),
    ("bud_prinsenhof_debt_2025", "2025", "9212294", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB schulden 9212294; tick1739"),
    ("bud_prinsenhof_lt_achtergesteld_2025", "2025", "4227992", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB LT achtergesteld 4227992; FOI; tick1739"),
    ("bud_prinsenhof_lt_leasing_2025", "2025", "3501999", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB LT leasing 3501999; FOI; tick1739"),
    ("bud_prinsenhof_opbr_2025", "2025", "4902312", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB bedrijfsopbrengsten 4902312; tick1739"),
    ("bud_prinsenhof_omzet_2025", "2025", "4858856", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB omzet 70 4858856; code73 empty; FOI RIZIV; tick1739"),
    ("bud_prinsenhof_andere_opbr_2025", "2025", "43456", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB andere 74 43456; tick1739"),
    ("bud_prinsenhof_staff_2025", "2025", "3230598", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB 62 3230598 / VTE 59.9 DROP vs 63.9; tick1739"),
    ("bud_prinsenhof_diensten_2025", "2025", "568168", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB diensten 61 568168; tick1739"),
    ("bud_prinsenhof_expl_2025", "2025", "298488", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB bedrijfswinst 9901 298488 FLIP vs -243153; tick1739"),
    ("bud_prinsenhof_pnl_2025", "2025", "43669", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB PnL 9904 43669 FLIP; AV 22.05.2026; Mazars zonder voorbehoud; tick1739"),
    ("bud_prinsenhof_onttrekking_ev_2025", "2025", "1405000", "executed", "src_prinsenhof_nbb_ye2025", "strong", "NBB onttrkking eigen vermogen 1405000 (resultaatverwerking); FOI; tick1739"),
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
        "title": "Prinsenhof YE2025 leftover VL WZC (opbr 4.90m / equity NEG 0.77m / debt 9.21m)",
        "entity_id": EID,
        "beneficiary": "WZC residents / care staff Koersel / Vivalto group",
        "legal_basis": "WVV VZW; Woonzorgdecreet; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-22",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "4902312",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00176220.pdf",
        "stated_goal": "Local leftover Prinsenhof WZC map — official NBB YE2025 dual Vivalto; FOI NEG equity + comfort letter",
        "cut_option": "Publish RIZIV omzet split despite empty 73; disclose achtergesteld+leasing counterparties; publish Vivalto comfort letter terms",
        "source_id": "src_prinsenhof_nbb_ye2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Prinsenhof>JR2025_L5",
        "notes": "tick1739; YE2025; opbr 4.90m omzet 4.86m staff 3.23m VTE 59.9 pnl +44k equity -0.77m debt 9.21m; Vivalto dual Molenheide; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "Prinsenhof YE2025: opbr 4.90m / equity NEG 0.77m / debt 9.21m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Prinsenhof>JR2025_L5",
        "annual_cost_eur": "4902312",
        "total_cost_eur": "9212294",
        "tco_notes": "Leftover Vivalto Prinsenhof WZC YE2025: opbr 4.90m (omzet 4.86m / code73 empty) / staff 3.23m VTE 59.9 DROP / pnl +44k FLIP; equity -0.77m NEG (improved via 1.41m onttrkking) / debt 9.21m (achtergesteld 4.23m + leasing 3.50m); Vivalto comfort letter continuity; Mazars zonder voorbehoud; dual Molenheide",
        "confidence": "strong",
        "source_id": "src_prinsenhof_nbb_ye2025",
        "beneficiaries": "WZC residents / care staff Koersel / Vivalto group",
        "stated_goal": "Local leftover Prinsenhof WZC map — official NBB YE2025 after Colisée residual",
        "measured_outcome": "Official NBB YE2025 2026-08-24: opbr 4902312 / staff 3230598 VTE 59.9 / pnl 43669 / equity -766800 / debt 9212294",
        "absurdity_score": "4.2",
        "cost_score": "3.5",
        "difficulty": "2.5",
        "priority_index": "3.8",
        "cut_proposal": "Publish RIZIV split of omzet; disclose achtergesteld+leasing counterparties; publish Vivalto comfort-letter scope and group integration plan",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1739; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / Colisee+Armonea+Gravenkasteel+Molenheide done; Vivalto; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Welzijn>WZC>Prinsenhof>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official NBB VOL-VZW publishes opbr 4902312 / omzet 4858856 / staff 3230598 VTE 59.9 / pnl 43669 / equity -766800 / debt 9212294 / achtergesteld 4227992 / leasing 3501999; RIZIV omzet split, debt counterparties, and Vivalto comfort-letter text unpublished; AV notulen 22.05.2026",
        "why_it_matters": "Vivalto leftover VL WZC with NEG equity relying on parent comfort letter while flipping to small profit — need public-care financing and group-support transparency",
        "priority": "8",
        "recipient_body": "WZC Prinsenhof VZW / Vivalto Home Belgium NV / Bestuursorgaan",
        "recipient_email": "prinsenhof@vivaltohome.com",
        "recipient_postal": "Heerbaan 375 3582 Koersel",
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
        "notes": "tick1739; human-send only; dual Molenheide Vivalto; AGB/NSZ/Dijk92/APEFE still blocked; next tick 1740 EVERY-10 MUST",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1739":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["notes"] = "DONE tick1739: Prinsenhof KBO 0644.497.395 NBB YE2025 opbr 4902312 equity -766800 debt 9212294 Vivalto comfort; FOI ready gap_prinsenhof_opbr_4_90m_equity_neg_0_77m_debt_9_21m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1740",
        "title": "EVERY-10 progress coverage % layers A-E + waste top10",
        "sprint": "hole_fill",
        "priority": "9",
        "status": "open",
        "hierarchy_target": "L0-L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1740 EVERY-10 MUST after 1739 Prinsenhof. Refresh docs/doge/data/progress_every_10_ticks.md (layers A-E % of €347.956 bn TE) and docs/doge/data/doge_waste_top10_current.md (top 10 by priority_index). Note major NEW since 1730: TerEngelen/WitteMeren/VeiligeHave/SintJozef/Molenheide/Gravenkasteel/Armonea/ColiseeBelgium/Prinsenhof. Then spawn rq_1741 leftover hole-fill. Do NOT skip decade refresh.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1739 Prinsenhof; EVERY-10 MUST next; then leftover AGB/NSZ/Bosgroep/Dijk92/APEFE/WZC/IGS",
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
        "last_unit_id": "rq_1739",
        "ticks_completed": "1739",
        "paused": "no",
        "notes": "tick1739 leftover Prinsenhof WZC residual; KBO 0644.497.395; official NBB VOL-VZW YE2025 deposit 2026-00176220 CDN 200; sourced euros assets 8445494 opbr 4902312 omzet 4858856 staff 3230598 VTE 59.9 pnl 43669 equity -766800 debt 9212294 achtergesteld 4227992 leasing 3501999 cash 430498; Mazars oordeel zonder voorbehoud; Vivalto comfort letter; FOI ready; AGB Bornem JR2024-only; NSZ CDN 403; Dijk92 CDN 403; APEFE CDN 403; NOT every-10 (next 1740 MUST); next rq_1740 EVERY-10 MUST then leftover hole_fill; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
