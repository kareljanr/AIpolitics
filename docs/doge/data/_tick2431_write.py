from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2431_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_witje_wiebel_jr2025_nbb_pdf_2431"
SRC_KBO="src_witje_wiebel_kbo_2431"
SRC_SBM="src_witje_wiebel_sbm_2431"
SRC_SITE="src_witje_wiebel_site_2431"
GAP="gap_witje_wiebel_opgroeien_matrix_bruto_1_88m_omzet73_empty_pnl_jump_301k_destin_300k_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 KINDERDAGVERBLIJF WITJE WIEBEL deposit 2026-00143338,http://cdn.staatsbladmonitor.be/2026pdf/2026-00143338.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2431; official native PDF 50509 bytes 13p VKT-VZW 26.0.12 m04-f; header 08.06.2026; AV 01.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-12; CreationDate 2026-06-08 14:20:42 UTC OpenPDF 1.3.26; all 13p native text; PDF-Verkort is native euros not scan; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO KINDERDAGVERBLIJF WITJE WIEBEL 0443.654.937,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443654937,KBO Public Search FOD Economie,{DAY},official_register,tick2431; Actief; 2 VE 2.150.816.533 Kortrijksesteenweg 1020 9000 Gent since 03.01.2006 + 2.152.579.656 Smidsestraat 88 9000 Gent since 30.03.2006; naam KINDERDAGVERBLIJF WITJE WIEBEL since 24.01.2003; VZW since 06.12.1990; begindatum 06.12.1990; zetel Kortrijksesteenweg 1020 9000 Gent since 11.03.2020; RSZ2025 88.911; RSZ-werkgever since 17.12.1990; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI witje.wiebel@mijnziekenhuis.be; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Duinhuisjes 0413.323.037; NOT t Bremhuisje 0445.265.533 stopgezet 1993; NOT Kinderlach 0450.275.186; NOT KISME 0894.549.440; NOT Kindercentrum 0408.226.775; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche Witje Wiebel 0443654937 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0443654937,NBB Consult,{DAY},official_register,tick2431; deposit-id 2026-00143338 YE 31/12/2025 filing header 08/06/2026 VKT-VZW PDF-Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Witje Wiebel FOI contact leftover city_gent CIK,https://witjewiebel.be/,VZW KINDERDAGVERBLIJF WITJE WIEBEL,{DAY},foi_contact,tick2431; FOI witje.wiebel@mijnziekenhuis.be / witje.wiebel.csp@telenet.be; zetel Kortrijksesteenweg 1020 9000 Gent; leftover mined city_gent after Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 2 VE campus Maria Middelares + campus Sint-Pieters same KBO; NOT Kloosterstraat 6 Drongen; NOT Beregoed; NOT Windekind; NOT Elfenbankje; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Duinhuisjes; NOT t Bremhuisje stopgezet 1993",
])
print("sources ok")
