# ephemeral tick2042 — Psychogeriatrisch Centrum (Arcus/Korian) YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T15:10:00Z"
ENTITY = "nv_psychogeriatrisch_centrum"
GAP = "gap_psychogeriatrisch_centrum_nbb_pdf_assets_debt_pnl_bruto_drop_matrix_l5"
SRC = "src_psychoger_jr2025_cw"
SRC_EN = "src_psychoger_jr2025_cw_en"
SRC_FR = "src_psychoger_jr2025_cw_fr"
SRC_KBO = "src_psychoger_kbo_2042"
SRC_SITE = "src_psychoger_arcus_korian_2042"

OMZET = "53397484"
PNL = "284351"
EQUITY = "13807612"
BRUTO = "34905368"
FTE = "642.4"
OMZET24 = "53135954"
PNL24 = "953218"
EQUITY24 = "13523261"
BRUTO24 = "43417032"
# pi = 0.55*5.5 + 0.35*6.0 + 0.10*(10-4) = 3.025 + 2.1 + 0.6 = 5.725
PI = "5.725"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
        # normalize any residual BOM on first header
        fields = [f.lstrip("\ufeff") for f in fields]
        for row in rows:
            if any(k.startswith("\ufeff") for k in row):
                for k in list(row):
                    if k.startswith("\ufeff"):
                        row[k.lstrip("\ufeff")] = row.pop(k)
        return rows, fields


def save(path, rows, fields):
    fields = [f.lstrip("\ufeff") for f in fields]
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2042")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Psychogeriatrisch Centrum YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0435357675/psychogeriatrisch-centrum",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2042; YE2025 omzet FLAT {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 28.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2042/psychoger_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Psychogeriatrisch Centrum YE2025 statutory",
        "url": "https://www.companyweb.be/en/0435357675/psychogeriatrisch-centrum",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2042; EN mirror YE2025 Medium; filed 28-07-2026; Last balance sheet year 2025; FTE 642.4; raw docs/doge/data/raw/tick2042/psychoger_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Psychogeriatrisch Centrum YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0435357675/psychogeriatrisch-centrum",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2042; FR mirror YE2025 Medium; déposés le 28-07-2026; raw docs/doge/data/raw/tick2042/psychoger_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Psychogeriatrisch Centrum 0435.357.675 Actief NV Sint-Agatha-Berchem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435357675",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2042; Actief NV; Gentsesteenweg 1050 1082 Sint-Agatha-Berchem; 6 VE; KBO email empty; rechtsvorm NV sinds 15.09.1988",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Korian Arcus Neuropsychogeriatrisch centrum contact",
        "url": "https://www.korian.be/woonzorgcentra/arcus/neuropsychogeratrischcentrum-arcus/",
        "publisher": "Korian Belgium / Arcus",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2042; info@arcusbru.be; Gentsesteenweg 1050 1082 Sint-Agatha-Berchem; +32 2 482 34 00; commercial Korian Arcus dual; raw docs/doge/data/raw/tick2042/arcus_korian.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_psychoger_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2042; omzet FLAT/JUMP {OMZET} +0.49pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_psychoger_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2042; pnl DROP {PNL} -70.17pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_psychoger_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2042; equity JUMP {EQUITY} +2.10pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_psychoger_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2042; bruto DROP {BRUTO} -19.60pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_psychoger_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2042; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_psychoger_jr2025_statutory_wzc_psych",
    "title": "Psychogeriatrisch Centrum YE2025 leftover dual (omzet FLAT 53.40m / pnl DROP 0.28m / bruto DROP)",
    "entity_id": ENTITY,
    "beneficiary": "Brussels psychogeriatric / elderly care residents (Arcus / Korian Berchem)",
    "legal_basis": "NV psychogeriatric/WZC operator (KBO 0435.357.675)",
    "decision_date": "2026-07-28",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0435357675/psychogeriatrisch-centrum",
    "stated_goal": "Psychogeriatric residential care Sint-Agatha-Berchem (Korian Arcus)",
    "cut_option": "Publish NBB PDF assets/debt + pnl/bruto DROP FOI; map public subsidies vs resident fees / Korian group TP",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Brussels>SintAgathaBerchem>PsychogeriatrischCentrum>JR2025_statutory_L5",
    "notes": "tick2042; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_psychoger_omzet_flat_53_40m_pnl_drop_bruto_drop_jr2025",
    "name": "Psychogeriatrisch Centrum omzet FLAT 53.40m / pnl DROP 0.28m / bruto DROP (YE2025)",
    "level": "L5",
    "type": "commercial_psychogeriatric_nv_dual",
    "hierarchy_path": "Brussels>SintAgathaBerchem>PsychogeriatrischCentrum>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet FLAT {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown; Korian Arcus dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Brussels psychogeriatric residents via Psychogeriatrisch Centrum NV (Arcus/Korian)",
    "stated_goal": "Psychogeriatric residential care Sint-Agatha-Berchem",
    "measured_outcome": "Medium CW YE2025; 53.40m omzet FLAT +0.49pct with pnl DROP -70.17pct and bruto DROP -19.60pct; NBB PDF residual",
    "absurdity_score": "6.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl/bruto DROP vs flat omzet; map subsidy vs resident fees and Korian group transfer pricing",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2042 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2050",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Psychogeriatrisch Centrum (Arcus / Korian, Sint-Agatha-Berchem)",
    "name_fr": "Centre psychogériatrique (Arcus / Korian, Berchem-Sainte-Agathe)",
    "name_en": "Psychogeriatric Centre (Arcus / Korian, Sint-Agatha-Berchem)",
    "level": "company",
    "parent_id": "brussels_gov",
    "community_language": "bi",
    "website": "https://www.korian.be/woonzorgcentra/arcus/neuropsychogeratrischcentrum-arcus/",
    "foi_email": "info@arcusbru.be",
    "foi_postal": "Gentsesteenweg 1050, 1082 Sint-Agatha-Berchem",
    "notes": (
        "tick2042 YE2025 Medium CW NL+EN+FR + Strong KBO 0435.357.675 Actief NV; omzet FLAT 53.40m pnl DROP 0.28m equity JUMP 13.81m bruto DROP 34.91m FTE 642.4; "
        "assets/debt Unknown; neerlegging 28.07.2026; 6 VE; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus/Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren/AZJP"
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
    "hierarchy_path": "Brussels>SintAgathaBerchem>PsychogeriatrischCentrum>NBB_PDF_assets_debt_pnl_bruto_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl DROP and bruto DROP recon (flat omzet); Korian group related-party / TP note",
    "why_it_matters": "Medium CW shows 53.40m omzet Brussels commercial psychogeriatric NV (Korian Arcus) with pnl DROP -70pct and bruto DROP -20pct without balance sheet or subsidy transparency",
    "priority": "8",
    "recipient_body": "Psychogeriatrisch Centrum NV (Arcus / Korian)",
    "recipient_email": "info@arcusbru.be",
    "recipient_postal": "Gentsesteenweg 1050, 1082 Sint-Agatha-Berchem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_psychoger_jr2025_statutory_wzc_psych",
    "linked_leaderboard_id": "lb_psychoger_omzet_flat_53_40m_pnl_drop_bruto_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2042; human-send only; Medium CW; next every-10 2050",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Psychogeriatrisch Centrum (NBB PDF / assets-debt / pnl+bruto DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Psychogeriatrisch Centrum NV (Arcus / Korian) — KBO **0435.357.675**  
**recipient:** info@arcusbru.be · Gentsesteenweg 1050, 1082 Sint-Agatha-Berchem  
**sources:** [CW NL](https://www.companyweb.be/nl/0435357675/psychogeriatrisch-centrum) · [CW EN](https://www.companyweb.be/en/0435357675/psychogeriatrisch-centrum) · [CW FR](https://www.companyweb.be/fr/0435357675/psychogeriatrisch-centrum) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435357675) · [site](https://www.korian.be/woonzorgcentra/arcus/neuropsychogeratrischcentrum-arcus/)  
**tick:** 2042  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **28.07.2026**): omzet **EUR53,397,484** FLAT +0.49%; pnl **EUR284,351** DROP −70.17% vs YE2024 EUR953,218; equity **EUR13,807,612** JUMP +2.10%; bruto **EUR34,905,368** DROP −19.60%; FTE **642.4**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. De Linde / Samen Ouder / Zonhoven / Orelia already mined.
- Commercial NV dual Korian Arcus (Brussels psychogeriatric / WZC).

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Psychogeriatrisch Centrum NV (Arcus / Korian) — Gentsesteenweg 1050, 1082 Sint-Agatha-Berchem
info@arcusbru.be
cc: Iriscare / GGC / Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Psychogeriatrisch Centrum + balans (KBO 0435.357.675)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 28.07.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Toelichting pnl DROP (van EUR953.218 YE2024 naar EUR284.351 YE2025) en bruto DROP (−19.60%) bij vrijwel vlakke omzet.
5. Eventuele verbonden-partij / transfer-pricing toelichting t.a.v. Korian-groep (niet-confidentieel deel).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, "
    "WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, "
    "WZC Sint-Carolus Ternat, WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), "
    "Maria Rustoord Ingelmunster, PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, "
    "PC Gent-Sleidinge, AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, "
    "Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, "
    "AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, "
    "Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, "
    "IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, "
    "BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, "
    "SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
    "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, "
    "Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren, Sint-Jozef Rumst, Gravenkasteel, "
    "Armonea, Colisée Belgium, Prinsenhof, Vivalto Home BE. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
)

for x in qrows:
    if x.get("task_id") == "rq_2042":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC De Linde Lievegem — Psychogeriatrisch Centrum YE2025 Medium"
        x["notes"] = (
            "tick2042 Psychogeriatrisch Centrum Medium omzet FLAT 53.40m pnl DROP 0.28m equity JUMP 13.81m bruto DROP 34.91m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2043; next every-10 2050"
        )
        x["instructions"] = (
            "Completed leftover Psychogeriatrisch Centrum YE2025 Medium CW; KBO 0435.357.675; "
            f"omzet FLAT {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2043" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2043",
            "title": "leftover dual hole-fill after Psychogeriatrisch Centrum",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2042 after Psychogeriatrisch Centrum YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(WZC De Verlosser Dilbeek YE2025 live deferred / other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2042 Psychogeriatrisch Centrum; next every-10 2050; De Verlosser YE2025 deferred",
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
        "last_unit_id": "rq_2042",
        "ticks_completed": "2042",
        "paused": "no",
        "notes": (
            "tick2042 leftover Psychogeriatrisch Centrum 0435.357.675 Medium CW (omzet FLAT 53.40m pnl DROP 0.28m equity JUMP 13.81m bruto DROP 34.91m FTE 642.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Verlosser deferred; next rq_2043; next every-10 2050; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2042 - {UTC} - rq_2042 Psychogeriatrisch Centrum (omzet FLAT 53.40m / pnl DROP 0.28m / bruto DROP / Medium)

- Unit: **rq_2042** leftover dual after **rq_2041 WZC De Linde Lievegem**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **Psychogeriatrisch Centrum** YE2025 (KBO **0435.357.675**; Gentsesteenweg 1050 Sint-Agatha-Berchem; Brussels **commercial psychogeriatric NV** / Korian Arcus / 6 VE). WZC De Verlosser Dilbeek YE2025 also live — deferred. Do not redo De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren/AZJP.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR53,397,484** FLAT +0.49%; pnl **EUR284,351** DROP -70.17%; equity **EUR13,807,612** JUMP +2.10%; bruto **EUR34,905,368** DROP -19.60%; FTE **642.4**; neerlegging **28.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief NV 6 VE; email info@arcusbru.be (Korian Arcus).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2042=done + rq_2043 open; loop_state ticks=2042; raw under docs/doge/data/raw/tick2042/.
- FOI: **ready not sent** (human-gated; info@arcusbru.be).
- NOT every-10 (**next every-10 is 2050**). Next: rq_2043 (AGB/FARO-if-YE2025 / AIESH-REW / De Verlosser deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2042 Psychogeriatrisch Centrum", OMZET, "pi", PI)
