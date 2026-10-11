from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2433_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_sint_coleta_jr2025_nbb_pdf_2433"
SRC_KBO="src_sint_coleta_kbo_2433"
SRC_SBM="src_sint_coleta_sbm_2433"
SRC_SITE="src_sint_coleta_site_2433"
GAP="gap_sint_coleta_wzc_matrix_omzet_5_61m_73_983k_pnl_drop_75k_destin_0_l5"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 WZC SINT-COLETA GENT deposit 2026-00192499,http://cdn.staatsbladmonitor.be/2026pdf/2026-00192499.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2433; official native PDF 652522 bytes 45p VOL-VZW 26.0.15 m05-f; header 22.06.2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-07; CreationDate 2026-06-24 14:01:26 UTC OpenPDF 1.3.26; all 45p native text euros; commissarisverslag pp.42-45 native; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO WZC SINT-COLETA GENT 0448.294.507,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0448294507,KBO Public Search FOD Economie,{DAY},official_register,tick2433; Actief; 1 VE 2.156.526.863 Sint-Coletastraat 4 9000 Gent since 09.10.2006; naam WOON- EN ZORGCENTRUM SINT-COLETA GENT since 26.11.2001; VZW since 15.06.1992; begindatum 15.06.1992; zetel Sint-Coletastraat 4 9000 Gent since 26.04.2007; RSZ2025 87.101; RSZ-werkgever since 01.01.2006; FOI info@sintcoleta.be; NOT Home Emmaus 0451.749.190; NOT De Foyer 0413.796.456; NOT Emmaus AZ 0411.515.075; NOT Witje Wiebel 0443.654.937; NOT Beregoed 0447.515.042; NOT Windekind 0431.806.386; NOT Elfenbankje 0417.638.151; NOT Vormingscentrum 0413.342.338; NOT Helan 0464.151.037; NOT Knuffelboom 0478.310.859; NOT De Zeppelin 0454.001.867; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche WZC Sint-Coleta Gent 0448294507 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0448294507,NBB Consult,{DAY},official_register,tick2433; deposit-id 2026-00192499 YE 30/12/2025 filing header 22/06/2026 VOL-VZW Volledig Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},WZC Sint-Coleta Gent FOI contact leftover city_gent WZC,https://www.sintcoleta.be/,VZW Woon- en Zorgcentrum Sint-Coleta Gent,{DAY},foi_contact,tick2433; FOI info@sintcoleta.be; zetel Sint-Coletastraat 4 9000 Gent; leftover mined city_gent after Home Emmaus / Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 1 VE Gent same KBO; RVT/ROB; NOT Kloosterstraat 6 Drongen; NOT Home Emmaus; NOT De Foyer; NOT Emmaus AZ; NOT Witje Wiebel; NOT Beregoed; NOT Windekind; NOT Elfenbankje; NOT Vormingscentrum; NOT Helan Kinderopvang; NOT Knuffelboom no NBB; NOT De Zeppelin no jaarrekening",
])
print("sources ok")
