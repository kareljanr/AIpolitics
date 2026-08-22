import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T08:10:00Z"
DATE = "2026-08-24"
EID = "igs_hvriv"
GAP = "gap_hvriv_spend_36_63m_pers_26_60m_rekening_l5"
COMM = "comm_hvriv_jr2025_spend"
LB = "lb_hvriv_spend_36_63m_pers_26_60m"
PDF = "https://www.willebroek.be/sites/default/files/public/Brandweer/Vereenvoudigde%20voorstelling%20rekening%202025.pdf"
PDF_FULL = "https://www.willebroek.be/sites/default/files/public/Brandweer/Jaarrekening%202025.pdf"


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
        "name_nl": "Brandweerzone Rivierenland / HVZ Rivierenland (leftover IGS hulpverleningszone of mined Mechelen+Willebroek+Bornem; NOT Meetjesland/Midwest/Kempen)",
        "name_fr": "Zone de secours Rivierenland (IGS residuel / zone de secours)",
        "name_en": "Rivierenland fire-rescue zone leftover IGS of mined Mechelen belt municipalities",
        "level": "other",
        "parent_id": "city_mechelen",
        "community_language": "nl",
        "website": "https://rivierenland.hulpverleningszone.be/",
        "foi_email": "info@bwzr.be",
        "foi_postal": "Plattebeekstraat 11 2800 Mechelen",
        "notes": "tick1748 leftover HVZ Rivierenland after Zusterhof; KBO/BTW 0500.913.839; official vereenvoudigde rekening 2025 on willebroek.be; zoneraad 03.04.2026; spend 36626383 pers 26595196; full JR image-only; FOI ready",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_hvriv_jr2025_vereenvoudigd",
        "title": "HVZ Rivierenland Vereenvoudigde voorstelling rekening 2025",
        "url": PDF,
        "publisher": "Brandweerzone Rivierenland / Stad Willebroek portal",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1748; zoneraad 03.04.2026; gewone uitgaven 36626383 pers 26595196 ontvangsten 33781156 gemdot 20853368 fed brand 6616305 fed DGH 3319025 invest 3707455; globaal saldo 3414106",
    },
    {
        "source_id": "src_hvriv_jr2025_full_pdf",
        "title": "HVZ Rivierenland full Jaarrekening 2025 PDF (image-only extract)",
        "url": PDF_FULL,
        "publisher": "Brandweerzone Rivierenland / Stad Willebroek portal",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1748; 47p ~7.4MB image-only OCR empty; euros from vereenvoudigde; FOI text/balans",
    },
    {
        "source_id": "src_hvriv_bekendmaking",
        "title": "HVZ Rivierenland bekendmaking rekening 2025",
        "url": "https://www.willebroek.be/sites/default/files/public/Brandweer/bekendmaking%20rekening%202025_hulpverleningszone%20Rivierenland.pdf",
        "publisher": "Brandweerzone Rivierenland",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1748; zoneraad 03.04.2026; inzage 13-27.04.2026; zonesecretaris Maaike Bryssinck; voorzitter Bart Somers",
    },
    {
        "source_id": "src_hvriv_kbo",
        "title": "HVZ Rivierenland KBO/BTW 0500.913.839",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=500913839",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1748; BTW BE 0500.913.839; zetel Plattebeekstraat 11 2800 Mechelen; facturatie Dijleweg 5 2850 Boom",
    },
    {
        "source_id": "src_hvriv_foi_contact_1748",
        "title": "HVZ Rivierenland FOI channel",
        "url": "https://rivierenland.hulpverleningszone.be/pagina/contactgegevens",
        "publisher": "Brandweerzone Rivierenland",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1748; info@bwzr.be; financien@bwzr.be; Plattebeekstraat 11 2800 Mechelen",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_hvriv_uitgaven_gewone_2025", "2025", "36626383", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Gewone uitgaven rekening 2025 36626383; tick1748"),
    ("bud_hvriv_pers_brandweer_2025", "2025", "26595196", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Personeel brandweer 26595196; VTE unpublished; tick1748"),
    ("bud_hvriv_werking_brandweer_2025", "2025", "6739159", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Werkingskosten brandweer 6739159; tick1748"),
    ("bud_hvriv_werking_dgh_2025", "2025", "261758", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Werkingskosten DGH 261758; tick1748"),
    ("bud_hvriv_schuld_aflossing_2025", "2025", "2012781", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Schuld aflossingen 2012781; tick1748"),
    ("bud_hvriv_schuld_intrest_2025", "2025", "774295", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Schuld intresten 774295; tick1748"),
    ("bud_hvriv_ontvangsten_gewone_2025", "2025", "33781156", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Gewone ontvangsten 33781156; tick1748"),
    ("bud_hvriv_gemdot_exploitatie_2025", "2025", "20853368", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Gemeentedotaties exploitatie 20853368; per-gemeente FOI; tick1748"),
    ("bud_hvriv_fed_brandweer_2025", "2025", "6616305", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Fed brandweer basis 1329767 + bijkomende/seveso 5286538 = 6616305; tick1748"),
    ("bud_hvriv_fed_dgh_2025", "2025", "3319025", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Fed DGH 3319025 JUMP vs begroting 1918925; tick1748"),
    ("bud_hvriv_prestaties_2025", "2025", "2600351", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Prestaties interventie 1490105 + DGH 692302 + overige 417944 = 2600351; tick1748"),
    ("bud_hvriv_invest_uitgaven_2025", "2025", "3707455", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Buitengewone investeringen 3707455; tick1748"),
    ("bud_hvriv_invest_gemdot_2025", "2025", "500000", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Investeringsdotaties gemeenten 500000; tick1748"),
    ("bud_hvriv_saldo_gewone_2025", "2025", "3414106", "executed", "src_hvriv_jr2025_vereenvoudigd", "strong", "Saldo gewone dienst / globaal 3414106; tick1748"),
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
        "title": "HVZ Rivierenland JR2025 leftover IGS (spend 36.63m / pers 26.60m / gemdot 20.85m)",
        "entity_id": EID,
        "beneficiary": "HVZ Rivierenland / dual mined Mechelen belt + Bornem / municipal + federal civiele-veiligheid",
        "legal_basis": "Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid",
        "decision_date": "2026-04-03",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "36626383",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": PDF,
        "stated_goal": "Local leftover IGS fire-rescue map VL Rivierenland — spend 36.63m / pers 26.60m / unpublished full balans",
        "cut_option": "Publish full rekening balans+VTE+per-gemeente gemdot split; scrutinise staff 26.6m (~73% of ordinary spend); map fed DGH JUMP",
        "source_id": "src_hvriv_jr2025_vereenvoudigd",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Mechelen>IGS>HVZ_Rivierenland>JR2025_L5",
        "notes": "tick1748; uitgaven_gewone 36626383 pers 26595196 ontvangsten 33781156 gemdot 20853368 fed 9935330 invest 3707455; full PDF image-only; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "HVZ Rivierenland JR2025: spend 36.63m / pers 26.60m / gemdot 20.85m",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Gemeenten>Mechelen>IGS>HVZ_Rivierenland>JR2025_L5",
        "annual_cost_eur": "36626383",
        "total_cost_eur": "36626383",
        "tco_notes": "Leftover HVZ Rivierenland JR2025 vereenvoudigde rekening: gewone uitgaven 36.63m (pers brandweer 26.60m ~73% / werking brand 6.74m / DGH werking 0.26m / schuld aflossing 2.01m / intrest 0.77m); ontvangsten 33.78m (gemdot expl 20.85m / fed brand 6.62m / fed DGH 3.32m JUMP vs budget 1.92m / prestaties 2.60m); invest 3.71m; saldo gewone 3.41m; full 47p JR PDF image-only; VTE + balans + per-gemeente gemdot unpublished; zone includes Bornem (AGB Bornem still JR2024-only)",
        "confidence": "strong",
        "source_id": "src_hvriv_jr2025_vereenvoudigd",
        "beneficiaries": "Rivierenland residents / municipal + federal civiele-veiligheid",
        "stated_goal": "Local leftover HVZ Rivierenland map — official JR2025 after Zusterhof residual",
        "measured_outcome": "Official vereenvoudigde rekening 2026-08-24: uitgaven 36626383 / pers 26595196 / gemdot 20853368 / fed brand+DGH 9935330 / invest 3707455 / saldo 3414106",
        "absurdity_score": "4.5",
        "cost_score": "6.5",
        "difficulty": "2.5",
        "priority_index": "5.5",
        "cut_proposal": "Publish full balans+VTE+per-gemeente gemdot; scrutinise staff share ~73%; disclose fed DGH JUMP mechanism; stop image-only public rekening",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1748; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / Vivalto CDN trio done; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Gemeenten>Mechelen>IGS>HVZ_Rivierenland>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official vereenvoudigde rekening publishes uitgaven gewone 36626383 / pers 26595196 / gemdot 20853368 / fed 9935330 / invest 3707455; full rekening balans/expl/PnL/VTE/per-gemeente gemdot split and text-extractable JR PDF unpublished (47p image-only)",
        "why_it_matters": "Large HVZ with 36.6m ordinary spend and 26.6m staff (~73%) plus 20.9m municipal dots — need VTE + per-gemeente transparency for public safety euros",
        "priority": "8",
        "recipient_body": "Brandweerzone Rivierenland / dienst openbaarheid / zonesecretaris",
        "recipient_email": "info@bwzr.be",
        "recipient_postal": "Plattebeekstraat 11 2800 Mechelen",
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
        "notes": "tick1748; human-send only; also financien@bwzr.be; AGB/NSZ/Dijk92/APEFE still blocked preferred path",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1748":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = "HVZ Rivierenland JR2025 leftover dual residual"
        r["notes"] = "DONE tick1748: HVZ Rivierenland KBO 0500.913.839 JR2025 vereenvoudigde spend 36626383 pers 26595196 gemdot 20853368; FOI ready gap_hvriv_spend_36_63m_pers_26_60m_rekening_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1749",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1749 after 1748 HVZ Rivierenland YE2025. Next every-10 is 1750 (MUST refresh progress+top10). SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo HVZRivierenland/Zusterhof/HofSchoten/Buitenhof/Familiehof/Akapella/DeVerlosser/VivaltoHomeBE/Prinsenhof/ColiseeBelgium/Armonea/Gravenkasteel/Molenheide/SintJozefRumst/VeiligeHave/WitteMeren/TerEngelen/LSC_OB/LSC_NB/DommelhofNV/DommelhofTW/GO!/Natuurpunt/OVSG/KOV/Erfpunt/BoeK/KLJ/Boerenbond/BIV/LaScam/FARO/SOFAM/NSZ/OP-TIL/VI.BE/HVZMeetjesland/Midwest/Kempen/Westhoek/Fluvia/OostOVL/Taxandria/HVZ1/HVZOostVB/ZWL/NoordLimburg/BVLAR. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, ABS/POV/BVAS, other IOED/HVZ (Waasland/Rand/Centrum/VBWest/Zuid-Oost/Oost-Limburg/Antwerpen) if official JR2025 euros live, other IGS/WZC.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1748 HVZ Rivierenland; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/POV/BVAS/IOED/HVZ-Waasland-Rand-Centrum; next every-10 1750 MUST",
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
        "last_unit_id": "rq_1748",
        "ticks_completed": "1748",
        "paused": "no",
        "notes": "tick1748 leftover HVZ Rivierenland residual; KBO 0500.913.839; official vereenvoudigde rekening 2025; sourced euros uitgaven 36626383 pers 26595196 ontvangsten 33781156 gemdot 20853368 fed brand 6616305 fed DGH 3319025 invest 3707455 saldo 3414106; zoneraad 03.04.2026; full JR image-only; FOI ready; AGB Bornem JR2024-only (Bornem in zone); NSZ/Dijk92/APEFE CDN 403; NOT every-10 (next 1750 MUST); next rq_1749 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-Waasland-Rand; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
