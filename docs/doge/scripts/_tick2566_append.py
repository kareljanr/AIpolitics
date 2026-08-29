#!/usr/bin/env python3
"""tick2566 leftover dual Vondels Ieper — append-only large CSVs."""
import csv, json, os
from datetime import datetime, timezone
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = "2026-08-29"
TICK = "2566"

eid = "vzw_vondels_ieper"
src_pdf = "src_vondels_ieper_jr2025_nbb_pdf_2566"
src_kbo = "src_vondels_ieper_kbo_2566"
src_vaph = "src_vondels_ieper_vaph_2566"
src_site = "src_vondels_ieper_site_2566"
comm_id = "comm_vondels_ieper_jr2025_statutory_70_76a_jump_10_49m_73_jump_9_05m_9901_jump_197k_cash_drop_762k"
lb_id = "lb_vondels_ieper_70_76a_jump_10_49m_73_jump_9_05m_9901_jump_197k_cash_drop_762k_jr2025"
gap_id = "gap_vondels_ieper_vaph_matrix_70_76a_jump_10_49m_73_jump_9_05m_9901_jump_197k_cash_drop_762k_l5"
hier = "Vlaanderen>West-Vlaanderen>Ieper>Vondels>JR2025"
hier_foi = "Vlaanderen>West-Vlaanderen>Ieper>Vondels>leftover_vaph"

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
        "title": "NBB VOL-VZW jaarrekening 2025 Vondels deposit 2026-00207010",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00207010.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2566; official native statutory PDF 1054665 bytes 44p VOL-VZW 23.0.10 m05-f; header 23/06/2026; AV 01.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-27 04:15:35 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN GET 200 1054665 MD5 c82eac38daca72931f8d13a7f6a9104c; NBB consult HTML stub 5344 B discarded; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.10 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; leftover city_genk leftover VAPH Bethanie 0414.744.977 SCAN/OCR Xerox AltaLink HARD SKIP this tick",
    },
    {
        "source_id": src_kbo,
        "title": "KBO Vondels 0415.108.728",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0415108728",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2566; Actief Normale toestand; VZW; official zetel Ter Waarde 45 8900 Ieper since 08.12.2014; 9 VE leftover-mined city_ieper + leftover-via-VE FROM leftover city_ieper (Heuvelland/Wervik/Veurne); RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een mentale handicap; Werkgever RSZ since 15.09.1978; FOI info@vondels.be from official NBB PDF; Identity trap 0415.108.728 != leftover city GE Ieper 0207.484.681 != leftover AGB Vauban 0877.643.330 != leftover AGB Musea 0759.387.858 != leftover CAR De Klinker 0430.535.290 remine@2386 != leftover Huize Zonnelied 0415.082.497 remine@2423 != leftover Wintershove 0459.245.312 remine@2422 != leftover Gesticht Zusters 0410.918.031 remine@2461 != leftover Duinhelm 0413.223.562 remine@2565 != leftover Bethanie 0414.744.977 SCAN skip",
    },
    {
        "source_id": src_vaph,
        "title": "VAPH adreslijst Vondels Vergunde Zorgaanbieder",
        "url": "https://www.vaph.be/organisaties/adressen/vondels",
        "publisher": "VAPH",
        "accessed_date": DATE,
        "source_class": "primary",
        "notes": "tick2566; official VAPH adreslijst Vondels Vergunde Zorgaanbieder; admin adres Ter Waarde 45 8900 Ieper; FOI info@vondels.be from official NBB PDF + VAPH; leftover mined city_ieper leftover VAPH after city GE tick851 leftover-mined AGB-only leftover type (AGB Vauban tick1186 + AGB Musea tick1187); FIRST LOCK leftover city_ieper leftover VAPH Vondels",
    },
    {
        "source_id": src_site,
        "title": "Vondels official site FOI email",
        "url": "https://www.vondels.be/",
        "publisher": "Vondels VZW",
        "accessed_date": DATE,
        "source_class": "org",
        "notes": "tick2566; FOI info@vondels.be from official NBB PDF internetadres www.vondels.be; leftover mined city_ieper leftover VAPH unused leftover type after city GE tick851 leftover-mined AGB-only leftover VAPH; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover city_oostende leftover VAPH Duinhelm remine@2565; NOT leftover Bethanie SCAN skip; NOT leftover Muylenberg leftover-via-VE Verbint remine@2401; NOT leftover De Link leftover-via-VE GO; NOT leftover OpWeg YE2024",
    },
]
append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": eid,
    "name_nl": "Vondels VZW (Ieper / VAPH Vergunde Zorgaanbieder; woonondersteuning volwassenen mentale handicap)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_ieper",
    "community_language": "nl",
    "website": "https://www.vondels.be/",
    "foi_email": "info@vondels.be",
    "foi_postal": "Ter Waarde 45, 8900 Ieper",
    "notes": "tick2566 YE2025 Strong official native NBB PDF deposit 2026-00207010 + Strong KBO 0415.108.728 Actief 9 VE; leftover mined city_ieper leftover VAPH unused leftover-mined AGB-only leftover type after city GE tick851; official zetel Ter Waarde 45 8900 Ieper; RSZ2025 87.202; envelope 70/76A JUMP 10485951; 73 JUMP 9049848; 9901 JUMP 451999; cash DROP 921799 (-762307); FTE 104,9 JUMP; Identity trap != leftover city GE 0207.484.681 != leftover AGB Vauban 0877.643.330 != leftover AGB Musea 0759.387.858 != leftover CAR De Klinker 0430.535.290; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/CuraCare/OCMW/commercial BV/convent",
}]
append_csv("docs/doge/data/entities.csv", entities)

def bud(bid, amount, basis, notes, empty=False):
    if empty:
        return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}
    a = str(amount)
    return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": a, "amount_min_eur": a, "amount_max_eur": a, "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}

budgets = [
    bud("bud_vondels_ieper_70_76a_jr2025_statutory", 10485951, "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +9.79%", "tick2566; PDF native; YE2024 9550809 identical; VOL envelope; FOI VAPH matrix behind 10485951"),
    bud("bud_vondels_ieper_omzet70_jr2025_statutory", 754516, "NBB VOL-VZW code 70 omzet YE2025 JUMP +12.26%", "tick2566; PDF native; YE2024 672096 identical; commercial-only vs large 73"),
    bud("bud_vondels_ieper_73_jr2025_statutory", 9049848, "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +10.30%", "tick2566; PDF native; YE2024 8204497 identical; 733 subsidies 9049848 / 731 empty; VAPH subsidy envelope"),
    bud("bud_vondels_ieper_74_jr2025_statutory", 606055, "NBB VOL-VZW code 74 andere bedrijfsopbrengsten YE2025 JUMP", "tick2566; PDF native; YE2024 552620 identical"),
    bud("bud_vondels_ieper_personnel62_jr2025_statutory", 7983439, "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +10.65%", "tick2566; PDF native; YE2024 7214906 identical; FTE 9087 104,9 JUMP from 95,4"),
    bud("bud_vondels_ieper_630_jr2025_statutory", 590453, "NBB VOL-VZW code 630 afschrijvingen YE2025 JUMP", "tick2566; PDF native; YE2024 588086 identical"),
    bud("bud_vondels_ieper_bedrijfswinst_jr2025_statutory", 451999, "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +77.41%", "tick2566; PDF native; YE2024 254774 identical; +197225"),
    bud("bud_vondels_ieper_pnl_jr2025_statutory", 455585, "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +56.79%", "tick2566; PDF native; YE2024 290569 identical; 9903 452241 JUMP"),
    bud("bud_vondels_ieper_equity_jr2025_statutory", 7255341, "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +5.46%", "tick2566; PDF native; YE2024 6879537 identical"),
    bud("bud_vondels_ieper_assets_jr2025_statutory", 10723136, "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +4.08%", "tick2566; PDF native; YE2024 10303059 identical; debt 17/49 3467795 JUMP vs 3422029"),
    bud("bud_vondels_ieper_cash_jr2025_statutory", 921799, "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -45.26%", "tick2566; PDF native; YE2024 1684106 identical; -762307; geldbeleggingen 50/53 JUMP 2000000 from 600000"),
]
append_csv("docs/doge/data/budgets.csv", budgets)

cash_json = json.dumps({"2025": 921799, "2024": 1684106}, separators=(",", ":"))
commitments = [{
    "commitment_id": comm_id,
    "title": "Vondels Ieper YE2025 (70/76A JUMP 10.49m / 73 JUMP 9.05m / 9901 JUMP 197k / cash DROP 762k / Strong PDF)",
    "entity_id": eid,
    "beneficiary": "VAPH + leftover city_ieper leftover dual",
    "legal_basis": "Vondels VZW (KBO 0415.108.728; Actief; 9 VE; official zetel Ieper; RSZ2025 87.202; VAPH Vergunde Zorgaanbieder)",
    "decision_date": "2026-06-01",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "10485951",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00207010.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_ieper leftover-mined AGB-only leftover VAPH",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind 70/76A JUMP 10485951 and 73 JUMP 9049848 and why 9901 JUMP 451999 while cash DROP 921799 (-762k) and FTE 104,9 JUMP",
    "source_id": src_pdf,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Ieper>Vondels>JR2025_statutory_L5",
    "notes": "tick2566; Strong official native PDF; leftover mined city_ieper leftover VAPH unused leftover-mined AGB-only leftover type after city GE tick851; 9 VE; prior-year identical; FIRST LOCK leftover city_ieper leftover VAPH Vondels; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}]
append_csv("docs/doge/data/commitments.csv", commitments)

leaderboard = [{
    "item_id": lb_id,
    "name": "Vondels Ieper 70/76A JUMP 10.49m / 73 JUMP 9.05m / 9901 JUMP 197k / cash DROP 762k (YE2025 leftover city_ieper leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": hier,
    "annual_cost_eur": "10485951",
    "total_cost_eur": "10485951",
    "tco_notes": "PDF 70/76A 10485951 JUMP; 73 9049848 JUMP; omzet70 754516 commercial-only; 76A 75533 DROP; bedrijfswinst JUMP 451999; pnl JUMP 455585; equity JUMP 7255341; assets JUMP 10723136; debt 3467795; cash DROP 921799; personnel62 JUMP 7983439; leftover city_ieper leftover VAPH",
    "confidence": "strong",
    "source_id": src_pdf,
    "beneficiaries": "VAPH + leftover city_ieper leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_ieper leftover-mined AGB-only leftover VAPH",
    "measured_outcome": "10.49m 70/76A JUMP; 9.05m 73 JUMP; 9901 JUMP 197k; 762k cash DROP; 104,9 FTE JUMP; leftover city_ieper leftover VAPH",
    "absurdity_score": "5.82",
    "cost_score": "5.78",
    "difficulty": "4.50",
    "priority_index": "5.80",
    "cut_proposal": "FOI VAPH / gemeente Ieper matrix behind 70/76A 10485951 and 73 9049848 and why 9901 JUMP 451999 while cash DROP 921799 (-762307 vs 1684106) and FTE 104,9 JUMP from 95,4",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2566 leftover mined city_ieper leftover VAPH Vondels after city GE tick851 leftover-mined AGB-only leftover VAPH; FIRST LOCK leftover city_ieper leftover VAPH Vondels; HARD SKIP leftover city_oostende Duinhelm remine@2565 leftover Bethanie SCAN leftover Muylenberg leftover-via-VE Verbint remine@2401 leftover De Link leftover-via-VE leftover OpWeg YE2024 leftover De Bezaan leftover-via-VE Ithaka leftover De Klokke leftover-via-VE; 9 VE; prior-year identical; next rq_2567 leftover dual (NOT every-10; next every-10 2570); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; never mix off-TE dual into 348bn TE pie",
}]
append_csv("docs/doge/data/leaderboard.csv", leaderboard)

foi_rows = [{
    "gap_id": gap_id,
    "hierarchy_path": hier_foi,
    "entity_id": eid,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VOL-VZW YE2025 70/76A JUMP 10485951 vs omzet70 commercial-only 754516, 73 JUMP 9049848 with 9901 JUMP 451999 while cash DROP 921799 (-762307) and FTE 104,9 JUMP",
    "why_it_matters": "Public leftover VAPH dual of mined city_ieper leftover-mined AGB-only leftover VAPH shows 10.49m 70/76A envelope while subsidy matrix and cash DROP amid operating-profit JUMP stay unsourced",
    "priority": "7",
    "recipient_body": "Vondels VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@vondels.be",
    "recipient_postal": "Ter Waarde 45, 8900 Ieper",
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
    "notes": "tick2566; concept NOT verzonden; Strong PDF 2026-00207010; prio7",
}]
append_csv("docs/doge/data/foi_queue.csv", foi_rows)

Path("/tmp/tick2566").mkdir(parents=True, exist_ok=True)
Path("/tmp/tick2566/NOW.txt").write_text(NOW)
Path("/tmp/tick2566/IDS.json").write_text(json.dumps({"eid": eid, "gap_id": gap_id, "comm_id": comm_id, "lb_id": lb_id, "NOW": NOW}))
print("NOW", NOW)
print("appended sources+4 entities+1 budgets+11 commitments+1 leaderboard+1 foi+1")
