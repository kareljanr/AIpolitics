# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_dds_othops_5_22m_inv_12_79m_prov_7_85m_l5",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>IGS>DDS>JR2025_L5",
    "entity_id": "igs_dds",
    "what_is_missing": "andere bedrijfsopbrengsten 5219038 mostly unpublished (only 740 subsidies 700935) + voorraden onroerend 12793375 dossier/aannemer unpublished + voorzieningen 7847265 (herstel 3345181 + overige 3866038) dossier unpublished + prepaid 2559272 counterpart unpublished + cash drop 2.26m bank/rate unpublished + commissaris fee unpublished (VOL-kap 8 image-only; 6.18 not filed) + named gemeente share-% unpublished",
    "why_it_matters": "Leftover streek IGS of mined Oost-Vlaanderen municipalities after leftover AGB/IGS hunt: 48.50m assets / 5.22m unpublished othops / 12.79m land bank / 7.85m voorzieningen hides development-fee and land-bank counterpart is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "DDS / Raad van Bestuur / voorzitter Hans Knop / algemeen directeur Kris Dooms",
    "recipient_email": "info@dds-streekregisseurs.be",
    "recipient_postal": "Bevrijdingslaan 201 9200 Dendermonde",
    "draft_letter_path": "docs/doge/foi/drafts/gap_dds_othops_5_22m_inv_12_79m_prov_7_85m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_dds_jr2025_pnl",
    "linked_leaderboard_id": "lb_dds_othops_5_22m_inv_12_79m_prov_7_85m",
    "created_utc": "2026-08-19T06:15:00Z",
    "updated_utc": "2026-08-19T06:15:00Z",
    "notes": "tick1402 leftover streek IGS after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VOL-kap PDF now extracted (2117343 bytes 45p deposit 2026-00188846). Leftover AGB first: already mined / extract-only / 2024 as of 1401 — skipped. IGO leftover Vlinter member last JR still 2024. IVAREM still JR2024. Dommelhof leftover EVA no 2025. Rematics/Sunfin not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
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
