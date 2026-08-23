# ephemeral tick2061 — WZC Ter Burg YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T20:20:00Z"
ENTITY = "vzw_wzc_ter_burg"
GAP = "gap_ter_burg_nbb_pdf_assets_debt_pnl_deeper_loss_matrix_l5"
SRC = "src_ter_burg_jr2025_cw"
SRC_EN = "src_ter_burg_jr2025_cw_en"
SRC_FR = "src_ter_burg_jr2025_cw_fr"
SRC_KBO = "src_ter_burg_kbo_2061"
SRC_SITE = "src_ter_burg_site_2061"
SRC_ZORG = "src_ter_burg_zorg_repertorium_2061"

OMZET = "7875893"
PNL = "-483158"
EQUITY = "10671689"
BRUTO = "7166919"
FTE = "88.3"
OMZET24 = "7376815"
PNL24 = "-209221"
EQUITY24 = "11577433"
BRUTO24 = "7276645"
# pi = 0.55*4.7 + 0.35*5.3 + 0.10*(10-4) = 2.585 + 1.855 + 0.6 = 5.04 → 5.0
PI = "5.0"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2061")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Ter Burg YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0479401318/woon-en-zorgcentrum-ter-burg",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2061; YE2025 omzet JUMP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; neerlegging 07.04.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2061/ter_burg_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Ter Burg YE2025 statutory",
        "url": "https://www.companyweb.be/en/0479401318/woon-en-zorgcentrum-ter-burg",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2061; EN mirror YE2025 Medium; filed 07-04-2026; Last balance sheet year 2025; FTE 88.3; raw docs/doge/data/raw/tick2061/ter_burg_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Ter Burg YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0479401318/woon-en-zorgcentrum-ter-burg",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2061; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2061/ter_burg_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO WZC Ter Burg 0479.401.318 Actief VZW Zaventem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0479401318",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2061; Actief VZW; Leuvensesteenweg 653 1930 Zaventem; 1 VE; NACE 87.101; aanbestedende overheid; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "WZC Ter Burg site info@terburg.be",
        "url": "https://www.terburg.be/",
        "publisher": "Woon en Zorgcentrum Ter Burg vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2061; site+contact info@terburg.be / silke.declercq@terburg.be; raw docs/doge/data/raw/tick2061/ter_burg_site.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_ZORG,
        "title": "Departement Zorg repertorium WZC Ter Burg info@terburg.be",
        "url": "https://www.zorg-en-gezondheid.be/sites/default/files/external/Repertorium_burst_def_-_ADRESSEN_WZC-_PROVINCIE_Vlaams-Brabant.pdf",
        "publisher": "Departement Zorg Vlaanderen",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2061; PE1257 Ter Burg Leuvensesteenweg 653; tel 02-759 79 44; email info@terburg.be; capacity 130",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_ter_burg_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2061; omzet JUMP {OMZET} +6.77pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_ter_burg_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2061; pnl DEEPER LOSS {PNL} vs YE2024 LOSS {PNL24}",
    },
    {
        "budget_id": "bud_ter_burg_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2061; equity DROP {EQUITY} -7.82pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_ter_burg_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2061; bruto DROP {BRUTO} -1.51pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_ter_burg_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2061; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_ter_burg_jr2025_statutory_wzc",
    "title": "WZC Ter Burg YE2025 leftover dual (omzet JUMP 7.88m / pnl DEEPER LOSS 0.48m)",
    "entity_id": ENTITY,
    "beneficiary": "Zaventem-Nossegem elderly residents (WZC Ter Burg)",
    "legal_basis": "VZW WZC / aanbestedende overheid / publiek gesubsidieerde zorg (KBO 0479.401.318)",
    "decision_date": "2026-04-07",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0479401318/woon-en-zorgcentrum-ter-burg",
    "stated_goal": "WZC residential elderly care + kortverblijf + assistentiewoningen Zaventem",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain DEEPER LOSS despite omzet JUMP",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Zaventem>TerBurg>JR2025_statutory_L5",
    "notes": "tick2061; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_ter_burg_omzet_jump_7_88m_pnl_deeper_loss_jr2025",
    "name": "WZC Ter Burg omzet JUMP 7.88m / pnl DEEPER LOSS 0.48m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Zaventem>TerBurg>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; assets/debt Unknown; WZC VZW dual aanbestedende overheid",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Zaventem-Nossegem elderly residents via WZC Ter Burg",
    "stated_goal": "WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 7.88m omzet JUMP +6.77pct with DEEPER LOSS -483k (from -209k) and equity DROP -7.82pct; NBB PDF residual",
    "absurdity_score": "5.3",
    "cost_score": "4.7",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain DEEPER LOSS vs omzet JUMP; map IFIC/Alivia vs dagprijs split",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2061 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2070",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woon en Zorgcentrum Ter Burg (VZW, Zaventem)",
    "name_fr": "Woon en Zorgcentrum Ter Burg (ASBL MRS, Zaventem)",
    "name_en": "WZC Ter Burg (VZW nursing home Zaventem-Nossegem)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.terburg.be/",
    "foi_email": "info@terburg.be",
    "foi_postal": "Leuvensesteenweg 653, 1930 Zaventem",
    "notes": (
        "tick2061 YE2025 Medium CW NL+EN+FR + Strong KBO 0479.401.318 Actief VZW aanbestedende overheid 1 VE; omzet JUMP 7.88m pnl DEEPER LOSS 0.48m equity DROP 10.67m bruto DROP 7.17m FTE 88.3; "
        "assets/debt Unknown; neerlegging 07.04.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; OLV Wezembeek/Sint-Antonius YE2025 deferred; do not redo Christine/Home Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof"
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
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Zaventem>TerBurg>NBB_PDF_assets_debt_pnl_deeper_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of DEEPER LOSS (-483k vs -209k) despite omzet JUMP +6.77pct",
    "why_it_matters": "Medium CW shows 7.88m omzet WZC VZW aanbestedende overheid with DEEPER LOSS + equity DROP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Woon en Zorgcentrum Ter Burg vzw",
    "recipient_email": "info@terburg.be",
    "recipient_postal": "Leuvensesteenweg 653, 1930 Zaventem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ter_burg_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_ter_burg_omzet_jump_7_88m_pnl_deeper_loss_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2061; human-send only; Medium CW; next every-10 2070",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Ter Burg (NBB PDF / assets-debt / pnl-deeper-loss)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woon en Zorgcentrum Ter Burg VZW — KBO **0479.401.318**  
**recipient:** info@terburg.be · Leuvensesteenweg 653, 1930 Zaventem  
**sources:** [CW NL](https://www.companyweb.be/nl/0479401318/woon-en-zorgcentrum-ter-burg) · [CW EN](https://www.companyweb.be/en/0479401318/woon-en-zorgcentrum-ter-burg) · [CW FR](https://www.companyweb.be/fr/0479401318/woon-en-zorgcentrum-ter-burg) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0479401318) · [site](https://www.terburg.be/)  
**tick:** 2061  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **07.04.2026**): omzet **EUR7,875,893** JUMP +6.77%; pnl **LOSS EUR-483,158** DEEPER vs YE2024 LOSS EUR-209,221; equity **EUR10,671,689** DROP -7.82%; bruto **EUR7,166,919** DROP -1.51%; FTE **88.3**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; aanbestedende overheid; zetel Leuvensesteenweg 653 Zaventem; NACE 87.101.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Deferred live YE2025: OLV Wezembeek / Sint-Antonius.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woon en Zorgcentrum Ter Burg vzw — Leuvensesteenweg 653, 1930 Zaventem
info@terburg.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Ter Burg + subsidiematrix (KBO 0479.401.318)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (aanbestedende overheid / publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 07.04.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting verdieping verlies van EUR-209.221 (YE2024) naar EUR-483.158 (YE2025) bij omzet JUMP +6,77%.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, "
    "Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, "
    "C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, "
    "Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, "
    "WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, IPFBW, IGRETEC, "
    "Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
    "Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2061":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after WZC Christine — Ter Burg YE2025 Medium"
        x["notes"] = (
            "tick2061 Ter Burg Medium omzet JUMP 7.88m pnl DEEPER LOSS 0.48m equity DROP 10.67m bruto DROP 7.17m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2062; next every-10 2070"
        )
        x["instructions"] = (
            "Completed leftover Ter Burg YE2025 Medium CW; KBO 0479.401.318; "
            f"omzet JUMP {OMZET} pnl DEEPER LOSS {PNL} equity DROP {EQUITY} bruto DROP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2062" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2062",
            "title": "leftover dual hole-fill after WZC Ter Burg",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2061 after Ter Burg YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(OLV Wezembeek / Sint-Antonius YE2025 deferred if still live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2061 Ter Burg; next every-10 2070",
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
        "last_unit_id": "rq_2061",
        "ticks_completed": "2061",
        "paused": "no",
        "notes": (
            "tick2061 leftover Ter Burg 0479.401.318 Medium CW (omzet JUMP 7.88m pnl DEEPER LOSS 0.48m equity DROP 10.67m bruto DROP 7.17m FTE 88.3; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2062; next every-10 2070; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2061 - 2026-08-24T20:20:00Z - rq_2061 Ter Burg (omzet JUMP 7.88m / pnl DEEPER LOSS 0.48m / Medium)

- Unit: **rq_2061** leftover dual after **rq_2060 Christine**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **WZC Ter Burg** YE2025 (KBO **0479.401.318**; Leuvensesteenweg 653 Zaventem-Nossegem; Vlaams-Brabant **aanbestedende-overheid VZW** WZC / **1 VE**). OLV Wezembeek / Sint-Antonius YE2025 also live - deferred. Do not redo Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR7,875,893** JUMP +6.77%; pnl **LOSS EUR-483,158** DEEPER vs YE2024 LOSS EUR-209,221; equity **EUR10,671,689** DROP -7.82%; bruto **EUR7,166,919** DROP -1.51%; FTE **88.3**; neerlegging **07.04.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 1 VE; email info@terburg.be.
- Wrote: sources (+6); budgets (+5); commitments (+1); leaderboard (+1 pi 5.0); entities (+1 vzw_wzc_ter_burg); foi + draft {GAP}; rq_2061=done + rq_2062 open; loop_state ticks=2061; raw under docs/doge/data/raw/tick2061/.
- FOI: **ready not sent** (human-gated; info@terburg.be).
- NOT every-10 (**next every-10 is 2070**). Next: rq_2062 (AGB/FARO-if-YE2025 / AIESH-REW / Wezembeek-Antonius deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2061")
