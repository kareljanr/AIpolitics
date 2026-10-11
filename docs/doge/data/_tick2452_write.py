from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2452_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_harlekijntjes_jr2025_nbb_pdf_2452"
SRC_KBO="src_harlekijntjes_kbo_2452"
SRC_SBM="src_harlekijntjes_sbm_2452"
SRC_SITE="src_harlekijntjes_site_2452"
GAP="gap_harlekijntjes_opgroeien_matrix_bruto_1_90m_omzet73_empty_pnl_drop_144k_destin_jump_662k_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 KINDEROPVANG De Harlekijntjes deposit 2026-00161949,http://cdn.staatsbladmonitor.be/2026pdf/2026-00161949.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2452; official native PDF 50965 bytes 14p VKT-VZW 26.0.12 m04-f; header 11.06.2026; AV 02.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-20; CreationDate 2026-06-16 01:08:00 UTC OpenPDF 1.3.26; all 14p native; VKT-VZW 6.1.3 6.3 6.5 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO KINDEROPVANG De Harlekijntjes 0407.700.403,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0407700403,KBO Public Search FOD Economie,{DAY},official_register,tick2452; Actief; 1 VE 2.153.760.185; VZW since 10.11.1970; begindatum 10.11.1970; zetel Keidamstraat 77 8700 Tielt since 01.01.2025 technical; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ2025 88.911; FOI info@deharlekijntjes.be; leftover mined city_tielt CIK; NOT Hartjes Ninove 0446.391.327; NOT Hartjes Tienen 0441.374.348; NOT OKO & ZO 0862.154.608; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche KINDEROPVANG De Harlekijntjes 0407700403 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0407700403,NBB Consult,{DAY},official_register,tick2452; deposit-id 2026-00161949 YE 31/12/2025 filing 16/06/2026 VKT-VZW Verkort; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},KINDEROPVANG De Harlekijntjes FOI contact leftover city_tielt CIK,https://deharlekijntjes.be,VZW KINDEROPVANG De Harlekijntjes leftover city_tielt CIK,{DAY},foi_contact,tick2452; FOI info@deharlekijntjes.be; zetel Keidamstraat 77 8700 Tielt; leftover mined city_tielt after Kinderdagverblijf De Hartjes Ninove different-KBO skip; 1 VE; NOT Kloosterstraat 6 Drongen; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels",
])
print("sources ok")
