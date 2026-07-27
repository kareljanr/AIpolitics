# -*- coding: utf-8 -*-
"""Tick 153 — rq_120 Myria federal migration centre funding."""
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
TICK = 153
UNIT = "rq_120"
UTC = "2026-07-28T00:30:00Z"


def read_text(p: Path) -> tuple[str, str]:
    raw = p.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1"), "latin-1"


def write_text(p: Path, text: str, enc: str = "utf-8") -> None:
    # Prefer utf-8 for new content; if file was latin-1/cp1252 mixed, write utf-8
    p.write_bytes(text.encode("utf-8", errors="replace"))


def append_rows(p: Path, rows: list[str]) -> None:
    text, enc = read_text(p)
    if not text.endswith("\n"):
        text += "\n"
    text += "\n".join(rows) + "\n"
    write_text(p, text)


def replace_line_startswith(p: Path, prefix: str, new_line: str) -> bool:
    text, _ = read_text(p)
    lines = text.splitlines()
    found = False
    out = []
    for L in lines:
        if L.startswith(prefix):
            out.append(new_line)
            found = True
        else:
            out.append(L)
    write_text(p, "\n".join(out) + ("\n" if text.endswith("\n") else ""))
    return found


# --- sources ---
src_rows = [
    'src_kamer_56k1281_004_myria,Kamer Doc 56 1281/004 Verantwoording AUB 2026 sectie 07 Onafhankelijke organen BA 41.10.414003 Myria,https://www.lachambre.be/FLWB/pdf/56/1281/56K1281004.pdf,Kamer van volksvertegenwoordigers,2026-07-28,official_budget,"AB 41.10.414003 Myria federal dotation kEUR 1579/1614/1600/1572/1543/1516 for 2024-2029 engagement=liquidation; AR 29 Jun 2014 art.15 1.5m indexed health index from 2014-01-01; tick153"',
    'src_myria_organic_ar,AR 29 June 2014 organic statute Myria financing art.15,https://www.myria.be,Belgian Official Gazette / Myria,2026-07-28,official_legal,"Cited in Kamer justification: annual 1.5m EUR indexed health index ref 2014-01-01; also historic lottery co-financing references in older Myria reports; tick153"',
]
# avoid duplicate source ids
text_s, _ = read_text(DATA / "sources.csv")
for row in src_rows:
    sid = row.split(",", 1)[0]
    if sid not in text_s:
        append_rows(DATA / "sources.csv", [row])

# --- entities ---
text_e, _ = read_text(DATA / "entities.csv")
if "myria," not in text_e and "\nmyria," not in text_e:
    ent = (
        "myria,Myria Federaal Migratiecentrum,Myria Centre federal Migration,"
        "Myria Belgian Federal Migration Centre,agency,sec_federal,bi,"
        "https://www.myria.be,,Brussels,"
        "Independent public body; federal AB 41.10.414003 path 1.579-1.614-1.600m 2024-26; "
        "mandates migration flows fundamental rights trafficking; Paris Principles class; "
        "equality/HR stack with Unia VMRI IEFH FIRM; tick153"
    )
    append_rows(DATA / "entities.csv", [ent])

# --- budgets ---
bud_rows = [
    "bud_myria_dot_2024,myria,2024,1579000,,,budgeted,src_kamer_56k1281_004_myria,strong,AB 41.10.414003 federal dotation engagement=liquidation 1579 kEUR Kamer 56 1281/004",
    "bud_myria_dot_2025,myria,2025,1614000,,,budgeted,src_kamer_56k1281_004_myria,strong,AB 41.10.414003 federal 1614 kEUR",
    "bud_myria_dot_2026,myria,2026,1600000,,,budgeted,src_kamer_56k1281_004_myria,strong,AB 41.10.414003 federal 1600 kEUR mild cut vs 2025",
    "bud_myria_dot_2027,myria,2027,1572000,,,budgeted,src_kamer_56k1281_004_myria,strong,AB path 1572 kEUR multi-year table",
    "bud_myria_dot_2028,myria,2028,1543000,,,budgeted,src_kamer_56k1281_004_myria,strong,AB path 1543 kEUR",
    "bud_myria_dot_2029,myria,2029,1516000,,,budgeted,src_kamer_56k1281_004_myria,strong,AB path 1516 kEUR continuing mild decline",
]
text_b, _ = read_text(DATA / "budgets.csv")
for row in bud_rows:
    bid = row.split(",", 1)[0]
    if bid not in text_b:
        append_rows(DATA / "budgets.csv", [row])

# --- commitments ---
cmt = (
    'cmt_myria_dotation_path,Myria federal AB 41.10.414003 multi-year path 2024-2029,myria,Myria,'
    'Samenwerkingsakkoord 12 jun 2013 + wet 15 feb 1993 / 17 aug 2013 + AR 29 jun 2014 art.15,2014-06-29,2024,2029,9424000,'
    '"{""2024"":1579000,""2025"":1614000,""2026"":1600000,""2027"":1572000,""2028"":1543000,""2029"":1516000,'
    '""note"":""Kamer engagement=liquidation kEUR; organic base 1.5m indexed from 2014; path mild decline after 2025; '
    'institutional total may exceed federal AB if other income (lottery/projects) — residual FOI""}",0,active,'
    'https://www.myria.be,Federal migration centre independence Paris Principles class,'
    'Publish outturn+other income annually; benchmark vs Unia/IEFH/FIRM stack,'
    'src_kamer_56k1281_004_myria,strong,BE>Myria>federal_dotation,'
    'tick153; political claim 2.213m secondary social media not matching AB 1.6m — do not use as official'
)
text_c, _ = read_text(DATA / "commitments.csv")
if "cmt_myria_dotation_path" not in text_c:
    append_rows(DATA / "commitments.csv", [cmt])

# --- leaderboard ---
# priority rough: absurdity 3 (mandate not pure waste), cost_score ~4 (1.6m small), difficulty 3, index ~3.5
lb = (
    "lb_myria_federal_dotation,Myria federal AB dotation ~1.6m 2026,federal,ops,BE>Myria>dotatie,"
    "1600000,9424000,"
    "Kamer 56 1281/004 strong: 1.579/1.614/1.600m 2024-26; path to 1.516m 2029; organic 1.5m indexed 2014; "
    "equality/HR multi-body stack Unia+IEFH+FIRM+Myria+VMRI,"
    "strong,src_kamer_56k1281_004_myria,"
    "Migrants foreign nationals trafficking victims public authorities,"
    "Migration flows fundamental rights trafficking rapporteur,"
    "Core mandate not pure waste; multi-body HR stack raises total,"
    "3,4.0,3,3.5,"
    "Publish cash outturn + other income; outcome KPIs; avoid dual-mandate creep,"
    "seed,,tick153"
)
text_l, _ = read_text(DATA / "leaderboard.csv")
if "lb_myria_federal_dotation" not in text_l:
    append_rows(DATA / "leaderboard.csv", [lb])

# --- overhead node note if file small ---
text_o, _ = read_text(DATA / "overhead_nodes.csv")
if "oh_equality_hr_stack" not in text_o:
    oh = (
        'oh_equality_hr_stack,"Equality/HR multi-body federal+interfederal stack (Unia federal + IEFH + FIRM + Myria; VMRI Flanders separate)",'
        "multi_body,unia_interfederal|iefh|firm_ifdh|myria|vmri_vlaanderen,"
        "40500000,2026,medium,src_kamer_56k1281_004_myria,"
        "\"Illustrative sum class: Unia fed AB ~4.0m + IEFH ~31.1m + Myria 1.6m + FIRM grant ~3.2m = ~40m federal-ish 2026; "
        "IEFH dominates; Unia also has federated; Flanders VMRI extra; not consolidated ESA; tick153\""
    )
    append_rows(DATA / "overhead_nodes.csv", [oh])

# --- FOI queue ---
gap_id = "gap_myria_other_income"
foi_row = (
    f"{gap_id},BE>Myria>other_income_outturn,myria,"
    "Cash outturn vs AB 41.10.414003 2022-2026; other income (Nationale Loterij projects EU own); FTE and exp split personnel/ops; reconcile any secondary 2.213m claim,"
    "Federal AB path strong 1.58-1.61m; institutional total and L5 exp may exceed line,"
    "5,Myria / FOD BOSA / IBZ FOI,myria@myria.be,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{gap_id}.md,ready,2026-07-28,,,,,"
    "cmt_myria_dotation_path,lb_myria_federal_dotation,2026-07-28T00:30:00Z,2026-07-28T00:30:00Z,"
    "tick153 partial AB fill; residual other-income human send"
)
text_f, _ = read_text(DATA / "foi_queue.csv")
if gap_id not in text_f:
    append_rows(DATA / "foi_queue.csv", [foi_row])

# --- FOI draft ---
FOI.mkdir(parents=True, exist_ok=True)
draft = f"""# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `{gap_id}`  
**Status:** ready (human send only)  
**Linked:** {UNIT} · cmt_myria_dotation_path · lb_myria_federal_dotation

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Myria — Centre federal Migration / Federaal Migratiecentrum
     en/of FOD BOSA / IBZ openbaarheid van bestuur
     https://www.ibz.be/nl/openbaarheid-van-bestuur
     Contact class: myria@myria.be (verify)

Betreft: Verzoek om openbaarmaking — Myria begroting, realisaties en andere inkomsten 2022-2026

Geachte,

Op grond van de wet 11 april 1994 inzake openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Cash-realisaties (vereffeningen) versus goedgekeurde kredieten voor
   basisallocatie 41.10.414003 (Dotatie Myria) voor de jaren 2022 tot en
   met 2026, inclusief eventuele aangepaste begrotingen.
2. Overzicht van alle andere inkomsten van Myria 2022-2026, met bron:
   Nationale Loterij / projectsubsidies / EU / eigen inkomsten / overige,
   met bedragen per jaar.
3. Uitgavensplit 2022-2025 (en 2026 indien beschikbaar): personeel;
   werking; publicaties/studies; externe opdrachten; investeringen.
4. FTE / personeelsbestand per 31/12 voor 2022-2025.
5. Indien van toepassing: verklaring van enig secundair genoemd bedrag
   rond EUR 2.213.000 dat niet overeenkomt met de Kamer-tabel
   (~EUR 1,6 miljoen in 2025-2026).

Periode: 2022-01-01 tot meest recente stand.

### 2. Context

Kamer Doc 56 1281/004 publiceert de federale AB-path:
2024 EUR 1.579.000; 2025 EUR 1.614.000; 2026 EUR 1.600.000
(engagement = liquidatie, duizenden euro in de tabel).
Organiek AR 29 juni 2014 art. 15: basis 1,5 miljoen euro geindexeerd
vanaf 1 januari 2014 (gezondheidsindex).
Ontbrekend: institutionele totalen (andere inkomsten) en L5-opsplit
voor vergelijking met Unia / IEFH / FIRM.

Hierarchie intern: BE > Myria > federal_dotation + other_income.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: {gap_id}

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling (Myria + BOSA/IBZ)
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
"""
(FOI / f"{gap_id}.md").write_text(draft, encoding="utf-8")

# --- research_queue update ---
rq_new = (
    f"rq_120,Myria federal migration centre funding,continuous,5,done,L2,myria,"
    f'"Myria budget/dotation 2024-2026 primary annual report or federal budget line.",'
    f"{gap_id},2026-07-27T12:00:00Z,{UTC},"
    "tick153: Kamer 56 1281/004 AB 41.10.414003 1.579/1.614/1.600m 2024-26 strong; path to 1.516m 2029; residual other-income FOI ready"
)
if not replace_line_startswith(DATA / "research_queue.csv", "rq_120,", rq_new):
    raise SystemExit("rq_120 not found")

# --- loop_state ---
state = (
    f"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    f'"Scheduler 60s. Next prio5 housing Brussels communes DGD; FOI ready human send. rq_120 Myria AB 1.6m 2026 done."\n'
)
write_text(DATA / "loop_state.csv", state)

# --- loop_log append ---
log_p = ROOT / "docs" / "doge" / "loop_log.md"
log_text, _ = read_text(log_p)
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Myria federal migration centre funding)
- Found (strong primary Kamer Doc 56 1281/004 sectie 07):
  - **AB 41.10.414003** Myria federal dotation (engagement = liquidation, kEUR):
    | Year | EUR |
    |------|-----|
    | 2024 | **1.579m** |
    | 2025 | **1.614m** |
    | 2026 | **1.600m** |
    | 2027-29 path | 1.572 / 1.543 / **1.516m** |
  - Organic AR 29 Jun 2014 art.15: base **1.5m** indexed health index from 2014-01-01.
  - Same table context: Unia federal AB **4.034m 2026**; IEFH **31.101m 2026** (stack).
  - Secondary social-media claim **EUR 2.213m** does **not** match Kamer AB (~1.6m) — **do not use** as official.
- Wrote: sources 2; entity myria; budgets 6; cmt 1; lb 1; overhead stack note; rq_120=done; FOI residual ready.
- FOI: gap_myria_other_income (outturn + lottery/other + FTE) human send only.
- Next: prio5 **rq_149 housing** / **rq_145 Brussels communes** / **rq_146 DGD** / **rq_121 hole-fill**.
"""
if not log_text.endswith("\n"):
    log_text += "\n"
write_text(log_p, log_text + entry)

print("OK tick", TICK, UNIT)
print("Myria 2024-26:", 1579000, 1614000, 1600000)
print("FOI:", gap_id)
