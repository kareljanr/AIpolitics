# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_ptri_omzet_empty_debt_4_57m_recv_1_57m_l5",
    "hierarchy_path": "Vlaanderen>Limburg>Sint-Truiden>AGB_Patri>JR2025_L5",
    "entity_id": "agb_ptri",
    "what_is_missing": "omzet 70 empty / 60/61 empty so diensten unpublished as a split (only brutomarge 574007 published) + pers 62 empty / VTE unpublished + ST vorderingen 1565883 counterpart unpublished + LT bank 3403750 terms unpublished + overige ST 216962 JUMP counterpart unpublished + commissaris 6.6 empty / no commissarisverslag + dividend 16986 named Stad Sint-Truiden share unpublished",
    "why_it_matters": "Leftover AGB of mined city Sint-Truiden after leftover AGB hunt: 9.69m assets / omzet empty / 0.57m brutomarge / 4.57m debt / 1.57m recv hides cultuurcentra turnover and vennoot dividend is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "AGB Patri / Raad van Bestuur / voorzitter Ann Ruyters",
    "recipient_email": "info.boekhouding@sint-truiden.be",
    "recipient_postal": "Gazometerstraat 9 3800 Sint-Truiden",
    "draft_letter_path": "docs/doge/foi/drafts/gap_ptri_omzet_empty_debt_4_57m_recv_1_57m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ptri_jr2025_pnl",
    "linked_leaderboard_id": "lb_ptri_omzet_empty_debt_4_57m_recv_1_57m",
    "created_utc": "2026-08-19T07:45:00Z",
    "updated_utc": "2026-08-19T07:45:00Z",
    "notes": "tick1407 leftover AGB of mined city Sint-Truiden after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VKT-inb PDF now extracted (58813 bytes 20p deposit 2026-00258861). Leftover AGB first: PATRI ST was JR2024-only last ticks; CDN live this tick. AGB Bredene already mined 1193. AGB Ieper Vauban/Musea already mined. AGB AGOST already mined. Trupark ST unpublished. Aarschot/Dendermonde/VESPA still 2024. AGB Genk already mined. AGB Lille liquidation. IGO leftover last JR still 2024. IVAREM still JR2024. Dommelhof leftover EVA not taken. Rematics/Sunfin not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
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
