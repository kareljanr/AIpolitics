# ephemeral tick1987 — ISoSL YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T00:20:00Z"
ENTITY = "igs_isosl"
GAP = "gap_isosl_nbb_pdf_assets_debt_fte_jump_matrix_l5"
SRC = "src_isosl_jr2025_cw"
SRC_EN = "src_isosl_jr2025_cw_en"
SRC_KBO = "src_isosl_kbo_1987"
SRC_SITE = "src_isosl_site_1987"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_1987")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL ISoSL YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0250610881/intercommunale-de-soins-specialises-de-liege",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1987; YE2025 omzet JUMP 271492164 pnl JUMP turnaround 2759863 equity DROP 110347790 bruto JUMP 239106191 FTE JUMP 3892.7; neerlegging 27.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1987/isosl_cw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN ISoSL YE2025 statutory",
        "url": "https://www.companyweb.be/en/0250610881/intercommunale-de-soins-specialises-de-liege",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1987; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1987/isosl_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO ISoSL 0250.610.881 Actief CV Liege",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0250610881",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1987; Actief CV; Rue Basse-Wez 145 4020 Liege; email officiel.ic-isosl@isosl.be; 25 VE; Aanbestedende overheid; NACE 86.104 psychiatric",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "isosl.be Liege specialised care intercommunale",
        "url": "https://www.isosl.be/",
        "publisher": "ISoSL",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1987; Liege specialised psychiatric/geriatric care IGS dual of CHU Citadelle/Epicura",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_isosl_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "271492164",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1987; omzet JUMP 271492164 +3.38pct vs YE2024 262613807",
    },
    {
        "budget_id": "bud_isosl_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "2759863",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss turnaround",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1987; pnl JUMP turnaround 2759863 vs YE2024 LOSS -4282035",
    },
    {
        "budget_id": "bud_isosl_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "110347790",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1987; equity DROP 110347790 -3.16pct vs YE2024 113949197",
    },
    {
        "budget_id": "bud_isosl_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "239106191",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1987; bruto JUMP 239106191 +2.7pct vs YE2024 232813955",
    },
    {
        "budget_id": "bud_isosl_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "3892.7",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1987; YE2025 FTE JUMP 3892.7 vs YE2024 3465.8 (+426.9)",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_isosl_jr2025_statutory_hospital",
    "title": "ISoSL YE2025 leftover Liege specialised-care IGS dual (omzet JUMP 271.49m / pnl turnaround 2.76m / FTE JUMP 3892.7)",
    "entity_id": ENTITY,
    "beneficiary": "Liege specialised psychiatric/geriatric patients / communes dual",
    "legal_basis": "Code democratie locale intercommunale soins specialises CV",
    "decision_date": "2026-06-27",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "271492164",
    "cash_by_year": '{"2025_omzet":271492164,"2025_pnl":2759863,"2025_equity":110347790,"2025_bruto":239106191,"2025_fte":3892.7}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0250610881/intercommunale-de-soins-specialises-de-liege",
    "stated_goal": "Specialised psychiatric and geriatric care for Liege province",
    "cut_option": "Publish NBB PDF assets/debt + FTE JUMP +426 recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Liege>ISoSL>JR2025_statutory_L5",
    "notes": "tick1987; Medium CW; assets/debt Unknown; FTE JUMP standout; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_isosl_omzet_jump_271_49m_pnl_turnaround_2_76m_fte_jump_jr2025",
    "name": "ISoSL omzet JUMP 271.49m / pnl turnaround 2.76m / FTE JUMP 3892.7 (Liege specialised care YE2025)",
    "level": "L5",
    "type": "walloon_igs_hospital_specialised_dual",
    "hierarchy_path": "Wallonie>Liege>ISoSL>JR2025_statutory_L5",
    "annual_cost_eur": "271492164",
    "total_cost_eur": "110347790",
    "tco_notes": "statutory omzet JUMP 271492164 pnl JUMP turnaround 2759863 equity DROP 110347790 bruto JUMP 239106191 FTE JUMP 3892.7 (+427); assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Liege specialised-care patients via psychiatric/geriatric IGS",
    "stated_goal": "Specialised psychiatric and geriatric hospital care",
    "measured_outcome": "Medium CW YE2025; 271m omzet with pnl turnaround and FTE JUMP +427; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "6.075",
    "cut_proposal": "Publish NBB PDF assets/debt + FTE JUMP recon FOI; dual vs Citadelle/Epicura/CHU hospital opacity",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1987 leftover dual; Medium CW; TE-adjacent specialised-care flow not pure-waste top10; next every-10 1990",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "ISoSL (Intercommunale de Soins Specialises de Liege)",
    "name_fr": "ISoSL (Intercommunale de Soins Specialises de Liege)",
    "name_en": "ISoSL (Liege specialised psychiatric/geriatric care IGS)",
    "level": "intercommunale",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://www.isosl.be/",
    "foi_email": "officiel.ic-isosl@isosl.be",
    "foi_postal": "Rue Basse-Wez 145, 4020 Liege",
    "notes": "tick1987 YE2025 Medium CW NL+EN + Strong KBO 0250.610.881 Actief CV; omzet JUMP 271.49m pnl JUMP turnaround 2.76m equity DROP 110.35m bruto JUMP 239.11m FTE JUMP 3892.7; assets/debt Unknown; neerlegging 27.06.2026; 25 VE; FOI gap_isosl_nbb_pdf_assets_debt_fte_jump_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo CHU UCL Namur/Epicura/CHwapi/Vivalia/HELORA/IDETA/SPI",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Liege>ISoSL>NBB_PDF_assets_debt_fte",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); FTE JUMP +427 recon; dual vs Citadelle/Epicura/CHU hospital path",
    "why_it_matters": "Medium CW shows 271m omzet specialised-care IGS with FTE JUMP +427 and pnl turnaround without balance sheet",
    "priority": "7",
    "recipient_body": "ISoSL",
    "recipient_email": "officiel.ic-isosl@isosl.be",
    "recipient_postal": "https://www.isosl.be/",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_isosl_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_isosl_omzet_jump_271_49m_pnl_turnaround_2_76m_fte_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1987; human-send only; Medium CW; next every-10 1990",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — ISoSL (NBB PDF / assets-debt / FTE JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** ISoSL CV — KBO **0250.610.881**  
**recipient:** officiel.ic-isosl@isosl.be  
**sources:** [CW NL](https://www.companyweb.be/nl/0250610881/intercommunale-de-soins-specialises-de-liege) · [CW EN](https://www.companyweb.be/en/0250610881/intercommunale-de-soins-specialises-de-liege) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0250610881) · [site](https://www.isosl.be/)  
**tick:** 1987  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **27.06.2026**): omzet **EUR271,492,164** JUMP +3.38%; pnl **EUR2,759,863** JUMP turnaround (vs LOSS -4.28m); equity **EUR110,347,790** DROP -3.16%; bruto **EUR239,106,191** JUMP +2.7%; FTE **3892.7** JUMP (+426.9 vs 3465.8); assets/debt **Unknown**.
- Liege specialised psychiatric/geriatric care IGS. Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: ISoSL — officiel.ic-isosl@isosl.be
Rue Basse-Wez 145, 4020 Liege
cc: SPW sante / Province Liege transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 ISoSL + balans + FTE JUMP recon (KBO 0250.610.881)
Geachte, op grond van decret wallon / CDLD vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 27.06.2026).
2. Assets / schulden LT-ST / cash.
3. Recon FTE JUMP (+427 vs YE2024 3465.8).
4. Recon pnl turnaround (vs YE2024 LOSS -4.28m).
5. Dual vs Citadelle / Epicura / CHU indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

for x in qrows:
    if x.get("task_id") == "rq_1987":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after CHU UCL Namur — ISoSL YE2025 Medium"
        x["notes"] = "tick1987 ISoSL Medium omzet JUMP 271.49m pnl turnaround 2.76m FTE JUMP 3892.7; FOI ready; next rq_1988; next every-10 1990"
        x["instructions"] = (
            "Completed leftover ISoSL Liege specialised-care YE2025 Medium CW; KBO 0250.610.881; "
            "omzet JUMP 271492164 pnl JUMP turnaround 2759863 equity DROP 110347790 bruto JUMP 239106191 FTE JUMP 3892.7; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1988" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1988",
            "title": "leftover dual hole-fill after ISoSL",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 1987 after ISoSL YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Citadelle if YE2025 / other). Do NOT redo ISoSL, CHU UCL Namur, Epicura, CHwapi, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, TIBI, IDELUX Environnement, IDELUX Eau, IDEA.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1987 ISoSL; next every-10 1990",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1987",
        "ticks_completed": "1987",
        "paused": "no",
        "notes": "tick1987 leftover ISoSL 0250.610.881 Medium CW (omzet JUMP 271.49m pnl JUMP turnaround 2.76m equity DROP 110.35m bruto JUMP 239.11m FTE JUMP 3892.7; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1988; next every-10 1990; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1987 - 2026-08-24T00:20:00Z - rq_1987 ISoSL (omzet JUMP 271.49m / pnl turnaround 2.76m / FTE JUMP 3892.7 / Medium)

- Unit: **rq_1987** leftover dual after **rq_1986 CHU UCL Namur**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **ISoSL** YE2025 (KBO **0250.610.881**; Rue Basse-Wez 145 Liege; Liege **specialised psychiatric/geriatric IGS**). Do not redo CHU UCL Namur/Epicura/CHwapi/Vivalia/HELORA/IDETA/SPI/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/IGRETEC/IPFBW/IDEA.
- Found: Companyweb NL+EN YE2025 - omzet **EUR271,492,164** JUMP +3.38%; pnl **EUR2,759,863** JUMP turnaround (vs LOSS -4.28m); equity **EUR110,347,790** DROP -3.16%; bruto **EUR239,106,191** JUMP +2.7%; FTE **3892.7** JUMP (+426.9); neerlegging **27.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief CV 25 VE; email officiel.ic-isosl@isosl.be.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 igs_isosl); foi + draft gap_isosl_nbb_pdf_assets_debt_fte_jump_matrix_l5; rq_1987=done + rq_1988 open; loop_state ticks=1987.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1990**). Next: rq_1988 (AGB/FARO-if-YE2025 / AIESH-REW / Citadelle / unused DSO-IGS-HVZ-hospital).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1987" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1987")
