import pypdf
import re
from pathlib import Path

r = pypdf.PdfReader(r"docs/doge/data/raw/56K1281005.pdf")
results = []
for i, p in enumerate(r.pages):
    t = p.extract_text() or ""
    for m in re.finditer(r"B\.A\.\s*:\s*(12\.\d{2}\.\d{2}\.\d{6})", t):
        ba = m.group(1)
        start = max(0, m.start() - 300)
        end = min(len(t), m.end() + 900)
        ctx = t[start:end]
        series = re.findall(r"Vastleggingen\s+([\d\.\s\-]+)\s+Engagement", ctx)
        liq = re.findall(r"Vereffeningen\s+([\d\.\s\-]+)\s+Liquidation", ctx)
        lab_nl = re.search(r"Tekst\s*:\s*([^\n]+)", ctx)
        lab_fr = re.search(r"Libell[eé]\s*:\s*([^\n]+)", ctx)
        results.append(
            {
                "page": i + 1,
                "ba": ba,
                "nl": lab_nl.group(1).strip() if lab_nl else "",
                "fr": lab_fr.group(1).strip() if lab_fr else "",
                "eng": series[0].strip() if series else "",
                "liq": liq[0].strip() if liq else "",
            }
        )

print("BA count", len(results))
out_lines = []
for res in results:
    eng = res["eng"]
    nums = [x.replace(".", "") for x in eng.split() if re.match(r"[\d\.]+", x) and x != "-"]
    if len(nums) >= 3:
        try:
            y2026 = int(nums[2])
        except ValueError:
            continue
        if y2026 >= 3000:  # >= 3m EUR
            line = f"p{res['page']} {res['ba']} 2026={y2026}k eng=[{eng}] | {res['nl'][:100]}"
            print(line)
            out_lines.append(line)

Path("docs/doge/data/raw/tick747_justice_large_ba.txt").write_text(
    "\n".join(out_lines), encoding="utf-8"
)
print("wrote", len(out_lines))
