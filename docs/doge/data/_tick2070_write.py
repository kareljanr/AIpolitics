# ephemeral tick2070 — EVERY-10 + WZC Welvaart YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T22:35:00Z"
ENTITY = "vzw_wzc_welvaart"
GAP = "gap_welvaart_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_welvaart_jr2025_cw"
SRC_EN = "src_welvaart_jr2025_cw_en"
SRC_FR = "src_welvaart_jr2025_cw_fr"
SRC_KBO = "src_welvaart_kbo_2070"
SRC_SITE = "src_welvaart_site_2070"
SRC_FOLDER = "src_welvaart_folder_2070"

OMZET = "8759815"
PNL = "357438"
EQUITY = "9779728"
BRUTO = "9226365"
FTE = "111.8"
OMZET24 = "8636093"
PNL24 = "400821"
EQUITY24 = "8737290"
BRUTO24 = "8976016"
# pi = 0.55*4.8 + 0.35*4.9 + 0.10*(10-4) = 2.64 + 1.715 + 0.6 = 4.955 → 5.0
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
r = next(x for x in qrows if x.get("task_id") == "rq_2070")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Woonzorgcentrum Welvaart YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0408516488/woonzorgcentrum-welvaart",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2070 EVERY-10; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 04.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2070/welvaart_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Woonzorgcentrum Welvaart YE2025 statutory",
        "url": "https://www.companyweb.be/en/0408516488/woonzorgcentrum-welvaart",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2070 EVERY-10; EN mirror YE2025 Medium; filed 04-07-2026; Last balance sheet year 2025; FTE 111.8; raw docs/doge/data/raw/tick2070/welvaart_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Woonzorgcentrum Welvaart YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0408516488/woonzorgcentrum-welvaart",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2070 EVERY-10; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2070/welvaart_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woonzorgcentrum Welvaart 0408.516.488 Actief VZW Kapellen",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408516488",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2070 EVERY-10; Actief VZW; Hoogboomsteenweg 124 2950 Kapellen; 1 VE on KBO (FinCheck lists 2 campuses); NACE 87.101; tel 03/660.06.90; NOT aanbestedende in KBO extract; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "WoonZorgCollectief / Welvaart site",
        "url": "https://woonzorgcollectief.be/",
        "publisher": "WoonZorgCollectief / WZC Welvaart",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2070 EVERY-10; Welvaart member of WoonZorgCollectief with Compostela; FOI email welvaart@wzcwelvaart.be from folder PDF; raw docs/doge/data/raw/tick2070/welvaart_site.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FOLDER,
        "title": "WZC Welvaart folder welvaart@wzcwelvaart.be",
        "url": "https://www.woonzorgweb.be/sites/default/files/attachment/Folder%20Welvaart%20-%20WZC%20%2829.7%20x%2021%20cm%29.pdf",
        "publisher": "WZC Welvaart",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2070 EVERY-10; folder lists welvaart@wzcwelvaart.be / 03 660 06 90 / Hoogboomsteenweg 124 Kapellen",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_welvaart_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2070 EVERY-10; omzet JUMP {OMZET} +1.43pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_welvaart_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2070 EVERY-10; pnl DROP {PNL} -10.82pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_welvaart_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2070 EVERY-10; equity JUMP {EQUITY} +11.93pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_welvaart_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2070 EVERY-10; bruto JUMP {BRUTO} +2.79pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_welvaart_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2070 EVERY-10; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_welvaart_jr2025_statutory_wzc",
    "title": "WZC Welvaart YE2025 leftover dual (omzet JUMP 8.76m / pnl DROP 0.36m)",
    "entity_id": ENTITY,
    "beneficiary": "Kapellen elderly residents (WZC Welvaart / WoonZorgCollectief)",
    "legal_basis": "VZW WZC / publiek gesubsidieerde zorg (KBO 0408.516.488)",
    "decision_date": "2026-07-04",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0408516488/woonzorgcentrum-welvaart",
    "stated_goal": "WZC residential elderly care Kapellen Hoogboomsteenweg (WoonZorgCollectief)",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI; explain pnl DROP -10.82pct with equity JUMP +11.93pct",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Antwerpen>Kapellen>Welvaart>JR2025_statutory_L5",
    "notes": "tick2070 EVERY-10; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nlb = {
    **{k: "" for k in lfields},
    "item_id": "lb_welvaart_omzet_jump_8_76m_pnl_drop_jr2025",
    "name": "WZC Welvaart omzet JUMP 8.76m / pnl DROP 0.36m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>Antwerpen>Kapellen>Welvaart>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; WZC VZW dual WoonZorgCollectief",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Kapellen elderly residents via WZC Welvaart",
    "stated_goal": "WZC residential elderly care",
    "measured_outcome": "Medium CW YE2025; 8.76m omzet JUMP +1.43pct with pnl DROP -10.82pct and equity JUMP +11.93pct; NBB PDF residual",
    "absurdity_score": "4.9",
    "cost_score": "4.8",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP vs equity JUMP; map IFIC/Alivia vs dagprijs split",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2070 EVERY-10 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2080",
}
if not any(x.get("item_id") == nlb["item_id"] for x in lrows):
    lrows.append(nlb)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorgcentrum Welvaart (VZW WZC, Kapellen)",
    "name_fr": "Maison de repos Welvaart (ASBL MRS, Kapellen)",
    "name_en": "Woonzorgcentrum Welvaart (VZW nursing home Kapellen)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://woonzorgcollectief.be/",
    "foi_email": "welvaart@wzcwelvaart.be",
    "foi_postal": "Hoogboomsteenweg 124, 2950 Kapellen",
    "notes": (
        "tick2070 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0408.516.488 Actief VZW 1 VE (FinCheck 2 campuses); "
        "omzet JUMP 8.76m pnl DROP 0.36m equity JUMP 9.78m bruto JUMP 9.23m FTE 111.8; assets/debt Unknown; "
        "neerlegging 04.07.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; WoonZorgCollectief sister of Compostela; "
        "do not redo Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/"
        "Christine/Home Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/"
        "Hof Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zusters Berlaar/Psychogeriatrisch/"
        "De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus/Cassiers/Lourdes/"
        "Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof/"
        "Werken Glorieux/Woonhaven/Always Home/Armonea"
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
    "hierarchy_path": "Vlaanderen>Antwerpen>Kapellen>Welvaart>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl DROP -10.82pct with equity JUMP +11.93pct YE2025",
    "why_it_matters": "Medium CW shows 8.76m omzet WZC VZW with pnl DROP + equity JUMP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "WZC Welvaart vzw",
    "recipient_email": "welvaart@wzcwelvaart.be",
    "recipient_postal": "Hoogboomsteenweg 124, 2950 Kapellen",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_welvaart_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_welvaart_omzet_jump_8_76m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2070 EVERY-10; human-send only; Medium CW; next every-10 2080",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Woonzorgcentrum Welvaart (NBB PDF / assets-debt / pnl-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum Welvaart VZW — KBO **0408.516.488**  
**recipient:** welvaart@wzcwelvaart.be · Hoogboomsteenweg 124, 2950 Kapellen  
**sources:** [CW NL](https://www.companyweb.be/nl/0408516488/woonzorgcentrum-welvaart) · [CW EN](https://www.companyweb.be/en/0408516488/woonzorgcentrum-welvaart) · [CW FR](https://www.companyweb.be/fr/0408516488/woonzorgcentrum-welvaart) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408516488) · [WoonZorgCollectief](https://woonzorgcollectief.be/) · [folder PDF](https://www.woonzorgweb.be/sites/default/files/attachment/Folder%20Welvaart%20-%20WZC%20%2829.7%20x%2021%20cm%29.pdf)  
**tick:** 2070 (EVERY-10)  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **04.07.2026**): omzet **EUR8,759,815** JUMP +1.43%; pnl **EUR357,438** DROP −10.82% vs YE2024 EUR400,821; equity **EUR9,779,728** JUMP +11.93%; bruto **EUR9,226,365** JUMP +2.79%; FTE **111.8**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE** (FinCheck lists 2 campuses); zetel Hoogboomsteenweg 124 Kapellen; NACE 87.101; tel 03/660.06.90; NOT aanbestedende in KBO extract; WoonZorgCollectief sister of Compostela.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: WZC Welvaart vzw — Hoogboomsteenweg 124, 2950 Kapellen
welvaart@wzcwelvaart.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 WZC Welvaart + subsidiematrix (KBO 0408.516.488)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 04.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting daling winst van EUR400.821 (YE2024) naar EUR357.438 (YE2025; −10,82%) bij equity JUMP +11,93%.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

n_bud = len(brows)
n_comm = len(crows)
n_lb = len(lrows)
n_ent = len(erows)
n_src = len(srows)
foi_ready = sum(1 for x in frows if (x.get("status") or "").strip() == "ready")
foi_ans = sum(1 for x in frows if (x.get("status") or "").strip() == "answered")
foi_part = sum(1 for x in frows if (x.get("status") or "").strip() == "partial")
foi_tot = len(frows)

# EVERY-10 progress prepend
progress = Path("docs/doge/data/progress_every_10_ticks.md")
old = progress.read_text(encoding="utf-8")
snap = f"""
## Snapshot at **tick 2070** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2061-2070 WZC continuum after 2060 Christine |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2061-2070 is residual dual L5 (not near-complete of 348bn):** **Ter Burg** omzet JUMP **7.88m** · **OLV Wezembeek** omzet DROP **4.44m** · **Sint-Antonius** omzet JUMP **7.46m** · **Huize Sint-Jozef Ieper** omzet JUMP **8.36m** · **OLV Bornem** omzet JUMP **9.03m** · **Zusters SV Deinze** omzet DROP **10.95m** · **Leiehome** omzet JUMP **10.83m** · **Compostela** omzet JUMP **37.80m** · **Vulpia Vlaanderen** omzet JUMP **198.15m** · **WZC Welvaart** omzet JUMP **8.76m** / pnl DROP Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital/psych shells** (**NEW 2061-2070** Ter Burg · Wezembeek · Sint-Antonius · Huize SJ Ieper · OLV Bornem · Zusters Deinze · Leiehome · Compostela · **Vulpia** · **Welvaart** · prior 2051-2060 / 2041-2050 / 2031-2040 / 2021-2030 stacks retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2070)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {n_bud} |
| commitments.csv | {n_comm} |
| leaderboard.csv | {n_lb} |
| entities.csv | {n_ent} |
| sources.csv | {n_src} |
| FOI ready | {foi_ready} |
| FOI answered | {foi_ans} |
| FOI partial | {foi_part} |
| FOI total rows | {foi_tot} |
| research_queue open | rq_2071 after progress |

### What improved since tick 2060

- **Residual dual (tick2061-2070):** **Ter Burg** · **OLV Wezembeek** · **Sint-Antonius** · **Huize Sint-Jozef Ieper** · **OLV Bornem** · **Zusters SV Deinze** · **Leiehome** · **Compostela** · **Vulpia Vlaanderen** · **WZC Welvaart** (this tick EVERY-10 dual — Kapellen WZC VZW YE2025 Medium CW / WoonZorgCollectief).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH 0201.712.587 / REW YE2024-only · Always Home=Armonea skipped · Jessa/ZOL CW N/A omzet · prior Eneco deposit FOI stack.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **2080**.


"""
proto_end = old.find("\n---\n")
if proto_end < 0:
    raise SystemExit("progress header marker missing")
proto = old[: proto_end + 5]
rest = old[proto_end + 5 :].lstrip("\n")
progress.write_text(proto + "\n" + snap + rest, encoding="utf-8")
print("progress ok")

top10 = Path("docs/doge/data/doge_waste_top10_current.md")
top10.write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2070** (2026-08-24) · **{n_lb}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55·cost_score + 0.35·absurdity + 0.10·(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 4 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 9 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |
| 10 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW residual 2061-2070:** **Vulpia omzet 198.15m** · **Compostela omzet 37.80m** · **Zusters Deinze omzet 10.95m** · **Leiehome omzet 10.83m** · **OLV Bornem omzet 9.03m** · **Welvaart omzet 8.76m** · **Huize SJ Ieper omzet 8.36m** · **Ter Burg omzet 7.88m** · **Sint-Antonius omzet 7.46m** · **Wezembeek omzet 4.44m** · prior 2051-2060 Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde stack retained · prior 2041-2050 Curando/Zusters Berlaar/Integro/Psychogeriatrisch/AGB Bornem/Ter Kimme/De Linde/Huize Vincent/Hof ter Waarbeek/De Verlosser stack retained · prior 2031-2040 Orelia/Samen Ouder/OLVA/Lourdes/CWZC/Kanunnik/Roosdaal/Vincentius Antwerpen/Cassiers/Bernardus stack retained · prior 2021-2030 Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hieronymus/hospital stack retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2060:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2061-2070 (off pure top10 / dual):** Ter Burg · Wezembeek · Sint-Antonius · Huize SJ Ieper · OLV Bornem · Zusters Deinze · Leiehome · Compostela · Vulpia · **Welvaart** (EVERY-10 dual). Count NEW since 2060: 10 residual dual ticks. **Prior 2051-2060 + 2041-2050 + 2031-2040 + 2021-2030 stacks retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 ok")

do_not_redo = (
    "Do NOT redo WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, "
    "Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, "
    "WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, "
    "Seniorenzorg Lendelede, Walfergem, Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, "
    "Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, "
    "Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, "
    "WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, "
    "WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, "
    "Always Home, Armonea, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, "
    "Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, "
    "ETB, Elia, BNO, SWDE, BRUGEL. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2070":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after Vulpia — WZC Welvaart YE2025 Medium"
        x["notes"] = (
            "tick2070 EVERY-10 + Welvaart Medium omzet JUMP 8.76m pnl DROP 0.36m equity JUMP 9.78m bruto JUMP 9.23m; "
            "FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2071; next every-10 2080"
        )
        x["instructions"] = (
            "Completed EVERY-10 progress+top10 + leftover WZC Welvaart YE2025 Medium CW; KBO 0408.516.488; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2071" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2071",
            "title": "leftover dual hole-fill after WZC Welvaart",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2070 after EVERY-10 + WZC Welvaart YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2070 Welvaart EVERY-10; next every-10 2080",
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
        "last_unit_id": "rq_2070",
        "ticks_completed": "2070",
        "paused": "no",
        "notes": (
            "tick2070 EVERY-10 + leftover Welvaart 0408.516.488 Medium CW (omzet JUMP 8.76m pnl DROP 0.36m equity JUMP 9.78m bruto JUMP 9.23m FTE 111.8; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2071; next every-10 2080; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("loop_state ok")

log = Path("docs/doge/loop_log.md")
block = f"""


## Tick 2070 - 2026-08-24T22:35:00Z - rq_2070 EVERY-10 + WZC Welvaart (omzet JUMP 8.76m / pnl DROP 0.36m / Medium)

### EVERY-10 coverage (A–E of EUR 347.956 bn TE)
- **A:** 100% L0 TE Strong (NBB/ESA 2025).
- **B:** 100% L1 unconsol map Strong.
- **C:** ~99% L2 entity totals (order of magnitude) + residual dual 2061-2070 WZC continuum.
- **D:** ~74-88% generous L5; NEW 2061-2070 residual dual (Ter Burg 7.88m · OLV Wezembeek 4.44m · Sint-Antonius 7.46m · Huize Sint-Jozef Ieper 8.36m · OLV Bornem 9.03m · Zusters Deinze 10.95m · Leiehome 10.83m · Compostela 37.80m · Vulpia 198.15m · **Welvaart 8.76m**) — **not** near-complete of 348bn.
- **E:** ~{foi_ready} FOI-ready drafts; answered ~{foi_ans}; partial ~{foi_part}; total FOI rows ~{foi_tot}.

### Waste top10
- Pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). OWV snowball / Metro3 / corrupt AGB pi>10 filtered off. Refreshed `doge_waste_top10_current.md` + `progress_every_10_ticks.md`.

### Unit hole-fill
- Unit: **rq_2070** EVERY-10 mandatory + leftover dual after **rq_2069 Vulpia Vlaanderen**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Always Home=Armonea skipped. Took unused leftover **WZC Welvaart** YE2025 (KBO **0408.516.488**; Hoogboomsteenweg 124 Kapellen; Antwerpen **VZW** WZC / **1 VE** / WoonZorgCollectief sister of Compostela; FinCheck 2 campuses). Do not redo Vulpia/Compostela/Leiehome/Zusters SV Deinze/OLV Bornem/Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zusters Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik/OLVA/Roosdaal/Bernardus/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren/Zusterhof/Werken Glorieux/Woonhaven/Always Home/Armonea.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR8,759,815** JUMP +1.43%; pnl **EUR357,438** DROP −10.82%; equity **EUR9,779,728** JUMP +11.93%; bruto **EUR9,226,365** JUMP +2.79%; FTE **111.8**; neerlegging **04.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email welvaart@wzcwelvaart.be (folder PDF).
- Wrote: sources (+6); budgets (+5); commitments (+1); leaderboard (+1 pi 5.0); entities (+1 vzw_wzc_welvaart); foi + draft {GAP}; progress + top10 EVERY-10; rq_2070=done + rq_2071 open; loop_state ticks=2070; raw under docs/doge/data/raw/tick2070/.
- FOI: **ready not sent** (human-gated; welvaart@wzcwelvaart.be).
- EVERY-10 done. Next: rq_2071 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych). Next every-10 **2080**.
"""
log.write_text(log.read_text(encoding="utf-8") + block, encoding="utf-8")
print("log ok")
print("DONE tick2070")
