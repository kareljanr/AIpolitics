#!/usr/bin/env python3
"""tick2569 leftover dual Hoito Tienen — append-only large CSVs."""
import csv, json, os
from datetime import datetime, timezone
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = "2026-08-29"
TICK = "2569"

eid = "vzw_hoito_tienen"
src_pdf = "src_hoito_tienen_jr2025_nbb_pdf_2569"
src_kbo = "src_hoito_tienen_kbo_2569"
src_vaph = "src_hoito_tienen_vaph_2569"
src_site = "src_hoito_tienen_site_2569"
comm_id = "comm_hoito_tienen_jr2025_statutory_70_76a_jump_2_87m_73_jump_2_79m_9901_jump_99k"
lb_id = "lb_hoito_tienen_70_76a_jump_2_87m_73_jump_2_79m_9901_jump_99k_jr2025"
gap_id = "gap_hoito_tienen_vaph_matrix_70_76a_jump_2_87m_73_jump_2_79m_9901_jump_99k_l5"
hier = "Vlaanderen>Vlaams-Brabant>Tienen>Hoito>JR2025"
hier_foi = "Vlaanderen>Vlaams-Brabant>Tienen>Hoito>leftover_vaph"

def append_csv(path, rows):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    ids = {list(row.values())[0] for row in existing}
    for row in rows:
        kid = list(row.values())[0]
        if kid in ids:
            raise SystemExit(f"ID collision {kid} in {path}")
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        for row in rows:
            out = {k: row.get(k, "") for k in fieldnames}
            w.writerow(out)

sources = [
    {
        "source_id": src_pdf,
        "title": "NBB VOL-VZW jaarrekening 2025 Hoito deposit 2026-00188348",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00188348.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2569; official native statutory PDF 73962 bytes 26p VOL-VZW 25.0.13 m05-f; header 23/06/2026; AV 19.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-23 22:40:04 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN GET 200 73962 MD5 ffa4a5283de20f6859f7d6a9dc2b4ad2; NBB published-deposits list official consult page this tick YE2025 2026-00188348 + YE2024 2025-00122918; NBB consult HTML stub 5344 B discarded; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.3.5 6.3.6 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.10 6.13 6.14 6.15 6.16 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; leftover city_genk leftover VAPH Bethanie 0414.744.977 SCAN/OCR Xerox AltaLink HARD SKIP this tick; leftover city_lokeren leftover VAPH Emiliani remine@2568 HARD SKIP",
    },
    {
        "source_id": src_kbo,
        "title": "KBO Hoito 0429.766.220",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0429766220",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2569; Actief Normale toestand; VZW; naam Hoito since 02.06.2025 (was Begeleid Wonen Tienen); official zetel Beauduinstraat 150 3300 Tienen since 27.12.2004; 1 VE leftover-mined city_tienen 2.154.428.792 Sociaal Pedagogische Dienst - Dienst Begeleid Wonen Beauduinstraat 150 since 13.06.2006; RSZ2025 88.999 Andere vormen van maatschappelijke dienstverlening zonder huisvesting neg; Werkgever RSZ since 03.01.1985; FOI ann.berwaerts@hoito.be from official NBB PDF + secretariaat@begeleidwonentienen.be from official VAPH + info@hoito.be from official Staatsblad; Identity trap 0429.766.220 != leftover city GE Tienen 0207.525.758 != leftover AGB Tienen 0872.382.861 != leftover CAR DAT 0463.347.917 remine@2382 != leftover Hartjes 0441.374.348 remine@2450 != leftover Ooievaarsnest 0418.588.256 remine@2465 != leftover Huis in de Stad 0407.637.748 remine@2308 != leftover Blankedale 0400.999.978 remine@2188 != leftover Emiliani 0421.911.297 remine@2568 != leftover Oikonde 0414.341.933 remine@2567 != leftover Vondels 0415.108.728 remine@2566 != leftover Duinhelm 0413.223.562 remine@2565 != leftover Bethanie 0414.744.977 SCAN skip",
    },
    {
        "source_id": src_vaph,
        "title": "VAPH adreslijst Hoito Vergunde Zorgaanbieder + RTH",
        "url": "https://www.vaph.be/organisaties/adressen/hoito",
        "publisher": "VAPH",
        "accessed_date": DATE,
        "source_class": "primary",
        "notes": "tick2569; official VAPH adreslijst Hoito Vergunde Zorgaanbieder + Rechtstreeks toegankelijke hulp; admin adres Beauduinstraat 150 3300 Tienen; FOI secretariaat@begeleidwonentienen.be from official VAPH; leftover mined city_tienen leftover VAPH after city GE tick1274 leftover-mined AGB-only leftover type (AGB Tienen tick1272); FIRST LOCK leftover city_tienen leftover VAPH Hoito",
    },
    {
        "source_id": src_site,
        "title": "Hoito official site FOI email",
        "url": "https://www.hoito.be/",
        "publisher": "Hoito VZW",
        "accessed_date": DATE,
        "source_class": "org",
        "notes": "tick2569; FOI ann.berwaerts@hoito.be from official NBB PDF + secretariaat@begeleidwonentienen.be from official VAPH + info@hoito.be from official Staatsblad naamwijziging 02.06.2025; leftover mined city_tienen leftover VAPH unused leftover type after city GE tick1274 leftover-mined AGB-only leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover city_lokeren leftover VAPH Emiliani remine@2568; NOT leftover city_mechelen leftover VAPH Oikonde remine@2567; NOT leftover city_ieper leftover VAPH Vondels remine@2566; NOT leftover Bethanie SCAN skip; NOT leftover CAR DAT remine@2382; NOT leftover Huis in de Stad remine@2308",
    },
]
append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": eid,
    "name_nl": "Hoito VZW (ex Begeleid Wonen Tienen / VAPH Vergunde Zorgaanbieder + RTH; begeleid wonen volwassenen met handicap)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_tienen",
    "community_language": "nl",
    "website": "https://www.hoito.be/",
    "foi_email": "ann.berwaerts@hoito.be",
    "foi_postal": "Beauduinstraat 150, 3300 Tienen",
    "notes": "tick2569 YE2025 Strong official native NBB PDF deposit 2026-00188348 + Strong KBO 0429.766.220 Actief 1 VE; leftover mined city_tienen leftover VAPH unused leftover-mined AGB-only leftover type after city GE tick1274; official zetel Beauduinstraat 150 3300 Tienen; RSZ2025 88.999; envelope 70/76A JUMP 2865864; 73 JUMP 2786262; 9901 JUMP 99051; 9904 JUMP 123462; debt JUMP 490193; cash JUMP 474597 (+128613); FTE 34,3 JUMP; Identity trap != leftover city GE 0207.525.758 != leftover AGB Tienen 0872.382.861 != leftover CAR DAT 0463.347.917 != leftover Hartjes 0441.374.348 != leftover Ooievaarsnest 0418.588.256 != leftover Huis in de Stad 0407.637.748 != leftover Blankedale 0400.999.978 != leftover Emiliani 0421.911.297; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/CuraCare/OCMW/commercial BV/convent",
}]
append_csv("docs/doge/data/entities.csv", entities)

def bud(bid, amount, basis, notes, empty=False):
    if empty:
        return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}
    a = str(amount)
    return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": a, "amount_min_eur": a, "amount_max_eur": a, "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}

budgets = [
    bud("bud_hoito_tienen_70_76a_jr2025_statutory", 2865864, "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +11.67%", "tick2569; PDF native; YE2024 2566396 identical; envelope 70/76A because VZW and omzet70 commercial-only vs large 73; FOI VAPH matrix behind 2865864"),
    bud("bud_hoito_tienen_omzet70_jr2025_statutory", 54564, "NBB VOL-VZW code 70 omzet YE2025 JUMP +45.41%", "tick2569; PDF native; YE2024 37523 identical; commercial-only vs large 73"),
    bud("bud_hoito_tienen_73_jr2025_statutory", 2786262, "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +11.59%", "tick2569; PDF native; YE2024 2496977 identical; 733 subsidies 2772253; 731 schenkingen 14008; VAPH subsidy envelope"),
    bud("bud_hoito_tienen_76a_jr2025_statutory", "", "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "tick2569; PDF native; YE2024 1986 identical; 74 25039 vs 29909", empty=True),
    bud("bud_hoito_tienen_personnel62_jr2025_statutory", 2479454, "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +8.97%", "tick2569; PDF native; YE2024 2275278 identical; FTE 9087 34,3 JUMP from 31,7"),
    bud("bud_hoito_tienen_630_jr2025_statutory", 66577, "NBB VOL-VZW code 630 afschrijvingen YE2025 DROP -20.79%", "tick2569; PDF native; YE2024 84049 identical"),
    bud("bud_hoito_tienen_bedrijfswinst_jr2025_statutory", 99051, "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +857%", "tick2569; PDF native; YE2024 10345 identical; +88706"),
    bud("bud_hoito_tienen_pnl_jr2025_statutory", 123462, "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +194.30%", "tick2569; PDF native; YE2024 41951 identical; 9903 123462 JUMP"),
    bud("bud_hoito_tienen_equity_jr2025_statutory", 2024353, "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +7.58%", "tick2569; PDF native; YE2024 1881754 identical"),
    bud("bud_hoito_tienen_assets_jr2025_statutory", 2514546, "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +7.91%", "tick2569; PDF native; YE2024 2330214 identical; debt 17/49 490193 JUMP vs 448460"),
    bud("bud_hoito_tienen_cash_jr2025_statutory", 474597, "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +37.17%", "tick2569; PDF native; YE2024 345984 identical; +128613; geldbeleggingen 50/53 1547410 vs 1530573"),
]
append_csv("docs/doge/data/budgets.csv", budgets)

cash_json = json.dumps({"2025": 474597, "2024": 345984}, separators=(",", ":"))
commitments = [{
    "commitment_id": comm_id,
    "title": "Hoito Tienen YE2025 (70/76A JUMP 2.87m / 73 JUMP 2.79m / 9901 JUMP 99k / Strong PDF)",
    "entity_id": eid,
    "beneficiary": "VAPH + leftover city_tienen leftover dual",
    "legal_basis": "Hoito VZW (KBO 0429.766.220; Actief; 1 VE; official zetel Tienen; RSZ2025 88.999; VAPH Vergunde Zorgaanbieder + RTH; naamwijziging Begeleid Wonen Tienen 02.06.2025)",
    "decision_date": "2026-06-19",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "2865864",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00188348.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_tienen leftover-mined AGB-only leftover VAPH",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind 70/76A JUMP 2865864 and 73 JUMP 2786262 and why 9901 JUMP 99051 (+88706) while cash JUMP 474597 (+128613) 9904 JUMP 123462 debt JUMP 490193 and FTE 34,3 JUMP",
    "source_id": src_pdf,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Tienen>Hoito>JR2025_statutory_L5",
    "notes": "tick2569; Strong official native PDF; leftover mined city_tienen leftover VAPH unused leftover-mined AGB-only leftover type after city GE tick1274; 1 VE; prior-year identical; FIRST LOCK leftover city_tienen leftover VAPH Hoito; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}]
append_csv("docs/doge/data/commitments.csv", commitments)

leaderboard = [{
    "item_id": lb_id,
    "name": "Hoito Tienen 70/76A JUMP 2.87m / 73 JUMP 2.79m / 9901 JUMP 99k (YE2025 leftover city_tienen leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": hier,
    "annual_cost_eur": "2865864",
    "total_cost_eur": "2865864",
    "tco_notes": "PDF 70/76A 2865864 JUMP; 73 2786262 JUMP; omzet70 54564 commercial-only; 76A empty; bedrijfswinst JUMP 99051; pnl JUMP 123462; equity JUMP 2024353; assets JUMP 2514546; debt JUMP 490193; cash JUMP 474597; personnel62 JUMP 2479454; leftover city_tienen leftover VAPH",
    "confidence": "strong",
    "source_id": src_pdf,
    "beneficiaries": "VAPH + leftover city_tienen leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_tienen leftover-mined AGB-only leftover VAPH",
    "measured_outcome": "2.87m 70/76A JUMP; 2.79m 73 JUMP; 99k 9901 JUMP; 129k cash JUMP; 34,3 FTE JUMP; leftover city_tienen leftover VAPH",
    "absurdity_score": "5.70",
    "cost_score": "5.80",
    "difficulty": "4.50",
    "priority_index": "5.50",
    "cut_proposal": "FOI VAPH / gemeente Tienen matrix behind 70/76A 2865864 and 73 2786262 and why 9901 JUMP 99051 (+88706 vs 10345) while cash JUMP 474597 (+128613 vs 345984) and 9904 JUMP 123462 and debt JUMP 490193 and FTE 34,3 JUMP from 31,7",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2569 leftover mined city_tienen leftover VAPH Hoito after city GE tick1274 leftover-mined AGB-only leftover VAPH; FIRST LOCK leftover city_tienen leftover VAPH Hoito; HARD SKIP leftover city_lokeren leftover VAPH Emiliani remine@2568 leftover Oikonde remine@2567 leftover Vondels remine@2566 leftover Duinhelm remine@2565 leftover Bethanie SCAN leftover CAR DAT remine leftover Huis in de Stad remine leftover Hartjes remine leftover Ooievaarsnest remine leftover Blankedale remine; 1 VE; prior-year identical; next rq_2570 leftover dual PLUS every-10; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; never mix off-TE dual into 348bn TE pie",
}]
append_csv("docs/doge/data/leaderboard.csv", leaderboard)

foi_rows = [{
    "gap_id": gap_id,
    "hierarchy_path": hier_foi,
    "entity_id": eid,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VOL-VZW YE2025 70/76A JUMP 2865864 vs omzet70 commercial-only 54564, 73 JUMP 2786262 with 9901 JUMP 99051 (+88706) while cash JUMP 474597 (+128613) 9904 JUMP 123462 debt JUMP 490193 and FTE 34,3 JUMP",
    "why_it_matters": "Public leftover VAPH dual of mined city_tienen leftover-mined AGB-only leftover VAPH shows 2.87m 70/76A envelope while subsidy matrix and 99k 9901 JUMP amid 129k cash JUMP stay unsourced",
    "priority": "7",
    "recipient_body": "Hoito VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "ann.berwaerts@hoito.be",
    "recipient_postal": "Beauduinstraat 150, 3300 Tienen",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": DATE,
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": comm_id,
    "linked_leaderboard_id": lb_id,
    "created_utc": NOW,
    "updated_utc": NOW,
    "notes": "tick2569; concept NOT verzonden; Strong PDF 2026-00188348; prio7",
}]
append_csv("docs/doge/data/foi_queue.csv", foi_rows)

Path("/tmp/tick2569").mkdir(parents=True, exist_ok=True)
Path("/tmp/tick2569/NOW.txt").write_text(NOW)
Path("/tmp/tick2569/IDS.json").write_text(json.dumps({"eid": eid, "gap_id": gap_id, "comm_id": comm_id, "lb_id": lb_id, "NOW": NOW}))
print("NOW", NOW)
print("appended sources+4 entities+1 budgets+11 commitments+1 leaderboard+1 foi+1")
