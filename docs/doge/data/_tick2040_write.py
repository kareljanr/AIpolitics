# ephemeral tick2040 — EVERY-10 + Woonzorg Samen Ouder YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T14:40:00Z"
ENTITY = "vzw_woonzorg_samen_ouder"
GAP = "gap_samen_ouder_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_samen_ouder_jr2025_cw"
SRC_EN = "src_samen_ouder_jr2025_cw_en"
SRC_FR = "src_samen_ouder_jr2025_cw_fr"
SRC_KBO = "src_samen_ouder_kbo_2040"
SRC_SITE = "src_samen_ouder_site_2040"

OMZET = "35265194"
PNL = "1416405"
EQUITY = "14440565"
BRUTO = "31884602"
FTE = "393"
OMZET24 = "32987159"
PNL24 = "123405"
EQUITY24 = "13498724"
BRUTO24 = "29551217"
# pi = 0.55*5.5 + 0.35*6.0 + 0.10*(10-4) = 3.025 + 2.1 + 0.6 = 5.725
PI = "5.725"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def count_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2040")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Woonzorg Samen Ouder YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0453287037/woonzorg-samen-ouder",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2040 EVERY-10; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 06.08.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2040/samen_ouder_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Woonzorg Samen Ouder YE2025 statutory",
        "url": "https://www.companyweb.be/en/0453287037/woonzorg-samen-ouder",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2040 EVERY-10; EN mirror YE2025 Medium; filed 06-08-2026; Last balance sheet year 2025; FTE 393; raw docs/doge/data/raw/tick2040/samen_ouder_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Woonzorg Samen Ouder YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0453287037/woonzorg-samen-ouder",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2040 EVERY-10; FR mirror YE2025 Medium; déposés le 06-08-2026; raw docs/doge/data/raw/tick2040/samen_ouder_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Woonzorg Samen Ouder 0453.287.037 Actief VZW Sint-Niklaas",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0453287037",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2040; Actief VZW; Tereken 14 9100 Sint-Niklaas; 5 VE; KBO email empty; rechtsvorm VZW sinds 16.03.1994",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "samenouder.be Woonzorg Samen Ouder contact",
        "url": "https://samenouder.be/contact/",
        "publisher": "Woonzorg Samen Ouder vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2040; info@samenouder.be; Tereken 14 9100 Sint-Niklaas; 03 760 03 80; 6 WZC Waasland; raw docs/doge/data/raw/tick2040/samenouder_contact.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_samen_ouder_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2040 EVERY-10; omzet JUMP {OMZET} +6.91pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_samen_ouder_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2040 EVERY-10; pnl JUMP {PNL} +1047.8pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_samen_ouder_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2040 EVERY-10; equity JUMP {EQUITY} +6.98pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_samen_ouder_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2040 EVERY-10; bruto JUMP {BRUTO} +7.90pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_samen_ouder_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2040 EVERY-10; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_samen_ouder_jr2025_statutory_wzc",
    "title": "Woonzorg Samen Ouder YE2025 leftover dual (omzet JUMP 35.27m / pnl JUMP 1.42m)",
    "entity_id": ENTITY,
    "beneficiary": "Waasland elderly care residents (Sint-Niklaas multi-campus WZC)",
    "legal_basis": "VZW WZC operator (KBO 0453.287.037)",
    "decision_date": "2026-08-06",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0453287037/woonzorg-samen-ouder",
    "stated_goal": "Residential elderly care Waasland (6 WZC campuses)",
    "cut_option": "Publish NBB PDF assets/debt + pnl JUMP FOI; map public subsidies vs resident fees",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>SintNiklaas>SamenOuder>JR2025_statutory_L5",
    "notes": "tick2040 EVERY-10; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Linde deferred; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_samen_ouder_omzet_jump_35_27m_pnl_jump_1_42m_jr2025",
    "name": "Woonzorg Samen Ouder omzet JUMP 35.27m / pnl JUMP 1.42m (YE2025)",
    "level": "L5",
    "type": "flemish_wzc_vzw_dual",
    "hierarchy_path": "OostVlaanderen>SintNiklaas>SamenOuder>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Waasland elderly via Samen Ouder VZW (Sint-Niklaas multi-campus)",
    "stated_goal": "Residential elderly care Waasland",
    "measured_outcome": "Medium CW YE2025; 35.27m omzet JUMP +6.91pct with pnl JUMP +1048pct (0.12m to 1.42m); NBB PDF residual",
    "absurdity_score": "6.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl JUMP vs public care euros; map subsidy vs resident fees",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2040 EVERY-10 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2050",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorg Samen Ouder (Sint-Niklaas)",
    "name_fr": "Woonzorg Samen Ouder (Saint-Nicolas)",
    "name_en": "Woonzorg Samen Ouder residential care (Sint-Niklaas)",
    "level": "vzw",
    "parent_id": "prov_oost_vlaanderen",
    "community_language": "nl",
    "website": "https://samenouder.be/",
    "foi_email": "info@samenouder.be",
    "foi_postal": "Tereken 14, 9100 Sint-Niklaas",
    "notes": "tick2040 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0453.287.037 Actief VZW; omzet JUMP 35.27m pnl JUMP 1.42m equity JUMP 14.44m bruto JUMP 31.88m FTE 393; assets/debt Unknown; neerlegging 06.08.2026; 5 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Linde YE2025 deferred; do not redo C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/OLV Roosdaal/Sint-Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have",
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
    "hierarchy_path": "OostVlaanderen>SintNiklaas>SamenOuder>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs resident-fee split; pnl JUMP recon (0.12m YE2024 to 1.42m YE2025)",
    "why_it_matters": "Medium CW shows 35.27m omzet Waasland multi-campus WZC VZW with ~11x pnl JUMP without balance sheet or subsidy transparency",
    "priority": "8",
    "recipient_body": "Woonzorg Samen Ouder vzw",
    "recipient_email": "info@samenouder.be",
    "recipient_postal": "Tereken 14, 9100 Sint-Niklaas",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_samen_ouder_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_samen_ouder_omzet_jump_35_27m_pnl_jump_1_42m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2040 EVERY-10; human-send only; Medium CW; next every-10 2050",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Woonzorg Samen Ouder (NBB PDF / assets-debt / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorg Samen Ouder vzw — KBO **0453.287.037**  
**recipient:** info@samenouder.be · Tereken 14, 9100 Sint-Niklaas  
**sources:** [CW NL](https://www.companyweb.be/nl/0453287037/woonzorg-samen-ouder) · [CW EN](https://www.companyweb.be/en/0453287037/woonzorg-samen-ouder) · [CW FR](https://www.companyweb.be/fr/0453287037/woonzorg-samen-ouder) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0453287037) · [site](https://samenouder.be/contact/)  
**tick:** 2040 (EVERY-10)  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **06.08.2026**): omzet **EUR35,265,194** JUMP +6.91%; pnl **EUR1,416,405** JUMP +1047.8% vs YE2024 EUR123,405; equity **EUR14,440,565** JUMP +6.98%; bruto **EUR31,884,602** JUMP +7.90%; FTE **393**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. C.W.Z.C. Zonhoven / Orelia already mined. De Linde YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorg Samen Ouder vzw — Tereken 14, 9100 Sint-Niklaas
info@samenouder.be
cc: Agentschap Zorg en Gezondheid / Provincie Oost-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Woonzorg Samen Ouder + balans (KBO 0453.287.037)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 06.08.2026).
2. Assets / schulden LT-ST / cash.
3. Split publieke subsidies vs residentiële dagprijzen/inkomsten 2025.
4. Toelichting pnl JUMP (van EUR123.405 YE2024 naar EUR1.416.405 YE2025).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

# EVERY-10 inventory after writes
n_bud = count_rows("docs/doge/data/budgets.csv")
n_comm = count_rows("docs/doge/data/commitments.csv")
n_lb = count_rows("docs/doge/data/leaderboard.csv")
n_ent = count_rows("docs/doge/data/entities.csv")
n_src = count_rows("docs/doge/data/sources.csv")
with open("docs/doge/data/foi_queue.csv", encoding="utf-8", newline="") as f:
    frows2 = list(csv.DictReader(f))
n_foi = len(frows2)
n_ready = sum(1 for x in frows2 if (x.get("status") or "").lower() == "ready")
n_ans = sum(1 for x in frows2 if (x.get("status") or "").lower() == "answered")
n_part = sum(1 for x in frows2 if (x.get("status") or "").lower() == "partial")

progress = Path("docs/doge/data/progress_every_10_ticks.md")
prog_text = progress.read_text(encoding="utf-8")
snapshot = f"""## Snapshot at **tick 2040** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2031-2040 WZC/psych continuum after 2030 Sint-Jozef Rillaar |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2031-2040 is residual dual L5 (not near-complete of 348bn):** **WZC St Vincentius Antwerpen/Ekeren** omzet JUMP **7.55m** · **WZC OLV Lourdes Kortenberg** omzet JUMP **10.97m** · **Cassiers WZC** omzet JUMP **7.20m** · **WZC Sint-Bernardus Assenede** omzet JUMP **6.36m** · **WZC OLV Roosdaal** omzet JUMP **7.60m** · **OLVA Antwerpen** omzet DROP **10.81m** · **WZC Kanunnik Triest** omzet JUMP **7.78m** · **Orelia Zorg** omzet JUMP **65.23m** / pnl LOSS / equity CRATER · **C.W.Z.C. Zonhoven** omzet JUMP **8.56m** / pnl FLIP · **Woonzorg Samen Ouder** omzet JUMP **35.27m** / pnl JUMP Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **~{n_ans}**; partial **~{n_part}**; total FOI rows **~{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital/psych shells** (**NEW 2031-2040** St Vincentius Antwerpen · Lourdes Kortenberg · Cassiers · Sint-Bernardus Assenede · OLV Roosdaal · OLVA · Kanunnik Triest · **Orelia** · **C.W.Z.C. Zonhoven** · **Samen Ouder** · prior 2021-2030 Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2040)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {n_bud} |
| commitments.csv | {n_comm} |
| leaderboard.csv | {n_lb} |
| entities.csv | {n_ent} |
| sources.csv | {n_src} |
| FOI ready | {n_ready} |
| FOI answered | {n_ans} |
| FOI partial | {n_part} |
| FOI total rows | {n_foi} |
| research_queue open | rq_2041 after progress |

### What improved since tick 2030

- **Residual dual (tick2031-2040):** **WZC St Vincentius Antwerpen/Ekeren** · **WZC OLV Lourdes Kortenberg** · **Cassiers WZC** · **WZC Sint-Bernardus Assenede** · **WZC OLV Roosdaal** · **OLVA Antwerpen** · **WZC Kanunnik Triest** · **Orelia Zorg** · **C.W.Z.C. Zonhoven** · **Woonzorg Samen Ouder** (this tick EVERY-10 dual — Oost-Vlaanderen Waasland WZC VZW YE2025 Medium CW).
- **Blocked still:** AGB Bornem JR2024-only · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH 0201.712.587 / REW YE2024-only · Jessa/ZOL CW N/A omzet · Bethanie Zoersel Emmaüs double-count · Veilige Have / Zusterhof / Molenheide already mined · prior Eneco deposit FOI stack. **Deferred live:** WZC De Linde Lievegem YE2025.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **2050**.


"""
if "## Snapshot at **tick 2040**" not in prog_text:
    anchor = "## Snapshot at **tick 2030**"
    if anchor in prog_text:
        prog_text = prog_text.replace(anchor, snapshot + anchor, 1)
    else:
        prog_text = prog_text + "\n" + snapshot
    progress.write_text(prog_text, encoding="utf-8")
    print("progress refreshed")
else:
    print("progress already has tick 2040")

top10 = Path("docs/doge/data/doge_waste_top10_current.md")
top10.write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2040** (2026-08-24) · **{n_lb}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW residual 2031-2040:** **Orelia omzet 65.23m** · **Samen Ouder omzet 35.27m** · **OLVA omzet 10.81m** · **Lourdes Kortenberg omzet 10.97m** · **C.W.Z.C. Zonhoven omzet 8.56m** · **Kanunnik Triest omzet 7.78m** · **OLV Roosdaal omzet 7.60m** · **St Vincentius Antwerpen omzet 7.55m** · **Cassiers omzet 7.20m** · **Sint-Bernardus Assenede omzet 6.36m** · prior 2021-2030 Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hiëronymus/hospital stack retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2030:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2031-2040 (off pure top10 / dual):** St Vincentius Antwerpen · Lourdes · Cassiers · Bernardus Assenede · Roosdaal · OLVA · Kanunnik Triest · Orelia · C.W.Z.C. Zonhoven · **Samen Ouder** (EVERY-10 dual). Count NEW since 2030: 10 residual dual ticks. **Prior 2021-2030 stack retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 refreshed")

do_not_redo = (
    "Do NOT redo Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, "
    "WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, WZC Sint-Carolus Ternat, "
    "WZC Zilverbos Zelzate, Sint Carolus Mayerhof, Evara, Multiversum (same CW as Evara), Maria Rustoord Ingelmunster, "
    "PPC Pittem, WZC Sint-Vincentius Avelgem, PC Sint-Hiëronymus, WZC Sint-Barbara Herselt, PC Gent-Sleidinge, "
    "AZ Rivierenland, AZ Zeno, Heilig Hart Tienen, Heilig Hart Leuven, Sint-Trudo, Sint-Andries Tielt, Heilig Hart Lier, "
    "Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, "
    "Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, "
    "Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, "
    "IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, "
    "BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
    "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
    "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, "
    "Tibi, IDELUX Environnement, IDELUX Eau, IDEA, Molenheide WZC, Veilige Have, Witte Meren. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart/Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica/Sint-Jan Brugge/"
    "Klina/Diest/Oudenaarde/Sint-Lucas/UZ Gent CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
)

for x in qrows:
    if x.get("task_id") == "rq_2040":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after C.W.Z.C. Zonhoven — Woonzorg Samen Ouder YE2025 Medium"
        x["notes"] = (
            "tick2040 EVERY-10 + Woonzorg Samen Ouder Medium omzet JUMP 35.27m pnl JUMP 1.42m equity JUMP 14.44m; FOI ready; "
            "progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Linde deferred; next rq_2041; next every-10 2050"
        )
        x["instructions"] = (
            "Completed EVERY-10 progress+top10 + leftover Woonzorg Samen Ouder YE2025 Medium CW; KBO 0453.287.037; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2041" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2041",
            "title": "leftover dual hole-fill after Woonzorg Samen Ouder EVERY-10",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2040 EVERY-10 after Woonzorg Samen Ouder YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(WZC De Linde Lievegem YE2025 live deferred / other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2040 EVERY-10 Samen Ouder; next every-10 2050; De Linde YE2025 deferred",
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
        "last_unit_id": "rq_2040",
        "ticks_completed": "2040",
        "paused": "no",
        "notes": (
            "tick2040 EVERY-10 + leftover Woonzorg Samen Ouder 0453.287.037 Medium CW (omzet JUMP 35.27m pnl JUMP 1.42m equity JUMP 14.44m bruto JUMP 31.88m FTE 393; "
            "assets/debt Unknown); progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; De Linde deferred; next rq_2041; next every-10 2050; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2040 - {UTC} - rq_2040 EVERY-10 + Woonzorg Samen Ouder (omzet JUMP 35.27m / pnl JUMP 1.42m / Medium)

- Unit: **rq_2040** EVERY-10 mandatory + leftover dual after **rq_2039 C.W.Z.C. Zonhoven**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **Woonzorg Samen Ouder** YE2025 (KBO **0453.287.037**; Tereken 14 Sint-Niklaas; Oost-Vlaanderen **WZC VZW** / 5 VE / Waasland multi-campus). De Linde YE2025 also live — deferred. Do not redo C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hiëronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have.
- EVERY-10: refreshed **progress_every_10_ticks.md** (tick 2040 snapshot; residual dual 2031-2040) + **doge_waste_top10_current.md** (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual dual off-top10).
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR35,265,194** JUMP +6.91%; pnl **EUR1,416,405** JUMP +1047.8%; equity **EUR14,440,565** JUMP +6.98%; bruto **EUR31,884,602** JUMP +7.90%; FTE **393**; neerlegging **06.08.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 5 VE; email info@samenouder.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; progress+top10; rq_2040=done + rq_2041 open; loop_state ticks=2040; raw under docs/doge/data/raw/tick2040/.
- FOI: **ready not sent** (human-gated; info@samenouder.be).
- EVERY-10 done. Next every-10 **2050**. Next: rq_2041 (AGB/FARO-if-YE2025 / AIESH-REW / De Linde deferred / unused DSO-IGS-HVZ).

### Every-10 brief (A/B/C/D/E)
- **A** L0 TE: **100%** (EUR347.956bn Strong)
- **B** L1 subsectors: **100%** unconsol. map Strong
- **C** L2 entity totals: **~99%** OoM (+ residual dual 2031-2040)
- **D** L5 named end-lines: **~74-88%** TE generous (residual dual gain; not near-complete of 348bn)
- **E** FOI-ready: **~{n_ready}** drafts; answered ~{n_ans}; partial ~{n_part}; total ~{n_foi}
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2040 Samen Ouder", OMZET, "pi", PI)
