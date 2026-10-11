# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_psln_omzet_empty_brutomarge_1_94m_debt_2_19m_l5",
    "hierarchy_path": "Vlaanderen>West-Vlaanderen>IGS>Psilon>JR2025_L5",
    "entity_id": "igs_psln",
    "what_is_missing": "omzet 70 empty on VKT-inb so crematie/uitvaartdienst/koffietafel euros unpublished (note 6.8 only % 90.9/4.6/4.5) + diensten 60/61 empty so brutomarge 1935397 split unpublished + debt 2186709 bank counterpart unpublished + vennoten guarantee 6200000 named gemeente share unpublished + voorziening herstel 327247 dossier unpublished + 5.0-6.8m energy-transit reserve plan unpublished",
    "why_it_matters": "Leftover crematorium IGS of 22 mined West-Vlaanderen municipalities after leftover AGB hunt: 8.63m assets / 1.94m brutomarge / omzet empty / 2.19m debt / 6.20m vennoten guarantee hides funeral-fee and bank counterpart is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "Psilon / Raad van Bestuur / voorzitter Piet Lombaerts / ondervoorzitter Greta Vandeputte",
    "recipient_email": "tine.bloeyaert@crematoriumuitzicht.be",
    "recipient_postal": "Ambassadeur Baertlaan 5 8500 Kortrijk",
    "draft_letter_path": "docs/doge/foi/drafts/gap_psln_omzet_empty_brutomarge_1_94m_debt_2_19m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_psln_jr2025_pnl",
    "linked_leaderboard_id": "lb_psln_omzet_empty_brutomarge_1_94m_debt_2_19m",
    "created_utc": "2026-08-19T06:50:00Z",
    "updated_utc": "2026-08-19T06:50:00Z",
    "notes": "tick1404 leftover crematorium IGS after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VKT-inb PDF now extracted (3254883 bytes 32p deposit 2026-00258944). Leftover AGB first: already mined / extract-only / no live 2025 AGB statutory PDF (Steenokkerzeel already mined; Zoersel/Duffel/WAGSO already mined; Aarschot/Dendermonde/Genk/VESPA last JR 2024) — skipped. IGO leftover Vlinter member last JR still 2024. IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening. Rematics/Sunfin not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
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
