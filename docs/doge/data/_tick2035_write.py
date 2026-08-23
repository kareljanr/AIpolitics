# ephemeral tick2035 — WZC OLV Roosdaal YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T13:25:00Z"
ENTITY = "vzw_wzc_olv_roosdaal"
GAP = "gap_wzc_olv_roosdaal_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_wzc_olv_roosdaal_jr2025_cw"
SRC_EN = "src_wzc_olv_roosdaal_jr2025_cw_en"
SRC_FR = "src_wzc_olv_roosdaal_jr2025_cw_fr"
SRC_KBO = "src_wzc_olv_roosdaal_kbo_2035"
SRC_SITE = "src_wzc_olv_roosdaal_site_2035"

OMZET = "7601527"
PNL = "303111"
EQUITY = "6832532"
BRUTO = "7274401"
FTE = "89.3"
OMZET24 = "7015213"
PNL24 = "117438"
EQUITY24 = "6529421"
BRUTO24 = "6775794"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2035")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC OLV Roosdaal YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0421031171/w-z-c-onze-lieve-vrouw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2035; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 02.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2035/roosdaal_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC OLV Roosdaal YE2025 statutory",
        "url": "https://www.companyweb.be/en/0421031171/w-z-c-onze-lieve-vrouw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2035; EN mirror YE2025 Medium; filed 02-06-2026; Last balance sheet year 2025; FTE 89.3; raw docs/doge/data/raw/tick2035/roosdaal_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC OLV Roosdaal YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0421031171/w-z-c-onze-lieve-vrouw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2035; FR mirror YE2025 Medium; déposés le 02-06-2026; raw docs/doge/data/raw/tick2035/roosdaal_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO W.Z.C. Onze-Lieve-Vrouw 0421.031.171 Actief VZW Roosdaal",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421031171",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2035; Actief VZW; Gasthuisstraat 57 1760 Roosdaal; 1 VE; no KBO email",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "wzc-olv-roosdaal.be WZC OLV Roosdaal",
        "url": "https://www.wzc-olv-roosdaal.be/",
        "publisher": "WZC OLV Roosdaal",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2035; info@wzc-olv-roosdaal.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_wzc_olv_roosdaal_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2035; omzet JUMP {OMZET} +8.36pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_wzc_olv_roosdaal_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2035; pnl JUMP {PNL} +158.10pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_wzc_olv_roosdaal_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2035; equity JUMP {EQUITY} +4.64pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_wzc_olv_roosdaal_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2035; bruto JUMP {BRUTO} +7.36pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_wzc_olv_roosdaal_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2035; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_wzc_olv_roosdaal_jr2025_statutory_wzc",
    "title": "WZC OLV Roosdaal YE2025 leftover dual (omzet JUMP 7.60m / pnl JUMP 0.30m / equity JUMP 6.83m)",
    "entity_id": ENTITY,
    "beneficiary": "Roosdaal elderly care residents / WZC OLV",
    "legal_basis": "VZW/ASBL WZC (KBO 0421.031.171)",
    "decision_date": "2026-06-02",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0421031171/w-z-c-onze-lieve-vrouw",
    "stated_goal": "Residential elderly care (Roosdaal)",
    "cut_option": "Publish NBB PDF assets/debt FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "VlaamsBrabant>WZC_OLV_Roosdaal>JR2025_statutory_L5",
    "notes": "tick2035; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint-Bernardus Assenede already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*3.5 + 0.35*5.0 + 0.10*(10-4) = 4.275
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_wzc_olv_roosdaal_omzet_jump_7_60m_pnl_jump_0_30m_jr2025",
    "name": "WZC OLV Roosdaal omzet JUMP 7.60m / pnl JUMP 0.30m / equity JUMP 6.83m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "VlaamsBrabant>WZC_OLV_Roosdaal>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Roosdaal elderly via WZC OLV VZW",
    "stated_goal": "Residential elderly care",
    "measured_outcome": "Medium CW YE2025; 7.60m omzet JUMP +8.36pct with pnl JUMP +158.10pct; NBB PDF residual",
    "absurdity_score": "5.0",
    "cost_score": "3.5",
    "difficulty": "4.0",
    "priority_index": "4.275",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map public subsidies vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2035 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2040",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "W.Z.C. Onze-Lieve-Vrouw (Roosdaal)",
    "name_fr": "Maison de repos Notre-Dame (Roosdaal)",
    "name_en": "WZC OLV Roosdaal (elderly care)",
    "level": "asbl",
    "parent_id": "prov_vlaams_brabant",
    "community_language": "nl",
    "website": "https://www.wzc-olv-roosdaal.be/",
    "foi_email": "info@wzc-olv-roosdaal.be",
    "foi_postal": "Gasthuisstraat 57, 1760 Roosdaal",
    "notes": "tick2035 YE2025 Medium CW NL+EN+FR + Strong KBO 0421.031.171 Actief VZW; omzet JUMP 7.60m pnl JUMP 0.30m equity JUMP 6.83m bruto JUMP 7.27m FTE 89.3; assets/debt Unknown; neerlegging 02.06.2026; 1 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Sint-Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende",
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
    "hierarchy_path": "VlaamsBrabant>WZC_OLV_Roosdaal>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl JUMP recon",
    "why_it_matters": "Medium CW shows 7.60m omzet Roosdaal WZC VZW without balance sheet or subsidy transparency",
    "priority": "6",
    "recipient_body": "W.Z.C. Onze-Lieve-Vrouw vzw (Roosdaal)",
    "recipient_email": "info@wzc-olv-roosdaal.be",
    "recipient_postal": "Gasthuisstraat 57, 1760 Roosdaal",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_wzc_olv_roosdaal_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_wzc_olv_roosdaal_omzet_jump_7_60m_pnl_jump_0_30m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2035; human-send only; Medium CW; next every-10 2040",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC OLV Roosdaal (NBB PDF / assets-debt / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** W.Z.C. Onze-Lieve-Vrouw vzw — KBO **0421.031.171**  
**recipient:** info@wzc-olv-roosdaal.be · Gasthuisstraat 57, 1760 Roosdaal  
**sources:** [CW NL](https://www.companyweb.be/nl/0421031171/w-z-c-onze-lieve-vrouw) · [CW EN](https://www.companyweb.be/en/0421031171/w-z-c-onze-lieve-vrouw) · [CW FR](https://www.companyweb.be/fr/0421031171/w-z-c-onze-lieve-vrouw) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421031171) · [site](https://www.wzc-olv-roosdaal.be/)  
**tick:** 2035  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **02.06.2026**): omzet **EUR7,601,527** JUMP +8.36%; pnl **EUR303,111** JUMP +158.10%; equity **EUR6,832,532** JUMP +4.64%; bruto **EUR7,274,401** JUMP +7.36%; FTE **89.3**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Sint-Bernardus Assenede already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: W.Z.C. Onze-Lieve-Vrouw vzw — Gasthuisstraat 57, 1760 Roosdaal
info@wzc-olv-roosdaal.be
cc: Agentschap Zorg en Gezondheid / Provincie Vlaams-Brabant indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC OLV Roosdaal + balans (KBO 0421.031.171)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 02.06.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Toelichting pnl JUMP (+158,10pct).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2035":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC Sint-Bernardus Assenede — WZC OLV Roosdaal YE2025 Medium"
        x["notes"] = (
            "tick2035 WZC OLV Roosdaal Medium omzet JUMP 7.60m pnl JUMP 0.30m equity JUMP 6.83m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2036; next every-10 2040"
        )
        x["instructions"] = (
            "Completed leftover WZC OLV Roosdaal YE2025 Medium CW; KBO 0421.031.171; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2036" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2036",
            "title": "leftover dual hole-fill after WZC OLV Roosdaal",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2035 after WZC OLV Roosdaal YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych (OLVA Antwerpen YE2025 live deferred / Kanunnik Triest YE2025 / other unused YE2025 if live with omzet). "
                "Do NOT redo WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren. "
                "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2035 WZC OLV Roosdaal; next every-10 2040; OLVA/Triest YE2025 deferred",
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
        "last_unit_id": "rq_2035",
        "ticks_completed": "2035",
        "paused": "no",
        "notes": (
            "tick2035 leftover WZC OLV Roosdaal 0421.031.171 Medium CW (omzet JUMP 7.60m pnl JUMP 0.30m equity JUMP 6.83m bruto JUMP 7.27m FTE 89.3; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2036; next every-10 2040; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2035 - {UTC} - rq_2035 WZC OLV Roosdaal (omzet JUMP 7.60m / pnl JUMP 0.30m / Medium)

- Unit: **rq_2035** leftover dual after **rq_2034 WZC Sint-Bernardus Assenede**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **WZC OLV Roosdaal** YE2025 (KBO **0421.031.171**; Gasthuisstraat 57 Roosdaal; Vlaams-Brabant **WZC VZW**). Do not redo Sint-Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/AZ Rivierenland/AZ Zeno/HH Tienen/Heilig Hart Leuven/Sint-Trudo/Sint-Andries/Heilig Hart Lier/Vlaamse Zorgkas/OLVT/AZ Oostende.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR7,601,527** JUMP +8.36%; pnl **EUR303,111** JUMP +158.10%; equity **EUR6,832,532** JUMP +4.64%; bruto **EUR7,274,401** JUMP +7.36%; FTE **89.3**; neerlegging **02.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@wzc-olv-roosdaal.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_wzc_olv_roosdaal); foi + draft {GAP}; rq_2035=done + rq_2036 open; loop_state ticks=2035; raw under docs/doge/data/raw/tick2035/.
- FOI: **ready not sent** (human-gated; info@wzc-olv-roosdaal.be).
- NOT every-10 (**next every-10 is 2040**). Next: rq_2036 (AGB/FARO-if-YE2025 / AIESH-REW / OLVA-Triest / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
