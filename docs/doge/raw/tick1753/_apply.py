# tick 1753 — Hulpverleningszone Zuid-Oost (igs_hvzzo)
import csv
import sys
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = Path("docs/doge/data")
NOW = "2026-08-24T10:15:00Z"
TODAY = "2026-08-24"


def append_csv(path: Path, rows: list[dict]):
    with path.open("a", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), extrasaction="ignore")
        for row in rows:
            w.writerow(row)


entity = {
    "entity_id": "igs_hvzzo",
    "name_nl": "Hulpverleningszone Zuid-Oost / HVZ Zuid-Oost (leftover IGS of mined Aalst+Ninove+Geraardsbergen belt; NOT Centrum/Waasland/Rand/Rivierenland/Oost Dendermonde)",
    "name_fr": "Zone de secours Sud-Est (IGS residuel / zone de secours Alost)",
    "name_en": "HVZ Zuid-Oost leftover fire-rescue IGS of mined Aalst belt; Begroting 2026 live / JR2025 rekening FOI",
    "level": "other",
    "parent_id": "city_aalst",
    "community_language": "nl",
    "website": "https://www.zonezuidoost.be/",
    "foi_email": "info@zonezuidoost.be",
    "foi_postal": "Keizersplein 44 9300 Aalst",
    "notes": "tick1753 leftover HVZ Zuid-Oost after Rand; KBO 0500.928.586; zetel Aalst; zoneraad 24.10.2025 Begroting 2026 uitgaven 26373693.59 pers 19718414.80 gem 15772106.73 DGH/MU 3340629.46; JR2025 FOI; 7 gemeenten / ~242k inwoners",
}
append_csv(ROOT / "entities.csv", [entity])

sources = [
    {
        "source_id": "src_hvzzo_begroting2026",
        "title": "HVZ Zuid-Oost Begroting 2026 + MJP 2026-2031 (zoneraad 24.10.2025)",
        "url": "https://www.zonezuidoost.be/s/HVZ-ZUID-OOST-B-2026.pdf",
        "publisher": "Hulpverleningszone Zuid-Oost",
        "accessed_date": TODAY,
        "source_class": "budget",
        "notes": "tick1753; official Begroting 2026 PDF 55p; 2025_ZR_00106 Vaststelling; euros PDF only; JR2025 rekening unpublished on portal this tick",
    },
    {
        "source_id": "src_hvzzo_zoneraad_portal",
        "title": "HVZ Zuid-Oost zoneraad openbare agenda's en beslissingen",
        "url": "https://www.zonezuidoost.be/zoneraad",
        "publisher": "Hulpverleningszone Zuid-Oost",
        "accessed_date": TODAY,
        "source_class": "primary_official",
        "notes": "tick1753; lists Begroting 2026; secondary indexes claim JR2025 Goedgekeurd but PDF body not on /s/ this tick",
    },
    {
        "source_id": "src_hvzzo_justel_mu_2025",
        "title": "Justel MB / BS 26.09.2025 — MU toelage Zuid-Oost 2025",
        "url": "https://www.ejustice.just.fgov.be/mopdf/2025/09/26_2.pdf",
        "publisher": "Belgisch Staatsblad / FOD Volksgezondheid",
        "accessed_date": TODAY,
        "source_class": "official_register",
        "notes": "tick1753; HULPVERLENINGSZONE ZUID-OOST KBO 0500.928.586; MU totaal 3340629.46 matches Begroting 2026 DGH line carried from 2025",
    },
    {
        "source_id": "src_hvzzo_kbo",
        "title": "KBO Hulpverleningszone Zuid-Oost 0500.928.586",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500928586",
        "publisher": "FPS Economy KBO",
        "accessed_date": TODAY,
        "source_class": "official_register",
        "notes": "tick1753; Actief; zetel Keizersplein 44 9300 Aalst; info@zonezuidoost.be; tel 053/60 76 10",
    },
    {
        "source_id": "src_hvzzo_foi_contact_1753",
        "title": "HVZ Zuid-Oost FOI / contact channel",
        "url": "https://www.zonezuidoost.be/contact",
        "publisher": "Hulpverleningszone Zuid-Oost",
        "accessed_date": TODAY,
        "source_class": "foi_contact",
        "notes": "tick1753; info@zonezuidoost.be; Keizersplein 44 9300 Aalst",
    },
]
append_csv(ROOT / "sources.csv", sources)

budgets = [
    {
        "budget_id": "bud_hvzzo_uitgaven_gewone_B2026",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "26373693.59",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "B2026 gewone uitgaven 26373693.59 envelope; tick1753; primary official Begroting 2026",
    },
    {
        "budget_id": "bud_hvzzo_pers_B2026",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "19718414.80",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "B2026 personeelsuitgaven 19718414.80; tick1753",
    },
    {
        "budget_id": "bud_hvzzo_werking_B2026",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "6603758.13",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "B2026 werkingskosten 6603758.13 (incl erfpacht Aalst+Ninove 983810.7 via reserves); tick1753",
    },
    {
        "budget_id": "bud_hvzzo_overdrachten_B2026",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "40892.65",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "B2026 overdrachten 40892.65; tick1753",
    },
    {
        "budget_id": "bud_hvzzo_schuld_B2026",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "10628",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "B2026 schulduitgaven 10628; tick1753",
    },
    {
        "budget_id": "bud_hvzzo_ontvangsten_B2026",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "25389882.89",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "B2026 ontvangsten gewone 25389882.89; tick1753",
    },
    {
        "budget_id": "bud_hvzzo_gem_toelage_B2026",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "15772106.73",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "B2026 gemeentelijke toelage 15772106.73 (new verdeelsleutel 7 gemeenten); tick1753",
    },
    {
        "budget_id": "bud_hvzzo_aalst_dot_B2026",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "7892362.21",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "B2026 Stad Aalst 50.05pct = 7892362.21; tick1753",
    },
    {
        "budget_id": "bud_hvzzo_dgh_B2025",
        "entity_id": "igs_hvzzo",
        "year": "2025",
        "amount_eur": "3340629.46",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "DGH toelage 2025 3340629.46 carried into B2026 text; matches Justel MU; tick1753",
    },
    {
        "budget_id": "bud_hvzzo_mu_fed_2025",
        "entity_id": "igs_hvzzo",
        "year": "2025",
        "amount_eur": "3340629.46",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": "src_hvzzo_justel_mu_2025",
        "confidence": "strong",
        "notes": "Justel MU toelage totaal 3340629.46; tick1753",
    },
    {
        "budget_id": "bud_hvzzo_prestaties_B2026",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "1893573.84",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "B2026 prestaties 1893573.84; tick1753",
    },
    {
        "budget_id": "bud_hvzzo_kazerneplan_mjp",
        "entity_id": "igs_hvzzo",
        "year": "2026",
        "amount_eur": "45000000",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "budget",
        "source_id": "src_hvzzo_begroting2026",
        "confidence": "strong",
        "notes": "MJP kazerneplan 45000000 multi-year (not annual ordinary spend); tick1753; loan-financed",
    },
]
append_csv(ROOT / "budgets.csv", budgets)

comm = {
    "commitment_id": "comm_hvzzo_B2026_spend_26_37m",
    "title": "HVZ Zuid-Oost B2026 leftover IGS (gewone uitgaven 26.37m / pers 19.72m / gem 15.77m; JR2025 FOI)",
    "entity_id": "igs_hvzzo",
    "beneficiary": "HVZ Zuid-Oost / dual mined Aalst belt / municipal + federal civiele-veiligheid",
    "legal_basis": "Wet 15.05.2007 civiele veiligheid; KB 19.04.2014 boekhouding hulpverleningszones; Bestuursdecreet openbaarheid",
    "decision_date": "2025-10-24",
    "start_year": "2026",
    "end_year": "2026",
    "total_envelope_eur": "26373693.59",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.zonezuidoost.be/s/HVZ-ZUID-OOST-B-2026.pdf",
    "stated_goal": "Local leftover IGS fire-rescue map VL Aalst — Begroting 2026 live 26.37m; FOI full JR2025 rekening",
    "cut_option": "Publish full JR2025 rekening (uitgaven/personeel/VTE/gemdot); scrutinise pers 19.72m + erfpacht 0.98m path; kazerneplan 45m loan transparency",
    "source_id": "src_hvzzo_begroting2026",
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Gemeenten>Aalst>IGS>HVZ_ZuidOost>JR2025_L5",
    "notes": "tick1753; B2026 uitgaven 26373693.59 pers 19718414.80 werking 6603758.13 gem 15772106.73 Aalst 7892362.21 DGH/MU 3340629.46; JR2025 FOI; not TE-additive of 348bn",
}
append_csv(ROOT / "commitments.csv", [comm])

lb = {
    "item_id": "lb_hvzzo_B2026_spend_26_37m_jr_foi",
    "name": "HVZ Zuid-Oost 2026: Begroting gewone uitgaven 26.37m (JR2025 FOI)",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": "Vlaanderen>Gemeenten>Aalst>IGS>HVZ_ZuidOost>JR2025_L5",
    "annual_cost_eur": "26373693.59",
    "total_cost_eur": "26373693.59",
    "tco_notes": "Leftover HVZ Zuid-Oost (KBO 0500.928.586) via official Begroting 2026: gewone uitgaven 26.37m (pers 19.72m + werking 6.60m); gem toelage 15.77m (Aalst 7.89m); DGH/MU 3.34m; kazerneplan MJP 45m loan-financed; JR2025 rekening FOI",
    "confidence": "strong",
    "source_id": "src_hvzzo_begroting2026",
    "beneficiaries": "Aalst + 6 Zuid-Oost municipalities / municipal + federal civiele-veiligheid",
    "stated_goal": "Local leftover HVZ Zuid-Oost map — official B2026 after Rand residual",
    "measured_outcome": "Official Begroting 2026-08-24: uitgaven 26373693.59 / pers 19718414.80 / gem 15772106.73 / MU 3340629.46",
    "absurdity_score": "3.5",
    "cost_score": "6.5",
    "difficulty": "2.5",
    "priority_index": "5.2",
    "cut_proposal": "Publish JR2025 rekening + reconcile vs B2025; scrutinise pers share and 45m kazerneplan debt path",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1753; leftover after AGB Bornem JR2024 / NSZ CDN403 / HVZRand/HVZWaasland; budget not executed JR; not TE-additive of 348bn",
}
append_csv(ROOT / "leaderboard.csv", [lb])

foi = {
    "gap_id": "gap_hvzzo_jr2025_rekening_unpublished_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Aalst>IGS>HVZ_ZuidOost>JR2025_L5",
    "entity_id": "igs_hvzzo",
    "what_is_missing": "Official Begroting 2026 publishes B2026 gewone uitgaven 26373693.59 / pers 19718414.80 / gem 15772106.73 / DGH 3340629.46; full JR2025 rekening (executed uitgaven/VTE/balans/gemdot) unpublished on portal this tick despite secondary Goedgekeurd signals",
    "why_it_matters": "HVZ covering 7 Dender municipalities / ~242k inwoners — need executed JR2025 spend transparency beyond B2026 budget and MU slice",
    "priority": "8",
    "recipient_body": "Hulpverleningszone Zuid-Oost / Financiële dienst / bijzonder rekenplichtige",
    "recipient_email": "info@zonezuidoost.be",
    "recipient_postal": "Keizersplein 44 9300 Aalst",
    "draft_letter_path": "docs/doge/foi/drafts/gap_hvzzo_jr2025_rekening_unpublished_l5.md",
    "status": "ready",
    "date_ready": TODAY,
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_hvzzo_B2026_spend_26_37m",
    "linked_leaderboard_id": "lb_hvzzo_B2026_spend_26_37m_jr_foi",
    "created_utc": NOW,
    "updated_utc": NOW,
    "notes": "tick1753; human-send only; AGB/NSZ/Dijk92/APEFE still blocked; VBWest JR2025 verdaged",
}
append_csv(ROOT / "foi_queue.csv", [foi])

# research_queue
rq_path = ROOT / "research_queue.csv"
with rq_path.open(encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    fields = reader.fieldnames
    rows = list(reader)

found = False
for row in rows:
    if row["task_id"] == "rq_1753":
        row["status"] = "done"
        row["entity_id"] = "igs_hvzzo"
        row["notes"] = (
            "DONE tick1753: HVZ Zuid-Oost KBO 0500.928.586; Begroting 2026 uitgaven 26373693.59; "
            "MU 3340629.46; JR FOI gap_hvzzo_jr2025_rekening_unpublished_l5"
        )
        row["updated_utc"] = NOW
        found = True
        break
if not found:
    print("WARN rq_1753 not found", file=sys.stderr)
    sys.exit(1)

rows.append(
    {
        "task_id": "rq_1754",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Tick 1754 after 1753 HVZ Zuid-Oost B2026. Next every-10 is 1760. "
            "Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, "
            "Bosgroep residual, ABS/POV/BVAS, other IOED/HVZ (VBWest if JR euros live — college 05.06.2026 verdaged; "
            "Oost-Limburg/BZA-full-rekening/Brandweerzone Oost Dendermonde if PDF live with euros) if official JR2025 euros live, "
            "other IGS/WZC. Do NOT redo HVZZuidOost/HVZRand/HVZWaasland/HVZCentrum/HVZRivierenland/Zusterhof continuum."
        ),
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned after tick1753 HVZ Zuid-Oost; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-VBWest-OostLimburg-BZA; next every-10 1760",
    }
)

with rq_path.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

# loop_state
ls_path = ROOT / "loop_state.csv"
with ls_path.open(encoding="utf-8", newline="") as fh:
    ls_rows = list(csv.DictReader(fh))
    ls_fields = list(ls_rows[0].keys())
ls_rows[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": NOW,
        "last_unit_id": "rq_1753",
        "ticks_completed": "1753",
        "paused": "no",
        "notes": (
            "tick1753 leftover HVZ Zuid-Oost; KBO 0500.928.586; Begroting 2026 gewone uitgaven 26373693.59 "
            "(pers 19718414.80 / gem 15772106.73 / DGH-MU 3340629.46); JR rekening FOI ready; "
            "AGB Bornem JR2024-only; NSZ/Dijk92/APEFE CDN 403; VBWest JR2025 verdaged; "
            "NOT every-10 (next 1760); next rq_1754 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-VBWest-OostLimburg-BZA; continuous hole_fill"
        ),
    }
)
with ls_path.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=ls_fields)
    w.writeheader()
    w.writerows(ls_rows)

log = Path("docs/doge/loop_log.md")
entry = f"""
### {NOW} - tick 1753
- Unit: rq_1753 Hulpverleningszone Zuid-Oost / HVZ Zuid-Oost (leftover IGS of mined Aalst+Ninove+Geraardsbergen) (KBO **0500.928.586**; Keizersplein 44 9300 Aalst; zonezuidoost.be; info@zonezuidoost.be; official **Begroting 2026** zoneraad **24.10.2025** 2025_ZR_00106; Justel MU matches DGH **3340629.46**). Honest leftover AGB Bornem still JR2024-only. NSZ/Dijk92/APEFE CDN **403**. VBWest JR2025 **verdaged**. Preferred AGB/NSZ blocked — leftover HVZ Zuid-Oost official B2026 euros **live** taken. New entity igs_hvzzo. Envelope = gewone uitgaven **26373693.59**. NOT every-10 (next 1760).
- Found (official Begroting strong): uitgaven **26373693.59** (pers **19718414.80**; werking **6603758.13**; overdrachten **40892.65**; schuld **10628**); ontvangsten **25389882.89** (gem **15772106.73** of which Aalst **7892362.21**; DGH/MU **3340629.46**; prestaties **1893573.84**); MJP kazerneplan **45000000** (loan). Full JR2025 rekening unpublished this tick.
- Wrote: sources +5; entities +1 igs_hvzzo; budgets +12; commitments +1; leaderboard +1; foi_queue +1 ready; rq_1753=done + rq_1754 spawn; ticks_completed=1753. Raw docs/doge/raw/tick1753/.
- FOI opened: gap_hvzzo_jr2025_rekening_unpublished_l5 ready (full JR/VTE/gemdot). Do not send.
- Next: rq_1754 leftover AGB/**NSZ if CDN 200**/Bosgroep/Dijk92 / APEFE / ABS/POV/BVAS / IOED/HVZ-VBWest-OostLimburg-BZA. Do NOT redo HVZZuidOost/HVZRand/HVZWaasland continuum. NOT every-10 (next **1760**).
"""
with log.open("a", encoding="utf-8") as fh:
    fh.write(entry)

print("OK tick 1753 applied")
