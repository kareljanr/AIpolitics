# ephemeral tick2050 — EVERY-10 + Hof ter Waarbeek YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T17:40:00Z"
ENTITY = "vzw_wzc_hof_ter_waarbeek"
GAP = "gap_hof_ter_waarbeek_nbb_pdf_assets_debt_equity_jump_matrix_l5"
SRC = "src_hof_waarbeek_jr2025_cw"
SRC_EN = "src_hof_waarbeek_jr2025_cw_en"
SRC_FR = "src_hof_waarbeek_jr2025_cw_fr"
SRC_KBO = "src_hof_waarbeek_kbo_2050"
SRC_SITE = "src_hof_waarbeek_site_2050"

OMZET = "6323859"
PNL = "346911"
EQUITY = "2415849"
BRUTO = "5934453"
FTE = "74.1"
OMZET24 = "6263462"
PNL24 = "342816"
EQUITY24 = "2068939"
BRUTO24 = "5854843"
# pi = 0.55*4.5 + 0.35*4.3 + 0.10*(10-4) = 2.475 + 1.505 + 0.6 = 4.58 → 4.6
PI = "4.6"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2050")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Hof ter Waarbeek YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0478728256/woonzorgcentrum-hof-ter-waarbeek",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2050 EVERY-10; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 02.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2050/hof_waarbeek_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Hof ter Waarbeek YE2025 statutory",
        "url": "https://www.companyweb.be/en/0478728256/woonzorgcentrum-hof-ter-waarbeek",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2050 EVERY-10; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; FTE 74.1; raw docs/doge/data/raw/tick2050/hof_waarbeek_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Hof ter Waarbeek YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0478728256/woonzorgcentrum-hof-ter-waarbeek",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2050 EVERY-10; FR mirror YE2025 Medium; depose le 02-07-2026; raw docs/doge/data/raw/tick2050/hof_waarbeek_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Hof ter Waarbeek 0478.728.256 Actief VZW aanbestedende overheid Asse",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0478728256",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2050 EVERY-10; Actief VZW; Waarbeek 28 1730 Asse; 1 VE; aanbestedende overheid sinds 27.09.2002; NACE 87.101; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Hof ter Waarbeek site info@waarbeek.be",
        "url": "https://www.hofterwaarbeek-wzc.be/",
        "publisher": "WZC Hof ter Waarbeek",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2050 EVERY-10; site lists info@waarbeek.be; raw docs/doge/data/raw/tick2050/hof_waarbeek_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_hof_waarbeek_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2050 EVERY-10; omzet JUMP {OMZET} +0.96pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_hof_waarbeek_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2050 EVERY-10; pnl JUMP {PNL} +1.19pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_hof_waarbeek_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2050 EVERY-10; equity JUMP {EQUITY} +16.77pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_hof_waarbeek_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2050 EVERY-10; bruto JUMP {BRUTO} +1.36pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_hof_waarbeek_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2050 EVERY-10; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_hof_waarbeek_jr2025_statutory_wzc",
    "title": "Hof ter Waarbeek YE2025 leftover dual (omzet JUMP 6.32m / equity JUMP 2.42m)",
    "entity_id": ENTITY,
    "beneficiary": "Vlaams-Brabant elderly-care residents (WZC Hof ter Waarbeek Asse)",
    "legal_basis": "VZW WZC operator / aanbestedende overheid (KBO 0478.728.256)",
    "decision_date": "2026-07-02",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0478728256/woonzorgcentrum-hof-ter-waarbeek",
    "stated_goal": "WZC Hof ter Waarbeek Asse",
    "cut_option": "Publish NBB PDF assets/debt + explain equity JUMP +16.77pct FOI",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Asse>HofTerWaarbeek>JR2025_statutory_L5",
    "notes": "tick2050 EVERY-10; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_hof_waarbeek_omzet_jump_6_32m_equity_jump_jr2025",
    "name": "Hof ter Waarbeek omzet JUMP 6.32m / equity JUMP 2.42m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_aanbestedende_overheid_dual",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Asse>HofTerWaarbeek>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; aanbestedende overheid VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Vlaams-Brabant elderly-care residents via Hof ter Waarbeek Asse",
    "stated_goal": "WZC Hof ter Waarbeek",
    "measured_outcome": "Medium CW YE2025; 6.32m omzet JUMP +0.96pct; equity JUMP +16.77pct; NBB PDF residual",
    "absurdity_score": "4.3",
    "cost_score": "4.5",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain equity JUMP; map subsidy stack",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2050 EVERY-10 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorgcentrum Hof ter Waarbeek (Asse)",
    "name_fr": "Maison de repos et de soins Hof ter Waarbeek (Asse)",
    "name_en": "Hof ter Waarbeek nursing home (Asse)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.hofterwaarbeek-wzc.be/",
    "foi_email": "info@waarbeek.be",
    "foi_postal": "Waarbeek 28, 1730 Asse",
    "notes": (
        "tick2050 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0478.728.256 Actief VZW aanbestedende overheid 1 VE; omzet JUMP 6.32m pnl JUMP 0.35m equity JUMP 2.42m bruto JUMP 5.93m FTE 74.1; "
        "assets/debt Unknown; neerlegging 02.07.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara"
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
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Asse>HofTerWaarbeek>NBB_PDF_assets_debt_equity_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of equity JUMP +16.77pct",
    "why_it_matters": "Medium CW shows 6.32m omzet VL aanbestedende-overheid WZC VZW with equity JUMP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Woonzorgcentrum Hof ter Waarbeek vzw",
    "recipient_email": "info@waarbeek.be",
    "recipient_postal": "Waarbeek 28, 1730 Asse",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_hof_waarbeek_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_hof_waarbeek_omzet_jump_6_32m_equity_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2050 EVERY-10; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Hof ter Waarbeek (NBB PDF / assets-debt / equity-jump matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum Hof ter Waarbeek VZW — KBO **0478.728.256**  
**recipient:** info@waarbeek.be · Waarbeek 28, 1730 Asse  
**sources:** [CW NL](https://www.companyweb.be/nl/0478728256/woonzorgcentrum-hof-ter-waarbeek) · [CW EN](https://www.companyweb.be/en/0478728256/woonzorgcentrum-hof-ter-waarbeek) · [CW FR](https://www.companyweb.be/fr/0478728256/woonzorgcentrum-hof-ter-waarbeek) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0478728256) · [site](https://www.hofterwaarbeek-wzc.be/)  
**tick:** 2050 (EVERY-10)  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **02.07.2026**): omzet **EUR6,323,859** JUMP +0.96%; pnl **EUR346,911** JUMP +1.19%; equity **EUR2,415,849** JUMP +16.77%; bruto **EUR5,934,453** JUMP +1.36%; FTE **74.1**; assets/debt **Unknown**.
- KBO: Actief VZW **aanbestedende overheid**; **1 VE**; zetel Waarbeek 28 Asse.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum Hof ter Waarbeek vzw — Waarbeek 28, 1730 Asse
info@waarbeek.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Hof ter Waarbeek + equity JUMP (KBO 0478.728.256)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (VZW is aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 02.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting equity JUMP (van EUR2.068.939 YE2024 naar EUR2.415.849 YE2025 = +16.77%).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

# inventory after writes
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
marker = "## Snapshot at **tick 2040**"
idx = old.find(marker)
head = old[: idx if idx >= 0 else old.find("---") + 4]
tail = old[idx:] if idx >= 0 else old
snap = f"""
## Snapshot at **tick 2050** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2041-2050 WZC/AGB continuum after 2040 Samen Ouder |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2041-2050 is residual dual L5 (not near-complete of 348bn):** **WZC De Linde Lievegem** omzet JUMP **8.54m** · **Psychogeriatrisch Centrum** omzet FLAT **53.40m** · **Zorggroep Zusters van Berlaar** omzet JUMP **77.35m** · **WZC De Verlosser Dilbeek** omzet JUMP **3.02m** · **AGB Bornem** assets JUMP **21.87m** / debt **20.50m** Strong · **Curando** omzet JUMP **87.69m** · **Integro** omzet JUMP **63.70m** · **Ter Kimme** omzet JUMP **8.54m** · **WZC Huize Vincent** omzet JUMP **6.38m** / pnl DEEPER LOSS · **Hof ter Waarbeek** omzet JUMP **6.32m** / equity JUMP Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{foi_ready}** drafts ready | Human send only; answered **~{foi_ans}**; partial **~{foi_part}**; total FOI rows **~{foi_tot}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital/psych shells** (**NEW 2041-2050** De Linde · Psychogeriatrisch · Zusters Berlaar · De Verlosser · **AGB Bornem** · **Curando** · **Integro** · **Ter Kimme** · **Huize Vincent** · **Hof ter Waarbeek** · prior 2031-2040 / 2021-2030 stacks retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2050)

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
| research_queue open | rq_2051 after progress |

### What improved since tick 2040

- **Residual dual (tick2041-2050):** **WZC De Linde Lievegem** · **Psychogeriatrisch Centrum** · **Zorggroep Zusters van Berlaar** · **WZC De Verlosser Dilbeek** · **AGB Bornem** (Strong JR2024) · **Curando** · **Integro** · **Ter Kimme** · **WZC Huize Vincent** · **Hof ter Waarbeek** (this tick EVERY-10 dual — Vlaams-Brabant WZC VZW YE2025 Medium CW).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH 0201.712.587 / REW YE2024-only · Jessa/ZOL CW N/A omzet · Bethanie Zoersel Emmaüs double-count · Veilige Have / Zusterhof / Molenheide already mined · prior Eneco deposit FOI stack.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **2060**.


"""
# keep protocol header: find first --- after title block
proto_end = old.find("\n---\n")
if proto_end < 0:
    raise SystemExit("progress header marker missing")
proto = old[: proto_end + 5]
# after protocol, insert snap then previous snapshots starting at tick 2040
rest = old[proto_end + 5 :]
# strip leading whitespace/newlines before first Snapshot
rest = rest.lstrip("\n")
if not rest.startswith("## Snapshot"):
    # maybe How to read section exists — keep everything after protocol
    progress.write_text(proto + "\n" + snap + rest, encoding="utf-8")
else:
    progress.write_text(proto + "\n" + snap + rest, encoding="utf-8")
print("progress ok")

top10 = Path("docs/doge/data/doge_waste_top10_current.md")
top10.write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2050** (2026-08-24) · **{n_lb}** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW residual 2041-2050:** **Curando omzet 87.69m** · **Zusters Berlaar omzet 77.35m** · **Integro omzet 63.70m** · **Psychogeriatrisch omzet 53.40m** · **AGB Bornem assets 21.87m** · **Ter Kimme omzet 8.54m** · **De Linde omzet 8.54m** · **Huize Vincent omzet 6.38m** · **Hof ter Waarbeek omzet 6.32m** · **De Verlosser omzet 3.02m** · prior 2031-2040 Orelia/Samen Ouder/OLVA/Lourdes/CWZC/Kanunnik/Roosdaal/Vincentius Antwerpen/Cassiers/Bernardus stack retained · prior 2021-2030 Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Maria Rustoord/PPC Pittem/Vincentius Avelgem/PC Sint-Hieronymus/hospital stack retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2040:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2041-2050 (off pure top10 / dual):** De Linde · Psychogeriatrisch · Zusters Berlaar · De Verlosser · AGB Bornem · Curando · Integro · Ter Kimme · Huize Vincent · **Hof ter Waarbeek** (EVERY-10 dual). Count NEW since 2040: 10 residual dual ticks. **Prior 2031-2040 + 2021-2030 stacks retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 ok")

do_not_redo = (
    "Do NOT redo Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, "
    "Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, "
    "Molenheide WZC, Veilige Have, Witte Meren, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2050":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after Huize Vincent — Hof ter Waarbeek YE2025 Medium"
        x["notes"] = (
            "tick2050 EVERY-10 + Hof ter Waarbeek Medium omzet JUMP 6.32m pnl JUMP 0.35m equity JUMP 2.42m bruto JUMP 5.93m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2051; next every-10 2060"
        )
        x["instructions"] = (
            "Completed EVERY-10 + leftover Hof ter Waarbeek YE2025 Medium CW; KBO 0478.728.256; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2051" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2051",
            "title": "leftover dual hole-fill after Hof ter Waarbeek",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2050 after EVERY-10 + Hof ter Waarbeek YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2050 EVERY-10 Hof ter Waarbeek; next every-10 2060",
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
        "last_unit_id": "rq_2050",
        "ticks_completed": "2050",
        "paused": "no",
        "notes": (
            "tick2050 EVERY-10 + leftover Hof ter Waarbeek 0478.728.256 Medium CW (omzet JUMP 6.32m pnl JUMP 0.35m equity JUMP 2.42m bruto JUMP 5.93m FTE 74.1; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2051; next every-10 2060; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2050 - {UTC} - rq_2050 EVERY-10 + Hof ter Waarbeek (omzet JUMP 6.32m / equity JUMP 2.42m / Medium)

- Unit: **rq_2050** EVERY-10 mandatory + leftover dual after **rq_2049 WZC Huize Vincent**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **Hof ter Waarbeek** YE2025 (KBO **0478.728.256**; Waarbeek 28 Asse; Vlaams-Brabant **aanbestedende-overheid VZW** WZC / **1 VE**). Do not redo Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hieronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren.
- EVERY-10: refreshed **progress_every_10_ticks.md** (tick 2050 snapshot; residual dual 2041-2050) + **doge_waste_top10_current.md** (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual dual off-top10).
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR6,323,859** JUMP +0.96%; pnl **EUR346,911** JUMP +1.19%; equity **EUR2,415,849** JUMP +16.77%; bruto **EUR5,934,453** JUMP +1.36%; FTE **74.1**; neerlegging **02.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 1 VE; email info@waarbeek.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; progress+top10; rq_2050=done + rq_2051 open; loop_state ticks=2050; raw under docs/doge/data/raw/tick2050/.
- FOI: **ready not sent** (human-gated; info@waarbeek.be).
- EVERY-10 done. Next every-10 **2060**. Next: rq_2051 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).

### Every-10 brief (A/B/C/D/E)
- **A** L0 TE: **100%** (EUR347.956bn Strong)
- **B** L1 subsectors: **100%** unconsol. map Strong
- **C** L2 entity totals: **~99%** OoM (+ residual dual 2041-2050)
- **D** L5 named end-lines: **~74-88%** TE generous (residual dual gain; not near-complete of 348bn)
- **E** FOI-ready: **~{foi_ready}** drafts; answered ~{foi_ans}; partial ~{foi_part}; total ~{foi_tot}
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2050 Hof ter Waarbeek EVERY-10", OMZET, "pi", PI)
