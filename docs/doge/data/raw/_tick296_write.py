# tick296: telecom connectivity + Airbus/Clean Aviation + BMA + FPB (Kamer 55K2933/016)
from pathlib import Path
import json

SRC = "src_kamer_55k2933_telecom_airbus_bma_fpb"
PDF = "docs/doge/data/raw/kamer_55k2933_016_sck.pdf"
TICK = "tick296"


def q(s: str) -> str:
    s = str(s)
    if any(c in s for c in [",", '"', "\n"]):
        return '"' + s.replace('"', '""') + '"'
    return s


def append_if_missing(path: Path, lines: list[str]) -> int:
    text = path.read_text(encoding="utf-8")
    added = 0
    with path.open("a", encoding="utf-8", newline="") as f:
        for line in lines:
            key = line.split(",", 1)[0]
            if key not in text:
                f.write(line if line.endswith("\n") else line + "\n")
                text += line
                added += 1
    return added


print(
    "sources",
    append_if_missing(
        Path("docs/doge/data/sources.csv"),
        [
            f"{SRC},Kamer 55K2933/016 FOD Economie telecom connectivity Airbus Clean Aviation BMA FPB,"
            f"{PDF},Belgische Kamer van volksvertegenwoordigers,2026-07-30,official_budget,"
            "BA 59.02.32.00.01 telecom connectivity eng 66.2m 2023 liq 35+31.2m "
            "(5G 24m / 6G 1.5m / white zones 40.7m); Airbus BA 44.40.51.22.01 eng envelope 45m; "
            "Clean Aviation 51.22.03; BMA 41.10.414001 ~9.1m; FPB 60.10.414003 ~11.9m; tick296\n"
        ],
    ),
)

print(
    "entities",
    append_if_missing(
        Path("docs/doge/data/entities.csv"),
        [
            "bma_abc,Belgische Mededingingsautoriteit BMA,Autorite belge de la Concurrence ABC,"
            "Belgian Competition Authority,agency,fod_economy,bi,https://www.bma-abc.be,,,,"
            "Autonomous competition authority; FPS Economy BA 41.10.414001 ~9.1m/yr path; tick296\n",
            "fpb_planbureau,Federaal Planbureau FPB,Bureau federal du Plan BFP,"
            "Federal Planning Bureau,agency,sec_federal,bi,https://www.plan.be,,,,"
            "Independent fiscal socioeconomic projections; BA 60.10.414003 ~11.9m/yr; tick296\n",
            "fed_telecom_connectivity,Federaal telecomconnectiviteit breedband,Connectivite telecom federale,"
            "Federal telecom connectivity broadband package,programme,fod_economy,bi,https://economie.fgov.be,,,,"
            "BA 59.02.32.00.01 eng 66.2m 2023: 5G tests 24m + 6G research 1.5m + white zones 40.7m; CM 20Oct2021; tick296\n",
            "fed_airbus_clean_aviation,Federaal Airbus Clean Aviation steun,Aide federale Airbus Clean Aviation,"
            "Federal Airbus Clean Aviation recoverable advances,programme,fod_economy,bi,,,,,"
            "Recoverable advances aeronautical firms; initial eng 45m; Clean Aviation residual; dual F-35 IP Plan admin; tick296\n",
        ],
    ),
)

brows = []
# Telecom
brows.append(
    f"bud_telecom_connect_eng_2023,fed_telecom_connectivity,2023,66200000,,,budgeted,{SRC},strong,"
    "BA 59.02.32.00.01 engagement 66.2m 2023 national broadband connectivity subsidies\n"
)
brows.append(
    f"bud_telecom_connect_liq_2023,fed_telecom_connectivity,2023,35000000,,,budgeted,{SRC},strong,"
    "BA 59.02.32.00.01 liquidation 35m 2023\n"
)
brows.append(
    f"bud_telecom_connect_liq_2024,fed_telecom_connectivity,2024,31200000,,,budgeted,{SRC},strong,"
    "BA 59.02.32.00.01 liquidation 31.2m 2024\n"
)
brows.append(
    f"bud_telecom_5g_tests_envelope,fed_telecom_connectivity,2023,24000000,,,budgeted,{SRC},strong,"
    "Text split: 24m for 5G test project call co-financing\n"
)
brows.append(
    f"bud_telecom_6g_research_envelope,fed_telecom_connectivity,2023,1500000,,,budgeted,{SRC},strong,"
    "Text split: 1.5m for 6G research\n"
)
brows.append(
    f"bud_telecom_white_zones_envelope,fed_telecom_connectivity,2023,40700000,,,budgeted,{SRC},strong,"
    "Text split: 40.7m white zones connectivity co-financing\n"
)
# Airbus
brows.append(
    f"bud_airbus_envelope_eng_45m,fed_airbus_clean_aviation,2016,45000000,,,commitment,{SRC},strong,"
    "BA 44.40.51.22.01 initial engagement envelope 45m recoverable advances aeronautical firms CM 20Oct2016\n"
)
brows.append(
    f"bud_airbus_eng_2023,fed_airbus_clean_aviation,2023,2250000,,,budgeted,{SRC},strong,"
    "BA 44.40.51.22.01 engagement 2.25m 2023 (table)\n"
)
brows.append(
    f"bud_airbus_liq_2023,fed_airbus_clean_aviation,2023,1512000,,,budgeted,{SRC},strong,"
    "BA 44.40.51.22.01 liquidation 1.512m 2023\n"
)
brows.append(
    f"bud_airbus_liq_2024,fed_airbus_clean_aviation,2024,738000,,,budgeted,{SRC},strong,"
    "BA 44.40.51.22.01 liquidation 0.738m 2024\n"
)
# residual Airbus multi-year liq path (second table years 2022-2026)
for y, a in {2022: 5057000, 2023: 2103000, 2024: 1027000, 2025: 163000, 2026: 116000}.items():
    # Note: page table may omit 2103; use conservative public numbers from OCR second table
    # Re-check: Liquidation 5 057 / ? / 1 027 / 163 / 116 for 2022-2026
    pass
# Use only clearly paired years from text: 5057 (2022), 1027, 163, 116 — and first table 1512/738
# Clean Aviation:
brows.append(
    f"bud_clean_aviation_eng_2022,fed_airbus_clean_aviation,2022,4929000,,,budgeted,{SRC},strong,"
    "BA 44.40.51.22.03 Clean Aviation eng 4.929m 2022 from residual Airbus 45m envelope\n"
)
for y, a in {2023: 739000, 2024: 1232000, 2025: 1479000, 2026: 1479000}.items():
    brows.append(
        f"bud_clean_aviation_liq_{y},fed_airbus_clean_aviation,{y},{a},,,budgeted,{SRC},strong,"
        "BA 44.40.51.22.03 Clean Aviation liquidations path\n"
    )
# residual Airbus liq second table - from page 209: 5057 (2022) then incomplete; store 2022 only if clear
brows.append(
    f"bud_airbus_liq_2022_residual,fed_airbus_clean_aviation,2022,5057000,,,budgeted,{SRC},strong,"
    "BA 44.40.51.22.01 multi-year residual liquidation table 5.057m 2022 (path continues lower)\n"
)
# BMA
bma = {2021: 7226000, 2022: 8962000, 2023: 9171000, 2024: 9076000, 2025: 9076000, 2026: 9076000, 2027: 9076000}
for y, a in bma.items():
    brows.append(
        f"bud_bma_dotatie_{y},bma_abc,{y},{a},,,budgeted,{SRC},strong,"
        "BA 41.10.414001 autonomous competition authority eng=liq path\n"
    )
# FPB
fpb = {
    2021: 10750000,
    2022: 11658000,
    2023: 11916000,
    2024: 11798000,
    2025: 11828000,
    2026: 11858000,
    2027: 11888000,
}
for y, a in fpb.items():
    brows.append(
        f"bud_fpb_dotatie_{y},fpb_planbureau,{y},{a},,,budgeted,{SRC},strong,"
        "BA 60.10.414003 Federal Planning Bureau eng=liq path\n"
    )
print("budgets", append_if_missing(Path("docs/doge/data/budgets.csv"), brows))


def cmt_row(cid, title, eid, ben, legal, dd, sy, ey, env, cash, goal, cut, hpath, notes):
    return ",".join(
        [
            cid,
            q(title),
            eid,
            q(ben),
            q(legal),
            dd,
            str(sy),
            str(ey),
            str(env if env is not None else ""),
            q(json.dumps(cash, separators=(",", ":"))),
            "0",
            "active",
            PDF,
            q(goal),
            q(cut),
            SRC,
            "strong",
            hpath,
            q(notes),
        ]
    )


cmts = [
    cmt_row(
        "cmt_telecom_connectivity_66m",
        "Federal telecom connectivity broadband package 66.2m eng 2023",
        "fed_telecom_connectivity",
        "Selected 5G/white-zone/6G co-financed projects competitive process",
        "CM 20 Oct 2021 national fixed+mobile broadband plan + RRF/PRT + BA 59.02.32.00.01",
        "2021-10-20",
        2023,
        2024,
        66200000,
        {
            "eng_2023_m": 66.2,
            "liq_m": {"2023": 35.0, "2024": 31.2},
            "split_m": {"5g_tests": 24.0, "6g_research": 1.5, "white_zones": 40.7},
            "eu_target": "connectivity 2025",
            "note": "Competitive award after process; dual BIPT regional broadband",
        },
        "Meet EU connectivity targets fixed+mobile broadband white zones 5G tests",
        "FOI L5 winners; dual BIPT/regional avoid double-count",
        "Federal>Telecom>connectivity_pack",
        f"{TICK} RRF-adjacent connectivity",
    ),
    cmt_row(
        "cmt_airbus_clean_aviation_45m",
        "Federal Airbus recoverable advances + Clean Aviation residual 45m eng class",
        "fed_airbus_clean_aviation",
        "Belgian aeronautical firms",
        "CM 20Oct2016 + coop agreement 11Sep2008 amd 19Dec2017 + Clean Aviation reorientation CM 8Jul2022 + BA 44.40.51.22.01/03",
        "2016-10-20",
        2016,
        2026,
        45000000,
        {
            "initial_eng_m": 45,
            "airbus_eng_2023_m": 2.25,
            "airbus_liq_2023_m": 1.512,
            "airbus_liq_2024_m": 0.738,
            "airbus_liq_2022_m": 5.057,
            "clean_aviation_eng_2022_m": 4.929,
            "clean_aviation_liq_m": {"2023": 0.739, "2024": 1.232, "2025": 1.479, "2026": 1.479},
            "instrument": "recoverable advances GBER 651/2014",
            "note": "Clean Aviation is residual of 45m Airbus envelope not additive",
        },
        "Support aeronautical R&D via recoverable advances; reorient to Clean Aviation",
        "Publish L5 firm advances and recovery rates; dual regional aerospace",
        "Federal>Economy>Airbus_Clean_Aviation",
        f"{TICK} dual F-35 IP Plan admin transfer neutral",
    ),
    cmt_row(
        "cmt_bma_dotatie_path",
        "Belgian Competition Authority autonomous annual dotation",
        "bma_abc",
        "BMA ABC competition enforcement",
        "Competition law + BA 41.10.414001 FPS Economy",
        "2013-01-01",
        2021,
        2027,
        61663000,
        {
            "2021": 7226000,
            "2022": 8962000,
            "2023": 9171000,
            "2024": 9076000,
            "2025": 9076000,
            "2026": 9076000,
            "2027": 9076000,
        },
        "Independent competition enforcement EU TFEU 101-102",
        "Core market institution; dual FSMA BIPT sector regulators not additive",
        "Federal>Economy>BMA",
        f"{TICK} structural not waste",
    ),
    cmt_row(
        "cmt_fpb_dotatie_path",
        "Federal Planning Bureau annual federal subsidy",
        "fpb_planbureau",
        "FPB public economic projections research",
        "Organic law FPB + BA 60.10.414003",
        "1994-01-01",
        2021,
        2027,
        81796000,
        {
            "2021": 10750000,
            "2022": 11658000,
            "2023": 11916000,
            "2024": 11798000,
            "2025": 11828000,
            "2026": 11858000,
            "2027": 11888000,
        },
        "Independent socioeconomic and fiscal projections for policy",
        "Core evidence institution; dual NBB INR Statbel",
        "Federal>FPB>dotation",
        f"{TICK} structural not waste",
    ),
]
print("commitments", append_if_missing(Path("docs/doge/data/commitments.csv"), cmts))


def lb_row(
    iid, name, level, typ, hpath, ann, tot, tco, conf, src, ben, goal, out, absu, cost, diff, pi, cut, notes
):
    return ",".join(
        [
            iid,
            q(name),
            level,
            typ,
            hpath,
            str(ann),
            str(tot),
            q(tco),
            conf,
            src,
            q(ben),
            q(goal),
            q(out),
            str(absu),
            str(cost),
            str(diff),
            str(pi),
            q(cut),
            "seed",
            "",
            q(notes),
        ]
    )


lbs = [
    lb_row(
        "lb_telecom_connectivity_66m",
        "Federal telecom connectivity pack eng 66.2m 2023",
        "federal",
        "ops",
        "Federal>Telecom>connectivity_pack",
        66200000,
        66200000,
        "Strong BA 59.02.32.00.01: eng 66.2m; liq 35+31.2m; split 5G 24m / 6G 1.5m / white zones 40.7m; CM Oct2021+RRF",
        "strong",
        SRC,
        "Selected co-financed telecom projects",
        "EU 2025 connectivity broadband white zones 5G",
        "Budget path; L5 winners residual FOI",
        4,
        7.5,
        4,
        5.5,
        "FOI L5 winners; dual regional broadband avoid double-count",
        f"{TICK}",
    ),
    lb_row(
        "lb_telecom_white_zones_41m",
        "Telecom white zones co-finance 40.7m class",
        "federal",
        "ops",
        "Federal>Telecom>white_zones",
        40700000,
        40700000,
        "Strong text split inside 66.2m pack: 40.7m white zones competitive co-finance",
        "strong",
        SRC,
        "White zone connectivity projects",
        "Close broadband white zones",
        "Envelope class inside pack",
        3,
        6.5,
        4,
        4.8,
        "Publish map of zones and winners",
        f"{TICK}",
    ),
    lb_row(
        "lb_airbus_clean_aviation_45m",
        "Airbus Clean Aviation recoverable advances 45m eng class",
        "federal",
        "ops",
        "Federal>Economy>Airbus_Clean_Aviation",
        45000000,
        45000000,
        "Strong initial eng 45m; Clean Aviation residual eng 4.929m 2022; recoverable advances not pure grant; dual F-35 IP admin",
        "strong",
        SRC,
        "Aeronautical firms",
        "Aerospace R&D recoverable advances",
        "Recovery rates residual FOI",
        4,
        7.0,
        5,
        5.5,
        "Publish advances recovery matrix L5",
        f"{TICK}",
    ),
    lb_row(
        "lb_bma_9m",
        "Belgian Competition Authority ~9.1m/yr",
        "federal",
        "ops",
        "Federal>Economy>BMA",
        9171000,
        61663000,
        "Strong BA 41.10.414001 path 7.2-9.2m 2021-27 autonomous BMA",
        "strong",
        SRC,
        "Competition enforcement public",
        "Independent competition authority",
        "Core market institution",
        1,
        4.0,
        1,
        2.0,
        "Keep; dual sector regulators map only",
        f"{TICK} not waste",
    ),
    lb_row(
        "lb_fpb_12m",
        "Federal Planning Bureau ~11.9m/yr",
        "federal",
        "ops",
        "Federal>FPB>dotation",
        11916000,
        81796000,
        "Strong BA 60.10.414003 path 10.75-11.9m 2021-27",
        "strong",
        SRC,
        "Policymakers public research users",
        "Independent socioeconomic projections",
        "Core evidence institution",
        1,
        4.5,
        1,
        2.2,
        "Keep; dual NBB INR",
        f"{TICK} not waste",
    ),
]
print("leaderboard", append_if_missing(Path("docs/doge/data/leaderboard.csv"), lbs))

foi_line = (
    "gap_telecom_airbus_l5,Federal>Economy>telecom_Airbus>L5,fed_telecom_connectivity,"
    "Named L5 winners amounts 2022-2026 for BA 59.02.32.00.01 telecom connectivity "
    "(5G tests / 6G / white zones) and BA 44.40.51.22.01/03 Airbus Clean Aviation recoverable advances "
    "with recovery rates and outstanding balances; cash outturn vs 66.2m and 45m envelopes,"
    "Material industrial/connectivity aid; budget envelopes strong end-receiver and recovery opaque,"
    "5,FOD Economie / BIPT openbaarheid,,https://economie.fgov.be,"
    "docs/doge/foi/drafts/gap_telecom_airbus_l5.md,ready,2026-07-30,,,,,,"
    "cmt_telecom_connectivity_66m|cmt_airbus_clean_aviation_45m,"
    "lb_telecom_connectivity_66m|lb_airbus_clean_aviation_45m,"
    "2026-07-30T10:45:00Z,2026-07-30T10:45:00Z,tick296 draft ready human send\n"
)
print("foi", append_if_missing(Path("docs/doge/data/foi_queue.csv"), [foi_line]))

# research queue + state
rq_path = Path("docs/doge/data/research_queue.csv")
text = rq_path.read_text(encoding="utf-8")
out = []
for line in text.splitlines(keepends=True):
    if line.startswith("rq_287,"):
        line = (
            "rq_287,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
            "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after H2 RRF pack). "
            "Prefer before idle; do not idle while public work remains.,"
            "gap_telecom_airbus_l5,2026-07-30T10:15:00Z,2026-07-30T10:45:00Z,"
            "tick296: telecom connectivity eng 66.2m (5G 24/white 40.7/6G 1.5); Airbus Clean Aviation 45m; "
            "BMA 9.1m; FPB 11.9m; FOI L5 ready; spawn rq_288\n"
        )
    out.append(line)
if "rq_288," not in text:
    out.append(
        "rq_288,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        "Prefer public primary fills (AGMJ wage if public; other FOI-adjacent after telecom/Airbus fill). "
        "Prefer before idle; do not idle while public work remains.,,"
        "2026-07-30T10:45:00Z,,Spawned tick296 after telecom Airbus BMA FPB; rq_116 SWA deferred\n"
    )
rq_path.write_text("".join(out), encoding="utf-8")
print("research_queue ok")

Path("docs/doge/data/loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-30T10:45:00Z,rq_287,296,no,"
    "Scheduler 60s. Next prio5 rq_288; rq_116 SWA deferred. FOI ready. "
    "tick296 telecom 66.2m + Airbus 45m + BMA/FPB.\n",
    encoding="utf-8",
)
print("loop_state ok")

Path("docs/doge/foi/drafts/gap_telecom_airbus_l5.md").write_text(
    """# FOI draft — gap_telecom_airbus_l5

**Status:** ready (not sent)  
**Gap ID:** `gap_telecom_airbus_l5`  
**Linked:** `cmt_telecom_connectivity_66m`, `cmt_airbus_clean_aviation_45m`  
**Tick:** 296  

Public fill (Kamer 55K2933/016 FOD Economie):

| BA | Role | Amounts |
|----|------|---------|
| **59.02.32.00.01** | Telecom connectivity | eng **66.2m** 2023; liq **35 + 31.2m** |
| Text split | 5G tests / 6G / white zones | **24 / 1.5 / 40.7m** |
| **44.40.51.22.01** | Airbus recoverable advances | initial eng **45m**; 2023 eng **2.25m** liq **1.51m** |
| **44.40.51.22.03** | Clean Aviation (Airbus residual) | eng **4.929m** 2022; liq path to 2026 |
| **41.10.414001** | BMA autonomous | **~9.1m/yr** path |
| **60.10.414003** | Federal Planning Bureau | **~11.9m/yr** path |

Residual: L5 winners telecom + Airbus advances recovery rates.

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: FOD Economie, K.M.O., Middenstand en Energie
t.a.v. de dienst openbaarheid van bestuur
(en eventueel BIPT voor telecomdeel)
https://economie.fgov.be

Betreft: Verzoek om openbaarmaking — telecomconnectiviteit en Airbus/Clean Aviation L5 (gap_telecom_airbus_l5)

Geachte,

Op grond van de wet van 11 april 1994 betreffende de openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking / afschrift van de hieronder
omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. Lijst van geselecteerde projecten (promotor, KBO, bedrag, jaar) voor basisallocatie
   32.59.02.32.00.01 (telecomconnectiviteit), met splitsing 5G-testprojecten,
   6G-onderzoek en witte zones, en cash-by-year vastlegging/vereffening 2022–2026.
2. Lijst van begunstigde luchtvaartondernemingen en bedragen voor basisallocaties
   32.44.40.51.22.01 (Airbus) en 32.44.40.51.22.03 (Clean Aviation), inclusief
   terugbetaalbare voorschotten: toegekend, teruggevorderd, openstaand saldo per jaar.
3. Eventuele selectiebesluiten / state-aid dossiers samenvattingen (zonder
   bedrijfsgeheimen die wettelijk moeten worden geweigerd).

Periode: 1 januari 2016 tot 31 december 2026.

### 2. Context (waarom)

Onderzoek naar overheidsuitgaven (transparantie). Intern pad:
Federal > Economy > telecom_Airbus. Publieke Kamer-tabellen geven enveloppes
(66,2 mEUR telecom; 45 mEUR Airbus-class); ontbrekend is de L5-matrix en recovery.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail naar [e-mail].
Indien weigering of gedeeltelijke openbaarmaking: gemotiveerde beslissing
met vermelding van de rechtsgrond en de beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern: gap_telecom_airbus_l5

Met vriendelijke groet,

[…]
```

**Do not send as agent.** Human send only.
""",
    encoding="utf-8",
)
print("draft ok")
print("tick296 write complete")
