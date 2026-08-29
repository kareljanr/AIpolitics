#!/usr/bin/env python3
"""tick2568 leftover dual Emiliani Lokeren — append-only large CSVs."""
import csv, json, os
from datetime import datetime, timezone
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = "2026-08-29"
TICK = "2568"

eid = "vzw_emiliani_lokeren"
src_pdf = "src_emiliani_lokeren_jr2025_nbb_pdf_2568"
src_kbo = "src_emiliani_lokeren_kbo_2568"
src_vaph = "src_emiliani_lokeren_vaph_2568"
src_site = "src_emiliani_lokeren_site_2568"
comm_id = "comm_emiliani_lokeren_jr2025_statutory_70_76a_jump_22_02m_73_jump_18_57m_debt_jump_5_02m"
lb_id = "lb_emiliani_lokeren_70_76a_jump_22_02m_73_jump_18_57m_debt_jump_5_02m_jr2025"
gap_id = "gap_emiliani_lokeren_vaph_matrix_70_76a_jump_22_02m_73_jump_18_57m_debt_jump_5_02m_l5"
hier = "Vlaanderen>Oost-Vlaanderen>Lokeren>Emiliani>JR2025"
hier_foi = "Vlaanderen>Oost-Vlaanderen>Lokeren>Emiliani>leftover_vaph"

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
        "title": "NBB VOL-VZW jaarrekening 2025 Emiliani deposit 2026-00260230",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00260230.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2568; official native statutory PDF 1218604 bytes 50p VOL-VZW 26.0.15 m05-f; header 07/07/2026; AV 26.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-07 07:08:30 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN GET 200 1218604 MD5 4b1db1dc294340a7824007d9993841af; NBB UUID 0c67c915-79d1-11f1-a491-8f537c3b104c; NBB published-deposits list 8 this tick with sort=depositDate,desc; NBB consult HTML stub 5344 B discarded; VOL-VZW 6.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.2 6.5.1 6.5.2 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; leftover city_genk leftover VAPH Bethanie 0414.744.977 SCAN/OCR Xerox AltaLink HARD SKIP this tick",
    },
    {
        "source_id": src_kbo,
        "title": "KBO Emiliani 0421.911.297",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421911297",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2568; Actief Normale toestand; VZW; official zetel Krekelstraat 17 9160 Lokeren since 01.01.2025 (KBO technical address-code change); 7 VE leftover-mined city_lokeren all 9160 Lokeren 2.152.232.436 vzw Emiliani Krekelstraat 17 since 15.03.2006 + 2.366.555.322 Woonproject Schoolstraat 14 bus W003 since 01.11.2023 + 2.366.556.312 Villa Molenbergplein 6A since 01.01.2016 + 2.366.558.587 De Teerling Daknam-dorp 89 since 01.01.2006 + 2.366.558.686 t Eikenhof Eekstraat 218 since 01.01.2016 + 2.366.558.884 Jan Persoonsstraat 56 since 01.10.2014 + 2.366.559.181 Jan Persoonsstraat 58 since 01.10.2014; RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een mentale handicap; Werkgever RSZ since 01.01.1982; FOI info@emiliani.be from official NBB PDF + VAPH; Identity trap 0421.911.297 != leftover city GE Lokeren 0207.463.402 != leftover AGB Lokeren 1031.996.262 != leftover Hagewinde 0861.262.010 remine@2481 != leftover Alderande 0431.893.389 remine@2489 != leftover De Sperwer 0415.344.892 remine@2490 != leftover CAR Waas 0415.472.279 remine@2397 != leftover De Cirkel 0470.413.079 remine@2338 != leftover Ter Engelen 0430.882.809 remine@1731 != leftover Oikonde 0414.341.933 remine@2567 != leftover Vondels 0415.108.728 remine@2566 != leftover Duinhelm 0413.223.562 remine@2565 != leftover Bethanie 0414.744.977 SCAN skip",
    },
    {
        "source_id": src_vaph,
        "title": "VAPH adreslijst Emiliani Vergunde Zorgaanbieder + RTH",
        "url": "https://www.vaph.be/organisaties/adressen/emiliani",
        "publisher": "VAPH",
        "accessed_date": DATE,
        "source_class": "primary",
        "notes": "tick2568; official VAPH adreslijst Emiliani Vergunde Zorgaanbieder + Rechtstreeks toegankelijke hulp; admin adres Krekelstraat 17 9160 Lokeren; FOI info@emiliani.be from official VAPH; leftover mined city_lokeren leftover VAPH after city GE tick865 leftover-mined AGB-only leftover type (AGB Lokeren tick1200); FIRST LOCK leftover city_lokeren leftover VAPH Emiliani",
    },
    {
        "source_id": src_site,
        "title": "Emiliani official site FOI email",
        "url": "https://www.emiliani.be/",
        "publisher": "Emiliani VZW",
        "accessed_date": DATE,
        "source_class": "org",
        "notes": "tick2568; FOI info@emiliani.be from official NBB PDF + official VAPH; leftover mined city_lokeren leftover VAPH unused leftover type after city GE tick865 leftover-mined AGB-only leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover city_mechelen leftover VAPH Oikonde remine@2567; NOT leftover city_ieper leftover VAPH Vondels remine@2566; NOT leftover Bethanie SCAN skip; NOT leftover Hagewinde remine@2481; NOT leftover Alderande remine@2489; NOT leftover De Sperwer remine@2490",
    },
]
append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": eid,
    "name_nl": "Emiliani VZW (Lokeren / VAPH Vergunde Zorgaanbieder + RTH; woonondersteuning volwassenen met verstandelijke handicap)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_lokeren",
    "community_language": "nl",
    "website": "https://www.emiliani.be/",
    "foi_email": "info@emiliani.be",
    "foi_postal": "Krekelstraat 17, 9160 Lokeren",
    "notes": "tick2568 YE2025 Strong official native NBB PDF deposit 2026-00260230 + Strong KBO 0421.911.297 Actief 7 VE; leftover mined city_lokeren leftover VAPH unused leftover-mined AGB-only leftover type after city GE tick865; official zetel Krekelstraat 17 9160 Lokeren; RSZ2025 87.202; envelope 70/76A JUMP 22024421; 73 JUMP 18573150; 9901 JUMP 1122855; 9904 DROP 1134875; debt JUMP 7843804 (+5024416); cash JUMP 3340047 (+105335); FTE 229,2 JUMP; Identity trap != leftover city GE 0207.463.402 != leftover AGB Lokeren 1031.996.262 != leftover Hagewinde 0861.262.010 != leftover Alderande 0431.893.389 != leftover De Sperwer 0415.344.892 != leftover CAR Waas 0415.472.279 != leftover De Cirkel 0470.413.079 != leftover Ter Engelen 0430.882.809 != leftover Oikonde 0414.341.933; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/CuraCare/OCMW/commercial BV/convent",
}]
append_csv("docs/doge/data/entities.csv", entities)

def bud(bid, amount, basis, notes, empty=False):
    if empty:
        return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}
    a = str(amount)
    return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": a, "amount_min_eur": a, "amount_max_eur": a, "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}

budgets = [
    bud("bud_emiliani_lokeren_70_76a_jr2025_statutory", 22024421, "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +4.40%", "tick2568; PDF native; YE2024 21096366 identical; envelope 70/76A because VZW and omzet70 commercial-only vs large 73; FOI VAPH matrix behind 22024421"),
    bud("bud_emiliani_lokeren_omzet70_jr2025_statutory", 3093895, "NBB VOL-VZW code 70 omzet YE2025 JUMP +4.45%", "tick2568; PDF native; YE2024 2962198 identical; commercial-only vs large 73"),
    bud("bud_emiliani_lokeren_73_jr2025_statutory", 18573150, "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +4.67%", "tick2568; PDF native; YE2024 17745220 identical; 733 subsidies 18564025; 731 schenkingen 9125; VAPH subsidy envelope"),
    bud("bud_emiliani_lokeren_76a_jr2025_statutory", "", "NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "tick2568; PDF native; YE2024 31766 identical; 74 357376 vs 357182", empty=True),
    bud("bud_emiliani_lokeren_personnel62_jr2025_statutory", 17964578, "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +4.72%", "tick2568; PDF native; YE2024 17155250 identical; FTE 9087 229,2 JUMP from 227,4"),
    bud("bud_emiliani_lokeren_630_jr2025_statutory", 443281, "NBB VOL-VZW code 630 afschrijvingen YE2025 DROP -8.52%", "tick2568; PDF native; YE2024 484558 identical"),
    bud("bud_emiliani_lokeren_bedrijfswinst_jr2025_statutory", 1122855, "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +4.54%", "tick2568; PDF native; YE2024 1074054 identical; +48801"),
    bud("bud_emiliani_lokeren_pnl_jr2025_statutory", 1134875, "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -6.41%", "tick2568; PDF native; YE2024 1212652 identical; 9903 1134875 DROP"),
    bud("bud_emiliani_lokeren_equity_jr2025_statutory", 12390807, "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +8.48%", "tick2568; PDF native; YE2024 11421713 identical"),
    bud("bud_emiliani_lokeren_assets_jr2025_statutory", 21349427, "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +39.51%", "tick2568; PDF native; YE2024 15302608 identical; debt 17/49 7843804 JUMP vs 2819388 (+5024416)"),
    bud("bud_emiliani_lokeren_cash_jr2025_statutory", 3340047, "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +3.26%", "tick2568; PDF native; YE2024 3234712 identical; +105335; geldbeleggingen 50/53 5074576 vs 5068596"),
]
append_csv("docs/doge/data/budgets.csv", budgets)

cash_json = json.dumps({"2025": 3340047, "2024": 3234712}, separators=(",", ":"))
commitments = [{
    "commitment_id": comm_id,
    "title": "Emiliani Lokeren YE2025 (70/76A JUMP 22.02m / 73 JUMP 18.57m / debt JUMP 5.02m / Strong PDF)",
    "entity_id": eid,
    "beneficiary": "VAPH + leftover city_lokeren leftover dual",
    "legal_basis": "Emiliani VZW (KBO 0421.911.297; Actief; 7 VE; official zetel Lokeren; RSZ2025 87.202; VAPH Vergunde Zorgaanbieder + RTH)",
    "decision_date": "2026-06-26",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "22024421",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00260230.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_lokeren leftover-mined AGB-only leftover VAPH",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind 70/76A JUMP 22024421 and 73 JUMP 18573150 and why debt JUMP 7843804 (+5024416) while aanbouw JUMP 7220675 capex 5922767 9901 JUMP 1122855 9904 DROP 1134875 cash JUMP 3340047 (+105335) and FTE 229,2 JUMP",
    "source_id": src_pdf,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Lokeren>Emiliani>JR2025_statutory_L5",
    "notes": "tick2568; Strong official native PDF; leftover mined city_lokeren leftover VAPH unused leftover-mined AGB-only leftover type after city GE tick865; 7 VE; prior-year identical; FIRST LOCK leftover city_lokeren leftover VAPH Emiliani; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}]
append_csv("docs/doge/data/commitments.csv", commitments)

leaderboard = [{
    "item_id": lb_id,
    "name": "Emiliani Lokeren 70/76A JUMP 22.02m / 73 JUMP 18.57m / debt JUMP 5.02m (YE2025 leftover city_lokeren leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": hier,
    "annual_cost_eur": "22024421",
    "total_cost_eur": "22024421",
    "tco_notes": "PDF 70/76A 22024421 JUMP; 73 18573150 JUMP; omzet70 3093895 commercial-only; 76A empty; bedrijfswinst JUMP 1122855; pnl DROP 1134875; equity JUMP 12390807; assets JUMP 21349427; debt JUMP 7843804; cash JUMP 3340047; personnel62 JUMP 17964578; leftover city_lokeren leftover VAPH",
    "confidence": "strong",
    "source_id": src_pdf,
    "beneficiaries": "VAPH + leftover city_lokeren leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_lokeren leftover-mined AGB-only leftover VAPH",
    "measured_outcome": "22.02m 70/76A JUMP; 18.57m 73 JUMP; debt JUMP 5.02m; 105k cash JUMP; 229,2 FTE JUMP; leftover city_lokeren leftover VAPH",
    "absurdity_score": "6.15",
    "cost_score": "6.35",
    "difficulty": "4.50",
    "priority_index": "6.00",
    "cut_proposal": "FOI VAPH / gemeente Lokeren matrix behind 70/76A 22024421 and 73 18573150 and why debt JUMP 7843804 (+5024416 vs 2819388) while aanbouw JUMP 7220675 from 1423626 and capex 5922767 (8166 5797049) and 9901 JUMP 1122855 while 9904 DROP 1134875 and cash JUMP 3340047 (+105335) and FTE 229,2 JUMP from 227,4",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2568 leftover mined city_lokeren leftover VAPH Emiliani after city GE tick865 leftover-mined AGB-only leftover VAPH; FIRST LOCK leftover city_lokeren leftover VAPH Emiliani; HARD SKIP leftover city_mechelen leftover VAPH Oikonde remine@2567 leftover Vondels remine@2566 leftover Duinhelm remine@2565 leftover Bethanie SCAN leftover Hagewinde remine leftover Alderande remine leftover De Sperwer remine leftover CAR Waas remine leftover De Cirkel remine leftover Ter Engelen remine; 7 VE; prior-year identical; next rq_2569 leftover dual (NOT every-10; next every-10 2570); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; never mix off-TE dual into 348bn TE pie",
}]
append_csv("docs/doge/data/leaderboard.csv", leaderboard)

foi_rows = [{
    "gap_id": gap_id,
    "hierarchy_path": hier_foi,
    "entity_id": eid,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VOL-VZW YE2025 70/76A JUMP 22024421 vs omzet70 commercial-only 3093895, 73 JUMP 18573150 with debt JUMP 7843804 (+5024416) while aanbouw JUMP 7220675 capex 5922767 9901 JUMP 1122855 9904 DROP 1134875 cash JUMP 3340047 (+105335) and FTE 229,2 JUMP",
    "why_it_matters": "Public leftover VAPH dual of mined city_lokeren leftover-mined AGB-only leftover VAPH shows 22.02m 70/76A envelope while subsidy matrix and 5.02m debt JUMP amid 5.80m aanbouw JUMP and 9904 DROP stay unsourced",
    "priority": "7",
    "recipient_body": "Emiliani VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@emiliani.be",
    "recipient_postal": "Krekelstraat 17, 9160 Lokeren",
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
    "notes": "tick2568; concept NOT verzonden; Strong PDF 2026-00260230; prio7",
}]
append_csv("docs/doge/data/foi_queue.csv", foi_rows)

Path("/tmp/tick2568").mkdir(parents=True, exist_ok=True)
Path("/tmp/tick2568/NOW.txt").write_text(NOW)
Path("/tmp/tick2568/IDS.json").write_text(json.dumps({"eid": eid, "gap_id": gap_id, "comm_id": comm_id, "lb_id": lb_id, "NOW": NOW}))
print("NOW", NOW)
print("appended sources+4 entities+1 budgets+11 commitments+1 leaderboard+1 foi+1")
