from pathlib import Path
import re
html=Path("/workspace/AIpolitics/docs/doge/raw/tick2474/hupskadee_kbo.html").read_text(errors="replace")
ve=Path("/workspace/AIpolitics/docs/doge/raw/tick2474/hupskadee_kbo_ve.html").read_text(errors="replace")
# strip tags loosely
def vis(s):
    s=re.sub(r'<script[\s\S]*?</script>',' ',s)
    s=re.sub(r'<style[\s\S]*?</style>',' ',s)
    s=re.sub(r'<[^>]+>','\n',s)
    s=re.sub(r'&nbsp;',' ',s)
    s=re.sub(r'&amp;','&',s)
    s=re.sub(r'\n+','\n',s)
    return s
t=vis(html)
Path("/workspace/AIpolitics/docs/doge/raw/tick2474/hupskadee_kbo.txt").write_text(t)
print(t[:6000])
print("\n===== VE =====\n")
print(vis(ve)[:4000])
