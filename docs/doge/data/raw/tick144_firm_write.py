# -*- coding: utf-8 -*-
"""Tick 144: rq_119 FIRM-IFDH funding map — append sourced rows."""
from pathlib import Path

ROOT = Path("docs/doge")
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
UTC = "2026-07-27T21:30:00Z"
TICK = 144
UNIT = "rq_119"


def read_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1"), "latin-1"


def write_text(path: Path, text: str, enc: str) -> None:
    # Prefer utf-8 for new clean files; keep existing encoding for mixed legacy CSVs
    path.write_bytes(text.encode(enc, errors="replace"))


def append_lines(path: Path, lines: list[str]) -> None:
    text, enc = read_text(path)
    if not text.endswith("\n"):
        text += "\n"
    # Append as ASCII-safe content; keep file encoding
    write_text(path, text + "\n".join(lines) + "\n", enc)


# --- sources (ASCII-safe notes) ---
append_lines(DATA / "sources.csv", [
    'src_firm_ra_2024,FIRM-IFDH Annual Report 2024 Finances section,https://institutfederaldroitshumains.be/sites/default/files/2025-08/Annual-Report-2024-FIRM-IFDH.pdf,FIRM-IFDH,2026-07-27,annual_report,"Grant 2024 4111000; surplus 237732.78; total budget 4348732.78; 2023 exp 1652638.76 grant 2776000"',
    'src_firm_ra_2025,FIRM Jaarverslag 2025 Financien en budget,https://institutfederaldroitshumains.be/sites/default/files/2026-06/Jaarverslag-2025-FIRM.pdf,FIRM-IFDH,2026-07-27,annual_report,"Dotatie 2025 3769000; total budget 4984094.75; exp 2025 3516071.02; 2024 exp 2488783.46; 2026 budget dotatie 3223000 total finance 5082949.32; staff 26 end-2025"',
])

append_lines(DATA / "budgets.csv", [
    "bud_firm_dotation_2023,firm_ifdh,2023,2776000,,,budgeted,src_firm_ra_2024,strong,Kamer grant / dotatie 2023",
    "bud_firm_funding_2023,firm_ifdh,2023,2867733.51,,,budgeted,src_firm_ra_2024,strong,Grant + surplus carried; other 0",
    "bud_firm_exp_2023,firm_ifdh,2023,1652638.76,,,outturn,src_firm_ra_2024,strong,Actual expenditure accounts 2023",
    "bud_firm_balance_2023,firm_ifdh,2023,1215094.75,,,outturn,src_firm_ra_2024,strong,Year-end surplus balance 2023",
    "bud_firm_dotation_2024,firm_ifdh,2024,4111000,,,budgeted,src_firm_ra_2025,strong,Kamer grant / dotatie 2024",
    "bud_firm_funding_2024,firm_ifdh,2024,4348732.78,,,budgeted,src_firm_ra_2025,strong,Grant 4.111m + surplus 0.238m",
    "bud_firm_exp_2024,firm_ifdh,2024,2488783.46,,,outturn,src_firm_ra_2025,strong,Actual expenditure rekeningen 2024",
    "bud_firm_balance_2024,firm_ifdh,2024,1859949.32,,,outturn,src_firm_ra_2025,strong,Year-end surplus balance 2024",
    "bud_firm_dotation_2025,firm_ifdh,2025,3769000,,,budgeted,src_firm_ra_2025,strong,Kamer grant / dotatie 2025 (RA2025)",
    "bud_firm_funding_2025,firm_ifdh,2025,4984094.75,,,budgeted,src_firm_ra_2025,strong,Grant 3.769m + surplus 1.215m",
    "bud_firm_exp_2025,firm_ifdh,2025,3516071.02,,,outturn,src_firm_ra_2025,strong,Actual expenditure 2025",
    "bud_firm_balance_2025,firm_ifdh,2025,1468023.73,,,outturn,src_firm_ra_2025,strong,Year-end surplus balance 2025",
    "bud_firm_dotation_2026,firm_ifdh,2026,3223000,,,budgeted,src_firm_ra_2025,strong,Kamer approved budget 2026 grant",
    "bud_firm_funding_2026,firm_ifdh,2026,5082949.32,,,budgeted,src_firm_ra_2025,strong,Grant 3.223m + surplus 1.860m; exp not yet",
])

append_lines(DATA / "commitments.csv", [
    'cmt_firm_dotation_path,FIRM-IFDH federal Kamer grant multi-year,firm_ifdh,FIRM-IFDH,Wet 12 mei 2019 oprichting FIRM + Kamer dotatie,2019-05-12,2023,2026,3223000,"{""2023_grant"":2776000,""2023_exp"":1652638.76,""2023_balance"":1215094.75,""2024_grant"":4111000,""2024_funding"":4348732.78,""2024_exp"":2488783.46,""2024_balance"":1859949.32,""2025_grant"":3769000,""2025_funding"":4984094.75,""2025_exp"":3516071.02,""2025_balance"":1468023.73,""2026_grant"":3223000,""2026_funding"":5082949.32,""2025_staff"":26,""note"":""grant falling 2025-26 while surplus buffer funds total budget; dual Unia VMRI IEFH architecture""}",0,active,https://institutfederaldroitshumains.be,Federal NHRI residual mandate Paris Principles,Publish annual accounts promptly; track surplus burn and interfederalisation cost,src_firm_ra_2025,strong,BE>FIRM_IFDH>dotatie,tick144; dual human-rights bodies with Unia/VMRI/IEFH',
])

append_lines(DATA / "leaderboard.csv", [
    "lb_firm_public_dotation,FIRM-IFDH public package exp ~3.5m 2025 (grant 3.8m),federal,ops,BE>FIRM_IFDH>dotatie,3516071,4984094,RA2025 strong: exp 3.516m 2025 grant 3.769m total budget 4.984m; path grant 2.78-4.11-3.77-3.22m 2023-26; surplus buffer large,strong,src_firm_ra_2025,General public rule-of-law stakeholders,Federal NHRI residual human rights,Core mandate not pure waste; multi-body equality/HR stack (Unia VMRI IEFH FIRM Myria),4,5.5,4,4.7,Benchmark outcomes vs Unia; track surplus burn; interfederal A-status path cost-neutral,seed,,tick144",
])

ent_text, ent_enc = read_text(DATA / "entities.csv")
if "firm_ifdh," not in ent_text:
    append_lines(DATA / "entities.csv", [
        "firm_ifdh,Federaal Instituut voor de rechten van de mens (FIRM),Institut federal des droits humains (IFDH),Federal Institute for Human Rights,agency,sec_federal,bi,https://institutfederaldroitshumains.be,,Brussels,Kamer-dotated NHRI residual federal mandate; exp 2025 3.52m grant 3.77m; staff 26; dual Unia/VMRI/IEFH",
    ])

# research_queue
rtext, renc = read_text(DATA / "research_queue.csv")
old = (
    'rq_119,FIRM-IFDH federal human rights institute funding,continuous,6,open,L2,firm_ifdh,'
    '"Map FIRM/IFDH federal dotation 2024-2026 from annual report or BGD; dual with Unia/VMRI.",'
    ",2026-07-27T12:00:00Z,2026-07-27T12:00:00Z,Human rights institutional map"
)
new = (
    'rq_119,FIRM-IFDH federal human rights institute funding,continuous,6,done,L2,firm_ifdh,'
    '"Map FIRM/IFDH federal dotation 2024-2026 from annual report or BGD; dual with Unia/VMRI.",'
    "gap_firm_funding_detail,2026-07-27T12:00:00Z,2026-07-27T21:30:00Z,"
    '"tick144: RA exp 2024 2.49m 2025 3.52m; grants 4.11/3.77/3.22m 2024-26; FOI residual L5 optional"'
)
if old not in rtext:
    raise SystemExit("rq_119 OLD NOT FOUND")
write_text(DATA / "research_queue.csv", rtext.replace(old, new, 1), renc)

# FOI draft
FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_firm_funding_detail.md").write_text(
    """# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `gap_firm_funding_detail`  
**Status:** ready (human send only)  
**Linked:** rq_119 · cmt_firm_dotation_path · lb_firm_public_dotation

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Federaal Instituut voor de rechten van de mens (FIRM/IFDH)
     en/of Kamer van volksvertegenwoordigers — dienst openbaarheid
     (federaal ook: https://www.ibz.be/nl/openbaarheid-van-bestuur)

Betreft: Verzoek om openbaarmaking — FIRM/IFDH begrotingscodes en uitgavensplit 2023-2026

Geachte,

Op grond van de wet 11 april 1994 inzake openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Basisallocatie-/begrotingscodes (Rijksmiddelenbegroting / Kamer) voor de
   FIRM-dotatie cash-by-year 2023-2026, met goedgekeurde en eventueel
   aangepaste kredieten.
2. Uitgavensplit 2023-2025 (en 2026 indien beschikbaar) in minstens:
   personeel; werking; projecten (NPM, klokkenluiders, anti-SLAPP, research);
   externe studies/consultants; investeringen.
3. Bevestiging van de overgedragen boni-path en regeling voor teruggave of
   heraanwending van ongebruikte saldi aan de Staat.
4. Eventuele bijkomende federale of EU-middelen buiten de Kamer-dotatie
   (indien >0 na 2025).

Periode: 2023-01-01 tot meest recente stand.

### 2. Context

Jaarverslagen 2024-2025 publiceren sterke totalen (dotatie/uitgaven/saldo).
Ontbrekend: begrotingscodes en L5 ops-split voor overhead-vergelijking
met Unia/IEFH/VMRI.

Hierarchie intern: BE > FIRM_IFDH > dotatie.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: gap_firm_funding_detail

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling (FIRM + Kamer)
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
""",
    encoding="utf-8",
    newline="\n",
)

append_lines(DATA / "foi_queue.csv", [
    "gap_firm_funding_detail,BE>FIRM_IFDH>dotatie_codes_L5,firm_ifdh,Kamer BGD/allocation codes cash-by-year 2023-2026 and L5 exp split personnel/ops/NPM/whistleblower/SLAPP; surplus return rules,Totals 2023-26 public in RA; codes and L5 ops split thin,5,FIRM-IFDH / Kamer openbaarheid,,https://www.ibz.be/nl/openbaarheid-van-bestuur,docs/doge/foi/drafts/gap_firm_funding_detail.md,ready,2026-07-27,,,,,cmt_firm_dotation_path,lb_firm_public_dotation,2026-07-27T21:30:00Z,2026-07-27T21:30:00Z,tick144 partial totals filled; residual L5 human send",
])

# loop_state
write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    '"Scheduler 60s. Next prio6 Myria RTBF/VRT Actiris; FOI ready human send. rq_119 FIRM done."\n',
    "utf-8",
)

# loop_log
log_text, log_enc = read_text(ROOT / "loop_log.md")
if not log_text.endswith("\n"):
    log_text += "\n"
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (FIRM-IFDH federal human rights institute funding)
- Found (strong FIRM annual reports 2024 EN + 2025 NL primary):
  - **Grant path:** 2023 **EUR 2.776m** -> 2024 **EUR 4.111m** -> 2025 **EUR 3.769m** -> 2026 **EUR 3.223m** (Kamer dotatie).
  - **Expenditure:** 2023 **EUR 1.653m** · 2024 **EUR 2.489m** · 2025 **EUR 3.516m**.
  - **Total budget 2025: EUR 4.984m** (grant + surplus **EUR 1.215m**); 2026 finance **EUR 5.083m** (grant 3.223 + surplus 1.860).
  - Large **surplus buffer** (balance end-2024 **EUR 1.860m** · end-2025 **EUR 1.468m**).
  - Staff end-2025: **26** (24 statutory + 2 temp); growth path 7->27 class.
  - Dual architecture note: residual federal NHRI alongside Unia / VMRI / IEFH.
- Wrote: sources 2; budgets 14; cmt_firm_dotation_path; lb_firm; entity firm_ifdh; rq_119=done; FOI residual ready.
- FOI: gap_firm_funding_detail (codes + L5 ops) human send only.
- Next: prio6 **rq_120 Myria** / **rq_135 RTBF** / **rq_136 VRT** / Actiris L5.
"""
write_text(ROOT / "loop_log.md", log_text + entry, log_enc)
print("tick144 write OK")
