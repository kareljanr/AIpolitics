from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2453_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_oko_zo_jr2025_nbb_pdf_2453"
SRC_KBO="src_oko_zo_kbo_2453"
SRC_SBM="src_oko_zo_sbm_2453"
SRC_SITE="src_oko_zo_site_2453"
GAP="gap_oko_zo_opgroeien_matrix_bruto_914k_omzet73_empty_pnl_flip_15k_destin_empty_l5"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()
def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)
append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 OKO & ZO deposit 2026-00191153,http://cdn.staatsbladmonitor.be/2026pdf/2026-00191153.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2453; official native PDF 52561 bytes 15p VKT-VZW 26.0.15 m04-f; header 24.06.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-07; CreationDate 2026-06-24 08:12:27 UTC OpenPDF 1.3.26; all 15p native; VKT-VZW 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO OKO & ZO 0862.154.608,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0862154608,KBO Public Search FOD Economie,{DAY},official_register,tick2453; Actief; 2 VE 2.157.862.889 + 2.226.538.592; VZW since 29.11.2003; begindatum 11.12.2003; zetel Rotstraat 20 9240 Zele since 22.06.2009; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ2025 88.911; FOI oko@skynet.be; leftover mined city_zele CIK; NOT Harlekijntjes 0407.700.403; NOT Hartjes Ninove 0446.391.327; NOT Hartjes Tienen 0441.374.348; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche OKO & ZO 0862154608 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0862154608,NBB Consult,{DAY},official_register,tick2453; deposit-id 2026-00191153 YE 30/12/2025 filing 24/06/2026 VKT-VZW Verkort; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},OKO & ZO FOI contact leftover city_zele CIK,https://www.oko-en-zo.be,VZW OKO & ZO leftover city_zele CIK,{DAY},foi_contact,tick2453; FOI oko@skynet.be; zetel Rotstraat 20 9240 Zele; leftover mined city_zele after KINDEROPVANG De Harlekijntjes different-KBO skip; 2 VE; NOT Kloosterstraat 6 Drongen; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels",
])
print("sources ok")
