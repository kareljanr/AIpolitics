# -*- coding: utf-8 -*-
"""Tick 156 — rq_146 Federal development cooperation DGD top L5 / envelopes."""
from pathlib import Path

ROOT = Path(r"C:\Users\karel\dev\AIpolitics")
DATA = ROOT / "docs" / "doge" / "data"
FOI = ROOT / "docs" / "doge" / "foi" / "drafts"
TICK = 156
UNIT = "rq_146"
UTC = "2026-07-28T01:40:00Z"
GAP = "gap_dgd_l5_projects"


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


srcs = [
    'src_dgd_ar_2025,DGD Annual Report 2025 Belgian International Cooperation and Humanitarian Aid,https://openaid.be/sites/default/files/2026-06/Annual%20Report%20DGD%202025%20ENG.pdf,DGD FPS Foreign Affairs,2026-07-28,official_annual_report,"Total DGD 1117.97m 2025; top recipients DRC 104.5m; humanitarian 170m; Enabel line 212m; -25pct path by 2027; tick156"',
    'src_enabel_ra_2025_26,Enabel Rapport d activites 2025-2026 finances,https://www.enabel.be/app/uploads/2026/05/Enabel_Rapport_dActivites_2025_26_FR.pdf,Enabel,2026-07-28,official_annual_report,"Turnover 407.1m 2025; op charges 438.1m; personnel 91.0m; EU contracts 152m; intl finance contracts 182m; target ~400m activities; tick156"',
    'src_openaid_about_2025,Openaid.be about Belgian ODA 2025 DGD 1.117bn,https://openaid.be/en/about,DGD Openaid,2026-07-28,official_web,"0.37pct GNI; DGD 1.117bn; humanitarian 170m 2025; tick156"',
    'src_oecd_dac_belgium_2025,OECD Development Cooperation Profiles Belgium 2025,https://www.oecd.org/en/publications/2025/06/development-co-operation-profiles_02ffa45c/belgium_561d9aeb.html,OECD DAC,2026-07-28,official_international,"ODA USD 2.7bn 0.37pct GNI 2025 prelim; DGD -25pct path to 2027; tick156"',
]
append_if_missing(DATA / "sources.csv", srcs)

ents = [
    "dgd,Direction generale Cooperation au developpement et Aide humanitaire (DGD),Directoraat-generaal Ontwikkelingssamenwerking en Humanitaire Hulp,Directorate-General for Development Cooperation and Humanitarian Aid,agency,sec_federal,bi,https://diplomatie.belgium.be,,Brussels,Federal ODA manager; total 1117.97m 2025; -25pct path 2027; tick156",
    "enabel,Enabel Agence belge de developpement,Enabel Belgisch ontwikkelingsagentschap,Enabel Belgian development agency,agency,sec_federal,bi,https://www.enabel.be,,Brussels,Public SA implementing governmental coop; turnover 407m 2025; >40pct EU resources; tick156",
    "bio_invest,BIO Belgian Investment Company for Developing Countries,BIO Belgische Investeringsmaatschappij,BIO development finance institution,agency,sec_federal,bi,https://www.bio-invest.be,,Brussels,DFI private sector developing countries; approvals class 217-230m 2024-25; tick156",
]
append_if_missing(DATA / "entities.csv", ents)

# budgets EUR
bud = [
    # DGD totals
    "bud_dgd_total_2025,dgd,2025,1117970000,,,outturn,src_dgd_ar_2025,strong,DGD total Official Development Assistance channel 1117.97m EUR 2025 AR table",
    "bud_dgd_total_2024,dgd,2024,1440920000,,,outturn,src_dgd_ar_2025,strong,DGD total 1440.92m 2024",
    "bud_dgd_total_2023,dgd,2023,1285900000,,,outturn,src_dgd_ar_2025,strong,DGD total 1285.90m 2023",
    "bud_dgd_cut_2025,dgd,2025,-106000000,,,budgeted,src_dgd_ar_2025,strong,Budget reduced by 106m in 2025 first year of progressive -25pct path to 2027",
    # channels
    "bud_dgd_enabel_2025,enabel,2025,212020000,,,outturn,src_dgd_ar_2025,strong,DGD line Belgian Development Agency Enabel 212.02m 2025",
    "bud_dgd_enabel_mgmt_2025,enabel,2025,25570000,,,outturn,src_dgd_ar_2025,strong,Management costs of Enabel 25.57m 2025",
    "bud_dgd_gov_subtotal_2025,dgd,2025,250350000,,,outturn,src_dgd_ar_2025,strong,Sub-total governmental cooperation 250.35m 2025",
    "bud_dgd_humanitarian_2025,dgd,2025,170000000,,,outturn,src_dgd_ar_2025,strong,Humanitarian programmes 170m 2025 exempt from cuts 70pct flexible",
    "bud_dgd_climate_policy_2025,dgd,2025,102180000,,,outturn,src_dgd_ar_2025,medium,Climate policy line ~102.18m 2025 from AR table (OCR-adjacent years 100.82/101.51)",
    # thematic fig
    "bud_dgd_theme_climate_2025,dgd,2025,365300000,,,outturn,src_dgd_ar_2025,strong,Theme climate and environment 365.3m 32.5pct of DGD 2025",
    "bud_dgd_theme_stability_2025,dgd,2025,301800000,,,outturn,src_dgd_ar_2025,strong,Theme stability 301.8m 26.9pct",
    "bud_dgd_theme_humanitarian_2025,dgd,2025,181500000,,,outturn,src_dgd_ar_2025,medium,Theme humanitarian 181.5m 16.2pct (vs line item 170m; provisional dual series)",
    "bud_dgd_theme_other_2025,dgd,2025,175000000,,,outturn,src_dgd_ar_2025,strong,Theme other mainly skills/education 175.0m 15.6pct",
    "bud_dgd_theme_health_2025,dgd,2025,98800000,,,outturn,src_dgd_ar_2025,strong,Theme health 98.8m 8.8pct",
    # top recipients
    "bud_dgd_drc_2025,dgd,2025,104490000,,,outturn,src_dgd_ar_2025,strong,Top recipient DR Congo 104.49m DGD ODA 2025",
    "bud_dgd_burkina_2025,dgd,2025,28020000,,,outturn,src_dgd_ar_2025,strong,Burkina Faso 28.02m",
    "bud_dgd_uganda_2025,dgd,2025,27800000,,,outturn,src_dgd_ar_2025,strong,Uganda 27.80m",
    "bud_dgd_burundi_2025,dgd,2025,27180000,,,outturn,src_dgd_ar_2025,strong,Burundi 27.18m",
    "bud_dgd_niger_2025,dgd,2025,26290000,,,outturn,src_dgd_ar_2025,strong,Niger 26.29m",
    "bud_dgd_palestine_2025,dgd,2025,24710000,,,outturn,src_dgd_ar_2025,strong,Palestine 24.71m",
    "bud_dgd_senegal_2025,dgd,2025,20060000,,,outturn,src_dgd_ar_2025,strong,Senegal 20.06m",
    "bud_dgd_ukraine_2025,dgd,2025,18160000,,,outturn,src_dgd_ar_2025,strong,Ukraine 18.16m",
    "bud_dgd_benin_2025,dgd,2025,17820000,,,outturn,src_dgd_ar_2025,strong,Benin 17.82m",
    "bud_dgd_mali_2025,dgd,2025,14590000,,,outturn,src_dgd_ar_2025,strong,Mali 14.59m",
    # named climate L5 samples from AR narrative
    "bud_dgd_ldcf_2025,dgd,2025,18500000,,,outturn,src_dgd_ar_2025,strong,LDCF contribution 18.5m 2025 Belgium 2nd largest donor",
    "bud_dgd_sahel_climate_2025,dgd,2025,50000000,,,outturn,src_dgd_ar_2025,strong,Belgium investing 50m in Sahel climate/stability package cited AR",
    "bud_dgd_soff_extra_2025,dgd,2025,8300000,,,outturn,src_dgd_ar_2025,strong,SOFF initiative additional 8.3m on top of prior 11m total >19m",
    # Enabel institutional
    "bud_enabel_turnover_2025,enabel,2025,407097008,,,outturn,src_enabel_ra_2025_26,strong,Chiffre d affaires 407097008 EUR 2025 (329159608 in 2024)",
    "bud_enabel_op_products_2025,enabel,2025,435600343,,,outturn,src_enabel_ra_2025_26,strong,Produits d exploitation 435.6m 2025",
    "bud_enabel_op_charges_2025,enabel,2025,438055645,,,outturn,src_enabel_ra_2025_26,strong,Charges d exploitation 438.1m 2025",
    "bud_enabel_personnel_2025,enabel,2025,91021649,,,outturn,src_enabel_ra_2025_26,strong,Personnel costs 91.02m 2025",
    "bud_enabel_assets_2025,enabel,2025,217367384,,,outturn,src_enabel_ra_2025_26,strong,Balance sheet total assets 217.4m EOY2025",
    "bud_enabel_eu_contracts_2025,enabel,2025,152000000,,,commitment,src_enabel_ra_2025_26,strong,EU/Team Europe 22 contracts +2 budget increases total 152m signed 2025",
    "bud_enabel_intl_finance_2025,enabel,2025,182000000,,,commitment,src_enabel_ra_2025_26,strong,Contracts with international financial partners 182m 2025 of which 80pct public mandate",
    "bud_enabel_activity_target_2025,enabel,2025,400000000,,,budgeted,src_enabel_ra_2025_26,medium,Organisational target approaching 400m annual activities 2025",
]
append_if_missing(DATA / "budgets.csv", bud)

cmts = [
    (
        'cmt_dgd_oda_path_2023_25,DGD total ODA multi-year path 2023-2025 + cut framework,dgd,Partner countries multilateral NGOs Enabel,'
        'DGD Annual Report 2025 + Arizona -25pct path,2025-01-01,2023,2027,1117970000,'
        '"{""2023"":1285900000,""2024"":1440920000,""2025"":1117970000,""cut_2025"":-106000000,'
        '""path"":""-25pct structural by 2027 first year 2025"",""humanitarian_2025"":170000000,'
        '""enabel_line_2025"":212020000,""gov_subtotal_2025"":250350000,'
        '""theme_climate"":365300000,""theme_stability"":301800000,""theme_health"":98800000}",0,active,'
        'https://openaid.be,International development humanitarian climate health stability,'
        'Publish Openaid machine L5 project export; track -25pct cash delivery; outcome KPIs by partner country,'
        'src_dgd_ar_2025,strong,Federal>DGD>ODA,'
        'tick156; residual project-level L5 FOI; OECD total ODA broader than DGD'
    ),
    (
        'cmt_enabel_package_2025,Enabel institutional turnover and EU diversification 2025,enabel,Enabel partners countries EU,'
        'Enabel RA 2025-2026 bilans,2026-05-01,2024,2026,407097008,'
        '"{""2025_turnover"":407097008,""2024_turnover"":329159608,""2025_op_charges"":438055645,'
        '""2025_personnel"":91021649,""2025_eu_contracts"":152000000,""2025_intl_finance"":182000000,'
        '""assets_eoy2025"":217367384,""eu_share_class"":""over 40pct resources from EU""}",0,active,'
        'https://www.enabel.be,Governmental development implementation Global Gateway corridors,'
        'Reconcile DGD 212m line vs Enabel turnover 407m (other donors); publish per-country portfolio L5,'
        'src_enabel_ra_2025_26,strong,Federal>Enabel>finance,'
        'tick156; multi-donor agency; Belgian DGD only part of turnover'
    ),
    (
        'cmt_dgd_top_recipients_2025,DGD top recipient countries 2025 sample L5,dgd,Partner country programmes,'
        'DGD AR 2025 top20 table,2026-05-01,2025,2025,346620000,'
        '"{""drc"":104490000,""burkina"":28020000,""uganda"":27800000,""burundi"":27180000,'
        '""niger"":26290000,""palestine"":24710000,""senegal"":20060000,""ukraine"":18160000,'
        '""benin"":17820000,""mali"":14590000,""top10_sum"":309280000}",0,active,'
        'https://openaid.be,Partner country development programmes,'
        'Open project-level cash inside country envelopes; Rwanda interruption 2025 noted Enabel,'
        'src_dgd_ar_2025,strong,Federal>DGD>recipients,'
        'tick156; country aggregates not end-project L5'
    ),
]
append_if_missing(DATA / "commitments.csv", cmts)

lbs = [
    "lb_dgd_oda_total,DGD ODA package ~1.12bn 2025 (-25pct path),federal,programme,Federal>DGD>ODA,1117970000,1117970000,AR strong: 1.118bn 2025 vs 1.441bn 2024; -106m cut year1; humanitarian 170m protected; climate theme 365m,strong,src_dgd_ar_2025,Partner countries vulnerable populations,Development humanitarian climate health stability,Core foreign policy spend; cut path needs outcome tracking not pure waste claim,3,8.5,4,6.0,Publish Openaid L5 CSV; protect high-impact health; track -25pct delivery,seed,,tick156",
    "lb_dgd_drc_envelope,DGD DR Congo top recipient ~104.5m 2025,federal,programme,Federal>DGD>DRC,104490000,104490000,Largest country envelope 104.49m; Enabel corridors Lobito/green shift; governance/mining CRM,strong,src_dgd_ar_2025,DRC populations institutions,Partner country development,Concentration risk; outcomes vs opacity of project L5,4,6.5,5,5.5,FOI top projects inside DRC envelope; publish unit costs,seed,,tick156",
    "lb_enabel_turnover,Enabel turnover ~407m 2025 (multi-donor),federal,ops,Federal>Enabel>turnover,407097008,407097008,RA strong turnover 407m vs DGD line 212m; EU contracts 152m; personnel 91m; result near zero,strong,src_enabel_ra_2025_26,Partner institutions EU Belgium foreign policy,Implement governmental and multi-donor programmes,Dual financing ok if additionality; overhead vs field ratio watch,3,7.0,4,5.3,Reconcile DGD vs multi-donor; open country portfolio L5,seed,,tick156",
    "lb_dgd_humanitarian,DGD humanitarian aid 170m 2025 protected,federal,programme,Federal>DGD>humanitarian,170000000,170000000,AR: 170m exempt from 2025 cuts; 70pct flexible; CERF/WFP channels cited,strong,src_dgd_ar_2025,Crisis-affected populations,Humanitarian principles emergency response,Core safety-net international; not waste if principled,2,6.0,3,4.3,Keep flexibility KPIs; publish top crises cash,seed,,tick156",
]
append_if_missing(DATA / "leaderboard.csv", lbs)

foi_row = (
    f"{GAP},Federal>DGD>Openaid>project_L5_top50,dgd,"
    "Machine-readable top 50 named projects/programmes by amount 2024-2026 with implementer (Enabel NGO multilateral BIO) country sector cash commitment vs disbursement; reconcile Enabel turnover 407m vs DGD Enabel line 212m,"
    "Country and channel aggregates public; end-project L5 bulk incomplete for DOGE matrix,"
    "6,DGD / FPS Foreign Affairs openbaarheid / Openaid,info.DGD@diplobel.fed.be,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    f"docs/doge/foi/drafts/{GAP}.md,ready,2026-07-28,,,,,"
    "cmt_dgd_oda_path_2023_25|cmt_enabel_package_2025,lb_dgd_oda_total,"
    f"{UTC},{UTC},tick156 partial fill country+channel; residual project L5 human send"
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
**Linked:** {UNIT} · cmt_dgd_oda_path_2023_25 · cmt_enabel_package_2025

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Datum]

Aan: Directie-generaal Ontwikkelingssamenwerking en Humanitaire Hulp (DGD)
     FOD Buitenlandse Zaken
     info.DGD@diplobel.fed.be
     en/of IBZ openbaarheid van bestuur

Betreft: Verzoek om openbaarmaking — top 50 DGD-projecten/programma's 2024-2026 (L5)

Geachte,

Op grond van de wet 11 april 1994 inzake openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Machine-readable export (CSV) van de 50 grootste DGD-financeringen 2024-2026
   met: project/programmanaam; implementer (Enabel / NGO / multilateraal / BIO / ander);
   partnerland; sector; verbintenis EUR; uitbetaling EUR; looptijd.
2. Reconciliatie van de DGD-lijn Enabel (EUR 212,02 miljoen 2025 in het jaarverslag)
   met de Enabel-omzet (EUR 407,1 miljoen 2025 in het Enabel-activiteitenverslag),
   inclusief aandeel Belgische vs EU/andere donoren.
3. Lijst van stopgezette of herziene bilaterale programma's 2025 (o.a. Rwanda)
   met resterende cash-verplichtingen.
4. BIO-goedkeuringen 2024-2026 met ticketgrootte per deal indien publiek deelbaar
   (of samenvatting top 20).

Periode: 2024-01-01 tot meest recente stand.

### 2. Context

DGD-jaarverslag 2025 en Openaid publiceren sterke totalen (DGD EUR 1.118 miljoen 2025;
topontvanger DRC EUR 104,5 miljoen; humanitair EUR 170 miljoen). Ontbrekend:
projectniveau L5 voor vergelijking end-receivers.

Hierarchie intern: Federal > DGD > Openaid projects L5.

### 3. Vorm

Digitale kopie (PDF/CSV) per e-mail naar [e-mail]. Bij voorkeur hergebruik Openaid-data.

### 4. Identiteit

Naam: […]
Dossierreferentie intern: {GAP}

Met vriendelijke groet,
[Naam]
```

---

## Checklist

- [x] Instelling (DGD)
- [x] Concrete documenten
- [x] Periode
- [ ] Contact verzoeker (human)
- [x] foi_queue ready

**Verify with counsel** — orientation only; human sends.
""", encoding="utf-8")

rq_new = (
    f"rq_146,Federal development cooperation top L5 projects,continuous,5,done,L5,sec_federal,"
    f'"DGD top projects with EUR.",{GAP},2026-07-27T14:00:00Z,{UTC},'
    "tick156: DGD total 1.118bn 2025; Enabel line 212m / turnover 407m; DRC 104.5m top; "
    "humanitarian 170m; residual project L5 FOI ready"
)
if not replace_line_startswith(DATA / "research_queue.csv", "rq_146,", rq_new):
    raise SystemExit("rq_146 not found")

write_text(
    DATA / "loop_state.csv",
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f'main,continuous,hole_fill,{UTC},{UNIT},{TICK},no,'
    f'"Scheduler 60s. Next prio5 defence justice police; FOI ready human send. rq_146 DGD ODA 1.12bn done."\n',
)

log_p = ROOT / "docs" / "doge" / "loop_log.md"
log_text = read_text(log_p)
entry = f"""
### {UTC} — tick {TICK}
- Unit: **{UNIT}** (Federal development cooperation DGD / Enabel L5 envelopes)
- Found (strong primary DGD AR 2025 + Enabel RA 2025-26):
  - **DGD total:** **EUR 1,117.97m 2025** (1,440.92m 2024; 1,285.90m 2023); cut **−106m** year1 of **−25% by 2027**.
  - **Channels:** Enabel line **212.02m** · gov subtotal **250.35m** · humanitarian **170m** (protected).
  - **Themes:** climate **365.3m** · stability **301.8m** · humanitarian theme **181.5m** · other **175.0m** · health **98.8m**.
  - **Top recipients:** DRC **104.49m** · Burkina **28.0** · Uganda **27.8** · Burundi **27.2** · Niger **26.3** · Palestine **24.7** · Senegal **20.1** · Ukraine **18.2** · Benin **17.8** · Mali **14.6**.
  - **Named samples:** LDCF **18.5m** · Sahel package **50m** · SOFF +**8.3m**.
  - **Enabel:** turnover **407.1m** (was 329.2m) · charges **438.1m** · personnel **91.0m** · EU contracts **152m** · intl finance **182m** · assets **217.4m**.
- Wrote: sources 4; entities 3; budgets ~35; cmt 3; lb 4; rq_146=done; FOI residual ready.
- FOI: {GAP} (top50 projects + Enabel reconcile) human send only.
- Next: prio5 **rq_147 defence** / **rq_150 justice** / **rq_151 police** / **rq_121 hole-fill**.
"""
if not log_text.endswith("\n"):
    log_text += "\n"
write_text(log_p, log_text + entry)
print("OK tick", TICK, UNIT)
