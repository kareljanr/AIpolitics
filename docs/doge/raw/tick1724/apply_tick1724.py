import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T00:05:00Z"
DATE = "2026-08-24"
EID = "vzw_natuurpunt"


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
        "name_nl": "Natuurpunt vzw / Vereniging voor Natuur en Landschap in Vlaanderen (leftover VL nature NGO unie; NOT Greenpeace / BBL / Amnesty)",
        "name_fr": "Natuurpunt asbl / Association nature et paysage Flandre (residuelle)",
        "name_en": "Natuurpunt leftover Flemish nature conservation NGO federation",
        "level": "other",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "https://www.natuurpunt.be",
        "foi_email": "info@natuurpunt.be",
        "foi_postal": "Coxiestraat 11 2800 Mechelen",
        "notes": "tick1724 leftover Natuurpunt after AGB/NSZ/Dijk92 hunt; official JR2025 text PDF live; NBB 2026-00118589 CDN 200 image-only; KBO 0434.364.713; FOI subsidy donor split",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": "src_natuurpunt_jr2025",
        "title": "Natuurpunt Jaarverslag 2025 official PDF",
        "url": "https://www.natuurpunt.be/system/files/2026-04/Jaarverslag%20Natuurpunt%202025.pdf",
        "publisher": "Natuurpunt vzw",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1724; consolidated JR elim intercompany; inkomsten 70796058 uitgaven 70529971 pnl 266087 assets 488808253; subs 72pct",
    },
    {
        "source_id": "src_natuurpunt_nbb_2026_00118589",
        "title": "Natuurpunt NBB VOL-VZW deposit 2026-00118589",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00118589.pdf",
        "publisher": "NBB / Staatsbladmonitor CDN",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1724; CDN 200 / 13374432 bytes / 52p; model VOL-VZW 26.0.11 m05-f-p IMAGE-only; KBO 0434364713; AV/neerlegging ~21.05.2026; text euros from JR not this PDF",
    },
    {
        "source_id": "src_natuurpunt_kbo",
        "title": "Natuurpunt KBO 0434.364.713",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=434364713",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1724; VZW; Coxiestraat 11 2800 Mechelen; VU on JR2025",
    },
    {
        "source_id": "src_natuurpunt_foi_contact_1724",
        "title": "Natuurpunt FOI channel",
        "url": "https://www.natuurpunt.be",
        "publisher": "Natuurpunt vzw",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1724; info@natuurpunt.be; Coxiestraat 11 2800 Mechelen",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_np_inkomsten_2025", "2025", "70796058", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 RESULTAAT inkomsten 70796058; tick1724"),
    ("bud_np_uitgaven_2025", "2025", "70529971", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 RESULTAAT uitgaven 70529971; tick1724"),
    ("bud_np_pnl_2025", "2025", "266087", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 positief resultaat 266087 naar balans; tick1724"),
    ("bud_np_assets_2025", "2025", "488808253", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 balans actief/passief 488808253; tick1724"),
    ("bud_np_va_2025", "2025", "443065442", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 vast actief 443065442; tick1724"),
    ("bud_np_natuurgebieden_2025", "2025", "425726099", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 natuurgebieden 425726099; tick1724"),
    ("bud_np_vlottend_2025", "2025", "45742811", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 vlottend 45742811; tick1724"),
    ("bud_np_cash_2025", "2025", "24292907", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 liquide middelen 24292907; tick1724"),
    ("bud_np_equity_2025", "2025", "442456532", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 eigen vermogen 442456532; tick1724"),
    ("bud_np_kapsubs_natuur_2025", "2025", "337336681", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 kapitaalsubsidies natuurgebieden 337336681; tick1724"),
    ("bud_np_vv_2025", "2025", "43255021", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 vreemd vermogen 43255021; tick1724"),
    ("bud_np_werkingssubs_2025", "2025", "42288071", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 werkingssubsidies 42288071 =60pct inkomsten; tick1724"),
    ("bud_np_aankoopsubs_2025", "2025", "8310831", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 aankoopsubsidies 8310831 =12pct; tick1724"),
    ("bud_np_lid_schenk_spons_2025", "2025", "12676999", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 lidgelden/schenkingen/sponsoring 12676999 =18pct; tick1724"),
    ("bud_np_studie_beheerwerken_rev_2025", "2025", "7520157", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 studieopdrachten/cursussen/beheerwerken 7520157 =10pct; tick1724"),
    ("bud_np_beheer_exp_2025", "2025", "42694096", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 beheer natuurgebieden 42694096 =61pct uitgaven; tick1724"),
    ("bud_np_aankopen_exp_2025", "2025", "12681503", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 aankopen natuurgebieden 12681503 =18pct; tick1724"),
    ("bud_np_overhead_2025", "2025", "4174454", "executed", "src_natuurpunt_jr2025", "strong", "JR2025 overhead 4174454 =6pct; tick1724"),
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
        "commitment_id": "comm_natuurpunt_jr2025_inkomsten",
        "title": "Natuurpunt JR2025 leftover VL nature NGO (inkomsten 70.80m / subs ~72% / assets 488.81m)",
        "entity_id": EID,
        "beneficiary": "VL nature areas / members / public biodiversity",
        "legal_basis": "WVV VZW; Bestuursdecreet openbaarheid; VL nature subsidies",
        "decision_date": "2026-04-01",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "70796058",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.natuurpunt.be/system/files/2026-04/Jaarverslag%20Natuurpunt%202025.pdf",
        "stated_goal": "Local leftover Natuurpunt map — official JR2025; FOI donor split",
        "cut_option": "Publish donor split of 42.29m werking + 8.31m aankoopsubs; reconcile NBB image deposit vs JR; scrutinise 72% public funding share",
        "source_id": "src_natuurpunt_jr2025",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Omgeving>Natuurpunt>JR2025_L5",
        "notes": "tick1724; JR2025 consolidated elim IC; inkomsten 70.80m uitgaven 70.53m pnl +266k assets 488.81m EV 442.46m; 612 staff narrative; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": "lb_natuurpunt_inkomsten_70_80m_subs_72pct_assets_488_81m",
        "name": "Natuurpunt JR2025 leftover VL nature NGO: inkomsten 70.80m / subsidies ~72%",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Omgeving>Natuurpunt>JR2025_L5",
        "annual_cost_eur": "70796058",
        "total_cost_eur": "70796058",
        "tco_notes": "Leftover Natuurpunt JR2025: inkomsten 70.80m (werkingssubs 42.29m + aankoopsubs 8.31m + lid/schenk/spons 12.68m + studie/beheerwerken 7.52m); uitgaven 70.53m; pnl +266k; assets 488.81m natuurgebieden 425.73m; NBB single-VZW image-only",
        "confidence": "strong",
        "source_id": "src_natuurpunt_jr2025",
        "beneficiaries": "VL nature / members / public",
        "stated_goal": "Local leftover Natuurpunt map — official JR2025 after NGO residual",
        "measured_outcome": "Official JR2025 2026-08-24: inkomsten 70796058 / uitgaven 70529971 / assets 488808253 / werkingssubs 42288071",
        "absurdity_score": "4.0",
        "cost_score": "5.5",
        "difficulty": "3.0",
        "priority_index": "4.2",
        "cut_proposal": "Publish public-donor matrix for 50.6m subsidies; text NBB for all VZWs; reconcile JR vs statutory",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1724; leftover after AGB unpublished / Dijk92 CDN403 / NSZ YE2025 filed but CDN opaque / ABS+BVAS no NBB; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": "gap_natuurpunt_inkomsten_70_80m_subs_72pct_assets_488_81m_l5",
        "hierarchy_path": "Vlaanderen>Omgeving>Natuurpunt>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official JR2025 publishes inkomsten 70796058 / uitgaven 70529971 / assets 488808253 / werkingssubs 42288071 / aankoopsubs 8310831; NBB 2026-00118589 image-only; public donor split + multi-VZW KBO list + VTE vs 612 staff unpublished",
        "why_it_matters": "Leftover VL nature NGO with ~70.8m inkomsten and ~72% subsidies — need donor transparency + statutory NBB text",
        "priority": "8",
        "recipient_body": "Natuurpunt vzw / Bestuursorgaan",
        "recipient_email": "info@natuurpunt.be",
        "recipient_postal": "Coxiestraat 11 2800 Mechelen",
        "draft_letter_path": "docs/doge/foi/drafts/gap_natuurpunt_inkomsten_70_80m_subs_72pct_assets_488_81m_l5.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_natuurpunt_jr2025_inkomsten",
        "linked_leaderboard_id": "lb_natuurpunt_inkomsten_70_80m_subs_72pct_assets_488_81m",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1724; human-send only; AGB/Dijk92 still blocked; NSZ YE2025 companyweb live but CDN deposit not taken",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1724":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = "gap_natuurpunt_inkomsten_70_80m_subs_72pct_assets_488_81m_l5"
        r["notes"] = "DONE tick1724: Natuurpunt KBO 0434.364.713 JR2025 inkomsten 70796058 uitgaven 70529971 assets 488808253 werkingssubs 42288071; FOI ready gap_natuurpunt_inkomsten_70_80m_subs_72pct_assets_488_81m_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1725",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1725 after 1724 Natuurpunt JR2025. Next every-10 is 1730. SBM HTML IP-blacklisted — prefer direct CDN / NBB / official org PDFs. Do NOT redo Natuurpunt/OVSG/KOV/KLJ/BoeK/LandelijkeGilden/Boerenbond/BIV/LaScam/deAuteurs/SACD/FARO/SOFAM. Prefer leftover AGB/APB if PDF live, else NSZ if CDN 200 (YE2025 filed companyweb 12.08.2026), Bosgroep residual, Dijk92 if JR euros, APEFE if budget euros, ABS/GO!/POV/BVAS, other IOED/HVZ/IGS.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1724 Natuurpunt; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/GO!/POV/BVAS/IOED/HVZ/IGS; Natuurpunt+OVSG+KOV DONE; next every-10 1730",
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
        "last_unit_id": "rq_1724",
        "ticks_completed": "1724",
        "paused": "no",
        "notes": "tick1724 leftover Natuurpunt JR2025 residual; KBO 0434.364.713; official JR2025 text PDF; sourced euros inkomsten 70796058 uitgaven 70529971 pnl 266087 assets 488808253 EV 442456532 werkingssubs 42288071 aankoopsubs 8310831; NBB 2026-00118589 CDN 200 image-only; FOI ready; AGB unpublished; Dijk92 CDN 403; NSZ YE2025 companyweb live CDN deposit opaque; ABS/BVAS no NBB; NOT every-10 (next 1730); next rq_1725 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/ABS/GO!/POV/BVAS/IOED/HVZ/IGS/other; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
