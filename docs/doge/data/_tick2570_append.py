#!/usr/bin/env python3
"""tick2570 leftover dual Het Balanske Tielt-Winge — append-only CSVs (EVERY-10 tick)."""
import csv, json, os, sys
from datetime import datetime, timezone
from pathlib import Path

csv.field_size_limit(sys.maxsize)
ROOT = "/workspace/AIpolitics"
os.chdir(ROOT)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = "2026-10-11"
TICK = "2570"

eid = "vzw_het_balanske_tielt_winge"
src_pdf = "src_het_balanske_tielt_winge_jr2025_nbb_pdf_2570"
src_kbo = "src_het_balanske_tielt_winge_kbo_2570"
src_site = "src_het_balanske_tielt_winge_site_2570"
comm_id = "comm_het_balanske_tielt_winge_jr2025_statutory_73_jump_1_61m_debt_jump_2_31m_9901_drop_12k"
lb_id = "lb_het_balanske_tielt_winge_73_jump_1_61m_debt_jump_2_31m_9901_drop_12k_jr2025"
gap_id = "gap_het_balanske_tielt_winge_vaph_matrix_73_jump_1_61m_debt_jump_2_31m_9901_drop_12k_l5"
hier = "Vlaanderen>Vlaams-Brabant>Tielt-Winge>Het Balanske>JR2025"
hier_foi = "Vlaanderen>Vlaams-Brabant>Tielt-Winge>Het Balanske>leftover_vaph"
PDF_URL = "https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/cab0e693-485f-11f1-bade-dd243584f05e"

def append_csv(path, rows):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        fieldnames = next(r)
        ids = {row[0] for row in r if row}
    for row in rows:
        kid = row[fieldnames[0]]
        if kid in ids:
            raise SystemExit(f"ID collision {kid} in {path}")
    with open(path, "rb") as f:
        f.seek(-1, 2)
        if f.read(1) != b"\n":
            raise SystemExit(f"{path} does not end with newline")
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="raise", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})

TRAP = ("Identity trap 0448.595.801 != leftover OCMW Tielt-Winge != leftover Hoito Tienen 0429.766.220 remine@2569 "
        "!= leftover Emiliani 0421.911.297 remine@2568 != leftover Bethanie 0414.744.977 SCAN skip; "
        "Eyckenborgh Gooik 0434.019.372 rejected (WZC / Gravenkasteel inrichtende macht, not VAPH); "
        "Zwart Goor Merksplas rejected (Klavier = Emmaus 0411.515.075 zetel Mechelen leftover-via-VE)")

sources = [
    {"source_id": src_pdf,
     "title": "NBB VKT-VZW jaarrekening 2025 Gezinsactiviteitencentrum Het Balanske deposit 2026-00206974",
     "url": PDF_URL, "publisher": "NBB CBSO official deposit PDF (consult.cbso.nbb.be)",
     "accessed_date": DATE, "source_class": "strong",
     "notes": "tick2570 EVERY-10; official native statutory PDF 51107 B 13p VKT-VZW 25.0.13 m04-f; header 23/06/2026; AV 15-06-2026; YE 01-01-2025..31-12-2025; Producer OpenPDF 1.3.26 CreationDate 2026-06-27 05:45:35 CEST; MD5 c9a5f896cbd4f7cf6d2865fdc1073aa4; NBB published-deposits API YE2025 2026-00206974 (deposit 2026-06-23, XBRL) + YE2024 2025-00191517; CDN staatsbladmonitor GET hung (timeout) -> official NBB broker PDF used instead; prior-year identical; niet dienstig VKT-VZW 6.1.3 6.2 6.5 6.6 7 8; euros from official NBB native PDF text only (not Companyweb/Belscope/Busibee/Firmo)"},
    {"source_id": src_kbo,
     "title": "KBO Gezinsactiviteitencentrum Het Balanske 0448.595.801",
     "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0448595801",
     "publisher": "KBO Public Search FOD Economie", "accessed_date": DATE, "source_class": "strong",
     "notes": "tick2570; Actief Normale toestand since 05.11.1992; VZW; afkorting G.A.C. Het Balanske; official zetel Halensebaan 2 3390 Tielt-Winge since 23.03.2001; 2 VE: 2.158.357.985 Halensebaan 2 Tielt-Winge since 08.01.2007 + 2.383.981.272 Villa 84 Hasseltsestraat 84 3290 Diest since 23.01.2026; RSZ2025 88.106 dagcentra volwassenen mentale handicap incl. ambulante hulpverlening; Werkgever RSZ since 03.11.1997; 9 bestuurders; KBO state 10/10/2026; " + TRAP},
    {"source_id": src_site,
     "title": "Het Balanske official site (dagcentrum Kalebas, Villa84 woonondersteuning, KDV De Bal, UiThuis)",
     "url": "https://www.balanske.be/", "publisher": "Het Balanske VZW", "accessed_date": DATE, "source_class": "org",
     "notes": "tick2570; dagcentrum Kalebas volwassenen + woonondersteuning Villa84 Diest (officieel geopend sept 2026, Warmste Week) + kinderdagverblijf De Bal (inclusief) + thuisopvangdienst UiThuis + vrijetijd/sport; FOI boekhouding@balanske.be from official NBB PDF + info@balanske.be from official algemene voorwaarden page; Nationale Loterij G-sport steun okt 2026 (amount not stated -> not booked)"},
]
append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": eid,
    "name_nl": "Gezinsactiviteitencentrum Het Balanske VZW (dagcentrum volwassenen met beperking + Villa84 woonondersteuning Diest + inclusief KDV)",
    "name_fr": "", "name_en": "", "level": "L5", "parent_id": "city_tielt_winge", "community_language": "nl",
    "website": "https://www.balanske.be/", "foi_email": "boekhouding@balanske.be",
    "foi_postal": "Halensebaan 2, 3390 Tielt-Winge",
    "notes": "tick2570 EVERY-10 YE2025 Strong official native NBB PDF deposit 2026-00206974 (VKT-VZW) + Strong KBO 0448.595.801 Actief 2 VE (Tielt-Winge zetel + Villa84 Diest since 23.01.2026); leftover city_tielt_winge (only OCMW child before) leftover VAPH-type dagcentrum; 73 JUMP 1608109; bruto 9900 JUMP 1273778; 62 JUMP 1146505; 9901 DROP 12273; 9904 DROP 36784; debt JUMP 2308489 (+193%); overige leningen 174/0 1644111; aanbouw 27 1359758; capex 8169 1241939; cash JUMP 1282461; FTE 17,9; " + TRAP + "; NOT Armonea/Korian/Vulpia/OCMW/commercial BV/convent",
}]
append_csv("docs/doge/data/entities.csv", entities)

def bud(bid, amount, basis, notes):
    a = str(amount)
    return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": a, "amount_min_eur": a, "amount_max_eur": a,
            "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": "tick2570; PDF native; " + notes}

P = "bud_het_balanske_tielt_winge_"
budgets = [
    bud(P + "73_jr2025_statutory", 1608109, "NBB VKT-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP +11.41%", "YE2024 1443428 identical; +164681; VKT no 733 split; VAPH/Kind en Gezin subsidy envelope; omzet 70 and 76A empty"),
    bud(P + "bruto9900_jr2025_statutory", 1273778, "NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +14.41%", "YE2024 1113307 identical; 60/61 334331 vs 330120"),
    bud(P + "personnel62_jr2025_statutory", 1146505, "NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +18.10%", "YE2024 970831 identical; FTE 9087 17,9 vs 15,7; 102 personeelskosten 1066450"),
    bud(P + "630_jr2025_statutory", 110947, "NBB VKT-VZW code 630 afschrijvingen YE2025 flat", "YE2024 110865 identical"),
    bud(P + "bedrijfswinst_jr2025_statutory", 12273, "NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -58.68%", "YE2024 29700 identical; -17427"),
    bud(P + "pnl_jr2025_statutory", 36784, "NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -41.11%", "YE2024 62462 identical; 75 fin opbrengsten 31070"),
    bud(P + "equity_jr2025_statutory", 2557203, "NBB VKT-VZW code 10/15 eigen vermogen YE2025 flat +0.40%", "YE2024 2546915 identical; kapitaalsubsidies 15 1018667 vs 1045163"),
    bud(P + "assets_jr2025_statutory", 4865692, "NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +45.92%", "YE2024 3334491 identical; MVA 22/27 3371311 vs 2238733; aanbouw 27 1359758 vs 123824 (Villa84 Diest)"),
    bud(P + "debt_jr2025_statutory", 2308489, "NBB VKT-VZW code 17/49 schulden YE2025 JUMP +193.11%", "YE2024 787577 identical; 17 >1j 1895905 vs 479330; overige leningen 174/0 1644111 vs 190614; 8913 >5j 1507092; lender not disclosed (VKT) -> FOI"),
    bud(P + "cash_jr2025_statutory", 1282461, "NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +28.35%", "YE2024 999176 identical; +283285"),
    bud(P + "capex8169_jr2025_statutory", 1241939, "NBB VKT-VZW code 8169 aanschaffingen MVA YE2025", "8199 aanschaffingswaarde 4558576 vs 3316637; 8279 afschrijving 109361"),
]
append_csv("docs/doge/data/budgets.csv", budgets)

commitments = [{
    "commitment_id": comm_id,
    "title": "Het Balanske Tielt-Winge YE2025 (73 JUMP 1.61m / debt JUMP 2.31m / 9901 DROP 12k / Strong PDF)",
    "entity_id": eid, "beneficiary": "VAPH + Kind en Gezin + leftover city_tielt_winge leftover dual",
    "legal_basis": "Gezinsactiviteitencentrum Het Balanske VZW (KBO 0448.595.801; Actief; 2 VE; zetel Tielt-Winge; RSZ2025 88.106 dagcentra)",
    "decision_date": "2026-06-15", "start_year": "2025", "end_year": "2025",
    "total_envelope_eur": "1608109",
    "cash_by_year": json.dumps({"2025": 1282461, "2024": 999176}, separators=(",", ":")),
    "remaining_eur": "0", "status": "active", "evaluation_url": PDF_URL,
    "stated_goal": "Public leftover VAPH-type dual of mined city_tielt_winge (dagcentrum + new Villa84 woonondersteuning Diest)",
    "cut_option": "Publish VAPH/K&G matrix behind 73 1608109 and lender + subsidy plan behind 174/0 overige leningen 1644111 / aanbouw 1359758 (Villa84) while 9901 DROP 12273",
    "source_id": src_pdf, "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Vlaams-Brabant>Tielt-Winge>Het Balanske>JR2025_statutory_L5",
    "notes": "tick2570 EVERY-10; Strong official native PDF; FIRST LOCK leftover city_tielt_winge leftover VAPH Het Balanske; prior-year identical; not TE-additive",
}]
append_csv("docs/doge/data/commitments.csv", commitments)

leaderboard = [{
    "item_id": lb_id,
    "name": "Het Balanske Tielt-Winge 73 JUMP 1.61m / debt JUMP 2.31m / 9901 DROP 12k (YE2025 leftover city_tielt_winge leftover VAPH)",
    "level": "L5", "type": "vaph_vzw_statutory", "hierarchy_path": hier,
    "annual_cost_eur": "1608109", "total_cost_eur": "1608109",
    "tco_notes": "PDF 73 1608109 JUMP; bruto 9900 1273778 JUMP; 62 1146505 JUMP; 9901 12273 DROP; 9904 36784 DROP; assets 4865692 JUMP; debt 2308489 JUMP +193%; overige leningen 1644111; aanbouw 1359758; capex 1241939; cash 1282461 JUMP",
    "confidence": "strong", "source_id": src_pdf,
    "beneficiaries": "VAPH + Kind en Gezin + leftover city_tielt_winge leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_tielt_winge",
    "measured_outcome": "1.61m 73 JUMP; 2.31m debt JUMP (+1.52m); 1.36m aanbouw; 12k 9901 DROP; 17,9 FTE",
    "absurdity_score": "5.50", "cost_score": "5.60", "difficulty": "4.50", "priority_index": "5.30",
    "cut_proposal": "FOI VAPH / K&G / gemeente Tielt-Winge matrix behind 73 1608109 and lender/terms of 174/0 overige leningen 1644111 financing Villa84 Diest (aanbouw 1359758) while bedrijfswinst DROP to 12273",
    "status": "active", "struck_reason": "",
    "notes": "tick2570 EVERY-10 leftover city_tielt_winge Het Balanske; FIRST LOCK; 2 VE (Villa84 Diest new 2026); prior-year identical; next rq_2571; never mix off-TE dual into 348bn TE pie",
}]
append_csv("docs/doge/data/leaderboard.csv", leaderboard)

foi_rows = [{
    "gap_id": gap_id, "hierarchy_path": hier_foi, "entity_id": eid,
    "what_is_missing": "VAPH/K&G/gemeentelijke matrix behind VKT-VZW YE2025 73 JUMP 1608109; lender, terms and public guarantees behind overige leningen 174/0 1644111 (debt JUMP 2308489 +193%) financing aanbouw 1359758 / Villa84 Diest; why 9901 DROP 12273",
    "why_it_matters": "Leftover VAPH-type dual of mined city_tielt_winge: 1.61m subsidy envelope plus 1.52m new debt for a new woonproject while operating result fell 59%; VKT model hides 733 split and lender",
    "priority": "7", "recipient_body": "Het Balanske VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "boekhouding@balanske.be", "recipient_postal": "Halensebaan 2, 3390 Tielt-Winge",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md", "status": "ready", "date_ready": DATE,
    "date_sent": "", "date_due": "", "date_answered": "", "response_summary": "",
    "linked_commitment_id": comm_id, "linked_leaderboard_id": lb_id, "created_utc": NOW, "updated_utc": NOW,
    "notes": "tick2570; concept NOT verzonden; Strong PDF 2026-00206974; prio7",
}]
append_csv("docs/doge/data/foi_queue.csv", foi_rows)

Path(f"docs/doge/foi/drafts/{gap_id}.md").write_text(f"""# FOI draft — Het Balanske Tielt-Winge (73 JUMP 1.61m / debt JUMP 2.31m / 9901 DROP 12k)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** Gezinsactiviteitencentrum Het Balanske VZW — KBO **0448.595.801** (Actief; VZW; zetel Halensebaan 2, 3390 Tielt-Winge; 2 VE incl. Villa 84, Hasseltsestraat 84, 3290 Diest since 23.01.2026; RSZ2025 88.106 dagcentra volwassenen met mentale handicap)  
**recipient:** Het Balanske VZW / Voorzitter Raad van Bestuur — boekhouding@balanske.be (official NBB PDF) / info@balanske.be — Halensebaan 2, 3390 Tielt-Winge  
**sources:** official NBB VKT-VZW native PDF deposit **2026-00206974** (51107 B / 13p; AV 15-06-2026; neergelegd 23/06/2026; MD5 c9a5f896cbd4f7cf6d2865fdc1073aa4) + KBO + balanske.be

## Onderwerp
Openbaarheid van bestuur — financieringsmatrix en leningen Het Balanske VZW YE2025

## Geachte

Op grond van het decreet van 26 maart 2004 betreffende de openbaarheid van bestuur (en, voor zover van toepassing, de subsidievoorwaarden van de verstrekkende overheden) vraag ik een kopie van / inzage in de volgende documenten en cijfers over **Gezinsactiviteitencentrum Het Balanske VZW** (KBO 0448.595.801):

1. De uitsplitsing per verstrekker (VAPH, Kind en Gezin / Opgroeien, gemeente Tielt-Winge, stad Diest, provincie, Nationale Loterij, giften) van code **73** lidgeld/schenkingen/legaten/subsidies **EUR 1.608.109** in 2025 (2024: **EUR 1.443.428**; +11,41%).
2. De identiteit van de kredietgever(s), looptijd, rente en eventuele overheidswaarborg voor de **overige leningen (174/0) EUR 1.644.111** (2024: **EUR 190.614**); totale schulden **17/49 EUR 2.308.489** (2024: **EUR 787.577**; +193%), waarvan **EUR 1.507.092** met looptijd > 5 jaar.
3. Het investerings- en subsidiedossier (o.a. VIPA of andere infrastructuursubsidie) voor **activa in aanbouw EUR 1.359.758** (2024: **EUR 123.824**) en aanschaffingen MVA **EUR 1.241.939** in 2025 — vermoedelijk wooncentrum Villa84, Hasseltsestraat 84, Diest.
4. Toelichting waarom de **bedrijfswinst (9901) daalde naar EUR 12.273** (2024: **EUR 29.700**) bij personeelskosten **62 EUR 1.146.505** (2024: **EUR 970.831**; FTE 17,9 vs 15,7) en liquide middelen **EUR 1.282.461** (2024: **EUR 999.176**).

Gelieve te antwoorden binnen de wettelijke termijn. Deze brief is een **concept** (status ready) en is **niet verzonden**.

Met vriendelijke groeten  
Kareljan Raes
""", encoding="utf-8")

Path("/tmp/tick2570").mkdir(parents=True, exist_ok=True)
Path("/tmp/tick2570/IDS.json").write_text(json.dumps({"eid": eid, "gap_id": gap_id, "comm_id": comm_id, "lb_id": lb_id, "NOW": NOW}))
print("NOW", NOW, "appended sources+3 entities+1 budgets+11 commitments+1 leaderboard+1 foi+1 + draft")
