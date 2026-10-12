#!/usr/bin/env python3
"""tick2575 leftover dual Mekanders Turnhout YE2025 — append-only large CSVs."""
import csv, json, os
from datetime import datetime, timezone
from pathlib import Path

csv.field_size_limit(10_000_000)
ROOT = Path(__file__).resolve().parents[3]
os.chdir(ROOT)
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DATE = "2026-10-12"
TICK = "2575"

eid = "vzw_mekanders_turnhout"
src_pdf = "src_mekanders_turnhout_jr2025_nbb_pdf_2575"
src_kbo = "src_mekanders_turnhout_kbo_2575"
src_vaph = "src_mekanders_turnhout_vaph_2575"
src_site = "src_mekanders_turnhout_site_2575"
comm_id = "comm_mekanders_turnhout_jr2025_statutory_70_76a_13_90m_733_11_46m_cash_jump_6_14m"
lb_id = "lb_mekanders_turnhout_70_76a_13_90m_733_11_46m_cash_jump_6_14m_jr2025"
gap_id = "gap_mekanders_turnhout_vaph_matrix_70_76a_13_90m_733_11_46m_cash_jump_6_14m_l5"
hier = "Vlaanderen>Antwerpen>Turnhout>Mekanders>JR2025"
hier_foi = "Vlaanderen>Antwerpen>Turnhout>Mekanders>leftover_vaph"


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
        "title": "NBB VOL-VZW jaarrekening 2025 Mekanders deposit 2026-00263425",
        "url": "https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/51f0ab05-641a-11f1-b667-29349a8a69a2",
        "publisher": "NBB CBSO official deposit PDF (consult.cbso.nbb.be)",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2575; FRESH HUNT (VAPH Vergunde Zorgaanbieder address list unscanned pages 5/6/12-14/20-22); official native statutory PDF 241491 bytes 42p VOL-VZW 23.0.10 m05-f; header 01/07/2026; AV 16.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-07 23:18:41 UTC OpenPDF 1.3.26; statutory pages native; prior-year RESTATED (niet identiek met eerder openbaar); broker GET 200 241491 MD5 f9feae6b23d06974c0dda22cea45b71b UUID 51f0ab05-641a-11f1-b667-29349a8a69a2; VOL-VZW 6.1 6.2.1-4 6.3.4 6.4.1-2 6.5.1-3 6.10 6.16 niet dienstig; Companyweb unused for euros; euros from official NBB native PDF text; commissaris Moore Audit / Guy Franken native text",
    },
    {
        "source_id": src_kbo,
        "title": "KBO Mekanders 0431.176.975",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431176975",
        "publisher": "KBO Public Search FOD Economie",
        "accessed_date": DATE,
        "source_class": "strong",
        "notes": "tick2575; Actief Normale toestand since 24.06.1985; VZW; naam Mekanders since 23.01.2019; zetel Steenweg op Oosthoven 25 2300 Turnhout since 15.06.2021; 11 VE leftover-mined city_turnhout + leftover-via-VE FROM leftover city_turnhout (Arendonk/Merksplas/Ravels/Dessel/Hoogstraten/Oud-Turnhout); RSZ2025 88.999 Andere vormen van maatschappelijke dienstverlening zonder huisvesting; Werkgever RSZ since 01.09.1986; Identity trap 0431.176.975 != leftover city GE Turnhout 0207.533.082 != leftover AGB Turnhout 0892.962.204 != leftover Zorggroep Orion 0665.553.622 != leftover Verbint 0408.032.379 remine@2401 != leftover Kinderopvang Turnhout 0465.284.947 != leftover Cirkant jeugdzorg 0423.592.268 != leftover Klim 0422.719.961 remine@2574",
    },
    {
        "source_id": src_vaph,
        "title": "VAPH adreslijst Mekanders Vergunde Zorgaanbieder + RTH + MFC",
        "url": "https://www.vaph.be/organisaties/adressen/mekanders",
        "publisher": "VAPH",
        "accessed_date": DATE,
        "source_class": "primary",
        "notes": "tick2575; official VAPH adreslijst Mekanders Type organisatie Rechtstreeks toegankelijke hulp + Multifunctionele Centra + Vergunde Zorgaanbieder; admin adres Steenweg op Oosthoven 25 2300 Turnhout; FOI info@mekanders.be from official VAPH; leftover mined city_turnhout leftover VAPH after city GE tick844 leftover AGB tick1133; FIRST LOCK leftover city_turnhout leftover VAPH Mekanders",
    },
    {
        "source_id": src_site,
        "title": "Mekanders official site FOI email",
        "url": "https://www.mekanders.be/",
        "publisher": "Mekanders VZW",
        "accessed_date": DATE,
        "source_class": "org",
        "notes": "tick2575; FOI info@mekanders.be + onthaal@mekanders.be from official site; NBB PDF internetadres www.mekanders.be email rik.aerts@mekanders.be; zorg/ondersteuning kinderen en volwassenen met een beperking Noorderkempen kleinschalige woonhuizen/dagcentra; leftover mined city_turnhout leftover VAPH unused leftover-mined AGB leftover type after city GE tick844; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; NOT OCMW; NOT leftover convent; NOT leftover Muylenberg leftover-via-VE Verbint remine@2401; NOT leftover OC Cirkant leftover-via-VE Evara; NOT leftover Clara Fey leftover-via-VE Evara; NOT leftover Klim remine@2574",
    },
]
append_csv("docs/doge/data/sources.csv", sources)

entities = [{
    "entity_id": eid,
    "name_nl": "Mekanders VZW (Turnhout / VAPH Vergunde Zorgaanbieder + RTH + MFC; woonhuizen en dagcentra Noorderkempen)",
    "name_fr": "",
    "name_en": "",
    "level": "L5",
    "parent_id": "city_turnhout",
    "community_language": "nl",
    "website": "https://www.mekanders.be/",
    "foi_email": "info@mekanders.be",
    "foi_postal": "Steenweg op Oosthoven 25, 2300 Turnhout",
    "notes": "tick2575 YE2025 Strong official native NBB PDF deposit 2026-00263425 + Strong KBO 0431.176.975 Actief 11 VE; leftover mined city_turnhout leftover VAPH unused leftover-mined AGB leftover type after city GE tick844 + AGB tick1133; official zetel Steenweg op Oosthoven 25 2300 Turnhout; RSZ2025 88.999; envelope 70/76A JUMP 13896468; 733 11456564 (reclass vs restated 2024 793415); 73 11682593; omzet70 DROP 1779637 (was restated 11840608); 9901 DROP 232982; 9904 JUMP 609540; cash JUMP 6135757 after termijnrekeningen 53 DROP to 0 from 5364549; FTE 146,8 FLAT; Identity trap != leftover city GE 0207.533.082 != leftover AGB 0892.962.204 != leftover Verbint 0408.032.379 remine@2401 != leftover Klim 0422.719.961 remine@2574; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea/Korian/Vulpia/CuraCare/OCMW/commercial BV/convent",
}]
append_csv("docs/doge/data/entities.csv", entities)


def bud(bid, amount, basis, notes):
    a = str(amount)
    return {"budget_id": bid, "entity_id": eid, "year": "2025", "amount_eur": a, "amount_min_eur": a, "amount_max_eur": a, "basis": basis, "source_id": src_pdf, "confidence": "strong", "notes": notes}


budgets = [
    bud("bud_mekanders_turnhout_733subsidies_jr2025_statutory", 11456564, "NBB VOL-VZW code 733 subsidies YE2025 JUMP (reclass vs restated 2024 793415)", "tick2575; PDF native; restated YE2024 793415; VAPH/Maribel/VIPA envelope; FOI matrix behind 11456564"),
    bud("bud_mekanders_turnhout_opbrengsten70_76a_jr2025_statutory", 13896468, "NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +2.93%", "tick2575; PDF native; restated YE2024 13501189 identical-in-this-PDF; VOL envelope"),
    bud("bud_mekanders_turnhout_73_jr2025_statutory", 11682593, "NBB VOL-VZW code 73 lidgeld/schenkingen/legaten/subsidies YE2025 JUMP (reclass)", "tick2575; PDF native; restated YE2024 876894; 733 11456564 / 731 101028 / 732 125000 / 730 empty"),
    bud("bud_mekanders_turnhout_omzet70_jr2025_statutory", 1779637, "NBB VOL-VZW code 70 omzet YE2025 DROP (reclass vs restated 2024 11840608)", "tick2575; PDF native; restated YE2024 11840608; commercial-only vs large 73 after VAPH settlements moved into result"),
    bud("bud_mekanders_turnhout_personnel62_jr2025_statutory", 11181965, "NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +5.91%", "tick2575; PDF native; restated YE2024 10557699; FTE 9087 146,8 FLAT from 146,6"),
    bud("bud_mekanders_turnhout_bedrijfswinst_jr2025_statutory", 232982, "NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -34.29%", "tick2575; PDF native; restated YE2024 354568; -121586"),
    bud("bud_mekanders_turnhout_pnl_jr2025_statutory", 609540, "NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +17.47%", "tick2575; PDF native; restated YE2024 518904; 9903 609540; fin 75/76B 401900"),
    bud("bud_mekanders_turnhout_equity_jr2025_statutory", 11208352, "NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +5.96%", "tick2575; PDF native; restated YE2024 10577893; kapitaalsubsidies 15 3640041"),
    bud("bud_mekanders_turnhout_assets_jr2025_statutory", 14493444, "NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +3.51%", "tick2575; PDF native; restated YE2024 14002049; aanbouw 27 738750 (was 0)"),
    bud("bud_mekanders_turnhout_debt_jr2025_statutory", 2881949, "NBB VOL-VZW code 17/49 schulden YE2025 DROP -0.90%", "tick2575; PDF native; restated YE2024 2908144; kredietinstellingen 173 767384 Belfius per jaarverslag"),
    bud("bud_mekanders_turnhout_cash_jr2025_statutory", 6135757, "NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +610.19%", "tick2575; PDF native; restated YE2024 863957; +5271800; termijnrekeningen 53 DROP 0 from 5364549 (cash parking reclass)"),
    bud("bud_mekanders_turnhout_capex816x_jr2025_statutory", 930409, "NBB VOL-VZW codes 8162+8163+8166 aanschaffingen MVA YE2025", "tick2575; PDF native; 8162 82554 + 8163 109105 + 8166 aanbouw 738750; 8161 empty; jaarverslag Goriën Dessel nieuwbouw + Beukenhof Turnhout renovatie"),
]
append_csv("docs/doge/data/budgets.csv", budgets)

cash_json = json.dumps({"2025": 6135757, "2024": 863957}, separators=(",", ":"))
commitments = [{
    "commitment_id": comm_id,
    "title": "Mekanders Turnhout YE2025 (70/76A JUMP 13.90m / 733 11.46m / cash JUMP 6.14m / Strong PDF)",
    "entity_id": eid,
    "beneficiary": "VAPH + leftover city_turnhout leftover dual",
    "legal_basis": "Mekanders VZW (KBO 0431.176.975; Actief; 11 VE; official zetel Turnhout; RSZ2025 88.999; VAPH Vergunde Zorgaanbieder + RTH + MFC)",
    "decision_date": "2026-06-16",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "13896468",
    "cash_by_year": cash_json,
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/51f0ab05-641a-11f1-b667-29349a8a69a2",
    "stated_goal": "Public leftover VAPH dual of mined city_turnhout leftover-mined AGB leftover VAPH",
    "cut_option": "Publish VAPH/gemeentelijke matrix behind 70/76A JUMP 13896468 and 733 11456564 and why omzet70 DROP while 73 JUMP and why cash JUMP 6135757 after emptying 5364549 termijnrekeningen",
    "source_id": src_pdf,
    "confidence": "strong",
    "hierarchy_path": "Vlaanderen>Antwerpen>Turnhout>Mekanders>JR2025_statutory_L5",
    "notes": "tick2575; Strong official native PDF; leftover mined city_turnhout leftover VAPH unused leftover-mined AGB leftover type after city GE tick844; 11 VE; prior-year restated; FIRST LOCK leftover city_turnhout leftover VAPH Mekanders; NOT leftover-via-VE of a DIFFERENT leftover city as parent; NOT Armonea; NOT Korian; NOT Vulpia; not TE-additive",
}]
append_csv("docs/doge/data/commitments.csv", commitments)

leaderboard = [{
    "item_id": lb_id,
    "name": "Mekanders Turnhout 70/76A JUMP 13.90m / 733 11.46m / cash JUMP 6.14m (YE2025 leftover city_turnhout leftover VAPH)",
    "level": "L5",
    "type": "vaph_vzw_statutory",
    "hierarchy_path": hier,
    "annual_cost_eur": "13896468",
    "total_cost_eur": "13896468",
    "tco_notes": "PDF 70/76A 13896468 JUMP +2.93%; 733 11456564; 73 11682593 (reclass vs restated 2024 876894); omzet70 DROP 1779637; bedrijfswinst DROP 232982; pnl JUMP 609540; equity JUMP 11208352; assets JUMP 14493444; debt DROP 2881949; cash JUMP 6135757 after termijnrekeningen 53 emptied 5364549; personnel62 JUMP 11181965; leftover city_turnhout leftover VAPH",
    "confidence": "strong",
    "source_id": src_pdf,
    "beneficiaries": "VAPH + leftover city_turnhout leftover dual",
    "stated_goal": "leftover VAPH dual leftover city_turnhout leftover-mined AGB leftover VAPH",
    "measured_outcome": "13.90m 70/76A JUMP; 11.46m 733; 9901 DROP 233k; 6.14m cash JUMP after 5.36m deposits emptied; 146,8 FTE FLAT; leftover city_turnhout leftover VAPH",
    "absurdity_score": "5.40",
    "cost_score": "6.50",
    "difficulty": "4.50",
    "priority_index": "5.50",
    "cut_proposal": "FOI VAPH / gemeente Turnhout matrix behind 70/76A 13896468 and 733 11456564 and why omzet70 DROP 1779637 while 73 JUMP 11682593 (jaarverslag: VAPH-afrekeningen 2024-2025 now in result) and why cash JUMP 6135757 after termijnrekeningen 53 DROP to 0 from 5364549",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2575 leftover mined city_turnhout leftover VAPH Mekanders after city GE tick844 leftover-mined AGB leftover VAPH; FIRST LOCK leftover city_turnhout leftover VAPH Mekanders; HARD SKIP leftover city_machelen Klim remine@2574 leftover Muylenberg leftover-via-VE Verbint remine@2401 leftover OC Cirkant leftover-via-VE Evara leftover Clara Fey leftover-via-VE Evara leftover De Witte Mol leftover-via-VE Stijn leftover DPA Zonhoven leftover-via-VE Stijn leftover Mok 0 deposits leftover Woonondersteuning Vlaanderen YE2024 leftover De Triangel YE2024 leftover Nektari remine leftover Nido Brussels leftover Bethanie SCAN leftover Voluit remine leftover VillaVip 0 leftover Armonea/Korian/Vulpia leftover OCMW leftover convent leftover leftover-via-VE of a DIFFERENT leftover city as parent leftover groenezorg leftover ouderinitiatief leftover YE2024-only leftover 0-deposit; 11 VE; prior-year restated; next rq_2576 leftover dual (NOT every-10; next every-10 2580); never mix off-TE dual into 348bn TE pie",
}]
append_csv("docs/doge/data/leaderboard.csv", leaderboard)

foi_rows = [{
    "gap_id": gap_id,
    "hierarchy_path": hier_foi,
    "entity_id": eid,
    "what_is_missing": "VAPH/gemeentelijke matrix behind VOL-VZW YE2025 70/76A JUMP 13896468 vs omzet70 DROP 1779637, 733 11456564 (reclass vs restated 2024 793415) with 9901 DROP 232982 while 9904 JUMP 609540 and cash JUMP 6135757 after emptying 5364549 termijnrekeningen",
    "why_it_matters": "Public leftover VAPH dual of mined city_turnhout leftover-mined AGB leftover VAPH shows 13.90m 70/76A envelope while subsidy matrix, 70-to-73 reclass of VAPH settlements, and cash parking of 6.14m stay unsourced",
    "priority": "6",
    "recipient_body": "Mekanders VZW / Voorzitter Raad van Bestuur",
    "recipient_email": "info@mekanders.be",
    "recipient_postal": "Steenweg op Oosthoven 25, 2300 Turnhout",
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
    "notes": "tick2575; concept NOT verzonden; Strong PDF 2026-00263425; prio6",
}]
append_csv("docs/doge/data/foi_queue.csv", foi_rows)

Path("/tmp/tick2575").mkdir(parents=True, exist_ok=True)
Path("/tmp/tick2575/NOW.txt").write_text(NOW)
Path("/tmp/tick2575/IDS.json").write_text(json.dumps({"eid": eid, "gap_id": gap_id, "comm_id": comm_id, "lb_id": lb_id, "NOW": NOW, "src_pdf": src_pdf}))
print("NOW", NOW)
print("appended sources+4 entities+1 budgets+12 commitments+1 leaderboard+1 foi+1")
