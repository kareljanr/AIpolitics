# ephemeral tick2043 — Zorggroep Zusters van Berlaar YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T15:25:00Z"
ENTITY = "vzw_zorggroep_zusters_van_berlaar"
GAP = "gap_zusters_berlaar_nbb_pdf_assets_debt_subsidy_matrix_l5"
SRC = "src_zusters_berlaar_jr2025_cw"
SRC_EN = "src_zusters_berlaar_jr2025_cw_en"
SRC_FR = "src_zusters_berlaar_jr2025_cw_fr"
SRC_KBO = "src_zusters_berlaar_kbo_2043"
SRC_SITE = "src_zusters_berlaar_site_jv2025_2043"

OMZET = "77348216"
PNL = "3731645"
EQUITY = "87709000"
BRUTO = "77507316"
FTE = "932.4"
OMZET24 = "73665432"
PNL24 = "4222523"
EQUITY24 = "84830721"
BRUTO24 = "74601823"
# pi = 0.55*6.5 + 0.35*5.5 + 0.10*(10-4) = 3.575 + 1.925 + 0.6 = 6.1
PI = "6.1"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
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
r = next(x for x in qrows if x.get("task_id") == "rq_2043")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Zorggroep Zusters van Berlaar YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0417703081/zorggroep-zusters-van-berlaar",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2043; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 05.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2043/zusters_berlaar_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Zorggroep Zusters van Berlaar YE2025 statutory",
        "url": "https://www.companyweb.be/en/0417703081/zorggroep-zusters-van-berlaar",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2043; EN mirror YE2025 Medium; filed 05-06-2026; Last balance sheet year 2025; FTE 932.4; raw docs/doge/data/raw/tick2043/zusters_berlaar_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Zorggroep Zusters van Berlaar YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0417703081/zorggroep-zusters-van-berlaar",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2043; FR mirror YE2025 Medium; déposés le 05-06-2026; raw docs/doge/data/raw/tick2043/zusters_berlaar_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Zorggroep Zusters van Berlaar 0417.703.081 Actief VZW aanbestedende overheid Berlaar",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0417703081",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2043; Actief VZW; Sollevelden 1 2590 Berlaar; 13 VE; aanbestedende overheid sinds 29.09.1977; KBO email empty; absorbed WZC Sint-Augustinus 0410.469.059 since 01.04.2024",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Zorggroep Zusters van Berlaar JV2025 narrative + site contact",
        "url": "https://zorggroepzvb2025.jaarverslag.org/financieel/",
        "publisher": "Zorggroep Zusters van Berlaar",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2043; official JV2025 narrative (ratios/% only — absolute euros from CW); uitgebreide omzet +~4pct; resultaat 3.99pct gecorr. omzet (was 4.70pct); subsidies ~15.72pct; equity share ~59.16pct balanstotaal; paid FTE avg ~828.95; info@zusters-berlaar.be; raw docs/doge/data/raw/tick2043/jv_financieel.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_zusters_berlaar_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2043; omzet JUMP {OMZET} +5.00pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_zusters_berlaar_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2043; pnl DROP {PNL} -11.63pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_zusters_berlaar_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2043; equity JUMP {EQUITY} +3.39pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_zusters_berlaar_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2043; bruto JUMP {BRUTO} +3.89pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_zusters_berlaar_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2043; YE2025 FTE {FTE} (JV narrative paid FTE avg ~828.95 — different metric)",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_zusters_berlaar_jr2025_statutory_wzc",
    "title": "Zorggroep Zusters van Berlaar YE2025 leftover dual (omzet JUMP 77.35m / pnl DROP 3.73m)",
    "entity_id": ENTITY,
    "beneficiary": "VL multi-site WZC/AW residents (Berlaar belt + Essen/Kapellen/Holsbeek/Lommel e.a.)",
    "legal_basis": "VZW WZC operator / aanbestedende overheid (KBO 0417.703.081)",
    "decision_date": "2026-06-05",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0417703081/zorggroep-zusters-van-berlaar",
    "stated_goal": "Multi-site VL woonzorg / buurtzorg (Zusters van Berlaar zorggroep)",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; scrutinise IFIC/Alivia/Vlaio subsidy stack vs 77m omzet",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Berlaar>ZorggroepZustersVanBerlaar>JR2025_statutory_L5",
    "notes": "tick2043; Medium CW + official JV2025 narrative corroboration; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Verlosser still deferred; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_zusters_berlaar_omzet_jump_77_35m_pnl_drop_jr2025",
    "name": "Zorggroep Zusters van Berlaar omzet JUMP 77.35m / pnl DROP 3.73m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_aanbestedende_overheid_dual",
    "hierarchy_path": "Vlaanderen>Antwerpen>Berlaar>ZorggroepZustersVanBerlaar>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; aanbestedende overheid VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "VL elderly-care residents via Zorggroep Zusters van Berlaar multi-site WZC/AW",
    "stated_goal": "Multi-site VL woonzorg / buurtzorg",
    "measured_outcome": "Medium CW YE2025; 77.35m omzet JUMP +5.00pct with pnl DROP -11.63pct; JV narrative subsidies ~15.72pct gecorr. omzet; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "6.5",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map subsidy vs dagprijs/IFIC/Alivia stack; explain pnl DROP vs omzet JUMP",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2043 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2050",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Zorggroep Zusters van Berlaar (VZW, multi-site WZC)",
    "name_fr": "Groupe de soins Soeurs de Berlaar (ASBL, MRS multi-sites)",
    "name_en": "Zorggroep Zusters van Berlaar (VZW multi-site nursing homes)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://zorggroepzvb.be/",
    "foi_email": "info@zusters-berlaar.be",
    "foi_postal": "Sollevelden 1, 2590 Berlaar",
    "notes": (
        "tick2043 YE2025 Medium CW NL+EN+FR + Strong KBO 0417.703.081 Actief VZW aanbestedende overheid 13 VE; omzet JUMP 77.35m pnl DROP 3.73m equity JUMP 87.71m bruto JUMP 77.51m FTE 932.4; "
        "assets/debt Unknown; neerlegging 05.06.2026; official JV2025 narrative corroborates omzet+/pnl-; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Verlosser deferred; do not redo Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus/Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren"
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
    "hierarchy_path": "Vlaanderen>Antwerpen>Berlaar>ZorggroepZustersVanBerlaar>NBB_PDF_assets_debt_subsidy_matrix",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split (IFIC/Alivia/Vlaio/code73); absolute balanstotaal recon to JV % equity share; related-party notes post Sint-Augustinus absorption",
    "why_it_matters": "Medium CW shows 77.35m omzet VL aanbestedende-overheid WZC VZW with pnl DROP and ~16pct subsidy share without balance sheet or euro subsidy matrix",
    "priority": "8",
    "recipient_body": "Zorggroep Zusters van Berlaar VZW",
    "recipient_email": "info@zusters-berlaar.be",
    "recipient_postal": "Sollevelden 1, 2590 Berlaar",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_zusters_berlaar_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_zusters_berlaar_omzet_jump_77_35m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2043; human-send only; Medium CW; next every-10 2050",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Zorggroep Zusters van Berlaar (NBB PDF / assets-debt / subsidy matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Zorggroep Zusters van Berlaar VZW — KBO **0417.703.081**  
**recipient:** info@zusters-berlaar.be · Sollevelden 1, 2590 Berlaar  
**sources:** [CW NL](https://www.companyweb.be/nl/0417703081/zorggroep-zusters-van-berlaar) · [CW EN](https://www.companyweb.be/en/0417703081/zorggroep-zusters-van-berlaar) · [CW FR](https://www.companyweb.be/fr/0417703081/zorggroep-zusters-van-berlaar) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0417703081) · [JV2025 financieel](https://zorggroepzvb2025.jaarverslag.org/financieel/) · [site](https://zorggroepzvb.be/)  
**tick:** 2043  
**confidence:** Medium (CW NL+EN+FR; official JV narrative corroboration; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **05.06.2026**): omzet **EUR77,348,216** JUMP +5.00%; pnl **EUR3,731,645** DROP −11.63% vs YE2024 EUR4,222,523; equity **EUR87,709,000** JUMP +3.39%; bruto **EUR77,507,316** JUMP +3.89%; FTE **932.4**; assets/debt **Unknown**.
- Official JV2025: uitgebreide omzet +~4%; resultaat **3.99%** gecorrigeerde omzet (was 4.70%); lidgeld/schenkingen/legaten/subsidies **~15.72%**; equity share ~**59.16%** balanstotaal; paid FTE avg ~828.95.
- KBO: Actief VZW **aanbestedende overheid**; 13 VE; absorbed WZC Sint-Augustinus 01.04.2024.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. De Verlosser YE2025 still deferred. Do not redo Psychogeriatrisch Centrum / De Linde / Samen Ouder / Zonhoven / Orelia / …

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Zorggroep Zusters van Berlaar VZW — Sollevelden 1, 2590 Berlaar
info@zusters-berlaar.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Zorggroep Zusters van Berlaar + subsidiematrix (KBO 0417.703.081)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (VZW is aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 05.06.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting pnl DROP (van EUR4.222.523 YE2024 naar EUR3.731.645 YE2025) bij omzet JUMP.
5. Effect fusie/opslorping WZC Sint-Augustinus (0410.469.059) op YE2025 cijfers (niet-confidentieel deel).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, "
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
    "Armonea, Colisée Belgium, Prinsenhof, Vivalto Home BE, emeis Belgium / ORPEA. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
)

for x in qrows:
    if x.get("task_id") == "rq_2043":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Psychogeriatrisch Centrum — Zorggroep Zusters van Berlaar YE2025 Medium"
        x["notes"] = (
            "tick2043 Zorggroep Zusters van Berlaar Medium omzet JUMP 77.35m pnl DROP 3.73m equity JUMP 87.71m bruto JUMP 77.51m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Verlosser deferred; next rq_2044; next every-10 2050"
        )
        x["instructions"] = (
            "Completed leftover Zorggroep Zusters van Berlaar YE2025 Medium CW; KBO 0417.703.081; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2044" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2044",
            "title": "leftover dual hole-fill after Zorggroep Zusters van Berlaar",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2043 after Zorggroep Zusters van Berlaar YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(WZC De Verlosser Dilbeek YE2025 live deferred / other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2043 Zorggroep Zusters van Berlaar; next every-10 2050; De Verlosser YE2025 deferred",
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
        "last_unit_id": "rq_2043",
        "ticks_completed": "2043",
        "paused": "no",
        "notes": (
            "tick2043 leftover Zorggroep Zusters van Berlaar 0417.703.081 Medium CW (omzet JUMP 77.35m pnl DROP 3.73m equity JUMP 87.71m bruto JUMP 77.51m FTE 932.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Verlosser deferred; next rq_2044; next every-10 2050; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2043 - {UTC} - rq_2043 Zorggroep Zusters van Berlaar (omzet JUMP 77.35m / pnl DROP 3.73m / Medium)

- Unit: **rq_2043** leftover dual after **rq_2042 Psychogeriatrisch Centrum**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **Zorggroep Zusters van Berlaar** YE2025 (KBO **0417.703.081**; Sollevelden 1 Berlaar; VL **aanbestedende-overheid VZW** multi-site WZC / 13 VE). WZC De Verlosser Dilbeek YE2025 also live — deferred. Do not redo Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR77,348,216** JUMP +5.00%; pnl **EUR3,731,645** DROP −11.63%; equity **EUR87,709,000** JUMP +3.39%; bruto **EUR77,507,316** JUMP +3.89%; FTE **932.4**; neerlegging **05.06.2026**. Assets/debt Unknown. Medium confidence. Official JV2025 narrative corroborates omzet+/resultaat− (3.99% vs 4.70% gecorr. omzet; subsidies ~15.72%). Strong KBO Actief VZW aanbestedende overheid 13 VE; email info@zusters-berlaar.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2043=done + rq_2044 open; loop_state ticks=2043; raw under docs/doge/data/raw/tick2043/.
- FOI: **ready not sent** (human-gated; info@zusters-berlaar.be).
- NOT every-10 (**next every-10 is 2050**). Next: rq_2044 (AGB/FARO-if-YE2025 / AIESH-REW / De Verlosser deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2043 Zorggroep Zusters van Berlaar", OMZET, "pi", PI)
