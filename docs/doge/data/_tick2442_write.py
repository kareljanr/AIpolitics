from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2442_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_anemoontje_jr2025_nbb_pdf_2442"
SRC_KBO="src_anemoontje_kbo_2442"
SRC_SBM="src_anemoontje_sbm_2442"
SRC_SITE="src_anemoontje_site_2442"
GAP="gap_anemoontje_opgroeien_matrix_opbr_835k_omzet_137k_73_698k_pnl_jump_105k_destin_jump_598k_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf t Anemoontje deposit 2026-00213975,http://cdn.staatsbladmonitor.be/2026pdf/2026-00213975.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2442; official native PDF 41833 bytes 11p VKT-VZW 26.0.15 m04-f; header 29.06.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-11; CreationDate 2026-06-29 20:21:01 UTC OpenPDF 1.3.26; all 11p native text euros; VKT-VZW 6.1.1 6.1.3 6.5 6.6 6.7 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf t Anemoontje 0413.354.612,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413354612,KBO Public Search FOD Economie,{DAY},official_register,tick2442; Actief; 1 VE 2.150.886.809 Bosstraat 30 3012 Leuven since 03.01.2006; naam Kinderdagverblijf t Anemoontje since 12.03.1979; VZW since 30.08.1973; begindatum 30.08.1973; zetel Bosstraat 30 3012 Leuven since 01.10.1990; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI info@kinderdagverblijfanemoontje.be; NOT Duinhuisjes VE t Anemoontje 2.375.207.425; NOT De Slabbertjes 0411.972.064; NOT Ferm Kinderopvang 0416.117.627; NOT t Eekhoorntje 0414.453.680; NOT Kinderlach 0450.275.186; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche t Anemoontje 0413354612 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0413354612,NBB Consult,{DAY},official_register,tick2442; deposit-id 2026-00213975 YE 31/12/2025 filing 29/06/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},t Anemoontje FOI contact leftover city_leuven CIK,https://www.kinderdagverblijfanemoontje.be/,VZW Kinderdagverblijf t Anemoontje Opgroeien CIK,{DAY},foi_contact,tick2442; FOI info@kinderdagverblijfanemoontje.be; zetel Bosstraat 30 3012 Leuven; leftover mined city_leuven after De Hummeltjes / De Ukkies / De Slabbertjes / De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje; Opgroeien CIK 40 plaatsen; 1 VE Leuven; NOT Kloosterstraat 6 Drongen; NOT Duinhuisjes VE t Anemoontje; NOT De Slabbertjes; NOT Ferm Kinderopvang; NOT Kinderlach; NOT Helan",
])
print("sources ok")
