# -*- coding: utf-8 -*-
"""Tick 1320 — every-10 progress FIRST, then APB KampC JR2025 leftover sister APB residual.
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

TICK = "1320"
UTC = "2026-08-17T18:35:00Z"
ENT = "apb_kmpc"
HIER = "Vlaanderen>Provincies>Antwerpen>APB>KampC"
GAP = "gap_kmpc_st_recv_3_06m_werksub_j5t2_1_25m_l5"
SRC = "src_kmpc_jr2025_pdf"
SRC2 = "src_kmpc_jaarverslag_2025"
SRC3 = "src_kbo_kmpc_0541415101"
SRC4 = "src_kmpc_foi_page"
SRC_URL = "https://assets.foleon.com/eu-central-1/de-uploads-7e3kk3/20500/2025-apb_kmpc.9a13977d877c.pdf"
SRC2_URL = "https://publicaties.provincieantwerpen.be/kamp-c-jaarverslag-2025/in-cijfers"
SRC3_URL = "https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0541415101"
SRC4_URL = "https://www.provincieantwerpen.be/nl/provinciebestuur/werking-provincie/provinciegriffier/inzagerecht"
FOI_EMAIL = "openbaarheid@provincieantwerpen.be"
FOI_POSTAL = "Koningin Elisabethlei 22 2018 Antwerpen"
DRAFT = "docs/doge/foi/drafts/gap_kmpc_st_recv_3_06m_werksub_j5t2_1_25m_l5.md"


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


def count_csv_rows(path: Path) -> int:
    with path.open(encoding="utf-8", errors="replace", newline="") as f:
        n = sum(1 for _ in f)
    return max(0, n - 1)


def foi_status_counts() -> Counter:
    with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return Counter((r.get("status") or "").strip() for r in rows)


def write_progress(counts: dict) -> None:
    prog = DATA / "progress_every_10_ticks.md"
    text = prog.read_text(encoding="utf-8")
    marker = "## Snapshot at **tick 1310** (2026-08-17)"
    if marker not in text:
        raise SystemExit("progress file missing tick 1310 marker")
    snap = f"""## Snapshot at **tick 1320** (2026-08-17)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 1311-1320: AGB Maaseik · AGBIM · AGB Merchtem FOI · AGB Sport Hulshout FOI · Lievegem FOI-TLS · Ranst FOI · APB PSES · APB GKC · APB Havencentrum · **APB KampC** |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 1311-1320 is VL residual dual L5 (not near-complete of 348bn):** **APB PSES** assets **186.52m** ST recv **165.31m** BBR **−1.29m** · **APB KampC** assets **5.93m** cash **2.65m** ST recv **3.06m** BBR **+2.39m** · **AGBIM** CCAO **8.91m** · **AGB Maaseik** fin debt **1.60m** AFM **−0.67m** · **APB GKC** assets **2.67m** · **APB Havencentrum** assets **0.97m** · prior Edegem / Beerse / VERA / Kortenaken stack retained |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_total']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB dual debt/AFM NEG + leasing/city-loan/erfpacht/DBFM shells** (**NEW APB KampC** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR3.06m** BBR **+EUR2.39m** J5/T2 werksub gap **EUR1.25m** · **APB PSES** assets **EUR186.52m** ST recv **EUR165.31m** BBR **−EUR1.29m** · **APB GKC** assets **EUR2.67m** cash **EUR2.11m** · **APB Havencentrum** assets **EUR0.97m** Havenwereld **EUR0.40m** · **AGBIM** CCAO **EUR8.91m** · **AGB Maaseik** fin debt **EUR1.60m** AFM **−EUR0.67m** · prior **APB VERA** fin debt **EUR1.72m** equity **−EUR1.64m** straight loan **EUR1.10m** · **Edegem** fin debt **EUR14.05m** pension **EUR23.40m** · **Beerse city** fin debt **EUR13.82m** · **AGB Beerse** fin debt **EUR5.02m** · **Pepingen city** fin debt **EUR3.47m** · **Vleteren** fin debt **EUR3.32m** · prior **Stad+OCMW Kortenaken** fin debt **EUR10.57m** IGS EV-reval **EUR8.90m** OCMW equity **−EUR5.41m** · **Heusden-Zolder** fin debt **EUR37.85m** IGS reval **EUR31.12m** · **Kapelle-op-den-Bos** fin debt **EUR18.87m** · **Oud-Heverlee** fin debt **EUR15.18m** · **Diepenbeek city** fin debt **EUR13.59m** IGS reval **EUR19.43m** · **Huldenberg** fin debt **EUR9.56m** · **AGB Kortenaken** fin debt **EUR3.28m** leasing **EUR3.22m** · **Voeren** fin debt **EUR3.37m** · **AGB Diepenbeek** fin debt **EUR3.03m** · **Steenokkerzeel** fin debt **EUR2.49m** · prior **Stad+OCMW Bekkevoort** fin debt **EUR9.77m** IGS EV-reval **EUR5.90m** · **HH city** fin debt **EUR17.37m** · **AGB Masterplan HH** fin debt **EUR27.81m** · **AGB Sport HH** fin debt **EUR10.72m** · **AGB SCO Ronse** fin debt **EUR22.65m** · **Ronse city** fin debt **EUR25.02m** pension **EUR19.50m** · **Kraainem** fin debt **EUR6.40m** · **Tielt-Winge** fin debt **EUR8.52m** · prior **Stad+OCMW Tienen** fin debt **EUR59.73m** pension **EUR51.29m** · **Machelen** fin debt **EUR26.37m** Farys lease **EUR16.90m** · **AGB Tienen** fin debt **EUR16.93m** · **AG Museum Leuven** fin debt **EUR14.51m** · **Gingelom** Fluvius reval **EUR9.75m** fin debt **EUR3.86m** · prior **AGB MAC** fin debt **EUR40.3m** leasing **EUR40.8m** · **Mintus** dual **EUR26.36m** · Digipolis assets **EUR73.61m** · **AG Vespa** fin debt **EUR179.6m** DBFM **EUR109.4m** · **sogent** AFM **−EUR3.90m** debt **EUR96.3m** · AG-O cum loss **−EUR29.2m** · Zorgbedrijf Antwerpen AFM **−EUR18.87m** debt **EUR220m** / Dodoens equity **−EUR18.88m** / Hasselt ~EUR95–103m stack retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market.

### Inventory (tick 1320)

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
| research_queue open | rq_116 deferred + rq_1321 hole-fill after progress |

### What improved since tick 1310

- **VL residual dual JR2025 Entity II / leftover APB (tick1311-1319):** **AGB Maaseik** fin debt **1.60m** AFM **−0.67m** city inject **1.43m** · **AGBIM** assets **20.41m** CCAO **8.91m** fin debt **0** · **AGB Merchtem / AGB Sport Hulshout / Lievegem / Ranst** JR2025 unpublished or TLS — FOI-ready no invented euros · **APB PSES** assets **186.52m** ST recv **165.31m** BBR **−1.29m** fin debt **0** · **APB GKC** assets **2.67m** cash **2.11m** · **APB Havencentrum** assets **0.97m** cash **364k** ST recv **609k** Havenwereld **395k**.
- **NEW (tick1320):** **APB Kamp C** (KBO 0541.415.101) assets **5.929m** JUMP vs **2.853m** · cash **2.651m** JUMP vs **1.335m** · ST recv **3.062m** JUMP (niet-ruil **2.975m**) · schulden **3.527m** ALL ST · fin debt T4 **0** · equity **2.403m** · PnL **+1.212m** · expl **+2.522m** · BBR **+2.395m** / cum **4.806m** · AFM **+2.522m** · pers **1.654m** · J5 werksub **3.035m** vs T2 **4.288m** (gap **1.253m**; andere entiteiten **1.863m** BE.HOT!/Eco-build) · FOI ST recv + J5/T2 recon ready.
- **Dual map themes:** **leftover APB pass-through / cash+ST-recv shells** (PSES 186.52m / KampC 5.93m / GKC 2.67m / Havencentrum 0.97m) · **AGB city-loan / AFM NEG** (AGB Maaseik 1.60m) · **AGB prijssub / CCAO** (AGBIM 8.91m) · prior APB equity NEG + city GE debt/pension + Fluvius/IGS EV-reval stack retained.
- **No pure-annual waste top10 reshuffle:** GIP / fossil / company cars / cheque / reporté stack remains #1-10.

---
"""
    text = text.replace(marker, snap + marker, 1)
    prog.write_text(text, encoding="utf-8")
    print("progress_every_10_ticks.md inserted tick 1320 snapshot")


def write_waste_top10(counts: dict) -> None:
    p = DATA / "doge_waste_top10_current.md"
    text = p.read_text(encoding="utf-8")
    text = text.replace(
        "**As-of:** tick **1310** (2026-08-17) · **7106** leaderboard rows",
        f"**As-of:** tick **1320** (2026-08-17) · **{counts['leaderboard']}** leaderboard rows",
        1,
    )
    old_dual = "(**NEW APB VERA** fin debt **€1.72m** equity **−€1.64m** straight loan **€1.10m**"
    new_dual = (
        "(**NEW APB KampC** assets **€5.93m** cash **€2.65m** ST recv **€3.06m** BBR **+€2.39m** · "
        "**APB PSES** assets **€186.52m** ST recv **€165.31m** BBR **−€1.29m** · "
        "**APB GKC** assets **€2.67m** cash **€2.11m** · "
        "**APB Havencentrum** assets **€0.97m** Havenwereld **€0.40m** · "
        "**AGBIM** CCAO **€8.91m** · "
        "**AGB Maaseik** fin debt **€1.60m** AFM **−€0.67m** · "
        "prior **APB VERA** fin debt **€1.72m** equity **−€1.64m** straight loan **€1.10m**"
    )
    if old_dual not in text:
        raise SystemExit("waste top10 missing VERA dual marker")
    text = text.replace(old_dual, new_dual, 1)
    old_chg = (
        "**Change vs tick 1300:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1301–1310 (off pure top10 / dual):**"
    )
    new_chg = (
        "**Change vs tick 1310:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10). "
        "**Major NEW residual 1311–1320 (off pure top10 / dual):** **APB PSES** assets **EUR186.52m** ST recv **EUR165.31m** · **APB KampC** assets **EUR5.93m** cash **EUR2.65m** ST recv **EUR3.06m** BBR **+EUR2.39m** · **AGBIM** CCAO **EUR8.91m** · **AGB Maaseik** fin debt **EUR1.60m** AFM **−EUR0.67m** · **APB GKC** **EUR2.67m** · **APB Havencentrum** **EUR0.97m**. "
        "Gain is **leftover APB pass-through / cash+ST-recv shells + AGB city-loan AFM NEG**. "
        "**Prior 1301–1310 retained:**"
    )
    if old_chg not in text:
        raise SystemExit("waste top10 missing change-vs-1300 marker")
    text = text.replace(old_chg, new_chg, 1)
    old_out = "| — | `lb_edgm_fin_debt_14_05m_2025` | **14.05 m stock** | **~7.5 dual** | **NEW 1303** Edegem fin debt / pension |"
    new_out = (
        "| — | `lb_pses_passthrough_186m_bbr_neg_1_29m` | **186.52 m stock** | **~6.8 dual** | **NEW 1317** APB PSES pass-through / ST recv 165.31m / BBR NEG |\n"
        "| — | `lb_agbim_ccao_8_91m_2025` | **8.91 m stock** | **~5.4 dual** | **NEW 1312** AGBIM CCAO+BIB renovation |\n"
        "| — | `lb_kmpc_cash_2_65m_recv_3_06m_bbr_2_39m` | **5.93 m stock** | **~5.3 dual** | **NEW 1320** APB KampC cash JUMP / ST recv 3.06m / BBR +2.39m |\n"
        "| — | `lb_agbmsk_fin_debt_1_60m_2025` | **1.60 m stock** | **~5.0 dual** | **NEW 1311** AGB Maaseik fin debt / AFM NEG |\n"
        + old_out.replace("**NEW 1303**", "1303")
    )
    if old_out not in text:
        raise SystemExit("waste top10 missing edgm just-outside row")
    text = text.replace(old_out, new_out, 1)
    old_abs = "| `lb_apbvera_equity_neg_1_64m_2025` | **7.5** | **NEW 1310** APB VERA nettoactief −1.64m NEG / straight loan 1.10m |"
    new_abs = (
        "| `lb_pses_passthrough_186m_bbr_neg_1_29m` | **6.5** | **NEW 1317** APB PSES 186.52m pass-through / BBR −1.29m / thin equity 2.42m |\n"
        "| `lb_kmpc_cash_2_65m_recv_3_06m_bbr_2_39m` | **6.0** | **NEW 1320** APB KampC assets JUMP 2.85→5.93m / J5 vs T2 werksub gap 1.25m |\n"
        + old_abs.replace("**NEW 1310**", "1310")
    )
    if old_abs not in text:
        raise SystemExit("waste top10 missing vera absurdity row")
    text = text.replace(old_abs, new_abs, 1)
    p.write_text(text, encoding="utf-8")
    print("doge_waste_top10_current.md updated tick 1320; pure top10 unchanged")


def main() -> None:
    n = append_rows(
        DATA / "sources.csv",
        [
            {
                "source_id": SRC,
                "title": "APB Kamp C jaarrekening 2025 (official BBC text PDF)",
                "url": SRC_URL,
                "publisher": "APB Kamp C / Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1320; Foleon BBC text PDF 0.78MB print 31.03.2026 volgnr 1474979; "
                    "KBO 0541.415.101; assets 5929335.44 cash 2650988.98 ST recv 3062038.29 "
                    "ST pay 3526655.00 BBR +2394768.21 AFM +2522060.21 PnL +1212347.39; primary BBC text"
                ),
            },
            {
                "source_id": SRC2,
                "title": "Kamp C jaarverslag 2025 in cijfers (official Foleon link)",
                "url": SRC2_URL,
                "publisher": "Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "budget",
                "notes": (
                    "tick1320; publicaties.provincieantwerpen.be/kamp-c-jaarverslag-2025/in-cijfers "
                    "links the same BBC PDF; leftover sister APB of mined provincie Antwerpen"
                ),
            },
            {
                "source_id": SRC3,
                "title": "KBO APB Kamp C 0541.415.101",
                "url": SRC3_URL,
                "publisher": "KBO Public Search FOD Economie",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1320; KBO 0541.415.101 actief APB since 26.09.2013; "
                    "zetel Britselaan 20 2260 Westerlo since 26.09.2013; 1 VE; "
                    "bestuurder Jinnih Beels since 02.12.2024; NACE 84.113; "
                    "RSZ-werkgever since 01.01.2022; aanbestedende overheid; no KBO e-mail/finance"
                ),
            },
            {
                "source_id": SRC4,
                "title": "Provincie Antwerpen openbaarheid van bestuur (FOI channel)",
                "url": SRC4_URL,
                "publisher": "Provincie Antwerpen",
                "accessed_date": "2026-08-17",
                "source_class": "official_register",
                "notes": (
                    "tick1320; FOI openbaarheid@provincieantwerpen.be / provinciegriffier; "
                    "Koningin Elisabethlei 22 2018"
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
                "name_nl": "APB Kamp C",
                "name_fr": "APB Kamp C (centre provincial construction durable)",
                "name_en": "APB Kamp C (provincial circular-building centre)",
                "level": "apb",
                "parent_id": "prov_antwerpen",
                "community_language": "nl",
                "website": "https://www.kampc.be",
                "foi_email": FOI_EMAIL,
                "foi_postal": FOI_POSTAL,
                "notes": (
                    "tick1320 JR2025 leftover sister APB residual; KBO 0541.415.101; assets 5929335 "
                    "fin debt 0 ST recv 3062038 ST pay 3526655 BBR +2394768 AFM +2522060 "
                    "PnL +1212347 cash 2650989 equity 2402680; FOI ready"
                ),
            },
        ],
    )
    print("entities", n)

    budget_rows = [
        ("bud_kmpc_assets_2025", "2025", "5929335", "YE2025 assets 5929335.44 was 2853348.37 JUMP; tick1320; primary BBC J4"),
        ("bud_kmpc_assets_2024", "2024", "2853348", "YE2024 assets 2853348.37; tick1320; primary BBC J4"),
        ("bud_kmpc_cash_2025", "2025", "2650989", "YE2025 cash 2650988.98 was 1334815.88 JUMP; tick1320; primary BBC J4"),
        ("bud_kmpc_cash_2024", "2024", "1334816", "YE2024 cash 1334815.88; tick1320; primary BBC J4"),
        ("bud_kmpc_current_2025", "2025", "5739045", "YE2025 vlottende activa 5739044.54; tick1320; primary BBC J4"),
        ("bud_kmpc_recv_st_2025", "2025", "3062038", "YE2025 ST recv 3062038.29 (ruil 87457.68 + niet-ruil 2974580.61) was 1374886.58 JUMP; tick1320; primary BBC J4"),
        ("bud_kmpc_recv_nietruil_2025", "2025", "2974581", "YE2025 ST niet-ruil recv 2974580.61; tick1320; primary BBC J4"),
        ("bud_kmpc_recv_ruil_2025", "2025", "87458", "YE2025 ST ruil recv 87457.68; tick1320; primary BBC J4"),
        ("bud_kmpc_inventories_2025", "2025", "826", "YE2025 voorraden 825.62; tick1320; primary BBC J4"),
        ("bud_kmpc_accruals_act_2025", "2025", "25192", "YE2025 overlopend actief 25191.65; tick1320; primary BBC J4"),
        ("bud_kmpc_fixed_2025", "2025", "190291", "YE2025 vaste activa 190290.90 was 116767.72; tick1320; primary BBC J4/T5"),
        ("bud_kmpc_fva_2025", "2025", "223", "YE2025 FVA 223.11 andere; tick1320; primary BBC J4/T5"),
        ("bud_kmpc_mva_2025", "2025", "128358", "YE2025 MVA 128357.79 leasing 0; tick1320; primary BBC J4"),
        ("bud_kmpc_iva_2025", "2025", "61710", "YE2025 IVA 61710.00 new 2025; tick1320; primary BBC J4/T2"),
        ("bud_kmpc_schulden_2025", "2025", "3526655", "YE2025 schulden 3526655.00 ALL ST was 1663015.32; tick1320; primary BBC J4"),
        ("bud_kmpc_pay_ruil_2025", "2025", "907425", "YE2025 non-fin ST ruil pay 907425.09 was 298868.49; tick1320; primary BBC J4"),
        ("bud_kmpc_accruals_2025", "2025", "2619230", "YE2025 overlopend passief 2619229.91 was 1364146.83 JUMP; tick1320; primary BBC J4"),
        ("bud_kmpc_fin_debt_2025", "2025", "0", "YE2025 T4 fin debt 0 (J4 empty financiële schulden; T2 financing empty; T4 schema unpublished); tick1320; primary BBC J4/T2"),
        ("bud_kmpc_equity_2025", "2025", "2402680", "YE2025 nettoactief 2402680.44 was 1190333.05; tick1320; primary BBC J4/T5"),
        ("bud_kmpc_cum_pnl_2025", "2025", "2208115", "YE2025 gecumuleerd overschot 2208114.93 was 995767.54; tick1320; primary BBC J4/T5"),
        ("bud_kmpc_pnl_2025", "2025", "1212347", "2025 J5 PnL +1212347.39 (ops +1205096.63 / fin +7250.76); tick1320; primary BBC J5"),
        ("bud_kmpc_expl_saldo_2025", "2025", "2522060", "2025 expl saldo +2522060.21 (ontv 4844962.43 / uitg 2322902.22); tick1320; primary BBC J2"),
        ("bud_kmpc_expl_ontv_2025", "2025", "4844962", "2025 expl ontv 4844962.43; tick1320; primary BBC J2"),
        ("bud_kmpc_expl_uitg_2025", "2025", "2322902", "2025 expl uitg 2322902.22; tick1320; primary BBC J2"),
        ("bud_kmpc_invest_2025", "2025", "127292", "2025 invest uitg 127292.00 (MVA 65582 + IVA 61710); tick1320; primary BBC J2/T2"),
        ("bud_kmpc_bbr_2025", "2025", "2394768", "2025 BBR year +2394768.21; tick1320; primary BBC J2"),
        ("bud_kmpc_cum_bbr_2025", "2025", "4805602", "YE2025 cum BBR 4805602.18 was 2410833.97; tick1320; primary BBC J2"),
        ("bud_kmpc_afm_2025", "2025", "2522060", "2025 AFM +2522060.21 = gecorr AFM; no afl; tick1320; primary BBC J2"),
        ("bud_kmpc_pers_2025", "2025", "1654303", "2025 J5 pers 1654303.44 / T2 1650129.04; VTE unpublished FOI; tick1320; primary BBC"),
        ("bud_kmpc_goods_2025", "2025", "673147", "2025 J5 goederen/diensten 673147.19 / T2 670503.45; tick1320; primary BBC"),
        ("bud_kmpc_werksub_in_2025", "2025", "3034955", "2025 J5 werksub ontv 3034954.63 (alg 2096863.23 + spec 938091.40); tick1320; primary BBC J5"),
        ("bud_kmpc_werksub_t2_2025", "2025", "4287819", "2025 T2 werksub kas 4287819.08 (alg provincie 1966516.00 + spec 2321303.08); J5/T2 gap 1252864.45 FOI; tick1320; primary BBC T2"),
        ("bud_kmpc_werksub_prov_2025", "2025", "1966516", "2025 T2 alg werksub van de provincie 1966516.00 vs J5 alg 2096863.23; tick1320; primary BBC T2/J5"),
        ("bud_kmpc_werksub_spec_andere_2025", "2025", "1863164", "2025 T2 spec werksub andere entiteiten 1863164.20 (BE.HOT! / Eco-build Kempen class); tick1320; primary BBC T2"),
        ("bud_kmpc_other_ops_2025", "2025", "111156", "2025 J5 andere operationele opbrengsten 111156.13; tick1320; primary BBC J5"),
        ("bud_kmpc_ops_rev_2025", "2025", "440205", "2025 J5 opbrengsten uit de werking 440205.32; tick1320; primary BBC J5"),
        ("bud_kmpc_costs_2025", "2025", "2383489", "2025 J5 costs 2383489.18; tick1320; primary BBC J5"),
        ("bud_kmpc_rev_2025", "2025", "3595837", "2025 J5 opbrengsten 3595836.57; tick1320; primary BBC J5"),
        ("bud_kmpc_deprec_2025", "2025", "53769", "2025 J5 afschrijvingen 53768.82; tick1320; primary BBC J5/T5"),
    ]
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
            for bid, year, amt, notes in budget_rows
        ],
    )
    print("budgets", n)

    n = append_rows(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_kmpc_jr2025_dual",
                "title": "APB KampC JR2025 leftover APB dual (cash 2.65m / ST recv 3.06m / J5-T2 werksub gap 1.25m)",
                "entity_id": ENT,
                "beneficiary": "BE.HOT! / Eco-build Kempen + provincie Antwerpen dual circular-building",
                "legal_basis": "Provinciedecreet APB; BBC; Bestuursdecreet openbaarheid",
                "decision_date": "",
                "start_year": "2025",
                "end_year": "2027",
                "total_envelope_eur": "5929335",
                "cash_by_year": "",
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": SRC_URL,
                "stated_goal": "Circular / biobased building centre (Circustraject, starterswerking, BE.HOT!, Eco-build, energiegemeenschap; Vonk renovatie 2026)",
                "cut_option": "Publish named ST recv ledger + J5/T2 werksub 1.25m recon + BE.HOT!/Eco-build envelopes + VTE; shrink leftover APB if intra-group",
                "source_id": SRC,
                "confidence": "strong",
                "hierarchy_path": HIER + ">jr2025_L5",
                "notes": "tick1320; assets 5929335 ST recv 3062038 ST pay 3526655 BBR +2394768 AFM +2522060 PnL +1212347; FOI ready not sent",
            }
        ],
    )
    print("commitments", n)

    n = append_rows(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_kmpc_cash_2_65m_recv_3_06m_bbr_2_39m",
                "name": "APB KampC JR2025 leftover APB: 5.93m assets / 2.65m cash / 3.06m ST recv / BBR +2.39m",
                "level": "L5",
                "type": "local_budget_line",
                "hierarchy_path": HIER + ">jr2025_L5",
                "annual_cost_eur": "2322902",
                "total_cost_eur": "5929335",
                "tco_notes": "Leftover dual APB shell: assets 5.93m JUMP / cash 2.65m JUMP / equity 2.40m; expl uitg 2.32m; J5/T2 werksub gap 1.25m; do not treat 5.93m as TE-additive of 348bn",
                "confidence": "strong",
                "source_id": SRC,
                "beneficiaries": "BE.HOT! / Eco-build Kempen + provincie Antwerpen dual",
                "stated_goal": "Circular / biobased building centre (Vonk renovatie 2026)",
                "measured_outcome": "Official BBC PDF 2026-08-17: BBR +2.395m / AFM +2.522m / PnL +1.212m; cash 2.65m JUMP; ST recv 3.06m JUMP; J5 werksub 3.035m vs T2 4.288m; VTE unpublished",
                "absurdity_score": "6.0",
                "cost_score": "4.5",
                "difficulty": "3.0",
                "priority_index": "5.3",
                "cut_proposal": "Publish named ST recv + J5/T2 werksub recon + BE.HOT!/Eco-build envelopes; shrink leftover APB if intra-group",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1320; leftover sister APB of mined provincie Antwerpen; FOI ready not sent; not TE-additive of 348bn; every-10",
            }
        ],
    )
    print("leaderboard", n)

    n = append_rows(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": GAP,
                "hierarchy_path": HIER + ">jr2025_L5",
                "entity_id": ENT,
                "what_is_missing": (
                    "Named counterparties behind ST recv 3062038.29 (ruil 87457.68 + niet-ruil 2974580.61) "
                    "and ST non-fin ruil pay 907425.09 + accruals 2619229.91 + recon J5 werksub 3034954.63 "
                    "vs T2 4287819.08 (gap 1252864.45) and named BE.HOT!/Eco-build / andere-entiteiten "
                    "1863164.20 envelopes + VTE behind pers 1654303.44 + T4 schema unpublished + T5 "
                    "opening equity 679522.77 vs J4 1190333.05 + provincieraad vaststelling JR2025 + "
                    "NBB non-filing legal basis"
                ),
                "why_it_matters": (
                    "Leftover unmapped sister APB of already-mined provincie Antwerpen after honest residual "
                    "dual hunt (Havencentrum 1319 / GKC 1318 / PSES 1317 done). KBO 0541.415.101 active. "
                    "Official BBC PDF now downloads (Foleon). 5.93m leftover APB shell with cash JUMP to 2.65m, "
                    "ST recv JUMP to 3.06m, and J5/T2 werksub gap 1.25m. Sister leftover APBs PSES/GKC/HC now mined. "
                    "Do not invent euros."
                ),
                "priority": "7",
                "recipient_body": "APB Kamp C / Provincie Antwerpen / provinciegriffier",
                "recipient_email": FOI_EMAIL,
                "recipient_postal": FOI_POSTAL,
                "draft_letter_path": DRAFT,
                "status": "ready",
                "date_ready": "2026-08-17",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_kmpc_jr2025_dual",
                "linked_leaderboard_id": "lb_kmpc_cash_2_65m_recv_3_06m_bbr_2_39m",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": f"tick{TICK}; ready not sent; do not send without human OK; sourced euros from primary BBC; every-10 progress also this tick",
            }
        ],
    )
    print("foi", n)

    rq_new = {
        "task_id": "rq_1320",
        "title": "APB KampC JR2025 dual residual leftover APB + every-10 progress",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENT,
        "instructions": (
            "Completed: every-10 progress refresh + APB KampC JR2025 leftover sister APB after honest hunt; "
            "KBO 0541.415.101; official BBC PDF downloads; assets 5.93m / cash 2.65m / ST recv 3.06m / "
            "BBR +2.39m / AFM +2.52m / PnL +1.21m; FOI ready; progress@1320"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-17T18:20:00Z",
        "updated_utc": UTC,
        "notes": (
            "tick1320 APB KampC JR2025 leftover sister APB residual + progress@1320; KBO 0541.415.101; "
            "assets 5929335 ST recv 3062038 ST pay 3526655 BBR +2394768 AFM +2522060 "
            "PnL +1212347; FOI ready not sent; next rq_1321 residual dual L5 VL"
        ),
    }
    rq_spawn = {
        "task_id": "rq_1321",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "hole_fill",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Residual dual L5 VL JR2025 hole-fill next AGB/GE/zorg/EVA not yet mined "
            "(prior 1255-1320 done including APB KampC 1320 leftover sister APB + every-10 / "
            "APB Havencentrum 1319 leftover sister APB / APB GKC 1318 leftover sister APB / "
            "APB PSES 1317 leftover APB / Stad+OCMW Ranst 1316 FOI-unpublished / Stad+OCMW Lievegem 1315 FOI-TLS / "
            "AGB Sport Hulshout 1314 FOI-unpublished / AGB Merchtem 1313 FOI-unpublished / AGBIM Maaseik 1312 / "
            "AGB Maaseik 1311 / APB VERA 1310); prefer other unmined AGB/zorg/EVA with direct "
            "PDF (provincie Antwerpen leftover sister APBs PSES/GKC/HC/KampC now mined; "
            "AGB Blankenberge only if a PDF actually downloads); "
            "leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/"
            "Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE/Bierbeek still unmined — take only if PDF fetches; "
            "skip already-mined APB KampC 1320 / APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / "
            "Stad+OCMW Ranst 1316 / Stad+OCMW Lievegem 1315 "
            "(FOI TLS) / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 / "
            "APB VERA 1310 / EVA Hoeve Holleken 1309 / Stad+OCMW Beerse 1308 / AGB Beerse 1307 / "
            "Ternat / Oostkamp / Wetteren / Poperinge / Haacht / Bilzen-Hoeselt / AGB Sport Geel / Zwevegem; "
            "skip Motena / Trupark / PATRI / Zorgbedrijf ST / Woonzorgnetwerk Edegem TLS; "
            "ebesluit TLS + Roeselare.be Cloudflare + zorgbedrijfsinttruiden.be TLS + "
            "vlaamsbrabant.be TLS + lievegem.be TLS + provincieantwerpen.be 403 (Foleon OK); not every-10"
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": "spawned tick1320 after APB KampC JR2025 leftover sister APB + progress@1320; next residual dual L5 VL",
    }
    found, spawned = patch_last_rq_and_spawn(DATA / "research_queue.csv", "rq_1320", rq_new, rq_spawn)
    print("research_queue 1320", found, "spawned_1321", spawned)

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
                "last_unit_id": "rq_1320",
                "ticks_completed": "1320",
                "paused": "no",
                "notes": (
                    "tick1320 APB KampC JR2025 leftover sister APB residual + progress@1320; KBO 0541.415.101; "
                    "assets 5.93m cash 2.65m ST recv 3.06m ST pay 3.53m BBR +2.39m AFM +2.52m PnL +1.21m; "
                    "FOI ready; next rq_1321 residual dual L5 VL; continuous hole_fill"
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
        "foi_total": count_csv_rows(DATA / "foi_queue.csv"),
    }
    print("COUNTS", counts)
    write_progress(counts)
    write_waste_top10(counts)

    log_entry = f"""
### Tick 1320 - 2026-08-17 - rq_1320 APB KampC dual residual leftover sister APB + progress@1320
- Unit: APB Kamp C JR2025 leftover sister APB/EVA of already-mined provincie Antwerpen after residual dual hunt (KBO **0541.415.101**; official BBC text PDF on Foleon 25p / 0.78MB; print **31.03.2026**; volgnr **1474979**; Jnl. via CSrapportaal). EVERY-10 first: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md from on-disk CSVs. THEN leftover sister APB KampC whose Foleon JR2025 PDF was still live/unmined as of 1319. Distinct from already-mined APB Havencentrum 1319 / APB GKC 1318 / APB PSES 1317 / APB VERA 1310 / Westtoer / APB Mercator. KBO zetel Britselaan 20 2260 Westerlo since 26.09.2013. Bestuurder Jinnih Beels since 02.12.2024. NACE 84.113; RSZ-werkgever since 01.01.2022; aanbestedende overheid; 1 VE; no KBO e-mail. APB states not an onderneming — no NBB filing. Circustraject / starterswerking / BE.HOT! / Eco-build Kempen / energiegemeenschap; Vonk renovatie verschoven naar 2026. Hunt leftover AGB first: AGB Blankenberge official still **JR2019-only** (unmined, no JR2025 PDF); AGB Bornem / AGB De Kluize already FOI — no new PDF. Leftover cities Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Maaseik GE/Bierbeek still no fetchable JR2025. provincieantwerpen.be 403 from this box (Foleon OK). Skip already-mined Havencentrum 1319 / GKC 1318 / PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313. Every-10 tick.
- EUR strong (primary BBC J2/J4/J5/T2/T5; T4 schema unpublished — fin debt **0** from J4 empty financiële schulden + T2 empty financing + AFM = expl): assets **5.929.335,44** (was 2.853.348,37) JUMP; cash **2.650.988,98** vs 1.334.815,88 JUMP; ST recv **3.062.038,29** (ruil **87.457,68** + niet-ruil **2.974.580,61**) JUMP vs 1.374.886,58; fixed **190.290,90**; FVA **223,11**; MVA **128.357,79**; IVA **61.710,00**; leasing **0**; schulden **3.526.655,00** ALL ST; fin debt T4 **0**; non-fin ST ruil pay **907.425,09**; accruals **2.619.229,91** JUMP; equity **2.402.680,44**; cum surplus **2.208.114,93**; expl **+2.522.060,21** (ontv **4.844.962,43** / uitg **2.322.902,22**); invest **−127.292,00**; fin **0**; BBR year **+2.394.768,21**; cum BBR **4.805.602,18**; AFM/gecorr **+2.522.060,21**; PnL **+1.212.347,39**; pers J5 **1.654.303,44** / T2 **1.650.129,04**; werksub granted **0**; werksub received J5 **3.034.954,63** vs T2 **4.287.819,08** (gap **1.252.864,45**; T2 andere entiteiten **1.863.164,20** BE.HOT!/Eco-build); other ops **111.156,13**. VTE unpublished.
- CSVs: sources+4/entities+1/budgets+39/commitments+1/leaderboard+1 + FOI ready `{GAP}` (not sent); rq_1320=done; spawn rq_1321; ticks=1320.
- Progress@1320: refreshed progress_every_10_ticks.md + doge_waste_top10_current.md. Layers A 100 / B 100 / C ~99 / D ~74-88 (not near-complete of 348bn) / E recounted ready **{counts['foi_ready']}** (answered {counts['foi_answered']} / partial {counts['foi_partial']} / total {counts['foi_total']}). Inventory: budgets {counts['budgets']} · commitments {counts['commitments']} · leaderboard {counts['leaderboard']} · entities {counts['entities']} · sources {counts['sources']}. Pure annual waste top10 **stable** vs 1310 (GIP/fossil/cars/cheque/reporté). Dual off-top10 adds PSES 186.52m / KampC 5.93m / AGBIM 8.91m / AGB Maaseik 1.60m / GKC 2.67m / Havencentrum 0.97m.
- Coverage: 1311–1320 is residual dual L5 (AGB Maaseik · AGBIM · AGB Merchtem FOI · AGB Sport Hulshout FOI · Lievegem FOI · Ranst FOI · APB PSES · APB GKC · APB Havencentrum · **APB KampC**). Does **not** move L5 near-complete of €347.956 bn TE. Taxex/FFS remain off-TE.
- Next: rq_1321 residual dual L5 VL JR2025 hole_fill (provincie Antwerpen leftover sister APBs PSES/GKC/HC/KampC now mined; leftover AGB Blankenberge only if a PDF now downloads; leftover Londerzeel/Holsbeek/Zwalm/Wortegem-Petegem/Maarkedal/Linkebeek/Kapellen/Drogenbos/Boutersem/Stad+OCMW Maaseik GE only if a PDF fetches; skip Motena / Trupark / PATRI / Zorgbedrijf ST / already-mined APB KampC 1320 / Havencentrum 1319 / GKC 1318 / PSES 1317 / Ranst 1316 / Lievegem 1315 / AGB Sport Hulshout 1314 / AGB Merchtem 1313 / AGBIM 1312 / AGB Maaseik 1311 unless a fetchable JR appears).
"""
    log = ROOT / "loop_log.md"
    raw = log.read_bytes()
    if not raw.endswith(b"\n"):
        raw += b"\n"
    log.write_bytes(raw + log_entry.encode("utf-8"))
    print("loop_log ok")
    print("tick1320 write done")


if __name__ == "__main__":
    main()
