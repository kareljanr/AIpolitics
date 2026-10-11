#!/usr/bin/env python3
"""Surgical tick 2384 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_car_roeselare"
SRC_PDF = "src_car_roeselare_jr2025_nbb_pdf_2384"
SRC_KBO = "src_car_roeselare_kbo_2384"
SRC_SBM = "src_car_roeselare_sbm_2384"
SRC_SITE = "src_car_roeselare_site_2384"
COMM = "comm_car_roeselare_jr2025_statutory_omzet_2_10m_73_414k_cash_2_24m"
LB = "lb_car_roeselare_omzet_2_10m_73_414k_cash_2_24m_jr2025"
GAP = "gap_car_roeselare_riziv_vl_matrix_omzet_2_10m_73_414k_cash_2_24m_destin_empty_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"
if not (ROOT / DRAFT).is_file():
    raise SystemExit("FOI draft missing")


def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)


append_lines(DATA / "sources.csv", [
    f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 CAR Roeselare deposit 2026-00155928,http://cdn.staatsbladmonitor.be/2026pdf/2026-00155928.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2384; official native PDF 47898 bytes 12p VKT-VZW 26.0.12 m04-f; header 12.06.2026; AV 19.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-19; CreationDate 2026-06-12 11:32:18 UTC OpenPDF 1.3.26; euros from native PDF text not SBM table not Companyweb not Belscope",
    f"{SRC_KBO},KBO Centrum voor Ambulante Revalidatie Roeselare vzw 0431.179.054,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431179054,KBO Public Search FOD Economie,{DAY},official_register,tick2384; Actief; 1 VE 2.154.449.479 Revalidatiecentrum voor Taal- en Ontwikkelingsproblemen Jules Lagaelaan 17 8800 Roeselare since 14.06.2006; zetel Jules Lagaelaan 17 8800 Roeselare since 22.07.1999; RSZ2025 86.959; gedelegeerd bestuurder Sabine Seynaeve; dagelijks bestuur Veerle Pelckmans",
    f"{SRC_SBM},Staatsbladmonitor fiche CAR Roeselare 0431179054 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0431179054,Staatsbladmonitor,{DAY},official_register,tick2384; deposit-id 2026-00155928 and CDN Last-Modified 2026-06-19; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},CAR Roeselare FOI contact / Departement Zorg REV953,https://carroeselare.be/,Centrum voor Ambulante Revalidatie Roeselare vzw,{DAY},foi_contact,tick2384; FOI info@carroeselare.be / veerle.pelckmans@carroeselare.be; zetel Jules Lagaelaan 17 8800 Roeselare; leftover city_roeselare; NOT Kloosterstraat 6; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort",
])

append_lines(DATA / "entities.csv", [
    f'{EID},CAR Roeselare VZW (ambulante revalidatie taal- en ontwikkelingsproblemen + gehoor),CAR Roeselare ASBL (revalidation ambulatoire langage et developpement + audition),CAR Roeselare VZW (outpatient rehabilitation language/development + hearing),parastatal,city_roeselare,nl,https://carroeselare.be/,info@carroeselare.be,"Jules Lagaelaan 17, 8800 Roeselare",tick2384 YE2025 Strong official native NBB PDF deposit 2026-00155928 + Strong KBO 0431.179.054 Actief 1 VE RSZ2025 86.959; omzet JUMP 2097478 CAR envelope; bruto JUMP 2215235; 73 JUMP 413808; pnl JUMP 136971; equity JUMP 2697073; assets JUMP 3042841; debt JUMP 345768; FTE 24.3 DROP; kapitaalsubsidies empty; destin691 empty; cash JUMP 2237649; geldbeleggingen JUMP 660000; leftover city_roeselare after Vijvens@2383; AGB/FARO/Gandae YE2024; not TE-additive',
])

append_lines(DATA / "budgets.csv", [
    f"bud_car_roeselare_omzet_jr2025_statutory,{EID},2025,2097478,2097478,2097478,NBB VKT-VZW code 70 omzet YE2025 JUMP +0.54% (primary L5 envelope; CAR RIZIV/Departement Zorg not commercial-only),{SRC_PDF},strong,tick2384; PDF p5 native; YE2024 2086281; 73 413808; bruto 2215235 ~1.06x",
    f"bud_car_roeselare_bruto_jr2025_statutory,{EID},2025,2215235,2215235,2215235,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +0.55%,{SRC_PDF},strong,tick2384; PDF p5 native; YE2024 2203176; 76A empty",
    f"bud_car_roeselare_subs73_jr2025_statutory,{EID},2025,413808,413808,413808,NBB VKT-VZW code 73 lidgeld schenkingen legaten subsidies YE2025 JUMP +8.06%,{SRC_PDF},strong,tick2384; PDF p5 native; YE2024 382931",
    f"bud_car_roeselare_pnl_jr2025_statutory,{EID},2025,136971,136971,136971,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +10.39%,{SRC_PDF},strong,tick2384; PDF p5 native; YE2024 124083; bedrijfswinst 9901 106316 JUMP vs YE2024 100464; destin691 empty",
    f"bud_car_roeselare_equity_jr2025_statutory,{EID},2025,2697073,2697073,2697073,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.35%,{SRC_PDF},strong,tick2384; PDF p4 native; YE2024 2560102; kapitaalsubsidies empty; overgedragen 14 1352156; fondsen 10 1344917; bestemde 13 empty",
    f"bud_car_roeselare_assets_jr2025_statutory,{EID},2025,3042841,3042841,3042841,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +4.97%,{SRC_PDF},strong,tick2384; PDF p3 native; YE2024 2898686",
    f"bud_car_roeselare_debt_jr2025_statutory,{EID},2025,345768,345768,345768,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +2.12%,{SRC_PDF},strong,tick2384; PDF p4 native; YE2024 338584; LT empty; ST 345556; handel 30986; sociaal 263481",
    f"bud_car_roeselare_cash_jr2025_statutory,{EID},2025,2237649,2237649,2237649,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +1.12%,{SRC_PDF},strong,tick2384; PDF p3 native; YE2024 2212885; geldbeleggingen 50/53 660000 JUMP vs 400000",
    f"bud_car_roeselare_beleggingen_jr2025_statutory,{EID},2025,660000,660000,660000,NBB VKT-VZW code 50/53 geldbeleggingen YE2025 JUMP +65.00%,{SRC_PDF},strong,tick2384; PDF p3 native; YE2024 400000; kapitaalsubsidies 15 empty",
    f"bud_car_roeselare_fte_jr2025_statutory,{EID},2025,24.3,24.3,24.3,NBB VKT-VZW gemiddeld personeelseffectief VTE YE2025 24.3 DROP -0.82%,{SRC_PDF},strong,tick2384; PDF p9 native; YE2024 24.5; koppen 105 23.3 VTE year-end 2 VT+34 PT; personnel 62 1989857; uitzend empty",
])

cash_json = (
    '"{""2025_omzet"":2097478,""2025_bruto"":2215235,""2025_73"":413808,'
    '""2025_pnl"":136971,""2025_bedrijfswinst"":106316,""2025_equity"":2697073,'
    '""2025_assets"":3042841,""2025_debt"":345768,""2025_fte"":24.3,'
    '""2025_kapitaalsubsidies"":0,""2025_destin691"":0,""2025_cash"":2237649,'
    '""2025_geldbeleggingen"":660000,""2025_personnel62"":1989857,'
    '""2025_gebouwen22"":788,""2025_aanbouw27"":0,'
    '""2025_capex8169"":5731,""2025_fondsen10"":1344917,'
    '""2025_bestemde13"":0,""2025_overgedragen14"":1352156,'
    '""2025_fin_opbr75"":31334,""2025_diensten6061"":304785,'
    '""2024_omzet"":2086281,""2024_bruto"":2203176,'
    '""2024_73"":382931,""2024_pnl"":124083,""2024_bedrijfswinst"":100464,'
    '""2024_equity"":2560102,""2024_assets"":2898686,""2024_debt"":338584,'
    '""2024_kapitaalsubsidies"":0,""2024_cash"":2212885,""2024_fte"":24.5,'
    '""2024_destin691"":0,""2024_geldbeleggingen"":400000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR Roeselare vzw YE2025 (omzet 2.10m / 73 414k / cash 2.24m / destin empty / Strong PDF),{EID},RIZIV + Departement Zorg + leftover city_roeselare,VZW CAR Roeselare (KBO 0431.179.054; Actief; 1 VE; RSZ2025 86.959),2026-06-12,2025,2025,2097478,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00155928.pdf,Public CAR dual of mined city_roeselare,Publish RIZIV/VL matrix inside omzet 2.10m + explain 73 414k JUMP + cash 2.24m + beleggingen 660k vs gebouwen 788 + destin empty + kapitaalsubsidies empty,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Roeselare>CAR_Roeselare>JR2025_statutory_L5,tick2384; Strong official native PDF; leftover city_roeselare after Vijvens@2383; NOT Kloosterstraat 6; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR Roeselare omzet 2.10m / 73 414k / cash 2.24m / destin empty (YE2025 Roeselare),L5,car_vzw_statutory,Vlaanderen>West-Vlaanderen>Roeselare>CAR_Roeselare>JR2025,2097478,2097478,PDF omzet JUMP 2097478 CAR envelope; bruto JUMP 2215235 ~1.06x; 73 JUMP 413808; bedrijfswinst JUMP 106316; pnl JUMP 136971; equity JUMP 2697073; assets JUMP 3042841; debt JUMP 345768; FTE 24.3 DROP; kapitaalsubsidies empty; destin691 empty; cash JUMP 2237649; geldbeleggingen JUMP 660000; gebouwen 788; capex 5731; personnel 1989857,strong,{SRC_PDF},children with developmental/hearing disorders + adults with hearing loss Roeselare,RIZIV + Departement Zorg + leftover city_roeselare,2.10m CAR omzet; 414k 73 subsidies JUMP; cash 2.24m + beleggingen 660k vs gebouwen 788; destin empty; kapitaalsubsidies empty; leftover city_roeselare,5.5,5.1,5.2,5.22,FOI RIZIV/VL matrix + 73 414k JUMP + cash 2.24m + beleggingen 660k vs gebouwen 788 + destin empty + kapitaalsubsidies empty,active,,tick2384; Strong official NBB native PDF + Strong KBO; leftover city_roeselare after Vijvens@2383; OFF Drongen OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>West-Vlaanderen>Roeselare>CAR_Roeselare>RIZIV_VL_CAR,{EID},RIZIV/Departement Zorg split inside omzet 2097478; why 73 413808 JUMP; why cash 2237649 + beleggingen 660000 vs gebouwen 788; nature of destin 691 empty and kapitaalsubsidies 15 empty while overgedragen 14 1352156; pnl JUMP 136971; FTE DROP 24.3,Strong official PDF leftover public CAR of city_roeselare; 2.10m omzet; public not private clinic,8,Centrum voor Ambulante Revalidatie Roeselare VZW / Sabine Seynaeve gedelegeerd bestuurder,info@carroeselare.be,"Jules Lagaelaan 17, 8800 Roeselare",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2384; ready NOT sent; Strong official native NBB PDF; leftover city_roeselare CAR after Vijvens@2383; off Drongen off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal; AGB/FARO/Gandae still YE2024',
])

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
if b"\r\n" in rq_raw:
    raise SystemExit("research_queue has CRLF; abort to avoid rewrite")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2384,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2384 line, found {n}")
if "rq_2385," in rq_text:
    raise SystemExit("rq_2385 already exists")

new_2384 = (
    "rq_2384,leftover dual — CAR Roeselare YE2025 Strong (omzet JUMP 2.10m / 73 414k / cash 2.24m / destin empty),"
    "hole_fill,8,done,L5,vzw_car_roeselare,"
    "Tick 2384 leftover after Vijvens. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC; NOT Heropbeuring; NOT Floordam; NOT Sint-Vincentius Zulte; NOT H.Hart Oudenaarde; NOT CAR DAT; NOT Vijvens). "
    "Took CAR Roeselare 0431.179.054 deposit 2026-00155928 leftover city_roeselare. "
    "Do NOT redo Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. Zwarte Zusters 0413.272.260 stopgezet skip. DCGZ empty skip; Steunfonds absorbed.,"
    f"{GAP},2026-08-24T23:45:46Z,{STAMP},"
    "tick2384 CAR Roeselare 0431.179.054 YE2025 Strong official native PDF 2026-00155928; omzet JUMP 2097478 CAR envelope; bruto JUMP 2215235; 73 JUMP 413808; pnl JUMP 136971; equity JUMP 2697073; assets JUMP 3042841; debt JUMP 345768; FTE 24.3 DROP; kapitaalsubsidies empty; destin691 empty; cash JUMP 2237649; geldbeleggingen JUMP 660000; FOI ready NOT sent; leftover city_roeselare after Vijvens@2383; OFF Drongen OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2384,"):
        parts.append(new_2384)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2384 replace count {replaced}")
new_rq = "".join(parts)
new_2385 = (
    "rq_2385,leftover dual after CAR Roeselare — hunt unused public dual elsewhere,"
    "hole_fill,8,open,L5,,"
    "After CAR Roeselare YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Kloosterstraat 6; NOT Sint-Lievenspoort; NOT Inkendaal; NOT Pulderbos; NOT MKL; NOT NMSC 0410.338.110; NOT Heropbeuring 0406.678.141; NOT Floordam 0428.792.557; NOT Sint-Vincentius Zulte 0448.633.413; NOT H.Hart Oudenaarde 0407.644.082; NOT CAR DAT 0463.347.917; NOT Vijvens 0415.093.385; NOT CAR Roeselare 0431.179.054). "
    "Do NOT redo CAR Roeselare/Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/CAR Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack. "
    "Named+unnamed Drongen CARs exhausted. Zwarte Zusters stopgezet skip. DCGZ empty skip; Steunfonds absorbed. Zeepreventorium still YE2024. De Bolster still YE2024. Next every-10 is 2390.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2384; CAR Roeselare taken leftover city_roeselare after Vijvens; AGB/FARO/Gandae still YE2024; next every-10 2390\n"
)
new_rq = new_rq + new_2385
rq_path.write_bytes(new_rq.encode("utf-8"))
print("patched research_queue rq_2384 + rq_2385; bytes", rq_path.stat().st_size)

state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2384,2384,no,"
    "tick2384 leftover dual CAR Roeselare 0431.179.054 Strong native PDF (omzet JUMP 2097478 CAR envelope; bruto JUMP 2215235; 73 JUMP 413808; pnl JUMP 136971; equity JUMP 2697073; assets JUMP 3042841; debt JUMP 345768; FTE 24.3 DROP; kapitaalsubsidies empty; destin691 empty; cash JUMP 2237649; geldbeleggingen JUMP 660000; 1 VE RSZ2025 86.959); leftover city_roeselare after Vijvens@2383; OFF Drongen OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal; AGB/FARO/Gandae YE2024; next rq_2385; next every-10 2390\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2384 - rq_2384 CAR Roeselare (omzet JUMP 2.10m / 73 414k / cash 2.24m / destin empty / Strong PDF)

- Unit: **rq_2384** leftover dual after **Vijvens@2383**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only; not re-downloaded); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Zeepreventorium still **YE2024**. De Bolster 0861.680.989 still **YE2024**. Zwarte Zusters 0413.272.260 **stopgezet 26.06.2000** (skip). Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Took FREE leftover Flemish **Centrum voor Ambulante Revalidatie Roeselare VZW (CAR Roeselare)** YE2025 (KBO **0431.179.054**; zetel Jules Lagaelaan 17, 8800 Roeselare; **Actief** **1 VE** **2.154.449.479** Revalidatiecentrum voor Taal- en Ontwikkelingsproblemen; RSZ2025 **86.959**; Departement Zorg REV953 / HCO 29612; leftover of mined **city_roeselare@1276**; info@carroeselare.be). Confirmed leftover public (Departement Zorg CAR + RIZIV ambulante revalidatie children developmental/hearing + adults hearing) not private clinic / not Vijvens 0415.093.385 / not CAR DAT 0463.347.917 / not H.Hart 0407.644.082 / not Sint-Vincentius Zulte / not Floordam / not NMSC. Do not redo Vijvens/CAR DAT/H.Hart Oudenaarde/Sint-Vincentius Zulte/Floordam/Heropbeuring/NMSC/MKL/Pulderbos/Inkendaal/Sint-Lievenspoort/Buggenhout/Impuls/Bolt/Mozaiek/DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg.
- Found: official NBB VKT-VZW native PDF deposit **2026-00155928** (47898 B / 12p; AV **19.05.2026**; header **12.06.2026**; CDN Last-Modified **19.06.2026**) — omzet 70 **EUR2097478** JUMP +0.54% (CAR envelope; not commercial-only); bruto 9900 **EUR2215235** JUMP +0.55% (~**1.06x**); 73 **EUR413808** JUMP +8.06%; bedrijfswinst 9901 **EUR106316** JUMP +5.83%; pnl 9904 **EUR136971** JUMP +10.39%; equity **EUR2697073** JUMP +5.35%; assets **EUR3042841** JUMP +4.97%; debt **EUR345768** JUMP +2.12%; FTE **24.3** DROP −0.82%; kapitaalsubsidies **empty**; destin 691 **empty**; cash **EUR2237649** JUMP +1.12%; geldbeleggingen **EUR660000** JUMP +65.00%; gebouwen **EUR788**; aanbouw empty; capex **EUR5731**; personeel 62 **EUR1989857**. Strong KBO + Strong PDF (native text; not SBM table; not Companyweb euros; smaller than CAR DAT 51k / Vijvens 3.1MB / Heropbeuring 9MB / NMSC 17MB / Inkendaal 28MB).
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.22); entities (+1 vzw_car_roeselare); foi + draft `{GAP}`; rq_2384=done + rq_2385 open; loop_state ticks=2384; raw tick2384/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2390**). Next: rq_2385 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT CAR Roeselare / NOT Vijvens / NOT CAR DAT / NOT H.Hart Oudenaarde / NOT Sint-Vincentius Zulte / NOT Floordam / NOT Heropbeuring / NOT NMSC / NOT MKL / NOT Pulderbos / NOT Inkendaal / NOT Sint-Lievenspoort / NOT Kloosterstraat 6). Candidate leftover CAR Overleie Kortrijk 0454.250.505 leftover city_kortrijk only if live 2026pdf (Companyweb last filing 03.09.2025 may still be YE2024). De Bolster 0861.680.989 still YE2024 public file. School Perk 0417.085.845 only if leftover school of mined parent is in priority. Zeepreventorium still YE2024.
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
