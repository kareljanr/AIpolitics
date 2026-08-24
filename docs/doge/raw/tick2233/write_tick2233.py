# tick2233 — Le Rucher YE2025 Medium leftover dual (named FREE after SDB)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_le_rucher_leuze"
TICK = "2233"
UTC = "2026-08-26T23:25:00Z"
GAP = "gap_le_rucher_nbb_pdf_assets_debt_pnl_loss_flip_bruto_gt_omzet_aviq_matrix_l5"
COMM = "comm_le_rucher_jr2025_statutory_eta_pnl_loss_flip_bruto_gt_omzet"
LB = "lb_le_rucher_omzet_3_75m_pnl_loss_flip_bruto_gt_omzet_jr2025"

OM25, OM24 = 3749862, 4292711
BR25, BR24 = 7621283, 7916121
PN25, PN24 = -193735, 34160
EQ25, EQ24 = 8786823, 9039068
FTE25, FTE24 = 245.6, 254.8


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


s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_le_rucher_jr2025_cw_nl",
        "Companyweb NL Le Rucher YE2025 statutory",
        "https://www.companyweb.be/nl/0860345458/le-rucher",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet DROP {OM25} (-12.65%) bruto DROP {BR25} (-3.72%; "
            f"bruto≫omzet ~2.03x) pnl LOSS FLIP {PN25} vs YE2024 profit {PN24} equity DROP "
            f"{EQ25} (-2.79%) FTE DROP {FTE25}; filed 25-06-2026"
        ),
    ),
    (
        "src_le_rucher_jr2025_cw_en",
        "Companyweb EN Le Rucher YE2025 statutory",
        "https://www.companyweb.be/en/0860345458/le-rucher",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 25-06-2026"
        ),
    ),
    (
        "src_le_rucher_jr2025_cw_fr",
        "Companyweb FR Le Rucher YE2025 statutory",
        "https://www.companyweb.be/fr/0860345458/le-rucher",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Perte {PN25}",
    ),
    (
        "src_le_rucher_kbo_2233",
        "KBO Le Rucher 0860.345.458 Actief Leuze-en-Hainaut 1 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0860345458",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2233; Actief VZW/ASBL Le Rucher; zetel Zone industrielle de l'Europe(L) 1 "
            "7900 Leuze-en-Hainaut; 1 VE Actief; NACE RSZ/BTW 88.993 beschutte/sociale "
            "werkplaatsen (ETA); AViQ path"
        ),
    ),
    (
        "src_le_rucher_site_contact_2233",
        "Le Rucher FOI channel contact@lerucher.be",
        "https://lerucher.be/",
        "Le Rucher ASBL",
        "foi_contact",
        "tick2233; contact@lerucher.be; 069/66 33 33; Zone de l'Europe II 1, 7900 Leuze-en-Hainaut",
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
            "accessed_date": "2026-08-26",
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
        "name_nl": "Le Rucher VZW / ETA (Leuze-en-Hainaut)",
        "name_fr": "Le Rucher ASBL / Entreprise de Travail Adapté (Leuze-en-Hainaut)",
        "name_en": "Le Rucher ASBL / Adapted work enterprise (Leuze-en-Hainaut)",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://lerucher.be/",
        "foi_email": "contact@lerucher.be",
        "foi_postal": "Zone industrielle de l'Europe(L) 1, 7900 Leuze-en-Hainaut",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0860.345.458 Actief 1 VE "
            f"NACE 88.993 ETA/AViQ; omzet DROP {OM25} bruto DROP {BR25} (~2.03x) pnl LOSS "
            f"FLIP {PN25} equity DROP {EQ25} FTE DROP {FTE25}; neerlegging 25.06.2026; "
            f"assets/debt Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW "
            "YE2024; Heropbeuring CW opaque; Travie race@2230 done; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_le_rucher_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet DROP -12.65% vs YE2024 {OM24}; primary envelope",
    ),
    (
        "bud_le_rucher_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto DROP -3.72% vs YE2024 {BR24}; bruto≫omzet ~2.03x",
    ),
    (
        "bud_le_rucher_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl LOSS FLIP vs YE2024 profit {PN24}",
    ),
    (
        "bud_le_rucher_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity DROP -2.79% vs YE2024 {EQ24}",
    ),
    (
        "bud_le_rucher_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 245.6",
        f"tick{TICK}; Medium CW; FTE DROP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_le_rucher_pnl_jr2024_statutory_cmp",
        "2024",
        PN24,
        "CW statutory winst/verlies YE2024 comparative (PROFIT)",
        f"tick{TICK}; YE2024 pnl PROFIT {PN24} comparative (pre LOSS FLIP)",
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
            "source_id": "src_le_rucher_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":{OM25},"2025_bruto":{BR25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_omzet":{OM24},"2024_bruto":{BR24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "Le Rucher YE2025 leftover dual (omzet DROP 3.75m / pnl LOSS FLIP -194k / "
            "bruto≫omzet ~2.03x / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "workers with disability Wallonie picarde (Leuze) / AViQ ETA public path"
        ),
        "legal_basis": (
            "ASBL Entreprise de Travail Adapté (KBO 0860.345.458; Actief; 1 VE; NACE 88.993)"
        ),
        "decision_date": "2026-06-25",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0860345458/le-rucher",
        "stated_goal": "Adapted work / socio-professional insertion for people with disability",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; reconcile pnl LOSS FLIP (+34k -> -194k) with "
            "omzet DROP -12.65% and FTE DROP; disclose AViQ/Wallonie ETA wage-cost subsidy "
            "matrix behind bruto≫omzet ~2.03x; equity DROP drivers"
        ),
        "source_id": "src_le_rucher_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>Leuze>LeRucher>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope {OM25}; bruto≫omzet ~2.03x; "
            f"pnl LOSS FLIP; FTE DROP {FTE25}; 1 VE; named FREE after SDB; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; Heropbeuring CW opaque; Travie race@2230 done; not TE-additive"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

l_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            "Le Rucher omzet DROP 3.75m / pnl LOSS FLIP -194k / bruto≫omzet ~2.03x "
            "(YE2025 ETA)"
        ),
        "level": "L5",
        "type": "eta_maatwerk_vzw_statutory",
        "hierarchy_path": "Wallonie>Hainaut>Leuze>LeRucher>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet DROP {OM25} / bruto {BR25} (~2.03x) / pnl LOSS FLIP {PN25} "
            f"(from profit {PN24}) / equity DROP {EQ25} / FTE DROP {FTE25} / 1 VE Leuze ETA AViQ"
        ),
        "confidence": "medium",
        "source_id": "src_le_rucher_jr2025_cw_en",
        "beneficiaries": "workers with disability Wallonie picarde / AViQ ETA path",
        "stated_goal": "Adapted work employment ETA",
        "measured_outcome": (
            f"omzet DROP -12.65%; bruto DROP -3.72% (~2.03x omzet); pnl LOSS FLIP "
            f"(+34k->-194k); equity DROP -2.79%; FTE DROP {FTE25} vs {FTE24}; filed 25.06.2026"
        ),
        "absurdity_score": "7.2",
        "cost_score": "4.8",
        "difficulty": "3.0",
        "priority_index": "6.30",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose AViQ/Wallonie ETA subsidy matrix "
            "behind bruto≫omzet ~2.03x; reconcile LOSS FLIP + omzet DROP + FTE DROP; "
            "dual unit-cost vs Travie/Waak maatwerk"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024 / "
            "AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after SDB@2232; Travie race@2230 "
            "done; next every-10 2240"
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
            "Wallonie>Hainaut>Leuze>LeRucher>NBB_PDF_assets_debt_pnl_loss_flip_bruto_gt_omzet_aviq"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); pnl LOSS FLIP "
            f"EUR{PN25} vs YE2024 profit EUR{PN24}; bruto EUR{BR25} ≫ omzet EUR{OM25} "
            f"(~2.03x) AViQ/Wallonie ETA wage-cost subsidy matrix; equity DROP EUR{EQ25}; "
            f"FTE DROP {FTE25} vs {FTE24} recon"
        ),
        "why_it_matters": (
            f"Medium CW shows Wallonie picarde ETA (omzet 3.75m / bruto 7.62m ~2.03x / "
            f"{FTE25} FTE / 1 VE) with pnl LOSS FLIP under AViQ adapted-work path; "
            "assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "Le Rucher ASBL / Entreprise de Travail Adapté",
        "recipient_email": "contact@lerucher.be",
        "recipient_postal": "Zone industrielle de l'Europe(L) 1, 7900 Leuze-en-Hainaut",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-26",
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
            "REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; Travie race@2230 done; "
            "next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — Le Rucher (NBB PDF / pnl LOSS FLIP / bruto≫omzet ~2.03x / AViQ ETA)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Le Rucher ASBL / ETA — KBO **0860.345.458** (Actief; Zone industrielle de l'Europe(L) 1, 7900 Leuze-en-Hainaut; **1 VE**; FTE {FTE25} CW; NACE **88.993**)  
**recipient:** contact@lerucher.be · Zone industrielle de l'Europe(L) 1, 7900 Leuze-en-Hainaut  
**sources:** [CW EN](https://www.companyweb.be/en/0860345458/le-rucher) · [CW NL](https://www.companyweb.be/nl/0860345458/le-rucher) · [CW FR](https://www.companyweb.be/fr/0860345458/le-rucher) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0860345458) · [site](https://lerucher.be/)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief ASBL; **1 VE**; zetel Leuze-en-Hainaut; NACE **88.993** ETA; contact@lerucher.be; lerucher.be.
- CW YE2025: omzet **EUR{OM25:,}** DROP -12.65% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** DROP -3.72% (bruto≫omzet ~2.03x); pnl **EUR{PN25:,}** LOSS FLIP vs YE2024 profit EUR{PN24:,}; equity **EUR{EQ25:,}** DROP -2.79%; FTE **{FTE25}**; filed **25.06.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. Travie race@2230 already done.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Le Rucher ASBL / Entreprise de Travail Adapté
via contact@lerucher.be
Zone industrielle de l'Europe(L) 1, 7900 Leuze-en-Hainaut
Betreft: Openbaarheid / Transparence — jaarrekening 2025 Le Rucher (KBO 0860.345.458)

Geachte / Madame, Monsieur,

Op grond van het Waals Decreet openbaarheid van bestuur / Code de la démocratie locale vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (bilan + résultats + annexes; assets/debt/cash).
2. PnL LOSS FLIP EUR{PN25} vs YE2024 winst EUR{PN24} — reconciliatie met omzet DROP -12,65% en FTE DROP naar {FTE25}.
3. Brutomarge EUR{BR25} ≫ omzet EUR{OM25} (~2,03x) — AViQ/Wallonie ETA loonkostsubsidie-matrix.
4. Eigen vermogen DROP EUR{EQ25} (−2,79%) — drivers.
5. Eventuele related-party / EWETA-federatie cost allocation.

Période YE2025 (+ YE2024 comparative). Ref: {GAP}

Met vriendelijke groeten / Cordialement,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2233",
    {
        "task_id": "rq_2233",
        "title": (
            "leftover dual — Le Rucher YE2025 Medium (omzet DROP 3.75m / pnl LOSS FLIP / "
            "bruto≫omzet ~2.03x)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "leftover dual after SDB; prefer AGB/FARO/AIESH/REW else named FREE Le Rucher"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T23:05:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; Le Rucher 0860.345.458 YE2025 Medium CW; omzet DROP {OM25} bruto "
            f"DROP {BR25} (~2.03x) pnl LOSS FLIP {PN25} equity DROP {EQ25} FTE DROP {FTE25}; "
            "1 VE Leuze ETA AViQ; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW "
            "opaque; Travie race@2230 done; next rq_2234; every-10 next 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2234",
    {
        "task_id": "rq_2234",
        "title": (
            "leftover dual hole-fill after Le Rucher — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-unused-VAPH-WZC-maatwerk"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after Le Rucher Leuze YE2025 Medium (omzet DROP 3.75m / pnl LOSS "
            "FLIP / bruto≫omzet ~2.03x). Prefer leftover AGB/APB if JR2025 PDF live, else "
            "FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if NBB/CW "
            "euros live, else unused VAPH-WZC-maatwerk/kringloop/IGS/HVZ with live sourced €. "
            "Do NOT redo Le Rucher, SDB, Travie, De Vleugels, Kiemkracht, De Oever, ViTeS BE, "
            "Kringwinkel Midwest, ViTeS, Reset, Den Azalee, Kringwinkel West, Manus BXL, "
            "Manus VZW groep, Manus Antwerpen, Kringwinkel Maasland, Kringwinkel ZOV, NBSW, "
            "Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, Kringloopwinkel Deltagroep, "
            "Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, Werkhuizen Min, ACG, "
            "Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, "
            "De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, Atelier Groot "
            "Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, "
            "SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel Antwerpen, Blankedale, Mirto, "
            "Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, "
            "MAAAT, WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, "
            "Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter "
            "(YE2024), Aralea (YE2024), IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, "
            "Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
            "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
            "Next EVERY-10: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2233 Le Rucher; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; Travie+Rucher done; prefer unused VAPH-WZC-maatwerk"
        ),
    },
)
write_csv("research_queue.csv", r_fields, rq)

ls_fields, ls = read_csv("loop_state.csv")
ls[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_2233",
    "ticks_completed": "2233",
    "paused": "no",
    "notes": (
        f"tick2233 leftover Le Rucher 0860.345.458 Medium (omzet DROP {OM25}; bruto DROP "
        f"{BR25} ~2.03x; pnl LOSS FLIP {PN25}; equity DROP {EQ25}; FTE DROP {FTE25}; 1 VE "
        "Leuze ETA AViQ); after SDB@2232; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        "Heropbeuring CW opaque; Travie race@2230 done; next rq_2234; next every-10 2240; "
        "continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2233 - 2026-08-26T23:25:00Z - rq_2233 Le Rucher Leuze (omzet DROP 3.75m / pnl LOSS FLIP / bruto≫omzet ~2.03x / Medium)

- Unit: **rq_2233** leftover dual after **rq_2232 SDB**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Travie race@2230 already done; Waak/Stroom/Stijn already mapped. Took named FREE leftover **Le Rucher ASBL / ETA** YE2025 (KBO **0860.345.458**; Zone industrielle de l'Europe(L) 1 Leuze-en-Hainaut; **Actief** **1 VE**; NACE **88.993** AViQ ETA) — named prefer in rq_2233. Do not redo SDB/Travie/De Vleugels/Kiemkracht/De Oever/ViTeS/Waak stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** DROP -12.65% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** DROP -3.72% (bruto≫omzet ~2.03x); pnl **EUR{PN25}** LOSS FLIP vs YE2024 profit EUR{PN24}; equity **EUR{EQ25}** DROP -2.79%; FTE **{FTE25}** DROP vs {FTE24}; neerlegging **25.06.2026**. Strong KBO Actief 1 VE; contact@lerucher.be. Assets/debt Unknown. Medium. FOI via contact@lerucher.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.30); entities (+1 vzw_le_rucher_leuze); foi + draft {GAP}; rq_2233=done + rq_2234 open; loop_state ticks=2233; raw docs/doge/raw/tick2233/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240**). Next: rq_2234 (AGB/FARO-if-YE2025 / AIESH-REW / unused-VAPH-WZC-maatwerk).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2233 LeRucher omzet={OM25} bruto={BR25} pnl={PN25} equity={EQ25} FTE={FTE25}"
)
