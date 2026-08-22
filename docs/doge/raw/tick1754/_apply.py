# tick 1754 — Brandweerzone Oost-Limburg / BWOL (igs_bwol)
import csv
import sys
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = Path("docs/doge/data")
NOW = "2026-08-24T10:45:00Z"
TODAY = "2026-08-24"


def append_csv(path: Path, rows: list[dict]):
    with path.open("a", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), extrasaction="ignore")
        for row in rows:
            w.writerow(row)


entity = {
    "entity_id": "igs_bwol",
    "name_nl": "Brandweerzone Oost-Limburg / BWOL / HVZ Oost-Limburg (leftover IGS of mined Genk+Maaseik belt; NOT ZWL/Noord-Limburg/Zuid-Oost/Rand)",
    "name_fr": "Zone de secours Limbourg oriental (IGS residuel / zone de secours Genk)",
    "name_en": "BWOL leftover fire-rescue IGS of mined Genk belt; JR2025 PDF live but euros unextractable; MU FOI",
    "level": "other",
    "parent_id": "city_genk",
    "community_language": "nl",
    "website": "https://www.bwol.be/",
    "foi_email": "info@bwol.be",
    "foi_postal": "C-Mine 50 3600 Genk",
    "notes": "tick1754 leftover BWOL after Zuid-Oost; KBO 0500.907.802; zetel Genk C-Mine 50; zoneraad 26.06.2026 JR2025 Goedgekeurd; Maaseik publishes Rekening-2025 PDF 228p CID/image-garbled; Justel MU 3334455.78; FOI searchable rekening; 13 gemeenten",
}
append_csv(ROOT / "entities.csv", [entity])

sources = [
    {
        "source_id": "src_bwol_jr2025_rekening_pdf",
        "title": "BWOL Rekening 2025 — boek toezicht (Maaseik publicatie)",
        "url": "https://www.maaseik.be/sites/default/files/2026-08/Rekening-2025-BWOL-boek-toezicht.pdf",
        "publisher": "Brandweerzone Oost-Limburg / Stad Maaseik",
        "accessed_date": TODAY,
        "source_class": "budget",
        "notes": "tick1754; official JR2025 PDF 228p / ~10.7MB; text layer CID/image-garbled — euros not reliably extractable this tick; FOI searchable copy",
    },
    {
        "source_id": "src_bwol_zr_20260626_besluit",
        "title": "BWOL besluitenlijst zoneraad 26.06.2026 — Jaarrekening 2025 Goedgekeurd",
        "url": "https://www.bwol.be/uploads/1/2/5/4/12549797/besluitenlijst_zoneraad_26_juni_2026.pdf",
        "publisher": "Brandweerzone Oost-Limburg",
        "accessed_date": TODAY,
        "source_class": "primary_official",
        "notes": "tick1754; item 3 Jaarrekening dienstjaar 2025 Goedgekeurd; BW1+2 2026 also approved",
    },
    {
        "source_id": "src_bwol_justel_mu_2025",
        "title": "Justel MB / BS 26.09.2025 — MU toelage BWOL 2025",
        "url": "https://www.ejustice.just.fgov.be/mopdf/2025/09/26_2.pdf",
        "publisher": "Belgisch Staatsblad / FOD Volksgezondheid",
        "accessed_date": TODAY,
        "source_class": "official_register",
        "notes": "tick1754; HULPVERLENINGSZONE BRANDWEERZONE OOST-LIMBURG KBO 0500.907.802; activatie 653618 + permanentie 2680837.78 = totaal 3334455.78",
    },
    {
        "source_id": "src_bwol_kbo",
        "title": "KBO Brandweerzone Oost-Limburg 0500.907.802",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500907802",
        "publisher": "FPS Economy KBO",
        "accessed_date": TODAY,
        "source_class": "official_register",
        "notes": "tick1754; Actief; zetel C-Mine 50 3600 Genk",
    },
    {
        "source_id": "src_bwol_foi_contact_1754",
        "title": "BWOL FOI / contact channel",
        "url": "https://www.bwol.be/contact.html",
        "publisher": "Brandweerzone Oost-Limburg",
        "accessed_date": TODAY,
        "source_class": "foi_contact",
        "notes": "tick1754; info@bwol.be; facturatie@bwol.be; C-Mine 50 3600 Genk; tel 089/69 73 00",
    },
    {
        "source_id": "src_bwol_jv2025",
        "title": "BWOL Activiteitenverslag / Jaarverslag 2025",
        "url": "https://www.bwol.be/uploads/1/2/5/4/12549797/2025_jaarverslag_def.pdf",
        "publisher": "Brandweerzone Oost-Limburg",
        "accessed_date": TODAY,
        "source_class": "primary_official",
        "notes": "tick1754; p61 Financieel overzicht deferred (JR still in opmaak at AV date); invest notes Bilzen-Hoeselt / Maasmechelen 6.3m / Maaseik reno >720k",
    },
]
append_csv(ROOT / "sources.csv", sources)

budgets = [
    {
        "budget_id": "bud_bwol_mu_fed_2025",
        "entity_id": "igs_bwol",
        "year": "2025",
        "amount_eur": "3334455.78",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": "src_bwol_justel_mu_2025",
        "confidence": "strong",
        "notes": "Justel MU toelage totaal 3334455.78; partial federal ambulance only — NOT full zone spend; tick1754",
    },
    {
        "budget_id": "bud_bwol_mu_activatie_2025",
        "entity_id": "igs_bwol",
        "year": "2025",
        "amount_eur": "653618",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": "src_bwol_justel_mu_2025",
        "confidence": "strong",
        "notes": "Justel MU activatie 653618; tick1754",
    },
    {
        "budget_id": "bud_bwol_mu_permanentie_2025",
        "entity_id": "igs_bwol",
        "year": "2025",
        "amount_eur": "2680837.78",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "executed",
        "source_id": "src_bwol_justel_mu_2025",
        "confidence": "strong",
        "notes": "Justel MU permanentie 2680837.78; tick1754",
    },
]
append_csv(ROOT / "budgets.csv", budgets)

comm = {
    "commitment_id": "comm_bwol_jr2025_pending_extract",
    "title": "BWOL JR2025 leftover IGS (zoneraad vaststelling + PDF live; euros unextractable; MU 3.33m partial)",
    "entity_id": "igs_bwol",
    "beneficiary": "BWOL / dual mined Genk+Maaseik belt / municipal + federal civiele-veiligheid",
    "legal_basis": "Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid",
    "decision_date": "2026-06-26",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "unknown",
    "evaluation_url": "https://www.maaseik.be/sites/default/files/2026-08/Rekening-2025-BWOL-boek-toezicht.pdf",
    "stated_goal": "Local leftover IGS fire-rescue map VL Genk BWOL — JR2025 approved PDF live; FOI searchable euros",
    "cut_option": "Publish searchable JR2025 rekening (uitgaven/personeel/VTE/gemdot); do not invent full-zone euros from garbled PDF",
    "source_id": "src_bwol_zr_20260626_besluit",
    "confidence": "weak",
    "hierarchy_path": "Vlaanderen>Gemeenten>Genk>IGS>HVZ_BWOL>JR2025_L5",
    "notes": "tick1754; JR2025 Goedgekeurd 26.06.2026; PDF live Maaseik CID/image-garbled; MU 3334455.78 strong partial; FOI ready; not TE-additive of 348bn",
}
append_csv(ROOT / "commitments.csv", [comm])

foi = {
    "gap_id": "gap_bwol_jr2025_rekening_unextractable_l5",
    "hierarchy_path": "Vlaanderen>Gemeenten>Genk>IGS>HVZ_BWOL>JR2025_L5",
    "entity_id": "igs_bwol",
    "what_is_missing": "Official zoneraad 26.06.2026 Jaarrekening 2025 Goedgekeurd; Maaseik publishes full Rekening-2025 PDF but text layer CID/image-garbled — executed uitgaven/personeel/VTE/gemdot not extractable; need searchable BBC",
    "why_it_matters": "HVZ covering 13 Oost-Limburg municipalities / ~329k inwoners — need published extractable JR2025 spend beyond partial MU 3.33m",
    "priority": "8",
    "recipient_body": "Brandweerzone Oost-Limburg / Financiën / bijzonder rekenplichtige",
    "recipient_email": "info@bwol.be",
    "recipient_postal": "C-Mine 50 3600 Genk",
    "draft_letter_path": "docs/doge/foi/drafts/gap_bwol_jr2025_rekening_unextractable_l5.md",
    "status": "ready",
    "date_ready": TODAY,
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_bwol_jr2025_pending_extract",
    "linked_leaderboard_id": "",
    "created_utc": NOW,
    "updated_utc": NOW,
    "notes": "tick1754; human-send only; also facturatie@bwol.be; AGB/NSZ/Dijk92/APEFE still blocked; VBWest JR2025 verdaged",
}
append_csv(ROOT / "foi_queue.csv", [foi])

rq_path = ROOT / "research_queue.csv"
with rq_path.open(encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    fields = reader.fieldnames
    rows = list(reader)

found = False
for row in rows:
    if row["task_id"] == "rq_1754":
        row["status"] = "done"
        row["entity_id"] = "igs_bwol"
        row["notes"] = (
            "DONE tick1754: BWOL KBO 0500.907.802; zoneraad 26.06.2026 JR2025 Goedgekeurd; "
            "Maaseik PDF live CID-garbled; MU 3334455.78; FOI gap_bwol_jr2025_rekening_unextractable_l5"
        )
        row["updated_utc"] = NOW
        found = True
        break
if not found:
    print("WARN rq_1754 not found", file=sys.stderr)
    sys.exit(1)

rows.append(
    {
        "task_id": "rq_1755",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Tick 1755 after 1754 BWOL JR2025 FOI. Next every-10 is 1760. "
            "Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, "
            "Bosgroep residual, ABS/POV/BVAS, other IOED/HVZ (VBWest if JR euros live — verdaged; "
            "Brandweerzone Oost Dendermonde/BZA-full-rekening if PDF live with extractable euros) if official JR2025 euros live, "
            "other IGS/WZC. Do NOT redo BWOL/HVZZuidOost/HVZRand/HVZWaasland/HVZCentrum/HVZRivierenland continuum."
        ),
        "blocked_gap_id": "",
        "created_utc": NOW,
        "updated_utc": NOW,
        "notes": "spawned after tick1754 BWOL FOI; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-VBWest-ZoneOost-BZA; next every-10 1760",
    }
)

with rq_path.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

ls_path = ROOT / "loop_state.csv"
with ls_path.open(encoding="utf-8", newline="") as fh:
    ls_rows = list(csv.DictReader(fh))
    ls_fields = list(ls_rows[0].keys())
ls_rows[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": NOW,
        "last_unit_id": "rq_1754",
        "ticks_completed": "1754",
        "paused": "no",
        "notes": (
            "tick1754 leftover BWOL; KBO 0500.907.802; zoneraad 26.06.2026 JR2025 Goedgekeurd; "
            "Maaseik Rekening-2025 PDF live but CID/image-garbled; Justel MU 3334455.78; FOI searchable rekening; "
            "AGB Bornem JR2024-only; NSZ/Dijk92/APEFE CDN 403; VBWest JR2025 verdaged; "
            "NOT every-10 (next 1760); next rq_1755 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-VBWest-ZoneOost-BZA; continuous hole_fill"
        ),
    }
)
with ls_path.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=ls_fields)
    w.writeheader()
    w.writerows(ls_rows)

log = Path("docs/doge/loop_log.md")
entry = f"""
### {NOW} - tick 1754
- Unit: rq_1754 Brandweerzone Oost-Limburg / BWOL (leftover IGS of mined Genk+Maaseik) (KBO **0500.907.802**; C-Mine 50 3600 Genk; bwol.be; info@bwol.be; official zoneraad **26.06.2026** Jaarrekening 2025 **Goedgekeurd**; Maaseik publishes **Rekening-2025-BWOL** PDF 228p; Justel MU **3334455.78**). Honest leftover AGB Bornem still JR2024-only. NSZ/Dijk92/APEFE CDN **403**. VBWest JR2025 **verdaged**. Preferred AGB/NSZ blocked — leftover BWOL JR2025 **PDF live / euros unextractable** → FOI-ready (anti-stuck) + MU partial. New entity igs_bwol. Envelope = **Unknown** (no invented full-zone euros). NOT every-10 (next 1760).
- Found (strong process / strong MU partial / weak full spend): JR2025 approved; PDF CID/image-garbled (pypdf+pymupdf); AV2025 finance tables deferred; MU activatie **653618** + permanentie **2680837.78** = **3334455.78**.
- Wrote: sources +6; entities +1 igs_bwol; budgets +3 (MU); commitments +1 (unknown envelope); foi_queue +1 ready; rq_1754=done + rq_1755 spawn; ticks_completed=1754. Raw docs/doge/raw/tick1754/. No leaderboard (no sourced annual full-zone €).
- FOI opened: gap_bwol_jr2025_rekening_unextractable_l5 ready (searchable JR/VTE/gemdot). Do not send.
- Next: rq_1755 leftover AGB/**NSZ if CDN 200**/Bosgroep/Dijk92 / APEFE / ABS/POV/BVAS / IOED/HVZ-VBWest-ZoneOost-BZA. Do NOT redo BWOL/HVZZuidOost/HVZRand continuum. NOT every-10 (next **1760**).
"""
with log.open("a", encoding="utf-8") as fh:
    fh.write(entry)

print("OK tick 1754 applied")
