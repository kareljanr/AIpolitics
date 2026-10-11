# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_iglg_omzet_48_16m_pers_40_51m_debt_31_77m_l5",
    "hierarchy_path": "Vlaanderen>Limburg>IGS>IGL>JR2025_L5",
    "entity_id": "igs_iglg",
    "what_is_missing": "6.10 geo empty (omzet 48156858; VL werkingsopbrengsten 40228178 unpublished per gemeente/centrum) + diensten 5366617 no split + pers 40508243 / 529.5 VTE / YE 680 unpublished per centrum + debt 31766387 (LT bank 20039581 counterpart/rate unpublished) + hypotheekmandaat 28715000 + capsub 8217525 dossier unpublished + termijndeposito 9500000 bank/rate unpublished + named vennoten list unpublished + masterplan fase2 aannemer unpublished",
    "why_it_matters": "Leftover zorg IGS of mined Limburg municipalities + provincie after leftover AGB hunt: 65.30m assets / 48.16m omzet (40.23m VL werkingsopbrengsten) / 40.51m pers / 529.5 VTE / 31.77m debt / 8.22m capsub / 9.50m deposito hides per-gemeente subsidy and bank counterpart is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "IGL / Raad van Bestuur / voorzitter Nele Beckers",
    "recipient_email": "info@iglimburg.be",
    "recipient_postal": "Klotstraat 125 3600 Genk",
    "draft_letter_path": "docs/doge/foi/drafts/gap_iglg_omzet_48_16m_pers_40_51m_debt_31_77m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_iglg_jr2025_pnl",
    "linked_leaderboard_id": "lb_iglg_omzet_48_16m_pers_40_51m_debt_31_77m",
    "created_utc": "2026-08-19T05:40:00Z",
    "updated_utc": "2026-08-19T05:40:00Z",
    "notes": "tick1400 leftover zorg IGS after honest leftover AGB hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1080297 bytes 70p deposit 2026-00270170). Leftover AGB first: already mined / extract-only / 404 as of 1399 — skipped. IGL was 2024 last tick 1399; now live 2025 — taken. OVCO leftover crematorium CDN also live — leftover next. IVAREM still 2024. IWVA already mined as Aquaduin 1349. Dommelhof not re-probed. Rematics/Sunfin not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
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
