# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_otar_omzet_12_43m_diensten_10_24m_div_14_47m_l5",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>NV>OtaryRS>JR2025_L5",
    "entity_id": "nv_otar",
    "what_is_missing": "6.10 omzet category/geo empty (omzet 12426978) + diensten 10235828 no split + dividend 14471000 DROP vs 63006000 per 12.5pct aandeelhouder unpublished + FVA 82864237 (Otary BIS 51pct / Rentel 52pct; Seastar+Mermaid path unpublished) + LT achtergesteld 11000000 counterpart/rate unpublished (ECO2050 1360 books 11m) + FVA income 19116262 DROP vs 63719833 which daughter paid unpublished + othops 1391323 JUMP vs 434814 + bestuurders 9503 empty + voorzitter unlabelled + jaarverslag/commissarisverslag pages image-only",
    "why_it_matters": "Leftover Nuhma-adjacent public-law NV offshore-wind holding of 8 equal 12.5pct aandeelhouders (Z-Kracht at Nuhma zetel + Aspiravi/DEME/Elicio/Green Offshore/Power@Sea/Socofe/WE Environnement) after leftover AGB/IGS hunt: 95.63m assets / 12.43m omzet / 82.86m FVA / 14.47m dividend DROP / 11.00m achtergesteld / 42.7 VTE / public-law NV hides omzet split and per-shareholder dividend is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "Otary RS NV / Raad van Bestuur / 8 aandeelhouders 12.5pct",
    "recipient_email": "administration@otary.be",
    "recipient_postal": "Buskruitstraat 3 8400 Oostende",
    "draft_letter_path": "docs/doge/foi/drafts/gap_otar_omzet_12_43m_diensten_10_24m_div_14_47m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_otar_jr2025_pnl",
    "linked_leaderboard_id": "lb_otar_omzet_12_43m_diensten_10_24m_div_14_47m",
    "created_utc": "2026-08-19T05:24:00Z",
    "updated_utc": "2026-08-19T05:24:00Z",
    "notes": "tick1399 leftover Nuhma-adjacent public-law NV after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VOL-kap PDF now extracted (589485 bytes 47p deposit 2026-00254280). Leftover AGB first: already mined / extract-only / 404 — skipped. Leftover IGS WAGSO already mined / IGL+IVAREM+IWVA still 2024 / IVEKA=Fluvius Kempen 1384 / IGEAN-milieu already mined 1341 / IVVO already mined 1345 — skipped. Dommelhof 0777.495.085 no jaarrekening — skipped. VENTUM not IGS/AGB — skipped. Otary RS leftover-next fallback live CDN this tick — taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
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
