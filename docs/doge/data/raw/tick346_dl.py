import urllib.request
from pathlib import Path
import pypdf

raw = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data\raw")

urls = {
    "adeps_ra_2025.pdf": (
        "https://www.sport-adeps.be/index.php?eID=tx_nawsecuredl&u=0&g=0"
        "&hash=e78caca1086224a24e0033c7bf9a906ed32128a5"
        "&file=fileadmin/sites/adeps/upload/adeps_super_editor/adeps_editor/"
        "documents/A_propos/Rapports_annuels/Rapport_annuel_Adeps_2025_2.pdf"
    ),
    "adeps_audit_2025.pdf": (
        "https://www.sport-adeps.be/index.php?eID=tx_nawsecuredl&u=0&g=0"
        "&hash=d88f43b7e518d54ce043f85a3c14be028fd069bd"
        "&file=uploads/media/20251024_AGS_Audit_de_fonctionnement_Rapport_final_version_incl_retour_AGS__003_.pdf"
    ),
    "adeps_audit_synthese.pdf": (
        "https://www.sport-adeps.be/index.php?eID=tx_nawsecuredl&u=0&g=0"
        "&hash=598f58a167dde7310b1a8834db5a985bd0c480c6"
        "&file=uploads/media/Synthese_Recommendations_Audit_AGS.pdf"
    ),
}

for name, url in urls.items():
    path = raw / name
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=60).read()
        path.write_bytes(data)
        print(name, len(data), data[:4])
    except Exception as e:
        print(name, "ERR", e)

for name in ["adeps_ra_2025.pdf", "adeps_audit_2025.pdf", "adeps_audit_synthese.pdf"]:
    path = raw / name
    if not path.exists() or path.stat().st_size < 1000:
        continue
    try:
        r = pypdf.PdfReader(str(path))
        print(name, "pages", len(r.pages))
        text = ""
        for i, p in enumerate(r.pages[:50]):
            t = p.extract_text() or ""
            text += f"\n---PAGE {i+1}---\n" + t
        out = raw / (name.replace(".pdf", ".txt"))
        out.write_text(text, encoding="utf-8")
        print("wrote", out.name, len(text))
        # keyword hits
        for kw in [
            "budget",
            "Budget",
            "million",
            "€",
            "EUR",
            "crédit",
            "dotation",
            "subvention",
            "personnel",
            "dépenses",
            "recettes",
        ]:
            if kw.lower() in text.lower():
                pass
        # print lines with euros/m
        hits = []
        for line in text.splitlines():
            l = line.strip()
            if any(
                x in l.lower()
                for x in [
                    "million",
                    "budget",
                    "crédit",
                    "dotation",
                    "€",
                    "eur",
                    "subvention",
                    "personnel",
                    "effectif",
                    "fte",
                    "dépense",
                ]
            ):
                if len(l) < 180:
                    hits.append(l)
        print("--- HITS", name, len(hits))
        for h in hits[:80]:
            print(h)
    except Exception as e:
        print("parse", name, e)
