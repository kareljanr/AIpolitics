# -*- coding: utf-8 -*-
import csv
import re
import ssl
import urllib.request
from html import unescape
from pathlib import Path

RAW = Path(__file__).resolve().parent
ROOT = RAW.parents[3]
DATA = ROOT / "data"
CTX = ssl.create_default_context()
UA = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "nl-BE,nl;q=0.9,en;q=0.8",
}
PAT = re.compile(
    r'(20\d\d)\s*:\s*\{\s*winst:\s*"([^"]+)",\s*eigen_vermogen:\s*"([^"]+)",'
    r'\s*bruto_marge:\s*"([^"]+)",\s*omzet:\s*"([^"]+)"'
)
csv.field_size_limit(10**7)

taken_text = (DATA / "entities.csv").read_text(encoding="utf-8", errors="replace")
taken_lb = (DATA / "leaderboard.csv").read_text(encoding="utf-8", errors="replace")

cands = [
    # unused WZC candidates from search / plausible public-interest
    ("wzc_sj_rumst", "0448190181", "woon-en-zorgcentrum-sint-jozef-vzw"),
    ("wzc_xxe_aout", "0443082637", "maison-de-repos-du-xxe-aout"),
    ("mrs_solbosch", "0403252642", ""),  # guess may 404
    ("wzc_imma_meulebeke", "0412123456", ""),  # placeholder skip if 404
    ("wzc_den_olm_berlaar", "0425175551", ""),
    ("wzc_de_meerssen", "0461754321", ""),
    # Walloon IGS / DSO leftovers
    ("cile", "0202395052", "compagnie-intercommunale-liegeoise-des-eaux"),
    ("tibi", "0200123456", ""),  # wrong - fix below
    ("hygea_cw", "0206612345", ""),
    ("logipole", "0465306214", ""),
    ("ceneo", "0200123789", ""),
    ("helora", "0678730865", ""),
    ("igretr", "0200363933", ""),  # IGRETEC already do-not-redo
    ("sofico", "0860325064", ""),
    ("sofico_alt", "0860.325.064".replace(".", ""), ""),
    ("spge", "0267440563", ""),
    ("aquafin", "0440.691.388".replace(".", ""), "aquafin"),
    ("fluvius_sc", "0477.445.084".replace(".", ""), ""),
    ("sibelga", "0222.867.266".replace(".", ""), "sibelga"),
    ("brugel", "0828.638.456".replace(".", ""), ""),
    # more WZC from google-style candidates
    ("wzc_de_wyngaerd", "0415273901", ""),
    ("wzc_huis_van_vrede", "0456789012", ""),
    ("wzc_olvh_diksmuide", "0408123456", ""),
    ("wzc_sint_anna_mol", "0412345678", ""),
    ("wzc_het_heiveld", "0425.846.789".replace(".", "") if False else "0425846789", ""),
]


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=40) as resp:
        return resp.read()


def parse(html: str):
    text = unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)))
    title = re.search(r"<title>([^<]+)</title>", html, re.I)
    lb = re.search(
        r"(?:Laatste balansjaar|Last balance sheet year|Dernier bilan)\s+(\d{4})",
        text,
        re.I,
    )
    euros = {m.group(1): m.groups()[1:] for m in PAT.finditer(html)}
    ftes = re.findall(r"([\d\.,]+)\s*FTE", text)
    neer = re.search(
        r"(?:neergelegd op|filed on|déposés le)\s+([\d\-]+)", text, re.I
    )
    return {
        "title": title.group(1)[:100] if title else "?",
        "year": lb.group(1) if lb else "?",
        "neer": neer.group(1) if neer else "?",
        "euros": euros,
        "ftes": ftes[:3],
        "text": text,
    }


# Real candidates with known KBOs
real = [
    ("wzc_sj_rumst", "0448190181"),
    ("wzc_xxe_aout", "0443082637"),
    ("cile", "0202395052"),
    ("sibelga", "0222867266"),
    ("aquafin", "0440691388"),
    ("sofico", "0860325064"),
    ("wzc_sj_rumst2", "0448190181"),
    # additional WZCs commonly public-interest VZW
    ("wzc_de_bijster_brasschaat", "0400375445"),  # may be wrong
    ("wzc_het_heiveld_schilde", "0412098765"),
    ("wzc_oline_berchem", "0452123456"),
    ("wzc_sint_anna", "0403205123"),
    ("wzc_olvl_lier", "0403205999"),
    ("wzc_gasthuiszusters", "0410399999"),
    ("wzc_huize_wallegem", "0475123456"),
    ("mrs_notre_dame", "0403211111"),
    ("intermosane", "0200122222"),
    ("alea", "0206611111"),
    ("resail", "0644111111"),
    ("ores_luxembourg", "0836222222"),
    ("rew_refresh", "0644638937"),
    ("aiesh_refresh", "0201712587"),
    ("faro_refresh", "0893863017"),
    # from northdata-style knowns
    ("wzc_sint_jozef_rumst", "0448190181"),
    ("wzc_avondvrede", "0408965432"),
    ("wzc_de_wynckel", "0421987654"),
    ("wzc_huize_ter_linde", "0412654321"),
    ("wzc_olvh_deerlijk", "0413765432"),
    ("wzc_rusthuis_heide", "0424876543"),
]

# Better: search companyweb pages we can resolve via known search results
# Plus probe known public hospital/IGS not in DO_NOT_REDO
real = [
    ("wzc_sj_rumst", "0448190181"),
    ("wzc_xxe_aout", "0443082637"),
    ("cile", "0202395052"),
    ("sibelga", "0222867266"),
    ("aquafin", "0440691388"),
    ("sofico", "0860325064"),
    ("brugel", "0828638456"),
    ("fluvius", "0477445084"),
    ("ores_assets", "0882591641"),  # likely taken
    ("tibi", "0200418803"),  # guess
    ("hygea", "0203200000"),
    ("ipalle", "0216695444"),  # guess
    ("inasep", "0206613594"),
    ("aide", "0200123450"),
    ("inbw", "0200123451"),
    ("spge", "0267440563"),
    ("hydria", "0679000000"),
    ("vivaqua", "0259000000"),
    ("aquiris", "0474000000"),
    # WZC candidates not in taken list from web
    ("wzc_sj_rumst_b", "0448190181"),
    ("wzc_molenheide_chk", "0810616132"),  # taken check
    ("wzc_christine_chk", "0421903676"),
]

for slug, kbo in real:
    dotted = f"{kbo[:4]}.{kbo[4:7]}.{kbo[7:]}"
    already = dotted in taken_text or kbo in taken_text or dotted in taken_lb
    try:
        body = fetch(f"https://www.companyweb.be/nl/{kbo}")
        (RAW / f"{slug}_nl.html").write_bytes(body)
        info = parse(body.decode("utf-8", "ignore"))
        if "Error 404" in info["title"] or info["year"] == "?":
            print(f"SKIP {slug} {kbo} already={already} title={info['title'][:60]}")
            continue
        e25 = info["euros"].get("2025")
        print(
            f"HIT {slug}|{kbo}|already={already}|y={info['year']}|neer={info['neer']}|"
            f"fte={info['ftes']}|e25={e25}|title={info['title'][:80]}"
        )
    except Exception as e:
        print(f"ERR {slug} {kbo} {type(e).__name__}: {e}")
