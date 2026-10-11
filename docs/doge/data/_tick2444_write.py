from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2444_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_wigwam_jr2025_nbb_pdf_2444"
SRC_KBO="src_wigwam_kbo_2444"
SRC_SBM="src_wigwam_sbm_2444"
SRC_SITE="src_wigwam_site_2444"
GAP="gap_wigwam_opgroeien_matrix_bruto_1_07m_omzet73_empty_pnl_drop_36_destin_jump_150k_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 KDV Wigwam deposit 2026-00159445,http://cdn.staatsbladmonitor.be/2026pdf/2026-00159445.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2444; official native PDF 57177 bytes 17p VKT-VZW 26.0.12 m04-f; header 11.06.2026; AV 11.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-20; CreationDate 2026-06-15 08:43:33 UTC OpenPDF 1.3.26; all 17p native; VKT-VZW 6.1.3 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Wigwam 0435.015.207,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0435015207,KBO Public Search FOD Economie,{DAY},official_register,tick2444; Actief; 1 VE 2.155.773.431 Diestsesteenweg 379/c 3010 Leuven since 28.08.2006; naam Wigwam since 26.06.2003; VZW since 08.06.1984; begindatum 08.06.1984; zetel Diestsesteenweg 379c 3010 Leuven since 01.11.2016; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI info@dewigwam.be; leftover mined city_leuven CIK; NOT t Anemoontje 0413.354.612; NOT De Slabbertjes 0411.972.064; NOT Ferm Kinderopvang 0416.117.627; NOT t Eekhoorntje 0414.453.680; NOT De Wissel 0421.913.376; NOT Monte Rosa 0413.350.751; NOT IZW 0430.278.439; NOT Jeugdhulp Don Bosco 0408.666.344; NOT Kinderlach 0450.275.186; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Wigwam 0435015207 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0435015207,NBB Consult,{DAY},official_register,tick2444; deposit-id 2026-00159445 YE 31/12/2025 filing 11/06/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Wigwam FOI contact leftover city_leuven CIK,https://www.dewigwam.be/,VZW Wigwam Opgroeien CIK,{DAY},foi_contact,tick2444; FOI info@dewigwam.be; zetel Diestsesteenweg 379c 3010 Leuven; leftover mined city_leuven after Jeugdhulp Don Bosco / t Anemoontje / De Slabbertjes / De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje; 1 VE 45 Opgroeien plaatsen; NOT Kloosterstraat 6 Drongen; NOT t Anemoontje; NOT De Slabbertjes; NOT Ferm; NOT Helan; NOT Kinderlach",
])
print("sources ok")
