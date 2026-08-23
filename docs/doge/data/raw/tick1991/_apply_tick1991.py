# one-shot tick1991 apply — Humani YE2025 Medium CW
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # docs/doge
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
UTC = "2026-08-24T01:20:00Z"
TICK = "1991"

csv.field_size_limit(10**7)


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r), list(r.fieldnames)


def write_csv(path, rows, fieldnames):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


# --- sources ---
sources, sh = read_csv(DATA / "sources.csv")
sources += [
    {
        "source_id": "src_humani_jr2025_cw",
        "title": "Companyweb NL Humani YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0216377108/humani",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1991; YE2025 omzet JUMP 662286253 pnl LOSS -6699123 equity DROP 204947965 bruto JUMP 410553328 FTE 5560; neerlegging 21.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1991/humani_nl.html; FAQ omzet 662286272 minor CW inconsistency — table used",
    },
    {
        "source_id": "src_humani_jr2025_cw_en",
        "title": "Companyweb EN Humani YE2025 statutory",
        "url": "https://www.companyweb.be/en/0216377108/humani",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1991; EN mirror YE2025 Medium; filed 21-07-2026; raw docs/doge/data/raw/tick1991/humani_en.html",
    },
    {
        "source_id": "src_humani_kbo_1991",
        "title": "KBO Humani 0216.377.108 Actief CV Charleroi",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0216377108",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1991; Actief CV; Boulevard Zoe Drion 1 6000 Charleroi; email nemo@humani.be; 31 VE; Aanbestedende overheid; CHU Charleroi-Chimay / hospital intercommunale dual",
    },
    {
        "source_id": "src_humani_site_1991",
        "title": "humani.be CHU Charleroi-Chimay hospital network",
        "url": "https://www.humani.be/",
        "publisher": "Humani",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1991; Marie Curie / Andre Vesale / Vincent Van Gogh hospital sites; distinct from GHdC Les Viviers (ghdc.be) deferred",
    },
]
write_csv(DATA / "sources.csv", sources, sh)

# --- entities ---
entities, eh = read_csv(DATA / "entities.csv")
entities.append(
    {
        "entity_id": "igs_humani",
        "name_nl": "Humani (CHU Charleroi-Chimay)",
        "name_fr": "Humani (CHU Charleroi-Chimay)",
        "name_en": "Humani (Charleroi-Chimay hospital intercommunale CV)",
        "level": "other",
        "parent_id": "wallonie_gov",
        "community_language": "fr",
        "website": "https://www.humani.be/",
        "foi_email": "nemo@humani.be",
        "foi_postal": "Boulevard Zoe Drion 1, 6000 Charleroi",
        "notes": "tick1991 YE2025 Medium CW NL+EN + Strong KBO 0216.377.108 Actief CV; omzet JUMP 662.29m pnl LOSS -6.70m equity DROP 204.95m bruto JUMP 410.55m FTE 5560; assets/debt Unknown; neerlegging 21.07.2026; 31 VE; FOI gap_humani_nbb_pdf_assets_debt_pnl_loss_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; GHdC deferred; do not redo CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia/HELORA",
    }
)
write_csv(DATA / "entities.csv", entities, eh)

# --- budgets ---
budgets, bh = read_csv(DATA / "budgets.csv")
budgets += [
    {
        "budget_id": "bud_humani_omzet_jr2025_statutory",
        "entity_id": "igs_humani",
        "year": "2025",
        "amount_eur": "662286253",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": "src_humani_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1991; omzet JUMP 662286253 +4.29pct vs YE2024 635037376",
    },
    {
        "budget_id": "bud_humani_pnl_jr2025_statutory",
        "entity_id": "igs_humani",
        "year": "2025",
        "amount_eur": "-6699123",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": "src_humani_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1991; pnl LOSS -6699123 swing -325.41pct vs YE2024 profit 2971999",
    },
    {
        "budget_id": "bud_humani_equity_jr2025_statutory",
        "entity_id": "igs_humani",
        "year": "2025",
        "amount_eur": "204947965",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": "src_humani_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1991; equity DROP 204947965 -4.22pct vs YE2024 213972304",
    },
    {
        "budget_id": "bud_humani_bruto_jr2025_statutory",
        "entity_id": "igs_humani",
        "year": "2025",
        "amount_eur": "410553328",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": "src_humani_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1991; bruto JUMP 410553328 +3.32pct vs YE2024 397361115",
    },
    {
        "budget_id": "bud_humani_fte_jr2025_statutory",
        "entity_id": "igs_humani",
        "year": "2025",
        "amount_eur": "5560",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_humani_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1991; YE2025 FTE 5560 vs YE2024 5463 (+97)",
    },
]
write_csv(DATA / "budgets.csv", budgets, bh)

# --- commitments ---
comms, ch = read_csv(DATA / "commitments.csv")
comms.append(
    {
        "commitment_id": "comm_humani_jr2025_statutory_hospital",
        "title": "Humani YE2025 leftover Charleroi-Chimay hospital dual (omzet JUMP 662.29m / pnl LOSS 6.70m / equity DROP 204.95m)",
        "entity_id": "igs_humani",
        "beneficiary": "Hainaut/Charleroi-Chimay patients / CHU network dual",
        "legal_basis": "CV hospital intercommunale Wallonie; Aanbestedende overheid",
        "decision_date": "2026-07-21",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": "662286253",
        "cash_by_year": '{"2025_omzet":662286253,"2025_pnl":-6699123,"2025_equity":204947965,"2025_bruto":410553328,"2025_fte":5560}',
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/nl/0216377108/humani",
        "stated_goal": "Hospital care CHU Charleroi-Chimay (Marie Curie / Vesale / Van Gogh)",
        "cut_option": "Publish NBB PDF assets/debt + pnl LOSS recon FOI",
        "source_id": "src_humani_jr2025_cw",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Charleroi>Humani>JR2025_statutory_L5",
        "notes": "tick1991; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; GHdC deferred; do not redo CHIREC",
    }
)
write_csv(DATA / "commitments.csv", comms, ch)

# --- leaderboard ---
lbs, lh = read_csv(DATA / "leaderboard.csv")
lbs.append(
    {
        "item_id": "lb_humani_omzet_jump_662_29m_pnl_loss_6_70m_equity_drop_jr2025",
        "name": "Humani omzet JUMP 662.29m / pnl LOSS 6.70m / equity DROP 204.95m (Charleroi-Chimay hospital YE2025)",
        "level": "L5",
        "type": "walloon_hospital_igs_dual",
        "hierarchy_path": "Wallonie>Hainaut>Charleroi>Humani>JR2025_statutory_L5",
        "annual_cost_eur": "662286253",
        "total_cost_eur": "204947965",
        "tco_notes": "statutory omzet JUMP 662286253 pnl LOSS -6699123 equity DROP 204947965 bruto JUMP 410553328 FTE 5560; assets/debt Unknown; LOSS turnaround vs YE2024 profit 2.97m",
        "confidence": "medium",
        "source_id": "src_humani_jr2025_cw",
        "beneficiaries": "Charleroi-Chimay / Hainaut patients via Humani CV hospital intercommunale",
        "stated_goal": "CHU Charleroi-Chimay hospital care network",
        "measured_outcome": "Medium CW YE2025; 662.3m omzet JUMP; pnl LOSS turnaround -6.70m; equity DROP -4.22pct; NBB PDF residual",
        "absurdity_score": "5.5",
        "cost_score": "7.5",
        "difficulty": "4.0",
        "priority_index": "6.35",
        "cut_proposal": "Publish NBB PDF assets/debt + pnl LOSS recon FOI; dual vs GHdC/CHIREC/Epicura hospital opacity",
        "status": "active",
        "struck_reason": "",
        "notes": "tick1991 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000; GHdC deferred",
    }
)
write_csv(DATA / "leaderboard.csv", lbs, lh)

# --- foi_queue ---
foi, fh = read_csv(DATA / "foi_queue.csv")
foi.append(
    {
        "gap_id": "gap_humani_nbb_pdf_assets_debt_pnl_loss_matrix_l5",
        "hierarchy_path": "Wallonie>Hainaut>Charleroi>Humani>NBB_PDF_assets_debt_pnl_loss",
        "entity_id": "igs_humani",
        "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl LOSS turnaround recon; dual vs GHdC/CHIREC hospital path",
        "why_it_matters": "Medium CW shows 662m omzet Charleroi-Chimay hospital CV with pnl LOSS -6.70m turnaround without balance sheet",
        "priority": "7",
        "recipient_body": "Humani",
        "recipient_email": "nemo@humani.be",
        "recipient_postal": "Boulevard Zoe Drion 1, 6000 Charleroi / humani.be",
        "draft_letter_path": "docs/doge/foi/drafts/gap_humani_nbb_pdf_assets_debt_pnl_loss_matrix_l5.md",
        "status": "ready",
        "date_ready": "2026-08-24",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": "comm_humani_jr2025_statutory_hospital",
        "linked_leaderboard_id": "lb_humani_omzet_jump_662_29m_pnl_loss_6_70m_equity_drop_jr2025",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "tick1991; human-send only; Medium CW; KBO email nemo@humani.be; next every-10 2000; GHdC deferred",
    }
)
write_csv(DATA / "foi_queue.csv", foi, fh)

# --- research_queue ---
rq, rh = read_csv(DATA / "research_queue.csv")
for row in rq:
    if row["task_id"] == "rq_1991":
        row["title"] = "leftover dual hole-fill after CHIREC EVERY-10 — Humani YE2025 Medium"
        row["status"] = "done"
        row["entity_id"] = "igs_humani"
        row["hierarchy_target"] = "Wallonie>Hainaut>Charleroi>Humani>JR2025_L5"
        row["instructions"] = (
            "Completed leftover Humani Charleroi-Chimay hospital YE2025 Medium CW; "
            "KBO 0216.377.108; omzet JUMP 662286253 pnl LOSS -6699123 equity DROP 204947965 "
            "bruto JUMP 410553328 FTE 5560; assets/debt Unknown; "
            "FOI gap_humani_nbb_pdf_assets_debt_pnl_loss_matrix_l5"
        )
        row["blocked_gap_id"] = "gap_humani_nbb_pdf_assets_debt_pnl_loss_matrix_l5"
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick1991 Humani Medium omzet JUMP 662.29m pnl LOSS 6.70m equity DROP 204.95m; "
            "FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; GHdC deferred; "
            "next rq_1992; next every-10 2000"
        )
        break

rq.append(
    {
        "task_id": "rq_1992",
        "title": "leftover dual hole-fill after Humani",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick 1991 after Humani YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/"
            "energy/hospital (GHdC / Haute Senne / Saint-Luc / CNDG if YE2025). "
            "Do NOT redo Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, "
            "CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, "
            "FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, "
            "BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, "
            "SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
            "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, "
            "Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, "
            "IDELUX Environnement, IDELUX Eau, IDEA."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned after tick1991 Humani; next every-10 2000; GHdC YE2025 deferred",
    }
)
write_csv(DATA / "research_queue.csv", rq, rh)

# --- loop_state ---
state, sth = read_csv(DATA / "loop_state.csv")
state[0].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1991",
        "ticks_completed": "1991",
        "paused": "no",
        "notes": (
            "tick1991 leftover Humani 0216.377.108 Medium CW (omzet JUMP 662.29m pnl LOSS -6.70m "
            "equity DROP 204.95m bruto JUMP 410.55m FTE 5560; assets/debt Unknown); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; GHdC deferred; next rq_1992; "
            "next every-10 2000; continuous hole_fill"
        ),
    }
)
write_csv(DATA / "loop_state.csv", state, sth)

# --- FOI draft ---
FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_humani_nbb_pdf_assets_debt_pnl_loss_matrix_l5.md").write_text(
    """# FOI draft — Humani (NBB PDF / assets-debt / pnl LOSS)

**gap_id:** `gap_humani_nbb_pdf_assets_debt_pnl_loss_matrix_l5`  
**status:** ready (NOT sent)  
**entity:** Humani CV — KBO **0216.377.108**  
**recipient:** nemo@humani.be · Boulevard Zoé Drion 1, 6000 Charleroi  
**sources:** [CW NL](https://www.companyweb.be/nl/0216377108/humani) · [CW EN](https://www.companyweb.be/en/0216377108/humani) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0216377108) · [site](https://www.humani.be/)  
**tick:** 1991  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **21.07.2026**): omzet **EUR662,286,253** JUMP +4.29%; pnl **NEG EUR-6,699,123** LOSS turnaround (−325.41% vs YE2024 profit EUR2,971,999); equity **EUR204,947,965** DROP −4.22%; bruto **EUR410,553,328** JUMP +3.32%; FTE **5560** (+97 vs 5463); assets/debt **Unknown**.
- CHU Charleroi-Chimay hospital intercommunale CV (Marie Curie / André Vésale / Vincent Van Gogh). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. CHIREC already mined. GHdC deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Humani — Boulevard Zoé Drion 1, 6000 Charleroi
via nemo@humani.be / humani.be openbaarheid
cc: SPW Intérieur / Province Hainaut transparence indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Humani + balans (KBO 0216.377.108)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 21.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl LOSS (NEG EUR-6,699,123 vs YE2024 winst EUR2,971,999).
4. Dual vs GHdC / CHIREC / Epicura indien relevant.
Periode 01.01.2025–31.12.2025. Ref: gap_humani_nbb_pdf_assets_debt_pnl_loss_matrix_l5
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

print("tick1991 apply OK")
