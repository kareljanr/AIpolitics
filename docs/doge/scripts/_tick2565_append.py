#!/usr/bin/env python3
"""tick2565 leftover dual Duinhelm Oostende — append-only large CSVs."""
import csv, json, os
from datetime import datetime, timezone
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = "2026-08-29"
TICK = "2565"

eid = "vzw_duinhelm_oostende"
src_pdf = "src_duinhelm_oostende_jr2025_nbb_pdf_2565"
src_kbo = "src_duinhelm_oostende_kbo_2565"
src_vaph = "src_duinhelm_oostende_vaph_2565"
src_site = "src_duinhelm_oostende_site_2565"
comm_id = "comm_duinhelm_oostende_jr2025_statutory_70_76a_jump_12_61m_73_jump_10_58m_9901_jump_887k_cash_drop_154k"
lb_id = "lb_duinhelm_oostende_70_76a_jump_12_61m_73_jump_10_58m_9901_jump_887k_cash_drop_154k_jr2025"
gap_id = "gap_duinhelm_oostende_vaph_matrix_70_76a_jump_12_61m_73_jump_10_58m_9901_jump_887k_cash_drop_154k_l5"
hier = "Vlaanderen>West-Vlaanderen>Oostende>Duinhelm>JR2025"
hier_foi = "Vlaanderen>West-Vlaanderen>Oostende>Duinhelm>leftover_vaph"

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
        "title": "NBB VOL-VZW jaarrekening 2025 Duinhelm deposit 2026-00157589",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00157589.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2565; official native statutory PDF 867669 bytes 59p VOL-VZW 26.0.12 m05-f; header 11/06/2026; AV 20.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-13 01:16:02 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN GET 200 867669 MD5 3f1f6ef973d0438874fc72d91d186fb3; NBB consult HTML stub 5344 B discarded; VOL-VZW 6.1 6.2.1 6.2.2 6.2.4 6.3.4 6.3.6 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.14 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; prior YE2024 deposit 2025-00138184 also deposited for YoY verify",
    },
    {
        "source_id": src_kbo,
        "title": "KBO Duinhelm 0413.223.562",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413223562",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2565; Actief Normale toestand; VZW; official zetel Rietmusstraat 24 8400 Oostende since 27.05.1987; 10 VE mostly Oostende + 1 Gistel leftover-via-VE FROM leftover city_oostende; RSZ2025 87.202 Instellingen met huisvesting voor volwassenen met een mentale handicap; Werkgever RSZ since 01.10.1976; FOI info@duinhelm.be from official NBB PDF; Identity trap 0413.223.562 != leftover city GE Oostende 0207.436.775 != leftover AG-O Oostende 0267.389.606 != leftover Ithaka 0448.387.646 remine@2325",
    },
    {
        "source_id": src_vaph,
        "title": "VAPH adreslijst Duinhelm Vergunde Zorgaanbieder",
        "url": "https://www.vaph.be/organisaties/adressen/duinhelm",
        "publisher": "VAPH",
        "accessed_date": DATE,
        "source_class": "primary",
        "notes": "tick2565; official VAPH adreslijst Duinhelm Vergunde Zorgaanbieder + Rechtstreeks toegankelijke hulp; admin adres Rietmusstraat 24 8400 Oostende; FOI annelore.devidts@duinhelm.be from VAPH + info@duinhelm.be from NBB PDF; leftover mined city_oostende leftover VAPH after city GE tick842; FIRST LOCK leftover city_oostende leftover VAPH Duinhelm",
    },
    {
        "source_id": src_site,
        "title": "Duinhelm official site FOI email",
        "url": "https://www.duinhelm.be/",
        "publisher": "Duinhelm VZW",
        "accessed_date": DATE,
        "source_class": "org",
        "notes": "tick2565; FOI info@duinhelm.be from official NBB PDF internetadres www.duinhelm.be; leftover mined city_oostende leftover VAPH unused leftover type after city GE tick842 (AG-O child exists but Duinhelm itself unused); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover city_overijse leftover VAPH De Berken remine@2564; NOT leftover Ithaka remine@2325; NOT leftover Assjette 0 deposits; NOT leftover Autisme Leeft 0 deposits; NOT leftover Agape Tielt groenezorg",
    },
]
append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": eid,
    "name_nl": "Duinhelm VZW (Oostende / VAPH Vergunde Zorgaanbieder; woonondersteuning volwassenen mentale handicap)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_oostende",
    "community_language": "nl",
    "website": "https://www.duinhelm.be/",
    "foi_email": "info@duinhelm.be",
    "foi_postal": "Rietmusstraat 24, 8400 Oostende",
    "notes": "tick2565 YE2025 Strong official native NBB PDF deposit 2026-00157589 + Strong KBO 0413.223.562 Actief 10 VE; leftover mined city_oostende leftover VAPH unused leftover type after city GE tick842; official zetel Rietmusstraat 24 8400 Oostende; RSZ2025 87.202; envelope 70/76A JUMP 12607017; 73 JUMP 10583537; 9901 JUMP 886627; cash DROP 541306 (-154349); FTE 128,8 JUMP; Identity trap != leftover city GE 0207.436.775 != leftover AG-O 0267.389.606 != leftover Ithaka 0448.387.646; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/CuraCare/OCMW/commercial BV/convent",
}]
append_csv("docs/doge/data/entities.csv", entities)

def bud(bid, amount, basis, notes, empty=False):
    if empty:
        return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}
    a = str(amount)
    return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": a, "amount_min_eur": a, "amount_max_eur": a, "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}

budgets = [
    bud("bud_duinhelm_oostende_70_76a_jr2025_statutory", 12607017, "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +9.19%", "tick2565; PDF native; YE2024 11546208 identical; VOL envelope; FOI VAPH matrix behind 12607017"),
    bud("bud_duinhelm_oostende_omzet70_jr2025_statutory", 1296875, "NBB VOL-VZW code 70 omzet YE2025 JUMP +3.81%", "tick2565; PDF native; YE2024 1249232 identical; commercial-only vs large 73"),
    bud("bud_duinhelm_oostende_73_jr2025_statutory", 10583537, "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +11.28%", "tick2565; PDF native; YE2024 9510384 identical; 733 subsidies 10546090 / 731 36923; VAPH subsidy envelope"),
    bud("bud_duinhelm_oostende_74_jr2025_statutory", 654956, "NBB VOL-VZW code 74 andere bedrijfsopbrengsten YE2025 JUMP", "tick2565; PDF native; YE2024 551284 identical"),
    bud("bud_duinhelm_oostende_personnel62_jr2025_statutory", 9458561, "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP", "tick2565; PDF native; YE2024 8541018 identical; FTE 9087 128,8 JUMP from 122,8"),
    bud("bud_duinhelm_oostende_630_jr2025_statutory", 403934, "NBB VOL-VZW code 630 afschrijvingen YE2025 DROP", "tick2565; PDF native; YE2024 440879 identical"),
    bud("bud_duinhelm_oostende_bedrijfswinst_jr2025_statutory", 886627, "NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +69.28%", "tick2565; PDF native; YE2024 523770 identical; +362857"),
    bud("bud_duinhelm_oostende_pnl_jr2025_statutory", 904762, "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +62.46%", "tick2565; PDF native; YE2024 556930 identical; 9903 919738 JUMP"),
    bud("bud_duinhelm_oostende_equity_jr2025_statutory", 7995963, "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +11.62%", "tick2565; PDF native; YE2024 7163438 identical"),
    bud("bud_duinhelm_oostende_assets_jr2025_statutory", 11997286, "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +7.19%", "tick2565; PDF native; YE2024 11192838 identical; debt 17/49 3423856 flat vs 3419079"),
    bud("bud_duinhelm_oostende_cash_jr2025_statutory", 541306, "NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -22.19%", "tick2565; PDF native; YE2024 695655 identical; -154349; geldbeleggingen 50/53 JUMP 2648693 from 1771133"),
]
append_csv("docs/doge/data/budgets.csv", budgets)

cash_json = json.dumps({"2025": 541306, "2024": 695655}, separators=(",", ":"))
commitments = [{
    "commitment_id": comm_id,
    "title": "Duinhelm Oostende YE2025 (70/76A JUMP 12.61m / 73 JUMP 10.58m / 9901 JUMP 887k / cash DROP 154k / Strong PDF)",
    "entity_id": eid,
    "beneficiary": "VAPH + leftover city_oostende leftover dual",
    "legal_basis": "Duinhelm VZW (KBO 0413.223.562; Actief; 10 VE; official zetel Oostende; RSZ2025 87.202; VAPH Vergunde Zorgaanbieder)",
    "decision_date": "2026-05-20",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "12607017",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00157589.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_oostende",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind 70/76A JUMP 12607017 and 73 JUMP 10583537 and why 9901 JUMP 886627 while cash DROP 541306 (-154k) and FTE 128,8 JUMP",
    "source_id": src_pdf,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Oostende>Duinhelm>JR2025_statutory_L5",
    "notes": "tick2565; Strong official native PDF; leftover mined city_oostende leftover VAPH unused leftover type after city GE tick842; 10 VE; prior-year identical; FIRST LOCK leftover city_oostende leftover VAPH Duinhelm; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}]
append_csv("docs/doge/data/commitments.csv", commitments)

leaderboard = [{
    "item_id": lb_id,
    "name": "Duinhelm Oostende 70/76A JUMP 12.61m / 73 JUMP 10.58m / 9901 JUMP 887k / cash DROP 154k (YE2025 leftover city_oostende leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": hier,
    "annual_cost_eur": "12607017",
    "total_cost_eur": "12607017",
    "tco_notes": "PDF 70/76A 12607017 JUMP; 73 10583537 JUMP; omzet70 1296875 commercial-only; 76A 71649 DROP; bedrijfswinst JUMP 886627; pnl JUMP 904762; equity JUMP 7995963; assets JUMP 11997286; debt 3423856; cash DROP 541306; personnel62 JUMP 9458561; leftover city_oostende leftover VAPH",
    "confidence": "strong",
    "source_id": src_pdf,
    "beneficiaries": "VAPH + leftover city_oostende leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_oostende",
    "measured_outcome": "12.61m 70/76A JUMP; 10.58m 73 JUMP; 9901 JUMP 887k; 154k cash DROP; 128,8 FTE JUMP; leftover city_oostende leftover VAPH",
    "absurdity_score": "5.90",
    "cost_score": "5.85",
    "difficulty": "4.50",
    "priority_index": "5.88",
    "cut_proposal": "FOI VAPH / gemeente Oostende matrix behind 70/76A 12607017 and 73 10583537 and why 9901 JUMP 886627 while cash DROP 541306 (-154349 vs 695655) and FTE 128,8 JUMP from 122,8",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2565 leftover mined city_oostende leftover VAPH Duinhelm after city GE tick842; FIRST LOCK leftover city_oostende leftover VAPH Duinhelm; HARD SKIP leftover city_overijse De Berken remine@2564 leftover Assjette 0 deposits leftover Autisme Leeft 0 deposits leftover Agape Tielt groenezorg leftover Ithaka remine@2325 leftover De Klokke leftover-via-VE; 10 VE; prior-year identical; next rq_2566 leftover dual (NOT every-10; next every-10 2570); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; never mix off-TE dual into 348bn TE pie",
}]
append_csv("docs/doge/data/leaderboard.csv", leaderboard)

foi_rows = [{
    "gap_id": gap_id,
    "hierarchy_path": hier_foi,
    "entity_id": eid,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VOL-VZW YE2025 70/76A JUMP 12607017 vs omzet70 commercial-only 1296875, 73 JUMP 10583537 with 9901 JUMP 886627 while cash DROP 541306 (-154349) and FTE 128,8 JUMP",
    "why_it_matters": "Public leftover VAPH dual of mined city_oostende shows 12.61m 70/76A envelope while subsidy matrix and cash DROP amid operating-profit JUMP stay unsourced",
    "priority": "7",
    "recipient_body": "Duinhelm VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@duinhelm.be",
    "recipient_postal": "Rietmusstraat 24, 8400 Oostende",
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
    "notes": "tick2565; concept NOT verzonden; Strong PDF 2026-00157589; prio7",
}]
append_csv("docs/doge/data/foi_queue.csv", foi_rows)

Path("/tmp/tick2565").mkdir(parents=True, exist_ok=True)
Path("/tmp/tick2565/NOW.txt").write_text(NOW)
Path("/tmp/tick2565/IDS.json").write_text(json.dumps({"eid": eid, "gap_id": gap_id, "comm_id": comm_id, "lb_id": lb_id, "NOW": NOW}))
print("NOW", NOW)
print("appended sources+4 entities+1 budgets+11 commitments+1 leaderboard+1 foi+1")
