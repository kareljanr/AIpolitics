# -*- coding: utf-8 -*-
"""Tick 145: rq_135 RTBF multi-year full financing primary."""
from pathlib import Path

ROOT = Path("docs/doge")
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
UTC = "2026-07-27T21:50:00Z"
TICK = 145
UNIT = "rq_135"


def read_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return raw.decode("latin-1"), "latin-1"


def write_text(path: Path, text: str, enc: str) -> None:
    path.write_bytes(text.encode(enc, errors="replace"))


def append_lines(path: Path, lines: list[str]) -> None:
    text, enc = read_text(path)
    if not text.endswith("\n"):
        text += "\n"
    write_text(path, text + "\n".join(lines) + "\n", enc)


# Sources
append_lines(DATA / "sources.csv", [
    'src_rtbf_ra_2025_finances,RTBF Rapport annuel 2025 finances page primary,https://www.rapportannuelrtbf.be/finances/,RTBF,2026-07-27,annual_report,"2025: recettes 479.7m; ordinary dot 350.8m; pension 13.7m; TV5 9.5m; access 4.1m; ads 61.4m; other 29.3m cable 12.6m; foregone index 15.9m; cash 92.8m LT debt 46.7m; op result 39.1m adj 10.6m"',
    'src_csa_rtbf_controle_2023,CSA Avis 109/2024 controle RTBF exercice 2023,https://www.csa.be/wp-content/uploads/2024/12/20241219-UE-Avis-109-2024-CONTROLE-2023-RTBF.pdf,CSA FWB,2026-07-27,regulator,"2023 ordinary 332793782; total dots 366.9m (TV5 9.4 pension 14.5 SEC 10.2); ads 66.0m; dots series 2017-23; expenses 464.4m; net cost mission 370.1m"',
    'src_rtbf_savings_132m,RTBF CA savings plan 132m 2025-2028,https://www.rtbf.be/article/la-rtbf-adopte-un-plan-d-economies-de-132-millions-sans-licenciements-secs-11535417,RTBF,2026-07-27,agency,"CA Apr 2025: effort >132m 2025-2028; 55.2m in 2028 alone; -12pct vs initial trajectory"',
])

# Budgets — 2023 CSA strong
append_lines(DATA / "budgets.csv", [
    "bud_rtbf_ordinary_2023,rtbf,2023,332793782,,,outturn,src_csa_rtbf_controle_2023,strong,Dotation ordinaire FWB 2023 CSA",
    "bud_rtbf_total_dots_2023,rtbf,2023,366900000,,,outturn,src_csa_rtbf_controle_2023,strong,All public dots 2023: ordinary+TV5 9.4+pension 14.5+SEC 10.2",
    "bud_rtbf_tv5_2023,rtbf,2023,9400000,,,outturn,src_csa_rtbf_controle_2023,strong,TV5 Monde participation cover 2023",
    "bud_rtbf_pension_2023,rtbf,2023,14500000,,,outturn,src_csa_rtbf_controle_2023,strong,Pension pool complementary 2023",
    "bud_rtbf_sec_2023,rtbf,2023,10200000,,,outturn,src_csa_rtbf_controle_2023,strong,Subvention responsabilisation SEC 2010 2023",
    "bud_rtbf_ads_2023,rtbf,2023,66000000,,,outturn,src_csa_rtbf_controle_2023,strong,Net advertising revenue 2023",
    "bud_rtbf_exp_2023,rtbf,2023,464400000,,,outturn,src_csa_rtbf_controle_2023,strong,Total expenses 2023 CSA",
    "bud_rtbf_net_cost_pso_2023,rtbf,2023,370100000,,,outturn,src_csa_rtbf_controle_2023,strong,Net cost of public service mission 2023",
    # 2025 RA strong
    "bud_rtbf_ordinary_2025,rtbf,2025,350800000,,,outturn,src_rtbf_ra_2025_finances,strong,Dotation ordinaire avenant contrat 2023-2027",
    "bud_rtbf_pension_2025,rtbf,2025,13700000,,,outturn,src_rtbf_ra_2025_finances,strong,Complementary pension subsidy 2025 (-1.5m vs 2024)",
    "bud_rtbf_pension_2024,rtbf,2024,15200000,,,outturn,src_rtbf_ra_2025_finances,strong,Implied 2024 pension = 13.7+1.5 from RA2025 delta",
    "bud_rtbf_tv5_2025,rtbf,2025,9500000,,,outturn,src_rtbf_ra_2025_finances,strong,TV5 dotation 2025",
    "bud_rtbf_access_2025,rtbf,2025,4100000,,,outturn,src_rtbf_ra_2025_finances,strong,Accessibilite dotation 2025",
    "bud_rtbf_public_package_2025,rtbf,2025,378100000,,,outturn,src_rtbf_ra_2025_finances,strong,Sum ordinary+pension+TV5+access 350.8+13.7+9.5+4.1",
    "bud_rtbf_recettes_2025,rtbf,2025,479700000,,,outturn,src_rtbf_ra_2025_finances,strong,Total operating receipts 2025 (-0.8pct vs 2024)",
    "bud_rtbf_ads_2025,rtbf,2025,61400000,,,outturn,src_rtbf_ra_2025_finances,strong,Advertising 2025 (-9pct)",
    "bud_rtbf_other_2025,rtbf,2025,29300000,,,outturn,src_rtbf_ra_2025_finances,strong,Other receipts 2025 incl cable 12.6m",
    "bud_rtbf_cable_2025,rtbf,2025,12600000,,,outturn,src_rtbf_ra_2025_finances,strong,Cable operator receipts subset of other",
    "bud_rtbf_foregone_index_2025,rtbf,2025,15900000,,,budgeted,src_rtbf_ra_2025_finances,strong,Foregone vs initial contrat (no index + no +2pct maj)",
    "bud_rtbf_cash_2025,rtbf,2025,92800000,,,outturn,src_rtbf_ra_2025_finances,strong,Net cash position end-2025",
    "bud_rtbf_ltdebt_2025,rtbf,2025,46700000,,,outturn,src_rtbf_ra_2025_finances,strong,Long-term bank debt end-2025",
    # multi-year dots series CSA
    "bud_rtbf_total_dots_2017,rtbf,2017,260500000,,,outturn,src_csa_rtbf_controle_2023,strong,Total public dots series CSA table",
    "bud_rtbf_total_dots_2018,rtbf,2018,270500000,,,outturn,src_csa_rtbf_controle_2023,strong,Total public dots series CSA table",
    "bud_rtbf_total_dots_2019,rtbf,2019,284600000,,,outturn,src_csa_rtbf_controle_2023,strong,Total public dots series CSA table",
    "bud_rtbf_total_dots_2020,rtbf,2020,297700000,,,outturn,src_csa_rtbf_controle_2023,strong,Total public dots series CSA table",
    "bud_rtbf_total_dots_2021,rtbf,2021,305600000,,,outturn,src_csa_rtbf_controle_2023,strong,Total public dots series CSA table",
    "bud_rtbf_total_dots_2022,rtbf,2022,334800000,,,outturn,src_csa_rtbf_controle_2023,strong,Total public dots series CSA table",
])

# Commitments — update path: append new fuller cmt
append_lines(DATA / "commitments.csv", [
    'cmt_rtbf_public_package_2023_28,RTBF multi-source public financing package + savings path,rtbf,RTBF,Contrat de gestion RTBF 2023-2027 + avenants FWB,2023-01-01,2023,2028,378100000,"{""2023_ordinary"":332793782,""2023_total_dots"":366900000,""2023_tv5"":9400000,""2023_pension"":14500000,""2023_sec"":10200000,""2023_ads"":66000000,""2023_exp"":464400000,""2023_net_pso"":370100000,""2024_pension"":15200000,""2025_ordinary"":350800000,""2025_pension"":13700000,""2025_tv5"":9500000,""2025_access"":4100000,""2025_public_package"":378100000,""2025_recettes"":479700000,""2025_ads"":61400000,""2025_other"":29300000,""2025_cable"":12600000,""2025_foregone_index"":15900000,""2025_cash"":92800000,""2025_ltdebt"":46700000,""savings_2025_28"":132000000,""savings_2028_alone"":55200000,""dots_series_2017_23"":[260500000,270500000,284600000,297700000,305600000,334800000,366900000]}",0,active,https://www.rapportannuelrtbf.be/finances/,Public media FR community dual with VRT,Track savings delivery; publish annual complementary-dot split 2024-26; dual VRT efficiency bench,src_rtbf_ra_2025_finances,strong,FWB>Media>RTBF,tick145 supersedes flat 350.8 illustrative; dual PSB VRT 296.4 + RTBF package ~378',
])

# Leaderboard
append_lines(DATA / "leaderboard.csv", [
    "lb_rtbf_public_package,RTBF public package ~378m 2025 (ordinary 350.8 + complements),multi,ops,FWB>Media>RTBF,378100000,378100000,RA2025 strong: ordinary 350.8 pension 13.7 TV5 9.5 access 4.1; total recettes 479.7; ads 61.4; dual VRT 296.4 ordinary; savings path 132m 2025-28,strong,src_rtbf_ra_2025_finances,Francophone households media consumers,Public service broadcasting FWB,Core remit not pure waste; dual NL/FR PSB structural cost; cash 92.8m buffer,5,8.0,7,6.3,Deliver 132m savings; open annual full package vs VRT; no automatic merge politics,seed,,tick145",
])

# Entity if missing
etext, eenc = read_text(DATA / "entities.csv")
if "rtbf," not in etext and not any(line.startswith("rtbf,") for line in etext.splitlines()):
    # check partial
    if ",rtbf," not in etext and not etext.__contains__("\nrtbf,"):
        append_lines(DATA / "entities.csv", [
            "rtbf,RTBF,RTBF,Radio-Television belge de la Communaute francaise,agency,fwb_gov,fr,https://www.rtbf.be,,,PSB FWB; 2025 public package 378.1m ordinary 350.8; recettes 479.7m; dual VRT",
        ])
else:
    # may already exist - skip
    pass

# research_queue
rtext, renc = read_text(DATA / "research_queue.csv")
old = (
    'rq_135,RTBF multi-year full financing primary,continuous,6,open,L2,rtbf,'
    '"RTBF public financing cash-by-year primary.",'
    ",2026-07-27T14:00:00Z,2026-07-27T14:00:00Z,"
)
new = (
    'rq_135,RTBF multi-year full financing primary,continuous,6,done,L2,rtbf,'
    '"RTBF public financing cash-by-year primary.",'
    "gap_rtbf_complement_split,2026-07-27T14:00:00Z,2026-07-27T21:50:00Z,"
    '"tick145: 2025 package 378.1m (ord 350.8+compl); 2023 total dots 366.9; savings 132m; FOI residual 2024 full split"'
)
if old not in rtext:
    # try without trailing empty notes
    raise SystemExit("rq_135 OLD NOT FOUND:\n" + "\n".join(l for l in rtext.splitlines() if "rq_135" in l))
write_text(DATA / "research_queue.csv", rtext.replace(old, new, 1), renc)

# FOI residual for 2024 full complementary split + 2026 budget codes
FOI.mkdir(parents=True, exist_ok=True)
(FOI / "gap_rtbf_complement_split.md").write_text(
    """# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `gap_rtbf_complement_split`  
**Status:** ready (human send only)  
**Linked:** rq_135 · cmt_rtbf_public_package_2023_28 · lb_rtbf_public_package

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: RTBF — service communication / transparantie
     en/of Federation Wallonie-Bruxelles — Budget et Medias / publicite de l administration
     (also CSA for control reports if held)

Betreft: Verzoek om openbaarmaking — RTBF volledige openbare financierings-split 2023-2026

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Cash-by-year 2023-2026 van alle openbare middelen aan de RTBF, gesplitst in:
   - dotation ordinaire;
   - subvention complementaire pensions / pool parastataux;
   - dotation TV5;
   - dotation accessibilite;
   - subvention responsabilisation SEC (of opvolger);
   - eventuele andere FWB- of federale lijnen.
2. Begrotingsartikels / codes FWB per lijn voor 2024, 2025 en 2026.
3. Uitvoeringscijfers van het spaarplan 132 miljoen 2025-2028 (gerealiseerd vs gepland per jaar).
4. Jaarrekening / rapport financier 2024 met dezelfde detailgraad als de website-pagina 2025.

Periode: 2023-01-01 tot meest recente stand.

### 2. Context

Primaire bronnen 2023 (CSA) en 2025 (rapportannuelrtbf.be) zijn publiek.
Ontbrekend: volledige 2024 complement-split en FWB budgetcodes; spaarpad-cash.

Hierarchie: FWB > Media > RTBF.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: gap_rtbf_complement_split

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling
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
    "gap_rtbf_complement_split,FWB>Media>RTBF>complementary_dots,rtbf,Full complementary public-dot split 2024 and FWB budget codes 2024-2026; savings plan 132m cash delivery by year,2023 CSA + 2025 RA package filled strong; 2024 full split thin,5,RTBF / FWB Budget Medias publicite,,,docs/doge/foi/drafts/gap_rtbf_complement_split.md,ready,2026-07-27,,,,,cmt_rtbf_public_package_2023_28,lb_rtbf_public_package,2026-07-27T21:50:00Z,2026-07-27T21:50:00Z,tick145 partial; human send",
])

# loop_state
write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    '"Scheduler 60s. Next prio6 VRT Actiris Myria; FOI ready human send. rq_135 RTBF package done."\n',
    "utf-8",
)

# loop_log
log_text, log_enc = read_text(ROOT / "loop_log.md")
if not log_text.endswith("\n"):
    log_text += "\n"
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (RTBF multi-year full public financing primary)
- Found (strong CSA 2023 control + RTBF RA 2025 finances page):
  - **2025 public package: EUR 378.1m** = ordinary **350.8** + pension **13.7** + TV5 **9.5** + access **4.1**.
  - **Total recettes 2025: EUR 479.7m** (−0.8%); ads **61.4m** (−9%); other **29.3m** (cable 12.6).
  - **2023 total dots: EUR 366.9m** (ordinary **332.8m** + TV5 9.4 + pension 14.5 + SEC 10.2); ads 66.0; exp 464.4; net PSO cost 370.1.
  - Dots series 2017-23: 260.5 → 366.9m; **foregone 2025 vs contract 15.9m** (no index/+2%).
  - Savings plan **EUR 132m 2025-28** (55.2m in 2028); cash **92.8m**; LT debt **46.7m**.
  - Dual PSB: VRT ordinary ~296.4 + RTBF package ~378 ≈ **~674m** class (updates prior 647m ordinary-only dual).
- Wrote: sources 3; budgets 27; cmt_rtbf_public_package; lb_rtbf; rq_135=done; FOI residual ready.
- FOI: gap_rtbf_complement_split (2024 split + codes + savings cash) human send.
- Next: prio6 **rq_136 VRT** / **rq_134 Actiris** / **rq_120 Myria**.
"""
write_text(ROOT / "loop_log.md", log_text + entry, log_enc)
print("tick145 write OK")
