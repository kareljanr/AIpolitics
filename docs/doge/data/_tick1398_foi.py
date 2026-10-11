# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_ibeg_omzet_empty_div_3_50m_fva_96_37m_l5",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>IGS>IBEG>JR2025_L5",
    "entity_id": "igs_ibeg",
    "what_is_missing": "omzet WVV 70 empty + 6.10 category/geo empty + 74 empty + diensten 809703 JUMP vs 271411 (WVV 61; no split; I.B.E.G.-fonds / adviseur unpublished) + dividend 3500000 DROP vs 5303780 (694; bijlage 3 verdeelsleutel per vennoot unpublished) + FVA 96372430 (Fluvius HV 64830538 21.48pct / VENTUM 9255000 92.55pct / Publigas+Publi-T 13286892) Publi-T kapitaleverhoging 3672433 unpublished + krediet Fluvius HV 9000000 (facility 30000000; rente/looptijd unpublished) + niet-recurrent 519509 minderwaarde / investeringsreserve per gemeente unpublished + VOL-inb 8 statutory audit oordeel missing (only 6:116 liquidity) + 0 VTE",
    "why_it_matters": "Leftover IGS energy holding of 5 mined Halle-Vilvoorde municipalities Grimbergen/Machelen/Meise/Vilvoorde/Wemmel (distinct from Fluvius Halle-Vilvoorde 1387 DSO and from IGS IVEBICA 1397 / Pontes 1396 / Fluvius 1382-1391): 100.49m assets / omzet unpublished / 96.37m FVA / 3.50m dividend / 9.00m Fluvius HV loan / 0 VTE / holding shell hides omzet and per-vennoot dividend is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "IGS IBEG / Raad van Bestuur / Jean-Pierre De Groef / Katrien Vaes / 5 HV vennoten",
    "recipient_email": "info@ibeg.be",
    "recipient_postal": "Laurent Benoit Dewezplein 6 1800 Vilvoorde",
    "draft_letter_path": "docs/doge/foi/drafts/gap_ibeg_omzet_empty_div_3_50m_fva_96_37m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ibeg_jr2025_pnl",
    "linked_leaderboard_id": "lb_ibeg_omzet_empty_div_3_50m_fva_96_37m",
    "created_utc": "2026-08-19T05:05:00Z",
    "updated_utc": "2026-08-19T05:05:00Z",
    "notes": "tick1398 leftover IGS energy holding 5 HV gemeenten after honest hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (1.93MB 40p deposit 2026-00238388). Leftover AGB first: Duffel/Zoersel/Diepenbeek/Dendermonde/Grimbergen/Tienen/Menen/Herk/sogent already mined — skipped; Zwevegem extract-only — skipped. IGS IVEBICA already mined 1397 — skipped. IGS Pontes already mined 1396 — skipped. Fluvius stack already mined 1382-1391 — skipped. IVAREM still 2024 — skipped. IGL last JR2024 — skipped. Dommelhof leftover next if a JR2025 PDF now downloads. Otary RS Nuhma-adjacent fallback not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
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
