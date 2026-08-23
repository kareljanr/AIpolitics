# ephemeral tick2022 — PPC Pittem YE2025 Medium (finish in_progress after WZC Sint-Vincentius Avelgem)
import csv
import shutil
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T10:20:00Z"
ENTITY = "vzw_ppc_pittem"
GAP = "gap_ppc_pittem_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_ppc_pittem_jr2025_cw"
SRC_EN = "src_ppc_pittem_jr2025_cw_en"
SRC_FR = "src_ppc_pittem_jr2025_cw_fr"
SRC_KBO = "src_ppc_pittem_kbo_2022"
SRC_SITE = "src_ppc_pittem_site_2022"

OMZET = "42447455"
PNL = "2266781"
EQUITY = "82904947"
BRUTO = "23335720"
FTE = "291.6"
OMZET24 = "38944245"
PNL24 = "1053904"
EQUITY24 = "80937909"
BRUTO24 = "22782870"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


# ensure raw copies
raw = Path("docs/doge/data/raw/tick2022")
raw.mkdir(parents=True, exist_ok=True)
for name in [
    "ppc_pittem.html",
    "ppc_pittem_en.html",
    "ppc_pittem_fr.html",
    "ppc_pittem_kbo.html",
    "ppc_pittem_site.html",
]:
    src = Path("docs/doge/data/raw/tick2021") / name
    if src.exists() and not (raw / name).exists():
        shutil.copy(src, raw / name)

qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2022")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL PPC Pittem YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2022; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 10.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2022/ppc_pittem.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN PPC Pittem YE2025 statutory",
        "url": "https://www.companyweb.be/en/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2022; EN mirror YE2025 Medium; filed 10-07-2026; Last balance sheet year 2025; FTE 291.6; raw docs/doge/data/raw/tick2022/ppc_pittem_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR PPC Pittem YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2022; FR mirror YE2025 Medium; déposés le 10-07-2026; raw docs/doge/data/raw/tick2022/ppc_pittem_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO PPC Pittem 0409.956.147 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409956147",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2022; Actief VZW; Psychotherapeutisch en Psychiatrisch Centrum Pittem / Kliniek Sint-Jozef; 1 VE; Pittem 8740",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "ppcpittem.be PPC Pittem contact",
        "url": "https://www.ppcpittem.be/",
        "publisher": "PPC Pittem",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2022; info@ppcpittem.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_ppc_pittem_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2022; omzet JUMP {OMZET} +9.00pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_ppc_pittem_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2022; pnl JUMP {PNL} +115.08pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_ppc_pittem_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2022; equity JUMP {EQUITY} +2.43pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_ppc_pittem_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2022; bruto JUMP {BRUTO} +2.43pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_ppc_pittem_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2022; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_ppc_pittem_jr2025_statutory_psych",
    "title": "PPC Pittem YE2025 leftover dual (omzet JUMP 42.45m / pnl JUMP 2.27m / equity JUMP 82.90m)",
    "entity_id": ENTITY,
    "beneficiary": "Pittem psych care patients / Kliniek Sint-Jozef perimeter",
    "legal_basis": "VZW/ASBL psych hospital (KBO 0409.956.147)",
    "decision_date": "2026-07-10",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem",
    "stated_goal": "Psychotherapeutic and psychiatric care (Pittem)",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "WestVlaanderen>PPC_Pittem>JR2025_statutory_L5",
    "notes": "tick2022; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Maria Ingelmunster YE2025 deferred; WZC Sint-Vincentius Avelgem already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*5.0 + 0.10*(10-4) = 5.375
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_ppc_pittem_omzet_jump_42_45m_pnl_jump_2_27m_jr2025",
    "name": "PPC Pittem omzet JUMP 42.45m / pnl JUMP 2.27m / equity JUMP 82.90m (YE2025)",
    "level": "L5",
    "type": "flemish_psych_hospital_vzw_dual",
    "hierarchy_path": "WestVlaanderen>PPC_Pittem>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Pittem psych patients via PPC Pittem / Kliniek Sint-Jozef VZW",
    "stated_goal": "Psychotherapeutic and psychiatric care",
    "measured_outcome": "Medium CW YE2025; 42.45m omzet JUMP +9.00pct with pnl JUMP +115.08pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.375",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public RIZIV/subsidy vs patient fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2022 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Psychotherapeutisch en Psychiatrisch Centrum Pittem (PPC Pittem)",
    "name_fr": "Centre psychothérapeutique et psychiatrique Pittem (PPC Pittem)",
    "name_en": "PPC Pittem (psychiatric hospital)",
    "level": "asbl",
    "parent_id": "prov_west_vlaanderen",
    "community_language": "nl",
    "website": "https://www.ppcpittem.be/",
    "foi_email": "info@ppcpittem.be",
    "foi_postal": "PPC Pittem, 8740 Pittem (Kliniek Sint-Jozef)",
    "notes": "tick2022 YE2025 Medium CW NL+EN+FR + Strong KBO 0409.956.147 Actief VZW; omzet JUMP 42.45m pnl JUMP 2.27m equity JUMP 82.90m bruto JUMP 23.34m FTE 291.6; assets/debt Unknown; neerlegging 10.07.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Maria Ingelmunster YE2025 deferred; do not redo WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
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
    "hierarchy_path": "WestVlaanderen>PPC_Pittem>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public RIZIV/subsidy vs patient-fee split; pnl JUMP recon",
    "why_it_matters": "Medium CW shows 42.45m omzet Pittem psych VZW without balance sheet or subsidy transparency",
    "priority": "6",
    "recipient_body": "PPC Pittem / Psychotherapeutisch en Psychiatrisch Centrum Pittem vzw",
    "recipient_email": "info@ppcpittem.be",
    "recipient_postal": "PPC Pittem, 8740 Pittem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_ppc_pittem_jr2025_statutory_psych",
    "linked_leaderboard_id": "lb_ppc_pittem_omzet_jump_42_45m_pnl_jump_2_27m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2022; human-send only; Medium CW; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — PPC Pittem (NBB PDF / assets-debt / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Psychotherapeutisch en Psychiatrisch Centrum Pittem vzw — KBO **0409.956.147**  
**recipient:** info@ppcpittem.be · 8740 Pittem  
**sources:** [CW NL](https://www.companyweb.be/nl/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem) · [CW EN](https://www.companyweb.be/en/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem) · [CW FR](https://www.companyweb.be/fr/0409956147/psychotherapeutisch-en-psychiatrisch-centrum-pittem) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0409956147) · [site](https://www.ppcpittem.be/)  
**tick:** 2022  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **10.07.2026**): omzet **EUR42,447,455** JUMP +9.00%; pnl **EUR2,266,781** JUMP +115.08%; equity **EUR82,904,947** JUMP +2.43%; bruto **EUR23,335,720** JUMP +2.43%; FTE **291.6**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Maria Rustoord Ingelmunster YE2025 deferred. WZC Sint-Vincentius Avelgem already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: PPC Pittem vzw — Psychotherapeutisch en Psychiatrisch Centrum Pittem, 8740 Pittem
info@ppcpittem.be
cc: Agentschap Zorg en Gezondheid / Provincie West-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 PPC Pittem + balans (KBO 0409.956.147)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 10.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke RIZIV/subsidies vs patiëntbijdragen 2025.
4. Toelichting pnl JUMP (+115,08pct).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2022":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC Sint-Vincentius Avelgem — PPC Pittem YE2025 Medium"
        x["notes"] = (
            "tick2022 PPC Pittem Medium omzet JUMP 42.45m pnl JUMP 2.27m equity JUMP 82.90m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Maria Ingelmunster YE2025 deferred; next rq_2023; next every-10 2030"
        )
        x["instructions"] = (
            "Completed leftover PPC Pittem YE2025 Medium CW; KBO 0409.956.147; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2023" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2023",
            "title": "leftover dual hole-fill after PPC Pittem",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2022 after PPC Pittem YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (Maria Rustoord Ingelmunster YE2025 live deferred / Multiversum-Evara if not double-count / Sint-Carolus / Zilverbos / other unused YE2025 if live with omzet). "
                "Do NOT redo PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2022 PPC Pittem; next every-10 2030; Maria Ingelmunster YE2025 deferred",
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
        "last_unit_id": "rq_2022",
        "ticks_completed": "2022",
        "paused": "no",
        "notes": (
            "tick2022 leftover PPC Pittem 0409.956.147 Medium CW (omzet JUMP 42.45m pnl JUMP 2.27m equity JUMP 82.90m bruto JUMP 23.34m FTE 291.6; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Maria Ingelmunster YE2025 deferred; next rq_2023; next every-10 2030; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2022 - {UTC} - rq_2022 PPC Pittem (omzet JUMP 42.45m / pnl JUMP 2.27m / Medium)

- Unit: **rq_2022** leftover dual after **rq_2021 WZC Sint-Vincentius Avelgem** (finish in_progress claim). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took claimed leftover **PPC Pittem** YE2025 (KBO **0409.956.147**; Kliniek Sint-Jozef; West-Vlaanderen **psych hospital VZW**). Maria Rustoord Ingelmunster YE2025 also live — deferred. Do not redo WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR42,447,455** JUMP +9.00%; pnl **EUR2,266,781** JUMP +115.08%; equity **EUR82,904,947** JUMP +2.43%; bruto **EUR23,335,720** JUMP +2.43%; FTE **291.6**; neerlegging **10.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@ppcpittem.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_ppc_pittem); foi + draft {GAP}; rq_2022=done + rq_2023 open; loop_state ticks=2022; raw under docs/doge/data/raw/tick2022/.
- FOI: **ready not sent** (human-gated; info@ppcpittem.be).
- NOT every-10 (**next every-10 is 2030**). Next: rq_2023 (AGB/FARO-if-YE2025 / AIESH-REW / Maria Ingelmunster-Multiversum / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
