from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2443_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_jdbv_jr2025_nbb_pdf_2443"
SRC_KBO="src_jdbv_kbo_2443"
SRC_SBM="src_jdbv_sbm_2443"
SRC_SITE="src_jdbv_site_2443"
GAP="gap_jdbv_jeugdhulp_matrix_opbr_29_16m_omzet_208k_73_27_79m_pnl_drop_830k_l5"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Jeugdhulp Don Bosco Vlaanderen deposit 2026-00259885,http://cdn.staatsbladmonitor.be/2026pdf/2026-00259885.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2443; official native PDF 1102230 bytes 45p VOL-VZW 26.0.15 m05-f; header 06.07.2026; AV 18.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-27; CreationDate 2026-07-07 06:38:28 UTC OpenPDF 1.3.26; financials pp.1-38 native; commissarisverslag pp.39-45 native text oordeel met voorbehoud; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.4.1 6.4.2 6.4.3 6.5.1 6.5.2 6.5.3 6.14 6.16 6.18 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Jeugdhulp Don Bosco Vlaanderen 0408.666.344,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408666344,KBO Public Search FOD Economie,{DAY},official_register,tick2443; Actief; 17 VE zetel Waaistraat 6 9900 Eeklo since 24.08.1994; naam Jeugdhulp Don Bosco Vlaanderen since 15.06.2015; VZW since 31.01.1967; begindatum 31.01.1967; RSZ2025 87.991; Aanbestedende overheid since 31.01.1967; Kinderopvang Vlaamse Gemeenschap since 25.12.2018; FOI info@jeugdhulpdonbosco.be; 2/17 VE Eeklo; NOT VIA Don Bosco vzw_via; NOT Kinderlach 0450.275.186; NOT m-accent Eeklo 0465.841.411; NOT Ascendere 0409.470.553; NOT Kloosterstraat 6 9031 Drongen (VE is Beekstraat 46c)",
f"{SRC_SBM},NBB Consult / SBM fiche Jeugdhulp Don Bosco Vlaanderen 0408666344 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0408666344,NBB Consult,{DAY},official_register,tick2443; deposit-id 2026-00259885 YE 31/12/2025 filing 06/07/2026 VOL-VZW Volledig Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Jeugdhulp Don Bosco Vlaanderen FOI contact leftover city_eeklo jeugdhulp,https://jeugdhulpdonbosco.be/contact/,VZW Jeugdhulp Don Bosco Vlaanderen Opgroeien jeugdhulp,{DAY},foi_contact,tick2443; FOI info@jeugdhulpdonbosco.be; zetel Waaistraat 6 9900 Eeklo; leftover mined city_eeklo after m-accent / Ascendere / CGG Adentro / HVZ Meetjesland; 17 VE 2/17 Eeklo; NOT Kloosterstraat 6 Drongen; NOT VIA Don Bosco; NOT Kinderlach; NOT Helan; NOT t Anemoontje",
])
print("sources ok")
