from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2450_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_hartjes_jr2025_nbb_pdf_2450"
SRC_KBO="src_hartjes_kbo_2450"
SRC_SBM="src_hartjes_sbm_2450"
SRC_SITE="src_hartjes_site_2450"
GAP="gap_hartjes_opgroeien_matrix_opbr_1_59m_omzet_252k_73_1_34m_pnl_jump_154k_destin_jump_154k_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Groepsopvang De Hartjes deposit 2026-00180031,http://cdn.staatsbladmonitor.be/2026pdf/2026-00180031.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2450; official native PDF 51600 bytes 14p VKT-VZW 26.0.15 m04-f; header 22.06.2026; AV 10.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-28; CreationDate 2026-06-22 06:53:51 UTC OpenPDF 1.3.26; all 14p native; VKT-VZW 6.1.1 6.3 6.5 6.6 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Groepsopvang De Hartjes 0441.374.348,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0441374348,KBO Public Search FOD Economie,{DAY},official_register,tick2450; Actief; 1 VE 2.144.427.597; VZW since 30.06.1989; begindatum 30.06.1989; zetel Oude Leuvensestraat 21 3300 Tienen since 30.06.1989; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ2025 88.911; FOI info@dehartjes.be; leftover mined city_tienen CIK; NOT De Hartjes Ninove 0446.391.327; NOT De Wissel 0421.913.376; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Groepsopvang De Hartjes 0441374348 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0441374348,NBB Consult,{DAY},official_register,tick2450; deposit-id 2026-00180031 YE 30/12/2025 filing 22/06/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Groepsopvang De Hartjes FOI contact leftover city_tienen CIK,https://dehartjes.be,VZW Groepsopvang De Hartjes leftover city_tienen CIK,{DAY},foi_contact,tick2450; FOI info@dehartjes.be; zetel Oude Leuvensestraat 21 3300 Tienen; leftover mined city_tienen after De Wissel Tienen-site same-KBO skip; 1 VE; NOT Kloosterstraat 6 Drongen; NOT De Hartjes Ninove remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels",
])
print("sources ok")
