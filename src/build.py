import html, os
HERE=os.path.dirname(os.path.abspath(__file__))
import datetime
# ---- Change these once a year ----
AGE = 31                              # the age I'm turning
BIRTHDAY = datetime.date(2027, 4, 13) # the birthday this list runs up to
# -----------------------------------
G = [
 ("done","creative","Join a craft circle","May 2026","2026-05"),
 ("done","creative","Keep a visual diary","May 2026","2026-05"),
 ("done","community","Volunteer at an arts organisation","August 2026","2026-08"),
 ("done","creative",'Learn "She Used to Be Mine" on the keyboard',"August 2026","2026-08"),
 ("done","self","Write letters to my future self","September 2026","2026-09"),
 ("done","learn","Read 12 books","September 2026","2026-09"),
 ("done","creative","Dry meaningful flowers as keepsakes","October 2026","2026-10"),
 ("done","community","Mentor someone in my industry","October 2026","2026-10"),
 ("done","self","Choose a personal scent for the year: Princess by Vera Wang","October 2026","2026-10"),
 ("done","self","Write a portrait of my future self: habits, passions, character traits, appearance","October 2026","2026-10"),
 ("doing","creative","Commit to a long-term art programme: a term-long painting class or studio","Still at the research stage. Aiming to enrol by mid-January.","2027-01"),
 ("doing","creative","Thrift-flip an item of clothing","December. Maybe the AAG shirt, with my name stitched on.","2026-12"),
 ("doing","creative","Make a giant piece of art for my wall","Materials over Labour Day weekend, then painting through December.","2026-12"),
 ("todo","body","Cut down my drinking, one drink less each month","4 drinks in November, 3 in December, 2 in January, 1 in February, then none in March. Lol.","2027-03"),
 ("todo","body","Start a yoga practice","February.","2027-02"),
 ("todo","body","Get good at pool","One regular night a week, from mid-November.","2026-11"),
 ("todo","self","Get a new tattoo of something sentimental","March 2027.","2027-03"),
 ("todo","learn","Cook a 3-course meal from one specific cuisine","November.","2026-11"),
 ("todo","community","Plan and host a themed 31st birthday party","Planning from mid-December. The party is Saturday 10 April.","2027-04"),
 ("todo","creative","Make a zine of my life","Drawing it over the Christmas break.","2026-12"),
 ("todo","creative","Record and post a cover of a song","December.","2026-12"),
 ("todo","community","Start a polaroid wall of memories and friends","Late December.","2026-12"),
 ("todo","adventure","Hike somewhere","Over the Christmas break.","2026-12"),
 ("todo","home","Get a city pad or flat","April.","2027-04"),
 ("todo","body","Spend a whole weekend with my phone off","Boxing Day weekend. This one will be hard.","2026-12"),
 ("todo","creative","Sketch live at the AUM festival while I volunteer","30 December to 2 January.","2026-12"),
 ("todo","home","Reach inbox zero and clean up my digital clutter","November.","2026-11"),
 ("todo","body","Have a proper pamper day: massage, facial and hair","A free weekend in late January.","2027-01"),
 ("todo","creative","Learn pottery properly","November.","2026-11"),
 ("todo","adventure","Do one thing that properly scares me","February. I still have to decide what.","2027-02"),
 ("todo","adventure","Take a relaxing trip somewhere","March.","2027-03"),
]
EMO = {"creative":"🎨","community":"🫶","body":"🧘‍♀️","adventure":"✈️","self":"🌷","learn":"📚","home":"🏡"}
NAME = {"creative":"Creative and making","community":"Community and people","body":"Body and wellbeing","adventure":"Adventure and travel","self":"Self and identity","learn":"Learning and food","home":"Home and admin"}
lis=[]
for i,(st,cat,g,n,mo) in enumerate(G,1):
    badge = {"done":'<span class="badge b-done">done 💖</span>',"doing":'<span class="badge b-doing">in progress 🦋</span>',"todo":""}[st]
    lis.append(f'''    <li class="goal {st}" id="goal-{i}" data-st="{st}" data-cat="{cat}" data-mo="{mo}">
      <span class="num">{i}</span>
      <span class="emo" role="img" aria-label="{NAME[cat]}">{EMO[cat]}</span>
      <div class="body"><span class="g">{html.escape(g)}</span>{badge}{('<span class="n">'+html.escape(n)+'</span>') if n else ''}</div>
    </li>''')
MN=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
MONTHS=[]
for k in range(11,-1,-1):
    y,m=BIRTHDAY.year,BIRTHDAY.month-k
    while m<1: m+=12; y-=1
    MONTHS.append((f"{y}-{m:02d}",MN[m-1]))
MONTHS.append(("tbc","No date yet"))
FIRSTS={MONTHS[0][0]}|{k for k,_ in MONTHS if k.endswith("-01")}
LBL={"done":"done","doing":"in progress","todo":"still to do"}
groups=[]
for key,lab in MONTHS:
    hb=[]
    for i,(st,cat,g,n,mo) in enumerate(G,1):
        if mo!=key: continue
        hb.append(f'<a class="h {st}" href="#goal-{i}" data-tip="{i}. {html.escape(g)}" aria-label="Goal {i}: {html.escape(g)}, {LBL[st]}">♥</a>')
    if key=='tbc' and not hb: continue
    inner=''.join(hb) if hb else '<span class="none" aria-hidden="true">·</span>'
    yr=' ’'+key[2:4] if key in FIRSTS else ''
    groups.append(f'<div class="mo{" empty" if not hb else ""}"><div class="mh">{inner}</div><span class="ml">{lab}{yr}</span></div>')
hearts=groups
tpl=open(os.path.join(HERE,'page.html')).read()
DAYS=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
LONG=f"{DAYS[BIRTHDAY.weekday()]} {BIRTHDAY.day} {BIRTHDAY.strftime('%B')} {BIRTHDAY.year}"
out=tpl.replace('%%GOALS%%','\n'.join(lis)).replace('%%HEARTS%%','\n      '.join(hearts)).replace('%%AGE%%',str(AGE)).replace('%%COUNT%%',str(len(G))).replace('%%BDAY_LONG%%',LONG).replace('%%BDAY_JS%%',f'{BIRTHDAY.year},{BIRTHDAY.month-1},{BIRTHDAY.day}')
def standalone(src):
    i=src.index('<style>'); head=src[:i].replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
    rest=src[i:]; j=rest.index('</style>')+8
    style=rest[:j].replace('<style>','<style>\n[hidden]{display:none!important}\nhtml{scroll-padding-top:env(safe-area-inset-top,0px)}',1)
    return ('<!DOCTYPE html>\n<html lang="en-NZ">\n<head>\n<meta charset="utf-8">\n'
      '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
      f'<meta name="description" content="{AGE} things I want to do before I turn {AGE}.">\n'
      f'<meta property="og:title" content="{AGE} before {AGE} 💕">\n'
      f'<meta property="og:description" content="{AGE} things I want to do before I turn {AGE}: some new, some borrowed and some scary.">\n'
      '<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🎂</text></svg>">\n'
      +head+style+'\n</head>\n<body>\n'+rest[j:].strip()+'\n</body>\n</html>\n')
open(os.path.join(HERE,'..','index.html'),'w').write(standalone(out))
import sys
if '--artifact' in sys.argv:  # also write the Claude artifact version
    open(sys.argv[sys.argv.index('--artifact')+1],'w').write(out)
print(len(G))
