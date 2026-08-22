import pypdf, re
from pathlib import Path
r=pypdf.PdfReader(r"docs/doge/raw/tick1729/lsc_noordbrabant_nbb_2026-00109506.pdf")
parts=[]
for i,p in enumerate(r.pages):
    t=p.extract_text() or ""
    parts.append(f"===== PAGE {i+1} =====\n{t}")
    # print pages with money
    if re.search(r"(9900|9901|9904|20/58|10/15|9087|bruto|Codes|ACTIVA|RESULTAT)", t, re.I) or i<3:
        print(f"\n######## PAGE {i+1} chars {len(t)} ########")
        print(t[:2200])
Path(r"docs/doge/raw/tick1729/lsc_noordbrabant_extract.txt").write_text("\n\n".join(parts), encoding="utf-8")
print("saved", sum(len(x) for x in parts))
