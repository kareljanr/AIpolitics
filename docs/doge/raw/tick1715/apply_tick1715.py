import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T21:05:00Z"
DATE = "2026-08-23"
EID = "cv_deauteurs"


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
        "name_nl": "deAuteurs cv (leftover NL-language AV/podium/literary collecting CV; NOT Sabam / SACD / SOFAM / Scam)",
        "name_fr": "deAuteurs sc (residuelle auteurs neerlandophones)",
        "name_en": "deAuteurs leftover Dutch-language authors collecting cooperative",
        "level": "other",
        "parent_id": "sec_federal",
        "community_language": "nl",
        "website": "https://www.deauteurs.be",
        "foi_email": "katrien.vanderperre@deauteurs.be",
        "foi_postal": "Koninklijke Prinsstraat 87 1050 Brussel",
        "notes": "tick1715 leftover deAuteurs after SACD/FARO/AGB/NSZ/APEFE-no-euros hunt; official JV2024 live; KBO 0837.299.149; FOI NBB YE2024/2025",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_deauteurs_jv2024_official",
        "title": "deAuteurs Jaarverslag 2024 (official org PDF; jaarcijfers + inningen)",
        "url": "https://wp.assets.sh/uploads/sites/1126/2025/06/Jaarverslag-dA-2024_online.pdf",
        "publisher": "deAuteurs cv",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1715; 47p; inningen 6973424; verdelingen 5276393; werkingskost/afhoudingen 1041058; personeel 396410; resultaat 99; members 2238",
    },
    {
        "source_id": "src_deauteurs_kbo",
        "title": "deAuteurs KBO 0837.299.149",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=837299149",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1715; CV; zetel Koninklijke Prinsstraat 87 1050; vergund MB 25.08.2011",
    },
    {
        "source_id": "src_deauteurs_portal",
        "title": "deAuteurs.be official portal",
        "url": "https://www.deauteurs.be",
        "publisher": "deAuteurs cv",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1715; MEDAA colocated with SACD/SOFAM",
    },
    {
        "source_id": "src_deauteurs_foi_contact_1715",
        "title": "deAuteurs FOI channel (algemeen directeur)",
        "url": "https://www.deauteurs.be",
        "publisher": "deAuteurs cv",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1715; katrien.vanderperre@deauteurs.be; Koninklijke Prinsstraat 87 1050 Brussel",
    },
    {
        "source_id": "src_apefe_ra2024_checked_no_budget",
        "title": "APEFE Rapport annuel 2024 checked (activity only; no budget euros)",
        "url": "https://www.apefe.org/wp-content/uploads/2025/06/APEFE_RA2024_final-light.pdf",
        "publisher": "APEFE",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1715; 76p activity; staff counts 20 HQ+52 abroad+6 expats; NO total budget/recettes euros — skipped for deAuteurs; APEFE full TCO FOI still ready",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_deauteurs_inningen_2024", "2024", "6973424", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 inningen totaal 6973424; tick1715"),
    ("bud_deauteurs_inningen_av_2024", "2024", "5162157", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 inningen audiovisueel 5162157; tick1715"),
    ("bud_deauteurs_inningen_podium_2024", "2024", "784941", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 inningen podiumkunsten 784941; tick1715"),
    ("bud_deauteurs_inningen_letter_2024", "2024", "1013410", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 inningen letterkundig/grafisch 1013410 JUMP (leenrecht objectivering); tick1715"),
    ("bud_deauteurs_inningen_audio_2024", "2024", "10839", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 inningen audiowerken 10839; tick1715"),
    ("bud_deauteurs_inningen_volgrecht_2024", "2024", "2077", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 volgrecht 2077 (via SOFAM); tick1715"),
    ("bud_deauteurs_verdelingen_2024", "2024", "5276393", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 verdelingen totaal 5276393; tick1715"),
    ("bud_deauteurs_werkingskost_2024", "2024", "1041058", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 werkingskost/statutaire afhoudingen 1041058 (=sum streams); tick1715"),
    ("bud_deauteurs_opbrengsten_2024", "2024", "1089085", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 totaal opbrengsten 1089085 (werkingskost 1041058 + andere 48027); tick1715"),
    ("bud_deauteurs_andere_opbr_2024", "2024", "48027", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 andere diverse opbrengsten 48027; tick1715"),
    ("bud_deauteurs_kosten_2024", "2024", "1088986", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 totaal kosten 1088986; tick1715"),
    ("bud_deauteurs_personeel_2024", "2024", "396410", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 personeelskosten 396410; VTE Unknown; tick1715"),
    ("bud_deauteurs_intercompany_2024", "2024", "357413", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 intercompany 357413 (SACD/SCAM backoffice share); tick1715"),
    ("bud_deauteurs_operationeel_2024", "2024", "257461", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 operationele kosten 257461; tick1715"),
    ("bud_deauteurs_representatie_2024", "2024", "15425", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 representatiekosten 15425; tick1715"),
    ("bud_deauteurs_bijdrage_belasting_2024", "2024", "62278", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 bijdrage/belastingen 62278; tick1715"),
    ("bud_deauteurs_pnl_2024", "2024", "99", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 resultaat 98.67 rounded 99; tick1715"),
    ("bud_deauteurs_late_payout_2024", "2024", "261432", "executed", "src_deauteurs_jv2024_official", "strong", "JV2024 rechten later dan wettelijke termijn uitbetaald 261432; tick1715"),
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
        "commitment_id": "comm_deauteurs_jv2024_werkingskost",
        "title": "deAuteurs JV2024 leftover NL authors CMO (werkingskost 1.04m / inningen 6.97m / verdelingen 5.28m)",
        "entity_id": EID,
        "beneficiary": "deAuteurs member authors AV/podium/literary/graphic",
        "legal_basis": "WVV CV; WER XI CMO; Bestuursdecreet openbaarheid",
        "decision_date": "2024-06-13",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "1041058",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://wp.assets.sh/uploads/sites/1126/2025/06/Jaarverslag-dA-2024_online.pdf",
        "stated_goal": "Local leftover deAuteurs map — official JV2024 werkingskost 1.04m; FOI NBB",
        "cut_option": "Do not treat inningen 6.97m as waste; scrutinise intercompany 0.36m + late payouts 0.26m; publish NBB YE2024/2025 + VTE",
        "source_id": "src_deauteurs_jv2024_official",
        "confidence": "strong",
        "hierarchy_path": "Belgie>Cultuur>deAuteurs>JV2024_L5",
        "notes": "tick1715; YE2024; werkingskost 1041058 inningen 6973424 verdelingen 5276393 personeel 396410 intercompany 357413 pnl ~99; members 2238; APEFE RA2024 checked no budget euros; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_deauteurs_werkingskost_1_04m_inningen_6_97m",
        "name": "deAuteurs JV2024 leftover NL authors CMO: werkingskost 1.04m / inningen 6.97m / intercompany 0.36m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Belgie>Cultuur>deAuteurs>JV2024_L5",
        "annual_cost_eur": "1041058",
        "total_cost_eur": "6973424",
        "tco_notes": "Leftover deAuteurs CV YE2024: statutaire afhoudingen/werkingskost 1.04m / totale kosten 1.09m / personeel 0.40m / intercompany 0.36m (SACD/SCAM) / inningen 6.97m / verdelingen 5.28m / late payouts 0.26m; pnl ~99; members 2238; VTE Unknown",
        "confidence": "strong",
        "source_id": "src_deauteurs_jv2024_official",
        "beneficiaries": "NL-language authors via deAuteurs",
        "stated_goal": "Local leftover deAuteurs map — official JV2024 live after SACD BE; APEFE RA2024 no euros",
        "measured_outcome": "Official deAuteurs JV2024 2026-08-23: werkingskost 1041058 / inningen 6973424 / verdelingen 5276393 / personeel 396410",
        "absurdity_score": "4.0",
        "cost_score": "4.0",
        "difficulty": "2.5",
        "priority_index": "3.9",
        "cut_proposal": "Do not treat inningen as waste; scrutinise intercompany 0.36m share + late-payout opacity; publish NBB + VTE",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1715; leftover after AGB unpublished / NSZ CDN403 / APEFE RA2024 no budget / SACD+FARO+SOFAM done; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_deauteurs_werkingskost_1_04m_inningen_6_97m_nbb_vte_l5",
        "hierarchy_path": "Belgie>Cultuur>deAuteurs>JV2024_L5",
        "entity_id": EID,
        "what_is_missing": "Official JV2024 publishes inningen 6973424 / verdelingen 5276393 / werkingskost/afhoudingen 1041058 / kosten 1088986 / personeel 396410 / intercompany 357413 / pnl ~99 / late payouts 261432 / members 2238; NBB statutory YE2024/YE2025 PDF deposit id Unknown (companyweb pointer neergelegd 11.07.2026); exact VTE Unknown; AV notulen for YE2024 approval; intercompany SACD/SCAM split detail",
        "why_it_matters": "Leftover Belgian NL-language collecting society with live official YE2024 euros (1.04m management / 6.97m inningen) — need NBB reconcile + VTE",
        "priority": "7",
        "recipient_body": "deAuteurs cv / Bestuursorgaan / Algemeen directeur",
        "recipient_email": "katrien.vanderperre@deauteurs.be",
        "recipient_postal": "Koninklijke Prinsstraat 87 1050 Brussel",
        "draft_letter_path": "docs/doge/foi/drafts/gap_deauteurs_werkingskost_1_04m_inningen_6_97m_nbb_vte_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_deauteurs_jv2024_werkingskost",
        "linked_leaderboard_id": "lb_deauteurs_werkingskost_1_04m_inningen_6_97m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1715; human-send only; APEFE RA2024 checked no budget euros this tick; NSZ/Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight/Welzijnszorg/SOFAM/FARO/SACD FOI still ready",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1715":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_deauteurs_werkingskost_1_04m_inningen_6_97m_nbb_vte_l5"
        r["notes"] = "DONE tick1715: deAuteurs KBO 0837.299.149 JV2024 werkingskost 1041058 inningen 6973424 verdelingen 5276393; APEFE RA2024 checked NO budget euros; FOI ready gap_deauteurs_werkingskost_1_04m_inningen_6_97m_nbb_vte_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1716",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1716 after 1715 deAuteurs JV2024. Next every-10 is 1720. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo deAuteurs/SACD/FARO/SOFAM/Welzijnszorg/PlayRight/SIMIM/Reprobel/Auvibel/Sabam/NSZ.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if JR/budget euros live, LaScam if RA2024/2025 PDF live, GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1715 deAuteurs; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE-if-euros/LaScam/GO!/POV/BVAS/IOED/HVZ/IGS; deAuteurs+SACD+FARO+SOFAM DONE; APEFE RA2024 no euros; next every-10 1720",
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
        "last_unit_id": "rq_1715",
        "ticks_completed": "1715",
        "paused": "no",
        "notes": "tick1715 leftover deAuteurs CV residual; KBO 0837.299.149; official Jaarverslag 2024 PDF live; sourced euros inningen 6973424 verdelingen 5276393 werkingskost 1041058 opbr 1089085 kosten 1088986 personeel 396410 intercompany 357413 pnl ~99 late_payouts 261432 members 2238; NBB deposit Unknown; APEFE RA2024 checked NO budget euros (staff counts only); FOI ready NBB/VTE; NSZ still CDN 403; Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight/Welzijnszorg/SOFAM/FARO/SACD FOI still ready; Natuurpunt opaque; Dijk92 CDN 403; AGB unpublished; LaScam RA2024 not yet on rapports page; NOT every-10 (next 1720); next rq_1716 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE-if-euros/LaScam/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
