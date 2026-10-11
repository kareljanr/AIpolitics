from pathlib import Path
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2440_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_ukkies_jr2025_nbb_pdf_2440"
SRC_KBO="src_ukkies_kbo_2440"
SRC_SBM="src_ukkies_sbm_2440"
SRC_SITE="src_ukkies_site_2440"
GAP="gap_ukkies_opgroeien_matrix_bruto_5_13m_omzet73_empty_pnl_flat_309k_destin_flat_309k_l5"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 De Ukkies deposit 2026-00164180,http://cdn.staatsbladmonitor.be/2026pdf/2026-00164180.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2440; official native PDF 1011593 bytes 26p VKT-VZW 26.0.12 m04-f; header 16.06.2026; AV 27.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-20; CreationDate 2026-06-16 13:48:48 UTC OpenPDF 1.3.26; financials pp.1-20 native text euros; commissarisverslag pp.21-26 scan; VKT-VZW 6.1.1 + VKT-VZW 7 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO De Ukkies 0412.729.654,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412729654,KBO Public Search FOD Economie,{DAY},official_register,tick2440; Actief; 3 VE 2.175.792.350 Erasmuslaan 14 3500 Hasselt since 01.07.1975 + 2.175.792.647 Kleinstraat 19 3500 Hasselt since 01.07.1975 + 2.175.793.538 Blijde-Inkomststraat 34 3500 Hasselt since 01.07.1975; naam De Ukkies since 09.06.2021; VZW since 17.05.1971; begindatum 17.05.1971; zetel Erasmuslaan 14 3500 Hasselt since 01.01.2025; RSZ2025 88.911; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI secretariaat@ukkies.be; NOT De Slabbertjes 0411.972.064; NOT Ferm Kinderopvang 0416.117.627; NOT Grauwzusters 0409.771.748; NOT Jessa 0821.142.117; NOT Kinderlach 0450.275.186; NOT Kloosterstraat 6 9031 Drongen",
f"{SRC_SBM},NBB Consult / SBM fiche De Ukkies 0412729654 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0412729654,NBB Consult,{DAY},official_register,tick2440; deposit-id 2026-00164180 YE 31/12/2025 filing 16/06/2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},De Ukkies FOI contact leftover city_hasselt CIK,https://www.ukkies.be/,VZW De Ukkies Opgroeien CIK+BOA,{DAY},foi_contact,tick2440; FOI secretariaat@ukkies.be; tel 011 21 21 15; zetel Erasmuslaan 14 3500 Hasselt; leftover mined city_hasselt after Grauwzusters convent skip / Integra / Kohesi / HVZ ZWL / Salvator / De Springplank / Stijn / De Wroeter / NBSW / De Oever / REVA Kohesi / LDSST; Opgroeien CIK 212 plaatsen 0-3 jaar + 5 BOA; site 462 kindplaatsen / 6 initiatieven; NOT Kloosterstraat 6 Drongen; NOT De Slabbertjes; NOT Ferm; NOT Grauwzusters convent; NOT Jessa hospital; NOT Kinderlach; NOT Helan",
])
print("sources ok")
