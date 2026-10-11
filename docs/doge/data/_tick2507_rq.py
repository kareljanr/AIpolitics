from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2507_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_capelderij_buggenhout"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2507,") != 1:
    raise SystemExit(f"bad 2507 count {rq_raw.count(b'rq_2507,')}")
if b"rq_2508," in rq_raw:
    raise SystemExit("2508 exists")
idx = rq_raw.rfind(b"rq_2507,")
if idx < 0:
    raise SystemExit("rq_2507 not found")

notes_2507 = (
    "Took unused leftover public leftover VAPH Capelderij 0417.002.505 leftover mined city_buggenhout. "
    "Official NBB VKT-VZW YE2025 2026-00310005 native statutory 15p. Envelope bruto9900 JUMP 3841282 "
    "(VKT because omzet70+73 empty; 76A 0 DROP); cash DROP 100666; pnl IMPROVED LOSS -2621; "
    "9901 IMPROVED LOSS -22415; destin empty; FTE JUMP 48.1 from empty/0. FIRST leftover unused + live official YE2025 after leftover-type hunt "
    "(Wonozo 0423.555.349 skip jeugdhulp Geraardsbergen not leftover WZC/VAPH/CAR/CIK; Anemoon/SLG 0410.958.712 Korian remine skip; leftover city_buggenhout leftover VAPH unused besides Avalon@2503; leftover WZC De Heymeulen still YE2024). "
    "NOT Avalon remine. NOT De Heymeulen YE2024. NOT CAR Buggenhout leftover-via-VE. NOT Blijdorp remine. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2507 = (
    "tick2507 leftover mined city_buggenhout leftover VAPH; Strong native PDF; 1 VE; prior-year identical; next rq_2508 leftover dual; next every-10 2510"
)
notes_2508 = (
    "Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_buggenhout leftover VAPH taken (Avalon@2503 + Capelderij@2507; leftover WZC De Heymeulen 0420.669.303 still YE2024 / SBM still YE2024 / broker HTML stub). leftover city_buggenhout leftover CAR Buggenhout 0412.404.903 zetel Kloosterstraat 6 9031 Gent leftover-via-VE SKIP. "
    "NOW leftover city_wetteren leftover CIK taken (Kinderdagverblijf Sint-Jozef@2502 + Fiola@2506; leftover VAPH Sint-Lodewijk@2505; leftover WZC = Zorg-Saam remine; leftover CAR/maatwerk still open/empty). "
    "NOW leftover city_herzele leftover CIK Fie&Ola Herzele is leftover-via-VE of leftover city_wetteren seated Fiola SKIP. leftover city_herzele leftover WZC taken (Hunnegem@2504; leftover WZC exhausted Stuyvenberg/Ter Linden CuraCare commercial; leftover VAPH De Kanteling/VillaVip no JR). "
    "leftover city_tielt WZC taken (SAMEN@2501 + De Zonnewende@2487; VAPH De Luifel + CIK Harlekijntjes already taken; leftover city_tielt CAR/maatwerk still open/empty). "
    "leftover city_niel still unused (2845 VZW census sports/culture only). "
    "leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open (De Ster no JR; WZC Sint-Vincentius YE2024; Meredal+Avondzon WZC taken; Hunnegem VE in Aaigem is Herzele-seated NOT leftover city_erpe_mere). "
    "leftover city_mol/denderleeuw still zero leftover children (Wonen met Zorg no JR; Ten Hove OCMW; Molleke/t Sas still YE2024). leftover city_lede WZC Prieelshof Korian skip. "
    "leftover city_bornem leftover WZC/VAPH remine/commercial (De Vlietoever BV; OLV remine; Huize Eyckerheyde remine@2341; CAR taken). "
    "leftover city_puurs leftover WZC commercial/OCMW (Sint-Pieter OCMW remine; Anemoon/SLG 0410.958.712 Korian remine; Sauvegarde CuraCare BV; maatwerk Nektari taken). "
    "leftover city_ninove leftover WZC commercial/OCMW (Klateringen OCMW; Wilgendries 0452.865.383; leftover VAPH Schoonderhage remine; leftover CIK Fie&Ola Ninove leftover-via-VE Fiola SKIP; CIK Hartjes taken). "
    "leftover city_kalmthout leftover WZC Beukenhof Vulpia commercial; leftover WZC Sint-Vincentius leftover-via-VE De Medemens remine. leftover city_ronse leftover WZC Hogerlucht = Werken Glorieux remine; De Linde still YE2024. "
    "Wonozo 0423.555.349 leftover city_geraardsbergen jeugdhulp SKIP (not leftover WZC/VAPH/CAR/hospital/maatwerk/CIK; leftover CAR Horizon already taken). "
    "Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / t Sas / Molleke / OpWeg / Aurora / Het Witte Huis / WZC Sint-Vincentius Erpe-Mere / Aralea / De Heymeulen still YE2024. "
    "Villa Boempatat YE2025 last-balansjaar 2025 but SCAN/CDN 403 / broker HTML stub. Jessa leftover city_hasselt hospital special schema CDN 403 / broker HTML stub. city_kapellen missing. "
    "NOT Capelderij remine. NOT Avalon remine. NOT Fiola remine. NOT Kinderdagverblijf Sint-Jozef remine. NOT Sint-Lodewijk remine. NOT Hunnegem remine. "
    "NOT leftover-via-VE. NOT KEERPUNT leftover-via-VE Gent. NOT CAR Buggenhout leftover-via-VE Gent. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2508 = (
    "spawned after tick2507 leftover city_buggenhout leftover VAPH; Capelderij taken leftover mined city_buggenhout leftover VAPH; leftover city_buggenhout leftover VAPH now Avalon+Capelderij; leftover city_buggenhout WZC De Heymeulen still YE2024; leftover city_wetteren leftover CIK now Sint-Jozef+Fiola; leftover city_wetteren CAR/maatwerk still open/empty; leftover city_herzele leftover CIK Fie&Ola Herzele leftover-via-VE SKIP; leftover city_niel still unused; leftover city_mol/denderleeuw still zero leftover children; leftover city_herzele leftover VAPH De Kanteling/VillaVip no JR; leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open; Wonozo skip; next every-10 2510"
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

new_2507 = rq_line([
    "rq_2507",
    "leftover dual Capelderij YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2507,
    "",
    STAMP,
    STAMP,
    extra_2507,
])
new_2508 = rq_line([
    "rq_2508",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2508,
    "",
    STAMP,
    STAMP,
    extra_2508,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2507)
    f.write(new_2508)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2507", chk.count(b"rq_2507,"), "n2508", chk.count(b"rq_2508,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2507,2507,no,"
    "tick2507 leftover dual Capelderij 0417.002.505 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A 0 DROP; envelope bruto9900 JUMP 3841282; pnl IMPROVED LOSS -2621; 9901 IMPROVED LOSS -22415; equity DROP 2764099; assets DROP 3376776; debt JUMP 612676; FTE JUMP 48.1 from empty/0; kapitaalsubsidies DROP 981457; destin691 empty; 791 empty; cash DROP 100666; geldbeleggingen JUMP 1500000; capex 69237; 1 VE leftover city_buggenhout leftover VAPH); leftover mined city_buggenhout leftover VAPH; prior-year identical; FIRST leftover unused + live official YE2025 after leftover-type hunt (leftover city_buggenhout leftover VAPH unused besides Avalon@2503; Wonozo skip jeugdhulp Geraardsbergen; Anemoon/SLG Korian remine skip; leftover WZC De Heymeulen still YE2024; leftover CAR Buggenhout leftover-via-VE Gent SKIP); NOT Avalon remine; NOT De Heymeulen YE2024; NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; next rq_2508 leftover dual; next every-10 2510\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
