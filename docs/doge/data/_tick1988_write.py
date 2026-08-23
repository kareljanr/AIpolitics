# ephemeral tick1988 — CHR Citadelle YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T00:30:00Z"
ENTITY = "igs_chr_citadelle"
GAP = "gap_citadelle_nbb_pdf_assets_debt_equity_jump_matrix_l5"
SRC = "src_citadelle_jr2025_cw"
SRC_EN = "src_citadelle_jr2025_cw_en"
SRC_KBO = "src_citadelle_kbo_1988"
SRC_SITE = "src_citadelle_site_1988"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1988")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL CHR Citadelle YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0237086311/centre-hospitalier-regional-de-la-citadelle",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1988; YE2025 omzet JUMP 593959237 pnl DROP 2232230 equity JUMP 81050938 (+68pct) bruto JUMP 283029421 FTE 3235; neerlegging 02.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1988/citadelle_cw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN CHR Citadelle YE2025 statutory",
        "url": "https://www.companyweb.be/en/0237086311/centre-hospitalier-regional-de-la-citadelle",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1988; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1988/citadelle_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO CHR Citadelle 0237.086.311 Actief CV Liege",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0237086311",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1988; Actief CV; Bld du Douzieme-de-Ligne 1 4000 Liege; email officiel.ic-chrcitadelle@chrcitadelle.be; Aanbestedende overheid; NACE 86.101",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "chrcitadelle.be Liege regional hospital",
        "url": "https://www.chrcitadelle.be/",
        "publisher": "CHR Citadelle",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1988; Liege regional hospital dual of ISoSL/Epicura/CHU",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_citadelle_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "593959237",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1988; omzet JUMP 593959237 +6.69pct vs YE2024 556722532",
    },
    {
        "budget_id": "bud_citadelle_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "2232230",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1988; pnl DROP 2232230 -73.58pct vs YE2024 8448674",
    },
    {
        "budget_id": "bud_citadelle_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "81050938",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1988; equity JUMP 81050938 +68.29pct vs YE2024 48160146",
    },
    {
        "budget_id": "bud_citadelle_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "283029421",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1988; bruto JUMP 283029421 +5.1pct vs YE2024 269286915",
    },
    {
        "budget_id": "bud_citadelle_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "3235",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1988; YE2025 FTE 3235 vs YE2024 3209",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_citadelle_jr2025_statutory_hospital",
    "title": "CHR Citadelle YE2025 leftover Liege regional hospital dual (omzet JUMP 593.96m / equity JUMP 81.05m +68pct)",
    "entity_id": ENTITY,
    "beneficiary": "Liege patients / communes dual",
    "legal_basis": "Code democratie locale intercommunale hospitaliere CV",
    "decision_date": "2026-07-02",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "593959237",
    "cash_by_year": '{"2025_omzet":593959237,"2025_pnl":2232230,"2025_equity":81050938,"2025_bruto":283029421,"2025_fte":3235}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0237086311/centre-hospitalier-regional-de-la-citadelle",
    "stated_goal": "Regional general hospital care for Liege",
    "cut_option": "Publish NBB PDF assets/debt + equity JUMP +68pct recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Liege>CHR_Citadelle>JR2025_statutory_L5",
    "notes": "tick1988; Medium CW; assets/debt Unknown; equity JUMP standout; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_citadelle_omzet_jump_593_96m_equity_jump_81_05m_jr2025",
    "name": "CHR Citadelle omzet JUMP 593.96m / equity JUMP 81.05m (+68pct) / pnl DROP 2.23m (Liege regional hospital YE2025)",
    "level": "L5",
    "type": "walloon_igs_hospital_dual",
    "hierarchy_path": "Wallonie>Liege>CHR_Citadelle>JR2025_statutory_L5",
    "annual_cost_eur": "593959237",
    "total_cost_eur": "81050938",
    "tco_notes": "statutory omzet JUMP 593959237 pnl DROP 2232230 equity JUMP 81050938 (+68pct) bruto JUMP 283029421 FTE 3235; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Liege patients via regional hospital IGS",
    "stated_goal": "Regional general hospital care",
    "measured_outcome": "Medium CW YE2025; 594m omzet with equity JUMP +68pct and pnl DROP; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "6.25",
    "cut_proposal": "Publish NBB PDF assets/debt + equity JUMP +68pct recon FOI; dual vs ISoSL/Epicura/CHU hospital opacity",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1988 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 1990",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "CHR Citadelle (Centre Hospitalier Regional de la Citadelle)",
    "name_fr": "CHR Citadelle (Centre Hospitalier Regional de la Citadelle)",
    "name_en": "CHR Citadelle (Liege regional hospital IGS)",
    "level": "intercommunale",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://www.chrcitadelle.be/",
    "foi_email": "officiel.ic-chrcitadelle@chrcitadelle.be",
    "foi_postal": "Bld du Douzieme-de-Ligne 1, 4000 Liege",
    "notes": "tick1988 YE2025 Medium CW NL+EN + Strong KBO 0237.086.311 Actief CV; omzet JUMP 593.96m pnl DROP 2.23m equity JUMP 81.05m (+68pct) bruto JUMP 283.03m FTE 3235; assets/debt Unknown; neerlegging 02.07.2026; FOI gap_citadelle_nbb_pdf_assets_debt_equity_jump_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo ISoSL/CHU UCL Namur/Epicura/CHwapi/Vivalia/HELORA",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Liege>CHR_Citadelle>NBB_PDF_assets_debt_equity",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); equity JUMP +68pct recon; dual vs ISoSL/Epicura/CHU hospital path",
    "why_it_matters": "Medium CW shows 594m omzet regional hospital with equity JUMP +68pct and pnl DROP without balance sheet",
    "priority": "7",
    "recipient_body": "CHR Citadelle",
    "recipient_email": "officiel.ic-chrcitadelle@chrcitadelle.be",
    "recipient_postal": "https://www.chrcitadelle.be/",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_citadelle_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_citadelle_omzet_jump_593_96m_equity_jump_81_05m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1988; human-send only; Medium CW; next every-10 1990",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — CHR Citadelle (NBB PDF / assets-debt / equity JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** CHR Citadelle CV — KBO **0237.086.311**  
**recipient:** officiel.ic-chrcitadelle@chrcitadelle.be  
**sources:** [CW NL](https://www.companyweb.be/nl/0237086311/centre-hospitalier-regional-de-la-citadelle) · [CW EN](https://www.companyweb.be/en/0237086311/centre-hospitalier-regional-de-la-citadelle) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0237086311) · [site](https://www.chrcitadelle.be/)  
**tick:** 1988  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **02.07.2026**): omzet **EUR593,959,237** JUMP +6.69%; pnl **EUR2,232,230** DROP -73.58%; equity **EUR81,050,938** JUMP **+68.29%**; bruto **EUR283,029,421** JUMP +5.1%; FTE **3235**; assets/debt **Unknown**.
- Liege regional hospital IGS. Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: CHR Citadelle — officiel.ic-chrcitadelle@chrcitadelle.be
Bld du Douzieme-de-Ligne 1, 4000 Liege
cc: SPW sante / Province Liege transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 CHR Citadelle + balans + equity JUMP recon (KBO 0237.086.311)
Geachte, op grond van decret wallon / CDLD vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 02.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon equity JUMP (+68pct vs YE2024 48.16m).
4. Recon pnl DROP (-74pct vs YE2024 8.45m) vs omzet JUMP.
5. Dual vs ISoSL / Epicura / CHU indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

for x in qrows:
    if x.get("task_id") == "rq_1988":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after ISoSL — CHR Citadelle YE2025 Medium"
        x["notes"] = "tick1988 Citadelle Medium omzet JUMP 593.96m equity JUMP 81.05m +68pct; FOI ready; next rq_1989; next every-10 1990"
        x["instructions"] = (
            "Completed leftover CHR Citadelle Liege regional hospital YE2025 Medium CW; KBO 0237.086.311; "
            "omzet JUMP 593959237 pnl DROP 2232230 equity JUMP 81050938 bruto JUMP 283029421 FTE 3235; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1989" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1989",
            "title": "leftover dual hole-fill after CHR Citadelle",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 1988 after CHR Citadelle YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital. Do NOT redo CHR Citadelle, ISoSL, CHU UCL Namur, Epicura, CHwapi, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, TIBI, IDELUX Environnement, IDELUX Eau, IDEA.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1988 Citadelle; next every-10 1990",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1988",
        "ticks_completed": "1988",
        "paused": "no",
        "notes": "tick1988 leftover CHR Citadelle 0237.086.311 Medium CW (omzet JUMP 593.96m pnl DROP 2.23m equity JUMP 81.05m +68pct bruto JUMP 283.03m FTE 3235; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1989; next every-10 1990; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1988 - 2026-08-24T00:30:00Z - rq_1988 CHR Citadelle (omzet JUMP 593.96m / equity JUMP 81.05m +68pct / Medium)

- Unit: **rq_1988** leftover dual after **rq_1987 ISoSL**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **CHR Citadelle** YE2025 (KBO **0237.086.311**; Bld du Douzieme-de-Ligne 1 Liege; Liege **regional hospital IGS**). Do not redo ISoSL/CHU UCL Namur/Epicura/CHwapi/Vivalia/HELORA/IDETA/SPI/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/IGRETEC/IPFBW/IDEA.
- Found: Companyweb NL+EN YE2025 - omzet **EUR593,959,237** JUMP +6.69%; pnl **EUR2,232,230** DROP -73.58%; equity **EUR81,050,938** JUMP **+68.29%**; bruto **EUR283,029,421** JUMP +5.1%; FTE **3235**; neerlegging **02.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief CV; email officiel.ic-chrcitadelle@chrcitadelle.be.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 igs_chr_citadelle); foi + draft gap_citadelle_nbb_pdf_assets_debt_equity_jump_matrix_l5; rq_1988=done + rq_1989 open; loop_state ticks=1988.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1990**). Next: rq_1989 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-hospital).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1988" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1988")
