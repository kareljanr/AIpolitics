from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2439_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_slabbertjes_jr2025_nbb_pdf_2439"
SRC_KBO="src_slabbertjes_kbo_2439"
SRC_SBM="src_slabbertjes_sbm_2439"
SRC_SITE="src_slabbertjes_site_2439"
GAP="gap_slabbertjes_opgroeien_matrix_bruto_520k_omzet73_empty_pnl_drop_48k_destin_jump_375k_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 De Slabbertjes deposit 2026-00138923,http://cdn.staatsbladmonitor.be/2026pdf/2026-00138923.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2439; official native PDF 41374 bytes 11p VKT-VZW 26.0.12 m04-f; header 04.06.2026; AV 31.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-12; CreationDate 2026-06-05 07:41:16 UTC OpenPDF 1.3.26; all 11p native text euros; VKT-VZW 7+8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf De Slabbertjes 0411.972.064,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0411972064,KBO Public Search FOD Economie,{DAY},official_register,tick2439; Actief; 1 VE 2.150.882.552 zetel Mechelsevest 4 3000 Leuven since 03.01.2006; naam Kinderdagverblijf De Slabbertjes since 31.08.1982; VZW since 20.12.1971; begindatum 20.12.1971; zetel Mechelsevest 4 3000 Leuven since 01.08.1977; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI info@deslabbertjes.be; NOT Ferm Kinderopvang 0416.117.627; NOT t Eekhoorntje 0414.453.680; NOT De Wissel 0421.913.376; NOT Monte Rosa 0413.350.751; NOT IZW 0430.278.439; NOT Grauwzusters 0409.771.748; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche De Slabbertjes 0411972064 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0411972064,NBB Consult,{DAY},official_register,tick2439; deposit-id 2026-00138923 YE 30/12/2025 filing 04/06/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},De Slabbertjes FOI contact leftover city_leuven CIK,https://www.deslabbertjes.be/,VZW Kinderdagverblijf De Slabbertjes Opgroeien CIK,{DAY},foi_contact,tick2439; FOI info@deslabbertjes.be; tel 016 29 05 85; zetel Mechelsevest 4 3000 Leuven; leftover mined city_leuven after De Wissel / Monte Rosa / IZW / Ferm Kinderopvang / t Eekhoorntje / Alvinnenberg / Hejmen / Staf; Opgroeien CIK 30 plaatsen 0-3 jaar IKT; NOT Kloosterstraat 6 Drongen; NOT Ferm; NOT t Eekhoorntje; NOT De Wissel; NOT Monte Rosa; NOT IZW; NOT Grauwzusters convent; NOT Helan",
])
print("sources ok")
