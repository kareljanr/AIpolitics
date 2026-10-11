from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2436_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_avida_jr2025_nbb_pdf_2436"
SRC_KBO="src_avida_kbo_2436"
SRC_SBM="src_avida_sbm_2436"
SRC_SITE="src_avida_site_2436"
GAP="gap_avida_wzc_matrix_omzet_42_86m_73_11_55m_pnl_drop_784k_destin_0_l5"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Avida deposit 2026-00206951,http://cdn.staatsbladmonitor.be/2026pdf/2026-00206951.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2436; official native PDF 803924 bytes 54p VOL-VZW 25.0.13 m05-f; header 24.06.2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-10; CreationDate 2026-06-27 03:20:42 UTC OpenPDF 1.3.26; all 54p native text euros; commissarisverslag pp.47-54 native oordeel zonder voorbehoud NV Callens Vandelanotte Kris Igodt 03.06.2026; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Avida 0438.814.241,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0438814241,KBO Public Search FOD Economie,{DAY},official_register,tick2436; Actief; 7 VE 2.150.811.484 Avida Sint-Jozef Molenaarsstraat 34 9000 Gent since 03.01.2006 + 2.298.033.235 Avida Sint-Vincentius Lochristi + 2.298.033.433 Avida Morgenster Damme + 2.298.033.631 Avida Focusplus Gent + 2.369.111.370 Avida Ter Hovingen Gent + 2.369.111.964 Avida Heilige Familie Beveren-Kruibeke-Zwijndrecht + 2.369.112.162 Avida OLV-ter-Rive Gent; naam Avida since 11.12.2024 (voorheen Exalta); VZW since 31.01.1989; begindatum 31.01.1989; zetel Molenaarsstraat 34 9000 Gent since 22.03.2001; RSZ2025 87.101; BTW2025 87.301; CONECTO 0433.961.964 opgeslorpt since 01.01.2025; FOI info@avida.be; NOT WZC Sint-Coleta Gent 0448.294.507; NOT Home Emmaus 0451.749.190; NOT De Foyer 0413.796.456; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche Avida 0438814241 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0438814241,NBB Consult,{DAY},official_register,tick2436; deposit-id 2026-00206951 YE 31/12/2025 filing 24/06/2026 VOL-VZW Volledig Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Avida FOI contact leftover city_gent WZC,https://www.avida.be/,VZW Avida Woonzorggroep,{DAY},foi_contact,tick2436; FOI info@avida.be; zetel Molenaarsstraat 34 9000 Gent; leftover mined city_gent after IZW / Ferm Kinderopvang / WZC Sint-Coleta Gent / Home Emmaus / Witje Wiebel / Beregoed / Windekind / Elfenbankje / AGB Kunsten / AGB Erfgoed; 7 VE Gent+Lochristi+Damme+Beveren same KBO; RVT/ROB; Conecto+Exalta merger 01.01.2025; NOT Kloosterstraat 6 Drongen; NOT WZC Sint-Coleta Gent; NOT Home Emmaus; NOT De Foyer; NOT Groep Zorg H. Familie; NOT Helan",
])
print("sources ok")
