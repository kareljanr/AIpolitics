from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2432_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_home_emmaus_jr2025_nbb_pdf_2432"
SRC_KBO="src_home_emmaus_kbo_2432"
SRC_SBM="src_home_emmaus_sbm_2432"
SRC_SITE="src_home_emmaus_site_2432"
GAP="gap_home_emmaus_vaph_matrix_opbr_2_23m_omzet_279k_73_1_95m_pnl_jump_271k_destin_0_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 HOME EMMAUS deposit 2026-00339558,http://cdn.staatsbladmonitor.be/2026pdf/2026-00339558.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2432; official native PDF 2816973 bytes 19p VKT-VZW 23.0.10 m04-f; header 28.07.2026; AV 02.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-08-05; CreationDate 2026-07-28 08:40:07 UTC OpenPDF 1.3.26; pp.1-14 native text euros; pp.15-19 commissaris scan empty text; PDF-Verkort native euros not scan; prior-year restated on same PDF; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO HOME EMMAUS 0451.749.190,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0451749190,KBO Public Search FOD Economie,{DAY},official_register,tick2432; Actief; 1 VE 2.156.748.775 Van den Heckestraat 41-43 9050 Gent since 16.10.2006; naam Home Emmaus since 14.12.1993; VZW since 14.12.1993; begindatum 14.12.1993; zetel Van den Heckestraat 41-43 9050 Gent since 14.12.1993; RSZ2025 88.104; RSZ-werkgever since 15.02.1994; FOI boekhouding@dovencentrum-emmaus.be; NOT Emmaus AZ 0411.515.075; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Knuffelboom 0478.310.859; NOT De Zeppelin 0454.001.867; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche Home Emmaus 0451749190 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0451749190,NBB Consult,{DAY},official_register,tick2432; deposit-id 2026-00339558 YE 30/12/2025 filing header 28/07/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Home Emmaus FOI contact leftover city_gent VAPH,https://dovencentrum-emmaus.be/,VZW Home Emmaus / Compagnie Emmaus,{DAY},foi_contact,tick2432; FOI boekhouding@dovencentrum-emmaus.be / info@dovencentrum-emmaus.be; zetel Van den Heckestraat 41-43 9050 Gent; leftover mined city_gent after Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 1 VE Gent-Ledeberg same KBO; VAPH-erkend dagcentrum + woonondersteuning; NOT Kloosterstraat 6 Drongen; NOT Emmaus AZ; NOT Witje Wiebel; NOT Beregoed; NOT Windekind; NOT Elfenbankje; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Knuffelboom no NBB; NOT De Zeppelin no jaarrekening",
])
print("sources ok")
