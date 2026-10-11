# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_ovco_omzet_empty_debt_6_31m_cip_0_98m_l5",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>IGS>OVCO>JR2025_L5",
    "entity_id": "igs_ovco",
    "what_is_missing": "omzet 70 empty (only brutomarge 1163024) + 60/61 empty so diensten unpublished + debt 6313967 (LT bank/lease 5608298 counterpart/rate unpublished; gov-guaranteed 5991820 which municipality unpublished) + CIP 975949 dossier/aannemer unpublished + invest 973616 bank/rate unpublished + capsub 1743380 dossier unpublished + named vennoten share-% unpublished + jaarverslag VKT 7/8/10 not filed",
    "why_it_matters": "Leftover crematorium IGS of mined arrondissement-Oostende municipalities after leftover AGB/IGS hunt: 9.37m assets / unpublished omzet / 6.31m debt (5.99m gov-guaranteed) / 0.98m CIP / 0.97m beleggingen hides funeral-fee and bank counterpart is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "OVCO / Raad van Bestuur / voorzitter Karel Labens / directeur Johan Seynaeve",
    "recipient_email": "info@polderbos.be",
    "recipient_postal": "Grintweg 120 8400 Oostende",
    "draft_letter_path": "docs/doge/foi/drafts/gap_ovco_omzet_empty_debt_6_31m_cip_0_98m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ovco_jr2025_pnl",
    "linked_leaderboard_id": "lb_ovco_omzet_empty_debt_6_31m_cip_0_98m",
    "created_utc": "2026-08-19T05:50:00Z",
    "updated_utc": "2026-08-19T05:50:00Z",
    "notes": "tick1401 leftover crematorium IGS after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VKT-kap PDF now extracted (908492 bytes 30p deposit 2026-00287142). Leftover AGB first: already mined / extract-only / 404 as of 1400 — skipped. OVCO leftover-next last tick 1400; now live 2025 — taken. IGL already mined 1400. Dommelhof not re-probed. Rematics/Sunfin not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
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
