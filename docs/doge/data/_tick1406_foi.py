# -*- coding: utf-8 -*-
import csv, sys
from pathlib import Path
csv.field_size_limit(sys.maxsize)
p = Path("/workspace/AIpolitics/docs/doge/data/foi_queue.csv")
row = {
    "gap_id": "gap_mlso_diensten_7_75m_interwaas_3_76m_nrec_4_42m_l5",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Waaslandhaven>MLSO>JR2025_L5",
    "entity_id": "igs_mlso",
    "what_is_missing": "diensten 7752488 split unpublished (jaarverslag 1.8m fietspad Kieldrecht / 1.4m extra cofinanciering) + Interwaas schadevergoeding LPW 3762955.84 booked split unpublished + nrec 66A 4415758 andere unpublished + overige schulden 6823728 counterpart unpublished + vennoten named share-pct unpublished + dividend 2910456 named vennoot share unpublished",
    "why_it_matters": "Leftover IGS of mined Waasland + Vlaams Gewest + PoAB after leftover AGB hunt: 227.28m assets / 24.04m omzet / 7.75m diensten / 3.76m Interwaas / 4.42m nrec hides port-land fee and vennoot dividend is a dual opacity residual, not TE-additive of 348bn.",
    "priority": "8",
    "recipient_body": "MLSO / Raad van Bestuur / voorzitter Boudewijn Vlegels / ondervoorzitter Marc Van De Vijver",
    "recipient_email": "info@mlso.be",
    "recipient_postal": "Sint-Paulusplein 27 9120 Beveren-Kruibeke-Zwijndrecht",
    "draft_letter_path": "docs/doge/foi/drafts/gap_mlso_diensten_7_75m_interwaas_3_76m_nrec_4_42m_l5.md",
    "status": "ready",
    "date_ready": "2026-08-19",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_mlso_jr2025_pnl",
    "linked_leaderboard_id": "lb_mlso_omzet_24_04m_diensten_7_75m_interwaas_3_76m",
    "created_utc": "2026-08-19T07:30:00Z",
    "updated_utc": "2026-08-19T07:30:00Z",
    "notes": "tick1406 leftover IGS of mined Waasland after honest leftover AGB/IGS hunt; live JR2025 official NBB WVV VOL-inb PDF now extracted (592563 bytes 61p deposit 2026-00247733). Leftover AGB first: Aarschot/Dendermonde/VESPA still 2024; AGB Genk already mined; AGB Lille liquidation; Harelbeke no distinct AGB. IGO leftover Vlinter member last JR still 2024. IVAREM still JR2024. Dommelhof leftover EVA no jaarrekening. Rematics/Sunfin not taken. NBB consult skipped. Belscope/Companyweb euros not used. ready not sent",
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
