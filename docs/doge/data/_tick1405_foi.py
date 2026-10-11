# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_tlt_omzet_empty_lease_9_30m_debt_11_90m_l5",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>Tielt>AGB_Tielt>JR2025_L5",
    "entity_id": "agb_tlt",
    "what_is_missing": "omzet 70 empty on VKT-kap so sport/monumenten euros unpublished + diensten 60/61 empty so brutomarge 679356 split unpublished + pers 62 empty / VTE 9087 empty despite defined-benefit groepsverzekering note + lease 9303045 counterpart unpublished + LT overige leningen 1989840 counterpart unpublished + commissaris unpublished (VKT-kap 8 not filed) + vergoeding inbreng 160660 named city-share unpublished + FVA 9753 counterpart unpublished",
    "why_it_matters": "Leftover AGB of mined city Tielt after leftover AGB hunt: 19.95m assets / 0.68m brutomarge / omzet empty / 9.30m lease / 11.90m debt hides sport-fee and lease counterpart is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "AGB Tielt / Raad van Bestuur / voorzitter Luc Vannieuwenhuyze / ondervoorzitter Lieve Germonprez",
    "recipient_email": "agb@tielt.be",
    "recipient_postal": "Markt 13 8700 Tielt",
    "draft_letter_path": "docs/doge/foi/drafts/gap_tlt_omzet_empty_lease_9_30m_debt_11_90m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_tlt_jr2025_pnl",
    "linked_leaderboard_id": "lb_tlt_omzet_empty_lease_9_30m_debt_11_90m",
    "created_utc": "2026-08-19T07:10:00Z",
    "updated_utc": "2026-08-19T07:10:00Z",
    "notes": "tick1405 leftover AGB of mined city Tielt after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VKT-kap PDF now extracted (61089 bytes 19p deposit 2026-00316168). Leftover AGB first: AGB Tielt statutory CDN live this tick (HTTP 200 / 61089 / 19p) — taken. Aarschot/Dendermonde/VESPA last JR 2024. AGB Genk JR2025 now live but already mined — skipped. AGB Lille in liquidation — skipped. IGO leftover Vlinter member last JR still 2024. IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening. Rematics/Sunfin not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
}
with p.open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    seen = {x[fields[0]] for x in r}
added = 0
with p.open("a", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    if row[fields[0]] not in seen:
        w.writerow({k: row.get(k, "") for k in fields})
        added = 1
print("foi", added)
