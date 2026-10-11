# -*- coding: utf-8 -*-
"""Tick 1390 — leftover Fluvius Riobra JR2025 official NBB WVV euros + every-10.
Surgical append/patch only. Does NOT rewrite research_queue.csv wholesale.
"""
from __future__ import annotations

import csv
import io
import sys
from collections import Counter
from pathlib import Path

csv.field_size_limit(sys.maxsize)
DATA = Path("/workspace/AIpolitics/docs/doge/data")
ROOT = DATA.parent

TICK = "1390"
UTC = "2026-08-19T05:50:00Z"
ENT = "igs_flri"
HIER = "Vlaanderen>VlaamsBrabant>IGS>FluviusRiobra"
GAP = "gap_flri_omzet_22_11m_diensten_10_19m_debt_122_29m_l5"
SRC = "src_flri_jr2025_nbb"
SRC2 = "src_flri_site"
SRC3 = "src_kbo_flri_0878051819"
SRC4 = "src_flri_foi_contact"
SRC_URL = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00205662.pdf"
SRC2_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-riobra/activiteitenverslagen"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0878051819"
SRC4_URL = "https://over.fluvius.be/nl/wie-zijn-we/governance/aandeelhouders/over-fluvius-riobra"
FOI_EMAIL = ""
FOI_POSTAL = "Diestsesteenweg 126 3210 Lubbeek"
DRAFT = "docs/doge/foi/drafts/gap_flri_omzet_22_11m_diensten_10_19m_debt_122_29m_l5.md"
COMM = "comm_flri_jr2025_pnl"
LB = "lb_flri_omzet_22_11m_diensten_10_19m_debt_122_29m"

VENNOTEN = (
    "Begijnendijk + Bekkevoort + Bertem + Bever + Boortmeerbeek + "
    "Boutersem + Geetbets + Glabbeek + Hoegaarden + Huldenberg + "
    "Kortenaken + Landen + Lennik + Linter + Lubbeek + Merchtem + "
    "Oud-Heverlee + Pepingen + Pajottegem + Rotselaar + "
    "Sint-Pieters-Leeuw + Steenokkerzeel + Tielt-Winge + Tienen + Zoutleeuw"
)


def append_rows(path, new_rows):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        existing_ids = set()
        id_key = fields[0]
        for row in reader:
            existing_ids.add(row.get(id_key))
    added = 0
    with open(path, "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        for row in new_rows:
            if row.get(id_key) in existing_ids:
                continue
            w.writerow({k: row.get(k, "") for k in fields})
            added += 1
    return added


def csv_line(fields, row):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", lineterminator="")
    w.writerow({k: row.get(k, "") for k in fields})
    return buf.getvalue()


def patch_last_rq_and_spawn(path, target_id, new_target, spawn_row):
    header = path.open(encoding="utf-8").readline()
    fields = next(csv.reader([header.strip("\n").strip("\r")]))
    with path.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        chunk = min(size, 131072)
        f.seek(size - chunk)
        tail = f.read()
    if tail.endswith(b"\n"):
        search = tail[:-1]
    else:
        search = tail
    last_nl = search.rfind(b"\n")
    last_line = search[last_nl + 1 :] if last_nl != -1 else search
    last_text = last_line.decode("utf-8")
    if not last_text.startswith(target_id + ","):
        raise SystemExit("last rq line is not %s: %s" % (target_id, last_text[:160]))
    last_start = (size - chunk) + (last_nl + 1 if last_nl != -1 else 0)
    spawn_id = spawn_row.get("task_id")
    if spawn_id and spawn_id.encode("utf-8") in tail:
        raise SystemExit("spawn id already in tail")
    payload = (csv_line(fields, new_target) + "\n" + csv_line(fields, spawn_row) + "\n").encode("utf-8")
    with path.open("r+b") as f:
        f.seek(last_start)
        f.truncate()
        f.write(payload)
    return True, True


def count_csv_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        n = sum(1 for _ in f) - 1
    return n


def foi_status_counts():
    c = Counter()
    with open(DATA / "foi_queue.csv", encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        for row in r:
            st = (row.get("status") or "").strip()
            if st in ("ready", "answered", "partial", "draft", "sent", "cancelled"):
                c[st] += 1
            else:
                c["_other"] += 1
    return c


BUDGETS = [
    ("bud_flri_assets_2025", "2025", "383253161", "2025 assets 383253161 VOL-inb 20/58; tick1390; primary official NBB WVV"),
    ("bud_flri_assets_2024", "2024", "345043278", "2024 assets 345043278 comparative; tick1390; primary official NBB WVV 20/58"),
    ("bud_flri_fixed_2025", "2025", "306642917", "2025 vaste activa 306642917 vs 274491993; tick1390; primary official NBB WVV 21/28"),
    ("bud_flri_iva_2025", "2025", "2203635", "2025 IVA 2203635 vs 2260451; tick1390; primary official NBB WVV 21"),
    ("bud_flri_iva_acq_2025", "2025", "355802", "2025 IVA aanschaf 355802 (8021); tick1390; primary official NBB WVV 6.2.1"),
    ("bud_flri_mva_2025", "2025", "304403990", "2025 MVA 304403990 vs 272196249; tick1390; primary official NBB WVV 22/27"),
    ("bud_flri_buildings_2025", "2025", "1636640", "2025 terreinen/gebouwen 1636640 vs 1260441; tick1390; primary official NBB WVV 22"),
    ("bud_flri_buildings_acq_2025", "2025", "376199", "2025 gebouwen aanschaf 376199 (8161); tick1390; primary official NBB WVV 6.3.1"),
    ("bud_flri_machines_2025", "2025", "235700437", "2025 machines 235700437 vs 211424643; tick1390; primary official NBB WVV 23"),
    ("bud_flri_machines_acq_2025", "2025", "3909709", "2025 machines aanschaf 3909709 (8162); tick1390; primary official NBB WVV 6.3.2"),
    ("bud_flri_furniture_2025", "2025", "575619", "2025 meubilair 575619 vs 238065; tick1390; primary official NBB WVV 24"),
    ("bud_flri_furniture_acq_2025", "2025", "461842", "2025 meubilair aanschaf 461842 (8163); tick1390; primary official NBB WVV 6.3.3"),
    ("bud_flri_cip_2025", "2025", "66491294", "2025 CIP 66491294 vs 59273100; tick1390; primary official NBB WVV 27"),
    ("bud_flri_cip_acq_2025", "2025", "35763574", "2025 CIP aanschaf 35763574 (8166); tick1390; primary official NBB WVV 6.3.6"),
    ("bud_flri_fva_2025", "2025", "35292", "2025 FVA 35292 FSO 1.47pct 518544 A; tick1390; primary official NBB WVV 28"),
    ("bud_flri_fva_part_2025", "2025", "35292", "2025 FVA deelnemingen 35292 FSO 0477.445.084; tick1390; primary official NBB WVV 282"),
    ("bud_flri_current_2025", "2025", "76610244", "2025 vlottend 76610244 vs 70551286; tick1390; primary official NBB WVV 29/58"),
    ("bud_flri_strecv_2025", "2025", "76609348", "2025 ST vorderingen 76609348 vs 70549921; tick1390; primary official NBB WVV 40/41"),
    ("bud_flri_trade_2025", "2025", "4252733", "2025 handelsvorderingen 4252733 vs 172046; tick1390; primary official NBB WVV 40"),
    ("bud_flri_othrecv_2025", "2025", "72356615", "2025 overige ST vorderingen 72356615 vs 70377875; tick1390; primary official NBB WVV 41"),
    ("bud_flri_cash_2025", "2025", "896", "2025 liquide middelen 896 vs 1365; tick1390; primary official NBB WVV 54/58"),
    ("bud_flri_equity_2025", "2025", "260963200", "2025 EV 260963200 vs 245967168; tick1390; primary official NBB WVV 10/15"),
    ("bud_flri_equity_2024", "2024", "245967168", "2024 EV 245967168 comparative; tick1390; primary official NBB WVV 10/15"),
    ("bud_flri_inbreng_2025", "2025", "150450749", "2025 inbreng 150450749 vs 152732098 (RI omzetting -2281349); tick1390; primary official NBB WVV 10/11"),
    ("bud_flri_reserves_2025", "2025", "24514589", "2025 reserves 24514589 vs 23201107; tick1390; primary official NBB WVV 13"),
    ("bud_flri_capsub_2025", "2025", "85997862", "2025 kapitaalsubsidies 85997862 vs 70033962; tick1390; primary official NBB WVV 15"),
    ("bud_flri_debt_2025", "2025", "122289961", "2025 schulden 122289961 vs 99076111; tick1390; primary official NBB WVV 17/49"),
    ("bud_flri_debt_2024", "2024", "99076111", "2024 schulden 99076111 comparative; tick1390; primary official NBB WVV 17/49"),
    ("bud_flri_lt_2025", "2025", "91296811", "2025 LT schulden 91296811 vs 76278065; tick1390; primary official NBB WVV 17"),
    ("bud_flri_ltbank_2025", "2025", "90126811", "2025 LT bank 90126811 vs 75108065; tick1390; primary official NBB WVV 173"),
    ("bud_flri_ltother_2025", "2025", "1170000", "2025 LT overige leningen 1170000; tick1390; primary official NBB WVV 174"),
    ("bud_flri_st_2025", "2025", "29510070", "2025 ST schulden 29510070 vs 21760405; tick1390; primary official NBB WVV 42/48"),
    ("bud_flri_st_due_2025", "2025", "1981254", "2025 LT-due binnen jaar 1981254 vs 1960178; tick1390; primary official NBB WVV 42"),
    ("bud_flri_sttrade_2025", "2025", "5074885", "2025 leveranciers 5074885 JUMP vs 1210; tick1390; primary official NBB WVV 440/4"),
    ("bud_flri_sttax_2025", "2025", "365028", "2025 belastingschulden 365028 vs 237626; tick1390; primary official NBB WVV 450/3"),
    ("bud_flri_stother_2025", "2025", "22088903", "2025 overige ST schulden 22088903 vs 19561390; tick1390; primary official NBB WVV 47/48"),
    ("bud_flri_accrued_2025", "2025", "1483080", "2025 overlopend passief 1483080 (intresten); tick1390; primary official NBB WVV 492/3"),
    ("bud_flri_reldebt_2025", "2025", "78513930", "2025 related-party schulden 78513930 (LT 73352689 / ST 5161241); tick1390; primary official NBB WVV 6.15 9352"),
    ("bud_flri_relrecv_2025", "2025", "74413510", "2025 related-party vorderingen 74413510 vs 70377770; tick1390; primary official NBB WVV 6.15 9292"),
    ("bud_flri_opsinc_2025", "2025", "22206286", "2025 bedrijfsopbrengsten 22206286 vs 19689232; tick1390; primary official NBB WVV 70/76A"),
    ("bud_flri_omzet_2025", "2025", "22112318", "2025 omzet 22112318 vs 19605894; tick1390; primary official NBB WVV 70"),
    ("bud_flri_omzet_2024", "2024", "19605894", "2024 omzet 19605894 comparative; tick1390; primary official NBB WVV 70"),
    ("bud_flri_omzet_rio_2025", "2025", "22112318", "2025 omzet riolering/saneringsbijdrage 22112318; geo empty; tick1390; primary official NBB WVV 6.10"),
    ("bud_flri_othops_2025", "2025", "93968", "2025 andere bedrijfsopbrengsten 93968 vs 83338; 740 empty; tick1390; primary official NBB WVV 74"),
    ("bud_flri_opscost_2025", "2025", "21540075", "2025 bedrijfskosten 21540075 vs 18903622; tick1390; primary official NBB WVV 60/66A"),
    ("bud_flri_diensten_2025", "2025", "10188740", "2025 diensten 10188740 vs 7461366; tick1390; primary official NBB WVV 61"),
    ("bud_flri_diensten_2024", "2024", "7461366", "2024 diensten 7461366 comparative; tick1390; primary official NBB WVV 61"),
    ("bud_flri_deprec_2025", "2025", "8716202", "2025 afschrijvingen 8716202 vs 8252121; tick1390; primary official NBB WVV 630"),
    ("bud_flri_othcost_2025", "2025", "2635134", "2025 andere bedrijfskosten 2635134 vs 3190135; tick1390; primary official NBB WVV 640/8"),
    ("bud_flri_expl_2025", "2025", "666211", "2025 expl +666211 vs +785610; tick1390; primary official NBB WVV 9901"),
    ("bud_flri_expl_2024", "2024", "785610", "2024 expl +785610 comparative; tick1390; primary official NBB WVV 9901"),
    ("bud_flri_fininc_2025", "2025", "3266372", "2025 financiele opbrengsten 3266372 vs 3815308; tick1390; primary official NBB WVV 75/76B"),
    ("bud_flri_fincost_2025", "2025", "2619100", "2025 financiele kosten 2619100 vs 1887581; tick1390; primary official NBB WVV 65/66B"),
    ("bud_flri_pnl_2025", "2025", "1313482", "2025 PnL +1313482 vs +2713338; tick1390; primary official NBB WVV 9904"),
    ("bud_flri_pnl_2024", "2024", "2713338", "2024 PnL +2713338 comparative; tick1390; primary official NBB WVV 9904"),
    ("bud_flri_alloc_2025", "2025", "1313482", "2025 te bestemmen 1313482 all to reserves 6921; 694 empty; tick1390; primary official NBB WVV 9906"),
    ("bud_flri_div_2025", "2025", "0", "2025 dividend 694 empty (all PnL to reserves); tick1390; primary official NBB WVV 694"),
    ("bud_flri_capex_2025", "2025", "42689000", "2025 bruto capex jaarverslag 42689000 (kerncijfers kEUR 42689); tick1390"),
    ("bud_flri_capex_wvv_2025", "2025", "40867126", "2025 WVV bruto aanschaf IVA+MVA 40867126 (8021+8161+8162+8163+8166); tick1390; primary official NBB WVV 6.2/6.3"),
    ("bud_flri_comm_2025", "2025", "7093", "2025 commissaris 9505 7093; tick1390; primary official NBB WVV 9505"),
    ("bud_flri_comm_extra_2025", "2025", "1650", "2025 commissaris extra controle 95061 1650 + tax 95082 629; tick1390; primary official NBB WVV 95061"),
    ("bud_flri_board_2025", "2025", "29126", "2025 bestuurders 9503 29126; tick1390; primary official NBB WVV 9503"),
]


def write_progress(counts):
    path = DATA / "progress_every_10_ticks.md"
    old = path.read_text(encoding="utf-8")
    marker = "## Snapshot at **tick 1380**"
    idx = old.find(marker)
    if idx < 0:
        raise SystemExit("progress file missing tick 1380 marker")
    header = old[:idx]
    rest = old[idx:]
    snap = f"""## Snapshot at **tick 1390** (2026-08-19)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1381-1390 leftover IGS: **INTERZA** · **INTERGEM** · **Imewo** · **Fluvius Kempen** · **Fluvius West** · **Fluvius Antwerpen** · **Fluvius Halle-Vilvoorde** · **Fluvius Limburg** · **Fluvius Zenne-Dijle** · **Fluvius Riobra** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1381-1390 is VL residual dual L5 leftover Fluvius/IGS (not near-complete of 348bn):** **Fluvius West** assets **3.378bn** · **Fluvius Limburg** assets **3.255bn** · **Imewo** assets **3.069bn** · **Fluvius Zenne-Dijle** assets **2.522bn** · **Fluvius Antwerpen** assets **2.456bn** · **Fluvius Halle-Vilvoorde** assets **1.355bn** · **INTERGEM** assets **1.295bn** · **Fluvius Kempen** assets **1.159bn** · **Fluvius Riobra** assets **383.25m** omzet **22.11m** diensten **10.19m** · **INTERZA** assets **7.44m** · prior leftover IGS/EVA INCOVO/ISVAG/De Nekker/MIROM/IVAGO stack retained |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM/portfolio/waste-water-streek/klimaat-holding/energy-DSO shells** (**NEW Fluvius Riobra** assets **EUR383.25m** omzet **EUR22.11m** diensten **EUR10.19m** debt **EUR122.29m** · **Fluvius Zenne-Dijle** assets **EUR2.522bn** omzet **EUR354.23m** diensten **EUR124.68m** · **Fluvius Limburg** assets **EUR3.255bn** · **Fluvius Halle-Vilvoorde** assets **EUR1.355bn** · **Fluvius Antwerpen** assets **EUR2.456bn** · **Fluvius West** assets **EUR3.378bn** · **Fluvius Kempen** assets **EUR1.159bn** · **Imewo** assets **EUR3.069bn** · **INTERGEM** assets **EUR1.295bn** · **INTERZA** assets **EUR7.44m** · prior leftover IGS/EVA INCOVO/ISVAG/De Nekker/MIROM/IVAGO/Veneco/IGEMO/Haviland/IMOG/IOK/Leiedal/Interleuven/Nuhma stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market.

### Inventory (tick 1390)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {counts['budgets']} |
| commitments.csv | {counts['commitments']} |
| leaderboard.csv | {counts['leaderboard']} |
| entities.csv | {counts['entities']} |
| sources.csv | {counts['sources']} |
| FOI ready | {counts['foi_ready']} |
| FOI answered | {counts['foi_answered']} |
| FOI partial | {counts['foi_partial']} |
| FOI total rows | {counts['foi_total']} |
| research_queue open | rq_116 deferred + rq_1391 hole-fill after progress |

### What improved since tick 1380

- **VL residual dual JR2025 leftover Fluvius/IGS (tick1381-1389):** **Fluvius West** assets **3.378bn** · **Fluvius Limburg** assets **3.255bn** · **Imewo** assets **3.069bn** · **Fluvius Zenne-Dijle** assets **2.522bn** · **Fluvius Antwerpen** assets **2.456bn** · **Fluvius Halle-Vilvoorde** assets **1.355bn** · **INTERGEM** assets **1.295bn** · **Fluvius Kempen** assets **1.159bn** · **INTERZA** assets **7.44m** — no invented euros.
- **NEW (tick1390):** **Fluvius Riobra** (KBO 0878.051.819) leftover opdrachthoudende vereniging / IGS riolering of 25 Vlaams-Brabant municipalities. Official NBB WVV VOL-inb deposit **2026-00205662** PDF (1.79MB / 73p; AV 23.06.2026; created 27.06.2026). Assets **383.253.161** · omzet **22.112.318** (6.10 riolering; geo empty) · diensten **10.188.740** · debt **122.289.961** · related recv **74.413.510** · PnL **+1.313.482** · dividend 694 empty · 0 VTE. FOI ready. Every-10 progress refresh from on-disk CSVs.
- **Dual map themes:** **leftover Fluvius energy DSO + leftover Fluvius sewerage IGS shells** (West 3.378bn / Limburg 3.255bn / Imewo 3.069bn / Zenne-Dijle 2.522bn / Antwerpen 2.456bn / Halle-Vilvoorde 1.355bn / INTERGEM 1.295bn / Kempen 1.159bn / Riobra 383.25m / INTERZA 7.44m) · prior leftover IGS waste/streek + Nuhma stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---
"""
    path.write_text(header + snap + rest, encoding="utf-8")
    print("progress ok")


def write_waste_top10(counts):
    path = DATA / "doge_waste_top10_current.md"
    old = path.read_text(encoding="utf-8")
    # keep ranking table body from 1380; refresh header + change note + add Riobra to just-outside
    # rewrite header and first stock-filter/change paragraphs by prefix replacement
    header = f"""# DOGE waste ranking — current top 10

**As-of:** tick **1390** (2026-08-19) · **{counts['leaderboard']}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**  
**Formula:** `0.55×cost_score + 0.35×absurdity + 0.10×(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

"""
    # keep the existing top10 table starting at "| # | ID |"
    tstart = old.find("| # | ID |")
    if tstart < 0:
        raise SystemExit("waste top10 table missing")
    # find change-vs paragraph to replace
    cstart = old.find("**Change vs tick 1370:**")
    if cstart < 0:
        raise SystemExit("waste change paragraph missing")
    table = old[tstart:cstart]
    # keep just-outside from old after replacing as-of INCOVO line with newer duals prepended
    jstart = old.find("### Just outside top 10")
    if jstart < 0:
        raise SystemExit("just outside missing")
    rest = old[jstart:]
    # prepend new just-outside rows after the table header of just-outside
    change = (
        "**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  \n"
        "**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  \n"
        "**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **WE consol €6.38bn** · **SOFICO €3.02bn** · **university/city balance sheets** · **AGB/zorg dual AFM NEG + debt + leasing/city-loan/DBFM/IGS energy-DSO/sewerage shells** (**NEW Fluvius Riobra** assets **€383.25m** omzet **€22.11m** diensten **€10.19m** debt **€122.29m** · **Fluvius Zenne-Dijle** assets **€2.522bn** · **Fluvius Limburg** assets **€3.255bn** · **Fluvius Halle-Vilvoorde** assets **€1.355bn** · **Fluvius Antwerpen** assets **€2.456bn** · **Fluvius West** assets **€3.378bn** · **Fluvius Kempen** assets **€1.159bn** · **Imewo** assets **€3.069bn** · **INTERGEM** assets **€1.295bn** · **INTERZA** assets **€7.44m** · prior leftover IGS/EVA INCOVO/ISVAG/De Nekker/MIROM/IVAGO/Veneco/IGEMO/Haviland/IMOG/IOK/Leiedal/Interleuven/Nuhma stack retained) · **LUWA PPP €590m** · private gambling stakes **€31.5bn** market.\n\n"
        "**Change vs tick 1380:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). **Major NEW residual 1381–1390 (off pure top10 / dual):** **Fluvius West** assets **EUR3.378bn** · **Fluvius Limburg** assets **EUR3.255bn** · **Imewo** assets **EUR3.069bn** · **Fluvius Zenne-Dijle** assets **EUR2.522bn** · **Fluvius Antwerpen** assets **EUR2.456bn** · **Fluvius Halle-Vilvoorde** assets **EUR1.355bn** · **INTERGEM** assets **EUR1.295bn** · **Fluvius Kempen** assets **EUR1.159bn** · **Fluvius Riobra** assets **EUR383.25m** omzet **EUR22.11m** diensten **EUR10.19m** debt **EUR122.29m** · **INTERZA** assets **EUR7.44m**. Gain is **leftover Fluvius energy DSO holdings + leftover Fluvius sewerage IGS + leftover INTERZA waste IGS**. Count only NEW since 1380: INTERZA 1381 + Fluvius stack 1382–1389 + Riobra 1390. **Prior 1371–1380 retained:** IVAGO 78.39m · Veneco 51.98m · ISVAG 42.72m · MIROM Roeselare 37.44m · IGEMO 25.44m · MIWA 19.60m · MIROM Menen 11.71m · IVOO 10.74m · INCOVO 9.40m · De Nekker 0.75m.\n\n"
    )
    # inject new just-outside row after header of that table
    jo_header_end = rest.find("| — | `lb_metro3_overrun_477pct`")
    if jo_header_end < 0:
        raise SystemExit("metro3 row missing")
    new_rows = (
        "| — | `lb_flri_omzet_22_11m_diensten_10_19m_debt_122_29m` | **383.25 m stock** | **~7.3 dual** | **NEW 1390** Fluvius Riobra leftover IGS omzet 22.11m / diensten 10.19m / debt 122.29m |\n"
        "| — | `lb_flzd_omzet_354_23m_diensten_124_68m_debt_1_97bn` | **2.522 bn stock** | **~7.3 dual** | 1389 Fluvius Zenne-Dijle leftover energy IGS omzet 354.23m / diensten 124.68m |\n"
        "| — | `lb_flli_omzet_434_32m_diensten_163_67m_debt_1_55bn` | **3.255 bn stock** | **~7.3 dual** | 1388 Fluvius Limburg leftover energy IGS |\n"
        "| — | `lb_flhv_omzet_238_16m_diensten_76_14m` | **1.355 bn stock** | **~7.2 dual** | 1387 Fluvius Halle-Vilvoorde leftover energy IGS |\n"
        "| — | `lb_flan_omzet_430_93m_diensten_165_12m` | **2.456 bn stock** | **~7.3 dual** | 1386 Fluvius Antwerpen leftover energy IGS |\n"
        "| — | `lb_flww_omzet_541_75m_diensten_173_84m` | **3.378 bn stock** | **~7.3 dual** | 1385 Fluvius West leftover energy IGS |\n"
        "| — | `lb_flkp_omzet_221_58m_diensten_63_61m` | **1.159 bn stock** | **~7.2 dual** | 1384 Fluvius Kempen leftover energy IGS |\n"
        "| — | `lb_imew_omzet_544_91m_diensten_185_22m` | **3.069 bn stock** | **~7.3 dual** | 1383 Imewo leftover energy IGS |\n"
        "| — | `lb_intg_omzet_242_74m_diensten_88_70m` | **1.295 bn stock** | **~7.2 dual** | 1382 INTERGEM leftover energy IGS |\n"
        "| — | `lb_inza_omzet_4_54m_subs_5_72m_diensten_4_92m` | **7.44 m stock** | **~6.2 dual** | 1381 INTERZA leftover IGS omzet 4.54m / subs 5.72m |\n"
    )
    rest2 = rest[:jo_header_end] + new_rows + rest[jo_header_end:]
    # strip old GIP honesty / stock filter / change that sat between table and just-outside
    # table already includes GIP honesty? In 1380 file, GIP honesty is BETWEEN table and Change vs.
    # We already sliced table as tstart:cstart which includes GIP honesty + stock filter.
    # Rebuild cleanly: header + table up to GIP honesty? Let's take only the ranking table.
    tend = old.find("**GIP honesty:**")
    ranking = old[tstart:tend]
    path.write_text(header + ranking + change + rest2, encoding="utf-8")
    print("waste top10 ok")


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "Fluvius Riobra (voorheen Riobra) jaarrekening boekjaar 2025 (official NBB WVV VOL-inb deposit 2026-00205662; AV 23.06.2026)",
                "url": SRC_URL,
                "publisher": "Fluvius Riobra / NBB WVV deposit",
                "accessed_date": "2026-08-19",
                "source_class": "budget",
                "notes": (
                    "tick1390; official NBB VOL-inb PDF 1.79MB 73p deposit 2026-00205662 header 24.06.2026 created 27.06.2026; "
                    "leftover IGS riolering of 25 Vlaams-Brabant municipalities; naam Fluvius Riobra since 01.01.2026; "
                    "euros extracted from the deposit PDF itself; NBB consult 403/SPA this box; "
                    "Belscope/Companyweb extracted tables not used; Staatsbladmonitor table euros not used (rounded scrape); "
                    "commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / "
                    "Paul Eelen + Line Vyvey oordeel zonder voorbehoud signed 20.03.2026; "
                    "VOL-inb 6.1/6.2.2-6.2.5/6.3.5/6.4.1/6.4.3/6.5.2/6.6/6.7.2/6.8/6.12/6.17/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62 empty; 694 empty"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Fluvius Riobra official governance + jaarverslag 2025 (leftover IGS riolering; voorheen Riobra; 25 vennoten)",
                "url": SRC2_URL,
                "publisher": "Fluvius / Fluvius Riobra",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1390; leftover IGS of 25 Vlaams-Brabant municipalities; "
                    "over.fluvius.be lists activiteitenverslagen + JR2025 https://over.fluvius.be/sites/fluvius/files/2026-06/riobra-jaarverslag-2025.pdf; "
                    "statutory 2025 balans is the NBB CDN deposit; naamwijziging Riobra -> Fluvius Riobra 01.01.2026"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO Fluvius Riobra 0878.051.819",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1390; KBO 0878.051.819 Actief / normale toestand since 07.12.2005; "
                    "statutaire naam Fluvius Riobra since 01.01.2026; "
                    "Opdrachthoudende vereniging (Vlaams Gewest) since 25.11.2005; "
                    "zetel Diestsesteenweg 126 3210 Lubbeek since 01.01.2026; 0 VE; "
                    "no KBO email/web/tel; btw since 01.01.2006; NACE 37.000 Afvalwaterafvoer; "
                    "aanbestedende overheid since 25.11.2005"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Fluvius Riobra FOI channel / official governance + secretariaat (KBO no email)",
                "url": SRC4_URL,
                "publisher": "Fluvius Riobra",
                "accessed_date": "2026-08-19",
                "source_class": "official_register",
                "notes": (
                    "tick1390; KBO no email/web/tel; zetel Diestsesteenweg 126 3210 Lubbeek; "
                    "secretariaat Brusselsesteenweg 199 9090 Merelbeke-Melle; "
                    "no dedicated openbaarheid mailbox found on official pages this tick"
                ),
            },
        ],
    )
    print("sources", n)

    n = append_rows(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENT,
                "name_nl": "Fluvius Riobra (voorheen Riobra; leftover IGS riolering Vlaams-Brabant)",
                "name_fr": "Fluvius Riobra (ex-Riobra; IGS residuel assainissement Brabant flamand)",
                "name_en": "Fluvius Riobra leftover IGS sewerage (formerly Riobra)",
                "level": "other",
                "parent_id": "sec_flanders",
                "community_language": "nl",
                "website": SRC2_URL,
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1390 leftover residual IGS riolering of 25 Vlaams-Brabant municipalities; "
                    "KBO 0878.051.819 Actief since 07.12.2005; naam Fluvius Riobra since 01.01.2026; official NBB WVV VOL-inb PDF downloads; "
                    "sourced euros assets 383253161 omzet 22112318 diensten 10188740 debt 122289961 pnl 1313482 equity 260963200 dividend 0; "
                    "FOI ready omzet geo empty / 94.0k 74 empty 740 / 10.19m 61 / 122.29m debt / 74.41m related recv; "
                    "distinct from already-mined Fluvius EG group entity fluvius and Zenne-Dijle 1389 / Limburg 1388 / Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382"
                ),
            },
        ],
    )
    print("entities", n)

    n = append_rows(
        DATA / "budgets.csv",
        [
            {
                "budget_id": bid,
                "entity_id": ENT,
                "year": year,
                "amount_eur": amt,
                "amount_min_eur": "",
                "amount_max_eur": "",
                "basis": "executed",
                "source_id": SRC,
                "confidence": "strong",
                "notes": notes,
            }
            for bid, year, amt, notes in BUDGETS
        ],
    )
    print("budgets", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": COMM,
                "title": "Fluvius Riobra JR2025 leftover IGS dual (assets 383.25m / omzet 22.11m / diensten 10.19m / debt 122.29m / dividend 0)",
                "entity_id": ENT,
                "beneficiary": "Fluvius Riobra / " + VENNOTEN,
                "legal_basis": "WVV OV; Decreet Lokaal Bestuur; NBB neerlegging",
                "decision_date": "2026-06-23",
                "start_year": "2005",
                "end_year": "",
                "total_envelope_eur": "383253161",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Local leftover IGS map VL sewerage — 22.11m omzet (geo empty) / 10.19m diensten / 122.29m debt / 0 dividend",
                "cut_option": "Publish unpublished omzet geo + 94.0k 74 + 10.19m 61 FSO pass-through + 122.29m debt counterparties + 74.41m related ST vorderingen; do not keep sewerage IGS as dual unpublished vehicle",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">JR2025_L5",
                "notes": "tick1390; assets 383253161 omzet 22112318 diensten 10188740 debt 122289961 pnl 1313482 equity 260963200 dividend 0; FOI ready not sent; not TE-additive of 348bn; double_count vs Fluvius EG possible",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": LB,
                "name": "Fluvius Riobra JR2025 leftover IGS: assets 383.25m / omzet 22.11m / diensten 10.19m / debt 122.29m / dividend 0 / 0 VTE",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">JR2025_L5",
                "annual_cost_eur": "10188740",
                "total_cost_eur": "383253161",
                "tco_notes": (
                    "Leftover dual IGS riolering of 25 Vlaams-Brabant municipalities (voorheen Riobra): "
                    "assets 383.25m / equity 260.96m / pnl +1.31m / omzet 22.11m (geo empty) / "
                    "diensten 10.19m / 0 VTE / debt 122.29m (related 78.51m) / dividend 0 / cash 896; "
                    "official NBB WVV live; do not treat 383.25m as TE-additive of 348bn; double_count vs Fluvius EG possible"
                ),
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "Fluvius Riobra / " + VENNOTEN,
                "stated_goal": "Local leftover IGS map VL sewerage — JR2025 live; dual omzet-geo/diensten/debt FOI",
                "measured_outcome": "Official NBB WVV 2026-08-19: assets 383.25m / omzet 22.11m / diensten 10.19m / debt 122.29m / dividend 0 / pnl +1.31m / 0 VTE",
                "absurdity_score": "7.0",
                "cost_score": "7.5",
                "difficulty": "3.0",
                "priority_index": "7.3",
                "cut_proposal": "Publish unpublished omzet geo + 94.0k 74 + 10.19m 61 FSO pass-through + 122.29m debt counterparties + 74.41m related ST vorderingen; do not keep sewerage IGS as dual unpublished vehicle",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1390; leftover IGS of 25 Vlaams-Brabant municipalities; FOI ready not sent; not TE-additive of 348bn; distinct from Fluvius EG and Zenne-Dijle 1389 / Limburg 1388 / Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382",
            }
        ],
    )
    print("leaderboard", n)

    n = append_rows(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": HIER + ">JR2025_L5",
                "entity_id": ENT,
                "what_is_missing": (
                    "omzet 22112318 vs 19605894 (WVV 70; 6.10 category riolering/saneringsbijdrage 22112318; geo empty) per vennoot/tariefstroom unpublished "
                    "+ andere bedrijfsopbrengsten 93968 (WVV 74; 740 empty) "
                    "+ diensten 10188740 vs 7461366 (WVV 61; no split) + FSO pass-through (pers 62/9087 empty / 0 VTE) "
                    "+ schulden 122289961 (LT bank 90126811; related-party 78513930) counterparties/rente unpublished "
                    "+ related-party ST vorderingen 74413510 vs 70377770 unpublished "
                    "+ FVA deelnemingen 35292 FSO 1.47pct unpublished "
                    "+ dividend 694 empty (all 1313482 to reserves) per vennoot unpublished "
                    "+ cash 896 vs debt 122.29m + VOL-inb 6.1/6.2.2-6.2.5/6.3.5/6.4.1/6.6/6.7.2/6.8/6.12/6.17/6.18/9 not filed"
                ),
                "why_it_matters": (
                    "Leftover IGS OV sewerage of 25 mined Vlaams-Brabant municipalities "
                    "(same leftover-IGS Fluvius seam as Zenne-Dijle 1389 / Limburg 1388 / Halle-Vilvoorde 1387 / Antwerpen 1386 / West 1385 / Kempen 1384 / Imewo 1383 / INTERGEM 1382; distinct from Fluvius EG and from energy DSO holdings): "
                    "383.25m assets / 22.11m omzet / 10.19m diensten / 122.29m debt / 0 dividend / "
                    "0 VTE / FSO shell "
                    "is a dual opacity residual, not TE-additive of 348bn."
                ),
                "priority": "8",
                "recipient_body": "Fluvius Riobra / Raad van Bestuur / Peter Kaspers / Jean Pierre Taverniers / 25 vennoten",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-19",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": COMM,
                "linked_leaderboard_id": LB,
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "tick1390 leftover IGS OV sewerage of 25 Vlaams-Brabant municipalities after honest hunt; "
                    "live JR2025 official NBB WVV VOL-inb PDF now extracted (1.79MB 73p deposit 2026-00205662). "
                    "Fluvius Zenne-Dijle already mined 1389 — skipped. Fluvius Limburg already mined 1388 — skipped. "
                    "Fluvius Halle-Vilvoorde already mined 1387 — skipped. Fluvius Antwerpen already mined 1386 — skipped. "
                    "Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. "
                    "Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. "
                    "Leftover AGB/zorg/EVA/APB of mined cities next if a 2025 PDF downloads. "
                    "Dommelhof leftover Limburg EVA 0777.495.085 not re-probed once live Riobra extracted. "
                    "Otary RS Nuhma-adjacent fallback not taken. "
                    "NBB consult skipped. Belscope/Companyweb euros not used. ready not sent; every-10"
                ),
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1390",
        "title": "Fluvius Riobra JR2025 leftover dual residual + every-10",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: EVERY-10 progress refresh from on-disk CSVs + Fluvius Riobra leftover IGS sewerage of 25 Vlaams-Brabant municipalities after honest hunt; "
            "KBO 0878.051.819 Actief; live JR2025 official NBB WVV VOL-inb PDF (1.79MB 73p deposit 2026-00205662; commissaris EY); "
            "sourced euros assets 383253161 / omzet 22112318 / diensten 10188740 / debt 122289961 / pnl 1313482 / dividend 0; "
            "FOI ready omzet geo empty / 94.0k 74 / 10.19m 61 / 122.29m debt / 74.41m related recv"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-19T05:30:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1390 Fluvius Riobra leftover IGS sewerage residual + every-10; KBO 0878.051.819; "
            "live JR2025 NBB WVV PDF; sourced euros; FOI ready not sent; next rq_1391 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1391",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA/IGS not yet mined "
            "(prior 1255-1390 done including Fluvius Riobra 1390 leftover sewerage IGS live NBB WVV + every-10 / "
            "Fluvius Zenne-Dijle 1389 leftover energy IGS live NBB WVV / "
            "Fluvius Limburg 1388 leftover energy IGS live NBB WVV / "
            "Fluvius Halle-Vilvoorde 1387 leftover energy IGS live NBB WVV / "
            "Fluvius Antwerpen 1386 leftover energy IGS live NBB WVV / "
            "Fluvius West 1385 leftover energy IGS live NBB WVV / "
            "Fluvius Kempen 1384 leftover energy IGS live NBB WVV / "
            "Fluvius Imewo 1383 leftover energy IGS live NBB WVV / "
            "INTERGEM / Fluvius Midden-Vlaanderen 1382 leftover energy IGS live NBB WVV); "
            "leftover AGB/zorg/EVA/APB of mined cities — take if a 2025 PDF actually downloads; "
            "Kunstenwerkplaats Dommelhof leftover Limburg EVA KBO 0777.495.085 — take only if a JR2025 PDF now downloads; "
            "Otary RS / Rematics / Sunfin leftover Nuhma daughters — take only if leftover AGB/zorg/EVA/IGS/APB outside Nuhma first; "
            "skip already-mined Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Fluvius Imewo 1383 / INTERGEM 1382 / INTERZA 1381 / INCOVO 1380 / ISVAG 1379 / De Nekker 1378 / MIROM Menen 1377 / MIROM Roeselare 1376 / IVAGO 1375 / MIWA 1374 / IVOO 1373 / IGEMO 1372 / Veneco 1371 / Haviland 1370 / IMOG 1369 / IOK 1368 / Leiedal 1367 / Interleuven 1366 / s-Lim DV 1365 / Herkenrode RE 1364 / MyCSN 1363 / s-Lim CV 1362 / Nuhmeris 1361 / ECO2050 1360 / Nubema 1359 / NUHMA DC 1358 / EcoWerf 1357 / Nuhma cv 1356 / NUHMA AC 1355 / Bionerga 1354 / Limburg.net 1353; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1390 after Fluvius Riobra leftover sewerage IGS live NBB WVV + every-10; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1390", rq_new, rq_spawn)
    print("research_queue 1390", found, "spawned_1391", spawned)

    with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "state_id",
                "mode",
                "current_sprint",
                "last_tick_utc",
                "last_unit_id",
                "ticks_completed",
                "paused",
                "notes",
            ],
            lineterminator="\r\n",
        )
        w.writeheader()
        w.writerow(
            {
                "state_id": "main",
                "mode": "continuous",
                "current_sprint": "hole_fill",
                "last_tick_utc": UTC,
                "last_unit_id": "rq_1390",
                "ticks_completed": "1390",
                "paused": "no",
                "notes": (
                    "tick1390 Fluvius Riobra leftover IGS sewerage residual + every-10; KBO 0878.051.819; "
                    "live JR2025 NBB WVV PDF; sourced euros assets 383253161 omzet 22112318 diensten 10188740 debt 122289961 pnl 1313482 equity 260963200 dividend 0; "
                    "FOI ready omzet geo empty/94.0k 74/10.19m 61/122.29m debt/74.41m related recv; next rq_1391 residual dual L5 VL; continuous hole_fill"
                ),
            }
        )
    print("loop_state ok")

    foi_c = foi_status_counts()
    counts = {
        "budgets": count_csv_rows(DATA / "budgets.csv"),
        "commitments": count_csv_rows(DATA / "commitments.csv"),
        "leaderboard": count_csv_rows(DATA / "leaderboard.csv"),
        "entities": count_csv_rows(DATA / "entities.csv"),
        "sources": count_csv_rows(DATA / "sources.csv"),
        "foi_ready": foi_c.get("ready", 0),
        "foi_answered": foi_c.get("answered", 0),
        "foi_partial": foi_c.get("partial", 0),
        "foi_total": sum(v for k, v in foi_c.items() if k != "_other") + foi_c.get("_other", 0),
    }
    print("inventory", counts)
    write_progress(counts)
    write_waste_top10(counts)

    log = ROOT / "loop_log.md"
    entry = (
        f"### Tick 1390 - 2026-08-19 - rq_1390 Fluvius Riobra dual residual leftover + every-10\n"
        f"- Unit: Fluvius Riobra (voorheen Riobra tot 31.12.2025; leftover IGS opdrachthoudende vereniging / riolering + afvalwaterafvoer of 25 mined Vlaams-Brabant municipalities; werkmaatschappij Fluvius System Operator) after residual dual hunt (KBO **0878.051.819**; official over.fluvius.be has activiteitenverslagen/governance + jaarverslag 2025; live NBB WVV VOL-inb deposit **2026-00205662** PDF 1.79MB / 73p; AV **23.06.2026**; header **24.06.2026**; created **27.06.2026**; commissaris EY Bedrijfsrevisoren BV B00160 / 0446.334.711 / Paul Eelen A02213 + Line Vyvey A02501 signed 20.03.2026 oordeel zonder voorbehoud assets 383.253.161 / PnL +1.313.482). Leftover Fluvius sewerage IGS whose official NBB deposit now yields a downloadable JR2025 PDF with euros (prefer live statutory PDF over another unpublished FOI; preferred leftover Fluvius Riobra this tick). Distinct from already-mined Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / Fluvius EG group-level (entity fluvius). First confirmed not already mined: no Fluvius Riobra / 0878.051.819 JR2025 extract in entities/sources/leaderboard. KBO Actief / normale toestand since **07.12.2005**; statutaire naam Fluvius Riobra since 01.01.2026; Opdrachthoudende vereniging (Vlaams Gewest) since 25.11.2005; zetel Diestsesteenweg 126 3210 Lubbeek since 01.01.2026; **0 VE**; KBO no email/web/tel; official site https://over.fluvius.be/; btw since 01.01.2006; NACE 37.000. Voorzitter Peter Kaspers since 12.03.2025; ondervoorzitter Jean Pierre Taverniers since 12.03.2025; commissaris EY 28.06.2023-12.06.2026. Hunt leftover Fluvius Riobra first: Riobra statutory CDN live this tick (HTTP 200 / 1788932 / 73p) — taken. Fluvius Zenne-Dijle already mined 1389 — skipped. Fluvius Limburg already mined 1388 — skipped. Fluvius Halle-Vilvoorde already mined 1387 — skipped. Fluvius Antwerpen already mined 1386 — skipped. Fluvius West already mined 1385 — skipped. Fluvius Kempen already mined 1384 — skipped. Imewo already mined 1383 — skipped. INTERGEM already mined 1382 — skipped. Dommelhof leftover Limburg EVA KBO 0777.495.085 not re-probed once live Riobra extracted. Otary RS Nuhma-adjacent fallback CDN 2026-00254280 live — not taken. NBB consult skipped (403/SPA); euros extracted from the official VOL-inb deposit PDF itself. Belscope/Companyweb euros not used. Staatsbladmonitor table euros not used (rounded scrape). Every-10 (last 1380 INCOVO).\n"
        f"- EUR strong (primary official WVV VOL-inb + commissaris oordeel zonder voorbehoud; VOL-inb 6.1/6.2.2-6.2.5/6.3.5/6.4.1/6.4.3/6.5.2/6.6/6.7.2/6.8/6.12/6.17/6.18.1-6.18.2/9/10/12-15 not filed; omzet 6.10 category filled / geo empty; 740 empty; 62/9087 empty; 694 empty): assets **383.253.161** (was 345.043.278); fixed **306.642.917** / MVA **304.403.990** (gebouwen **1.636.640**; machines **235.700.437**; meubilair **575.619**; CIP **66.491.294** aanschaf **35.763.574**); IVA 2.203.635; FVA **35.292** (FSO 1,47% / 518.544 A); current **76.610.244**; cash **896**; ST recv **76.609.348** (trade 4.252.733 / other 72.356.615); equity **260.963.200**; kapitaalsubsidies **85.997.862**; schulden **122.289.961** (LT **91.296.811** waarvan bank **90.126.811**; ST **29.510.070** waarvan leveranciers **5.074.885 JUMP**; related-party FSO-seam **78.513.930**); omzet **22.112.318** vs 19.605.894 (all riolering/saneringsbijdrage; geo empty); othops **93.968** (740 empty); diensten **10.188.740** vs 7.461.366; pers **empty / 0 VTE**; afschr 8.716.202; expl **+666.211** vs +785.610; fin opbr 3.266.372; fin kosten 2.619.100; tax 0; PnL **+1.313.482** vs +2.713.338 all to reserves; dividend **0** (694 empty); bruto capex jaarverslag **42.689.000**; WVV aanschaf 40.867.126; commissaris 7.093 + extra 1.650; bestuurders 29.126. Jaarverslag same Fluvius glossy: 25 vennoten; 5.895.644 aandelen; investeringsplan ~40,5m/jr.\n"
        f"- CSVs: sources+4/entities+1/budgets+62/commitments+1/leaderboard+1 + FOI ready `gap_flri_omzet_22_11m_diensten_10_19m_debt_122_29m_l5` (not sent); rq_1390=done; spawn rq_1391; ticks=1390.\n"
        f"- Coverage: residual dual L5 (Fluvius Riobra leftover sewerage IGS live WVV). Does **not** move L5 near-complete of EUR 347.956 bn TE. Taxex/FFS remain off-TE. Double_count vs Fluvius EG possible.\n"
        f"- Every-10 progress (recount from disk after this tick writes): **A 100** / **B 100** / **C ~99** / **D ~74-88** (generous; not near-complete of 348bn) / **E ready {counts['foi_ready']}** (answered {counts['foi_answered']} / partial {counts['foi_partial']} / total {counts['foi_total']}). Inventory: budgets {counts['budgets']} · commitments {counts['commitments']} · leaderboard {counts['leaderboard']} · entities {counts['entities']} · sources {counts['sources']}. Waste top10 **stable** (GIP #1; fossil / cars / cheque / reporté #2-10). Dual off-top10 NEW since 1380: INTERZA 7.44m · INTERGEM 1.295bn · Imewo 3.069bn · Fluvius Kempen 1.159bn · Fluvius West 3.378bn · Fluvius Antwerpen 2.456bn · Fluvius Halle-Vilvoorde 1.355bn · Fluvius Limburg 3.255bn · Fluvius Zenne-Dijle 2.522bn · **Fluvius Riobra 383.25m**. Progress files refreshed: `progress_every_10_ticks.md` + `doge_waste_top10_current.md`.\n"
        f"- Next: rq_1391 residual dual L5 VL JR2025 hole_fill (prefer leftover AGB/zorg/EVA/APB of mined cities if a 2025 PDF actually downloads; leftover Dommelhof KBO 0777.495.085 only if a JR2025 PDF now downloads; leftover Nuhma daughters Otary RS only after leftover IGS/EVA/AGB; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined Fluvius Riobra 1390 / Fluvius Zenne-Dijle 1389 / Fluvius Limburg 1388 / Fluvius Halle-Vilvoorde 1387 / Fluvius Antwerpen 1386 / Fluvius West 1385 / Fluvius Kempen 1384 / Imewo 1383 / INTERGEM 1382 / INTERZA 1381).\n"
    )
    with log.open("a", encoding="utf-8") as f:
        f.write(entry)
    print("loop_log ok")
    print("tick1390 write done")


if __name__ == "__main__":
    main()
