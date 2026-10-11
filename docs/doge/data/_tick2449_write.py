from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2449_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_familia_jr2025_nbb_pdf_2449"
SRC_KBO="src_familia_kbo_2449"
SRC_SBM="src_familia_sbm_2449"
SRC_SITE="src_familia_site_2449"
GAP="gap_familia_opgroeien_matrix_opbr_7_57m_omzet_1_25m_73_6_23m_pnl_jump_645k_destin_jump_462k_l5"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Kinderdagverblijf Familia deposit 2026-00272867,http://cdn.staatsbladmonitor.be/2026pdf/2026-00272867.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2449; official native PDF 442417 bytes 44p VOL-VZW 26.0.15 m05-f; header 09.07.2026; AV 15.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-28; CreationDate 2026-07-09 13:46:23 UTC OpenPDF 1.3.26; all 44p native; VOL-VZW 6.2.1 6.2.2 6.2.3 6.2.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.13 6.14 6.16 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf Familia 0461.401.779,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0461401779,KBO Public Search FOD Economie,{DAY},official_register,tick2449; Actief; 1 VE 2.150.823.362; VZW since 18.09.1997; begindatum 18.09.1997; zetel Halmstraat 3 3600 Genk since 07.09.1999; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ2025 88.911; FOI info@kdvfamilia.be; leftover mined city_genk CIK; NOT BKO GENK-OOST 0475.432.830; NOT Peutertuinen GO Mariakerke; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Kinderdagverblijf Familia 0461401779 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0461401779,NBB Consult,{DAY},official_register,tick2449; deposit-id 2026-00272867 YE 30/12/2025 filing 09/07/2026 VOL-VZW Volledig Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Kinderdagverblijf Familia FOI contact leftover city_genk CIK,https://kdvfamilia.be,VZW Kinderdagverblijf Familia leftover city_genk CIK,{DAY},foi_contact,tick2449; FOI info@kdvfamilia.be; zetel Halmstraat 3 3600 Genk; leftover mined city_genk after BKO GENK-OOST; 1 VE; NOT Kloosterstraat 6 Drongen; NOT BKO GENK-OOST remine; NOT Peutertuinen GO Mariakerke remine; NOT Mini-creches GO Next Hasselt; NOT t Sloeberke YE2024; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels",
])
print("sources ok")
