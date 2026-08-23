# ephemeral tick2010 — EVERY-10 + Vlaamse Zorgkas YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T06:55:00Z"
ENTITY = "vzw_vlaamse_zorgkas"
GAP = "gap_vlaamse_zorgkas_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_vlaamse_zorgkas_jr2025_cw"
SRC_EN = "src_vlaamse_zorgkas_jr2025_cw_en"
SRC_FR = "src_vlaamse_zorgkas_jr2025_cw_fr"
SRC_KBO = "src_vlaamse_zorgkas_kbo_2010"
SRC_SITE = "src_vlaamse_zorgkas_vl_2010"

OMZET = "193923835"
PNL = "154861"
EQUITY = "619261"
BRUTO = "4620876"
FTE = "0"
OMZET24 = "190022220"
PNL24 = "262200"
EQUITY24 = "464400"
BRUTO24 = "2773452"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2010")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Vlaamse Zorgkas YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0475581694/vlaamse-zorgkas",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2010 EVERY-10; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 02.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2010/zorgkas_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Vlaamse Zorgkas YE2025 statutory",
        "url": "https://www.companyweb.be/en/0475581694/vlaamse-zorgkas",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2010 EVERY-10; EN mirror YE2025 Medium; filed 02-06-2026; Last balance sheet year 2025; Other associations n.e.c.; Big; 0 FTE; raw docs/doge/data/raw/tick2010/zorgkas_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Vlaamse Zorgkas YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0475581694/vlaamse-zorgkas",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2010 EVERY-10; FR mirror YE2025 Medium; déposés le 02-06-2026; raw docs/doge/data/raw/tick2010/zorgkas_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Vlaamse Zorgkas 0475.581.694 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0475581694",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2010; Actief VZW since 10.05.2001; Simon Bolivarlaan 17 1000 Brussel; 0 VE; no KBO email; Normale toestand; Departement Zorg dual",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "vlaanderen.be Vlaamse Zorgkas official org page",
        "url": "https://www.vlaanderen.be/vlaamse-zorgkas",
        "publisher": "Vlaanderen.be / Departement Zorg",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2010; public VL zorgkas; vlaamsezorgkas@vlaanderen.be; Belpairegebouw Simon Bolivarlaan 17; post Koning Albert II-laan 15 bus 499 1210 Brussel",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_vlaamse_zorgkas_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2010 EVERY-10; omzet JUMP {OMZET} +2.05pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_vlaamse_zorgkas_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2010 EVERY-10; pnl DROP {PNL} -40.94pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_vlaamse_zorgkas_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2010 EVERY-10; equity JUMP {EQUITY} +33.35pct vs YE2024 {EQUITY24}; thin equity vs 194m omzet flow-through",
    },
    {
        "budget_id": "bud_vlaamse_zorgkas_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2010 EVERY-10; bruto JUMP {BRUTO} +66.61pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_vlaamse_zorgkas_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2010 EVERY-10; YE2025 FTE {FTE} (staff via Departement Zorg path)",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_vlaamse_zorgkas_jr2025_statutory_zorgkas",
    "title": "Vlaamse Zorgkas YE2025 EVERY-10 leftover dual (omzet JUMP 193.92m / pnl DROP 0.15m / equity JUMP 0.62m)",
    "entity_id": ENTITY,
    "beneficiary": "VL zorgpremie members / zorgbudget recipients / voorzieningen via derdebetaler",
    "legal_basis": "VZW/ASBL Vlaamse Zorgkas (KBO 0475.581.694); Departement Zorg / Vlaamse sociale bescherming",
    "decision_date": "2026-06-02",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0475581694/vlaamse-zorgkas",
    "stated_goal": "Public VL zorgkas / mandatory Vlaamse sociale bescherming alternative",
    "cut_option": "Publish NBB PDF assets/debt + thin equity vs 194m omzet FOI; recon pnl DROP",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>DepartementZorg>VlaamseZorgkas>JR2025_statutory_L5",
    "notes": "tick2010 EVERY-10; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; OLVT already mined; thin equity 0.62m vs omzet 193.92m",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*5.8 + 0.10*4.0 = 3.025 + 2.03 + 0.4 = 5.455 ≈ 5.46
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_vlaamse_zorgkas_omzet_jump_193_92m_pnl_drop_0_15m_jr2025",
    "name": "Vlaamse Zorgkas omzet JUMP 193.92m / pnl DROP 0.15m (YE2025)",
    "level": "L5",
    "type": "flemish_zorgkas_vzw_dual",
    "hierarchy_path": "Vlaanderen>DepartementZorg>VlaamseZorgkas>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; thin equity vs flow; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "VL zorgpremie members / zorgbudget recipients",
    "stated_goal": "Public VL zorgkas / sociale bescherming",
    "measured_outcome": "Medium CW YE2025; 193.92m omzet JUMP +2.05pct with pnl DROP -40.94pct and thin equity JUMP to 0.62m; NBB PDF residual",
    "absurdity_score": "5.8",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.46",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; scrutinise thin equity + 0 FTE vs Departement Zorg staff path",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2010 EVERY-10 leftover dual; Medium CW; TE-adjacent zorgpremie flow not pure-waste top10; next every-10 2020",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Vlaamse Zorgkas",
    "name_fr": "Caisse flamande de soins / Vlaamse Zorgkas",
    "name_en": "Flemish Care Fund (Vlaamse Zorgkas)",
    "level": "asbl",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.vlaanderen.be/vlaamse-zorgkas",
    "foi_email": "vlaamsezorgkas@vlaanderen.be",
    "foi_postal": "Simon Bolivarlaan 17, 1000 Brussel (post: Koning Albert II-laan 15 bus 499, 1210 Brussel)",
    "notes": "tick2010 EVERY-10 YE2025 Medium CW NL+EN+FR + Strong KBO 0475.581.694 Actief VZW; omzet JUMP 193.92m pnl DROP 0.15m equity JUMP 0.62m bruto JUMP 4.62m FTE 0; assets/debt Unknown; neerlegging 02.06.2026; 0 VE; Departement Zorg dual; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo OLVT/AZ Sint-Blasius/AZ Oostende/Glorieux/Alma/Herentals/Vitaz/Emmaüs/AZORG/Z.org/AZ Delta/AZJP/ZAS",
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
    "hierarchy_path": "Vlaanderen>DepartementZorg>VlaamseZorgkas>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); thin equity vs 194m omzet recon; pnl DROP path; Departement Zorg staff dual",
    "why_it_matters": "Medium CW shows 193.92m omzet public VL zorgkas with only 0.62m equity and 0 FTE without balance sheet",
    "priority": "8",
    "recipient_body": "Vlaamse Zorgkas VZW / Departement Zorg",
    "recipient_email": "vlaamsezorgkas@vlaanderen.be",
    "recipient_postal": "Simon Bolivarlaan 17, 1000 Brussel",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_vlaamse_zorgkas_jr2025_statutory_zorgkas",
    "linked_leaderboard_id": "lb_vlaamse_zorgkas_omzet_jump_193_92m_pnl_drop_0_15m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2010 EVERY-10; human-send only; Medium CW; next every-10 2020",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Vlaamse Zorgkas (NBB PDF / assets-debt / pnl DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Vlaamse Zorgkas VZW — KBO **0475.581.694**  
**recipient:** vlaamsezorgkas@vlaanderen.be · Simon Bolivarlaan 17, 1000 Brussel  
**sources:** [CW NL](https://www.companyweb.be/nl/0475581694/vlaamse-zorgkas) · [CW EN](https://www.companyweb.be/en/0475581694/vlaamse-zorgkas) · [CW FR](https://www.companyweb.be/fr/0475581694/vlaamse-zorgkas) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0475581694) · [Vlaanderen.be](https://www.vlaanderen.be/vlaamse-zorgkas)  
**tick:** 2010 EVERY-10  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **02.06.2026**): omzet **EUR193,923,835** JUMP +2.05%; pnl **EUR154,861** DROP −40.94%; equity **EUR619,261** JUMP +33.35%; bruto **EUR4,620,876** JUMP +66.61%; FTE **0**; assets/debt **Unknown**.
- Public VL zorgkas VZW under Departement Zorg (Belpairegebouw). Thin equity vs 194m omzet flow-through. Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. OLVT already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Vlaamse Zorgkas VZW / Departement Zorg — Simon Bolivarlaan 17, 1000 Brussel
vlaamsezorgkas@vlaanderen.be
cc: openbaarheid@vlaanderen.be
Betreft: Openbaarmaking NBB-jaarrekening 2025 Vlaamse Zorgkas + balans (KBO 0475.581.694)
Geachte, op grond van het Bestuursdecreet vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 02.06.2026).
2. Assets / schulden LT-ST / cash.
3. Recon thin equity (EUR619.261) vs omzet (EUR193.923.835) + pnl DROP (−40,94pct).
4. Departement Zorg personeelspad vs FTE 0 in statutory.
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
snapshot = f"""## Snapshot at **tick 2010** (2026-08-24)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2001-2010 hospital/zorgkas continuum after 2000 AZ Delta |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2001-2010 is residual dual L5 (not near-complete of 348bn):** **Z.org KU Leuven** omzet JUMP **111.24m** · **AZORG** omzet **824.93m** / pnl LOSS · **Emmaüs** omzet JUMP **624.17m** · **Vitaz** omzet JUMP **474.71m** · **Herentals** omzet JUMP **171.67m** / pnl DROP · **AZ Alma** omzet JUMP **191.40m** · **Glorieux** omzet JUMP **164.36m** / pnl DROP · **AZ Oostende** omzet JUMP **308.72m** · **OLVT/Blasius** omzet JUMP **235.94m** / pnl DROP · **Vlaamse Zorgkas** omzet JUMP **193.92m** / pnl DROP / thin equity Medium (this tick EVERY-10 dual) |
| **E. FOI-ready gaps** | **~{n_ready}** drafts ready | Human send only; answered **~{n_ans}**; partial **~{n_part}**; total FOI rows **~{n_foi}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/property/renewable/energy/nuclear/water/forest/hospital/zorgkas shells** (**NEW 2001-2010** Z.org · AZORG · Emmaüs · Vitaz · Herentals · Alma · Glorieux · AZ Oostende · OLVT/Blasius · **Vlaamse Zorgkas** · prior ZAS/AZ Delta/AZJP/Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2010)

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
| research_queue open | rq_2011 after progress |

### What improved since tick 2000

- **Residual dual (tick2001-2010):** **Z.org KU Leuven** · **AZORG** · **Emmaüs** · **Vitaz** · **AZ St.-Elisabeth Herentals** · **AZ Alma** · **Werken Glorieux** · **AZ Oostende** · **OLVT/AZ Sint-Blasius** · **Vlaamse Zorgkas** (this tick EVERY-10 dual — public VL zorgkas VZW YE2025 Medium CW).
- **Blocked still:** AGB Bornem JR2024-only · FARO NBB YE2025 unpublished (YE2024 filing) · AIESH/REW YE2024-only · Erasme/UZ Brussel CW opaque · AZ Sint-Lucas / Groeninge / Zottegem / Turnhout / Waregem / Yperman / Maria Middelares / Imelda / Monica CW N/A omzet · Bosgroep IJzer/Houtland/Limburg YE2025 unpublished · prior Eneco deposit FOI stack.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10 (re-verified; corrupt AGB pi>10 / OWV snowball stock / Metro3 stock filtered off pure annual). Not TE-additive of ~348bn. TE denominator still **EUR347.956 bn**. Next every-10 is **2020**.


"""
if "## Snapshot at **tick 2010**" not in prog_text:
    anchor = "## Snapshot at **tick 2000**"
    if anchor in prog_text:
        prog_text = prog_text.replace(anchor, snapshot + anchor, 1)
    else:
        prog_text = prog_text + "\n" + snapshot
    progress.write_text(prog_text, encoding="utf-8")
    print("progress refreshed")
else:
    print("progress already has tick 2010")

top10 = Path("docs/doge/data/doge_waste_top10_current.md")
top10.write_text(
    f"""# DOGE waste ranking — current top 10

**As-of:** tick **2010** (2026-08-24) · **{n_lb}** leaderboard rows  
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
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij shells** · **NEW leftover 2001-2010:** **AZORG omzet 824.93m** · **Emmaüs omzet 624.17m** · **Vitaz omzet 474.71m** · **AZ Oostende omzet 308.72m** · **OLVT/Blasius omzet 235.94m** · **Vlaamse Zorgkas omzet 193.92m** · Alma/Glorieux/Herentals/Z.org · prior **ZAS/AZ Delta/Saint-Luc/Humani/GHdC/Verviers/CHBA/CNDG/Haute Senne/AZJP/CHIREC** stack retained · prior nuclear/Fluxys/Elia/Enodia/RESA · prior Eneco continuum · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2000:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off). **Major NEW residual 2001-2010 (off pure top10 / dual):** Z.org · AZORG · Emmaüs · Vitaz · Herentals · Alma · Glorieux · AZ Oostende · OLVT/Blasius · **Vlaamse Zorgkas** (EVERY-10 dual). Count NEW since 2000: 10 residual dual ticks. **Prior ZAS/AZ Delta stack retained.** Not TE-additive of ~348bn.
""",
    encoding="utf-8",
)
print("top10 refreshed")

for x in qrows:
    if x.get("task_id") == "rq_2010":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "EVERY-10 + leftover dual after OLVT — Vlaamse Zorgkas YE2025 Medium"
        x["notes"] = (
            "tick2010 EVERY-10 + Vlaamse Zorgkas Medium omzet JUMP 193.92m pnl DROP 0.15m equity JUMP 0.62m; FOI ready; "
            "progress+top10 refreshed; next rq_2011; next every-10 2020"
        )
        x["instructions"] = (
            "Completed EVERY-10 progress+top10 + leftover Vlaamse Zorgkas YE2025 Medium CW; KBO 0475.581.694; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2011" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2011",
            "title": "leftover dual hole-fill after Vlaamse Zorgkas EVERY-10",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2010 EVERY-10 after Vlaamse Zorgkas YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Heilig Hart Lier / Sint-Jan Brugge / Vesalius / other unused YE2025 if live). "
                "Do NOT redo Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2010 EVERY-10 Vlaamse Zorgkas; next every-10 2020",
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
        "last_unit_id": "rq_2010",
        "ticks_completed": "2010",
        "paused": "no",
        "notes": (
            "tick2010 EVERY-10 + leftover Vlaamse Zorgkas 0475.581.694 Medium CW (omzet JUMP 193.92m pnl DROP 0.15m equity JUMP 0.62m bruto JUMP 4.62m FTE 0; "
            "assets/debt Unknown); progress+top10 refreshed; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2011; next every-10 2020; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2010 - {UTC} - rq_2010 EVERY-10 + Vlaamse Zorgkas (omzet JUMP 193.92m / pnl DROP 0.15m / Medium)

- Unit: **rq_2010** EVERY-10 mandatory + leftover dual after **rq_2009 OLVT/AZ Sint-Blasius**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Zottegem/Turnhout/Waregem/Yperman CW **N/A omzet**. Took preferred leftover **Vlaamse Zorgkas** YE2025 (KBO **0475.581.694**; Simon Bolivarlaan 17 Brussel; **public VL zorgkas VZW** under Departement Zorg). Do not redo OLVT/AZ Oostende/Glorieux/Alma/Herentals/Vitaz/Emmaüs/AZORG/Z.org/AZ Delta/AZJP/ZAS.
- EVERY-10: refreshed **progress_every_10_ticks.md** (tick 2010 snapshot; residual dual 2001-2010) + **doge_waste_top10_current.md** (pure annual top10 stable GIP/fossil/cars/cheque/reporté; NEW residual dual off-top10).
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR193,923,835** JUMP +2.05%; pnl **EUR154,861** DROP −40.94%; equity **EUR619,261** JUMP +33.35% (thin vs flow); bruto **EUR4,620,876** JUMP +66.61%; FTE **0**; neerlegging **02.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 0 VE; email vlaamsezorgkas@vlaanderen.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_vlaamse_zorgkas); foi + draft {GAP}; progress+top10; rq_2010=done + rq_2011 open; loop_state ticks=2010; raw under docs/doge/data/raw/tick2010/.
- FOI: **ready not sent** (human-gated; vlaamsezorgkas@vlaanderen.be).
- EVERY-10 done. Next every-10 **2020**. Next: rq_2011 (AGB/FARO-if-YE2025 / AIESH-REW / Heilig Hart Lier-Sint-Jan-Vesalius / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
