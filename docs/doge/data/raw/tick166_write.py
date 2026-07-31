# -*- coding: utf-8 -*-
"""Tick 166: HR Rail NV PR institutional omzet/FTE from NBB-filed accounts (via Companyweb)."""
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
TS = "2026-07-28T05:25:00Z"
TICK = 166
UNIT = "rq_161"


def append_lines(path: Path, lines: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def replace_line_startswith(path: Path, prefix: str, new_line: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []
    found = False
    for line in lines:
        if line.startswith(prefix):
            out.append(new_line if new_line.endswith("\n") else new_line + "\n")
            found = True
        else:
            out.append(line)
    if not found:
        raise SystemExit(f"prefix not found: {prefix}")
    path.write_text("".join(out), encoding="utf-8", newline="\n")


# HR Rail series (Companyweb citing NBB CBSO jaarrekening filings)
omzet = {2022: 2077763226, 2023: 2205907450, 2024: 2304846457, 2025: 2368227721}
profit = {2022: 9201712, 2023: 2960494, 2024: 693536, 2025: 1568042}
equity = {2022: 23120618, 2023: 26069315, 2024: 26754065, 2025: 28313321}
fte = {2022: 27435.1, 2023: 27524.5, 2024: 27568.5, 2025: 27811}
gross = {2022: 2054039716, 2023: 2180649199, 2024: 2277584166, 2025: 2339082399}

append_lines(
    DATA / "sources.csv",
    [
        "src_hr_rail_companyweb_nbb,HR Rail NV PR financials Companyweb citing NBB CBSO filings,"
        "https://www.companyweb.be/nl/0541691352/hr-rail,"
        "Companyweb / NBB Central Balance Sheet Office,2026-07-28,secondary_nbb_filing,"
        '"BE0541691352; omzet 2.368bn 2025 / 2.305bn 2024; FTE 27811/27568.5; profit ~1.6m pass-through; '
        'filing date class 2026-06-10; residual free NBB PDF FOI optional; tick166"'
    ],
)

append_lines(
    DATA / "entities.csv",
    [
        "hr_rail,HR Rail NV van publiek recht,HR Rail SA de droit public,HR Rail public limited company,"
        "parastatal,sec_federal,bi,https://www.hr-rail.be,,"
        "Frankrijkstraat 85 1060 Sint-Gillis,"
        "Legal employer all NMBS+Infrabel staff (KB 11 Dec 2013); omzet ~2.37bn 2025 pass-through payroll; "
        "FTE 27811; dual rail structure; tick166",
    ],
)

bud = []
for y in (2022, 2023, 2024, 2025):
    bud.append(
        f"bud_hr_rail_omzet_{y},hr_rail,{y},{omzet[y]},,,outturn,src_hr_rail_companyweb_nbb,medium,"
        f"HR Rail turnover {y} NBB filing via Companyweb (payroll re-invoice NMBS+Infrabel)"
    )
    bud.append(
        f"bud_hr_rail_profit_{y},hr_rail,{y},{profit[y]},,,outturn,src_hr_rail_companyweb_nbb,medium,"
        f"HR Rail net result {y} (near-zero pass-through entity)"
    )
    bud.append(
        f"bud_hr_rail_equity_{y},hr_rail,{y},{equity[y]},,,outturn,src_hr_rail_companyweb_nbb,medium,"
        f"HR Rail equity EOY {y}"
    )
    bud.append(
        f"bud_hr_rail_fte_{y},hr_rail,{y},{int(round(fte[y]))},,,outturn,src_hr_rail_companyweb_nbb,medium,"
        f"HR Rail FTE average {y} ({fte[y]})"
    )
    bud.append(
        f"bud_hr_rail_gross_margin_{y},hr_rail,{y},{gross[y]},,,outturn,src_hr_rail_companyweb_nbb,medium,"
        f"HR Rail gross margin {y} (nearly equals omzet)"
    )
# unit cost class
bud.append(
    "bud_hr_rail_omzet_per_fte_2025,hr_rail,2025,85154,,,outturn,src_hr_rail_companyweb_nbb,medium,"
    "Implied omzet/FTE 2025 ~85.2k EUR (2.368bn/27811)"
)
append_lines(DATA / "budgets.csv", bud)

append_lines(
    DATA / "commitments.csv",
    [
        'cmt_hr_rail_payroll_pass_through,HR Rail legal employer rail payroll pass-through multi-year,hr_rail,'
        "NMBS Infrabel staff via KB 11 Dec 2013,HR Rail NV PR statutory employer + NBB filings,"
        "2013-11-04,2022,2025,2368227721,"
        '"{""2022_omzet"":2077763226,""2023_omzet"":2205907450,""2024_omzet"":2304846457,""2025_omzet"":2368227721,'
        '""2022_fte"":27435.1,""2023_fte"":27524.5,""2024_fte"":27568.5,""2025_fte"":27811,'
        '""2025_profit"":1568042,""2025_equity"":28313321,""be_number"":""0541691352"",'
        '""role"":""juridische_werkgever_alle_spoorpersoneel"",'
        '""note"":""turnover is almost entirely staff costs re-invoiced to NMBS and Infrabel; not additional public subsidy beyond PSO packages""}",'
        "0,active,https://www.companyweb.be/nl/0541691352/hr-rail,"
        "Centralise rail employment dual NMBS+Infrabel,"
        "Publish free NBB PDF; FTE matrix by NMBS vs Infrabel charge; simplify dual structure,"
        "src_hr_rail_companyweb_nbb,medium,Federal>Mobiliteit>HR_Rail,"
        "tick166; dual overhead opacity reduced on size",
    ],
)

append_lines(
    DATA / "leaderboard.csv",
    [
        "lb_hr_rail_payroll_2_4bn,HR Rail payroll pass-through omzet ~2.37bn 2025,federal,ops,"
        "Federal>Mobiliteit>HR_Rail,2304846457,2368227721,"
        "Medium NBB filing via Companyweb: 2.305bn 2024 / 2.368bn 2025; FTE 27.6k-27.8k; dual NMBS+Infrabel legal employer,"
        "medium,src_hr_rail_companyweb_nbb,Rail staff taxpayers,"
        "Legal employer of all Belgian rail public staff,"
        "Not pure waste (core ops) but dual structure opacity: tiny profit 1.6m on 2.4bn; HR admin overhead critiques,"
        "5,9.5,7,7.3,"
        "Open NBB PDF; publish NMBS vs Infrabel staff charge split; consider structure simplification,"
        "seed,,tick166",
        "lb_hr_rail_fte_27k,HR Rail workforce ~27.8k FTE 2025,federal,ops,"
        "Federal>Mobiliteit>HR_Rail>FTE,27569,27811,"
        "Medium: FTE 27568.5 2024 / 27811 2025; omzet/FTE ~85k; dual with NMBS 16976 own count partial,"
        "medium,src_hr_rail_companyweb_nbb,Rail users,"
        "Rail public employment stock,"
        "Core public service employment; dual employer layer,"
        "4,8.5,6,6.2,"
        "Reconcile NMBS reported staff 16976 vs HR Rail total 27811 (rest Infrabel+other),"
        "seed,,tick166",
    ],
)

# FOI: optional gap for free NBB PDF + charge matrix, update infrabel gap note
replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_infrabel_dotatie_cash,",
    "gap_infrabel_dotatie_cash,Federal>Mobiliteit>Infrabel>subsidies_cash,infrabel,"
    "FPS/BOSA cash-by-year article codes for exploitatiesubsidies and kapitaalsubsidies 2022-2026 reconcile to JV 560.9m/794.9m; "
    "HR Rail personnel charge matrix NMBS vs Infrabel (HR Rail omzet 2.37bn 2025 now medium public); multi-year invest L5; Liefkenshoek series,"
    "JV 2024 + HR Rail size filled; absolute federal cash codes and staff charge split still opaque,"
    "6,FOD Mobiliteit / BOSA / Infrabel / IBZ FOI,,https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_infrabel_dotatie_cash.md,ready,2026-07-28,,,,,"
    "cmt_infrabel_results_2024|cmt_hr_rail_payroll_pass_through,lb_hr_rail_payroll_2_4bn,"
    "2026-07-28T03:45:00Z,2026-07-28T05:25:00Z,"
    "tick161 JV |tick166 HR Rail omzet/FTE medium; residual FPS cash+charge matrix human send\n",
)

# new FOI gap for HR Rail free NBB confirmation + L5 charge split
foi = (DATA / "foi_queue.csv").read_text(encoding="utf-8")
if "gap_hr_rail_charge_matrix" not in foi:
    append_lines(
        DATA / "foi_queue.csv",
        [
            "gap_hr_rail_charge_matrix,Federal>Mobiliteit>HR_Rail>charge_matrix,hr_rail,"
            "Free official NBB CBSO full jaarrekening PDF 2023-2025; annual staff charge re-invoice L5 split NMBS vs Infrabel vs other; "
            "FTE by entity and statute; admin overhead of HR Rail entity itself,"
            "Institutional omzet/FTE now medium via aggregator; dual structure charge L5 and free primary PDF still needed,"
            "5,HR Rail / FOD Mobiliteit / IBZ FOI,,"
            "https://www.ibz.be/nl/openbaarheid-van-bestuur,"
            "docs/doge/foi/drafts/gap_hr_rail_charge_matrix.md,draft,,,,,,,"
            "cmt_hr_rail_payroll_pass_through,lb_hr_rail_payroll_2_4bn,"
            f"{TS},{TS},tick166 draft pending letter",
        ],
    )

# draft FOI letter from template
template_path = ROOT / "foi-template-nl.md"
draft_path = ROOT / "foi" / "drafts" / "gap_hr_rail_charge_matrix.md"
if template_path.exists() and not draft_path.exists():
    tpl = template_path.read_text(encoding="utf-8")
else:
    tpl = ""

letter = f"""# FOI draft — gap_hr_rail_charge_matrix

**Status:** draft (complete for human review → set ready when approved)  
**Gap ID:** gap_hr_rail_charge_matrix  
**Tick:** {TICK}  
**Recipient:** HR Rail NV van publiek recht / FOD Mobiliteit / IBZ openbaarheid  
**Do not send as agent** — human only.

---

**Betreft:** Openbaarheid van bestuur — jaarrekening HR Rail en doorrekening personeelskosten NMBS/Infrabel

Geachte,

In het kader van de openbaarheid van bestuur (wet 11 april 1994 / toepasselijke federale regels) verzoek ik om de volgende documenten en gegevens over **HR Rail NV van publiek recht** (KBO 0541.691.352), juridische werkgever van het spoorwegpersoneel:

1. **Jaarrekeningen 2023, 2024 en 2025** zoals neergelegd bij de NBB (volledige PDF of bevestiging van de openbare CBSO-neerlegging), met toelichting omzet, brutomarge, resultaat, eigen vermogen en FTE.

2. **Doorrekening personeelskosten** (cash of facturatie) per kalenderjaar 2022–2025, opgesplitst naar:
   - NMBS/SNCB;
   - Infrabel;
   - overige entiteiten (indien van toepassing).

3. **FTE-matrix** per 1 februari of jaargemiddelde, gesplitst naar NMBS vs Infrabel en naar hoofdstatuut (statutair/contractueel).

4. **Eigen werkingskosten** van de entiteit HR Rail (administratie HR) als aandeel van de omzet, indien afzonderlijk gerapporteerd.

Doel is de duale spoorstructuur (NMBS + Infrabel + HR Rail) te reconstrueren zonder inventie van bedragen.  
Reeds publiek (secundair, Companyweb/NBB-neerlegging): omzet ca. **EUR 2,368 bn (2025)** / **2,305 bn (2024)**; FTE **27.811 (2025)**.

Gelieve te antwoorden binnen de wettelijke termijn, digitaal indien mogelijk.

Met vriendelijke groet,  
[Naam / mandaat — in te vullen door menselijke afzender]  
[Contact]

---

## Agent notes
- Aggregator figures medium; free NBB PDF would upgrade to strong.
- Do not mark sent without human confirmation.
"""
draft_path.parent.mkdir(parents=True, exist_ok=True)
draft_path.write_text(letter, encoding="utf-8", newline="\n")

# upgrade FOI to ready now that draft exists
replace_line_startswith(
    DATA / "foi_queue.csv",
    "gap_hr_rail_charge_matrix,",
    "gap_hr_rail_charge_matrix,Federal>Mobiliteit>HR_Rail>charge_matrix,hr_rail,"
    "Free official NBB CBSO full jaarrekening PDF 2023-2025; annual staff charge re-invoice L5 split NMBS vs Infrabel vs other; "
    "FTE by entity and statute; admin overhead of HR Rail entity itself,"
    "Institutional omzet/FTE now medium via aggregator; dual structure charge L5 and free primary PDF still needed,"
    "5,HR Rail / FOD Mobiliteit / IBZ FOI,,"
    "https://www.ibz.be/nl/openbaarheid-van-bestuur,"
    "docs/doge/foi/drafts/gap_hr_rail_charge_matrix.md,ready,2026-07-28,,,,,"
    "cmt_hr_rail_payroll_pass_through,lb_hr_rail_payroll_2_4bn,"
    f"{TS},{TS},tick166 draft ready human send\n",
)

replace_line_startswith(
    DATA / "research_queue.csv",
    "rq_161,",
    "rq_161,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register VIPA Mons BI2026 HR Rail) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    "gap_hr_rail_charge_matrix,2026-07-28T05:05:00Z,2026-07-28T05:25:00Z,"
    '"tick166: HR Rail omzet 2.368bn 2025 / 2.305bn 2024 FTE 27811 medium NBB via Companyweb; FOI charge matrix ready; spawn rq_162"\n',
)

rq = (DATA / "research_queue.csv").read_text(encoding="utf-8")
if "rq_162," not in rq:
    append_lines(
        DATA / "research_queue.csv",
        [
            "rq_162,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
            '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register VIPA Mons BI2026) if new PDFs appear; else next open rq; do not idle while public work remains.",'
            ",2026-07-28T05:25:00Z,,"
            '"Spawned tick166 after HR Rail map; rq_116 SWA deferred Oct-Dec 2026"',
        ],
    )

(DATA / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{TS},{UNIT},{TICK},no,"
    '"Scheduler 60s. Next prio5 rq_162 hole-fill De Lijn/Antwerp/VIPA/Mons; rq_116 SWA deferred. FOI ready human send. tick166 HR Rail 2.37bn."\n',
    encoding="utf-8",
    newline="\n",
)

log = ROOT / "loop_log.md"
entry = f"""
### {TS} — tick {TICK}
- Unit: **{UNIT}** (FOI-adjacent hole-fill — **HR Rail NV PR institutional omzet/FTE**)
- Found (medium: Companyweb citing **NBB CBSO** jaarrekening BE0541.691.352; filing class 2026-06-10):
  - **Omzet:** **EUR 2.368bn 2025** (+2.75%) · **2.305bn 2024** · **2.206bn 2023** · **2.078bn 2022**.
  - **FTE:** **27 811 (2025)** · 27 568.5 (2024) · 27 524.5 (2023) · 27 435 (2022).
  - **Resultaat:** ~**1.57m 2025** (pass-through; not a profit centre) · equity **28.3m**.
  - **Brutomarge** ≈ omzet (payroll re-invoice to NMBS+Infrabel under KB 11 Dec 2013).
  - Dual rail stack: NMBS staff count 16 976 (2025 results) ⊂ HR Rail 27.8k (rest mostly Infrabel).
  - Implied ~**85k EUR** omzet/FTE 2025.
- De Lijn full 2025-26 JV / Mons BI2026 / Antwerp register still not newly filled this tick.
- Wrote: sources 1; entity 1; budgets 21; cmt 1; lb 2; FOI **gap_hr_rail_charge_matrix** ready; gap_infrabel note; rq_161=done; seeded **rq_162**.
- FOI: human send gap_hr_rail (NBB PDF + charge L5) + residual De Lijn/Infrabel/NMBS.
- Next: prio5 **rq_162**; deferred **rq_116** SWA.
"""
lt = log.read_text(encoding="utf-8")
if not lt.endswith("\n"):
    lt += "\n"
log.write_text(lt + entry, encoding="utf-8", newline="\n")
print("tick166 OK", omzet[2025], fte[2025])
