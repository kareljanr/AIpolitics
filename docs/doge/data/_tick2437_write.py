from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2437_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_monte_rosa_jr2025_nbb_pdf_2437"
SRC_KBO="src_monte_rosa_kbo_2437"
SRC_SBM="src_monte_rosa_sbm_2437"
SRC_SITE="src_monte_rosa_site_2437"
GAP="gap_monte_rosa_opgroeien_matrix_opbr_5_42m_omzet_empty_73_5_32m_pnl_jump_349k_destin_2_05m_l5"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Monte Rosa deposit 2026-00093041,http://cdn.staatsbladmonitor.be/2026pdf/2026-00093041.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2437; official native PDF 232744 bytes 31p VOL-VZW 26.0.10 m05-f; header 29.04.2026; AV 23.04.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-05-01; CreationDate 2026-04-29 16:28:35 UTC OpenPDF 1.3.26; all 31p native text euros; jaarverslag pp.29-31 native; VOL-VZW 8 commissaris niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Monte Rosa 0413.350.751,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0413350751,KBO Public Search FOD Economie,{DAY},official_register,tick2437; Actief; 4 VE 2.153.773.350 zetel Heidebergstraat 249 3010 Leuven since 30.05.2006 + 2.231.430.560 De Vlieger Drakenhoflaan 246 2100 Antwerpen since 01.01.2014 + 2.231.430.659 Herent Van Bladelstraat 30 3020 Herent since 01.01.2008 + 2.231.430.857 Denoek Bovenloweg 2 3010 Leuven since 01.01.2008; naam Monte Rosa Jeugdzorg van de Zusters der Christelijke Scholen since 22.09.2004; VZW since 23.07.1973; begindatum 23.07.1973; zetel Heidebergstraat 249 3010 Leuven since 27.06.2001; RSZ2025 87.991; BTW2025 87.991 since 01.03.2026; FOI info@monterosa.be; NOT Jeugdhulp Don Bosco 0408.666.344; NOT Ferm Kinderopvang 0416.117.627; NOT IZW 0430.278.439; NOT Avida 0438.814.241; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche Monte Rosa 0413350751 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0413350751,NBB Consult,{DAY},official_register,tick2437; deposit-id 2026-00093041 YE 30/12/2025 filing 29/04/2026 VOL-VZW Volledig Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Monte Rosa FOI contact leftover city_leuven OVBJ,https://monterosa.be/,VZW Monte Rosa Jeugdzorg,{DAY},foi_contact,tick2437; FOI info@monterosa.be; zetel Heidebergstraat 249 3010 Leuven; leftover mined city_leuven after IZW / Ferm Kinderopvang / Alvinnenberg / Hejmen / Staf / Annuntiaten / Woonzorgnet-Dijleland; also leftover mined city_herent + leftover mined city_antwerpen same KBO; OVBJ Opgroeien HCO 27693; NOT Kloosterstraat 6 Drongen; NOT Don Bosco; NOT Ferm; NOT IZW; NOT Avida; NOT Konekt; NOT Helan",
])
print("sources ok")
