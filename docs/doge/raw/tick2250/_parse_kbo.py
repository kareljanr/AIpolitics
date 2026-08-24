from pathlib import Path
import re
t = Path(__file__).with_name("kbo.html").read_text(encoding="utf-8", errors="ignore")
m = re.search(r"vestigingseenheden \(VE\):.*?<strong>(\d+)", t, re.S)
print("VE", m.group(1) if m else "unknown")
m = re.search(r"mailto:([^\"']+)", t)
print("email", m.group(1) if m else "none")
