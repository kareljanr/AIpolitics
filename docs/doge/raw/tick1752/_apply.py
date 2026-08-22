# tick 1752 — Brandweer Zone Rand (igs_hvzr)
import csv
import sys
from pathlib import Path
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)
ROOT = Path("docs/doge/data")
NOW = "2026-08-24T09:45:00Z"
TODAY = "2026-08-24"


def append_csv(path: Path, rows: list[dict]):
    with path.open("a", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), extrasaction="ignore")
        for row in rows:
            w.writerow(row)


# --- entities ---
entity = {
    "entity_id": "igs_hvzr",
    "name_nl": "Brandweer Zone Rand / HVZ Rand (leftover IGS hulpverleningszone of mined Brasschaat+Brecht+Schoten belt; NOT Rivierenland/Centrum/Waasland/Kempen/Taxandria)",
    "name_fr": "Zone de secours Rand (IGS residuel / zone de secours Anvers Rand)",
    "name_en": "Brandweer Zone Rand leftover fire-rescue IGS of mined Antwerp Rand municipalities; Budget 2026 motivatienota live / JR2025 rekening FOI",
    "level": "other",
    "parent_id": "city_brasschaat",
    "community_language": "nl",
    "website": "https://www.brandweerzonerand.be/",
    "foi_email": "financien@brandweer.zonerand.be",
    "foi_postal": "Ruiterijschool 1 bus 2 2930 Brasschaat",
    "notes": "tick1752 leftover HVZ Rand after Waasland; KBO 0500.914.730; zetel Brasschaat; zoneraad 24.10.2025 Budget 2026; Motivatienota B2025 inkomsten 29036748; Justel MU 568670.97; JR2025 rekening FOI; ~19 gemeenten / 676 vrijwilligers / 64 beroeps",
}
append_csv(ROOT / "entities.csv", [entity])

# --- sources ---
sources = [
    {
        "source_id": "src_hvzr_motivatienota_budget2026",
        "title": "Brandweer Zone Rand Motivatienota Budget 2026 (zoneraad 24.10.2025)",
        "url": "https://drive.google.com/file/d/1DH7sjg1L-dzJ_yvo50dbdJPKZ5zFbHqT/view",
        "publisher": "Brandweer Zone Rand",
        "accessed_date": TODAY,
        "source_class": "budget",
        "notes": "tick1752; official Motivatienota Budget 2026 PDF 23p; zoneraad 24.10.2025; B2025 comparative inkomsten table page 8; euros PDF only; JR2025 rekening unpublished",
    },
    {
        "source_id": "src_hvzr_begroting2026_nieuws",
        "title": "Brandweer Zone Rand — Begroting 2026 goedgekeurd",
        "url": "https://www.brandweerzonerand.be/nieuws/begroting-2026-goedgekeurd",
        "publisher": "Brandweer Zone Rand",
        "accessed_date": TODAY,
        "source_class": "primary_official",
        "notes": "tick1752; zoneraad 24.10.2025 budget 2026 approved; links Motivatienota + Begroting Drive",
    },
    {
        "source_id": "src_hvzr_justel_mu_2025",
        "title": "Justel MB 26.08.2025 / BS 26.09.2025 — MU toelage ziekenwagendiensten 2025 (Rand)",
        "url": "https://www.ejustice.just.fgov.be/mopdf/2025/09/26_2.pdf",
        "publisher": "Belgisch Staatsblad / FOD Volksgezondheid",
        "accessed_date": TODAY,
        "source_class": "official_register",
        "notes": "tick1752; HULPVERLENINGSZONE BRANDWEER ZONE RAND KBO 0500.914.730; activatie 136816 + permanentie 431854.97 = totaal 568670.97; partial DGH ambulance MU not full zone spend",
    },
    {
        "source_id": "src_hvzr_kbo",
        "title": "KBO Brandweer Zone Rand 0500.914.730",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500914730",
        "publisher": "FPS Economy KBO",
        "accessed_date": TODAY,
        "source_class": "official_register",
        "notes": "tick1752; BRANDWEER ZONE RAND Actief sinds 05.10.2012; zetel Ruiterijschool 1 bus 2 2930 Brasschaat; tel 03 205 80 00",
    },
    {
        "source_id": "src_hvzr_foi_contact_1752",
        "title": "Brandweer Zone Rand FOI / financiën channel",
        "url": "https://www.brandweerzonerand.be/contact",
        "publisher": "Brandweer Zone Rand",
        "accessed_date": TODAY,
        "source_class": "foi_contact",
        "notes": "tick1752; financien@brandweer.zonerand.be; ann.vandenbussche@brandweer.zonerand.be; jerry.kegels@brandweer.zonerand.be; info@brandweer.zonerand.be; Ruiterijschool 1 bus 2 2930 Brasschaat",
    },
]
append_csv(ROOT / "sources.csv", sources)

# --- budgets (B2025 from Motivatienota + MU Justel) ---
budgets = [
    {
        "budget_id": "bud_hvzr_inkomsten_B2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "29036748",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzr_motivatienota_budget2026",
        "confidence": "strong",
        "notes": "B2025 totale inkomsten overzicht 29036748 (Motivatienota p8 comparative); tick1752; NOT executed JR rekening",
    },
    {
        "budget_id": "bud_hvzr_gem_werking_B2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "18040021",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzr_motivatienota_budget2026",
        "confidence": "strong",
        "notes": "B2025 gemeentelijke werkingstoelagen 18040021; tick1752",
    },
    {
        "budget_id": "bud_hvzr_gem_invest_B2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "3947337",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzr_motivatienota_budget2026",
        "confidence": "strong",
        "notes": "B2025 gemeentelijke investeringstoelagen 3947337; tick1752",
    },
    {
        "budget_id": "bud_hvzr_fed_dot_B2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "5669972",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzr_motivatienota_budget2026",
        "confidence": "strong",
        "notes": "B2025 federale dotaties 5669972 (basis+bijkomend as used for 2026 = same); tick1752",
    },
    {
        "budget_id": "bud_hvzr_prestaties_B2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "1064418",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzr_motivatienota_budget2026",
        "confidence": "strong",
        "notes": "B2025 prestaties 1064418; tick1752",
    },
    {
        "budget_id": "bud_hvzr_dgh_werking_B2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "315000",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzr_motivatienota_budget2026",
        "confidence": "strong",
        "notes": "B2025 DGH werkingstoelage 315000 (budget line; distinct from Justel MU ambulance 568670.97); tick1752",
    },
    {
        "budget_id": "bud_hvzr_pers_B2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "16747577",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzr_motivatienota_budget2026",
        "confidence": "strong",
        "notes": "B2025 personeelskosten EG70 derived 16985011-237434=16747577 (Motivatienota: 2026 only 1.42pct/237434 higher than 2025); tick1752",
    },
    {
        "budget_id": "bud_hvzr_pers_B2026",
        "entity_id": "igs_hvzr",
        "year": "2026",
        "amount_eur": "16985011",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzr_motivatienota_budget2026",
        "confidence": "strong",
        "notes": "B2026 personeelskosten EG70 16985011; tick1752",
    },
    {
        "budget_id": "bud_hvzr_inkomsten_B2026",
        "entity_id": "igs_hvzr",
        "year": "2026",
        "amount_eur": "30280052",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzr_motivatienota_budget2026",
        "confidence": "strong",
        "notes": "B2026 totale inkomsten overzicht 30280052; tick1752",
    },
    {
        "budget_id": "bud_hvzr_mu_fed_2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "568670.97",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": "src_hvzr_justel_mu_2025",
        "confidence": "strong",
        "notes": "Justel MU toelage totaal 568670.97 (activatie 136816 + permanentie 431854.97); partial federal ambulance; tick1752",
    },
    {
        "budget_id": "bud_hvzr_mu_activatie_2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "136816",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": "src_hvzr_justel_mu_2025",
        "confidence": "strong",
        "notes": "Justel MU activatie 136816; tick1752",
    },
    {
        "budget_id": "bud_hvzr_mu_permanentie_2025",
        "entity_id": "igs_hvzr",
        "year": "2025",
        "amount_eur": "431854.97",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": "src_hvzr_justel_mu_2025",
        "confidence": "strong",
        "notes": "Justel MU permanentie 431854.97; tick1752",
    },
]
append_csv(ROOT / "budgets.csv", budgets)

# --- commitment ---
comm = {
    "commitment_id": "comm_hvzr_B2025_inkomsten_29_04m",
    "title": "HVZ Rand B2025 leftover IGS (inkomsten budget 29.04m / gem werking 18.04m / fed 5.67m; JR rekening FOI)",
    "entity_id": "igs_hvzr",
    "beneficiary": "Brandweer Zone Rand / dual mined Brasschaat+Brecht+Schoten belt / municipal + federal civiele-veiligheid",
    "legal_basis": "Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid",
    "decision_date": "2025-10-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "29036748",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://drive.google.com/file/d/1DH7sjg1L-dzJ_yvo50dbdJPKZ5zFbHqT/view",
    "stated_goal": "Local leftover IGS fire-rescue map VL Antwerp Rand — Budget 2026 motivatienota live B2025 29.04m; FOI full JR2025 rekening",
    "cut_option": "Publish full JR2025 rekening (uitgaven/personeel/VTE/gemdot per gemeente/fed); scrutinise pers ~16.75m path; do not invent executed euros beyond sourced budget/MU",
    "source_id": "src_hvzr_motivatienota_budget2026",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Gemeenten>Brasschaat>IGS>HVZ_Rand>JR2025_L5",
    "notes": "tick1752; B2025 inkomsten 29036748 gem_werking 18040021 fed 5669972 invest_toelagen 3947337 prestaties 1064418 dgh_werking 315000; pers_B2025 16747577; Justel MU 568670.97; NOT executed JR; FOI ready; not TE-additive of 348bn",
}
append_csv(ROOT / "commitments.csv", [comm])

# --- leaderboard ---
lb = {
    "item_id": "lb_hvzr_B2025_inkomsten_29_04m_jr_foi",
    "name": "HVZ Rand 2025: Budget inkomsten 29.04m (JR rekening FOI)",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>Gemeenten>Brasschaat>IGS>HVZ_Rand>JR2025_L5",
    "annual_cost_eur": "29036748",
    "total_cost_eur": "29036748",
    "tco_notes": "Leftover Brandweer Zone Rand (KBO 0500.914.730) via official Motivatienota Budget 2026: B2025 totale inkomsten 29.04m (gem werking 18.04m + fed 5.67m + invest toelagen 3.95m + prestaties 1.06m + DGH 0.32m); pers B2025 ~16.75m; Justel MU ambulance 0.57m partial; full JR rekening FOI",
    "confidence": "strong",
    "source_id": "src_hvzr_motivatienota_budget2026",
    "beneficiaries": "Brasschaat + Antwerp Rand municipalities / municipal + federal civiele-veiligheid",
    "stated_goal": "Local leftover HVZ Rand map — official B2025 budget after Waasland residual",
    "measured_outcome": "Official Motivatienota 2026-08-24: B2025 inkomsten 29036748 / gem 18040021 / fed 5669972 / pers~16747577; MU Justel 568670.97",
    "absurdity_score": "3.5",
    "cost_score": "6.5",
    "difficulty": "2.5",
    "priority_index": "5.2",
    "cut_proposal": "Publish full JR2025 rekening + per-gemeente dots; reconcile budget vs executed; scrutinise pers share",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1752; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / HVZWaasland FOI; budget not executed; not TE-additive of 348bn",
}
append_csv(ROOT / "leaderboard.csv", [lb])

# --- foi_queue ---
foi = {
    "gap_id": "gap_hvzr_jr2025_rekening_unpublished_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Brasschaat>IGS>HVZ_Rand>JR2025_L5",
    "entity_id": "igs_hvzr",
    "what_is_missing": "Official Motivatienota Budget 2026 publishes B2025 budget inkomsten 29036748 / gem werking 18040021 / fed 5669972 / pers~16747577; full JR2025 rekening (executed uitgaven/personeel/VTE/balans/gemdot per gemeente) unpublished; Brecht municipal dotatie PDF image-only",
    "why_it_matters": "HVZ covering Antwerp Rand (~19 gemeenten / 676 vrijwilligers / 64 beroeps) — need executed JR2025 spend transparency beyond budget comparative and partial MU 0.57m",
    "priority": "8",
    "recipient_body": "Brandweer Zone Rand / Directie Financiën / zonesecretaris",
    "recipient_email": "financien@brandweer.zonerand.be",
    "recipient_postal": "Ruiterijschool 1 bus 2 2930 Brasschaat",
    "draft_letter_path": "docs/doge/foi/drafts/gap_hvzr_jr2025_rekening_unpublished_l5.md",
    "status": "ready",
    "date_ready": TODAY,
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_hvzr_B2025_inkomsten_29_04m",
    "linked_leaderboard_id": "lb_hvzr_B2025_inkomsten_29_04m_jr_foi",
    "created_utc": NOW,
    "updated_utc": NOW,
    "notes": "tick1752; human-send only; also ann.vandenbussche@brandweer.zonerand.be; AGB/NSZ/Dijk92/APEFE still blocked preferred path; VBWest JR2025 verdaged 05.06.2026",
}
append_csv(ROOT / "foi_queue.csv", [foi])

# --- research_queue: mark 1752 done + spawn 1753 ---
rq_path = ROOT / "research_queue.csv"
with rq_path.open(encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    fields = reader.fieldnames
    rows = list(reader)

found = False
for row in rows:
    if row["task_id"] == "rq_1752":
        row["status"] = "done"
        row["entity_id"] = "igs_hvzr"
        row["notes"] = (
            "DONE tick1752: Brandweer Zone Rand KBO 0500.914.730; Motivatienota Budget 2026 B2025 inkomsten 29036748; "
            "Justel MU 568670.97; JR rekening FOI gap_hvzr_jr2025_rekening_unpublished_l5"
        )
        row["updated_utc"] = NOW
        found = True
        break
if not found:
    print("WARN rq_1752 not found", file=sys.stderr)
    sys.exit(1)

spawn = {
    "task_id": "rq_1753",
    "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
    "sprint": "hole_fill",
    "priority": "5",
    "status": "open",
    "hierarchy_target": "L5",
    "entity_id": "gg_belgium",
    "instructions": (
        "Tick 1753 after 1752 Brandweer Zone Rand B2025 budget. Next every-10 is 1760. "
        "Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, "
        "Bosgroep residual, ABS/POV/BVAS, other IOED/HVZ (VBWest if JR euros live — college 05.06.2026 verdaged; "
        "Zuid-Oost/Oost-Limburg/BZA-full-rekening if PDF live with euros) if official JR2025 euros live, other IGS/WZC. "
        "Do NOT redo HVZRand/HVZWaasland/HVZCentrum/HVZRivierenland/Zusterhof/HofSchoten/Buitenhof/Familiehof/Akapella/"
        "DeVerlosser/VivaltoHomeBE."
    ),
    "blocked_gap_id": "",
    "created_utc": NOW,
    "updated_utc": NOW,
    "notes": "spawned after tick1752 HVZ Rand; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-VBWest-ZuidOost-BZA; next every-10 1760",
}
rows.append(spawn)

with rq_path.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

# --- loop_state ---
ls_path = ROOT / "loop_state.csv"
with ls_path.open(encoding="utf-8", newline="") as fh:
    ls_rows = list(csv.DictReader(fh))
    ls_fields = list(ls_rows[0].keys()) if ls_rows else []
ls_rows[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": NOW,
        "last_unit_id": "rq_1752",
        "ticks_completed": "1752",
        "paused": "no",
        "notes": (
            "tick1752 leftover Brandweer Zone Rand; KBO 0500.914.730; Motivatienota Budget 2026 B2025 inkomsten 29036748 "
            "(gem werking 18040021 / fed 5669972); Justel MU 568670.97; JR rekening FOI ready; "
            "AGB Bornem JR2024-only; NSZ/Dijk92/APEFE CDN 403; VBWest JR2025 verdaged; "
            "NOT every-10 (next 1760); next rq_1753 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-VBWest-ZuidOost-BZA; continuous hole_fill"
        ),
    }
)
with ls_path.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=ls_fields)
    w.writeheader()
    w.writerows(ls_rows)

# --- loop_log ---
log = Path("docs/doge/loop_log.md")
entry = f"""
### {NOW} - tick 1752
- Unit: rq_1752 Brandweer Zone Rand / HVZ Rand (leftover IGS of mined Brasschaat+Brecht+Schoten belt) (KBO **0500.914.730**; Ruiterijschool 1 bus 2 2930 Brasschaat; brandweerzonerand.be; financien@brandweer.zonerand.be; official **Motivatienota Budget 2026** zoneraad **24.10.2025**; Justel MU MB BS **26.09.2025**). Honest leftover AGB Bornem still JR2024-only. NSZ/Dijk92/APEFE CDN **403**. VBWest JR2025 **verdaged** college 05.06.2026. Preferred AGB/NSZ blocked — leftover HVZ Rand official Budget **B2025 euros live** taken. New entity igs_hvzr. Envelope = B2025 inkomsten **29036748**. NOT every-10 (next 1760).
- Found (official Motivatienota strong budget / Justel MU strong executed partial): B2025 inkomsten **29036748** (gem werking **18040021**; fed **5669972**; invest toelagen **3947337**; prestaties **1064418**; DGH werking **315000**); pers B2025 **16747577** (derived from B2026 **16985011** +1.42%/237434); Justel MU totaal **568670.97** (activatie **136816** + permanentie **431854.97**). Full JR2025 rekening unpublished.
- Wrote: sources +5; entities +1 igs_hvzr; budgets +12; commitments +1; leaderboard +1; foi_queue +1 ready; rq_1752=done + rq_1753 spawn; ticks_completed=1752. Raw docs/doge/raw/tick1752/.
- FOI opened: gap_hvzr_jr2025_rekening_unpublished_l5 ready (full JR/VTE/gemdot). Do not send.
- Next: rq_1753 leftover AGB/**NSZ if CDN 200**/Bosgroep/Dijk92 / APEFE / ABS/POV/BVAS / IOED/HVZ-VBWest-ZuidOost-BZA. Do NOT redo HVZRand/HVZWaasland/HVZCentrum/HVZRivierenland/Zusterhof continuum. NOT every-10 (next **1760**).
"""
with log.open("a", encoding="utf-8") as fh:
    fh.write(entry)

print("OK tick 1752 applied")
