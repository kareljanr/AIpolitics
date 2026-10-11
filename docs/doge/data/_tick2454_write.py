from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2454_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_medemens_kdv_jr2025_nbb_pdf_2454"
SRC_KBO="src_medemens_kdv_kbo_2454"
SRC_SBM="src_medemens_kdv_sbm_2454"
SRC_SITE="src_medemens_kdv_site_2454"
GAP="gap_medemens_kdv_opgroeien_matrix_opbr_9_55m_omzet_1_76m_73_7_57m_pnl_drop_500k_destin_jump_5_67m_l5"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 De Medemens Kinderdagverblijven deposit 2026-00206605,http://cdn.staatsbladmonitor.be/2026pdf/2026-00206605.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2454; official native PDF 2267541 bytes 52p VOL-VZW 25.0.13 m05-f; header 25.06.2026; AV 17.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-10; CreationDate 2026-06-27 01:49:18 UTC OpenPDF 1.3.26; all 52p native; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.3.5 6.4.1 6.4.2 6.5.1 6.5.2 6.13 6.16 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO De Medemens Kinderdagverblijven 0893.678.915,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0893678915,KBO Public Search FOD Economie,{DAY},official_register,tick2454; Actief; 9 VE; VZW since 07.11.2007; begindatum 23.11.2007; zetel Lokkaardstraat 10 2018 Antwerpen since 22.06.2023; toelating Kinderopvang Vlaamse Gemeenschap since 08.03.2017; RSZ2025 88.911; aanbestedende overheid; FOI yonca.albayrak@demedemens.be; leftover mined city_antwerpen CIK; NOT De Medemens parent 0428.692.191 remine; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche De Medemens Kinderdagverblijven 0893678915 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0893678915,NBB Consult,{DAY},official_register,tick2454; deposit-id 2026-00206605 YE 31/12/2025 filing 27/06/2026 VOL-VZW; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},De Medemens Kinderdagverblijven FOI contact leftover city_antwerpen CIK,https://www.demedemens.be/aanbod/kinderopvang,VZW De Medemens Kinderdagverblijven leftover city_antwerpen CIK,{DAY},foi_contact,tick2454; FOI yonca.albayrak@demedemens.be; zetel Lokkaardstraat 10 2018 Antwerpen; leftover mined city_antwerpen after OKO & ZO different-KBO skip; 9 VE Antwerp-region CIK; NOT Kloosterstraat 6 Drongen; NOT De Medemens 0428.692.191 remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels",
])
print("sources ok")
