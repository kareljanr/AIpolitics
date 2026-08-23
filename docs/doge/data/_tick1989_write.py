# ephemeral tick1989 — CHU Tivoli YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T00:40:00Z"
ENTITY = "vzw_chu_tivoli"
GAP = "gap_chu_tivoli_nbb_pdf_assets_debt_equity_jump_matrix_l5"
SRC = "src_chu_tivoli_jr2025_cw"
SRC_EN = "src_chu_tivoli_jr2025_cw_en"
SRC_KBO = "src_chu_tivoli_kbo_1989"
SRC_SITE = "src_chu_tivoli_site_1989"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1989")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL CHU Tivoli YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0401793202/centre-hospitalier-universitaire-de-tivoli-institut-medical-des-mutualites-socialistes",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1989; YE2025 omzet JUMP 252947458 pnl JUMP 4949133 equity JUMP 43135426 (+31pct) bruto JUMP 131470767 FTE 1588; neerlegging 10.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1989/tivoli_cw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CHU Tivoli YE2025 statutory",
        "url": "https://www.companyweb.be/en/0401793202/centre-hospitalier-universitaire-de-tivoli-institut-medical-des-mutualites-socialistes",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1989; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1989/tivoli_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CHU Tivoli 0401.793.202 Actief ASBL La Louviere",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0401793202",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1989; Actief ASBL; Avenue Max Buset 34 7100 La Louviere; no KBO email; Aanbestedende overheid; Mutualites socialistes medical institute",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "chu-tivoli.be La Louviere university hospital",
        "url": "https://www.chu-tivoli.be/",
        "publisher": "CHU Tivoli",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1989; Hainaut university hospital dual of HELORA/CHwapi/Epicura",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_chu_tivoli_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "252947458",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1989; omzet JUMP 252947458 +3.94pct vs YE2024 243356645",
    },
    {
        "budget_id": "bud_chu_tivoli_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "4949133",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1989; pnl JUMP 4949133 +7.31pct vs YE2024 4612157",
    },
    {
        "budget_id": "bud_chu_tivoli_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "43135426",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1989; equity JUMP 43135426 +31.16pct vs YE2024 32886828",
    },
    {
        "budget_id": "bud_chu_tivoli_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "131470767",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1989; bruto JUMP 131470767 +2.97pct vs YE2024 127672574",
    },
    {
        "budget_id": "bud_chu_tivoli_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "1588",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1989; YE2025 FTE 1588 vs YE2024 1557",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_chu_tivoli_jr2025_statutory_hospital",
    "title": "CHU Tivoli YE2025 leftover La Louviere university hospital dual (omzet JUMP 252.95m / equity JUMP 43.14m +31pct)",
    "entity_id": ENTITY,
    "beneficiary": "Hainaut/La Louviere patients / Mutualites socialistes dual",
    "legal_basis": "WVV ASBL / university hospital Wallonie",
    "decision_date": "2026-07-10",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "252947458",
    "cash_by_year": '{"2025_omzet":252947458,"2025_pnl":4949133,"2025_equity":43135426,"2025_bruto":131470767,"2025_fte":1588}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0401793202/centre-hospitalier-universitaire-de-tivoli-institut-medical-des-mutualites-socialistes",
    "stated_goal": "University hospital care La Louviere / Mutualites socialistes medical institute",
    "cut_option": "Publish NBB PDF assets/debt + equity JUMP +31pct recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Hainaut>LaLouviere>CHU_Tivoli>JR2025_statutory_L5",
    "notes": "tick1989; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHBA YE2025 deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_chu_tivoli_omzet_jump_252_95m_equity_jump_43_14m_jr2025",
    "name": "CHU Tivoli omzet JUMP 252.95m / equity JUMP 43.14m (+31pct) / pnl JUMP 4.95m (La Louviere university hospital YE2025)",
    "level": "L5",
    "type": "walloon_hospital_asbl_dual",
    "hierarchy_path": "Wallonie>Hainaut>LaLouviere>CHU_Tivoli>JR2025_statutory_L5",
    "annual_cost_eur": "252947458",
    "total_cost_eur": "43135426",
    "tco_notes": "statutory omzet JUMP 252947458 pnl JUMP 4949133 equity JUMP 43135426 (+31pct) bruto JUMP 131470767 FTE 1588; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "La Louviere / Hainaut patients via Mutualites socialistes university hospital",
    "stated_goal": "University hospital care network",
    "measured_outcome": "Medium CW YE2025; 253m omzet with equity JUMP +31pct; NBB PDF residual",
    "absurdity_score": "4.5",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "5.9",
    "cut_proposal": "Publish NBB PDF assets/debt + equity JUMP recon FOI; dual vs HELORA/CHwapi/Epicura hospital opacity",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1989 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 1990; CHBA deferred",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "CHU Tivoli (Centre hospitalier universitaire de Tivoli)",
    "name_fr": "CHU Tivoli (Centre hospitalier universitaire de Tivoli - Mutualites socialistes)",
    "name_en": "CHU Tivoli (La Louviere university hospital ASBL)",
    "level": "other",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://www.chu-tivoli.be/",
    "foi_email": "",
    "foi_postal": "Avenue Max Buset 34, 7100 La Louviere",
    "notes": "tick1989 YE2025 Medium CW NL+EN + Strong KBO 0401.793.202 Actief ASBL; omzet JUMP 252.95m pnl JUMP 4.95m equity JUMP 43.14m (+31pct) bruto JUMP 131.47m FTE 1588; assets/debt Unknown; neerlegging 10.07.2026; FOI gap_chu_tivoli_nbb_pdf_assets_debt_equity_jump_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHBA YE2025 deferred; do not redo Citadelle/ISoSL/CHU UCL Namur/Epicura/CHwapi/Vivalia/HELORA",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Hainaut>LaLouviere>CHU_Tivoli>NBB_PDF_assets_debt_equity",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); equity JUMP +31pct recon; dual vs HELORA/CHwapi/Epicura hospital path",
    "why_it_matters": "Medium CW shows 253m omzet university hospital with equity JUMP +31pct without balance sheet",
    "priority": "6",
    "recipient_body": "CHU Tivoli",
    "recipient_email": "",
    "recipient_postal": "https://www.chu-tivoli.be/",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_chu_tivoli_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_chu_tivoli_omzet_jump_252_95m_equity_jump_43_14m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1989; human-send only; Medium CW; KBO no email — route via chu-tivoli.be; next every-10 1990; CHBA deferred",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — CHU Tivoli (NBB PDF / assets-debt / equity JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** CHU Tivoli ASBL — KBO **0401.793.202**  
**recipient:** CHU Tivoli (KBO has no email; route via https://www.chu-tivoli.be/ contact)  
**sources:** [CW NL](https://www.companyweb.be/nl/0401793202/centre-hospitalier-universitaire-de-tivoli-institut-medical-des-mutualites-socialistes) · [CW EN](https://www.companyweb.be/en/0401793202/centre-hospitalier-universitaire-de-tivoli-institut-medical-des-mutualites-socialistes) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0401793202) · [site](https://www.chu-tivoli.be/)  
**tick:** 1989  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **10.07.2026**): omzet **EUR252,947,458** JUMP +3.94%; pnl **EUR4,949,133** JUMP +7.31%; equity **EUR43,135,426** JUMP **+31.16%**; bruto **EUR131,470,767** JUMP +2.97%; FTE **1588**; assets/debt **Unknown**.
- La Louviere university hospital (Mutualites socialistes). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. CHBA YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: CHU Tivoli — Avenue Max Buset 34, 7100 La Louviere
cc: SPW sante / Mutualites socialistes transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 CHU Tivoli + balans + equity JUMP recon (KBO 0401.793.202)
Geachte, op grond van decret wallon / CDLD / openbaarheid vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 10.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon equity JUMP (+31pct vs YE2024 32.89m).
4. Dual vs HELORA / CHwapi / Epicura indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

for x in qrows:
    if x.get("task_id") == "rq_1989":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after CHR Citadelle — CHU Tivoli YE2025 Medium"
        x["notes"] = "tick1989 CHU Tivoli Medium omzet JUMP 252.95m equity JUMP 43.14m +31pct; FOI ready; CHBA deferred; next rq_1990 EVERY-10; next every-10 1990"
        x["instructions"] = (
            "Completed leftover CHU Tivoli La Louviere university hospital YE2025 Medium CW; KBO 0401.793.202; "
            "omzet JUMP 252947458 pnl JUMP 4949133 equity JUMP 43135426 bruto JUMP 131470767 FTE 1588; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1990" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1990",
            "title": "EVERY-10 + leftover dual hole-fill after CHU Tivoli",
            "sprint": "hole_fill",
            "priority": "9",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 1989 after CHU Tivoli YE2025 Medium. MANDATORY every-10: refresh progress_every_10_ticks.md + doge_waste_top10_current.md THEN one leftover dual. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (CHBA if YE2025 / other). Do NOT redo CHU Tivoli, CHR Citadelle, ISoSL, CHU UCL Namur, Epicura, CHwapi, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, TIBI, IDELUX Environnement, IDELUX Eau, IDEA.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1989 CHU Tivoli; EVERY-10 at 1990; CHBA YE2025 deferred",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1989",
        "ticks_completed": "1989",
        "paused": "no",
        "notes": "tick1989 leftover CHU Tivoli 0401.793.202 Medium CW (omzet JUMP 252.95m pnl JUMP 4.95m equity JUMP 43.14m +31pct bruto JUMP 131.47m FTE 1588; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHBA deferred; next rq_1990 EVERY-10; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1989 - 2026-08-24T00:40:00Z - rq_1989 CHU Tivoli (omzet JUMP 252.95m / equity JUMP 43.14m +31pct / Medium)

- Unit: **rq_1989** leftover dual after **rq_1988 CHR Citadelle**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **CHU Tivoli** YE2025 (KBO **0401.793.202**; Avenue Max Buset 34 La Louviere; Hainaut **university hospital ASBL**). **CHBA** YE2025 also live deferred. Do not redo Citadelle/ISoSL/CHU UCL Namur/Epicura/CHwapi/Vivalia/HELORA/IDETA/SPI/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/IGRETEC/IPFBW/IDEA.
- Found: Companyweb NL+EN YE2025 - omzet **EUR252,947,458** JUMP +3.94%; pnl **EUR4,949,133** JUMP +7.31%; equity **EUR43,135,426** JUMP **+31.16%**; bruto **EUR131,470,767** JUMP +2.97%; FTE **1588**; neerlegging **10.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief ASBL; no KBO email.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_chu_tivoli); foi + draft gap_chu_tivoli_nbb_pdf_assets_debt_equity_jump_matrix_l5; rq_1989=done + rq_1990 open (EVERY-10); loop_state ticks=1989.
- FOI: **ready not sent** (human-gated; route via chu-tivoli.be).
- NOT every-10 (**next every-10 is 1990**). Next: rq_1990 (EVERY-10 progress + AGB/FARO-if-YE2025 / AIESH-REW / CHBA / unused DSO-IGS-HVZ).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1989" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1989")
