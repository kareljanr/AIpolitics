#!/usr/bin/env python3
"""tick2567 leftover dual Oikonde Mechelen — append-only large CSVs."""
import csv, json, os
from datetime import datetime, timezone
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = "2026-08-29"
TICK = "2567"

eid = "vzw_oikonde_mechelen"
src_pdf = "src_oikonde_mechelen_jr2025_nbb_pdf_2567"
src_kbo = "src_oikonde_mechelen_kbo_2567"
src_vaph = "src_oikonde_mechelen_vaph_2567"
src_site = "src_oikonde_mechelen_site_2567"
comm_id = "comm_oikonde_mechelen_jr2025_statutory_bruto_jump_2_84m_73_jump_2_93m_9901_jump_62k_cash_jump_131k"
lb_id = "lb_oikonde_mechelen_bruto_jump_2_84m_73_jump_2_93m_9901_jump_62k_cash_jump_131k_jr2025"
gap_id = "gap_oikonde_mechelen_vaph_matrix_bruto_jump_2_84m_73_jump_2_93m_9901_jump_62k_cash_jump_131k_l5"
hier = "Vlaanderen>Antwerpen>Mechelen>Oikonde>JR2025"
hier_foi = "Vlaanderen>Antwerpen>Mechelen>Oikonde>leftover_vaph"

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
        "title": "NBB VKT-VZW jaarrekening 2025 Oikonde deposit 2026-00134362",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00134362.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2567; official native statutory PDF 55019 bytes 16p VKT-VZW 26.0.11 m04-f; header 03/06/2026; AV 26.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-03 10:53:27 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN GET 200 55019 MD5 0a132501c77691057c48fb022d854d57; NBB consult HTML stub 5344 B discarded; VKT-VZW 6.5 6.6 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; leftover city_genk leftover VAPH Bethanie 0414.744.977 SCAN/OCR Xerox AltaLink HARD SKIP this tick",
    },
    {
        "source_id": src_kbo,
        "title": "KBO Oikonde 0414.341.933",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414341933",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2567; Actief Normale toestand; VZW; official zetel Colomastraat 36-38 2800 Mechelen since 13.09.1996; 1 VE leftover-mined city_mechelen 2.200.731.149 oikonde mechelen vzw Colomastraat 36-38 since 26.07.2011; RSZ2025 88.999 Andere vormen van maatschappelijke dienstverlening zonder huisvesting n.e.g.; Werkgever RSZ since 01.01.1978; FOI info@oikonde.org from official KBO VE + VAPH; Identity trap 0414.341.933 != leftover city GE Mechelen 0207.499.430 != leftover AGB Energiepunt 0843.922.170 != leftover AGB SAM 0871.106.718 != leftover AGB MAC 0546.688.337 != leftover Pardoes 0417.400.205 remine@2473 != leftover Vondels 0415.108.728 remine@2566 != leftover Duinhelm 0413.223.562 remine@2565 != leftover Bethanie 0414.744.977 SCAN skip",
    },
    {
        "source_id": src_vaph,
        "title": "VAPH adreslijst Oikonde Vergunde Zorgaanbieder + RTH",
        "url": "https://www.vaph.be/organisaties/adressen/oikonde",
        "publisher": "VAPH",
        "accessed_date": DATE,
        "source_class": "primary",
        "notes": "tick2567; official VAPH adreslijst Oikonde Vergunde Zorgaanbieder + Rechtstreeks toegankelijke hulp; admin adres Colomastraat 36 2800 Mechelen; FOI info@oikonde.org from official VAPH; leftover mined city_mechelen leftover VAPH after city GE tick829 leftover-mined AGB-only leftover type (AGB Energiepunt tick1162 + AGB SAM tick1173 + AGB MAC tick1270); FIRST LOCK leftover city_mechelen leftover VAPH Oikonde",
    },
    {
        "source_id": src_site,
        "title": "Oikonde official site FOI email",
        "url": "https://www.oikonde.org/",
        "publisher": "Oikonde VZW",
        "accessed_date": DATE,
        "source_class": "org",
        "notes": "tick2567; FOI info@oikonde.org from official VAPH + official KBO VE; leftover mined city_mechelen leftover VAPH unused leftover type after city GE tick829 leftover-mined AGB-only leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover city_ieper leftover VAPH Vondels remine@2566; NOT leftover Bethanie SCAN skip; NOT leftover Stijn leftover-via-VE Hasselt; NOT leftover De Lovie remine@2089",
    },
]
append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": eid,
    "name_nl": "Oikonde VZW (Mechelen / VAPH Vergunde Zorgaanbieder + RTH; mobiele ambulante ondersteuning volwassenen)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_mechelen",
    "community_language": "nl",
    "website": "https://www.oikonde.org/",
    "foi_email": "info@oikonde.org",
    "foi_postal": "Colomastraat 36-38, 2800 Mechelen",
    "notes": "tick2567 YE2025 Strong official native NBB PDF deposit 2026-00134362 + Strong KBO 0414.341.933 Actief 1 VE; leftover mined city_mechelen leftover VAPH unused leftover-mined AGB-only leftover type after city GE tick829; official zetel Colomastraat 36-38 2800 Mechelen; RSZ2025 88.999; envelope bruto9900 JUMP 2839493; 73 JUMP 2931036; 9901 JUMP 61595; cash JUMP 580801 (+131019); FTE 32,4 JUMP; Identity trap != leftover city GE 0207.499.430 != leftover AGB Energiepunt 0843.922.170 != leftover AGB SAM 0871.106.718 != leftover AGB MAC 0546.688.337 != leftover Pardoes 0417.400.205; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/CuraCare/OCMW/commercial BV/convent",
}]
append_csv("docs/doge/data/entities.csv", entities)

def bud(bid, amount, basis, notes, empty=False):
    if empty:
        return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}
    a = str(amount)
    return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": a, "amount_min_eur": a, "amount_max_eur": a, "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}

budgets = [
    bud("bud_oikonde_mechelen_bruto9900_jr2025_statutory", 2839493, "NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +9.53%", "tick2567; PDF native; YE2024 2592486 identical; VKT envelope because 73 is the subsidy envelope and bruto >> omzet; FOI VAPH matrix behind 2839493"),
    bud("bud_oikonde_mechelen_omzet70_jr2025_statutory", 17651, "NBB VKT-VZW code 70 omzet YE2025 JUMP +42.93%", "tick2567; PDF native; YE2024 12349 identical; commercial-only vs large 73"),
    bud("bud_oikonde_mechelen_73_jr2025_statutory", 2931036, "NBB VKT-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +9.32%", "tick2567; PDF native; YE2024 2681181 identical; VAPH subsidy envelope"),
    bud("bud_oikonde_mechelen_76a_jr2025_statutory", "", "NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 empty", "tick2567; PDF native; YE2024 empty identical; 74 not on VKT form", empty=True),
    bud("bud_oikonde_mechelen_personnel62_jr2025_statutory", 2696720, "NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +8.46%", "tick2567; PDF native; YE2024 2486379 identical; FTE 9087 32,4 JUMP from 31,5"),
    bud("bud_oikonde_mechelen_630_jr2025_statutory", 59417, "NBB VKT-VZW code 630 afschrijvingen YE2025 JUMP", "tick2567; PDF native; YE2024 58170 identical"),
    bud("bud_oikonde_mechelen_bedrijfswinst_jr2025_statutory", 61595, "NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +114.53%", "tick2567; PDF native; YE2024 28712 identical; +32883"),
    bud("bud_oikonde_mechelen_pnl_jr2025_statutory", 64061, "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +150.89%", "tick2567; PDF native; YE2024 25534 identical; 9903 64061 JUMP"),
    bud("bud_oikonde_mechelen_equity_jr2025_statutory", 1080752, "NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.74%", "tick2567; PDF native; YE2024 1022120 identical"),
    bud("bud_oikonde_mechelen_assets_jr2025_statutory", 1816621, "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +6.25%", "tick2567; PDF native; YE2024 1709771 identical; debt 17/49 735869 JUMP vs 687651"),
    bud("bud_oikonde_mechelen_cash_jr2025_statutory", 580801, "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +29.13%", "tick2567; PDF native; YE2024 449782 identical; +131019; geldbeleggingen 50/53 empty DROP from 250000"),
]
append_csv("docs/doge/data/budgets.csv", budgets)

cash_json = json.dumps({"2025": 580801, "2024": 449782}, separators=(",", ":"))
commitments = [{
    "commitment_id": comm_id,
    "title": "Oikonde Mechelen YE2025 (bruto JUMP 2.84m / 73 JUMP 2.93m / 9901 JUMP 62k / cash JUMP 131k / Strong PDF)",
    "entity_id": eid,
    "beneficiary": "VAPH + leftover city_mechelen leftover dual",
    "legal_basis": "Oikonde VZW (KBO 0414.341.933; Actief; 1 VE; official zetel Mechelen; RSZ2025 88.999; VAPH Vergunde Zorgaanbieder + RTH)",
    "decision_date": "2026-05-26",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "2839493",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00134362.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_mechelen leftover-mined AGB-only leftover VAPH",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind bruto9900 JUMP 2839493 and 73 JUMP 2931036 and why 9901 JUMP 61595 while cash JUMP 580801 (+131019) and FTE 32,4 JUMP and capex 371907 aanbouw JUMP 473087",
    "source_id": src_pdf,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Mechelen>Oikonde>JR2025_statutory_L5",
    "notes": "tick2567; Strong official native PDF; leftover mined city_mechelen leftover VAPH unused leftover-mined AGB-only leftover type after city GE tick829; 1 VE; prior-year identical; FIRST LOCK leftover city_mechelen leftover VAPH Oikonde; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}]
append_csv("docs/doge/data/commitments.csv", commitments)

leaderboard = [{
    "item_id": lb_id,
    "name": "Oikonde Mechelen bruto JUMP 2.84m / 73 JUMP 2.93m / 9901 JUMP 62k / cash JUMP 131k (YE2025 leftover city_mechelen leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": hier,
    "annual_cost_eur": "2839493",
    "total_cost_eur": "2839493",
    "tco_notes": "PDF bruto9900 2839493 JUMP; 73 2931036 JUMP; omzet70 17651 commercial-only; 76A empty; bedrijfswinst JUMP 61595; pnl JUMP 64061; equity JUMP 1080752; assets JUMP 1816621; debt 735869; cash JUMP 580801; personnel62 JUMP 2696720; leftover city_mechelen leftover VAPH",
    "confidence": "strong",
    "source_id": src_pdf,
    "beneficiaries": "VAPH + leftover city_mechelen leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_mechelen leftover-mined AGB-only leftover VAPH",
    "measured_outcome": "2.84m bruto JUMP; 2.93m 73 JUMP; 9901 JUMP 62k; 131k cash JUMP; 32,4 FTE JUMP; leftover city_mechelen leftover VAPH",
    "absurdity_score": "5.52",
    "cost_score": "5.48",
    "difficulty": "4.50",
    "priority_index": "5.50",
    "cut_proposal": "FOI VAPH / gemeente Mechelen matrix behind bruto9900 2839493 and 73 2931036 and why 9901 JUMP 61595 while cash JUMP 580801 (+131019 vs 449782) and FTE 32,4 JUMP from 31,5 and capex 371907 aanbouw JUMP 473087 from 136056",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2567 leftover mined city_mechelen leftover VAPH Oikonde after city GE tick829 leftover-mined AGB-only leftover VAPH; FIRST LOCK leftover city_mechelen leftover VAPH Oikonde; HARD SKIP leftover city_ieper Vondels remine@2566 leftover Duinhelm remine@2565 leftover Bethanie SCAN leftover Stijn leftover-via-VE leftover De Lovie remine leftover De Lier remine leftover Pelikaan OCMW leftover Zorghoeve groenezorg; 1 VE; prior-year identical; next rq_2568 leftover dual (NOT every-10; next every-10 2570); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; never mix off-TE dual into 348bn TE pie",
}]
append_csv("docs/doge/data/leaderboard.csv", leaderboard)

foi_rows = [{
    "gap_id": gap_id,
    "hierarchy_path": hier_foi,
    "entity_id": eid,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VKT-VZW YE2025 bruto9900 JUMP 2839493 vs omzet70 commercial-only 17651, 73 JUMP 2931036 with 9901 JUMP 61595 while cash JUMP 580801 (+131019) and FTE 32,4 JUMP and capex 371907 aanbouw JUMP 473087",
    "why_it_matters": "Public leftover VAPH dual of mined city_mechelen leftover-mined AGB-only leftover VAPH shows 2.84m bruto envelope while subsidy matrix and cash JUMP amid operating-profit JUMP and capex 372k stay unsourced",
    "priority": "7",
    "recipient_body": "Oikonde VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@oikonde.org",
    "recipient_postal": "Colomastraat 36-38, 2800 Mechelen",
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
    "notes": "tick2567; concept NOT verzonden; Strong PDF 2026-00134362; prio7",
}]
append_csv("docs/doge/data/foi_queue.csv", foi_rows)

Path("/tmp/tick2567").mkdir(parents=True, exist_ok=True)
Path("/tmp/tick2567/NOW.txt").write_text(NOW)
Path("/tmp/tick2567/IDS.json").write_text(json.dumps({"eid": eid, "gap_id": gap_id, "comm_id": comm_id, "lb_id": lb_id, "NOW": NOW}))
print("NOW", NOW)
print("appended sources+4 entities+1 budgets+11 commitments+1 leaderboard+1 foi+1")
