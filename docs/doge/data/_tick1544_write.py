#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1544 surgical writes. Do not rewrite research_queue whole-file."""
from pathlib import Path
import sys
ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_hvwh"
SRC = "src_hvwh_jr2025_bbc"
PDF = "https://brandweerwesthoek.be/wp-content/uploads/2026/06/2025-Activiteitenverslag-Brandweer-Westhoek_LR.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Brandweer Westhoek official activiteitenverslag 2025,{PDF},HVZ Westhoek,2026-08-20,budget,tick1544; official activiteitenverslag 2025; PDF 50p / 5676746 bytes; pdfinfo created 05.05.2026 09:01:49 UTC Adobe InDesign 21.3; Financieel overzicht pages 45-46; euros PDF only; full zoneraad rekening 2025 unpublished",
        "src_hvwh_kbo_0500929873,KBO Hulpverleningszone Brandweer Westhoek 0500.929.873,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0500929873,FPS Economy KBO,2026-08-20,official_register,tick1544; leftover IGS hulpverleningszone of mined Koksijde + leftover of Veurne/Ieper/Poperinge/Diksmuide/Nieuwpoort/De Panne and remaining Westhoek gemeenten; zetel Zeelaan 37 8670 Koksijde; KBO 0500.929.873 Actief; prefix hvwh unused",
        "src_hvwh_site,HVZ Westhoek official site (activiteitenverslag 2025 published),https://brandweerwesthoek.be/over-ons/,HVZ Westhoek,2026-08-20,official_web,tick1544; leftover IGS of mined Koksijde; official AV2025 live on brandweerwesthoek.be; full rekening 2025 unpublished (inzage / FOI)",
        "src_hvwh_foi_contact,HVZ Westhoek FOI channel (info@brandweerwesthoek.be),https://brandweerwesthoek.be/over-ons/,HVZ Westhoek,2026-08-20,official_web,tick1544; leftover IGS of mined Koksijde; FOI ready not sent; Zeelaan 37 8670 Koksijde; official e-mail info@brandweerwesthoek.be; NOT leftover HVZ Fluvia 0500.929.774 / leftover HVZ1 1539 / leftover CAW NWVL 1535 / leftover DVV Westhoek / leftover RL Westhoek",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_hvwh," in raw or raw.startswith(b"igs_hvwh,"):
        raise SystemExit("igs_hvwh already present")
    if b"0500.929.873" in raw or b"0500929873" in raw:
        raise SystemExit("HVZ Westhoek KBO already present as entity")
    row = (
        "igs_hvwh,Hulpverleningszone Brandweer Westhoek / HVZ Westhoek (leftover IGS hulpverleningszone of mined Koksijde + leftover of Veurne/Ieper/Poperinge/Diksmuide/Nieuwpoort/De Panne and remaining Westhoek gemeenten; NOT leftover HVZ Fluvia / leftover HVZ1 1539 / leftover CAW NWVL 1535 / leftover DVV Westhoek / leftover RL Westhoek / leftover CO7 / leftover IJzer en Zee 1494 / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover HVZ Rivierenland / leftover HVZ Waasland / leftover Brandweerzone Centrum / leftover HVZ Oost-Limburg / leftover Brandweerzone Rand / leftover HVZ Vlaams-Brabant West),"
        "Zone de secours Westhoek (IGS residuel / zone de secours),"
        "Brandweer Westhoek leftover fire-rescue IGS of mined Koksijde + remaining Westhoek municipalities (not leftover HVZ Fluvia / leftover HVZ1 / leftover CAW NWVL / leftover DVV Westhoek / leftover RL Westhoek / leftover HVZ Kempen),"
        "other,city_koksijde,nl,https://brandweerwesthoek.be/,info@brandweerwesthoek.be,Zeelaan 37 8670 Koksijde,"
        "tick1544 leftover residual IGS hulpverleningszone of mined Koksijde after leftover AGB/APB/Bosgroep/IOED/Dijk92 hunt; leftover AGB/Bosgroep/Dijk92/IOED still unpublished this tick so leftover IGS with live official AV2025 taken; KBO 0500.929.873 Actief; zetel Koksijde 8670; live official activiteitenverslag 2025 50p 5676746 created 05.05.2026; sourced euros uitgaven_gewone 17511626 pers 13083164 werking 4428462 prestaties 1493651 werkingstoelagen 18487764 invest 2782545; FOI ready not sent; parent city_koksijde; prefix hvwh; NOT leftover HVZ Fluvia / leftover HVZ1 1539 / leftover CAW NWVL 1535 / leftover DVV Westhoek / leftover RL Westhoek / leftover HVZ Kempen 1543 / leftover BVLAR 1542 / leftover HVZ Midwest 1541 / leftover HVZ Meetjesland 1540 / leftover HVZ1 already taken / leftover HVZ Taxandria 1538 / leftover HVZ Oost 1537 / leftover Brandweerzone Antwerpen / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535 / leftover official-41 1464-1505 / leftover Erfpunt 1536 / leftover IVAREM 1524"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_hvwh")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
