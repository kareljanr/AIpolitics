import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T20:45:00Z"
DATE = "2026-08-23"
EID = "ogc_sacd_be"


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
        "name_nl": "SACD België / Société des Auteurs et Compositeurs Dramatiques (leftover FR CMO Belgian branch; NOT Sabam / deAuteurs / SOFAM / SCAM)",
        "name_fr": "SACD Belgique / Societe des Auteurs et Compositeurs Dramatiques (succursale residuelle)",
        "name_en": "SACD Belgium leftover French dramatic/AV authors collecting society Belgian branch",
        "level": "other",
        "parent_id": "sec_federal",
        "community_language": "fr",
        "website": "https://www.sacd.be",
        "foi_email": "info@sacd.be",
        "foi_postal": "Rue du Prince Royal 85-87 1050 Bruxelles",
        "notes": "tick1714 leftover SACD BE after FARO/SOFAM/AGB/NSZ hunt; official RA2025 Art.23 live; French SACD Belgian succursale at MEDAA; Belgian establishment KBO Unknown; FOI KBO/NBB",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_sacd_be_ra2025_official",
        "title": "SACD Belgique Rapport annuel 2025 (official Art.23 + gestion)",
        "url": "https://sacd.be/images/Documents_SACD/SACD-RapportAnnuel-2025-WEB.pdf",
        "publisher": "SACD Belgique",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1714; 76p; Art.23 p71-73 droits_percus 19666713 frais_nets 2710153 ratio 13.78pct; staff 29/27.78 ETP; action culturelle 162000",
    },
    {
        "source_id": "src_sacd_be_portal",
        "title": "SACD.be official portal",
        "url": "https://www.sacd.be",
        "publisher": "SACD Belgique",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1714; Rue du Prince Royal 85-87 MEDAA; info@sacd.be; +32 2 551 03 42",
    },
    {
        "source_id": "src_sacd_be_medaa_pointer",
        "title": "MEDAA house pointer (SACD colocated; KBO 0457.701.032 MEDAA itself)",
        "url": "https://medaa.be/",
        "publisher": "MEDAA",
        "accessed_date": DATE,
        "source_class": "secondary",
        "notes": "tick1714; SACD BE shares MEDAA building; MEDAA KBO not SACD; SACD Belgian establishment KBO still Unknown",
    },
    {
        "source_id": "src_sacd_be_foi_contact_1714",
        "title": "SACD Belgique FOI channel (info@sacd.be)",
        "url": "https://www.sacd.be/fr/services",
        "publisher": "SACD Belgique",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1714; info@sacd.be; +32 2 551 03 42; Rue du Prince Royal 85-87 1050 Bruxelles",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_sacd_be_droits_percus_2025", "2025", "19666713", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 A droits percUS 19666713 (SPF Eco definition; excl deAuteurs brut fiscal); tick1714"),
    ("bud_sacd_be_droits_sv_2025", "2025", "5822309", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 A spectacle vivant 5822309; tick1714"),
    ("bud_sacd_be_droits_av_2025", "2025", "6446665", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 A audiovisuel 6446665; tick1714"),
    ("bud_sacd_be_droits_cable_2025", "2025", "6557919", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 A cable 6557919; tick1714"),
    ("bud_sacd_be_droits_copie_privee_2025", "2025", "708562", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 A copie privee 708562; tick1714"),
    ("bud_sacd_be_droits_repartis_payes_2025", "2025", "22093833", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 E droits percUS repartis=payes 22093833; tick1714"),
    ("bud_sacd_be_droits_non_repartis_dettes_2025", "2025", "22499053", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 F droits percUS non encore repartis dettes 22499053 (BE+siege); tick1714"),
    ("bud_sacd_be_droits_attente_paiement_2025", "2025", "1793624", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 G droits repartis en attente paiement 1793624; tick1714"),
    ("bud_sacd_be_frais_total_2025", "2025", "2911486", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 Partie2 A total frais 2911486 (nets + action culturelle + fonds organique); tick1714"),
    ("bud_sacd_be_frais_nets_2025", "2025", "2710153", "executed", "src_sacd_be_ra2025_official", "strong", "Art.23 Partie2 B frais nets gestion 2710153; ratio 13.78pct; tick1714"),
    ("bud_sacd_be_depenses_nettes_2025", "2025", "2749486", "executed", "src_sacd_be_ra2025_official", "strong", "RA2025 p65 depenses nettes globales 2749486 (hors Action culturelle); budget revise was 2860851; tick1714"),
    ("bud_sacd_be_budget_revise_2025", "2025", "2860851", "budgeted", "src_sacd_be_ra2025_official", "strong", "RA2025 p65 budget revise CA 2860851 (72pct personnel); tick1714"),
    ("bud_sacd_be_action_culturelle_2025", "2025", "162000", "executed", "src_sacd_be_ra2025_official", "strong", "RA2025 action culturelle budget 162000 (direct soutiens 132000=82pct); tick1714"),
    ("bud_sacd_be_encaissements_avant_partage_2025", "2025", "31331540", "executed", "src_sacd_be_ra2025_official", "medium", "RA2025 p52 encaissements avant partage 31331540 INCLUDES Sofam/deAuteurs/LaScam representation — not pure SACD; tick1714"),
    ("bud_sacd_be_perceptions_membres_sacd_2025", "2025", "17761040", "executed", "src_sacd_be_ra2025_official", "strong", "RA2025 p53 perceptions delegation belge membres SACD only 17761040; tick1714"),
    ("bud_sacd_be_repartis_membres_be_2025", "2025", "6657133", "executed", "src_sacd_be_ra2025_official", "strong", "RA2025 p53/54 repartis a membres residant BE 6657133; tick1714"),
    ("bud_sacd_be_factures_non_encaissees_2025", "2025", "2026724", "executed", "src_sacd_be_ra2025_official", "strong", "RA2025 p67 factures non encaissees fin 2025 2026724; tick1714"),
    ("bud_sacd_be_fonds_organique_2025", "2025", "39334", "executed", "src_sacd_be_ra2025_official", "strong", "RA2025 p66 contribution fonds organique 39334; tick1714"),
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
        "commitment_id": "comm_sacd_be_ra2025_frais_nets",
        "title": "SACD Belgique RA2025 leftover FR CMO Belgian branch (frais nets 2.71m / droits percUS 19.7m / droits dettes 22.5m)",
        "entity_id": EID,
        "beneficiary": "SACD members / dramatic AV literary authors in Belgium",
        "legal_basis": "CDE OGC Art.23 AR 25.04.2014; French SACD Belgian succursale; Bestuursdecreet / openbaarheid",
        "decision_date": "2026-05-28",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "2710153",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://sacd.be/images/Documents_SACD/SACD-RapportAnnuel-2025-WEB.pdf",
        "stated_goal": "Local leftover SACD BE map — official RA2025 Art.23 frais nets 2.71m; FOI Belgian KBO/NBB",
        "cut_option": "Do not treat droits dettes 22.5m as waste; scrutinise 13.78pct management ratio + 72pct personnel share; publish Belgian establishment KBO/NBB",
        "source_id": "src_sacd_be_ra2025_official",
        "confidence": "strong",
        "hierarchy_path": "Belgie>Cultuur>SACD_BE>RA2025_L5",
        "notes": "tick1714; YE2025 Art.23; frais_nets 2710153 droits_percus 19666713 droits_non_repartis 22499053 staff 27.78 ETP; Belgian establishment KBO Unknown; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_sacd_be_frais_nets_2_71m_droits_19_7m_dettes_22_5m",
        "name": "SACD Belgique RA2025 leftover FR CMO Belgian branch: frais nets 2.71m / droits 19.7m / dettes 22.5m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Belgie>Cultuur>SACD_BE>RA2025_L5",
        "annual_cost_eur": "2710153",
        "total_cost_eur": "22499053",
        "tco_notes": "Leftover SACD BE YE2025 Art.23: frais nets gestion 2.71m (ratio 13.78pct) / total frais 2.91m / droits percUS 19.7m / droits non repartis dettes 22.5m fiduciary; staff 29 / 27.78 ETP; 72pct personnel in budget; action culturelle 0.16m",
        "confidence": "strong",
        "source_id": "src_sacd_be_ra2025_official",
        "beneficiaries": "Dramatic/AV/literary authors via SACD Belgium",
        "stated_goal": "Local leftover SACD BE map — official RA2025 Art.23 live after SOFAM/Sabam/Auvibel/Reprobel/SIMIM/PlayRight",
        "measured_outcome": "Official SACD BE RA2025 2026-08-23: frais_nets 2710153 / droits_percus 19666713 / droits_non_repartis 22499053 / ETP 27.78",
        "absurdity_score": "4.5",
        "cost_score": "5.0",
        "difficulty": "2.5",
        "priority_index": "4.6",
        "cut_proposal": "Do not treat droits dettes 22.5m as waste; scrutinise 13.78pct management ratio vs peers; publish Belgian establishment KBO + NBB branch accounts",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1714; leftover after AGB unpublished / NSZ CDN403 / FARO+SOFAM done; French succursale; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_sacd_be_frais_nets_2_71m_droits_19_7m_kbo_nbb_l5",
        "hierarchy_path": "Belgie>Cultuur>SACD_BE>RA2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official RA2025 Art.23 publishes droits percUS 19666713 / frais nets 2710153 / ratio 13.78pct / droits non repartis dettes 22499053 / staff 29 / 27.78 ETP / action culturelle 162000; Belgian establishment KBO number Unknown (French SACD succursale at MEDAA Rue du Prince Royal 85-87); NBB Belgian branch statutory accounts / deposit id Unknown; retenue statutaire taken at French siege (0 in BE Art.23); remuneration Comite belge/Dirigeant amounts truncated in extract",
        "why_it_matters": "Leftover FR dramatic/AV collecting society Belgian branch with live official YE2025 Art.23 euros (2.71m management / 19.7m droits / 22.5m fiduciary dettes) — need Belgian KBO + NBB reconcile",
        "priority": "7",
        "recipient_body": "SACD Belgique / Delegation generale / Comite belge",
        "recipient_email": "info@sacd.be",
        "recipient_postal": "Rue du Prince Royal 85-87 1050 Bruxelles",
        "draft_letter_path": "docs/doge/foi/drafts/gap_sacd_be_frais_nets_2_71m_droits_19_7m_kbo_nbb_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_sacd_be_ra2025_frais_nets",
        "linked_leaderboard_id": "lb_sacd_be_frais_nets_2_71m_droits_19_7m_dettes_22_5m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1714; human-send only; NSZ/Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight/Welzijnszorg/SOFAM/FARO FOI still ready",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1714":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_sacd_be_frais_nets_2_71m_droits_19_7m_kbo_nbb_l5"
        r["notes"] = "DONE tick1714: SACD BE RA2025 Art.23 frais_nets 2710153 droits_percus 19666713 droits_non_repartis 22499053 staff 27.78 ETP; FOI ready gap_sacd_be_frais_nets_2_71m_droits_19_7m_kbo_nbb_l5; Belgian KBO Unknown"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1715",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1715 after 1714 SACD BE RA2025. Next every-10 is 1720. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs / Northdata deposit→CDN. Do NOT redo SACD/FARO/SOFAM/Welzijnszorg/PlayRight/SIMIM/Reprobel/Auvibel/Sabam/NSZ/FBM/Biovia/Medvia/BlauweCluster.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE RA2024 if euros live, deAuteurs/LaScam if unused live, GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1714 SACD BE; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/deAuteurs/LaScam/GO!/POV/BVAS/IOED/HVZ/IGS; SACD+FARO+SOFAM DONE; next every-10 1720",
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
        "last_unit_id": "rq_1714",
        "ticks_completed": "1714",
        "paused": "no",
        "notes": "tick1714 leftover SACD Belgique FR CMO Belgian branch residual; official Rapport annuel 2025 PDF live sacd.be Art.23; sourced euros frais_nets 2710153 total_frais 2911486 droits_percus 19666713 droits_repartis 22093833 droits_non_repartis_dettes 22499053 depenses 2749486 action_culturelle 162000 staff 29/27.78 ETP ratio 13.78pct; Belgian establishment KBO Unknown; FOI ready KBO/NBB; NSZ still CDN 403; Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight/Welzijnszorg/SOFAM/FARO FOI still ready; Natuurpunt opaque; Dijk92 CDN 403; APEFE RA2024 PDF live unused; AGB unpublished; NOT every-10 (next 1720); next rq_1715 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE/deAuteurs/LaScam/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
