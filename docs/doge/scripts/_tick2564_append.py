#!/usr/bin/env python3
"""tick2564 leftover dual De Berken Overijse — append-only large CSVs."""
import csv, json, os
from datetime import datetime, timezone

csv.field_size_limit(10_000_000)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = "2026-08-29"
TICK = "2564"

eid = "vzw_de_berken_overijse"
src_pdf = "src_de_berken_overijse_jr2025_nbb_pdf_2564"
src_kbo = "src_de_berken_overijse_kbo_2564"
src_vaph = "src_de_berken_overijse_vaph_2564"
src_site = "src_de_berken_overijse_site_2564"
comm_id = "comm_de_berken_overijse_jr2025_statutory_bruto_drop_1_12m_73_drop_1_01m_9901_flip_loss_75k_cash_jump_217k"
lb_id = "lb_de_berken_overijse_bruto_drop_1_12m_73_drop_1_01m_9901_flip_loss_75k_cash_jump_217k_jr2025"
gap_id = "gap_de_berken_overijse_vaph_matrix_bruto_drop_1_12m_73_drop_1_01m_9901_flip_loss_75k_cash_jump_217k_l5"
hier = "Vlaanderen>Vlaams-Brabant>Overijse>De Berken>JR2025"
hier_foi = "Vlaanderen>Vlaams-Brabant>Overijse>De Berken>leftover_vaph"

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
        "title": "NBB VKT-VZW jaarrekening 2025 De Berken deposit 2026-00213938",
        "url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00213938.pdf",
        "publisher": "NBB official WVV deposit PDF via CDN",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2564; official native statutory PDF 50434 bytes 14p VKT-VZW 26.0.15 m04-f; header 29/06/2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-29 20:13:44 UTC OpenPDF 1.3.26; statutory pages native; prior-year identical not restated; CDN GET 200 50434 MD5 3f49303ce08b6a68847d2f5d9ec2d4a6; NBB consult HTML stub 5344 B discarded; VKT-VZW 6.1.1 6.1.2 6.2 6.3 6.5 6.6 7 8 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee not Northdata; prior YE2024 deposit 2025-00292601 also deposited for YoY verify",
    },
    {
        "source_id": src_kbo,
        "title": "KBO De Berken 0425.840.688",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0425840688",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2564; Actief Normale toestand; VZW; official zetel Schavei 70 3090 Overijse since 25.08.1983; 1 VE 2.150.826.431 De Berken Schavei 70 3090 Overijse since 03.01.2006; RSZ2025 88.106 Activiteiten van dagcentra voor volwassenen met een mentale handicap, met inbegrip van ambulante hulpverlening; Werkgever RSZ since 28.09.1983; FOI directie@deberken.be from official VAPH; Identity trap 0425.840.688 != leftover city GE Overijse 0207.512.001 != leftover OCMW Overijse 0212.207.393",
    },
    {
        "source_id": src_vaph,
        "title": "VAPH adreslijst De Berken Vergunde Zorgaanbieder",
        "url": "https://www.vaph.be/organisaties/adressen/de-berken-0",
        "publisher": "VAPH",
        "accessed_date": DATE,
        "source_class": "primary",
        "notes": "tick2564; official VAPH adreslijst De Berken Vergunde Zorgaanbieder; admin adres Schavei 70 3090 Overijse; FOI directie@deberken.be; leftover mined city_overijse leftover VAPH after city GE tick1068; FIRST LOCK leftover city_overijse leftover VAPH De Berken",
    },
    {
        "source_id": src_site,
        "title": "De Berken official site FOI email",
        "url": "https://deberken.be/",
        "publisher": "De Berken VZW",
        "accessed_date": DATE,
        "source_class": "org",
        "notes": "tick2564; FOI directie@deberken.be from official VAPH adreslijst; leftover mined city_overijse leftover VAPH unused leftover type after city GE tick1068 (no AGB child); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover city_staden leftover VAPH Kerckstede remine@2563; NOT leftover De Lommerte Laakdal groenezorg",
    },
]
append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": eid,
    "name_nl": "De Berken VZW (Overijse / VAPH Vergunde Zorgaanbieder; dagcentrum volwassenen mentale handicap)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_overijse",
    "community_language": "nl",
    "website": "https://deberken.be/",
    "foi_email": "directie@deberken.be",
    "foi_postal": "Schavei 70, 3090 Overijse",
    "notes": "tick2564 YE2025 Strong official native NBB PDF deposit 2026-00213938 + Strong KBO 0425.840.688 Actief 1 VE; leftover mined city_overijse leftover VAPH unused leftover type after city GE tick1068 (no AGB child); official zetel Schavei 70 3090 Overijse; RSZ2025 88.106; bruto9900 DROP 1115742; 73 DROP 1010312; 9901 FLIP LOSS -74568; cash JUMP 684185 (+216864); FTE 13,5 DROP; Identity trap != leftover city GE 0207.512.001 != leftover OCMW 0212.207.393; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/CuraCare/OCMW/commercial BV/convent",
}]
append_csv("docs/doge/data/entities.csv", entities)

def bud(bid, amount, basis, notes, empty=False):
    if empty:
        return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": "", "amount_min_eur": "", "amount_max_eur": "", "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}
    a = str(amount)
    return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": a, "amount_min_eur": a, "amount_max_eur": a, "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}

budgets = [
    bud("bud_de_berken_overijse_bruto9900_jr2025_statutory", 1115742, "NBB VKT-VZW code 9900 brutomarge YE2025 DROP -8.20%", "tick2564; PDF native; YE2024 1215402 identical; VKT envelope because 73 is the subsidy envelope and bruto >> omzet70; FOI VAPH matrix behind 1115742"),
    bud("bud_de_berken_overijse_omzet70_jr2025_statutory", 158625, "NBB VKT-VZW code 70 omzet YE2025 DROP -3.42%", "tick2564; PDF native; YE2024 164235 identical; commercial-only vs large 73"),
    bud("bud_de_berken_overijse_73_jr2025_statutory", 1010312, "NBB VKT-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 DROP -8.13%", "tick2564; PDF native; YE2024 1099776 identical; VAPH subsidy envelope"),
    bud("bud_de_berken_overijse_74_jr2025_statutory", None, "NBB VKT-VZW code 74 not on VKT form", "tick2564; 74 not on VKT form (niet dienstig pattern); YE2024 n/a", empty=True),
    bud("bud_de_berken_overijse_personnel62_jr2025_statutory", 1059410, "NBB VKT-VZW code 62 bezoldigingen YE2025 DROP -0.92%", "tick2564; PDF native; YE2024 1069276 identical; FTE 9087 13,5 DROP from 13,8"),
    bud("bud_de_berken_overijse_630_jr2025_statutory", 68916, "NBB VKT-VZW code 630 afschrijvingen YE2025 JUMP +7.45%", "tick2564; PDF native; YE2024 64135 identical"),
    bud("bud_de_berken_overijse_bedrijfswinst_jr2025_statutory", -74568, "NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP LOSS", "tick2564; PDF native; YE2024 +32675 identical; FLIP from profit to loss -74568"),
    bud("bud_de_berken_overijse_pnl_jr2025_statutory", -28725, "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP LOSS", "tick2564; PDF native; YE2024 +79693 identical; 9903 also -28725 FLIP LOSS"),
    bud("bud_de_berken_overijse_equity_jr2025_statutory", 1957246, "NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -2.81%", "tick2564; PDF native; YE2024 2013814 identical"),
    bud("bud_de_berken_overijse_assets_jr2025_statutory", 2077732, "NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -2.83%", "tick2564; PDF native; YE2024 2138256 identical; debt 17/49 120486 DROP from 124442"),
    bud("bud_de_berken_overijse_cash_jr2025_statutory", 684185, "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +46.41%", "tick2564; PDF native; YE2024 467321 identical; +216864; geldbeleggingen 50/53 DROP 1000000 from 1257372"),
]
append_csv("docs/doge/data/budgets.csv", budgets)

cash_json = json.dumps({"2025": 684185, "2024": 467321}, separators=(",", ":"))
commitments = [{
    "commitment_id": comm_id,
    "title": "De Berken Overijse YE2025 (bruto9900 DROP 1.12m / 73 DROP 1.01m / 9901 FLIP LOSS 75k / cash JUMP 217k / Strong PDF)",
    "entity_id": eid,
    "beneficiary": "VAPH + leftover city_overijse leftover dual",
    "legal_basis": "De Berken VZW (KBO 0425.840.688; Actief; 1 VE; official zetel Overijse; RSZ2025 88.106; VAPH Vergunde Zorgaanbieder)",
    "decision_date": "2026-06-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1115742",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "http://cdn.staatsbladmonitor.be/2026pdf/2026-00213938.pdf",
    "stated_goal": "Public leftover VAPH dual of mined city_overijse",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind bruto9900 DROP 1115742 and 73 DROP 1010312 and why 9901 FLIP LOSS -74568 while cash JUMP 684185 (+217k) and FTE 13,5 DROP",
    "source_id": src_pdf,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Overijse>De Berken>JR2025_statutory_L5",
    "notes": "tick2564; Strong official native PDF; leftover mined city_overijse leftover VAPH unused leftover type after city GE tick1068; 1 VE; prior-year identical; FIRST LOCK leftover city_overijse leftover VAPH De Berken; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}]
append_csv("docs/doge/data/commitments.csv", commitments)

leaderboard = [{
    "item_id": lb_id,
    "name": "De Berken Overijse bruto9900 DROP 1.12m / 73 DROP 1.01m / 9901 FLIP LOSS 75k / cash JUMP 217k (YE2025 leftover city_overijse leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": hier,
    "annual_cost_eur": "1115742",
    "total_cost_eur": "1115742",
    "tco_notes": "PDF bruto9900 1115742 DROP; 73 1010312 DROP; omzet70 158625 commercial-only; 76A empty; bedrijfswinst FLIP LOSS -74568; pnl FLIP LOSS -28725; equity DROP 1957246; assets DROP 2077732; debt DROP 120486; cash JUMP 684185; personnel62 DROP 1059410; leftover city_overijse leftover VAPH",
    "confidence": "strong",
    "source_id": src_pdf,
    "beneficiaries": "VAPH + leftover city_overijse leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_overijse",
    "measured_outcome": "1.12m bruto9900 DROP; 1.01m 73 DROP; 9901 FLIP LOSS 75k; 217k cash JUMP; 13,5 FTE DROP; leftover city_overijse leftover VAPH",
    "absurdity_score": "5.40",
    "cost_score": "5.25",
    "difficulty": "4.40",
    "priority_index": "5.35",
    "cut_proposal": "FOI VAPH / gemeente Overijse matrix behind bruto9900 1115742 and 73 1010312 and why 9901 FLIP LOSS -74568 while cash JUMP 684185 (+216864 vs 467321) and FTE 13,5 DROP from 13,8",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2564 leftover mined city_overijse leftover VAPH De Berken after city GE tick1068; FIRST LOCK leftover city_overijse leftover VAPH De Berken; HARD SKIP leftover city_staden Kerckstede remine@2563 leftover city_jabbeke Licht en Liefde Heem remine@2562 leftover city_leopoldsburg Berkenhof remine@2561 leftover De Lommerte Laakdal groenezorg; 1 VE; prior-year identical; next rq_2565 leftover dual (NOT every-10; next every-10 2570); NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; never mix off-TE dual into 348bn TE pie",
}]
append_csv("docs/doge/data/leaderboard.csv", leaderboard)

foi_rows = [{
    "gap_id": gap_id,
    "hierarchy_path": hier_foi,
    "entity_id": eid,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VKT-VZW YE2025 bruto9900 DROP 1115742 vs omzet70 commercial-only 158625, 73 DROP 1010312 with 9901 FLIP LOSS -74568 while cash JUMP 684185 (+216864) and FTE 13,5 DROP",
    "why_it_matters": "Public leftover VAPH dual of mined city_overijse shows 1.12m bruto9900 envelope while subsidy matrix and FLIP to operating loss with simultaneous cash JUMP stay unsourced",
    "priority": "7",
    "recipient_body": "De Berken VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "directie@deberken.be",
    "recipient_postal": "Schavei 70, 3090 Overijse",
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
    "notes": "tick2564; concept NOT verzonden; Strong PDF 2026-00213938; prio7",
}]
append_csv("docs/doge/data/foi_queue.csv", foi_rows)

# persist NOW for rq script
Path = __import__("pathlib").Path
Path("/tmp/tick2564/NOW.txt").write_text(NOW)
Path("/tmp/tick2564/IDS.json").write_text(json.dumps({"eid": eid, "gap_id": gap_id, "comm_id": comm_id, "lb_id": lb_id, "NOW": NOW}))
print("NOW", NOW)
print("appended sources+4 entities+1 budgets+11 commitments+1 leaderboard+1 foi+1")
