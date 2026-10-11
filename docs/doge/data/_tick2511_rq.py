from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2511_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "bv_den_bogaet_grimbergen"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2511,") != 1:
    raise SystemExit(f"bad 2511 count {rq_raw.count(b'rq_2511,')}")
if b"rq_2512," in rq_raw:
    raise SystemExit("2512 exists")
idx = rq_raw.rfind(b"rq_2511,")
if idx < 0:
    raise SystemExit("rq_2511 not found")

notes_2511 = (
    "Took unused leftover public leftover WZC Den Bogaet 0471.673.980 leftover mined city_grimbergen. "
    "Official NBB VOL-inb YE2025 2026-00341036 native statutory 30p. Envelope omzet70 JUMP 7593721 "
    "(70 present and not commercial-only; 6.10 OCMW 51256 + mutualiteit 3677526 inside 70; 73 empty VOL; 76A empty DROP); "
    "694 JUMP 2500000; cash DROP 272100; pnl FLIP PROFIT 166838; 9901 DROP 143914; equity DROP 4375649; debt JUMP 3572177; FTE DROP 73.8. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt "
    "(retry lock first valid hit DEN BOGAET; Jules/i-mens 0416.603.716 zetel Gent leftover-via-VE / 7158 FTE chain SKIP; "
    "Pamperbroekje 0661.886.527 leftover city_erpe_mere leftover CIK BV unused not locked; "
    "INFANO 0477.578.411 leftover-via-VE Ronse Zonnetje SKIP; De Schakel 0409.470.553 remine SKIP; "
    "Aurora Dilbeek 0407.624.484 still YE2024 SKIP; Helan Kinderopvang 0464.151.037 large chain SKIP; "
    "leftover city_grimbergen leftover maatwerk taken Den Diepen Boomgaard@2510; leftover VAPH Havinet remine@2301; leftover WZC Heilig Hart remine@2074; leftover CIK Kribbekrabbel BV + FERM leftover-via-VE Leuven; "
    "leftover city_niel still unused sports/culture only; leftover city_mol leftover CIK Molleke YE2024; leftover city_denderleeuw leftover CIK t Sas YE2024; AZ Waregem leftover hospital YE2025 SCAN/OCR HARD SKIP). "
    "NOT WZC Heilig Hart remine. NOT Havinet remine. NOT Den Diepen Boomgaard remine. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Zorg-Saam remine."
)
extra_2511 = (
    "tick2511 leftover mined city_grimbergen leftover WZC; Strong native PDF; 1 VE; prior-year identical; NOT every-10 (next every-10 2520); next rq_2512 leftover dual"
)
notes_2512 = (
    "Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_grimbergen leftover WZC taken (Den Bogaet@2511; leftover WZC Heilig Hart remine@2074 parent sec_flanders; leftover VAPH Havinet remine@2301; leftover maatwerk Den Diepen Boomgaard@2510; leftover CIK Kribbekrabbel BV + FERM leftover-via-VE Leuven). "
    "NOW leftover city_asse leftover CIK taken (Kribbe Kinderpret@2509; 3Wplus Kinderopvang@2407; Vijverbeek@2469; leftover VAPH Hopperank@2491; leftover maatwerk 3Wplus Werk@2492). "
    "NOW leftover city_geraardsbergen leftover maatwerk taken (De Dagmoed@2508; leftover CAR Horizon@2395; leftover WZC OCMW/commercial/YE2023; leftover jeugdhulp Wonozo skip; leftover CIK no local leftover VZW). "
    "NOW leftover city_buggenhout leftover VAPH taken (Avalon@2503 + Capelderij@2507; leftover WZC De Heymeulen 0420.669.303 still YE2024 / SBM still YE2024 / broker HTML stub HARD SKIP). leftover city_buggenhout leftover CAR Buggenhout 0412.404.903 zetel Kloosterstraat 6 9031 Gent leftover-via-VE SKIP. "
    "NOW leftover city_wetteren leftover CIK taken (Kinderdagverblijf Sint-Jozef@2502 + Fiola@2506; leftover VAPH Sint-Lodewijk@2505; leftover WZC = Zorg-Saam remine; leftover CAR/maatwerk still open/empty). "
    "NOW leftover city_herzele leftover CIK Fie&Ola Herzele is leftover-via-VE of leftover city_wetteren seated Fiola SKIP; leftover CIK Bengeltjes/Klettekes BV; Klavertje Vier = gemeente. leftover city_herzele leftover WZC taken (Hunnegem@2504; leftover WZC exhausted Stuyvenberg/Ter Linden CuraCare commercial; leftover VAPH De Kanteling/VillaVip no JR). leftover city_herzele leftover CAR/maatwerk may still be open. "
    "leftover city_tielt WZC taken (SAMEN@2501 + De Zonnewende@2487; VAPH De Luifel + CIK Harlekijntjes already taken; leftover city_tielt CAR/maatwerk still open/empty). "
    "leftover city_niel still unused (2845 VZW census sports/culture only). "
    "leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open/empty (WZC Avondzon + Meredal taken; Pamperbroekje 0661.886.527 leftover CIK BV unused YE2025 last-balansjaar not locked this tick). "
    "leftover city_mol leftover WZC remine/commercial/OCMW (Witte Meren remine tick1732 parent sec_flanders; Hemelrijck Armonea; Ten Hove OCMW; leftover hospital Heilig Hart YE2024; leftover maatwerk Lidwina remine; leftover CIK Molleke 0448.186.520 YE2024 SKIP). leftover city_denderleeuw leftover WZC Armonea/Gravenkasteel commercial; leftover CIK t Sas 0448.731.106 YE2024 SKIP. leftover city_mol/denderleeuw still zero leftover children parented under city_*. "
    "leftover city_bornem leftover WZC/VAPH remine/commercial (De Vlietoever BV; OLV remine@2065; Huize Eyckerheyde remine@2341; CAR taken; leftover WZC Seniorencentrum Onze Lieve Vrouw unused-check if still free). "
    "leftover city_puurs leftover WZC commercial/OCMW (Sint-Pieter OCMW remine; Anemoon/SLG 0410.958.712 Korian remine; Sauvegarde CuraCare BV; maatwerk Nektari taken). "
    "leftover city_kontich leftover CIK De Drie Klavertjes 0473.660.797 no NBB deposit SKIP; leftover VAPH Pegode taken@2497. "
    "leftover city_lokeren leftover CIK EVA Gezinswelzijn remine tick1253; leftover CIK Junior 0862.446.202 unused VZW 0 deposits SKIP; leftover VAPH Alderande + Hagewinde taken; leftover maatwerk De Sperwer taken. "
    "leftover city_dilbeek leftover CIK GOOFY 0521.958.483 unused VZW 0 deposits SKIP. "
    "leftover city_ronse leftover CIK Zonnetje = Infano remine leftover-via-VE; Sprookjesbos leftover-via-VE WZC Sint-Vincentius Erpe-Mere; Kinderopvang Glorieux = Werken Glorieux remine; leftover maatwerk/VAPH Grijkoort taken. "
    "leftover city_halle leftover CIK Palmboompje BV; CKG Sloebernest leftover-via-VE Gent. "
    "leftover city_ninove leftover CIK De Krekeltjes BV. leftover city_dendermonde leftover CIK Zonneschijn last JR YE2024. leftover city_herentals leftover CIK Zandkapoentjes BV. leftover city_geel leftover CIK NEVERLAND VZW bestuurder Korian SKIP. "
    "AZ Waregem 0405.460.592 unused leftover hospital YE2025 deposit 2026-00189439 S-vzw SCAN/OCR HARD SKIP do not invent euros. "
    "Jules/i-mens 0416.603.716 zetel Gent leftover-via-VE / large chain SKIP. "
    "Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / t Sas / Molleke / OpWeg / Aurora / Het Witte Huis / WZC Sint-Vincentius Erpe-Mere / Aralea / De Heymeulen / Edelweis / Baronie still YE2024/YE2023. "
    "NOT Den Bogaet remine. NOT Den Diepen Boomgaard remine. NOT Kribbe Kinderpret remine. NOT 3Wplus Kinderopvang remine. NOT Vijverbeek remine. NOT De Dagmoed remine. NOT Wonozo skip jeugdhulp. NOT Havinet remine. NOT WZC Heilig Hart Grimbergen remine. "
    "NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE Gent. NOT CAR Buggenhout leftover-via-VE Gent. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2512 = (
    "spawned after tick2511 leftover city_grimbergen leftover WZC; Den Bogaet taken leftover mined city_grimbergen leftover WZC; leftover city_grimbergen leftover maatwerk taken@2510; leftover VAPH/WZC remine; leftover city_asse leftover CIK now 3Wplus Kinderopvang+Vijverbeek+Kinderpret; leftover city_geraardsbergen leftover maatwerk now taken; leftover city_buggenhout leftover VAPH now Avalon+Capelderij; leftover city_buggenhout WZC De Heymeulen still YE2024; leftover city_wetteren leftover CIK now Sint-Jozef+Fiola; leftover city_wetteren CAR/maatwerk still open/empty; leftover city_niel still unused; leftover city_mol leftover CIK Molleke YE2024; leftover city_denderleeuw leftover CIK t Sas YE2024; leftover city_herzele leftover VAPH De Kanteling/VillaVip no JR; leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open; leftover city_kontich leftover CIK De Drie Klavertjes no NBB; leftover city_lokeren leftover CIK Junior 0 NBB; leftover city_dilbeek leftover CIK GOOFY 0 NBB; AZ Waregem SCAN HARD SKIP; Jules/i-mens leftover-via-VE SKIP; Wonozo skip; this tick is NOT every-10 (next every-10 2520)"
)

def rq_line(fields):
    buf = StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(fields)
    line = buf.getvalue()
    n = len(next(csv.reader(StringIO(line))))
    if n != 12:
        raise SystemExit(f"rq fields {n} != 12 for {fields[0]}")
    if not line.endswith("\n"):
        raise SystemExit("rq line no LF")
    if line.count("\n") != 1:
        raise SystemExit("rq line extra NL")
    return line.encode("utf-8")

new_2511 = rq_line([
    "rq_2511",
    "leftover dual Den Bogaet YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2511,
    "",
    STAMP,
    STAMP,
    extra_2511,
])
new_2512 = rq_line([
    "rq_2512",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2512,
    "",
    STAMP,
    STAMP,
    extra_2512,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2511)
    f.write(new_2512)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2511", chk.count(b"rq_2511,"), "n2512", chk.count(b"rq_2512,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2511,2511,no,"
    "tick2511 leftover dual Den Bogaet 0471.673.980 Strong native PDF (omzet70 JUMP 7593721 not commercial-only 6.10 OCMW+mutualiteit; 73 empty VOL; 76A empty DROP; envelope omzet70 JUMP 7593721; 694 JUMP 2500000; pnl FLIP PROFIT 166838; 9901 DROP 143914; equity DROP 4375649; assets FLAT 7947826; debt JUMP 3572177; FTE DROP 73.8; kapitaalsubsidies empty; destin691 empty; 792 JUMP 2500000; cash DROP 272100; geldbeleggingen JUMP 5417200; 1 VE leftover city_grimbergen leftover WZC); leftover mined city_grimbergen leftover WZC; prior-year identical; NOT every-10 (next every-10 2520); FIRST leftover unused + live official YE2025 after leftover-type hunt (retry lock DEN BOGAET first valid hit; Jules/i-mens leftover-via-VE Gent SKIP; Pamperbroekje leftover CIK BV not locked; leftover city_grimbergen leftover maatwerk Den Diepen Boomgaard@2510; leftover VAPH Havinet remine@2301; leftover WZC Heilig Hart remine@2074; leftover city_niel unused sports/culture; leftover city_mol leftover CIK Molleke YE2024; leftover city_denderleeuw leftover CIK t Sas YE2024; AZ Waregem SCAN HARD SKIP); NOT WZC Heilig Hart remine; NOT Havinet remine; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; next rq_2512 leftover dual\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
