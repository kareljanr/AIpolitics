# ephemeral tick2028 — WZC De Foyer Gent YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T11:40:00Z"
ENTITY = "vzw_wzc_de_foyer_gent"
GAP = "gap_wzc_de_foyer_gent_nbb_pdf_assets_debt_pnl_recovery_matrix_l5"
SRC = "src_wzc_de_foyer_gent_jr2025_cw"
SRC_EN = "src_wzc_de_foyer_gent_jr2025_cw_en"
SRC_FR = "src_wzc_de_foyer_gent_jr2025_cw_fr"
SRC_KBO = "src_wzc_de_foyer_gent_kbo_2025"
SRC_SITE = "src_wzc_de_foyer_gent_site_2025"

OMZET = "19026367"
PNL = "38805"
EQUITY = "714486"
BRUTO = "12366559"
FTE = "188.1"
OMZET24 = "18426642"
PNL24 = "-666940"
EQUITY24 = "675680"
BRUTO24 = "12655960"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2028")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Woon- en Zorgcentra De Foyer Gent YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0413796456/woon-en-zorgcentra-de-foyer",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2028; YE2025 omzet JUMP {OMZET} pnl RECOVERY {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 30.04.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2028/foyer_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Woon- en Zorgcentra De Foyer Gent YE2025 statutory",
        "url": "https://www.companyweb.be/en/0413796456/woon-en-zorgcentra-de-foyer",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2028; EN mirror YE2025 Medium; filed 30-04-2026; Last balance sheet year 2025; FTE 188.1; raw docs/doge/data/raw/tick2028/foyer_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Woon- en Zorgcentra De Foyer Gent YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0413796456/woon-en-zorgcentra-de-foyer",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2028; FR mirror YE2025 Medium; déposés le 30-04-2026; raw docs/doge/data/raw/tick2028/foyer_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woon- en Zorgcentra De Foyer 0413.796.456 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413796456",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2028; Actief VZW; Heerweg-Zuid 126 9052 Gent; 4 VE; sinds 17.03.1924; raw docs/doge/data/raw/tick2028/foyer_kbo.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "wzcdefoyer.be WZC De Foyer Gent (Zilversterre e.a.)",
        "url": "https://www.wzcdefoyer.be/",
        "publisher": "WZC De Foyer",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2028; info@wzcdefoyer.be; +32 9 330 20 35; Heerweg-Zuid 126 Gent; campuses o.a. Zilversterre",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_de_foyer_gent_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2028; omzet JUMP {OMZET} +3.25pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_de_foyer_gent_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2028; pnl RECOVERY {PNL} from YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_wzc_de_foyer_gent_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2028; equity JUMP {EQUITY} +5.74pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_de_foyer_gent_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2028; bruto DROP {BRUTO} -2.29pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_de_foyer_gent_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2028; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_de_foyer_gent_jr2025_statutory",
    "title": "WZC De Foyer Gent YE2025 leftover dual (omzet JUMP 19.03m / pnl RECOVERY 39k / equity JUMP 0.71m)",
    "entity_id": ENTITY,
    "beneficiary": "Gent elderly residents via Woon- en Zorgcentra De Foyer VZW",
    "legal_basis": "VZW/ASBL woonzorgcentrum (KBO 0413.796.456)",
    "decision_date": "2026-04-30",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0413796456/woon-en-zorgcentra-de-foyer",
    "stated_goal": "Residential elderly care / WZC Gent (multi-campus)",
    "cut_option": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees; explain pnl recovery from YE2024 loss",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>Gent>WZC_De_Foyer>JR2025_statutory_L5",
    "notes": "tick2028; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH YE2024; REW YE2024",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.0 + 0.35*5.0 + 0.10*(10-4) = 5.1
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_de_foyer_gent_omzet_jump_19_03m_pnl_recovery_39k_jr2025",
    "name": "WZC De Foyer Gent omzet JUMP 19.03m / pnl RECOVERY 39k (from -667k) / equity JUMP 0.71m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "OostVlaanderen>Gent>WZC_De_Foyer>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl RECOVERY {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Gent elderly via WZC De Foyer VZW (multi-campus)",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 19.03m omzet JUMP +3.25pct with pnl RECOVERY from YE2024 LOSS -667k; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "5.0",
    "difficulty": "4.0",
    "priority_index": "5.1",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidy vs resident-fee mix; reconcile pnl recovery",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2028 leftover WZC dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2030",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woon- en Zorgcentra De Foyer (Gent)",
    "name_fr": "Woon- en Zorgcentra De Foyer (maison de repos Gand)",
    "name_en": "Woon- en Zorgcentra De Foyer (nursing home Ghent)",
    "level": "asbl",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.wzcdefoyer.be/",
    "foi_email": "info@wzcdefoyer.be",
    "foi_postal": "Heerweg-Zuid 126, 9052 Gent",
    "notes": "tick2028 YE2025 Medium CW NL+EN+FR + Strong KBO 0413.796.456 Actief VZW; omzet JUMP 19.03m pnl RECOVERY 39k equity JUMP 0.71m bruto DROP 12.37m FTE 188.1; assets/debt Unknown; neerlegging 30.04.2026; 4 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; AIESH 0201.712.587 YE2024; REW YE2024; do not redo WZC Sint-Carolus Ternat/WZC Zilverbos/Sint Carolus Mayerhof/Evara/Maria Rustoord Ingelmunster/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
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
    "hierarchy_path": "OostVlaanderen>Gent>WZC_De_Foyer>NBB_PDF_assets_debt_pnl_recovery",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl RECOVERY recon vs YE2024 LOSS -666940",
    "why_it_matters": "Medium CW shows 19.03m omzet multi-campus WZC with pnl recovery from large prior loss without balance sheet or public/private revenue mix",
    "priority": "7",
    "recipient_body": "Woon- en Zorgcentra De Foyer VZW Gent",
    "recipient_email": "info@wzcdefoyer.be",
    "recipient_postal": "Heerweg-Zuid 126, 9052 Gent",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_de_foyer_gent_jr2025_statutory",
    "linked_leaderboard_id": "lb_wzc_de_foyer_gent_omzet_jump_19_03m_pnl_recovery_39k_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2028; human-send only; Medium CW; next every-10 2030",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC De Foyer Gent (NBB PDF / assets-debt / pnl RECOVERY)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woon- en Zorgcentra De Foyer VZW Gent — KBO **0413.796.456**  
**recipient:** info@wzcdefoyer.be · Heerweg-Zuid 126, 9052 Gent  
**sources:** [CW NL](https://www.companyweb.be/nl/0413796456/woon-en-zorgcentra-de-foyer) · [CW EN](https://www.companyweb.be/en/0413796456/woon-en-zorgcentra-de-foyer) · [CW FR](https://www.companyweb.be/fr/0413796456/woon-en-zorgcentra-de-foyer) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413796456) · [wzcdefoyer.be](https://www.wzcdefoyer.be/)  
**tick:** 2028  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **30.04.2026**): omzet **EUR19,026,367** JUMP +3.25%; pnl **EUR38,805** RECOVERY from YE2024 LOSS EUR-666,940; equity **EUR714,486** JUMP +5.74%; bruto **EUR12,366,559** DROP -2.29%; FTE **188.1**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO YE2024; AIESH 0201.712.587 YE2024; REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon- en Zorgcentra De Foyer VZW — Heerweg-Zuid 126, 9052 Gent
info@wzcdefoyer.be
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC De Foyer Gent (KBO 0413.796.456)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 30.04.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs bewonersbijdragen 2025.
4. Toelichting pnl RECOVERY (EUR38.805) t.o.v. YE2024 verlies EUR-666.940.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

skip_list = (
    "Do NOT redo WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara/Multiversum, "
    "Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, "
    "PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, "
    "Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, "
    "AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, "
    "Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, "
    "IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, "
    "BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, "
    "SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
    "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, "
    "Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
)

for x in qrows:
    if x.get("task_id") == "rq_2028":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC Sint-Carolus Ternat — WZC De Foyer Gent YE2025 Medium"
        x["notes"] = (
            "tick2028 WZC De Foyer Gent Medium omzet JUMP 19.03m pnl RECOVERY 39k equity JUMP 0.71m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH YE2024; REW YE2024; next rq_2029; next every-10 2030"
        )
        x["instructions"] = (
            "Completed leftover WZC De Foyer Gent YE2025 Medium CW; KBO 0413.796.456; "
            f"omzet JUMP {OMZET} pnl RECOVERY {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2029" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2029",
            "title": "leftover dual hole-fill after WZC De Foyer Gent",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2028 after WZC De Foyer Gent YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (other unused YE2025 if live with omzet). "
                + skip_list
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2028 WZC De Foyer Gent; next every-10 2030",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue updated")

srows2, sfields2 = load("docs/doge/data/loop_state.csv")
for x in srows2:
    if x.get("state_id") == "main":
        x["mode"] = "continuous"
        x["current_sprint"] = "hole_fill"
        x["last_tick_utc"] = UTC
        x["last_unit_id"] = "rq_2028"
        x["ticks_completed"] = "2028"
        x["paused"] = "no"
        x["notes"] = (
            "tick2028 leftover WZC De Foyer Gent 0413.796.456 Medium CW (omzet JUMP 19.03m pnl RECOVERY 39k "
            "equity JUMP 0.71m bruto DROP 12.37m FTE 188.1; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH YE2024; "
            "REW YE2024; next rq_2029; next every-10 2030; continuous hole_fill"
        )
save("docs/doge/data/loop_state.csv", srows2, sfields2)
print("loop_state updated")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2028 - {UTC} - rq_2028 WZC De Foyer Gent (omzet JUMP 19.03m / pnl RECOVERY 39k / Medium)

- Unit: **rq_2028** leftover dual after **rq_2027 WZC Sint-Carolus Ternat**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH **0201.712.587** still **YE2024**; REW still **YE2024**. Took unused leftover **WZC De Foyer Gent** YE2025 (KBO **0413.796.456**; Heerweg-Zuid 126 Gent; Oost-Vlaanderen **WZC VZW** multi-campus / Zilversterre e.a.). Do not redo Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara Herselt/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR19,026,367** JUMP +3.25%; pnl **EUR38,805** RECOVERY from YE2024 LOSS -666,940; equity **EUR714,486** JUMP +5.74%; bruto **EUR12,366,559** DROP -2.29%; FTE **188.1**; neerlegging **30.04.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 4 VE; email info@wzcdefoyer.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_de_foyer_gent); foi + draft gap_wzc_de_foyer_gent_nbb_pdf_assets_debt_pnl_recovery_matrix_l5; rq_2028=done + rq_2029 open; loop_state ticks=2028; raw under docs/doge/data/raw/tick2028/.
- FOI: **ready not sent** (human-gated; info@wzcdefoyer.be).
- NOT every-10 (**next every-10 is 2030**). Next: rq_2029 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-hospital-psych-WZC).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("log appended")
print("DONE tick2028")
