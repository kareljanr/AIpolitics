# ephemeral tick2038 — Orelia Zorg YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T14:10:00Z"
ENTITY = "nv_orelia_zorg"
GAP = "gap_orelia_zorg_nbb_pdf_assets_debt_equity_crater_pnl_loss_matrix_l5"
SRC = "src_orelia_zorg_jr2025_cw"
SRC_EN = "src_orelia_zorg_jr2025_cw_en"
SRC_FR = "src_orelia_zorg_jr2025_cw_fr"
SRC_KBO = "src_orelia_zorg_kbo_2038"
SRC_SITE = "src_orelia_zorg_site_2038"

OMZET = "65232164"
PNL = "-5932888"
EQUITY = "71210"
BRUTO = "48867976"
FTE = "734.4"
OMZET24 = "63911783"
PNL24 = "214063"
EQUITY24 = "6004099"
BRUTO24 = "51310159"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2038")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Orelia Zorg YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0810196557/orelia-zorg",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2038; YE2025 omzet JUMP {OMZET} pnl LOSS {PNL} equity CRATER {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 13.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2038/orelia_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Orelia Zorg YE2025 statutory",
        "url": "https://www.companyweb.be/en/0810196557/orelia-zorg",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2038; EN mirror YE2025 Medium; filed 13-07-2026; Last balance sheet year 2025; FTE 734.4; equity crater -98.81pct; raw docs/doge/data/raw/tick2038/orelia_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Orelia Zorg YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0810196557/orelia-zorg",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2038; FR mirror YE2025 Medium; déposés le 13-07-2026; raw docs/doge/data/raw/tick2038/orelia_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Orelia Zorg 0810.196.557 Actief NV Wommelgem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0810196557",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2038; Actief NV; Selsaetenstraat 50 B 2160 Wommelgem; 16 VE; no KBO email",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "orelia.be Orelia Zorg",
        "url": "https://www.orelia.be/",
        "publisher": "Orelia Zorg",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2038; info@orelia.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_orelia_zorg_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2038; omzet JUMP {OMZET} +2.07pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_orelia_zorg_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2038; pnl LOSS {PNL} FLIP vs YE2024 profit {PNL24}",
    },
    {
        "budget_id": "bud_orelia_zorg_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2038; equity CRATER {EQUITY} -98.81pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_orelia_zorg_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2038; bruto DROP {BRUTO} -4.76pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_orelia_zorg_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2038; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_orelia_zorg_jr2025_statutory_wzc",
    "title": "Orelia Zorg YE2025 leftover dual (omzet JUMP 65.23m / pnl LOSS 5.93m / equity CRATER 71k)",
    "entity_id": ENTITY,
    "beneficiary": "Antwerp-belt elderly care residents / Orelia WZC network",
    "legal_basis": "NV/SA WZC operator (KBO 0810.196.557)",
    "decision_date": "2026-07-13",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0810196557/orelia-zorg",
    "stated_goal": "Commercial residential elderly care (Antwerp belt)",
    "cut_option": "Publish NBB PDF assets/debt + equity crater FOI; map public subsidies vs resident fees",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>Orelia_Zorg>JR2025_statutory_L5",
    "notes": "tick2038; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; equity crater -98.81pct + pnl LOSS flip; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*7.0 + 0.10*(10-4) = 3.025 + 2.45 + 0.6 = 6.075
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_orelia_zorg_omzet_jump_65_23m_pnl_loss_5_93m_equity_crater_jr2025",
    "name": "Orelia Zorg omzet JUMP 65.23m / pnl LOSS 5.93m / equity CRATER 71k (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_nv_dual",
    "hierarchy_path": "Antwerpen>Orelia_Zorg>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl LOSS {PNL} equity CRATER {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Antwerp-belt elderly via Orelia Zorg NV",
    "stated_goal": "Commercial residential elderly care",
    "measured_outcome": "Medium CW YE2025; 65.23m omzet JUMP +2.07pct with pnl LOSS flip and equity crater -98.81pct; NBB PDF residual",
    "absurdity_score": "7.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "6.075",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain equity crater + loss vs public care euros; map subsidy vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2038 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2040",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Orelia Zorg (Wommelgem)",
    "name_fr": "Orelia Zorg (Wommelgem)",
    "name_en": "Orelia Zorg (elderly care NV)",
    "level": "nv",
    "parent_id": "prov_antwerpen",
    "community_language": "nl",
    "website": "https://www.orelia.be/",
    "foi_email": "info@orelia.be",
    "foi_postal": "Selsaetenstraat 50 B, 2160 Wommelgem",
    "notes": "tick2038 YE2025 Medium CW NL+EN+FR + Strong KBO 0810.196.557 Actief NV; omzet JUMP 65.23m pnl LOSS 5.93m equity CRATER 71k bruto DROP 48.87m FTE 734.4; assets/debt Unknown; neerlegging 13.07.2026; 16 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Kanunnik Triest/OLVA/OLV Roosdaal/Sint-Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren",
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
    "hierarchy_path": "Antwerpen>Orelia_Zorg>NBB_PDF_assets_debt_equity_crater_pnl_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; equity crater (-98.81pct) + pnl LOSS flip recon",
    "why_it_matters": "Medium CW shows 65.23m omzet Antwerp-belt commercial WZC NV with equity crater to 71k and 5.93m LOSS without balance sheet or subsidy transparency",
    "priority": "8",
    "recipient_body": "Orelia Zorg NV",
    "recipient_email": "info@orelia.be",
    "recipient_postal": "Selsaetenstraat 50 B, 2160 Wommelgem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_orelia_zorg_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_orelia_zorg_omzet_jump_65_23m_pnl_loss_5_93m_equity_crater_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2038; human-send only; Medium CW; next every-10 2040",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Orelia Zorg (NBB PDF / assets-debt / equity crater / pnl LOSS)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Orelia Zorg NV — KBO **0810.196.557**  
**recipient:** info@orelia.be · Selsaetenstraat 50 B, 2160 Wommelgem  
**sources:** [CW NL](https://www.companyweb.be/nl/0810196557/orelia-zorg) · [CW EN](https://www.companyweb.be/en/0810196557/orelia-zorg) · [CW FR](https://www.companyweb.be/fr/0810196557/orelia-zorg) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0810196557) · [site](https://www.orelia.be/)  
**tick:** 2038  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **13.07.2026**): omzet **EUR65,232,164** JUMP +2.07%; pnl **LOSS EUR-5,932,888** FLIP vs YE2024 profit; equity **EUR71,210** CRATER -98.81%; bruto **EUR48,867,976** DROP -4.76%; FTE **734.4**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Kanunnik Triest already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Orelia Zorg NV — Selsaetenstraat 50 B, 2160 Wommelgem
info@orelia.be
cc: Agentschap Zorg en Gezondheid / Provincie Antwerpen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Orelia Zorg + balans (KBO 0810.196.557)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 13.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Toelichting equity crater (-98,81pct tot EUR71.210) en pnl LOSS (EUR-5.932.888).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2038":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC Kanunnik Triest — Orelia Zorg YE2025 Medium"
        x["notes"] = (
            "tick2038 Orelia Zorg Medium omzet JUMP 65.23m pnl LOSS 5.93m equity CRATER 71k; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2039; next every-10 2040"
        )
        x["instructions"] = (
            "Completed leftover Orelia Zorg YE2025 Medium CW; KBO 0810.196.557; "
            f"omzet JUMP {OMZET} pnl LOSS {PNL} equity CRATER {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2039" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2039",
            "title": "leftover dual hole-fill after Orelia Zorg",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2038 after Orelia Zorg YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Woonzorg Samen Ouder YE2025 live deferred / C.W.Z.C. Zonhoven YE2025 / WZC De Linde Lievegem YE2025 / other unused YE2025 if live with omzet). "
                "Do NOT redo Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2038 Orelia Zorg; next every-10 2040; Samen Ouder/CWZC/De Linde YE2025 deferred",
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
        "last_unit_id": "rq_2038",
        "ticks_completed": "2038",
        "paused": "no",
        "notes": (
            "tick2038 leftover Orelia Zorg 0810.196.557 Medium CW (omzet JUMP 65.23m pnl LOSS 5.93m equity CRATER 71k bruto DROP 48.87m FTE 734.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2039; next every-10 2040; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2038 - {UTC} - rq_2038 Orelia Zorg (omzet JUMP 65.23m / pnl LOSS 5.93m / equity CRATER 71k / Medium)

- Unit: **rq_2038** leftover dual after **rq_2037 WZC Kanunnik Triest**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **Orelia Zorg** YE2025 (KBO **0810.196.557**; Selsaetenstraat 50 B Wommelgem; Antwerpen **commercial WZC NV**; 16 VE). Do not redo Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR65,232,164** JUMP +2.07%; pnl **LOSS EUR-5,932,888** FLIP vs YE2024 profit; equity **EUR71,210** CRATER -98.81%; bruto **EUR48,867,976** DROP -4.76%; FTE **734.4**; neerlegging **13.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief NV 16 VE; email info@orelia.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.075); entities (+1 nv_orelia_zorg); foi + draft {GAP}; rq_2038=done + rq_2039 open; loop_state ticks=2038; raw under docs/doge/data/raw/tick2038/.
- FOI: **ready not sent** (human-gated; info@orelia.be).
- NOT every-10 (**next every-10 is 2040**). Next: rq_2039 (AGB/FARO-if-YE2025 / AIESH-REW / Samen Ouder-CWZC-De Linde deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
