import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
TICK = "1713"
UTC = "2026-08-23T20:25:00Z"
DATE = "2026-08-23"
EID = "vzw_faro"


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
        "name_nl": "FARO. Vlaams steunpunt voor cultureel erfgoed vzw (leftover VL cultureel-erfgoed steunpunt; NOT meemoo / Kunstenpunt / OP-TIL)",
        "name_fr": "FARO. Point d appui flamand pour le patrimoine culturel asbl (residuel)",
        "name_en": "FARO Flemish cultural-heritage support centre VZW leftover",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://faro.be",
        "foi_email": "info@faro.be",
        "foi_postal": "Grasmarkt 105 bus 44 1000 Brussel",
        "notes": "tick1713 leftover FARO after SOFAM/AGB/NSZ hunt; official JV2025 finance live + NBB YE2024 CDN 200; KBO 0893.863.017; FOI NBB YE2025",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_faro_jv2025_official",
        "title": "FARO Jaarverslag 2025 (official org PDF; DE FINANCIEN p21)",
        "url": "https://faro.be/sites/default/files/bijlagen/e-documenten/jaarverslag_2025_def_0.pdf",
        "publisher": "FARO vzw",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1713; 23p; werkingsbudget afgerond 2875000; overschot 70194; VL werkingssubsidie 2481000; pie subsidies 93.15pct / pers 81.01pct",
    },
    {
        "source_id": "src_faro_nbb_ye2024",
        "title": "FARO NBB VKT-VZW YE2024 deposit 2025-00569658",
        "url": "http://cdn.staatsbladmonitor.be/2025pdf/2025-00569658.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1713; AV 27.03.2025; neergelegd 24.11.2025; assets 1020016 bruto 2383082 code73 2740761 staff 2334908 VTE 21.6 pnl 37243; model VKT-VZW 23.0.6",
    },
    {
        "source_id": "src_faro_kbo",
        "title": "FARO KBO Public Search 0893.863.017",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=893863017",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1713; active VZW; zetel Grasmarkt 105/44 1000 Brussel; NACE 94.999",
    },
    {
        "source_id": "src_faro_jv2025_portal",
        "title": "FARO publicaties Jaarverslag 2025 portal page",
        "url": "https://faro.be/publicaties/jaarverslag-2025",
        "publisher": "FARO vzw",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1713; portal + PDF bijlage pointer; blog 26.05.2026",
    },
    {
        "source_id": "src_faro_foi_contact_1713",
        "title": "FARO FOI channel (info@faro.be)",
        "url": "https://faro.be/faro",
        "publisher": "FARO vzw",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1713; info@faro.be; +32 2 213 10 60; BE02 0682 4904 8840",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_faro_werkingsbudget_2025", "2025", "2875000", "executed", "src_faro_jv2025_official", "strong", "JV2025 p21 totale werkingsbudget afgerond 2875000; tick1713"),
    ("bud_faro_overschot_2025", "2025", "70194", "executed", "src_faro_jv2025_official", "strong", "JV2025 p21 overschot 70194; tick1713"),
    ("bud_faro_vl_werkingssubsidie_2025", "2025", "2481000", "executed", "src_faro_jv2025_official", "strong", "JV2025 p21 Vlaamse werkingssubsidie 2481000; tick1713"),
    ("bud_faro_personeel_derived_2025", "2025", "2329038", "executed", "src_faro_jv2025_official", "medium", "Derived 81.01pct of rounded werkingsbudget 2875000; pie uitgaven; tick1713"),
    ("bud_faro_werking_derived_2025", "2025", "531013", "executed", "src_faro_jv2025_official", "medium", "Derived 18.47pct of rounded werkingsbudget 2875000; tick1713"),
    ("bud_faro_subsidies_share_derived_2025", "2025", "2678063", "executed", "src_faro_jv2025_official", "medium", "Derived 93.15pct of rounded werkingsbudget 2875000 (incl VL 2.481m + tewerkstelling/project/Nationale Loterij); tick1713"),
    ("bud_faro_eigen_middelen_derived_2025", "2025", "168763", "executed", "src_faro_jv2025_official", "medium", "Derived 5.87pct of rounded werkingsbudget 2875000; tick1713"),
    ("bud_faro_assets_2024", "2024", "1020016", "executed", "src_faro_nbb_ye2024", "strong", "NBB VKT-VZW 20/58 assets 1020016; tick1713"),
    ("bud_faro_va_2024", "2024", "44978", "executed", "src_faro_nbb_ye2024", "strong", "NBB VA 21/28 44978 (MVA 44606 FVA 372); tick1713"),
    ("bud_faro_vlottend_2024", "2024", "975039", "executed", "src_faro_nbb_ye2024", "strong", "NBB vlottend 29/58 975039; tick1713"),
    ("bud_faro_cash_2024", "2024", "678952", "executed", "src_faro_nbb_ye2024", "strong", "NBB liquide 54/58 678952 DROP vs 861994; tick1713"),
    ("bud_faro_equity_2024", "2024", "694010", "executed", "src_faro_nbb_ye2024", "strong", "NBB EV 10/15 694010 (fondsen 39057 + bestemde 400000 + overgedragen 254953); tick1713"),
    ("bud_faro_debt_2024", "2024", "326007", "executed", "src_faro_nbb_ye2024", "strong", "NBB schulden 17/49 326007 (ST 299637 + overlopend 26370); tick1713"),
    ("bud_faro_bruto_2024", "2024", "2383082", "executed", "src_faro_nbb_ye2024", "strong", "NBB brutomarge 9900 2383082; tick1713"),
    ("bud_faro_omzet_2024", "2024", "175996", "executed", "src_faro_nbb_ye2024", "strong", "NBB omzet 70 175996; tick1713"),
    ("bud_faro_code73_2024", "2024", "2740761", "executed", "src_faro_nbb_ye2024", "strong", "NBB code73 lidgeld/schenkingen/legaten/subsidies 2740761; tick1713"),
    ("bud_faro_diensten_2024", "2024", "552414", "executed", "src_faro_nbb_ye2024", "strong", "NBB 60/61 552414; tick1713"),
    ("bud_faro_staff_2024", "2024", "2334908", "executed", "src_faro_nbb_ye2024", "strong", "NBB 62 bezoldigingen 2334908 / VTE 21.6; tick1713"),
    ("bud_faro_expl_2024", "2024", "30633", "executed", "src_faro_nbb_ye2024", "strong", "NBB bedrijfswinst 9901 30633; tick1713"),
    ("bud_faro_pnl_2024", "2024", "37243", "executed", "src_faro_nbb_ye2024", "strong", "NBB PnL 9904 37243; AV 27.03.2025; tick1713"),
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
        "commitment_id": "comm_faro_jv2025_werkingsbudget",
        "title": "FARO JV2025 leftover VL cultural-heritage steunpunt (werkingsbudget 2.88m / VL subsidy 2.48m / overschot 70k)",
        "entity_id": EID,
        "beneficiary": "VL cultural-heritage sector / museums archives libraries IOEDs via FARO",
        "legal_basis": "WVV VZW; Cultureelerfgoeddecreet / steunpunt beheersovereenkomst; Bestuursdecreet openbaarheid",
        "decision_date": "2026-05-26",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "2875000",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://faro.be/sites/default/files/bijlagen/e-documenten/jaarverslag_2025_def_0.pdf",
        "stated_goal": "Local leftover FARO map — official JV2025 werkingsbudget 2.88m; FOI NBB YE2025",
        "cut_option": "Publish NBB YE2025 statutory + non-rounded budget + VTE YE2025 + subsidy split; scrutinise 81pct personnel share",
        "source_id": "src_faro_jv2025_official",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Koepel>FARO>JV2025_L5",
        "notes": "tick1713; YE2025 JV strong + YE2024 NBB baseline assets 1.02m bruto 2.38m code73 2.74m staff 2.33m VTE 21.6; NBB YE2025 still unpublished; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_faro_werkingsbudget_2_88m_vl_subs_2_48m_pers_81pct",
        "name": "FARO JV2025 leftover VL cultural-heritage steunpunt: werkingsbudget 2.88m / VL subsidy 2.48m / pers ~81pct",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Koepel>FARO>JV2025_L5",
        "annual_cost_eur": "2875000",
        "total_cost_eur": "2875000",
        "tco_notes": "Leftover FARO VZW YE2025: rounded werkingsbudget 2.875m / VL werkingssubsidie 2.481m / overschot 70.2k; pie subsidies 93.15pct / personnel 81.01pct; YE2024 NBB baseline assets 1.02m bruto 2.38m staff 2.33m VTE 21.6",
        "confidence": "strong",
        "source_id": "src_faro_jv2025_official",
        "beneficiaries": "VL cultural-heritage organisations via FARO advice/training/Erfgoeddag",
        "stated_goal": "Local leftover FARO map — official JV2025 finance newly live (was JR2024-only)",
        "measured_outcome": "Official FARO JV2025 2026-08-23: werkingsbudget 2875000 / VL subs 2481000 / overschot 70194; NBB YE2024 assets 1020016 / bruto 2383082",
        "absurdity_score": "4.5",
        "cost_score": "5.0",
        "difficulty": "2.5",
        "priority_index": "4.6",
        "cut_proposal": "Do not treat full 2.88m as waste; scrutinise 81pct personnel + publish NBB YE2025 + subsidy split (VL/tewerkstelling/project/Nationale Loterij)",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1713; leftover after AGB unpublished / NSZ CDN403 / SOFAM done; prior ticks said FARO no JR2025 — JV2025 now live; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_faro_werkingsbudget_2_88m_vl_subs_2_48m_nbb_ye2025_l5",
        "hierarchy_path": "Vlaanderen>Koepel>FARO>JV2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official JV2025 publishes rounded werkingsbudget 2875000 / VL werkingssubsidie 2481000 / overschot 70194 / pie subsidies 93.15pct pers 81.01pct; NBB YE2024 deposit 2025-00569658 live (assets 1020016 bruto 2383082 staff 2334908 VTE 21.6); NBB YE2025 statutory PDF / non-rounded budget lines / exact VTE YE2025 / AV notulen / subsidy split (VL vs tewerkstelling vs project vs Nationale Loterij) still Unknown",
        "why_it_matters": "Leftover VL cultural-heritage steunpunt with live official YE2025 activity-report euros (2.88m werkingsbudget / 2.48m VL subsidy) — need NBB YE2025 statutory reconcile + non-rounded lines + VTE",
        "priority": "8",
        "recipient_body": "FARO. Vlaams steunpunt voor cultureel erfgoed vzw / Bestuursorgaan",
        "recipient_email": "info@faro.be",
        "recipient_postal": "Grasmarkt 105 bus 44 1000 Brussel",
        "draft_letter_path": "docs/doge/foi/drafts/gap_faro_werkingsbudget_2_88m_vl_subs_2_48m_nbb_ye2025_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_faro_jv2025_werkingsbudget",
        "linked_leaderboard_id": "lb_faro_werkingsbudget_2_88m_vl_subs_2_48m_pers_81pct",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1713; human-send only; NSZ/Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight/Welzijnszorg/SOFAM FOI still ready",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1713":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_faro_werkingsbudget_2_88m_vl_subs_2_48m_nbb_ye2025_l5"
        r["notes"] = "DONE tick1713: FARO KBO 0893.863.017 JV2025 werkingsbudget 2875000 VL_subs 2481000 overschot 70194 + NBB YE2024 assets 1020016 bruto 2383082 staff 2334908 VTE 21.6; FOI ready gap_faro_werkingsbudget_2_88m_vl_subs_2_48m_nbb_ye2025_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1714",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1714 after 1713 FARO JV2025. Next every-10 is 1720. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs / Northdata deposit→CDN. Do NOT redo FARO/SOFAM/Welzijnszorg/PlayRight/SIMIM/Reprobel/Auvibel/Sabam/NSZ/FBM/Biovia/Medvia/BlauweCluster/Flux50/Catalisti/FlandersFOOD/Avansa*/meemoo/Kunstenpunt/OP-TIL/VI.BE.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep, Dijk92 if JR euros, APEFE if JR euros, GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1713 FARO; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/GO!/POV/BVAS/IOED/HVZ/IGS; FARO+SOFAM+Welzijnszorg+PlayRight+SIMIM+Reprobel DONE; next every-10 1720",
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
        "last_unit_id": "rq_1713",
        "ticks_completed": "1713",
        "paused": "no",
        "notes": "tick1713 leftover FARO VZW residual; KBO 0893.863.017; official Jaarverslag 2025 PDF live faro.be + NBB YE2024 deposit 2025-00569658 CDN 200; sourced euros YE2025 werkingsbudget 2875000 VL_subs 2481000 overschot 70194 (JV rounded) + YE2024 assets 1020016 bruto 2383082 code73 2740761 staff 2334908 VTE 21.6 pnl 37243; NBB YE2025 still unpublished; FOI ready NBB YE2025; NSZ still CDN 403; Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight/Welzijnszorg/SOFAM FOI still ready; Natuurpunt opaque; Dijk92 CDN 403; APEFE RA2023; AGB unpublished; NOT every-10 (next 1720); next rq_1714 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
