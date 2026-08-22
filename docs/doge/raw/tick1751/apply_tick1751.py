import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T09:15:00Z"
DATE = "2026-08-24"
EID = "igs_hvzw"
GAP = "gap_hvzw_jr2025_rekening_unpublished_l5"
COMM = "comm_hvzw_jr2025_pending_rekening"
SRC = "src_hvzw_zr_jr2025_vaststelling"


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
        "name_nl": "Hulpverleningszone Waasland / HVZ Waasland (leftover IGS hulpverleningszone of mined Sint-Niklaas+Temse; JR2025 vastgesteld unpublished euros; NOT Centrum/Rivierenland/Meetjesland)",
        "name_fr": "Zone de secours Pays de Waes (IGS residuel / zone de secours)",
        "name_en": "Waasland fire-rescue zone leftover IGS of mined Sint-Niklaas belt; JR2025 approved euros unpublished",
        "level": "other",
        "parent_id": "city_sint_niklaas",
        "community_language": "nl",
        "website": "https://www.hvzwaasland.be/",
        "foi_email": "Boekhouding@hvzwaasland.be",
        "foi_postal": "Nijverheidsstraat 33 9100 Sint-Niklaas",
        "notes": "tick1751 leftover HVZ Waasland after Centrum; KBO 0500.928.388; zoneraad 01.07.2026 Vaststelling Begrotings- en jaarrekening 2025 Goedgekeurd; euros unpublished on portal (meldingslijst only); FOI ready; AGB/NSZ/Dijk92/APEFE still blocked",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": SRC,
        "title": "HVZ Waasland zoneraad 01.07.2026 meldingslijst — Begrotings- en jaarrekening 2025 Vaststelling Goedgekeurd",
        "url": "https://cdn.prod.website-files.com/68b9ea0c64b4393f8cabeb7f/6a46159d1355a0703a54db57_Meldingslijst%20ZR%20-%201%20juli%202026%2009-00.pdf",
        "publisher": "Hulpverleningszone Waasland",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1751; 2026_ZR_00030 Begrotings- en jaarrekening 2025 Vaststelling Goedgekeurd; euros not in meldingslijst; FOI full rekening",
    },
    {
        "source_id": "src_hvzw_besluitvorming",
        "title": "HVZ Waasland besluitvorming portal (zoneraad/zonecollege)",
        "url": "https://www.hvzwaasland.be/over-ons/besluitvorming",
        "publisher": "Hulpverleningszone Waasland",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1751; public meldingslijsten; JR2025 body not attached",
    },
    {
        "source_id": "src_hvzw_kbo",
        "title": "HVZ Waasland KBO 0500.928.388",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=500928388",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1751; Hulpverleningszone; Nijverheidsstraat 33 9100 Sint-Niklaas",
    },
    {
        "source_id": "src_hvzw_foi_contact_1751",
        "title": "HVZ Waasland FOI / boekhouding channel",
        "url": "https://www.hvzwaasland.be/contact",
        "publisher": "Hulpverleningszone Waasland",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1751; Boekhouding@hvzwaasland.be; Nijverheidsstraat 33 9100 Sint-Niklaas",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("commitments.csv")
rows.append(
    {
        "commitment_id": COMM,
        "title": "HVZ Waasland JR2025 leftover IGS (zoneraad vaststelling live; rekening euros unpublished)",
        "entity_id": EID,
        "beneficiary": "HVZ Waasland / dual mined Sint-Niklaas belt / municipal + federal civiele-veiligheid",
        "legal_basis": "Wet 15.05.2007 civiele veiligheid; KB boekhouding hulpverleningszones; Bestuursdecreet openbaarheid",
        "decision_date": "2026-07-01",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "unknown",
        "evaluation_url": "https://cdn.prod.website-files.com/68b9ea0c64b4393f8cabeb7f/6a46159d1355a0703a54db57_Meldingslijst%20ZR%20-%201%20juli%202026%2009-00.pdf",
        "stated_goal": "Local leftover IGS fire-rescue map VL Waasland — JR2025 approved; FOI publish rekening euros",
        "cut_option": "Publish full begrotings- en jaarrekening 2025 (uitgaven/personeel/VTE/gemdot/fed); do not invent euros",
        "source_id": SRC,
        "confidence": "weak",
        "hierarchy_path": "Vlaanderen>Gemeenten>SintNiklaas>IGS>HVZ_Waasland>JR2025_L5",
        "notes": "tick1751; JR2025 Vaststelling Goedgekeurd 01.07.2026; no public euros this tick; FOI ready; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Gemeenten>SintNiklaas>IGS>HVZ_Waasland>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official zoneraad 01.07.2026 Vaststelling Begrotings- en jaarrekening 2025 Goedgekeurd (2026_ZR_00030); full rekening euros (uitgaven gewone/personeel/VTE/balans/gemdot per gemeente/fed dots) unpublished on portal (meldingslijst only)",
        "why_it_matters": "HVZ covering 6 Waasland municipalities with ~550 staff — need published JR2025 spend transparency after official vaststelling",
        "priority": "8",
        "recipient_body": "Hulpverleningszone Waasland / dienst boekhouding / zonesecretaris",
        "recipient_email": "Boekhouding@hvzwaasland.be",
        "recipient_postal": "Nijverheidsstraat 33 9100 Sint-Niklaas",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": DATE,
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1751; human-send only; AGB/NSZ/Dijk92/APEFE still blocked; Rand Brecht dotatie PDF image-only this tick",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1751":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = "HVZ Waasland JR2025 leftover dual residual (vaststelling live / euros FOI)"
        r["notes"] = "DONE tick1751: HVZ Waasland KBO 0500.928.388 zoneraad 01.07.2026 JR2025 Vaststelling Goedgekeurd; euros unpublished; FOI ready gap_hvzw_jr2025_rekening_unpublished_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1752",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1752 after 1751 HVZ Waasland JR2025 FOI-ready. Next every-10 is 1760. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, ABS/POV/BVAS, other IOED/HVZ (Rand/VBWest/Zuid-Oost/Oost-Limburg/BZA-full-rekening if PDF live with euros) if official JR2025 euros live, other IGS/WZC. Do NOT redo HVZWaasland/HVZCentrum/HVZRivierenland/Zusterhof/HofSchoten/Buitenhof/Familiehof/Akapella/DeVerlosser/VivaltoHomeBE/already-mined HVZs.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1751 HVZ Waasland FOI; NEXT AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-Rand-VBWest-BZA; next every-10 1760",
    }
)
write("research_queue.csv", fields, rows)
print("rq", len(rows))

fields, rows = read("loop_state.csv")
rows[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1751",
        "ticks_completed": "1751",
        "paused": "no",
        "notes": "tick1751 leftover HVZ Waasland residual; KBO 0500.928.388; zoneraad 01.07.2026 JR2025 Vaststelling Goedgekeurd; euros unpublished (meldingslijst only); FOI ready; AGB Bornem JR2024-only; NSZ/Dijk92/APEFE CDN 403; Rand Brecht dotatie PDF image-only; NOT every-10 (next 1760); next rq_1752 AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-Rand-VBWest-BZA; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
