import csv
from pathlib import Path

csv.field_size_limit(10**7)
base = Path("docs/doge/data")
UTC = "2026-08-24T08:35:00Z"
DATE = "2026-08-24"
EID = "igs_hvzc"
GAP = "gap_hvzc_gent_dot_46_93m_zone_rekening_l5"
COMM = "comm_hvzc_jr2025_gent_dot"
LB = "lb_hvzc_gent_dot_46_93m_zone_rekening"
SRC = "src_hvzc_gent_dotatie_2025"
PDF = "https://ebesluitvorming.gent.be/document/690ca39aed6961690d9e21e9"


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
        "name_nl": "Brandweerzone Centrum / HVZ Centrum (leftover IGS hulpverleningszone of mined Gent+Merelbeke-Melle; NOT Rivierenland/Meetjesland/OostOVL)",
        "name_fr": "Zone de secours Centre (IGS residuel / zone de secours Gand)",
        "name_en": "Brandweerzone Centrum leftover fire-rescue IGS of mined Gent belt municipalities",
        "level": "other",
        "parent_id": "city_gent",
        "community_language": "nl",
        "website": "https://www.brandweerzonecentrum.be/",
        "foi_email": "zonesecretariaat@bwzc.be",
        "foi_postal": "Roggestraat 70 9000 Gent",
        "notes": "tick1749 leftover HVZ Centrum after Rivierenland; KBO 0500.927.497; official Gent GR 17.11.2025 dotatie 2025 expl 42392583.88 invest 4224870 pens 315000; zone JR rekening FOI; 16 gemeenten",
    }
)
write("entities.csv", fields, rows)
print("entities", len(rows))

fields, rows = read("sources.csv")
new_sources = [
    {
        "source_id": SRC,
        "title": "Stad Gent GR 2025_GR_01012 HVZ Centrum gewijzigde dotatie dienstjaar 2025",
        "url": PDF,
        "publisher": "Stad Gent / ebesluitvorming",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1749; GR 17.11.2025; expl 42392583.88 invest 4224870 pens 315000 ristorno -1917070.84 voorgestelde uitgaven 45015383.04; zoneraad budget 22.10.2025; zone resultaat 2.5m mentioned",
    },
    {
        "source_id": "src_hvzc_kbo",
        "title": "Brandweerzone Centrum KBO 0500.927.497",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=500927497",
        "publisher": "KBO",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1749; Hulpverleningszone; Roggestraat 70 9000 Gent; zonesecretariaat@bwzc.be",
    },
    {
        "source_id": "src_hvzc_portal",
        "title": "Brandweerzone Centrum portal",
        "url": "https://www.brandweerzonecentrum.be/",
        "publisher": "Brandweerzone Centrum",
        "accessed_date": DATE,
        "source_class": "primary_official",
        "notes": "tick1749; 16 gemeenten; info@bwzc.be / zonesecretariaat@bwzc.be",
    },
    {
        "source_id": "src_hvzc_foi_contact_1749",
        "title": "Brandweerzone Centrum FOI channel",
        "url": "https://www.brandweerzonecentrum.be/contact",
        "publisher": "Brandweerzone Centrum",
        "accessed_date": DATE,
        "source_class": "foi_contact",
        "notes": "tick1749; zonesecretariaat@bwzc.be; Roggestraat 70 9000 Gent",
    },
]
for s in new_sources:
    assert not any(r["source_id"] == s["source_id"] for r in rows)
    rows.append(s)
write("sources.csv", fields, rows)
print("sources", len(rows))

fields, rows = read("budgets.csv")
budgets = [
    ("bud_hvzc_gent_expl_2025", "2025", "42392583.88", "budget", SRC, "strong", "Gent exploitatiedotatie HVZC 2025 42392583.88; tick1749"),
    ("bud_hvzc_gent_invest_2025", "2025", "4224870", "budget", SRC, "strong", "Gent investeringsdotatie HVZC 2025 4224870; tick1749"),
    ("bud_hvzc_gent_pensioen_2025", "2025", "315000", "budget", SRC, "strong", "Gent pensioenbijdrage HVZC 2025 315000; tick1749"),
    ("bud_hvzc_gent_gross_dot_2025", "2025", "46932453.88", "budget", SRC, "strong", "Gent gross dots expl+invest+pens 46932453.88; tick1749"),
    ("bud_hvzc_gent_ristorno_2025", "2025", "-1917070.84", "budget", SRC, "strong", "Gent ristorno begrotingsresultaat -1917070.84 (zone resultaat 2.5m mentioned); tick1749"),
    ("bud_hvzc_gent_net_outlay_2025", "2025", "45015383.04", "budget", SRC, "strong", "Gent voorgestelde uitgaven net 45015383.04; tick1749"),
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
        "title": "HVZ Centrum JR2025 leftover IGS (Gent dot 46.93m gross / 45.02m net; full zone rekening FOI)",
        "entity_id": EID,
        "beneficiary": "HVZ Centrum / dual mined Gent belt / municipal + federal civiele-veiligheid",
        "legal_basis": "Wet 15.05.2007 civiele veiligheid art 67-68; Decreet lokaal bestuur; Bestuursdecreet openbaarheid",
        "decision_date": "2025-11-17",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "46932453.88",
        "cash_by_year": "",
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": PDF,
        "stated_goal": "Local leftover IGS fire-rescue map VL Gent HVZ Centrum — Gent municipal dots 46.93m; FOI full zone rekening",
        "cut_option": "Publish full zone JR2025 rekening (uitgaven/personeel/VTE/all-gemeente dots); scrutinise Gent 73% share path; disclose 2.5m zone resultaat ristorno mechanics",
        "source_id": SRC,
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>Gemeenten>Gent>IGS>HVZ_Centrum>JR2025_L5",
        "notes": "tick1749; Gent gross 46.93m (expl 42.39 invest 4.22 pens 0.32) net 45.02m after ristorno; NOT full zone TE; full rekening FOI; not TE-additive of 348bn",
    }
)
write("commitments.csv", fields, rows)
print("commitments", len(rows))

fields, rows = read("leaderboard.csv")
rows.append(
    {
        "item_id": LB,
        "name": "HVZ Centrum 2025: Gent municipal dots 46.93m (full zone rekening FOI)",
        "level": "L5",
        "type": "local_budget_line",
        "hierarchy_path": "Vlaanderen>Gemeenten>Gent>IGS>HVZ_Centrum>JR2025_L5",
        "annual_cost_eur": "46932453.88",
        "total_cost_eur": "46932453.88",
        "tco_notes": "Leftover Brandweerzone Centrum (KBO 0500.927.497) via official Stad Gent GR 17.11.2025: Gent exploitatiedotatie 42.39m + invest 4.22m + pensioen 0.32m = gross 46.93m; ristorno -1.92m (Gent share of zone begrotingsresultaat 2.5m) → net proposed outlays 45.02m; Gent ~73% of zone verdeelsleutel; FULL zone JR2025 rekening (uitgaven/personeel/VTE/all 16 gemeenten) still unpublished this tick — FOI; NSZ/Dijk92/APEFE CDN 403; AGB Bornem JR2024-only",
        "confidence": "strong",
        "source_id": SRC,
        "beneficiaries": "Gent + 15 HVZC municipalities / municipal + federal civiele-veiligheid",
        "stated_goal": "Local leftover HVZ Centrum map — official Gent 2025 dots after Rivierenland residual",
        "measured_outcome": "Official Gent GR 2026-08-24: expl 42392583.88 / invest 4224870 / pens 315000 / gross 46932453.88 / ristorno -1917070.84 / net 45015383.04",
        "absurdity_score": "4.0",
        "cost_score": "7.0",
        "difficulty": "2.5",
        "priority_index": "5.5",
        "cut_proposal": "Publish full zone JR2025 rekening + all-gemeente dots; scrutinise staff share once live; stop Gent-only opacity on 16-municipality fire zone",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1749; leftover after AGB Bornem JR2024-only / NSZ CDN403 / Dijk92 CDN403 / APEFE CDN403 / Rivierenland done; BZA JR afkondiging live but rekening PDFs not currently downloadable; not TE-additive of 348bn",
    }
)
write("leaderboard.csv", fields, rows)
print("leaderboard", len(rows))

fields, rows = read("foi_queue.csv")
rows.append(
    {
        "gap_id": GAP,
        "hierarchy_path": "Vlaanderen>Gemeenten>Gent>IGS>HVZ_Centrum>JR2025_L5",
        "entity_id": EID,
        "what_is_missing": "Official Gent GR publishes Gent dots expl 42392583.88 / invest 4224870 / pens 315000 / ristorno -1917070.84; full Brandweerzone Centrum JR2025 rekening (uitgaven gewone/personeel/VTE/balans/all-gemeente dots / fed dots) and zoneraad JR besluit unpublished",
        "why_it_matters": "Large HVZ covering 16 municipalities with Gent alone contributing 46.9m — need full zone spend transparency beyond one-member dots",
        "priority": "8",
        "recipient_body": "Brandweerzone Centrum / dienst openbaarheid / zonesecretaris",
        "recipient_email": "zonesecretariaat@bwzc.be",
        "recipient_postal": "Roggestraat 70 9000 Gent",
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
        "notes": "tick1749; human-send only; also info@bwzc.be; AGB/NSZ/Dijk92/APEFE still blocked preferred path",
    }
)
write("foi_queue.csv", fields, rows)
print("foi", len(rows))

fields, rows = read("research_queue.csv")
found = False
for r in rows:
    if r["task_id"] == "rq_1749":
        r["status"] = "done"
        r["entity_id"] = EID
        r["updated_utc"] = UTC
        r["blocked_gap_id"] = GAP
        r["title"] = "HVZ Centrum / Brandweerzone Centrum JR2025 leftover dual residual"
        r["notes"] = "DONE tick1749: HVZ Centrum KBO 0500.927.497 Gent dots 2025 gross 46932453.88 net 45015383.04; FOI ready gap_hvzc_gent_dot_46_93m_zone_rekening_l5"
        found = True
assert found
rows.append(
    {
        "task_id": "rq_1750",
        "title": "leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": "Tick 1750 after 1749 HVZ Centrum. MUST refresh progress_every_10_ticks.md + doge_waste_top10_current.md (every-10). Then one leftover unit: prefer leftover AGB/APB if PDF live (Bornem still JR2024), else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, ABS/POV/BVAS, other IOED/HVZ (Waasland/Rand/VBWest/Zuid-Oost/Oost-Limburg/BZA-full-rekening if PDF live) if official JR2025 euros live, other IGS/WZC. Do NOT redo HVZCentrum/HVZRivierenland/Zusterhof/HofSchoten/Buitenhof/Familiehof/Akapella/DeVerlosser/VivaltoHomeBE/Prinsenhof/already-mined HVZs.",
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1749 HVZ Centrum; NEXT every-10 MUST + AGB/NSZ-if-200/Bosgroep/Dijk92/APEFE/HVZ-Waasland-Rand-BZA-rekening",
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
        "last_unit_id": "rq_1749",
        "ticks_completed": "1749",
        "paused": "no",
        "notes": "tick1749 leftover HVZ Centrum residual; KBO 0500.927.497; official Gent GR 2025_GR_01012; sourced euros Gent expl 42392583.88 invest 4224870 pens 315000 gross 46932453.88 ristorno -1917070.84 net 45015383.04; zone resultaat 2.5m mentioned; FOI full zone rekening; AGB Bornem JR2024-only; NSZ/Dijk92/APEFE CDN 403; BZA JR afkondiging live rekening PDFs not on page; NOT every-10 (next 1750 MUST progress); next rq_1750 every-10 + AGB/NSZ/Bosgroep/HVZ-Waasland-Rand; continuous hole_fill",
    }
)
write("loop_state.csv", fields, rows)
print("loop_state ok")
print("DONE writes")
