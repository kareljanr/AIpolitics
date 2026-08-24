# -*- coding: utf-8 -*-
"""Tick 2240 EVERY-10 + ETA 123 Beauraing YE2025 leftover dual."""
import csv
import json
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
FOI = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-27T02:10:00Z"
TICK = 2240

ENTITY = "vzw_eta123_beauraing"
OMZET = 6827815
OMZET_PY = 5788729
BRUTO = 10297128
BRUTO_PY = 9725393
PNL = 941729
PNL_PY = 1781296
EQUITY = 10182232
EQUITY_PY = 9285250
FTE = 267.9
FTE_PY = 252.0
OMZET_PCT = round((OMZET - OMZET_PY) / OMZET_PY * 100, 2)  # +17.95
BRUTO_PCT = round((BRUTO - BRUTO_PY) / BRUTO_PY * 100, 2)  # +5.88
PNL_PCT = round((PNL - PNL_PY) / PNL_PY * 100, 2)  # -47.13
EQUITY_PCT = round((EQUITY - EQUITY_PY) / EQUITY_PY * 100, 2)  # +9.66
BRUTO_OMZET_X = round(BRUTO / OMZET, 2)  # ~1.51

SRC_EN = "src_eta123_jr2025_cw_en"
COMM = "comm_eta123_jr2025_statutory_eta_bruto_gt_omzet_pnl_drop_47pct"
LB = "lb_eta123_bruto_10_30m_gt_omzet_1_51x_pnl_drop_47pct_equity_jump_jr2025"
GAP = "gap_eta123_nbb_pdf_assets_debt_bruto_gt_omzet_1_51x_pnl_drop_47pct_eta_matrix_l5"

# cost_score <100m band → 5.5 (bruto 10.3m); abs 7.2 (bruto≫omzet + pnl DROP 47%); diff 3.0
# pi = 0.55*5.5 + 0.35*7.2 + 0.10*7.0 = 3.025 + 2.52 + 0.7 = 6.245 → 6.25
PI = "6.25"
ABS = "7.2"
COST = "5.5"
DIFF = "3.0"


def append_csv(path, rows):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    idkey = cols[0]
    have = {row[idkey] for row in existing}
    added = 0
    for row in rows:
        if row.get(idkey) in have:
            print("SKIP", path.name, row.get(idkey))
            continue
        existing.append({c: row.get(c, "") for c in cols})
        added += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
    print("append", path.name, "+", added, "total", len(existing))
    return len(existing)


def update_csv_rows(path, key, updates):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        cols = r.fieldnames
        rows = list(r)
    n = 0
    for row in rows:
        if row.get(key) in updates:
            row.update(updates[row[key]])
            n += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("update", path.name, n)


# race check
with (ROOT / "entities.csv").open(newline="", encoding="utf-8") as f:
    ents = list(csv.DictReader(f))
if any("0407.845.903" in str(e) or e.get("entity_id") == ENTITY for e in ents):
    raise SystemExit("RACE: ETA 123 Beauraing already in entities — abort")

# --- sources ---
n_src = append_csv(
    ROOT / "sources.csv",
    [
        dict(
            source_id="src_eta123_jr2025_cw_nl",
            title="Companyweb NL ETA 123 Beauraing YE2025 statutory",
            url="https://www.companyweb.be/nl/0407845903/eta-123-atelier-protege-de-beauraing",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-27",
            source_class="secondary_aggregator",
            notes=(
                f"tick2240 EVERY-10; YE2025 omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} "
                f"(+{BRUTO_PCT}%; ~{BRUTO_OMZET_X}x) pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} "
                f"(+{EQUITY_PCT}%) FTE JUMP {FTE}; neerlegging 17.06.2026; Groot; raw tick2240/"
            ),
        ),
        dict(
            source_id=SRC_EN,
            title="Companyweb EN ETA 123 Beauraing YE2025 statutory",
            url="https://www.companyweb.be/en/0407845903/eta-123-atelier-protege-de-beauraing",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-27",
            source_class="secondary_aggregator",
            notes=(
                f"tick2240; EN mirror YE2025 Medium; filed 17-06-2026; Last balance sheet year 2025; "
                f"Big; Turnover {OMZET}; Gross margin {BRUTO}; Profit/Loss {PNL}; Equity {EQUITY}; "
                f"Employees {FTE}; raw tick2240/"
            ),
        ),
        dict(
            source_id="src_eta123_jr2025_cw_fr",
            title="Companyweb FR ETA 123 Beauraing YE2025 statutory",
            url="https://www.companyweb.be/fr/0407845903/eta-123-atelier-protege-de-beauraing",
            publisher="Companyweb (NBB-derived)",
            accessed_date="2026-08-27",
            source_class="secondary_aggregator",
            notes=(
                f"tick2240; FR mirror YE2025 Medium; deposés 17-06-2026; CA {OMZET}; Marge brute "
                f"{BRUTO}; Benefice {PNL}; Capitaux propres {EQUITY}; raw tick2240/"
            ),
        ),
        dict(
            source_id="src_eta123_kbo_2240",
            title="KBO ETA 123 Beauraing 0407.845.903 Actief ASBL 1 VE",
            url="https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0407845903",
            publisher="KBO FOD Economie",
            accessed_date="2026-08-27",
            source_class="official_register",
            notes=(
                "tick2240; Actief VZW/ASBL sinds 21.10.1968; Entreprise de Travail adapté 123 - "
                "Atelier protégé de Beauraing; afkorting ETA 123; rue de Rochefort 201 5570 Beauraing; "
                "1 VE; RSZ NACE 88.993; BTW 16.281; Werkgever RSZ sinds 01.07.1970"
            ),
        ),
        dict(
            source_id="src_eta123_site_contact_2240",
            title="ETA 123 FOI channel secretariat@eta123.be via eta123.be",
            url="https://eta123.be/",
            publisher="ETA 123 - Atelier Protégé de Beauraing ASBL",
            accessed_date="2026-08-27",
            source_class="foi_contact",
            notes=(
                "tick2240; secretariat@eta123.be (Facebook/public); Route de Rochefort 201-203 "
                "5570 Beauraing; tel +32 82 71 19 72; AViQ-agréé Walloon ETA"
            ),
        ),
    ],
)

# --- budgets ---
budgets = []
for bid, year, amount, basis, notes in [
    (
        "bud_eta123_omzet_jr2025_statutory",
        "2025",
        OMZET,
        "CW statutory omzet / Turnover YE2025",
        f"tick2240; Medium CW; omzet JUMP +{OMZET_PCT}% vs YE2024 {OMZET_PY}",
    ),
    (
        "bud_eta123_bruto_jr2025_statutory",
        "2025",
        BRUTO,
        "CW statutory bruto_marge / Gross margin YE2025",
        f"tick2240; Medium CW; bruto JUMP +{BRUTO_PCT}% vs YE2024 {BRUTO_PY}; bruto≫omzet ~{BRUTO_OMZET_X}x",
    ),
    (
        "bud_eta123_pnl_jr2025_statutory",
        "2025",
        PNL,
        "CW statutory winst / Profit-Loss after tax YE2025",
        f"tick2240; Medium CW; pnl DROP {PNL_PCT}% vs YE2024 {PNL_PY}",
    ),
    (
        "bud_eta123_equity_jr2025_statutory",
        "2025",
        EQUITY,
        "CW statutory eigen_vermogen / Equity YE2025",
        f"tick2240; Medium CW; equity JUMP +{EQUITY_PCT}% vs YE2024 {EQUITY_PY}",
    ),
    (
        "bud_eta123_fte_jr2025_statutory",
        "2025",
        FTE,
        f"CW social-balance FTE / Employees {FTE}",
        f"tick2240; Medium CW; FTE JUMP vs YE2024 {FTE_PY}; assets/debt Unknown",
    ),
    (
        "bud_eta123_pnl_jr2024_statutory_cmp",
        "2024",
        PNL_PY,
        "CW statutory winst/verlies YE2024 comparative",
        f"tick2240; YE2024 pnl {PNL_PY} comparative for DROP calc",
    ),
]:
    budgets.append(
        dict(
            budget_id=bid,
            entity_id=ENTITY,
            year=year,
            amount_eur=str(amount),
            amount_min_eur=str(amount),
            amount_max_eur=str(amount),
            basis=basis,
            source_id=SRC_EN,
            confidence="medium",
            notes=notes,
        )
    )
n_bud = append_csv(ROOT / "budgets.csv", budgets)

n_comm = append_csv(
    ROOT / "commitments.csv",
    [
        dict(
            commitment_id=COMM,
            title=(
                f"ETA 123 Beauraing YE2025 leftover dual (bruto 10.30m / bruto≫omzet "
                f"~{BRUTO_OMZET_X}x / pnl DROP {PNL_PCT:.0f}% / Medium)"
            ),
            entity_id=ENTITY,
            beneficiary="ETA workers Beauraing (Namur) / AViQ adapted-work public path",
            legal_basis="ASBL ETA 123 (KBO 0407.845.903; Actief; 1 VE; NACE 88.993; Walloon AViQ)",
            decision_date="2026-06-17",
            start_year="2025",
            end_year="2025",
            total_envelope_eur=str(BRUTO),
            cash_by_year=json.dumps(
                {
                    "2025_omzet": OMZET,
                    "2025_bruto": BRUTO,
                    "2025_pnl": PNL,
                    "2025_equity": EQUITY,
                    "2025_fte": FTE,
                    "2024_omzet": OMZET_PY,
                    "2024_bruto": BRUTO_PY,
                    "2024_pnl": PNL_PY,
                    "2024_equity": EQUITY_PY,
                    "2024_fte": FTE_PY,
                },
                separators=(",", ":"),
            ),
            remaining_eur="0",
            status="active",
            evaluation_url="https://www.companyweb.be/en/0407845903/eta-123-atelier-protege-de-beauraing",
            stated_goal="Walloon ETA social workshop Beauraing (packaging/wood/outdoor/laundry)",
            cut_option=(
                f"Publish NBB PDF assets/debt FOI; explain bruto≫omzet ~{BRUTO_OMZET_X}x; "
                f"reconcile pnl DROP {PNL_PCT:.0f}% with equity JUMP +{EQUITY_PCT:.0f}% + AViQ matrix"
            ),
            source_id=SRC_EN,
            confidence="medium",
            hierarchy_path="Wallonie>Namur>Beauraing>ETA123>JR2025_statutory_L5",
            notes=(
                f"tick2240 EVERY-10; Medium CW; bruto primary envelope {BRUTO}; bruto≫omzet "
                f"~{BRUTO_OMZET_X}x; pnl DROP {PNL_PCT}%; equity JUMP +{EQUITY_PCT}%; FTE JUMP "
                f"{FTE}; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "after Manufast@2239; not TE-additive of 348bn"
            ),
        )
    ],
)

n_lb = append_csv(
    ROOT / "leaderboard.csv",
    [
        dict(
            item_id=LB,
            name=(
                f"ETA 123 bruto 10.30m / bruto≫omzet ~{BRUTO_OMZET_X}x / pnl DROP "
                f"{PNL_PCT:.0f}% / equity JUMP +{EQUITY_PCT:.0f}% (YE2025 Beauraing ETA)"
            ),
            level="L5",
            type="eta_vzw_statutory",
            hierarchy_path="Wallonie>Namur>Beauraing>ETA123>JR2025",
            annual_cost_eur=str(BRUTO),
            total_cost_eur=str(BRUTO),
            tco_notes=(
                f"CW bruto {BRUTO} / omzet {OMZET} (~{BRUTO_OMZET_X}x) / pnl DROP {PNL} "
                f"({PNL_PCT}% from {PNL_PY}) / equity JUMP {EQUITY} (+{EQUITY_PCT}%) / FTE {FTE}; "
                "Walloon AViQ ETA; assets/debt Unknown"
            ),
            confidence="medium",
            source_id=SRC_EN,
            beneficiaries="ETA workers Beauraing / AViQ adapted-work public path",
            stated_goal="Walloon ETA social workshop Beauraing",
            measured_outcome=(
                f"omzet JUMP +{OMZET_PCT}%; bruto≫omzet ~{BRUTO_OMZET_X}x; pnl DROP {PNL_PCT}%; "
                f"equity JUMP +{EQUITY_PCT}%; FTE JUMP {FTE_PY}->{FTE}"
            ),
            absurdity_score=ABS,
            cost_score=COST,
            difficulty=DIFF,
            priority_index=PI,
            cut_proposal=(
                f"Publish NBB PDF assets/debt/cash FOI; disclose bruto≫omzet ~{BRUTO_OMZET_X}x "
                f"vs AViQ ETA matrix; reconcile pnl DROP {PNL_PCT:.0f}% with equity JUMP"
            ),
            status="open",
            struck_reason="",
            notes=(
                f"tick2240 EVERY-10; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "AGB Bornem JR2024; after Manufast@2239"
            ),
        )
    ],
)

n_ent = append_csv(
    ROOT / "entities.csv",
    [
        dict(
            entity_id=ENTITY,
            name_nl="ETA 123 / Atelier protégé de Beauraing ASBL (Namur / Walloon ETA)",
            name_fr="ETA 123 - Atelier protégé de Beauraing ASBL (Namur / entreprise de travail adapté)",
            name_en="ETA 123 sheltered workshop Beauraing (Walloon AViQ adapted-work ASBL)",
            level="parastatal",
            parent_id="sec_wallonia",
            community_language="fr",
            website="https://eta123.be/",
            foi_email="secretariat@eta123.be",
            foi_postal="Route de Rochefort 201-203, 5570 Beauraing",
            notes=(
                f"tick2240 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0407.845.903 Actief "
                f"1 VE NACE 88.993; omzet JUMP {OMZET} (+{OMZET_PCT}%) bruto JUMP {BRUTO} "
                f"(+{BRUTO_PCT}%; ~{BRUTO_OMZET_X}x) pnl DROP {PNL} ({PNL_PCT}%) equity JUMP "
                f"{EQUITY} (+{EQUITY_PCT}%) FTE JUMP {FTE}; neerlegging 17.06.2026; assets/debt "
                f"Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "not TE-additive of 348bn"
            ),
        )
    ],
)

n_foi = append_csv(
    ROOT / "foi_queue.csv",
    [
        dict(
            gap_id=GAP,
            hierarchy_path=(
                "Wallonie>Namur>Beauraing>ETA123>"
                "NBB_PDF_assets_debt_bruto_gt_omzet_1_51x_pnl_drop_47pct"
            ),
            entity_id=ENTITY,
            what_is_missing=(
                f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); bruto EUR{BRUTO} vs "
                f"omzet EUR{OMZET} (~{BRUTO_OMZET_X}x); pnl DROP EUR{PNL} vs YE2024 EUR{PNL_PY} "
                f"({PNL_PCT}%) recon with equity JUMP EUR{EQUITY} (+{EQUITY_PCT}%); AViQ ETA "
                "subsidy matrix behind bruto"
            ),
            why_it_matters=(
                f"Medium CW shows Walloon ETA ASBL Beauraing (bruto 10.30m / omzet 6.83m / "
                f"~{BRUTO_OMZET_X}x / pnl DROP {PNL_PCT:.0f}% / equity JUMP / FTE {FTE}) under "
                "AViQ public path; assets/debt unpublished"
            ),
            priority="8",
            recipient_body="ETA 123 - Atelier Protégé de Beauraing ASBL",
            recipient_email="secretariat@eta123.be",
            recipient_postal="Route de Rochefort 201-203, 5570 Beauraing",
            draft_letter_path=f"docs/doge/foi/drafts/{GAP}.md",
            status="ready",
            date_ready="2026-08-27",
            date_sent="",
            date_due="",
            date_answered="",
            response_summary="",
            linked_commitment_id=COMM,
            linked_leaderboard_id=LB,
            created_utc=TS,
            updated_utc=TS,
            notes=(
                "tick2240 EVERY-10; ready NOT sent; Medium CW + Strong KBO; stall FARO/AIESH/REW "
                "YE2024; AGB Bornem JR2024; next every-10 2250"
            ),
        )
    ],
)

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(
    f"""# FOI draft — ETA 123 Beauraing (NBB PDF / bruto≫omzet ~{BRUTO_OMZET_X}x / pnl DROP {PNL_PCT:.0f}%)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** ETA 123 - Atelier protégé de Beauraing ASBL — KBO **0407.845.903** (Actief; Route de Rochefort 201-203, 5570 Beauraing; **1 VE**; FTE {FTE} CW; NACE **88.993**; Walloon AViQ ETA)  
**recipient:** secretariat@eta123.be · Route de Rochefort 201-203, 5570 Beauraing  
**sources:** [CW EN](https://www.companyweb.be/en/0407845903/eta-123-atelier-protege-de-beauraing) · [CW NL](https://www.companyweb.be/nl/0407845903/eta-123-atelier-protege-de-beauraing) · [CW FR](https://www.companyweb.be/fr/0407845903/eta-123-atelier-protege-de-beauraing) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407845903) · [site](https://eta123.be/)  
**tick:** 2240 (EVERY-10)  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL sinds 21.10.1968; **1 VE**; zetel rue de Rochefort 201 Beauraing; RSZ NACE **88.993**; BTW 16.281.
- CW YE2025: omzet **EUR{OMZET:,}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET_PY:,}; bruto **EUR{BRUTO:,}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{BRUTO_OMZET_X}x); pnl **EUR{PNL:,}** DROP {PNL_PCT}% vs YE2024 EUR{PNL_PY:,}; equity **EUR{EQUITY:,}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** JUMP vs {FTE_PY}; filed **17.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. After Manufast@2239.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
A: ETA 123 - Atelier Protégé de Beauraing ASBL
via secretariat@eta123.be
Route de Rochefort 201-203, 5570 Beauraing
Objet: Publicité des comptes annuels 2025 ETA 123 (BCE 0407.845.903)

Madame, Monsieur,

Sur la base du décret wallon relatif à la publicité de l'administration, je demande la communication de:

1. PDF BNB/CBSO des comptes YE2025 (bilan + résultats + annexe; actifs/dettes/cash).
2. Composition marge brute EUR{BRUTO} vs chiffre d'affaires EUR{OMZET} (~{BRUTO_OMZET_X}x).
3. PnL DROP EUR{PNL} vs bénéfice YE2024 EUR{PNL_PY} ({PNL_PCT}%) — réconciliation avec equity JUMP +{EQUITY_PCT}% et FTE JUMP.
4. Matrice des subsides AViQ / ETA derrière la marge brute EUR{BRUTO}.

Période YE2025 (+ comparative YE2024). Réf: {GAP}

Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées,
[Nom]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("FOI draft written")

update_csv_rows(
    ROOT / "research_queue.csv",
    "task_id",
    {
        "rq_2240": {
            "status": "done",
            "entity_id": ENTITY,
            "blocked_gap_id": GAP,
            "updated_utc": TS,
            "title": (
                f"EVERY-10 + leftover dual — ETA 123 Beauraing YE2025 Medium "
                f"(bruto 10.30m / ~{BRUTO_OMZET_X}x / pnl DROP {PNL_PCT:.0f}%)"
            ),
            "instructions": (
                "Completed EVERY-10@2240 + leftover ETA 123 Beauraing after Manufast; preferred "
                "AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; Medium CW YE2025 + Strong KBO; "
                "FOI ready not sent"
            ),
            "notes": (
                f"tick2240 EVERY-10 + ETA123 0407.845.903 Medium; omzet JUMP {OMZET} bruto JUMP "
                f"{BRUTO} (~{BRUTO_OMZET_X}x) pnl DROP {PNL} ({PNL_PCT}%) equity JUMP {EQUITY} "
                f"(+{EQUITY_PCT}%) FTE JUMP {FTE}; 1 VE Beauraing; FOI secretariat@eta123.be; "
                "next rq_2241; every-10 next 2250"
            ),
        }
    },
)

next_instructions = (
    "Leftover dual hole-fill after rq_2240 ETA 123 Beauraing YE2025 Medium (bruto 10.30m / "
    f"bruto≫omzet ~{BRUTO_OMZET_X}x / pnl DROP {PNL_PCT:.0f}% / equity JUMP). Prefer NON-stall "
    "live: AGB Bornem if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
    "else unused DSO/water/nuclear/IGS/HVZ/ETA/maatwerk/WZC with live sourced €. Do NOT redo "
    "ETA 123 Beauraing, Manufast, Metalgroup, EntrAnam, Enghien, Entra, Ateliers Tertre, "
    "Le Rucher, SDB, De Vleugels, Travie, Kiemkracht, De Oever, ViTeS, Manus stack, "
    "IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
    "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
    "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
    "Senes. Next EVERY-10 at 2250."
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2241",
            title=(
                "leftover dual hole-fill after ETA 123 Beauraing — prefer "
                "AGB/FARO-YE2025/AIESH-REW/unused DSO-water-nuclear-IGS-HVZ-ETA"
            ),
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=next_instructions,
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes=(
                "spawned after tick2240 EVERY-10 + ETA123 Beauraing; FARO/AIESH/REW still YE2024; "
                "AGB Bornem JR2024; Heropbeuring CW opaque; next EVERY-10 at 2250"
            ),
        )
    ],
)

with (ROOT / "loop_state.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("state_id") == "main":
        row["mode"] = "continuous"
        row["current_sprint"] = "hole_fill"
        row["last_tick_utc"] = TS
        row["last_unit_id"] = "rq_2240"
        row["ticks_completed"] = str(TICK)
        row["paused"] = "no"
        row["notes"] = (
            f"tick2240 EVERY-10 + leftover ETA123 Beauraing 0407.845.903 Medium "
            f"(bruto {BRUTO} ~{BRUTO_OMZET_X}x omzet {OMZET}; pnl DROP {PNL} {PNL_PCT}%; "
            f"equity JUMP {EQUITY} +{EQUITY_PCT}%; FTE JUMP {FTE}; 1 VE Beauraing); "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; after Manufast@2239; next rq_2241; "
            "next every-10 2250; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2240")

# inventory counts post-write
counts = {}
for fn in ["budgets.csv", "commitments.csv", "leaderboard.csv", "entities.csv", "sources.csv", "foi_queue.csv"]:
    with (ROOT / fn).open(newline="", encoding="utf-8") as f:
        counts[fn] = sum(1 for _ in csv.DictReader(f))
foi_ready = 0
foi_answered = 0
foi_partial = 0
with (ROOT / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        st = (row.get("status") or "").strip().lower()
        if st == "ready":
            foi_ready += 1
        elif st == "answered":
            foi_answered += 1
        elif st == "partial":
            foi_partial += 1

progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2240** (2026-08-27)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2231-2240 continuum; AGB Bornem / FARO / AIESH / REW still YE2024 stalls; Heropbeuring CW opaque |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2231-2240 is residual dual L5 (not near-complete of 348bn):** **De Vleugels** bruto **35.11m** ~**7.37×** · **SDB** omzet **9.36m** / PROFIT FLIP · **Le Rucher** bruto **7.62m** ~**2.03×** / LOSS FLIP · **Ateliers Tertre** omzet **10.00m** / pnl DROP **-97%** · **Entra** omzet **28.61m** / FTE **885** · **Enghien** bruto **4.63m** ~**1.96×** / equity JUMP **+77%** · **EntrAnam** bruto **7.66m** ~**1.83×** / LOSS DEEPEN · **Metalgroup** bruto **6.62m** ~**2.22×** / pnl DROP **-69%** · **Manufast** bruto **6.25m** ~**1.87×** / LOSS FLIP · **ETA 123 Beauraing** bruto **10.30m** ~**{BRUTO_OMZET_X}×** / pnl DROP **{PNL_PCT:.0f}%** (EVERY-10 primary) Medium |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_answered}**; partial **~{foi_partial}**; total FOI rows **~{counts['foi_queue.csv']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability/maatwerk shells** (**NEW 2231-2240** De Vleugels · SDB · Le Rucher · Ateliers Tertre · Entra · Enghien · EntrAnam · Metalgroup · Manufast · **ETA 123 Beauraing** · prior 2221-2230 Manus/Kringwinkel/Reset/ViTeS/Kiemkracht/Travie/De Oever stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2240)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {counts['budgets.csv']}+ |
| commitments.csv | {counts['commitments.csv']}+ |
| leaderboard.csv | {counts['leaderboard.csv']}+ |
| entities.csv | {counts['entities.csv']}+ |
| sources.csv | {counts['sources.csv']}+ |
| FOI ready | ~{foi_ready} |
| FOI answered | {foi_answered} |
| FOI partial | {foi_partial} |
| FOI total rows | ~{counts['foi_queue.csv']} |
| research_queue open | rq_2241 after EVERY-10 + ETA123 |

### What improved since tick 2230

- **Residual dual (tick2231-2240):** **De Vleugels** bruto **35.11m** ~**7.37×** · **SDB** omzet **9.36m** / PROFIT FLIP / equity JUMP **+57%** · **Le Rucher** bruto **7.62m** ~**2.03×** / LOSS FLIP · **Ateliers Tertre** omzet **10.00m** / pnl DROP **-97%** · **Entra** omzet **28.61m** / FTE **885** · **Enghien** bruto **4.63m** ~**1.96×** / equity JUMP **+77%** · **EntrAnam** bruto **7.66m** ~**1.83×** / LOSS DEEPEN · **Metalgroup** bruto **6.62m** ~**2.22×** / pnl DROP **-69%** · **Manufast** bruto **6.25m** ~**1.87×** / LOSS FLIP / equity DROP **-27%** · **ETA 123 Beauraing** (EVERY-10 primary — omzet JUMP **{OMZET/1e6:.2f}m** **+{OMZET_PCT}%**; bruto≫omzet **~{BRUTO_OMZET_X}x**; pnl DROP **{PNL_PCT}%**; equity JUMP **+{EQUITY_PCT}%**; FTE JUMP **{FTE}**; Medium CW; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024; narrative JV2025 only) · AIESH / REW YE2024-only · Heropbeuring CW kern opaque · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs FOI-ready.
"""
(ROOT / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")
print("progress_every_10_ticks.md refreshed")

top10 = f"""# DOGE waste ranking — current top 10

**As-of:** tick **2240** (2026-08-27) · **{counts['leaderboard.csv']}+** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 4 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |
| 9 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 10 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2231-2240:** **De Vleugels bruto 35.11m / ~7.37×** · **SDB omzet 9.36m / PROFIT FLIP** · **Le Rucher bruto 7.62m / ~2.03×** · **Ateliers Tertre omzet 10.00m / pnl DROP −97%** · **Entra omzet 28.61m / FTE 885** · **Enghien bruto 4.63m / equity JUMP +77%** · **EntrAnam bruto 7.66m / LOSS DEEPEN** · **Metalgroup bruto 6.62m / ~2.22×** · **Manufast bruto 6.25m / LOSS FLIP** · **ETA 123 Beauraing bruto 10.30m / ~{BRUTO_OMZET_X}× / pnl DROP {PNL_PCT:.0f}%** (EVERY-10@2240 primary) · prior 2221-2230 Manus/Kringwinkel/Reset/ViTeS/Kiemkracht/Travie/De Oever stack retained · Walloon HVZ opacity stack · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2230:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV snowball filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2231-2240 (off pure top10 / dual):** De Vleugels · SDB · Le Rucher · Ateliers Tertre · Entra · Enghien · EntrAnam · Metalgroup · Manufast · **ETA 123 Beauraing omzet JUMP 6.83m / bruto≫omzet ~{BRUTO_OMZET_X}x / pnl DROP {PNL_PCT:.0f}% / FTE JUMP {FTE}** (EVERY-10@2240 primary). Count NEW since 2230: ~10 residual dual fills. **Prior 2221-2230 + 2211-2220 stacks retained.** Not TE-additive of ~348bn.

### High-absurdity residual (not pure top10)

- **ETA 123 Beauraing** EVERY-10 primary bruto **EUR10.30m** / omzet **EUR6.83m** (~**{BRUTO_OMZET_X}×**) / pnl DROP **-47%** / equity JUMP **+{EQUITY_PCT}%** / FTE **{FTE}** — Walloon AViQ ETA subsidy opacity.
- **De Vleugels** bruto **EUR35.11m** / omzet **EUR4.77m** (~**7.37×**) / equity JUMP **EUR35.35m** / FTE **442.8** — VAPH disability dual.
- **Manufast** bruto **EUR6.25m** / omzet **EUR3.34m** (~**1.87×**) / pnl LOSS FLIP **-300k** / equity DROP **-27%**.
- **Metalgroup** bruto **EUR6.62m** / omzet **EUR2.99m** (~**2.22×**) / pnl DROP **-69%**.
- **EntrAnam** bruto **EUR7.66m** / omzet **EUR4.20m** (~**1.83×**) / LOSS DEEPEN.
- **Enghien** bruto **EUR4.63m** / ~**1.96×** / equity JUMP **+77%**.
- **Entra** omzet **EUR28.61m** / bruto **EUR35.33m** / FTE **885**.
- **Ateliers Tertre** omzet **EUR10.00m** / pnl DROP **-97%**.
- **Le Rucher** bruto **EUR7.62m** / ~**2.03×** / LOSS FLIP.
- **Travie** race dual bruto **EUR11.39m** / ~**2.84×** / pnl DROP **−89%** (prior retained).
- **Kiemkracht** omzet JUMP **EUR13.26m** / bruto≫omzet **~1.41x** / pnl DROP **-75%** (prior retained).
- **OptimaT** bruto **~3.54×** omzet / equity JUMP **EUR39.4m** (prior retained).
- Walloon **ZS** stack FTE-only budget opacity.
"""
(ROOT / "doge_waste_top10_current.md").write_text(top10, encoding="utf-8")
print("doge_waste_top10_current.md refreshed")

log_entry = f"""

### 2026-08-27T02:10:00Z — tick 2240 — rq_2240 EVERY-10 + ETA 123 Beauraing (bruto 10.30m / ~{BRUTO_OMZET_X}x / pnl DROP {PNL_PCT:.0f}% / Medium)

- Unit: **rq_2240** EVERY-10 mandatory + leftover dual after **rq_2239 Manufast**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**; Senes already mined. Took FREE unused Walloon ETA **ETA 123 / Atelier protégé de Beauraing ASBL** YE2025 (KBO **0407.845.903**; rue de Rochefort 201 Beauraing; **Actief** **1 VE**; NACE **88.993** AViQ). Do not redo Manufast/Metalgroup/EntrAnam/Enghien/Entra/Ateliers Tertre stack.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +{OMZET_PCT}% vs YE2024 EUR{OMZET_PY}; bruto **EUR{BRUTO}** JUMP +{BRUTO_PCT}% (bruto≫omzet ~{BRUTO_OMZET_X}x); pnl **EUR{PNL}** DROP {PNL_PCT}% vs YE2024 EUR{PNL_PY}; equity **EUR{EQUITY}** JUMP +{EQUITY_PCT}%; FTE **{FTE}** JUMP vs {FTE_PY}; neerlegging **17.06.2026**. Strong KBO Actief 1 VE. Assets/debt Unknown. Medium. FOI via secretariat@eta123.be.
- Wrote: EVERY-10 `progress_every_10_ticks.md` + `doge_waste_top10_current.md` (pure top10 stable); sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2240=done + rq_2241 open; loop_state ticks=2240; raw docs/doge/data/raw/tick2240/.
- FOI: **ready not sent** (human-gated).
- EVERY-10@**2240** done. Next: rq_2241 (AGB/FARO-if-YE2025 / AIESH-REW / unused). Next every-10 **2250**.
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_entry)
print("loop_log appended")
print("DONE tick2240", {"src": n_src, "bud": n_bud, "comm": n_comm, "lb": n_lb, "ent": n_ent, "foi": n_foi, "counts": counts, "foi_ready": foi_ready})
