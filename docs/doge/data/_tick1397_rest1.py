# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ENT = "igs_ivbc"
SRC = "src_ivbc_jr2025_nbb"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00160301.pdf"
HIER = "Vlaanderen>Antwerpen>IGS>IVEBICA>JR2025_L5"
VENNOTEN = "Hemiksem + Schelle + Niel (ivebica.be/over-ivebica; 7 VE; leftover IGS library/culture/academy Rupel)"
UTC = "2026-08-19T05:15:00Z"
GAP = "gap_ivbc_omzet_empty_toelagen_1_38m_pers_1_02m_l5"
COMM = "comm_ivbc_jr2025_pnl"
LB = "lb_ivbc_omzet_empty_toelagen_1_38m_pers_1_02m"
FOI_EMAIL = "cultuur@ivebica.be"
FOI_POSTAL = "Heuvelstraat 111-117 2620 Hemiksem"
DRAFT = "docs/doge/foi/drafts/gap_ivbc_omzet_empty_toelagen_1_38m_pers_1_02m_l5.md"

def append_one(path, row):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
        idk = fields[0]
        ids = {x.get(idk) for x in r}
    if row.get(idk) in ids:
        print(path.name, "skip")
        return 0
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writerow({k: row.get(k, "") for k in fields})
    print(path.name, 1)
    return 1

append_one(DATA / "commitments.csv", {
    "commitment_id": COMM,
    "title": "IGS IVEBICA JR2025 leftover IGS dual (assets 0.92m / omzet empty-form / toelagen 1.38m / pers 1.02m / PnL +61k)",
    "entity_id": ENT,
    "beneficiary": "IGS IVEBICA / " + VENNOTEN,
    "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
    "decision_date": "2026-06-10",
    "start_year": "2003",
    "end_year": "",
    "total_envelope_eur": "1382095",
    "cash_by_year": "",
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": SRC_URL,
    "stated_goal": "Local leftover IGS map VL library/culture/academy Hemiksem/Schelle/Niel — omzet unpublished on form / 1.38m andere opbr / 1.02m pers / PnL +61k",
    "cut_option": "Publish omzet + 60/61 split + 1.38m vennoot-toelagen per gemeente + 1.02m pers split; do not keep library IGS as dual unpublished vehicle",
    "source_id": SRC,
    "confidence": "strong",
    "hierarchy_path": HIER,
    "notes": "tick1397; assets 919753 omzet empty-form/207858-jv diensten empty-form pers 1023843 debt 338424 pnl 60844 equity 581329 capex 42867 othinc 1382095; FOI ready not sent; not TE-additive of 348bn",
})
append_one(DATA / "leaderboard.csv", {
    "item_id": LB,
    "name": "IGS IVEBICA JR2025 leftover IGS: assets 0.92m / omzet empty-form / toelagen 1.38m / pers 1.02m / 12.2 VTE",
    "level": "L5",
    "type": "local_budget_line",
    "hierarchy_path": HIER,
    "annual_cost_eur": "1023843",
    "total_cost_eur": "1382095",
    "tco_notes": "Leftover dual IGS library/culture/academy 3 municipalities (Hemiksem/Schelle/Niel): assets 0.92m / equity 0.58m / pnl +61k / omzet unpublished on form (jaarverslag 208k) / 60-61 unpublished / diensten unpublished on form / pers 1.02m / 12.2 VTE / andere bedrijfsopbrengsten 1.38m / debt 0.34m (no LT) / cash 455k / capex 43k / voorraad uitleenmateriaal 137k (qualified emphasis); official NBB WVV live; do not treat 1.38m as TE-additive of 348bn",
    "confidence": "strong",
    "source_id": SRC,
    "beneficiaries": "IGS IVEBICA / " + VENNOTEN,
    "stated_goal": "Local leftover IGS map VL library/culture/academy Hemiksem/Schelle/Niel — JR2025 live; dual omzet/toelagen FOI",
    "measured_outcome": "Official NBB WVV 2026-08-19: assets 0.92m / omzet empty-form / toelagen 1.38m / pers 1.02m / pnl +61k / 12.2 VTE",
    "absurdity_score": "6.5",
    "cost_score": "5.5",
    "difficulty": "3.0",
    "priority_index": "5.6",
    "cut_proposal": "Publish omzet + 60/61 split + 1.38m vennoot-toelagen per gemeente + 1.02m pers split; do not keep library IGS as dual unpublished vehicle",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1397; leftover IGS IVEBICA library/culture/academy IGS; FOI ready not sent; not TE-additive of 348bn; distinct from IGS Pontes 1396 and IGS Hofheide 1395 and IGS Westlede 1394 and HAVICREM 1393 and IVLA 1392 / Fluvius stack 1382-1391",
})
append_one(DATA / "foi_queue.csv", {
    "gap_id": GAP,
    "hierarchy_path": HIER,
    "entity_id": ENT,
    "what_is_missing": "omzet WVV 70 empty + 60/61 empty (abbreviated VKT; only brutomarge 1211667 vs 1176709 published; jaarverslag omzet 207858 / diensten 370466) per stroom/gemeente unpublished + andere bedrijfsopbrengsten 1382095 (jaarverslag; subsidies listed 148220) vennoot-toelage per gemeente unpublished + pers 1023843 / 12.2 VTE / split unpublished + voorraden 137079 uitleenmateriaal (commissaris emphasis; WV 69937) unpublished + MVA aanschaf 42867 / IVA 16928 tender unpublished + 6.6 related empty + dividend 694 empty + voorzitter unpublished",
    "why_it_matters": "Leftover IGS library/culture/academy of 3 mined Rupel municipalities Hemiksem/Schelle/Niel (distinct from IGS Pontes 1396 and IGS Hofheide 1395 and IGS Westlede 1394 and HAVICREM 1393 and from IVLA 1392 / Fluvius 1382-1391): 0.92m assets / omzet unpublished on form / 60-61 unpublished / 1.38m andere opbr / 1.02m pers / 137k collectie / abbreviated VKT hides omzet and diensten is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "IGS IVEBICA / Raad van Bestuur / Inge Cornelis / Hemiksem+Schelle+Niel vennoten",
    "recipient_email": FOI_EMAIL,
    "recipient_postal": FOI_POSTAL,
    "draft_letter_path": DRAFT,
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": COMM,
    "linked_leaderboard_id": LB,
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1397 leftover IGS library/culture/academy 3 gemeenten after honest hunt; live JR2025 official NBB WVV VKT-inb PDF now extracted (1.55MB 35p deposit 2026-00160301). IGS Pontes already mined 1396 — skipped. IGS Hofheide already mined 1395 — skipped. IGS Westlede already mined 1394 — skipped. HAVICREM already mined 1393 — skipped. IVLA already mined 1392 — skipped. Fluvius stack already mined 1382-1391 — skipped. Leftover AGB Duffel/Zoersel/Diepenbeek already mined — skipped. IVAREM still 2024 — skipped. Dommelhof leftover next if a JR2025 PDF now downloads. Otary RS Nuhma-adjacent fallback not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
})
