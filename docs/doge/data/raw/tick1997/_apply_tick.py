# tick1997 apply — CHR Verviers
import csv
from pathlib import Path

csv.field_size_limit(10**7)

DATA = Path(__file__).resolve().parents[2]


def append_rows(path, rows):
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        for r in rows:
            w.writerow(r)


cash = (
    '{"2025_omzet":251756992,"2025_pnl":890809,'
    '"2025_equity":62397208,"2025_bruto":125531398,"2025_fte":1272.9}'
)

append_rows(
    DATA / "sources.csv",
    [
        [
            "src_chr_verviers_jr2025_cw",
            "CHR Verviers YE2025 Companyweb NL+EN+FR",
            "https://www.companyweb.be/nl/0250893369/centre-hospitalier-regional-de-verviers",
            "Companyweb / NBB-derived",
            "2026-08-24",
            "secondary_aggregator",
            "tick1997; Medium CW; omzet JUMP 251756992 pnl JUMP turnaround 890809 equity JUMP 62397208 bruto JUMP 125531398 FTE 1272.9; neerlegging 18.07.2026; assets/debt Unknown",
        ],
        [
            "src_chr_verviers_jr2025_cw_en",
            "CHR Verviers YE2025 Companyweb EN",
            "https://www.companyweb.be/en/0250893369/centre-hospitalier-regional-de-verviers",
            "Companyweb",
            "2026-08-24",
            "secondary_aggregator",
            "tick1997; EN cross-check",
        ],
        [
            "src_chr_verviers_jr2025_cw_fr",
            "CHR Verviers YE2025 Companyweb FR",
            "https://www.companyweb.be/fr/0250893369/centre-hospitalier-regional-de-verviers",
            "Companyweb",
            "2026-08-24",
            "secondary_aggregator",
            "tick1997; FR cross-check",
        ],
        [
            "src_chr_verviers_kbo_1997",
            "KBO Public Search CHR Verviers 0250.893.369",
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0250893369",
            "KBO",
            "2026-08-24",
            "official_register",
            "tick1997; Actief CV; Rue du Parc 29 4800 Verviers; 8 VE; email officiel.ic-chrverviers@chrverviers.be",
        ],
        [
            "src_chr_verviers_site_1997",
            "chrverviers.be CHR Verviers East Belgium",
            "https://www.chrverviers.be/",
            "CHR Verviers",
            "2026-08-24",
            "official_org",
            "tick1997; contact dirgen@chrverviers.be / officiel.ic-chrverviers@chrverviers.be",
        ],
    ],
)

append_rows(
    DATA / "entities.csv",
    [
        [
            "igs_chr_verviers",
            "CHR Verviers (Centre Hospitalier Regional de Verviers)",
            "CHR Verviers (Centre Hospitalier Regional de Verviers)",
            "CHR Verviers (regional hospital CV)",
            "igs",
            "wallonie_gov",
            "fr",
            "https://www.chrverviers.be/",
            "officiel.ic-chrverviers@chrverviers.be",
            "Rue du Parc 29, 4800 Verviers",
            "tick1997 YE2025 Medium CW NL+EN+FR + Strong KBO 0250.893.369 Actief CV 8 VE; omzet JUMP 251.76m pnl JUMP turnaround 0.89m",
        ],
    ],
)

append_rows(
    DATA / "budgets.csv",
    [
        [
            "bud_chr_verviers_omzet_jr2025_statutory",
            "igs_chr_verviers",
            "2025",
            "251756992",
            "",
            "",
            "CW statutory omzet",
            "src_chr_verviers_jr2025_cw",
            "medium",
            "tick1997; YE2025 omzet JUMP 251756992 (+3.47pct)",
        ],
        [
            "bud_chr_verviers_pnl_jr2025_statutory",
            "igs_chr_verviers",
            "2025",
            "890809",
            "",
            "",
            "CW statutory pnl",
            "src_chr_verviers_jr2025_cw",
            "medium",
            "tick1997; YE2025 pnl JUMP turnaround 890809 (vs YE2024 LOSS -927625)",
        ],
        [
            "bud_chr_verviers_equity_jr2025_statutory",
            "igs_chr_verviers",
            "2025",
            "62397208",
            "",
            "",
            "CW statutory equity",
            "src_chr_verviers_jr2025_cw",
            "medium",
            "tick1997; YE2025 equity JUMP 62397208 (+0.02pct)",
        ],
        [
            "bud_chr_verviers_bruto_jr2025_statutory",
            "igs_chr_verviers",
            "2025",
            "125531398",
            "",
            "",
            "CW statutory bruto",
            "src_chr_verviers_jr2025_cw",
            "medium",
            "tick1997; YE2025 bruto JUMP 125531398 (+4.48pct)",
        ],
        [
            "bud_chr_verviers_fte_jr2025_statutory",
            "igs_chr_verviers",
            "2025",
            "1272.9",
            "",
            "",
            "CW social-balance FTE",
            "src_chr_verviers_jr2025_cw",
            "medium",
            "tick1997; YE2025 FTE 1272.9 (was 1286.3)",
        ],
    ],
)

append_rows(
    DATA / "commitments.csv",
    [
        [
            "comm_chr_verviers_jr2025_statutory_hospital",
            "CHR Verviers YE2025 leftover hospital dual (omzet JUMP 251.76m / pnl JUMP turnaround 0.89m / equity JUMP 62.40m)",
            "igs_chr_verviers",
            "Verviers hospital patients / CHR Verviers",
            "CV / cooperative hospital (KBO 0250.893.369)",
            "2026-07-18",
            "2025",
            "2025",
            "251756992",
            cash,
            "0",
            "active",
            "https://www.companyweb.be/nl/0250893369/centre-hospitalier-regional-de-verviers",
            "Regional hospital care (Verviers East Belgium)",
            "Publish NBB PDF assets/debt + pnl turnaround recon FOI",
            "src_chr_verviers_jr2025_cw",
            "medium",
            "Liege>Verviers>CHR_Verviers>JR2025_statutory_L5",
            "tick1997; Medium CW; assets/debt Unknown; AGB Bornem JR2024; FARO/AIESH/REW YE2024; CNDG already mined; Erasme/UZ/AZ Sint-Lucas deferred",
        ],
    ],
)

append_rows(
    DATA / "leaderboard.csv",
    [
        [
            "lb_chr_verviers_omzet_jump_251_76m_pnl_turnaround_0_89m_equity_jump_jr2025",
            "CHR Verviers omzet JUMP 251.76m / pnl JUMP turnaround 0.89m / equity JUMP 62.40m (YE2025)",
            "L5",
            "walloon_hospital_cv_dual",
            "Liege>Verviers>CHR_Verviers>JR2025_statutory_L5",
            "251756992",
            "62397208",
            "statutory omzet JUMP 251756992 pnl JUMP turnaround 890809 equity JUMP 62397208 bruto JUMP 125531398 FTE 1272.9; assets/debt Unknown",
            "medium",
            "src_chr_verviers_jr2025_cw",
            "Verviers hospital patients via CHR Verviers CV",
            "Regional hospital care",
            "Medium CW YE2025; 251.76m omzet with pnl turnaround from LOSS; equity flat +0.02pct; NBB PDF residual",
            "5.5",
            "6.0",
            "4.0",
            "5.55",
            "Publish NBB PDF assets/debt FOI; recon pnl turnaround vs YE2024 LOSS path vs CNDG/Haute Senne",
            "active",
            "",
            "tick1997 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000",
        ],
    ],
)

append_rows(
    DATA / "foi_queue.csv",
    [
        [
            "gap_chr_verviers_nbb_pdf_assets_debt_pnl_turnaround_matrix_l5",
            "Liege>Verviers>CHR_Verviers>NBB_PDF_assets_debt_pnl_turnaround",
            "igs_chr_verviers",
            "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl turnaround recon vs YE2024 LOSS",
            "Medium CW shows 251.76m omzet Verviers hospital CV with pnl turnaround without balance sheet",
            "7",
            "CHR Verviers CV",
            "officiel.ic-chrverviers@chrverviers.be",
            "Rue du Parc 29, 4800 Verviers",
            "docs/doge/foi/drafts/gap_chr_verviers_nbb_pdf_assets_debt_pnl_turnaround_matrix_l5.md",
            "ready",
            "2026-08-24",
            "",
            "",
            "",
            "",
            "comm_chr_verviers_jr2025_statutory_hospital",
            "lb_chr_verviers_omzet_jump_251_76m_pnl_turnaround_0_89m_equity_jump_jr2025",
            "2026-08-24T02:50:00Z",
            "2026-08-24T02:50:00Z",
            "tick1997; human-send only; Medium CW; also dirgen@chrverviers.be; next every-10 2000",
        ],
    ],
)

# research_queue
rq_path = DATA / "research_queue.csv"
with open(rq_path, encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys())

for r in rows:
    if r.get("task_id") == "rq_1997":
        r["title"] = "leftover dual hole-fill after CNDG — CHR Verviers YE2025 Medium"
        r["status"] = "done"
        r["hierarchy_target"] = "Liege>Verviers>CHR_Verviers>JR2025_L5"
        r["entity_id"] = "igs_chr_verviers"
        r["instructions"] = (
            "Completed leftover CHR Verviers YE2025 Medium CW; KBO 0250.893.369; "
            "omzet JUMP 251756992 pnl JUMP turnaround 890809 equity JUMP 62397208 bruto JUMP 125531398 FTE 1272.9; "
            "FOI gap_chr_verviers_nbb_pdf_assets_debt_pnl_turnaround_matrix_l5"
        )
        r["blocked_gap_id"] = "gap_chr_verviers_nbb_pdf_assets_debt_pnl_turnaround_matrix_l5"
        r["updated_utc"] = "2026-08-24T02:50:00Z"
        r["notes"] = (
            "tick1997 CHR Verviers Medium omzet JUMP 251.76m pnl JUMP turnaround 0.89m equity JUMP 62.40m; "
            "FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Erasme/UZ Brussel/AZ Sint-Lucas deferred; next rq_1998; next every-10 2000"
        )

instr_1998 = (
    "Tick 1997 after CHR Verviers YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital "
    "(Erasme / UZ Brussel / AZ Sint-Lucas / AZJP / ZAS if YE2025). "
    "Do NOT redo CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, "
    "CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, "
    "SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, "
    "BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, "
    "SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
    "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, "
    "IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
)

rows.append(
    {
        "task_id": "rq_1998",
        "title": "leftover dual hole-fill after CHR Verviers",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": instr_1998,
        "blocked_gap_id": "",
        "created_utc": "2026-08-24T02:50:00Z",
        "updated_utc": "2026-08-24T02:50:00Z",
        "notes": "spawned after tick1997 CHR Verviers; next every-10 2000; Erasme/UZ Brussel/AZ Sint-Lucas deferred",
    }
)

with open(rq_path, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

with open(DATA / "loop_state.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "hole_fill",
            "2026-08-24T02:50:00Z",
            "rq_1997",
            "1997",
            "no",
            "tick1997 leftover CHR Verviers 0250.893.369 Medium CW (omzet JUMP 251.76m pnl JUMP turnaround 0.89m equity JUMP 62.40m bruto JUMP 125.53m FTE 1272.9; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Erasme/UZ deferred; next rq_1998; next every-10 2000; continuous hole_fill",
        ]
    )

print("tick1997 CSVs OK")
