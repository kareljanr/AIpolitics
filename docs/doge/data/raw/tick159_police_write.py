# -*- coding: utf-8 -*-
"""Tick 159 — rq_151 Local police zones financing consolidate Gent Brugge + multi-city."""
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
TICK = 159
UNIT = "rq_151"
UTC = "2026-07-28T02:55:00Z"
GAP = "gap_police_zones_fed_top50"


def read_text(p: Path) -> str:
    raw = p.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1")


def write_text(p: Path, text: str) -> None:
    p.write_bytes(text.encode("utf-8", errors="replace"))


def append_if_missing(p: Path, rows: list[str]) -> None:
    text = read_text(p)
    if not text.endswith("\n"):
        text += "\n"
    for row in rows:
        if row.split(",", 1)[0] not in text:
            text += row + "\n"
    write_text(p, text)


def replace_line_startswith(p: Path, prefix: str, new_line: str) -> bool:
    text = read_text(p)
    lines = text.splitlines()
    out, found = [], False
    for L in lines:
        if L.startswith(prefix):
            out.append(new_line)
            found = True
        else:
            out.append(L)
    write_text(p, "\n".join(out) + "\n")
    return found


# Snapshot synthesis (primary unit output)
snap = f"""# Local police zones — city financing L5 consolidate (tick {TICK})

**Unit:** {UNIT} · **No invented euros.** Consolidate public city-side transfers already in DOGE + mechanism notes.  
**Not** a full Belgium zone ranking (183 zones) — only cities with public EUR.

## Financing mechanism (strong)

| Layer | Share (class) | Source |
|-------|---------------|--------|
| **Municipal/city dotations** | **~64%** of local police financing | BeSafe (FPS Interior / local police financing portal) |
| **Federal grants** to zones/municipalities | **~36%** | Same BeSafe overview |
| Zone budgets | Voted by police council; city transfer is largest single line in large cities | PLP budget circulars |

Core public safety — **not** discretionary culture L5. Flag as **ops / mandated multi-level**.

## Ranked city-side police zone transfers (public sample)

| Rank | Zone / city line | Year | City transfer EUR | Confidence | Source class |
|-----:|------------------|------|------------------:|------------|--------------|
| 1 | **Politiezone Gent** (city register charge) | 2024 | **110,603,827** | strong | Gent open subsidieregister |
| 2 | **Zone de police Charleroi (ZPL)** city intervention | 2026 | **82,893,812** | strong | Charleroi BI2026 cahier |
| 3 | **Politiezone Brugge** (register) | 2024 | **32,933,882** | strong | Brugge open register |
| 3b | Politiezone Brugge (MJP nominative) | 2026 | **33,750,000** | strong | Brugge MJP |
| 4 | **Zone de police Namur** (city hors Namur Capitale) | 2026 | **27,587,286** | strong | Namur DGF BI2026 |
| 5 | Ixelles police zone (delta only published) | 2026 | **+300,000** | medium | DH quote echevine — **not** full zone total |

### Related safety zones (fire/rescue — not police; do not mix ranks)

| Entity | Year | EUR | Notes |
|--------|------|----:|-------|
| HVZ Centrum (Gent) | 2024 | **42,254,533** | Fire/rescue zone intern register |
| HVZ Zone 1 West-Vlaanderen (Brugge) | 2024 | **10,077,985** | Fire; MJP 2026 ~10.03m |

## Multi-year path (medium — press quoting MJP)

| Zone | Path | EUR | Confidence |
|------|------|----:|------------|
| Politiezone Gent | 6-year city MJP path class | **~746m** total (~**120–130m**/yr class) | medium (HLN/BusinessAM citing MJP; not open PDF extract this tick) |

## Flemish municipalities aggregate (medium secondary)

HLN (Jan 2026) reporting on MJP data: municipal police spending path **~1.5bn (2026)** rising toward **~1.7bn** later in plan horizon — **secondary**; not used as audited total.

## Federal layer (partial)

- Structure: municipal majority + federal base/extra dotations (KUL-norm capacity formula historically).
- Kamer commission 56K1280/020 discusses sectie 17 Federale Politie + local financing (PDF blocked this tick).
- Press class: federal police budget envelope order **1.5–1.6bn** in 2026 debate — **weak/medium**, FOI residual for official sectie 17.

## Sum of strong single-year city police sample (not national)

Gent 110.6m (2024) + Charleroi 82.9m (2026) + Brugge 33.75m (2026) + Namur 27.6m (2026)  
**= EUR 254.85m** across 4 cities — **illustrative sample only**, mixed years, city-side only (excludes federal share to those zones).

## Mechanism takeaways

1. **Largest “subsidy” lines in open city registers are police zones** — must separate from discretionary ASBL L5 (see `cities_l5_transparency_compare_2026.md`).
2. **Dual financing** (city + federal) creates opacity: city register shows municipal charge; federal per-zone table not machine-public.
3. **Walloon large cities** (Charleroi) publish zone intervention in budget cahier; **Flemish** cities often via register/MJP.
4. Missing for top-10 national map: **Antwerp, Brussels City, Liège, Schaerbeek, Anderlecht, Leuven, Mechelen, Kortrijk** full zone budgets.

## FOI residual (human send)

`{GAP}` — federal export top 50 zones by federal + municipal financing 2024-2026; fill Antwerp/Brussels/Liège.
"""
write_text(DATA / "police_zones_financing_2026_snapshot.md", snap)

srcs = [
    'src_besafe_police_financing,BeSafe politiefinanciering municipal 64pct federal 36pct,https://www.besafe.be/nl/politiefinanciering,FPS Interior / BeSafe,2026-07-28,official_web,"Local police dual financing share class 64 municipal / 36 federal; PLP circulars; tick159"',
    'src_hln_vl_police_mjp_2026,HLN Vlaamse gemeenten politie MJP path Gent 746m class,https://www.hln.be/gent/zo-evolueren-de-uitgaven-aan-politie-volgens-de-meerjarenplanning-van-gent~aaa636f8/,HLN citing MJP data,2026-07-28,press_secondary,"VL municipal police ~1.5bn 2026 path; Gent zone ~746m over 6y; medium; tick159"',
]
append_if_missing(DATA / "sources.csv", srcs)

bud = [
    "bud_police_financing_share_municipal,gg_belgium,2025,64,,,ratio_pct,src_besafe_police_financing,strong,Municipal share ~64pct of local police financing BeSafe official portal",
    "bud_police_financing_share_federal,gg_belgium,2025,36,,,ratio_pct,src_besafe_police_financing,strong,Federal share ~36pct of local police financing BeSafe",
    "bud_gent_politiezone_mjp6y_class,city_gent,2026,746000000,,,budgeted,src_hln_vl_police_mjp_2026,medium,Press: Gent police zone city path ~746m over 6y MJP (~120-130m/yr class)",
    "bud_police_city_sample_sum_tick159,gg_belgium,2026,254838925,,,mixed,src_doge_police_zones_snap_2026,strong,Sum sample city transfers: Gent110.6m2024+Charleroi82.9m2026+Brugge33.75m2026+Namur27.59m2026=254.84m mixed years",
    "bud_brugge_politiezone_2026,city_brugge,2026,33750000,,,budgeted,src_brugge_mjp_2026,strong,Brugge MJP nominative police zone 33.75m 2026 (already cmt; ensure budget row)",
]
append_if_missing(DATA / "budgets.csv", bud)

# source id for snap
srcs2 = [
    'src_doge_police_zones_snap_2026,DOGE police zones financing snapshot tick159,docs/doge/data/police_zones_financing_2026_snapshot.md,AIpolitics DOGE loop,2026-07-28,internal_synthesis,"Consolidates Gent Brugge Charleroi Namur public lines; no invent; tick159"',
]
append_if_missing(DATA / "sources.csv", srcs2)

cmts = [
    (
        'cmt_police_zones_city_sample,Local police zone city transfers multi-city sample,gg_belgium,Local police zones Gent Charleroi Brugge Namur,'
        'Open city registers + BI2026 + MJP + BeSafe financing rules,2024-01-01,2024,2026,254838925,'
        '"{""gent_2024"":110603827,""charleroi_2026"":82893812,""brugge_2026"":33750000,""namur_2026"":27587286,'
        '""sample_sum"":254838925,""municipal_share_class_pct"":64,""federal_share_class_pct"":36,'
        '""gent_mjp6y_class"":746000000,""note"":""city-side only; mixed years; not national total""}",0,active,'
        'docs/doge/data/police_zones_financing_2026_snapshot.md,Local public safety dual municipal-federal finance,'
        'Publish federal per-zone table; open Antwerp Brussels Liege zone budgets,'
        'src_doge_police_zones_snap_2026,strong,BE>Local_police>city_transfers,'
        'tick159; core ops not waste L5; dual financing opacity'
    ),
]
append_if_missing(DATA / "commitments.csv", cmts)

lbs = [
    "lb_police_zones_city_sample,City police zone transfers sample ~255m (4 cities),Belgium,ops,BE>Local_police>city_sample,254838925,254838925,Strong multi-city: Gent 110.6m 2024 Charleroi 82.9m Brugge 33.75m Namur 27.6m; municipal ~64pct federal ~36pct,strong,src_doge_police_zones_snap_2026,City residents,Local integrated police,Core safety; dual finance opacity; not ASBL waste,2,7.5,4,5.2,Federal top50 zone export FOI; keep city open registers,seed,,tick159",
    "lb_gent_politiezone,Gent police zone city charge ~110.6m 2024,local,ops,Gent>Politiezone,110603827,746000000,Register 110.6m 2024; MJP path class 746m/6y medium; dominates Gent register,strong,src_gent_subsidieregister_od,Gent residents,Local police,Core; largest Gent register line,2,7.0,3,4.7,Publish full zone budget PDF + federal share,seed,,tick159",
    "lb_charleroi_zpl_xref,Charleroi ZPL city transfer 82.9m (xref tick152),local,ops,Charleroi>ZPL,82893812,82893812,BI2026 cahier strong; cross-listed police consolidate tick159,strong,src_charleroi_cahier_ord_bi2026,Charleroi residents,Local police zone,Core multi-level,3,7.0,5,5.0,Federal/zone financing reform transparency,seed,,tick159",
]
append_if_missing(DATA / "leaderboard.csv", lbs)

foi_row = (
    f"{GAP},BE>Local_police>federal_and_municipal_by_zone,gg_belgium,"
    "Machine-readable table all police zones 2024-2026: federal base+extra dotation EUR; municipal contribution EUR; zone total budget; FTE; for top 50 by total and missing large cities Antwerp Brussels Liege Leuven,"
    "City sample strong for 4 cities; national zone matrix and federal per-zone still opaque,"
    "6,FOD Binnenlandse Zaken / BeSafe / Federale Politie openbaarheid,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-07-28,,,,,"
    "cmt_police_zones_city_sample,lb_police_zones_city_sample,"
    f"{UTC},{UTC},tick159 partial city consolidate; residual federal matrix human send"
)
text_f = read_text(DATA / "foi_queue.csv")
if GAP not in text_f:
    if not text_f.endswith("\n"):
        text_f += "\n"
    write_text(DATA / "foi_queue.csv", text_f + foi_row + "\n")

FOI.mkdir(parents=True, exist_ok=True)
(FOI / f"{GAP}.md").write_text(f"""# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `{GAP}`  
**Status:** ready (human send only)  
**Linked:** {UNIT}

---

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: FOD Binnenlandse Zaken / BeSafe — openbaarheid van bestuur
     en/of Federale Politie (geintegreerde werking)
     https://www.ibz.be/nl/openbaarheid-van-bestuur

Betreft: Verzoek om openbaarmaking — financiering politiezones 2024-2026 (federaal + gemeentelijk)

Geachte,

Op grond van de wet 11 april 1994 inzake openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Machine-readable export (CSV) van alle politiezones voor 2024, 2025 en 2026 met:
   - federale basisdotatie en eventuele bijkomende federale toelagen (EUR);
   - som van gemeentelijke dotaties aan de zone (EUR);
   - totale zonebegroting indien bij de FOD gekend;
   - eventueel FTE of KUL-norm referentie.
2. Top 50 zones gerangschikt op totale publieke financiering (federaal + gemeentelijk).
3. Specifiek de rijen voor zones Antwerpen, Brussel-Hoofdstad / Brusselse zones,
   Luik, Leuven, Mechelen, Kortrijk (indien nog niet in open stadregisters).
4. Verwijzing naar de begrotingsartikelen (sectie 17 / FOD BIZA) waarop de federale
   toelagen 2024-2026 worden aangerekend.

Periode: 2024-01-01 tot 2026-12-31.

### 2. Context

Open stedelijke registers tonen al sterke gemeentelijke transfers (o.a. Gent EUR 110,6 m
2024; Charleroi EUR 82,9 m 2026; Brugge EUR 33,8 m 2026; Namur EUR 27,6 m 2026).
BeSafe vermeldt de verdeling ca. 64% gemeentelijk / 36% federaal. Ontbrekend: complete
federale matrix per zone.

Hierarchie intern: BE > Local_police > financing_by_zone.

### 3. Vorm

Digitale kopie (CSV/PDF) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: {GAP}

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling (BIZA / BeSafe)
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
""", encoding="utf-8")

rq_new = (
    f"rq_151,Local police zones top 10 provincial financing already cross-check,continuous,4,done,L5,gg_belgium,"
    f'"Consolidate zone financing L5 from city registers Gent Brugge.",{GAP},2026-07-27T14:00:00Z,{UTC},'
    "tick159: snapshot Gent 110.6m Charleroi 82.9m Brugge 33.8m Namur 27.6m; 64/36 municipal/federal; residual FOI"
)
if not replace_line_startswith(DATA / "research_queue.csv", "rq_151,", rq_new):
    raise SystemExit("rq_151 not found")

# After this, only rq_121 prio5 and rq_116 prio1 deferred remain open
write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    f'"Scheduler 60s. Next prio5 rq_121 FOI-adjacent hole-fill; rq_116 SWA deferred to Oct-Dec. FOI ready human send. rq_151 police zones done."\n',
)

log_p = ROOT / "docs" / "doge" / "loop_log.md"
log_text = read_text(log_p)
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Local police zones financing consolidate Gent/Brugge + multi-city)
- Found (strong city sources + BeSafe mechanism):
  - **Mechanism:** municipal **~64%** / federal **~36%** of local police financing (BeSafe).
  - **City-side sample (ranked):** Gent **EUR 110.6m** (2024 register) · Charleroi ZPL **82.9m** (BI2026) · Brugge **33.75m** (MJP 2026; 32.9m register 2024) · Namur **27.6m** (2026).
  - **Sample sum (mixed years):** **EUR 254.8m** (4 cities, city-side only).
  - **Gent MJP path (medium press):** **~746m / 6y** (~120–130m/yr class).
  - Fire HVZ not mixed into police ranks (Gent HVZ 42.3m; Brugge HVZ 10.1m).
- Wrote: snapshot md; sources 3; budgets 5; cmt 1; lb 3; rq_151=done; FOI residual ready.
- FOI: {GAP} (federal+municipal matrix all zones) human send only.
- Next: prio5 **rq_121** FOI-adjacent public hole-fill; **rq_116** SWA deferred (Oct–Dec).
"""
if not log_text.endswith("\n"):
    log_text += "\n"
write_text(log_p, log_text + entry)
print("OK tick", TICK, UNIT)
