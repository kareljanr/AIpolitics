import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-23T21:25:00Z"
DATE = "2026-08-23"
EID = "ogc_scam_be"


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
        "name_nl": "LaScam / Scam België (leftover FR CMO Belgian branch documentary/écrit/AV; NOT SACD / deAuteurs / Sabam)",
        "name_fr": "LaScam Belgique / Societe civile des auteurs multimedia (succursale residuelle)",
        "name_en": "LaScam Belgium leftover French multimedia authors collecting society Belgian branch",
        "level": "other",
        "parent_id": "sec_federal",
        "community_language": "fr",
        "website": "https://www.scam.be",
        "foi_email": "info@scam.be",
        "foi_postal": "Rue du Prince Royal 87 1050 Bruxelles",
        "notes": "tick1716 leftover LaScam BE after deAuteurs/SACD/AGB/NSZ hunt; official RA2025 Art.23 live; KBO 0425.440.416; French succursale MEDAA; FOI NBB",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_scam_be_ra2025_official",
        "title": "LaScam Belgique Rapport annuel 2025 (official Art.23 + gestion)",
        "url": "https://www.scam.be/uploads/2026/06/WEB-260603_SCAM-RapportAnnuel-2025.pdf",
        "publisher": "LaScam Belgique",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1716; Art.23 droits_percus 9609149 frais_nets 1423856 ratio 14.82pct; staff 12/10 ETP; depenses 1443074; action culturelle BE ecrit 290125",
    },
    {
        "source_id": "src_scam_be_rapports_portal",
        "title": "LaScam Belgique statuts reglement et rapports annuels portal",
        "url": "https://www.scam.be/centre-de-ressources/statuts-reglement-et-rapports-annuels/",
        "publisher": "LaScam Belgique",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1716; lists RA2025 + RA2024; prior tick1715 said RA2024 not on page — RA2025 now live",
    },
    {
        "source_id": "src_scam_be_kbo",
        "title": "LaScam / Scam Belgique KBO 0425.440.416",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=425440416",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1716; BCE BE 0425.440.416 from official tarifaires PDF; Rue du Prince Royal 87",
    },
    {
        "source_id": "src_scam_be_foi_contact_1716",
        "title": "LaScam Belgique FOI channel (info@scam.be)",
        "url": "https://www.scam.be",
        "publisher": "LaScam Belgique",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1716; info@scam.be; +32 2 551 03 20; Rue du Prince Royal 87 1050 Bruxelles",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_scam_be_droits_percus_2025", "2025", "9609149", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 A droits percUS 9609149 (SPF Eco def; excl deAuteurs); tick1716"),
    ("bud_scam_be_droits_av_2025", "2025", "3063295", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 A communication publique AV 3063295; tick1716"),
    ("bud_scam_be_droits_cable_2025", "2025", "4546005", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 A cable 4546005; tick1716"),
    ("bud_scam_be_droits_copie_privee_2025", "2025", "878471", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 A copie privee 878471; tick1716"),
    ("bud_scam_be_droits_repro_2025", "2025", "665600", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 A reprographie 665600; tick1716"),
    ("bud_scam_be_droits_enseignement_2025", "2025", "270646", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 A enseignement/recherche 270646; tick1716"),
    ("bud_scam_be_droits_pret_2025", "2025", "184798", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 A pret public 184798; tick1716"),
    ("bud_scam_be_retenue_statutaire_2025", "2025", "127425", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 B retenue statutaire succursale 127425; tick1716"),
    ("bud_scam_be_droits_repartis_payes_2025", "2025", "9292831", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 E droits percUS repartis=payes 9292831; tick1716"),
    ("bud_scam_be_droits_non_repartis_dettes_2025", "2025", "14386973", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 F droits non repartis dettes 14386973 (BE+siege); tick1716"),
    ("bud_scam_be_droits_attente_paiement_2025", "2025", "1156501", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 G droits repartis attente paiement 1156501; tick1716"),
    ("bud_scam_be_frais_total_2025", "2025", "1554474", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 Partie2 A total frais 1554474; tick1716"),
    ("bud_scam_be_frais_nets_2025", "2025", "1423856", "executed", "src_scam_be_ra2025_official", "strong", "Art.23 Partie2 B frais nets 1423856; ratio 14.82pct; tick1716"),
    ("bud_scam_be_depenses_nettes_2025", "2025", "1443074", "executed", "src_scam_be_ra2025_official", "strong", "RA2025 depenses nettes 1443074 (budget revise 1529206; 65pct personnel); tick1716"),
    ("bud_scam_be_budget_revise_2025", "2025", "1529206", "budgeted", "src_scam_be_ra2025_official", "strong", "RA2025 budget revise CA 1529206 hors Action culturelle; tick1716"),
    ("bud_scam_be_perceptions_narrative_2025", "2025", "9566536", "executed", "src_scam_be_ra2025_official", "strong", "RA2025 narrative perceptions 9566536 (-13pct vs 2024); Art.23 A 9609149 differs by siege/deAuteurs adjust; tick1716"),
    ("bud_scam_be_repartis_membres_be_2025", "2025", "3577432", "executed", "src_scam_be_ra2025_official", "strong", "RA2025 20 repartitions total 3577432 to 2752 auteurs residant BE; tick1716"),
    ("bud_scam_be_action_culturelle_fr_2025", "2025", "111400", "executed", "src_scam_be_ra2025_official", "strong", "RA2025 action culturelle financed 111400 from FR copie privee 25pct; tick1716"),
    ("bud_scam_be_bourses_ecrit_be_2025", "2025", "290125", "executed", "src_scam_be_ra2025_official", "strong", "RA2025 BE 10pct droits ecrit bourses 290124.68 rounded 290125; 540 beneficiaires; tick1716"),
    ("bud_scam_be_remuneration_comite_delegue_2025", "2025", "128730", "executed", "src_scam_be_ra2025_official", "strong", "RA2025 remun+avantages Delegue+Comite 128729.97; tick1716"),
    ("bud_scam_be_fonds_organique_2025", "2025", "19218", "executed", "src_scam_be_ra2025_official", "strong", "RA2025 contribution fonds organique 19218; tick1716"),
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
        "commitment_id": "comm_scam_be_ra2025_frais_nets",
        "title": "LaScam Belgique RA2025 leftover FR CMO Belgian branch (frais nets 1.42m / droits percUS 9.61m / dettes 14.4m)",
        "entity_id": EID,
        "beneficiary": "LaScam members / documentary AV literary authors in Belgium",
        "legal_basis": "CDE OGC Art.23 AR 25.04.2014; French Scam Belgian succursale; Bestuursdecreet openbaarheid",
        "decision_date": "2026-06-03",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "1423856",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.scam.be/uploads/2026/06/WEB-260603_SCAM-RapportAnnuel-2025.pdf",
        "stated_goal": "Local leftover LaScam BE map — official RA2025 Art.23 frais nets 1.42m; FOI NBB",
        "cut_option": "Do not treat droits dettes 14.4m as waste; scrutinise 14.82pct management ratio + 65pct personnel; publish NBB branch accounts",
        "source_id": "src_scam_be_ra2025_official",
        "confidence": "strong",
        "hierarchy_path": "Belgie>Cultuur>LaScam_BE>RA2025_L5",
        "notes": "tick1716; YE2025 Art.23; frais_nets 1423856 droits_percus 9609149 droits_non_repartis 14386973 staff 10 ETP; KBO 0425.440.416; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_scam_be_frais_nets_1_42m_droits_9_61m_dettes_14_4m",
        "name": "LaScam Belgique RA2025 leftover FR CMO Belgian branch: frais nets 1.42m / droits 9.61m / dettes 14.4m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Belgie>Cultuur>LaScam_BE>RA2025_L5",
        "annual_cost_eur": "1423856",
        "total_cost_eur": "14386973",
        "tco_notes": "Leftover LaScam BE YE2025 Art.23: frais nets 1.42m (ratio 14.82pct) / total frais 1.55m / droits percUS 9.61m / droits non repartis dettes 14.4m fiduciary; staff 12/10 ETP; 65pct personnel; remun Comite+Delegue 0.13m; bourses ecrit BE 0.29m",
        "confidence": "strong",
        "source_id": "src_scam_be_ra2025_official",
        "beneficiaries": "Documentary/AV/literary authors via LaScam Belgium",
        "stated_goal": "Local leftover LaScam BE map — official RA2025 Art.23 newly live after deAuteurs/SACD",
        "measured_outcome": "Official LaScam BE RA2025 2026-08-23: frais_nets 1423856 / droits_percus 9609149 / droits_non_repartis 14386973 / ETP 10",
        "absurdity_score": "4.5",
        "cost_score": "4.5",
        "difficulty": "2.5",
        "priority_index": "4.4",
        "cut_proposal": "Do not treat droits dettes 14.4m as waste; scrutinise 14.82pct management ratio vs peers; publish NBB branch accounts",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1716; leftover after AGB unpublished / NSZ CDN403 / deAuteurs+SACD+FARO done; French succursale KBO 0425.440.416; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_scam_be_frais_nets_1_42m_droits_9_61m_nbb_l5",
        "hierarchy_path": "Belgie>Cultuur>LaScam_BE>RA2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official RA2025 Art.23 publishes droits percUS 9609149 / frais nets 1423856 / ratio 14.82pct / droits non repartis dettes 14386973 / staff 12 / 10 ETP / depenses 1443074 / remun Comite+Delegue 128730 / bourses ecrit 290125; NBB Belgian branch statutory accounts / deposit id Unknown; narrative perceptions 9566536 vs Art.23 A 9609149 reconcile; RA2024 PDF if separate full Art.23",
        "why_it_matters": "Leftover FR multimedia collecting society Belgian branch with live official YE2025 Art.23 euros (1.42m management / 9.61m droits / 14.4m fiduciary dettes) — need NBB reconcile",
        "priority": "7",
        "recipient_body": "LaScam Belgique / Delegation generale / Comite belge",
        "recipient_email": "info@scam.be",
        "recipient_postal": "Rue du Prince Royal 87 1050 Bruxelles",
        "draft_letter_path": "docs/doge/foi/drafts/gap_scam_be_frais_nets_1_42m_droits_9_61m_nbb_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_scam_be_ra2025_frais_nets",
        "linked_leaderboard_id": "lb_scam_be_frais_nets_1_42m_droits_9_61m_dettes_14_4m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1716; human-send only; NSZ/Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight/Welzijnszorg/SOFAM/FARO/SACD/deAuteurs FOI still ready",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1716":
        r["status"] = "done"
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_scam_be_frais_nets_1_42m_droits_9_61m_nbb_l5"
        r["notes"] = "DONE tick1716: LaScam BE KBO 0425.440.416 RA2025 Art.23 frais_nets 1423856 droits_percus 9609149 droits_non_repartis 14386973 staff 10 ETP; FOI ready gap_scam_be_frais_nets_1_42m_droits_9_61m_nbb_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1717",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1717 after 1716 LaScam BE RA2025. Next every-10 is 1720. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo LaScam/deAuteurs/SACD/FARO/SOFAM/Welzijnszorg/PlayRight/SIMIM/Reprobel/Auvibel/Sabam/NSZ.... Prefer leftover AGB/APB if PDF live, else NatuurpuntVZW if CDN, NSZ if CDN 200, Bosgroep residual, Dijk92 if JR euros, APEFE if budget euros, GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1716 LaScam BE; NEXT AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE-if-euros/GO!/POV/BVAS/IOED/HVZ/IGS; LaScam+deAuteurs+SACD+FARO+SOFAM DONE; next every-10 1720",
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
        "last_unit_id": "rq_1716",
        "ticks_completed": "1716",
        "paused": "no",
        "notes": "tick1716 leftover LaScam Belgique FR CMO Belgian branch residual; KBO 0425.440.416; official Rapport annuel 2025 PDF live scam.be Art.23; sourced euros frais_nets 1423856 total_frais 1554474 droits_percus 9609149 droits_repartis 9292831 droits_non_repartis_dettes 14386973 depenses 1443074 repartis_BE 3577432 bourses_ecrit 290125 remun_comite 128730 staff 12/10 ETP ratio 14.82pct; FOI ready NBB; NSZ still CDN 403; Blauwe/Sabam/Auvibel/Reprobel/SIMIM/PlayRight/Welzijnszorg/SOFAM/FARO/SACD/deAuteurs FOI still ready; Natuurpunt opaque; Dijk92 CDN 403; APEFE no budget euros; AGB unpublished; NOT every-10 (next 1720); next rq_1717 AGB/NatuurpuntVZW/NSZ-if-200/Bosgroep/Dijk92/APEFE-if-euros/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
