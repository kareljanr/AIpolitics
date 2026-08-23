# ephemeral tick2024 — Evara YE2025 Medium (leftover Multiversum-Evara dual after Maria Rustoord)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T10:40:00Z"
ENTITY = "vzw_evara"
GAP = "gap_evara_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_evara_jr2025_cw"
SRC_EN = "src_evara_jr2025_cw_en"
SRC_FR = "src_evara_jr2025_cw_fr"
SRC_KBO = "src_evara_kbo_2024"
SRC_SITE = "src_evara_site_2024"

OMZET = "443168637"
PNL = "32701878"
EQUITY = "750376596"
BRUTO = "714422920"
FTE = "7600.9"
OMZET24 = "423398216"
PNL24 = "38175879"
EQUITY24 = "721541356"
BRUTO24 = "675557826"

CW_NL = "https://www.companyweb.be/nl/0406633304/evara"
CW_EN = "https://www.companyweb.be/en/0406633304/evara"
CW_FR = "https://www.companyweb.be/fr/0406633304/evara"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0406633304"
SITE = "https://evara.be/"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2024")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Evara YE2025 statutory",
        "url": CW_NL,
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2024; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 07.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2024/evara_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Evara YE2025 statutory",
        "url": CW_EN,
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2024; EN mirror YE2025 Medium; filed 07-07-2026; Last balance sheet year 2025; FTE 7600.9; raw docs/doge/data/raw/tick2024/evara_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Evara YE2025 statutory",
        "url": CW_FR,
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2024; FR mirror YE2025 Medium; déposés le 07-07-2026; raw docs/doge/data/raw/tick2024/evara_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Evara 0406.633.304 Actief VZW",
        "url": KBO_URL,
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2024; Actief VZW; naam Evara sinds 01.01.2026 (ex Broeders van Liefde zorg/onderwijs); Stropkaai 38E 9000 Gent; 281 VE; Multiversum is zorggroep/facility under Evara — not separate statutory double-count",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "evara.be Evara contact",
        "url": SITE,
        "publisher": "Evara",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2024; info@evara.be; Multiversum care-group pages under evara.be / multiversum.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_evara_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2024; omzet JUMP {OMZET} +4.67pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_evara_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2024; pnl DROP {PNL} -14.34pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_evara_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2024; equity JUMP {EQUITY} +4.00pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_evara_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2024; bruto JUMP {BRUTO} +5.75pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_evara_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2024; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_evara_jr2025_statutory_psych_edu",
    "title": "Evara YE2025 leftover Multiversum dual (omzet JUMP 443.17m / pnl DROP 32.70m / equity JUMP 750.38m)",
    "entity_id": ENTITY,
    "beneficiary": "Flanders psych/ortho/education users via Evara (ex Broeders van Liefde; Multiversum zorggroep)",
    "legal_basis": "VZW/ASBL care+education group (KBO 0406.633.304; naam Evara sinds 01.01.2026)",
    "decision_date": "2026-07-07",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": CW_NL,
    "stated_goal": "Psychiatric hospitals, orthopedagogic centres, schools (Evara / Multiversum perimeter)",
    "cut_option": "Publish NBB PDF assets/debt FOI; map public subsidy vs tuition/care fees by sector",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Evara_ex_Broeders_van_Liefde>JR2025_statutory_L5",
    "notes": "tick2024; Medium CW; assets/debt Unknown; Multiversum is facility/group under Evara — not double-counted; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Maria Rustoord already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*7.5 + 0.35*5.0 + 0.10*(10-4) = 4.125+1.75+0.6 = 6.475
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_evara_omzet_jump_443_17m_pnl_drop_32_70m_jr2025",
    "name": "Evara omzet JUMP 443.17m / pnl DROP 32.70m / equity JUMP 750.38m (YE2025)",
    "level": "L5",
    "type": "flemish_psych_edu_vzw_dual",
    "hierarchy_path": "Vlaanderen>Evara_ex_Broeders_van_Liefde>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; Multiversum under Evara",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Flanders care/education users via Evara VZW (Multiversum + other facilities)",
    "stated_goal": "Psychiatric, orthopedagogic and education services",
    "measured_outcome": "Medium CW YE2025; 443.17m omzet JUMP +4.67pct with pnl DROP -14.34pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "7.5",
    "difficulty": "4.0",
    "priority_index": "6.475",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; split education vs care public money; Multiversum facility recon",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2024 leftover Multiversum-Evara dual; Medium CW; TE-adjacent care/edu flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Evara (ex Broeders van Liefde; Multiversum zorggroep)",
    "name_fr": "Evara (ex Frères de la Charité; groupe Multiversum)",
    "name_en": "Evara (ex Brothers of Charity; Multiversum care group)",
    "level": "asbl",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": SITE,
    "foi_email": "info@evara.be",
    "foi_postal": "Stropkaai 38E, 9000 Gent",
    "notes": (
        "tick2024 YE2025 Medium CW NL+EN+FR + Strong KBO 0406.633.304 Actief VZW; naam Evara sinds 01.01.2026; "
        "omzet JUMP 443.17m pnl DROP 32.70m equity JUMP 750.38m bruto JUMP 714.42m FTE 7600.9; assets/debt Unknown; "
        "neerlegging 07.07.2026; 281 VE; Multiversum is zorggroep under Evara (not separate statutory double-count); FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Maria Rustoord Ingelmunster/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende"
    ),
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
else:
    for x in erows:
        if x.get("entity_id") == ENTITY:
            x.update({k: v for k, v in ne.items() if v})
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>Evara>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs care/tuition fee split by sector; Multiversum facility recon; pnl DROP recon",
    "why_it_matters": "Medium CW shows 443.17m omzet Flanders mega care/education VZW without balance sheet or public-money transparency",
    "priority": "7",
    "recipient_body": "Evara vzw (ex Broeders van Liefde)",
    "recipient_email": "info@evara.be",
    "recipient_postal": "Stropkaai 38E, 9000 Gent",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_evara_jr2025_statutory_psych_edu",
    "linked_leaderboard_id": "lb_evara_omzet_jump_443_17m_pnl_drop_32_70m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2024; human-send only; Medium CW; Multiversum under Evara; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Evara (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Evara vzw (ex Broeders van Liefde; Multiversum zorggroep) — KBO **0406.633.304**  
**recipient:** info@evara.be · Stropkaai 38E, 9000 Gent  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** 2024  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **07.07.2026**): omzet **EUR443,168,637** JUMP +4.67%; pnl **EUR32,701,878** DROP −14.34%; equity **EUR750,376,596** JUMP +4.00%; bruto **EUR714,422,920** JUMP +5.75%; FTE **7600.9**; assets/debt **Unknown**.
- Naam **Evara** sinds 01.01.2026; Multiversum is zorggroep/facility under Evara (not separate statutory double-count).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Maria Rustoord Ingelmunster already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Evara vzw — Stropkaai 38E, 9000 Gent
info@evara.be
cc: Agentschap Zorg en Gezondheid / Departement Onderwijs indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Evara + balans (KBO 0406.633.304)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 07.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies (zorg/RIZIV/onderwijs) vs eigen inkomsten 2025.
4. Toelichting Multiversum vs andere voorzieningen binnen Evara (geen dubbeltelling).
5. Toelichting pnl DROP (−14,34pct).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

SKIP = (
    "Do NOT redo Evara/Multiversum double-count, Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, "
    "PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, "
    "Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, "
    "Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, "
    "AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, "
    "Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
    "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
    "Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, "
    "INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
)

for x in qrows:
    if x.get("task_id") == "rq_2024":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = (
            "leftover dual hole-fill after Maria Rustoord Ingelmunster — Evara YE2025 Medium"
        )
        x["notes"] = (
            "tick2024 Evara Medium omzet JUMP 443.17m pnl DROP 32.70m equity JUMP 750.38m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Multiversum under Evara (no double-count); next rq_2025; next every-10 2030"
        )
        x["instructions"] = (
            "Completed leftover Evara YE2025 Medium CW; KBO 0406.633.304; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2025" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2025",
            "title": "leftover dual hole-fill after Evara",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2024 after Evara YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Sint-Carolus / Zilverbos / other unused YE2025 if live with omzet). "
                + SKIP
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2024 Evara; next every-10 2030",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2024",
        "ticks_completed": "2024",
        "paused": "no",
        "notes": (
            "tick2024 leftover Evara 0406.633.304 Medium CW (omzet JUMP 443.17m pnl DROP 32.70m equity JUMP 750.38m bruto JUMP 714.42m FTE 7600.9; "
            "assets/debt Unknown; Multiversum under Evara); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2025; next every-10 2030; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2024 - {UTC} - rq_2024 Evara (omzet JUMP 443.17m / pnl DROP 32.70m / Medium)

- Unit: **rq_2024** leftover dual after **rq_2023 Maria Rustoord Ingelmunster**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took preferred leftover **Evara** YE2025 (KBO **0406.633.304**; Stropkaai 38E Gent; Flanders **care+education VZW**; naam Evara sinds 01.01.2026; Multiversum is zorggroep under Evara — **no double-count**). Do not redo Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR443,168,637** JUMP +4.67%; pnl **EUR32,701,878** DROP -14.34%; equity **EUR750,376,596** JUMP +4.00%; bruto **EUR714,422,920** JUMP +5.75%; FTE **7600.9**; neerlegging **07.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 281 VE; email info@evara.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_evara); foi + draft {GAP}; rq_2024=done + rq_2025 open; loop_state ticks=2024; raw under docs/doge/data/raw/tick2024/.
- FOI: **ready not sent** (human-gated; info@evara.be).
- NOT every-10 (**next every-10 is 2030**). Next: rq_2025 (AGB/FARO-if-YE2025 / AIESH-REW / Sint-Carolus-Zilverbos / unused DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("log ok")
print("DONE tick2024 Evara")
