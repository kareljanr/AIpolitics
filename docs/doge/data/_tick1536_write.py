#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick 1536 surgical writes. Do not rewrite research_queue whole-file.
Run with argv part: sources|entities
"""
from pathlib import Path
import sys

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
ENT = "igs_erfp"
SRC = "src_erfp_jr2025_nbb"
PDF = "http://cdn.staatsbladmonitor.be/2026pdf/2026-00165556.pdf"

def append_lf(path: Path, rows):
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    out = [r.rstrip("\r\n") + "\n" for r in rows]
    path.write_bytes(raw + "".join(out).encode("utf-8"))

def part_sources():
    append_lf(DATA / "sources.csv", [
        f"{SRC},Erfpunt official NBB WVV VKT-kap JR2025,{PDF},NBB / Erfpunt,2026-08-20,budget,tick1536; official NBB WVV VKT-kap JR2025 PDF 16p / 55040 bytes; deposit 2026-00165556 Initial (NBB consult enterprise page listed this single 2025 deposit filing 16.06.2026 year-end 30.12.2025 Verkort model kapitaalvennootschap; no later Aanpassing visible); AV 11.06.2026; pdfinfo created 17.06.2026 00:59:40 UTC; model VKT-kap 26.0.12 m01-f; euros PDF only",
        "src_erfp_kbo_0860274885,KBO Erfpunt 0860.274.885,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0860274885,FPS Economy KBO,2026-08-20,official_register,tick1536; leftover recognized IOED / leftover IGS projectvereniging of mined Sint-Niklaas + leftover of Temse Lokeren Stekene Sint-Gillis-Waas Waasmunster Beveren-Kruibeke-Zwijndrecht; zetel Regentiestraat 63 9100 Sint-Niklaas; KBO 0860.274.885 Actief; prefix erfp unused",
        "src_erfp_nbb_consult,NBB Consult Erfpunt published deposits 0860274885,https://consult.cbso.nbb.be/consult-enterprise/0860274885,NBB Central Balance Sheet Office,2026-08-20,official_register,tick1536; leftover IOED; JR2025 reference 2026-00165556 Initial filing 16.06.2026 year-end 30.12.2025 Verkort model kapitaalvennootschap; 11 results listed",
        "src_erfp_foi_contact,Erfpunt FOI channel (admin@erfpunt.be),https://www.erfpunt.be/contact/,Erfpunt,2026-08-20,official_web,tick1536; leftover recognized IOED of mined Sint-Niklaas; FOI ready not sent; Regentiestraat 63 9100 Sint-Niklaas; official contact admin@erfpunt.be; NOT leftover Erfgoed Denderland / leftover Erfgoed Voorkempen / leftover Erfgoed Noorderkempen / leftover Woonpunt Waas / leftover WoonST Temse / leftover IVAREM",
    ])
    print("sources +4")

def part_entities():
    pth = DATA / "entities.csv"
    raw = pth.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raw += b"\n"
    if b"\nigs_erfp," in raw or raw.startswith(b"igs_erfp,"):
        raise SystemExit("igs_erfp already present")
    if b"0860.274.885" in raw or b"0860274885" in raw:
        raise SystemExit("Erfpunt KBO already present as entity")
    row = (
        "igs_erfp,Erfpunt / Projectvereniging Erfpunt (leftover recognized IOED / leftover IGS projectvereniging of mined Sint-Niklaas + leftover of Temse Lokeren Stekene Sint-Gillis-Waas Waasmunster Beveren-Kruibeke-Zwijndrecht; NOT leftover Erfgoed Denderland / leftover Erfgoed Voorkempen / leftover Erfgoed Noorderkempen / leftover Woonpunt Waas / leftover WoonST Temse / leftover Dimensa / leftover IVAREM / leftover CAW Oost-Vlaanderen 1532 / leftover official-41 1464-1505 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "Erfpunt (IOED residuel / association de projet Waasland),"
        "Erfpunt leftover recognized IOED / IGS projectvereniging of mined Sint-Niklaas + remaining Waasland municipalities (not leftover Erfgoed Denderland / leftover Erfgoed Voorkempen / leftover Erfgoed Noorderkempen / leftover Woonpunt Waas / leftover WoonST Temse / leftover Dimensa / leftover IVAREM / leftover CAW Oost-Vlaanderen / leftover official-41 / leftover APB Inovant / Atlas / leftover Puyenbroeck),"
        "other,city_sint_niklaas,nl,https://www.erfpunt.be/,admin@erfpunt.be,Regentiestraat 63 9100 Sint-Niklaas,"
        "tick1536 leftover residual recognized IOED / leftover IGS projectvereniging of mined Sint-Niklaas after leftover AGB/APB/Bosgroep/CAW hunt; leftover AGB/Bosgroep still unpublished this tick so leftover IOED with live JR2025 taken; KBO 0860.274.885 Actief; zetel Sint-Niklaas 9100; live JR2025 official NBB WVV VKT-kap PDF Initial; sourced euros assets 438711 bruto 700561 pers 677959 7.8 VTE cash 61449 debt 297897 pnl -929 expl PROFIT 8742; FOI ready not sent; parent city_sint_niklaas; prefix erfp; NOT leftover Erfgoed Denderland / leftover Erfgoed Voorkempen / leftover Erfgoed Noorderkempen / leftover Woonpunt Waas / leftover WoonST Temse / leftover Dimensa / leftover IVAREM / leftover official-41 1464-1505 / leftover CGG 1507-1523 / leftover 11-CAW 1525-1535"
        "\n"
    )
    pth.write_bytes(raw + row.encode("utf-8"))
    print("entities +1 igs_erfp")

if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part == "sources":
        part_sources()
    elif part == "entities":
        part_entities()
    else:
        raise SystemExit("use sources|entities")
