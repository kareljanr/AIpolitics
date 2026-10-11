# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_vrko_omzet_26_15m_diensten_12_45m_debt_28_73m_l5",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>IGS>VERKO>JR2025_L5",
    "entity_id": "igs_vrko",
    "what_is_missing": "omzet lokale besturen 18552275 per-gemeente unpublished + diensten 12448633 consultancy/elek split unpublished + debt 28727165 bank/lease counterpart unpublished + pers 11760008 vs sociale balans 12750499 unpublished + voorzieningen herstel 5218575 dossier unpublished + commissaris fee unpublished (VOL-kap 8 image-only; 6.18 not filed) + named gemeente share-% unpublished",
    "why_it_matters": "Leftover waste IGS of mined Oost-Vlaanderen municipalities after leftover AGB hunt: 38.42m assets / 26.15m omzet / 12.45m diensten / 11.76m pers / 28.73m debt hides waste-fee and bank counterpart is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "VERKO / Raad van Bestuur / voorzitter Raf De Wolf / algemeen directeur Peter De Leeuw",
    "recipient_email": "boekhouding@dds-verko.be",
    "recipient_postal": "Bevrijdingslaan 201 9200 Dendermonde",
    "draft_letter_path": "docs/doge/foi/drafts/gap_vrko_omzet_26_15m_diensten_12_45m_debt_28_73m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_vrko_jr2025_pnl",
    "linked_leaderboard_id": "lb_vrko_omzet_26_15m_diensten_12_45m_debt_28_73m",
    "created_utc": "2026-08-19T06:40:00Z",
    "updated_utc": "2026-08-19T06:40:00Z",
    "notes": "tick1403 leftover waste IGS after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VOL-kap PDF now extracted (2087128 bytes 48p deposit 2026-00195553). Leftover AGB first: already mined / extract-only / no live 2025 AGB statutory PDF — skipped. IGO leftover Vlinter member last JR still 2024. IVAREM still JR2024. Dommelhof leftover EVA no 2025. Rematics/Sunfin not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
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
