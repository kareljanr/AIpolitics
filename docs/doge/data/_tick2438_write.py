from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2438_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_de_wissel_jr2025_nbb_pdf_2438"
SRC_KBO="src_de_wissel_kbo_2438"
SRC_SBM="src_de_wissel_sbm_2438"
SRC_SITE="src_de_wissel_site_2438"
GAP="gap_de_wissel_opgroeien_matrix_opbr_8_58m_omzet_empty_73_8_10m_pnl_jump_102k_destin_200k_l5"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 De Wissel deposit 2026-00213923,http://cdn.staatsbladmonitor.be/2026pdf/2026-00213923.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2438; official native PDF 170301 bytes 30p VOL-VZW 26.0.15 m05-f; header 29.06.2026; AV 24.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-11; CreationDate 2026-06-29 20:10:34 UTC OpenPDF 1.3.26; all 30p native text euros; VOL-VZW 8 commissaris niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO De Wissel 0421.913.376,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0421913376,KBO Public Search FOD Economie,{DAY},official_register,tick2438; Actief; 1 VE 2.154.399.692 zetel Parkstraat 64 3000 Leuven since 12.06.2006; naam De Wissel since 07.09.2004; VZW since 27.02.1981; begindatum 27.02.1981; zetel Parkstraat 64 3000 Leuven since 10.02.2025; RSZ2025 87.991; BTW2025 87.991 since 01.01.2025; FOI info@wissel.be; NOT Monte Rosa 0413.350.751; NOT MFC Combo; NOT Jeugdhulp Don Bosco 0408.666.344; NOT Ferm Kinderopvang 0416.117.627; NOT IZW 0430.278.439; NOT Avida 0438.814.241; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche De Wissel 0421913376 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0421913376,NBB Consult,{DAY},official_register,tick2438; deposit-id 2026-00213923 YE 30/12/2025 filing 29/06/2026 VOL-VZW Volledig Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},De Wissel FOI contact leftover city_leuven OVBJ,https://www.wissel.be/,VZW De Wissel CANO-jeugdhulp,{DAY},foi_contact,tick2438; FOI info@wissel.be; tel 016 28 49 44; zetel Parkstraat 64 3000 Leuven; leftover mined city_leuven after Monte Rosa / IZW / Ferm Kinderopvang / Alvinnenberg / Hejmen / Staf / Annuntiaten / Woonzorgnet-Dijleland; Opgroeien CANO/OVBJ; sites De Shelter / De Rotonda / Het Vertrek Leuven + De Switch Sint-Pieters-Rode + Centrum Molenmoes Wezemaal + OverKop Tienen same KBO; NOT Kloosterstraat 6 Drongen; NOT Monte Rosa; NOT MFC Combo; NOT Don Bosco; NOT Ferm; NOT IZW; NOT Avida; NOT Helan",
])
print("sources ok")
