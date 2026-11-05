from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("docs/assets")
OUT.mkdir(parents=True, exist_ok=True)
BG=(14,11,25); PANEL=(30,22,45); PURPLE=(111,77,153); GOLD=(224,184,92)
TEXT=(245,235,255); MUTED=(183,166,207); RED=(170,43,78); BLUE=(83,126,194)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
def f(sz,b=False): return ImageFont.truetype(BOLD if b else FONT,sz)
def txt(d,xy,s,size=18,color=TEXT,b=False): d.text(xy,s,font=f(size,b),fill=color)
def box(d,xy,fill=PANEL,outline=PURPLE,w=3): d.rounded_rectangle(xy,radius=8,fill=fill,outline=outline,width=w)
def px(d,xy,c): d.rectangle(xy,fill=c)
def scale(im,n): return im.resize((im.width*n,im.height*n),Image.Resampling.NEAREST)
def sprite(): return Image.new("RGBA",(32,36),(0,0,0,0))

def finn():
 im=sprite(); d=ImageDraw.Draw(im)
 px(d,(5,17,10,28),(66,125,62)); px(d,(6,19,9,25),(108,162,80))
 px(d,(11,27,15,32),(48,97,169)); px(d,(19,27,23,32),(48,97,169))
 px(d,(10,31,16,34),(86,57,47)); px(d,(18,31,24,34),(86,57,47))
 px(d,(9,18,23,29),(47,120,202)); px(d,(7,20,10,27),(232,190,145)); px(d,(23,20,26,27),(232,190,145))
 px(d,(10,7,22,19),(242,206,166)); px(d,(8,5,24,13),(239,239,230)); px(d,(9,2,23,7),(239,239,230)); px(d,(6,7,9,12),(239,239,230)); px(d,(23,7,26,12),(239,239,230))
 px(d,(12,12,13,13),(26,22,32)); px(d,(19,12,20,13),(26,22,32)); px(d,(15,16,18,16),(160,81,73))
 return im
def jake():
 im=sprite(); d=ImageDraw.Draw(im)
 for xy in [(5,18,10,26),(22,18,27,25),(10,25,14,32),(19,25,23,32)]: px(d,xy,(222,158,47))
 px(d,(8,10,24,27),(246,188,57)); px(d,(5,14,27,23),(246,188,57)); px(d,(10,7,22,14),(246,188,57))
 px(d,(10,12,13,15),(255,248,221)); px(d,(19,12,22,15),(255,248,221)); px(d,(12,13,12,14),(25,21,28)); px(d,(20,13,20,14),(25,21,28))
 px(d,(15,16,18,18),(139,77,49)); px(d,(14,19,19,20),(255,229,181))
 return im
def marceline():
 im=sprite(); d=ImageDraw.Draw(im)
 px(d,(6,1,25,27),(26,23,39)); px(d,(5,8,9,30),(26,23,39)); px(d,(22,7,26,31),(26,23,39)); px(d,(8,25,11,33),(26,23,39))
 px(d,(11,6,21,17),(216,216,221)); px(d,(9,18,23,29),(90,94,112)); px(d,(7,19,10,27),(216,216,221)); px(d,(22,19,25,27),(216,216,221))
 px(d,(9,19,23,23),(141,45,65)); px(d,(13,11,14,12),(25,21,28)); px(d,(19,11,20,12),(25,21,28)); px(d,(15,15,18,15),(135,69,78))
 px(d,(11,29,15,34),(42,39,57)); px(d,(19,29,22,34),(42,39,57))
 return im
def bubblegum():
 im=sprite(); d=ImageDraw.Draw(im)
 px(d,(7,8,25,22),(236,122,177)); px(d,(5,14,9,26),(236,122,177)); px(d,(23,14,27,26),(236,122,177))
 px(d,(11,7,21,17),(255,207,220)); px(d,(9,18,23,30),(245,151,190)); px(d,(6,30,26,33),(196,102,161))
 px(d,(10,3,22,6),(241,196,79)); px(d,(10,1,12,4),(241,196,79)); px(d,(15,0,17,4),(241,196,79)); px(d,(20,1,22,4),(241,196,79))
 px(d,(13,11,14,12),(38,27,42)); px(d,(19,11,20,12),(38,27,42)); px(d,(16,14,18,14),(201,89,132))
 return im
def iceking():
 im=sprite(); d=ImageDraw.Draw(im)
 px(d,(6,18,26,33),(74,132,200)); px(d,(9,15,23,24),(99,166,218)); px(d,(11,32,15,35),(227,229,238)); px(d,(19,32,23,35),(227,229,238))
 px(d,(11,8,21,17),(241,207,171)); px(d,(8,16,24,23),(238,239,245)); px(d,(10,20,22,27),(238,239,245)); px(d,(13,24,19,29),(238,239,245))
 px(d,(20,12,25,14),(234,163,131)); px(d,(12,12,13,13),(29,26,37))
 px(d,(9,5,23,8),(218,224,237)); px(d,(9,2,12,6),(218,224,237)); px(d,(14,0,17,6),(218,224,237)); px(d,(20,2,23,6),(218,224,237)); px(d,(14,5,18,7),(103,176,218))
 return im
def bmo():
 im=sprite(); d=ImageDraw.Draw(im)
 px(d,(7,4,25,29),(79,179,162)); px(d,(9,6,23,27),(112,208,188)); px(d,(11,9,21,19),(36,77,83)); px(d,(12,10,20,18),(163,225,200))
 px(d,(14,12,14,13),(26,49,57)); px(d,(18,12,18,13),(26,49,57)); px(d,(15,16,17,16),(26,49,57))
 px(d,(11,21,13,23),(224,82,99)); px(d,(16,21,18,23),(240,198,87)); px(d,(21,21,22,23),(80,115,206))
 px(d,(10,29,13,34),(76,168,157)); px(d,(20,29,23,34),(76,168,157))
 return im

chars={"Finn":finn(),"Jake":jake(),"Marceline":marceline(),"Princess Bubblegum":bubblegum(),"Ice King":iceking(),"BMO":bmo()}
def board(title,sub,w=1400,h=900):
 im=Image.new("RGB",(w,h),BG); d=ImageDraw.Draw(im)
 d.rectangle((24,24,w-24,h-24),outline=PURPLE,width=4)
 txt(d,(64,48),title,36,GOLD,True); txt(d,(66,100),sub,18,MUTED)
 for x,y in [(90,135),(1260,125),(1300,730),(180,770),(720,130)]: d.rectangle((x,y,x+6,y+6),fill=PURPLE)
 return im,d

# 1) Character sprite roster
im,d=board("THE HOLLOW REALMS / CHARACTER PIXEL ART","16-bit sprite studies • Adventure Time roster candidates • final licensed art not included")
for i,(name,spr) in enumerate(chars.items()):
 x=64+(i%3)*438; y=160+(i//3)*340
 box(d,(x,y,x+400,y+300))
 d.rectangle((x+28,y+25,x+372,y+235),fill=(20,15,32),outline=(73,56,97),width=2)
 for gx in range(x+36,x+365,24): d.line((gx,y+32,gx,y+228),fill=(36,28,54),width=1)
 for gy in range(y+32,y+228,24): d.line((x+36,gy,x+364,gy),fill=(36,28,54),width=1)
 s=scale(spr,5); im.paste(s,(x+200-s.width//2,y+28),s)
 txt(d,(x+28,y+250),name.upper(),20,TEXT,True); txt(d,(x+28,y+278),"CLASS / SKILLS / STATS: TBD",13,MUTED)
txt(d,(66,860),"Visual study only. Confirm roster, mechanics and licensed source art before release.",14,(209,190,223))
im.save(OUT/"character-pixel-roster.png")

# 2) Weapons and passive Rune icon sheet
def item(kind):
 im=Image.new("RGBA",(48,48),(0,0,0,0)); d=ImageDraw.Draw(im)
 if kind=="Grass Sword":
  px(d,(22,3,25,29),(155,219,93)); px(d,(20,7,27,27),(112,191,74)); px(d,(22,3,23,26),(208,238,145))
  px(d,(14,26,32,29),(83,139,63)); px(d,(17,24,20,31),(83,139,63)); px(d,(27,24,30,31),(83,139,63)); px(d,(22,29,25,39),(129,84,53)); px(d,(20,38,27,42),(191,152,91))
 elif kind=="Demon Blood Sword":
  px(d,(22,3,25,29),(172,44,61)); px(d,(19,8,28,27),(205,54,68)); px(d,(22,4,23,26),(247,118,111))
  px(d,(13,25,34,29),(112,34,51)); px(d,(21,29,26,39),(107,67,54)); px(d,(18,38,29,42),(185,145,91)); px(d,(17,23,30,31),(124,39,54))
 else:
  # bass-guitar axe silhouette, diagonal neck and offset body
  px(d,(22,3,25,28),(115,73,57)); px(d,(23,5,24,27),(205,173,117))
  px(d,(13,23,23,34),(79,35,59)); px(d,(10,27,20,38),(151,43,67)); px(d,(18,30,31,38),(151,43,67))
  px(d,(20,26,29,33),(198,70,88)); px(d,(21,2,26,6),(225,190,112))
 return im
weapons={n:item(n) for n in ["Grass Sword","Demon Blood Sword","Bass Axe"]}
rune_colors={"ATK":(211,75,69),"HP":(204,71,111),"MANA":(86,155,220),"HEAL":(100,198,139),"DEF":(180,174,194),"CRIT":(222,184,83)}
def rune(name,color):
 im=Image.new("RGBA",(24,24),(0,0,0,0)); d=ImageDraw.Draw(im)
 d.polygon([(8,1),(16,1),(22,7),(22,16),(16,22),(8,22),(2,16),(2,7)],fill=color,outline=(245,230,255))
 d.rectangle((8,5,15,18),fill=tuple(int(c*.62) for c in color))
 if name=="ATK": d.polygon([(12,4),(8,13),(12,12),(10,19),(17,9),(13,10)],fill=(255,231,185))
 elif name=="HP": d.polygon([(12,18),(4,10),(5,6),(10,6),(12,9),(15,6),(20,6),(20,11)],fill=(255,232,239))
 elif name=="MANA": d.polygon([(12,3),(7,12),(8,17),(12,20),(17,17),(18,12)],fill=(220,241,255))
 elif name=="HEAL": d.rectangle((10,5,13,19),fill=(238,255,235)); d.rectangle((5,10,18,13),fill=(238,255,235))
 elif name=="DEF": d.polygon([(12,4),(19,7),(18,15),(12,20),(6,15),(5,7)],fill=(232,235,255),outline=(73,78,102)); d.line((8,12,11,15,16,9),fill=(79,128,117),width=2)
 else: d.polygon([(12,3),(14,9),(20,8),(16,13),(19,19),(12,16),(6,20),(8,13),(4,8),(10,9)],fill=(255,245,187))
 return im
runes={n:rune(n,c) for n,c in rune_colors.items()}
im,d=board("WEAPONS / RUNES / EQUIPMENT","Adventure Time item art studies + game-system passive Rune buff icons")
for i,(name,spr) in enumerate(weapons.items()):
 x=64+i*430; y=160; box(d,(x,y,x+390,y+315))
 d.rectangle((x+25,y+24,x+365,y+235),fill=(19,15,29),outline=(73,56,97),width=2)
 s=scale(spr,5); im.paste(s,(x+195-s.width//2,y+33),s)
 txt(d,(x+25,y+255),name.upper(),19,GOLD,True); txt(d,(x+25,y+285),"PIXEL ITEM STUDY",12,MUTED)
box(d,(64,510,1336,820)); txt(d,(92,540),"RUNE BUFF ICONS",22,GOLD,True)
for i,(name,spr) in enumerate(runes.items()):
 x=105+i*205; d.rectangle((x,592,x+150,758),fill=(22,17,35),outline=(83,65,109),width=2)
 s=scale(spr,4); im.paste(s,(x+75-s.width//2,608),s); txt(d,(x+54,730),name,15,TEXT,True)
txt(d,(92,785),"Passive buffs: Attack / HP / Mana / Healing / Defense / Critical. Rune icons are game-system artwork.",12,MUTED)
im.save(OUT/"weapons-runes-equipment.png")

# 3) Character collection cards; these are not combat cards/decks
im,d=board("CHARACTER COLLECTION CARDS","Collection UI only • no deck / no draw / no deck-based battle")
for i,(name,spr) in enumerate(list(chars.items())[:4]):
 x=64+i*326; y=170; box(d,(x,y,x+290,y+610))
 d.rectangle((x+15,y+15,x+275,y+55),fill=(60,40,77),outline=GOLD,width=2); txt(d,(x+28,y+26),"CHARACTER",14,GOLD,True)
 d.rectangle((x+25,y+80,x+265,y+330),fill=(19,15,29),outline=(87,68,117),width=2)
 s=scale(spr,6); im.paste(s,(x+145-s.width//2,y+89),s)
 txt(d,(x+25,y+355),name.upper(),18,TEXT,True); txt(d,(x+25,y+392),"CLASS: TBD",13,MUTED); txt(d,(x+25,y+425),"LEVEL: —   RARITY: TBD",12,MUTED)
 txt(d,(x+25,y+475),"HP",12,(223,116,139)); d.rectangle((x+75,y+473,x+250,y+488),fill=(61,47,73)); d.rectangle((x+77,y+475,x+190,y+486),fill=RED)
 txt(d,(x+25,y+508),"MP",12,(127,173,232)); d.rectangle((x+75,y+506,x+250,y+521),fill=(61,47,73)); d.rectangle((x+77,y+508,x+158,y+519),fill=BLUE)
 d.rectangle((x+25,y+550,x+265,y+590),fill=(57,42,82),outline=(126,99,164),width=2); txt(d,(x+53,y+562),"VIEW DETAILS",13,TEXT,True)
im.save(OUT/"character-collection-cards.png")

# 4) Battle / equipment interface concept
im,d=board("BATTLE + EQUIPMENT UI CONCEPT","Discord-ready presentation • team of three • Attack / Skill / Defend / Item")
box(d,(64,160,1336,485)); txt(d,(94,185),"TURN-BASED BATTLE / TEAM OF THREE",22,GOLD,True)
for i,(name,spr) in enumerate(list(chars.items())[:3]):
 x=100+i*265; d.rectangle((x,225,x+220,430),fill=(20,15,32),outline=(80,62,108),width=2)
 s=scale(spr,4); im.paste(s,(x+110-s.width//2,232),s); txt(d,(x+20,370),name,14,TEXT,True)
 d.rectangle((x+20,394,x+200,408),fill=(61,47,73)); d.rectangle((x+22,396,x+142,406),fill=RED); txt(d,(x+20,414),"HP —   MANA —",10,MUTED)
for i,label in enumerate(["ATTACK","SKILL","DEFEND","ITEM"]):
 x=930+(i%2)*175; y=255+(i//2)*70; d.rectangle((x,y,x+150,y+48),fill=(64,45,91),outline=GOLD,width=2); txt(d,(x+29,y+15),label,14,TEXT,True)
box(d,(64,520,1336,830)); txt(d,(94,545),"FIVE EQUIPMENT SLOTS",22,GOLD,True)
for i,label in enumerate(["WEAPON","ARMOR","RUNE","ACCESSORY 1","ACCESSORY 2"]):
 x=94+i*245; d.rectangle((x,595,x+215,785),fill=(20,15,32),outline=(86,66,115),width=2)
 if i==0: s=scale(weapons["Grass Sword"],3); im.paste(s,(x+107-s.width//2,602),s)
 elif i==2: s=scale(runes["HP"],4); im.paste(s,(x+107-s.width//2,620),s)
 else: d.rectangle((x+83,630,x+132,694),fill=(85,71,106),outline=GOLD,width=2); d.rectangle((x+73,646,x+142,657),fill=(116,95,137))
 txt(d,(x+20,735),label,12,TEXT,True); txt(d,(x+20,759),"ITEM SLOT",10,MUTED)
im.save(OUT/"battle-equipment-ui.png")

# 5) Crypt room path sample
im,d=board("THE HOLLOW CRYPT","Branching exploration map • persistent run condition • temporary Run Relics")
routes=[((220,360),(470,260)),((220,360),(470,500)),((470,260),(710,360)),((470,500),(710,360)),((710,360),(950,260)),((710,360),(950,500)),((950,260),(1170,360)),((950,500),(1170,360))]
for a,b in routes: d.line((a,b),fill=(122,92,165),width=7)
for x,y,label in [(220,360,"START"),(470,260,"BATTLE"),(470,500,"EVENT"),(710,360,"ELITE"),(950,260,"TREASURE"),(950,500,"MERCHANT"),(1170,360,"BOSS")]:
 col=(73,53,101) if label not in ("BOSS","ELITE") else (102,41,65)
 d.rounded_rectangle((x-82,y-38,x+82,y+38),radius=5,fill=col,outline=GOLD,width=3)
 bb=d.textbbox((0,0),label,font=f(15,True)); d.text((x-(bb[2]-bb[0])//2,y-10),label,font=f(15,True),fill=TEXT)
txt(d,(80,770),"Map and room schedule are examples only; final generation and reward rules remain open.",14,MUTED)
im.save(OUT/"hollow-crypt-map.png")

# Re-run asset generation after workflow setup.
