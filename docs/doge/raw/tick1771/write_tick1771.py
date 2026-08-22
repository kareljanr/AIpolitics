import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1771'; utc='2026-08-24T17:30:00Z'
eid='vzw_vrienden_hofschoten'; sid='src_vrienden_hofschoten_jr2025_nbb'
gap='gap_vrienden_hofschoten_bruto_172_empty_70_73_vivalto_shell_l5'
lb='lb_vrienden_hofschoten_bruto_172_empty_70_73_0_vte_l5'
comm='comm_vrienden_hofschoten_jr2025_bruto_172'
hier='Vlaanderen>Provincies>Antwerpen>Gemeenten>Schoten>WZC>DeVriendenHofVanSchoten>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'De Vrienden van Hof van Schoten VZW NBB VKT-VZW YE2025 deposit 2026-00139428','http://cdn.staatsbladmonitor.be/2026pdf/2026-00139428.pdf','Nationale Bank van België / De Vrienden van Hof van Schoten VZW','2026-08-24','primary_official','tick1771; AV 08.05.2026; VKT-VZW; Vivalto Home Belgium gedelegeerd; Forvis Mazars/Collie oordeel zonder voorbehoud; Botermelkdijk 282 twin Hof van Schoten BV'])
    w.writerow(['src_vrienden_hofschoten_site','Vivalto Home — Hof van Schoten (friends VZW twin seat)','https://www.vivaltohome.com/nl/maisons/hof-van-schoten/','Vivalto Home','2026-08-24','primary_official','tick1771; Botermelkdijk 282 2900 Schoten; hofvanschoten@vivaltohome.com'])
    w.writerow(['src_vrienden_hofschoten_kbo','KBO De Vrienden van Hof van Schoten VZW 0526.901.129','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0526901129','KBO','2026-08-24','primary_official','tick1771; VZW; Botermelkdijk 282 2900 Schoten; RPR Antwerpen'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'De Vrienden van Hof van Schoten VZW (leftover Vivalto friends dual / Schoten)','Les Amis de Hof van Schoten ASBL (amis Vivalto residuel / Schoten)','De Vrienden van Hof van Schoten VZW leftover Vivalto friends dual Schoten','other','nv_vivalto_home_be','nl','https://www.vivaltohome.com/nl/maisons/hof-van-schoten/','hofvanschoten@vivaltohome.com','Botermelkdijk 282 2900 Schoten','tick1771 leftover Vivalto friends VZW dual after EVERY-10; KBO 0526.901.129 Actief; VZW; official NBB VKT-VZW YE2025 deposit 2026-00139428 CDN 200; AV 08.05.2026; moeder Vivalto Home Belgium gedelegeerd; commissaris Forvis Mazars/Collie oordeel zonder voorbehoud; seat twin Hof van Schoten BV 0501.918.481; 0 VTE near-empty shell; sourced euros assets 11074 equity 6674 debt 4400 bruto 172 omzet empty lidgeld/subs empty pnl 36; FOI ready empty 70/73 / activity / cashflow vs Hof BV'])

buds=[
 ('bud_vrienden_hofschoten_assets_2025',11074,'stock','Assets YE2025 11074 DROP vs 14373; tick1771'),
 ('bud_vrienden_hofschoten_equity_2025',6674,'stock','Equity 6674; tick1771'),
 ('bud_vrienden_hofschoten_debt_2025',4400,'stock','Debt 4400 trade ST; tick1771'),
 ('bud_vrienden_hofschoten_cash_2025',11074,'stock','Cash 11074 (= almost all assets); tick1771'),
 ('bud_vrienden_hofschoten_bruto_2025',172,'realized','Brutomarge 172 (VKT; omzet 70 + lidgeld/subs 73 empty); tick1771'),
 ('bud_vrienden_hofschoten_pnl_2025',36,'realized','PnL 36 TURNAROUND vs -570; tick1771'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'De Vrienden Hof van Schoten VZW JR2025 leftover Vivalto dual (bruto 172 / empty 70+73 / 0 VTE)',eid,'De Vrienden van Hof van Schoten VZW / Vivalto Home Belgium / Hof van Schoten dual','WVV VZW; Bestuursdecreet openbaarheid; Woonzorgdecreet cascade via twin','2026-05-08',2025,2025,172,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00139428.pdf','Local leftover Vivalto friends VZW map VL Schoten — near-empty shell twin Hof BV','Publish activity/omzet/lidgeld split + cashflow vs Hof van Schoten BV; explain Vivalto control of 11k shell',sid,'strong',hier,'tick1771; assets 11074 equity 6674 debt 4400 bruto 172 VTE 0 pnl 36; FOI ready not sent; not TE-additive; empty 70/73; twin bv_hofschoten'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'De Vrienden Hof van Schoten VZW 2025: bruto 172 / 0 VTE (empty 70+73 / Vivalto-controlled shell twin Hof BV)','L5','nursing_home_friends_dual',hier.replace('>JR2025_L5',''),172,11074,'Envelope=brutomarge 172 (VKT; omzet+lidgeld/subs empty); 0 VTE; assets=cash 11k; Vivalto Home Belgium gedelegeerd; seat twin Hof van Schoten BV Botermelkdijk 282','strong',sid,'Hof van Schoten residents / friends association dual / Vivalto group','Friends/support association for WZC','Near-empty Vivalto-controlled VZW with undisclosed 70/73 and tiny bruto; dual opacity vs operating Hof BV',4.5,1.5,3,3.6,'Publish activity + omzet/lidgeld + link to Hof BV cashflows; or dissolve unused shell','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB VKT-VZW YE2025 live bruto 172 but omzet 70 and lidgeld/schenkingen/subsidies 73 empty; 0 VTE; need activity description + any transfers with Hof van Schoten BV 0501.918.481; why Vivalto Home Belgium controls near-empty 11k shell; trade debt 4400 counterparties','Vivalto friends VZW dual at same seat as operating WZC with empty revenue codes — opacity on purpose and public/care-euro path',7,'De Vrienden van Hof van Schoten VZW / Vivalto Home Belgium NV','hofvanschoten@vivaltohome.com','Botermelkdijk 282 2900 Schoten',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1771; human-send only; Brembloem still no JR2025; AGB Bornem JR2024; NOT Rapsode continuum; twin bv_hofschoten already mined 1746'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1771':
        row['status']='done'
        row['title']='De Vrienden van Hof van Schoten VZW JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: De Vrienden van Hof van Schoten VZW leftover Vivalto friends dual after EVERY-10; '
            'KBO 0526.901.129 Actief; live JR2025 official NBB VKT-VZW PDF (203457 bytes 22p deposit 2026-00139428; AV 08.05.2026; '
            'Vivalto Home Belgium gedelegeerd; Forvis Mazars/Collie oordeel zonder voorbehoud); '
            'sourced euros assets 11074 equity 6674 debt 4400 bruto 172 VTE 0 pnl 36 omzet/73 empty; '
            'FOI ready not sent; twin Hof van Schoten BV already mined; NOT Rapsode continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1771 De Vrienden Hof Schoten leftover Vivalto friends residual; KBO 0526.901.129; live JR2025 NBB VKT-VZW PDF; sourced euros; FOI ready not sent; next rq_1772 residual dual L5'
        print('updated rq_1771'); break
else:
    raise SystemExit('missing')
if not any(r.get('task_id')=='rq_1772' for r in rows):
    rows.append({
        'task_id':'rq_1772','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1772 after 1771 De Vrienden Hof Schoten. Next every-10 is 1780. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200, '
                 'other IOED/HVZ (VBWest if JR euros live), other IGS/WZC. Do NOT redo DeVriendenHofSchoten/Rapsode/ImmoRJS continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1771 De Vrienden Hof Schoten; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/HVZ-VBWest/other-Vivalto-if-200; next every-10 1780'
    })
    print('spawned rq_1772')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)
print('OK')
