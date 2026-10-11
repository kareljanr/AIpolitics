#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2395_stamp.txt").read_text().strip().splitlines()
EID = "vzw_car_horizon"
SRC_PDF = "src_horizon_jr2025_nbb_pdf_2395"
COMM = "comm_horizon_jr2025_statutory_omzet_3_00m_73_464k_pnl_drop"
LB = "lb_horizon_omzet_3_00m_73_464k_pnl_drop_destin_246k_jr2025"
GAP = "gap_horizon_riziv_vl_vaph_matrix_omzet_3_00m_73_464k_pnl_drop_destin_246k_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"

def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)

cash_json = (
    '"{""2025_omzet"":3001208,""2025_bruto9900"":2680880,""2025_73"":464125,'
    '""2025_7076A"":3001208,""2025_pnl"":246289,""2025_bedrijfswinst"":143692,'
    '""2025_equity"":2542581,""2025_assets"":2952629,""2025_debt"":410048,'
    '""2025_fte"":35,""2025_kapitaalsubsidies"":131925,""2025_destin691"":246289,'
    '""2025_cash"":958792,""2025_geldbeleggingen"":1352010,'
    '""2025_personnel62"":2426658,""2025_gebouwen22"":96635,'
    '""2025_aanbouw27"":0,""2025_capex"":115289,""2025_fondsen10"":0,'
    '""2025_bestemde13"":2410656,""2025_overgedragen14"":0,'
    '""2025_76A"":0,""2025_66A"":26427,""2025_76B"":97592,'
    '""2025_791"":0,""2024_omzet"":3134235,""2024_73"":457696,'
    '""2024_bruto9900"":2784424,""2024_pnl"":397075,""2024_bedrijfswinst"":316341,'
    '""2024_equity"":2296293,""2024_assets"":2739676,""2024_debt"":443383,'
    '""2024_kapitaalsubsidies"":131925,""2024_cash"":1305994,""2024_fte"":31.6,'
    '""2024_destin691"":397075,""2024_geldbeleggingen"":885845}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},CAR Horizon vzw YE2025 (omzet DROP 3.00m / 73 464k / pnl DROP 246k / destin 246k / Strong PDF),{EID},RIZIV + VAPH + leftover city_geraardsbergen,VZW Horizon (KBO 0418.529.759; Actief; 1 VE; RSZ2025 86.959),2026-07-08,2025,2025,3001208,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00268911.pdf,Public CAR dual of mined city_geraardsbergen,Publish RIZIV/VAPH/VAZG/stad matrix inside omzet 3.00m + 73 464k + pnl drop 246k + destin 246k + cash drop vs geldbeleggingen jump,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Geraardsbergen>CAR Horizon>JR2025_statutory_L5,tick2395; Strong official native PDF; leftover city_geraardsbergen after ZWZ@2394; NOT ZWZ 0832.024.923; NOT Zonnebloem 0421.039.386; NOT CAR Houtland-Westkust 0408.436.019; NOT De Schans 0430.473.231; NOT LDSST 0410.121.344; NOT REVA Kohesi 0410.121.641; NOT CGG Kohesi 0472.466.907; NOT BW Kohesi 0451.932.995; NOT Kloosterstraat 6; NOT CAR De Hert; NOT CAR De Klinker; NOT Ascendere; NOT CAR Roeselare; NOT Vijvens; NOT CAR DAT; NOT H.Hart Oudenaarde; NOT Sint-Vincentius Zulte; NOT Floordam; NOT Heropbeuring; NOT NMSC; NOT MKL; NOT Pulderbos; NOT Inkendaal; NOT Sint-Lievenspoort; NOT CAR Overleie; NOT Leieborg; NOT Ten Anker; not TE-additive",
])

append_lines(DATA / "leaderboard.csv", [
    f"{LB},CAR Horizon omzet DROP 3.00m / 73 464k / pnl DROP 246k / destin 246k (YE2025 Geraardsbergen),L5,car_vzw_statutory,Vlaanderen>Oost-Vlaanderen>Geraardsbergen>CAR Horizon>JR2025,3001208,3001208,PDF omzet DROP 3001208 CAR envelope; 73 JUMP 464125; bruto9900 DROP 2680880; bedrijfswinst DROP 143692; pnl DROP 246289; equity JUMP 2542581; assets JUMP 2952629; debt DROP 410048; FTE 35; kapitaalsubsidies FLAT 131925; destin691 DROP 246289; cash DROP 958792; geldbeleggingen JUMP 1352010; gebouwen 96635; aanbouw empty; capex 115289; personeel 62 2426658,strong,{SRC_PDF},children CAR Geraardsbergen ambulante revalidatie,RIZIV + VAPH + leftover city_geraardsbergen,3.00m CAR omzet DROP 4.2pct; 73 464k; pnl DROP 246k; destin 246k; cash DROP 959k vs beleggingen JUMP 1.35m; leftover city_geraardsbergen,5.4,5.3,5.2,5.28,FOI RIZIV/VAPH/VAZG/stad matrix + omzet 3.00m + 73 464k + pnl drop 246k + destin 246k + cash vs geldbeleggingen + 66A 26k,active,,tick2395; Strong official NBB native PDF + Strong KBO; leftover city_geraardsbergen after ZWZ@2394; OFF Drongen OFF De Schans OFF LDSST OFF REVA Kohesi OFF CGG Kohesi OFF BW Kohesi OFF CAR De Hert OFF CAR De Klinker OFF Ascendere OFF CAR Roeselare OFF Vijvens OFF CAR DAT OFF H.Hart Oudenaarde OFF Sint-Vincentius Zulte OFF Floordam OFF Heropbeuring OFF NMSC OFF MKL OFF Pulderbos OFF Inkendaal OFF CAR Overleie OFF Houtland OFF Zonnebloem OFF ZWZ OFF Ten Anker OFF Leieborg",
])

append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost-Vlaanderen>Geraardsbergen>CAR Horizon>RIZIV_VAPH_VAZG,{EID},RIZIV/VAPH/VAZG/stad split inside omzet 3001208 + 73 464125; why pnl DROP 246289 (was 397075) and 9901 DROP 143692; why 691 246289 full to bestemde 2410656; why cash DROP 958792 vs geldbeleggingen JUMP 1352010; why kapitaalsubsidies FLAT 131925 with capex 115289; why 66A 26427,Strong official PDF leftover public CAR of city_geraardsbergen; 3.00m omzet; public CAR not private clinic; not ZWZ 0832.024.923; not Zonnebloem 0421.039.386; not CAR Houtland-Westkust 0408.436.019; not De Schans 0430.473.231; not LDSST 0410.121.344; not REVA Kohesi 0410.121.641; not CGG Kohesi 0472.466.907; not BW Kohesi 0451.932.995,8,Horizon VZW / Raad van Bestuur,erwin.franceus@horizonvzw.be,"Oudenaardsestraat 215, 9500 Geraardsbergen",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2395; ready NOT sent; Strong official native NBB PDF; leftover city_geraardsbergen CAR after ZWZ@2394; off Drongen off De Schans off LDSST off REVA Kohesi off CGG Kohesi off BW Kohesi off CAR De Hert off CAR De Klinker off Ascendere off CAR Roeselare off Vijvens off CAR DAT off H.Hart Oudenaarde off Sint-Vincentius Zulte off Floordam off Heropbeuring off NMSC off MKL off Pulderbos off Inkendaal off CAR Overleie off Houtland off Zonnebloem off ZWZ off Ten Anker off Leieborg; AGB/FARO/Gandae still YE2024',
])
print("commitments+lb+foi ok")
