# tick2241 — leftover dual ETA Jean Gielen YE2025 Medium (FREE Walloon ETA Waremme)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_jean_gielen_waremme"
TICK = "2241"
UTC = "2026-08-27T02:25:00Z"
GAP = "gap_jean_gielen_nbb_pdf_assets_debt_equity_jump_54pct_eta_matrix_l5"
COMM = "comm_jean_gielen_jr2025_statutory_eta_equity_jump_54pct"
LB = "lb_jean_gielen_bruto_5_95m_equity_jump_54pct_jr2025"

OM25, OM24 = 4921661, 4202291
BR25, BR24 = 5954785, 6093374
PN25, PN24 = 902861, 835157
EQ25, EQ24 = 2457459, 1594509
FTE25, FTE24 = 157.6, 154.2
RATIO = round(BR25 / OM25, 2)  # ~1.21
EQ_JUMP_PCT = round((EQ25 - EQ24) / EQ24 * 100, 2)  # ~54.12


def read_csv(name: str) -> tuple[list[str], list[dict]]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(name: str, fields: list[str], rows: list[dict]) -> None:
    with (DATA / name).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def upsert(rows: list[dict], key: str, kid: str, new: dict) -> None:
    for i, r in enumerate(rows):
        if r.get(key) == kid:
            rows[i] = {**r, **new}
            return
    rows.append(new)


# --- sources ---
s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_jean_gielen_jr2025_cw_nl",
        "Companyweb NL ETA Jean Gielen Waremme YE2025 statutory",
        "https://www.companyweb.be/nl/0407850653/entreprise-de-travail-adapte-de-waremme-jean-gielen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+17.12%) bruto DROP {BR25} (-2.27%; "
            f"bruto≫omzet ~{RATIO}x) pnl JUMP {PN25} (+8.11%) equity JUMP {EQ25} "
            f"(+{EQ_JUMP_PCT}%) FTE JUMP {FTE25}; neerlegging 26.06.2026; Groot"
        ),
    ),
    (
        "src_jean_gielen_jr2025_cw_en",
        "Companyweb EN ETA Jean Gielen Waremme YE2025 statutory",
        "https://www.companyweb.be/en/0407850653/entreprise-de-travail-adapte-de-waremme-jean-gielen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror YE2025 Medium; filed 26-06-2026; Last balance sheet year 2025; "
            f"Big; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; Equity {EQ25}; "
            f"Employees {FTE25}; raw tick2241/"
        ),
    ),
    (
        "src_jean_gielen_jr2025_cw_fr",
        "Companyweb FR ETA Jean Gielen Waremme YE2025 statutory",
        "https://www.companyweb.be/fr/0407850653/entreprise-de-travail-adapte-de-waremme-jean-gielen",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; FR mirror YE2025 Medium; déposés 26-06-2026; CA {OM25}; "
            f"Marge brute {BR25}; Bénéfice {PN25}; Capitaux propres {EQ25}; raw tick2241/"
        ),
    ),
    (
        "src_jean_gielen_kbo_2241",
        "KBO ETA Jean Gielen 0407.850.653 Actief ASBL 1 VE Waremme",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0407850653",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2241; Actief VZW/ASBL sinds 24.09.1970; ENTREPRISE DE TRAVAIL ADAPTE DE WAREMME "
            "JEAN GIELEN; afkorting ETA Jean GIELEN; Chaussée Romaine (War) 178 4300 Waremme; "
            "1 VE; RSZ/BTW NACE 88.993; Werkgever RSZ sinds 01.10.1970"
        ),
    ),
    (
        "src_jean_gielen_site_contact_2241",
        "ETA Jean Gielen FOI channel info@jeangielen.be via jeangielen.be",
        "https://jeangielen.be/",
        "ETA Jean Gielen ASBL",
        "foi_contact",
        (
            "tick2241; info@jeangielen.be (Facebook/public); +32 19 33 87 77; "
            "Chaussée Romaine 178 4300 Waremme; AViQ-agréé Walloon ETA food packaging"
        ),
    ),
]:
    upsert(
        sources,
        "source_id",
        sid,
        {
            "source_id": sid,
            "title": title,
            "url": url,
            "publisher": publisher,
            "accessed_date": "2026-08-27",
            "source_class": sclass,
            "notes": notes,
        },
    )
write_csv("sources.csv", s_fields, sources)

e_fields, entities = read_csv("entities.csv")
upsert(
    entities,
    "entity_id",
    ENTITY,
    {
        "entity_id": ENTITY,
        "name_nl": "ETA Jean Gielen VZW (Waremme / Walloon ETA maatwerk)",
        "name_fr": "ETA Jean Gielen ASBL (Waremme / entreprise de travail adapté)",
        "name_en": "ETA Jean Gielen adapted-work ASBL (Waremme Walloon ETA)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://jeangielen.be/",
        "foi_email": "info@jeangielen.be",
        "foi_postal": "Chaussée Romaine (War) 178, 4300 Waremme",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0407.850.653 Actief 1 VE "
            f"NACE 88.993; omzet JUMP {OM25} (+17.12%) bruto DROP {BR25} (~{RATIO}x) pnl JUMP "
            f"{PN25} equity JUMP {EQ25} (+{EQ_JUMP_PCT}%) FTE JUMP {FTE25}; neerlegging "
            f"26.06.2026; assets/debt Unknown; FOI {GAP}; preferred stalls AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; Heropbeuring CW opaque; after Axedis@2240; do NOT redo "
            "Axedis/Manufast/Metalgroup/EntrAnam/Enghien/Entra/ETA123; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_jean_gielen_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025 (primary envelope)",
        f"tick{TICK}; Medium CW; bruto DROP -2.27% vs YE2024 {BR24}; bruto≫omzet ~{RATIO}x",
    ),
    (
        "bud_jean_gielen_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +17.12% vs YE2024 {OM24}",
    ),
    (
        "bud_jean_gielen_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl JUMP +8.11% vs YE2024 {PN24}",
    ),
    (
        "bud_jean_gielen_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +{EQ_JUMP_PCT}% vs YE2024 {EQ24}",
    ),
    (
        "bud_jean_gielen_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 157.6",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_jean_gielen_equity_jr2024_statutory_cmp",
        "2024",
        EQ24,
        "CW statutory eigen_vermogen YE2024 comparative",
        f"tick{TICK}; YE2024 equity {EQ24} comparative (pre JUMP +{EQ_JUMP_PCT}%)",
    ),
]:
    upsert(
        budgets,
        "budget_id",
        bid,
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": year,
            "amount_eur": str(amt),
            "amount_min_eur": str(amt),
            "amount_max_eur": str(amt),
            "basis": basis,
            "source_id": "src_jean_gielen_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_bruto":{BR25},"2025_omzet":{OM25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_bruto":{BR24},"2024_omzet":{OM24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            f"ETA Jean Gielen YE2025 leftover dual (bruto 5.95m / bruto≫omzet ~{RATIO}x / "
            f"equity JUMP +{EQ_JUMP_PCT:.0f}% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": "ETA workers Waremme (Liège) / AViQ adapted-work public path",
        "legal_basis": (
            "ASBL ETA Jean Gielen (KBO 0407.850.653; Actief; 1 VE; NACE 88.993; Walloon AViQ)"
        ),
        "decision_date": "2026-06-26",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(BR25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": (
            "https://www.companyweb.be/en/0407850653/entreprise-de-travail-adapte-de-waremme-jean-gielen"
        ),
        "stated_goal": (
            "Walloon ETA food manufacturing/packaging + electrical subcontracting Waremme"
        ),
        "cut_option": (
            f"Publish NBB PDF assets/debt FOI; explain equity JUMP +{EQ_JUMP_PCT}% with "
            f"bruto DROP -2.27%; disclose AViQ ETA subsidy matrix behind bruto {BR25}"
        ),
        "source_id": "src_jean_gielen_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Liege>Waremme>JeanGielen>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; bruto primary envelope {BR25}; bruto≫omzet ~{RATIO}x; "
            f"equity JUMP +{EQ_JUMP_PCT}%; omzet JUMP +17.12%; FTE JUMP {FTE25}; 1 VE; after "
            "Axedis@2240; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; "
            "not TE-additive"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

# priority_index ≈ 0.55*5.4 + 0.35*6.6 + 0.10*7 = 2.97 + 2.31 + 0.7 = 5.98 → 6.00
l_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            f"ETA Jean Gielen bruto 5.95m / equity JUMP +{EQ_JUMP_PCT:.0f}% / omzet JUMP +17% "
            "(YE2025 Waremme ETA)"
        ),
        "level": "L5",
        "type": "eta_vzw_statutory",
        "hierarchy_path": "Wallonie>Liege>Waremme>JeanGielen>JR2025",
        "annual_cost_eur": str(BR25),
        "total_cost_eur": str(BR25),
        "tco_notes": (
            f"CW bruto {BR25} / omzet JUMP {OM25} (~{RATIO}x) / pnl JUMP {PN25} / equity JUMP "
            f"{EQ25} (+{EQ_JUMP_PCT}%) / FTE JUMP {FTE25} / 1 VE Waremme ETA"
        ),
        "confidence": "medium",
        "source_id": "src_jean_gielen_jr2025_cw_en",
        "beneficiaries": "ETA workers Waremme / AViQ adapted-work public path",
        "stated_goal": "Walloon ETA food packaging / electrical subcontracting",
        "measured_outcome": (
            f"omzet JUMP +17.12%; bruto≫omzet ~{RATIO}x (bruto DROP -2.27%); pnl JUMP +8.11%; "
            f"equity JUMP +{EQ_JUMP_PCT}%; FTE JUMP {FTE25}; filed 26.06.2026"
        ),
        "absurdity_score": "6.6",
        "cost_score": "5.4",
        "difficulty": "3.0",
        "priority_index": "6.00",
        "cut_proposal": (
            f"Publish NBB PDF assets/debt/cash FOI; disclose equity JUMP +{EQ_JUMP_PCT}% vs "
            f"bruto DROP; AViQ ETA subsidy matrix behind bruto {BR25}"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024 / "
            "AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after Axedis@2240; next every-10 2250"
        ),
    },
)
write_csv("leaderboard.csv", l_fields, leaderboard)

f_fields, foi = read_csv("foi_queue.csv")
upsert(
    foi,
    "gap_id",
    GAP,
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Wallonie>Liege>Waremme>JeanGielen>NBB_PDF_assets_debt_equity_jump_54pct"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); equity JUMP "
            f"EUR{EQ25} (+{EQ_JUMP_PCT}% from EUR{EQ24}) with bruto DROP EUR{BR25}; "
            f"AViQ ETA subsidy matrix behind bruto {BR25}; omzet JUMP {OM25}"
        ),
        "why_it_matters": (
            f"Medium CW shows Walloon ETA ASBL (bruto 5.95m / omzet 4.92m / equity JUMP "
            f"+{EQ_JUMP_PCT}% / FTE {FTE25}) under AViQ path; assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "ETA Jean Gielen ASBL",
        "recipient_email": "info@jeangielen.be",
        "recipient_postal": "Chaussée Romaine (War) 178, 4300 Waremme",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-27",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/"
            "REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; next every-10 2250"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — ETA Jean Gielen (NBB PDF / equity JUMP +{EQ_JUMP_PCT}% / bruto DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** ETA Jean Gielen ASBL — KBO **0407.850.653** (Actief; Chaussée Romaine 178, 4300 Waremme; **1 VE**; FTE {FTE25} CW; NACE **88.993**; Walloon Liège ETA)  
**recipient:** info@jeangielen.be · Chaussée Romaine (War) 178, 4300 Waremme  
**sources:** [CW EN](https://www.companyweb.be/en/0407850653/entreprise-de-travail-adapte-de-waremme-jean-gielen) · [CW NL](https://www.companyweb.be/nl/0407850653/entreprise-de-travail-adapte-de-waremme-jean-gielen) · [CW FR](https://www.companyweb.be/fr/0407850653/entreprise-de-travail-adapte-de-waremme-jean-gielen) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407850653) · [site](https://jeangielen.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW/ASBL; **1 VE**; zetel Chaussée Romaine Waremme; NACE **88.993**.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +17.12% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** DROP -2.27% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25:,}** JUMP +8.11%; equity **EUR{EQ25:,}** JUMP +{EQ_JUMP_PCT}% vs YE2024 EUR{EQ24:,}; FTE **{FTE25}** JUMP vs {FTE24}; filed **26.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Axedis@2240.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: ETA Jean Gielen ASBL
via info@jeangielen.be
Chaussée Romaine 178, 4300 Waremme
Objet: Publicité des comptes annuels 2025 ETA Jean Gielen (BCE 0407.850.653)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BR25} (DROP -2.27%) vs chiffre d'affaires EUR{OM25} (~{RATIO}x).
3. Equity JUMP EUR{EQ25} (+{EQ_JUMP_PCT}% vs YE2024 EUR{EQ24}) — réconciliation avec bruto DROP.
4. Matrice des subsides AVIQ / ETA derrière la marge brute EUR{BR25}.
5. Répartition activités agroalimentaire / conditionnement / sous-traitance électrique.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

# --- research_queue: close rq_2241, spawn rq_2242 ---
rq_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2241",
    {
        "task_id": "rq_2241",
        "title": (
            f"leftover dual ETA Jean Gielen YE2025 Medium (bruto 5.95m / equity JUMP "
            f"+{EQ_JUMP_PCT:.0f}% / omzet JUMP +17%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "leftover dual after Axedis YE2025. Prefer AGB/FARO-YE2025/AIESH-REW/Heropbeuring "
            "if live; else unused ETA-VAPH-WZC-maatwerk. Took FREE Jean Gielen Waremme YE2025."
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-27T02:05:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Jean Gielen 0407.850.653 YE2025 Medium CW; bruto {BR25} (~{RATIO}x) "
            f"omzet JUMP {OM25} equity JUMP {EQ25} (+{EQ_JUMP_PCT}%) pnl JUMP {PN25} FTE "
            f"{FTE25}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW "
            "opaque; after Axedis@2240; next rq_2242; next EVERY-10 2250; do NOT redo "
            "Axedis/Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers/Rekreatief/ETA123/JeanGielen"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2242",
    {
        "task_id": "rq_2242",
        "title": (
            "leftover dual after Jean Gielen - prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused ETA-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after Jean Gielen YE2025 Medium (bruto 5.95m / equity JUMP +54% / "
            "omzet JUMP +17%). Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE "
            "NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW euros live, else "
            "unused ETA/VAPH/WZC/maatwerk (e.g. Le Perron / IN-Z Genk / other FREE Walloon ETA). "
            "Do NOT redo Jean Gielen, Axedis, Manufast, Metalgroup, EntrAnam, Enghien, Entra, "
            "Ateliers de Tertre, Le Rucher, Het Rekreatief, Travie, SDB, De Vleugels, Kiemkracht, "
            "De Oever, ViTeS*, Kringwinkel*, Manus*, Reset, Den Azalee, Kemphaan, ETA 123. "
            "Next EVERY-10: 2250."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"spawned after tick{TICK} Jean Gielen; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; next every-10 2250"
        ),
    },
)
write_csv("research_queue.csv", rq_fields, rq)

# --- loop_state ---
ls_fields, ls = read_csv("loop_state.csv")
upsert(
    ls,
    "state_id",
    "main",
    {
        "state_id": "main",
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2241",
        "ticks_completed": "2241",
        "paused": "no",
        "notes": (
            f"tick{TICK} leftover Jean Gielen 0407.850.653 Medium (bruto {BR25} ~{RATIO}x "
            f"omzet; equity JUMP {EQ25} +{EQ_JUMP_PCT}%; pnl JUMP {PN25}; FTE JUMP {FTE25}; "
            f"1 VE Waremme ETA); after Axedis@2240; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; next rq_2242; next EVERY-10 2250; continuous hole_fill"
        ),
    },
)
write_csv("loop_state.csv", ls_fields, ls)

log_entry = f"""
### {UTC} - tick {TICK} - rq_2241 ETA Jean Gielen Waremme (bruto 5.95m / equity JUMP +{EQ_JUMP_PCT:.0f}% / Medium)

- Unit: **rq_2241** leftover dual after **rq_2240 Axedis**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took named FREE unused Walloon ETA **ETA Jean Gielen ASBL** YE2025 (KBO **0407.850.653**; Chaussée Romaine 178 Waremme; **Actief** **1 VE**; NACE **88.993** AViQ). Do not redo Axedis/Manufast/Metalgroup/EntrAnam/Enghien/Entra/ETA123 stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +17.12% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** DROP -2.27% (bruto≫omzet ~{RATIO}x); pnl **EUR{PN25}** JUMP +8.11% vs YE2024 EUR{PN24}; equity **EUR{EQ25}** JUMP +{EQ_JUMP_PCT}% vs YE2024 EUR{EQ24}; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **26.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via info@jeangielen.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.00); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2241=done + rq_2242 open; loop_state ticks=2241; raw docs/doge/raw/tick2241/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2240**; next **2250**). Next: rq_2242 (AGB/FARO-if-YE2025 / AIESH-REW / Le Perron-IN-Z-or-unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_entry)

print(f"tick{TICK} OK Jean Gielen bruto={BR25} equity={EQ25} (+{EQ_JUMP_PCT}%) ratio~{RATIO}x")
