from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2451_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_hartjes_ninove_jr2025_nbb_pdf_2451"
SRC_KBO="src_hartjes_ninove_kbo_2451"
SRC_SBM="src_hartjes_ninove_sbm_2451"
SRC_SITE="src_hartjes_ninove_site_2451"
GAP="gap_hartjes_ninove_opgroeien_matrix_bruto_484k_omzet73_empty_pnl_jump_31k_destin_empty_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf De Hartjes Ninove deposit 2026-00170536,http://cdn.staatsbladmonitor.be/2026pdf/2026-00170536.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2451; official native PDF 45187 bytes 11p VKT-VZW 23.0.9 m04-f; header 11.06.2026; AV 11.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-21; CreationDate 2026-06-18 06:59:48 UTC OpenPDF 1.3.26; all 11p native; VKT-VZW 6.1.1 6.1.3 6.2 6.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf De Hartjes Ninove 0446.391.327,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0446391327,KBO Public Search FOD Economie,{DAY},official_register,tick2451; Actief; 1 VE 2.159.645.117; VZW since 09.12.1991; begindatum 09.12.1991; zetel Onderwijslaan 14 9400 Ninove since 09.12.1991; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ2025 88.911; FOI info@dehartjesninove.be; leftover mined city_ninove CIK; NOT Groepsopvang De Hartjes Tienen 0441.374.348; NOT De Wissel 0421.913.376; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Kinderdagverblijf De Hartjes Ninove 0446391327 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0446391327,NBB Consult,{DAY},official_register,tick2451; deposit-id 2026-00170536 YE 31/12/2025 filing 18/06/2026 VKT-VZW Verkort; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Kinderdagverblijf De Hartjes Ninove FOI contact leftover city_ninove CIK,https://dehartjesninove.be,VZW Kinderdagverblijf De Hartjes leftover city_ninove CIK,{DAY},foi_contact,tick2451; FOI info@dehartjesninove.be; zetel Onderwijslaan 14 9400 Ninove; leftover mined city_ninove after Groepsopvang De Hartjes Tienen different-KBO skip; 1 VE; NOT Kloosterstraat 6 Drongen; NOT De Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels",
])
print("sources ok")
