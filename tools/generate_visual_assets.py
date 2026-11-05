from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path("docs/assets")
OUT.mkdir(parents=True, exist_ok=True)
BG=(14,11,25); PANEL=(30,22,45); PURPLE=(111,77,153); GOLD=(224,184,92)
TEXT=(245,235,255); MUTED=(183,166,207); RED=(170,43,78); BLUE=(83,126,194)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)

def txt(draw, xy, value, size=18, color=TEXT, bold=False):
    draw.text(xy, value, font=font(size,bold), fill=color)

def panel(draw, xy, fill=PANEL, outline=PURPLE, width=3):
    draw.rounded_rectangle(xy, radius=8, fill=fill, outline=outline, width=width)

def rect(draw, xy, color, outline=None, width=1):
    draw.rectangle(xy, fill=color, outline=outline, width=width if outline else 1)

def scale_nearest(image, factor):
    return image.resize((image.width*factor,image.height*factor), Image.Resampling.NEAREST)

def sprite_canvas():
    return Image.new("RGBA",(64,72),(0,0,0,0))

# All character sprites are manually drawn as pixel clusters on a 64x72 canvas.
# This makes the silhouettes and shading much more detailed than the first 32x36 study.
def finn():
    im=sprite_canvas(); d=ImageDraw.Draw(im)
    # Backpack and straps
    rect(d,(38,31,52,52),(48,91,58)); rect(d,(40,33,49,49),(86,133,76))
    rect(d,(38,34,41,47),(174,187,112)); rect(d,(42,35,48,38),(122,161,90))
    # Legs and boots
    rect(d,(23,52,31,64),(48,85,151)); rect(d,(36,52,44,64),(48,85,151))
    rect(d,(19,63,32,68),(109,70,47)); rect(d,(34,63,48,68),(109,70,47))
    rect(d,(20,63,31,64),(171,119,74)); rect(d,(35,63,46,64),(171,119,74))
    # Blue shirt and sleeves
    rect(d,(20,32,45,55),(47,112,190)); rect(d,(23,35,42,51),(61,139,218))
    rect(d,(16,35,22,49),(232,188,143)); rect(d,(43,35,49,49),(232,188,143))
    rect(d,(15,44,22,49),(213,159,119)); rect(d,(44,44,51,49),(213,159,119))
    rect(d,(24,51,42,55),(31,82,154))
    # Hat outer silhouette, ears and inner face
    rect(d,(17,7,24,18),(228,231,222)); rect(d,(40,7,47,18),(228,231,222))
    rect(d,(14,13,50,31),(244,244,231)); rect(d,(18,7,46,22),(244,244,231))
    rect(d,(21,13,43,31),(238,194,158)); rect(d,(24,17,40,30),(248,211,174))
    rect(d,(15,14,18,23),(214,220,214)); rect(d,(46,14,49,23),(214,220,214))
    # Hat details, seams and face
    rect(d,(20,9,24,12),(255,255,246)); rect(d,(40,9,44,12),(255,255,246))
    rect(d,(20,27,44,31),(228,231,222)); rect(d,(25,14,28,16),(42,35,42))
    rect(d,(38,14,41,16),(42,35,42)); rect(d,(23,19,25,20),(232,142,136))
    rect(d,(42,19,44,20),(232,142,136)); rect(d,(31,22,36,23),(165,91,82))
    rect(d,(28,25,38,26),(185,101,91))
    # Pixel outline accents
    rect(d,(17,12,19,13),(210,214,206)); rect(d,(46,12,48,13),(210,214,206))
    rect(d,(25,34,27,36),(112,174,232)); rect(d,(39,34,41,36),(112,174,232))
    return im

def jake():
    im=sprite_canvas(); d=ImageDraw.Draw(im)
    # Tail and limbs
    rect(d,(45,39,57,47),(192,125,35)); rect(d,(51,35,58,41),(232,174,54))
    rect(d,(15,43,22,59),(207,143,39)); rect(d,(42,43,49,59),(207,143,39))
    rect(d,(11,56,24,64),(174,112,35)); rect(d,(40,56,53,64),(174,112,35))
    rect(d,(14,56,22,60),(244,193,76)); rect(d,(42,56,50,60),(244,193,76))
    # Main body and head
    rect(d,(10,20,53,51),(244,181,48)); rect(d,(7,28,57,45),(255,197,66))
    rect(d,(14,14,49,39),(251,194,59)); rect(d,(10,19,53,36),(244,181,48))
    # Ears
    rect(d,(8,15,17,29),(224,151,42)); rect(d,(9,16,14,24),(255,198,64))
    rect(d,(45,15,54,29),(224,151,42)); rect(d,(48,16,53,24),(255,198,64))
    # Snout and cheeks
    rect(d,(20,29,45,43),(255,215,126)); rect(d,(24,32,42,40),(255,224,153))
    rect(d,(17,31,22,35),(255,207,98)); rect(d,(44,31,48,35),(255,207,98))
    # Eyes and smile
    rect(d,(22,24,26,29),(255,250,220)); rect(d,(38,24,42,29),(255,250,220))
    rect(d,(24,25,25,28),(35,29,35)); rect(d,(39,25,40,28),(35,29,35))
    rect(d,(30,34,34,36),(134,71,44)); rect(d,(27,38,38,39),(134,71,44))
    rect(d,(29,40,36,41),(255,239,189))
    # Highlights and shadows
    rect(d,(17,19,28,21),(255,218,113)); rect(d,(34,19,46,21),(255,218,113))
    rect(d,(13,43,18,48),(217,148,42)); rect(d,(45,43,50,48),(217,148,42))
    return im

def marceline():
    im=sprite_canvas(); d=ImageDraw.Draw(im)
    # Long legs and boots
    rect(d,(24,49,30,65),(45,39,57)); rect(d,(37,49,43,65),(45,39,57))
    rect(d,(21,63,31,69),(26,22,35)); rect(d,(35,63,46,69),(26,22,35))
    rect(d,(23,63,29,65),(103,51,78)); rect(d,(38,63,43,65),(103,51,78))
    # Dress and arms
    rect(d,(20,34,47,55),(73,42,70)); rect(d,(23,37,44,51),(112,45,83))
    rect(d,(15,36,21,50),(205,205,214)); rect(d,(46,36,52,50),(205,205,214))
    rect(d,(16,48,20,52),(178,180,194)); rect(d,(47,48,51,52),(178,180,194))
    rect(d,(25,52,42,55),(42,27,52))
    # Hair mass behind head
    rect(d,(9,4,48,37),(27,24,40)); rect(d,(5,12,18,51),(32,27,47))
    rect(d,(42,9,54,47),(32,27,47)); rect(d,(10,39,18,59),(24,20,36))
    rect(d,(44,38,51,58),(24,20,36))
    # Face
    rect(d,(18,12,44,35),(218,218,226)); rect(d,(22,15,41,33),(233,231,235))
    rect(d,(18,18,22,29),(201,201,214)); rect(d,(42,18,45,29),(201,201,214))
    # Bangs, eyes, lips
    rect(d,(15,7,48,18),(31,27,44)); rect(d,(20,9,41,14),(42,35,55))
    rect(d,(25,22,28,24),(40,31,42)); rect(d,(37,22,40,24),(40,31,42))
    rect(d,(29,28,36,29),(159,67,93)); rect(d,(31,29,35,30),(194,94,111))
    # Red belt and pendant
    rect(d,(23,43,44,46),(173,45,70)); rect(d,(31,43,36,49),(225,184,104))
    rect(d,(32,48,35,51),(112,180,206))
    # Hair highlights
    rect(d,(12,10,17,21),(70,61,83)); rect(d,(45,15,49,26),(67,57,82))
    rect(d,(12,36,16,47),(58,48,73)); rect(d,(48,36,51,45),(58,48,73))
    return im

def bubblegum():
    im=sprite_canvas(); d=ImageDraw.Draw(im)
    # Legs and shoes
    rect(d,(24,53,30,65),(246,165,195)); rect(d,(37,53,43,65),(246,165,195))
    rect(d,(20,63,32,68),(171,78,139)); rect(d,(35,63,48,68),(171,78,139))
    # Dress and sleeves
    rect(d,(19,34,48,56),(244,127,178)); rect(d,(24,37,43,51),(255,164,199))
    rect(d,(14,36,22,51),(255,207,221)); rect(d,(45,36,52,51),(255,207,221))
    rect(d,(25,51,43,55),(211,87,155)); rect(d,(30,39,36,48),(255,211,225))
    # Hair silhouette
    rect(d,(9,9,52,37),(243,139,190)); rect(d,(13,5,48,19),(251,169,205))
    rect(d,(8,17,15,33),(230,111,176)); rect(d,(46,17,53,33),(230,111,176))
    rect(d,(12,28,18,41),(243,139,190)); rect(d,(44,28,50,41),(243,139,190))
    # Face and neck
    rect(d,(19,13,43,34),(255,222,211)); rect(d,(23,17,40,31),(255,232,222))
    rect(d,(18,19,21,29),(245,194,193)); rect(d,(42,19,45,29),(245,194,193))
    # Crown
    rect(d,(23,3,40,9),(235,187,75)); rect(d,(20,7,44,11),(241,204,93))
    rect(d,(25,1,29,5),(255,228,128)); rect(d,(32,0,36,5),(255,228,128)); rect(d,(39,2,42,6),(255,228,128))
    rect(d,(30,5,35,8),(111,177,208))
    # Face details
    rect(d,(25,22,28,24),(56,40,54)); rect(d,(36,22,39,24),(56,40,54))
    rect(d,(30,28,35,29),(210,111,135)); rect(d,(29,27,36,27),(243,161,171))
    # Highlights and seams
    rect(d,(14,12,18,16),(255,194,218)); rect(d,(44,13,48,17),(255,194,218))
    rect(d,(26,37,29,39),(255,201,220)); rect(d,(39,37,42,39),(255,201,220))
    return im

def iceking():
    im=sprite_canvas(); d=ImageDraw.Draw(im)
    # Robe and feet
    rect(d,(14,35,51,59),(61,119,191)); rect(d,(19,39,46,55),(86,157,218))
    rect(d,(20,56,28,66),(225,232,242)); rect(d,(38,56,46,66),(225,232,242))
    rect(d,(16,64,30,69),(51,85,143)); rect(d,(36,64,50,69),(51,85,143))
    # Arms and robe trim
    rect(d,(9,39,17,54),(88,152,213)); rect(d,(49,39,57,54),(88,152,213))
    rect(d,(14,51,51,56),(199,224,242)); rect(d,(30,43,36,55),(226,238,247))
    # Face
    rect(d,(20,12,43,35),(240,203,168)); rect(d,(25,15,41,31),(247,218,184))
    rect(d,(18,18,22,29),(224,187,157)); rect(d,(41,18,46,29),(224,187,157))
    # Nose, eye
    rect(d,(35,22,52,27),(235,160,145)); rect(d,(48,23,54,26),(217,126,123))
    rect(d,(24,20,27,22),(36,38,61)); rect(d,(29,20,32,22),(36,38,61))
    # Long white beard
    rect(d,(20,30,44,46),(235,239,243)); rect(d,(23,37,41,53),(249,250,251))
    rect(d,(25,48,30,57),(229,233,242)); rect(d,(36,48,41,57),(229,233,242))
    rect(d,(29,53,37,61),(242,245,249))
    # Crown base and spikes
    rect(d,(17,8,47,14),(206,220,234)); rect(d,(20,5,26,10),(220,232,242))
    rect(d,(29,1,34,9),(220,232,242)); rect(d,(38,4,44,10),(220,232,242))
    rect(d,(29,4,34,10),(93,168,220)); rect(d,(21,7,24,10),(129,194,234))
    # Blue shadows and accents
    rect(d,(15,43,20,51),(50,106,179)); rect(d,(45,43,50,51),(50,106,179))
    rect(d,(26,32,39,35),(218,225,238))
    return im

def bmo():
    im=sprite_canvas(); d=ImageDraw.Draw(im)
    # Legs and arms
    rect(d,(18,57,25,66),(62,151,140)); rect(d,(39,57,46,66),(62,151,140))
    rect(d,(15,64,27,69),(40,111,112)); rect(d,(37,64,49,69),(40,111,112))
    rect(d,(8,31,15,44),(49,155,144)); rect(d,(49,31,56,44),(49,155,144))
    rect(d,(7,41,15,48),(83,198,180)); rect(d,(49,41,57,48),(83,198,180))
    # Console shell
    rect(d,(14,7,50,59),(49,157,147)); rect(d,(17,9,47,55),(88,197,181))
    rect(d,(19,12,45,38),(24,58,67)); rect(d,(21,14,43,35),(165,224,208))
    rect(d,(22,15,42,17),(189,241,220)); rect(d,(22,32,42,34),(108,181,168))
    # Face on screen
    rect(d,(26,21,29,23),(31,52,58)); rect(d,(37,21,40,23),(31,52,58))
    rect(d,(29,29,37,30),(31,52,58)); rect(d,(27,28,29,29),(31,52,58))
    rect(d,(38,28,39,29),(31,52,58))
    # Buttons and control pad
    rect(d,(20,42,28,47),(224,83,96)); rect(d,(32,42,39,47),(237,193,83))
    rect(d,(41,42,46,47),(93,127,207)); rect(d,(23,49,28,52),(229,225,180))
    rect(d,(36,49,41,52),(229,225,180))
    # Shell highlights / screws / feet
    rect(d,(16,10,19,18),(142,223,202)); rect(d,(44,10,47,17),(142,223,202))
    rect(d,(16,55,48,58),(48,128,123)); rect(d,(15,8,18,11),(197,239,222))
    rect(d,(46,8,49,11),(197,239,222))
    return im

characters={
    "Finn":finn(),
    "Jake":jake(),
    "Marceline":marceline(),
    "Princess Bubblegum":bubblegum(),
    "Ice King":iceking(),
    "BMO":bmo()
}

def board(title, subtitle, width=1600, height=1000):
    image=Image.new("RGB",(width,height),BG); draw=ImageDraw.Draw(image)
    draw.rectangle((24,24,width-24,height-24),outline=PURPLE,width=4)
    txt(draw,(64,48),title,36,GOLD,True)
    txt(draw,(66,102),subtitle,18,MUTED)
    return image,draw

# Character sprites: larger source canvas, more color clusters, face/outfit details and shading.
image,draw=board("THE HOLLOW REALMS / CHARACTER SPRITES","Detailed 64x72 pixel studies • Adventure Time roster candidates • not final licensed assets")
for index,(name,sprite) in enumerate(characters.items()):
    x=64+(index%3)*500; y=160+(index//3)*390
    panel(draw,(x,y,x+460,y+350))
    draw.rectangle((x+28,y+24,x+432,y+280),fill=(19,15,30),outline=(73,56,97),width=2)
    for gx in range(x+36,x+428,24): draw.line((gx,y+30,gx,y+274),fill=(32,25,47),width=1)
    for gy in range(y+30,y+275,24): draw.line((x+36,gy,x+424,gy),fill=(32,25,47),width=1)
    enlarged=scale_nearest(sprite,4)
    image.paste(enlarged,(x+230-enlarged.width//2,y+36),enlarged)
    txt(draw,(x+28,y+293),name.upper(),21,TEXT,True)
    txt(draw,(x+28,y+324),"CLASS / SKILLS / STATS: PENDING",13,MUTED)
txt(draw,(66,952),"Detailed pixel studies • 64x72 base sprites enlarged with nearest-neighbor scaling.",14,(209,190,223))
image.save(OUT/"character-pixel-roster.png")

# Pixel-art item icons.
def weapon_icon(kind):
    im=Image.new("RGBA",(64,64),(0,0,0,0)); d=ImageDraw.Draw(im)
    if kind=="Grass Sword":
        rect(d,(28,5,35,42),(90,150,56)); rect(d,(31,4,34,39),(178,222,115))
        rect(d,(24,10,39,29),(111,183,67)); rect(d,(28,7,30,18),(219,242,160))
        rect(d,(19,28,25,34),(100,166,70)); rect(d,(38,26,44,33),(100,166,70))
        rect(d,(27,39,36,47),(120,80,51)); rect(d,(24,45,40,49),(153,104,65))
        rect(d,(29,49,35,58),(202,167,101)); rect(d,(25,57,39,60),(226,203,144))
        rect(d,(29,12,34,31),(210,239,146))
    elif kind=="Demon Blood Sword":
        rect(d,(29,5,35,43),(111,28,48)); rect(d,(27,8,38,37),(179,42,61))
        rect(d,(30,5,32,35),(245,116,108)); rect(d,(25,12,28,28),(216,67,78))
        rect(d,(22,32,42,37),(117,32,52)); rect(d,(18,30,25,39),(117,32,52))
        rect(d,(39,29,46,38),(117,32,52)); rect(d,(30,39,35,51),(104,69,54))
        rect(d,(26,50,39,54),(176,136,81)); rect(d,(28,54,37,59),(218,184,111))
        rect(d,(29,13,35,17),(255,163,133)); rect(d,(27,23,37,27),(214,65,84))
    else:
        # Bass Axe: guitar body, frets, strings, neck and headstock.
        rect(d,(9,33,30,51),(85,34,61)); rect(d,(13,29,31,47),(151,42,70))
        rect(d,(24,34,41,51),(151,42,70)); rect(d,(29,29,40,44),(191,60,82))
        rect(d,(17,35,26,43),(224,173,99)); rect(d,(20,38,25,43),(36,27,43))
        rect(d,(31,31,36,38),(224,173,99)); rect(d,(32,35,36,42),(36,27,43))
        rect(d,(35,21,42,34),(105,67,53)); rect(d,(39,12,46,28),(105,67,53))
        rect(d,(42,5,49,18),(105,67,53)); rect(d,(44,3,53,9),(204,165,102))
        rect(d,(39,15,41,28),(238,211,151)); rect(d,(35,24,37,34),(238,211,151))
        rect(d,(42,8,50,11),(219,186,125)); rect(d,(13,31,20,35),(218,76,98))
    return im

weapons={name:weapon_icon(name) for name in ("Grass Sword","Demon Blood Sword","Bass Axe")}

rune_palette={
    "ATK":(211,75,69),"HP":(204,71,111),"MANA":(86,155,220),
    "HEAL":(100,198,139),"DEF":(180,174,194),"CRIT":(222,184,83)
}
def rune_icon(name,color):
    im=Image.new("RGBA",(40,40),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.polygon([(13,2),(27,2),(37,12),(37,27),(27,37),(13,37),(3,27),(3,12)],fill=(49,35,68),outline=(246,229,255))
    d.polygon([(14,6),(26,6),(33,13),(33,26),(26,33),(14,33),(7,26),(7,13)],fill=color,outline=(255,245,220))
    shade=tuple(max(0,int(v*.58)) for v in color)
    rect(d,(15,10,25,30),shade)
    if name=="ATK":
        d.polygon([(22,8),(13,22),(20,20),(17,31),(29,16),(22,18)],fill=(255,233,183))
    elif name=="HP":
        d.polygon([(20,30),(8,18),(9,12),(15,11),(20,16),(25,11),(32,13),(32,19)],fill=(255,232,239))
    elif name=="MANA":
        d.polygon([(20,8),(12,20),(14,28),(20,33),(27,28),(29,20)],fill=(221,242,255))
        rect(d,(18,14,21,26),(255,255,255))
    elif name=="HEAL":
        rect(d,(17,10,23,30),(238,255,235)); rect(d,(10,17,30,23),(238,255,235))
    elif name=="DEF":
        d.polygon([(20,9),(31,14),(29,25),(20,32),(11,25),(9,14)],fill=(231,238,252),outline=(66,74,99))
        d.line((14,21,18,25,27,16),fill=(79,142,114),width=3)
    else:
        d.polygon([(20,8),(24,17),(33,15),(27,22),(31,31),(20,27),(10,32),(13,22),(7,15),(17,17)],fill=(255,245,187))
    return im
runes={name:rune_icon(name,color) for name,color in rune_palette.items()}

# Accessories are shape studies only; final named items must be sourced from approved Adventure Time content.
def accessory_icon(kind):
    im=Image.new("RGBA",(48,48),(0,0,0,0)); d=ImageDraw.Draw(im)
    gold=(221,179,92); light=(255,229,151); silver=(188,205,224)
    gem=(100,167,205); redgem=(190,61,91); dark=(68,43,74)
    if kind=="Pendant":
        d.arc((9,3,39,36),start=0,end=180,fill=gold,width=4)
        d.polygon([(24,18),(33,30),(24,42),(15,30)],fill=gem,outline=light)
        rect(d,(22,29,26,35),(202,231,239))
    elif kind=="Ring":
        d.ellipse((8,14,40,42),fill=gold,outline=light,width=3); d.ellipse((16,22,32,35),fill=BG)
        d.polygon([(24,4),(33,12),(24,19),(15,12)],fill=redgem,outline=light)
        rect(d,(21,16,27,21),silver)
    elif kind=="Bracelet":
        d.arc((5,7,43,43),start=0,end=360,fill=gold,width=6)
        for x,y in [(8,21),(18,7),(31,8),(40,21),(30,39),(16,39)]:
            rect(d,(x,y,x+3,y+3),light)
        d.polygon([(24,1),(29,7),(24,13),(19,7)],fill=gem,outline=light)
    elif kind=="Brooch":
        d.polygon([(24,3),(29,17),(43,18),(32,27),(36,42),(24,33),(12,42),(16,27),(5,18),(19,17)],fill=gold,outline=light)
        d.polygon([(24,12),(28,21),(36,21),(29,27),(31,35),(24,30),(17,35),(19,27),(12,21),(20,21)],fill=gem)
    elif kind=="Charm":
        rect(d,(22,2,26,12),silver); d.ellipse((18,8,30,20),outline=gold,width=3)
        d.polygon([(24,17),(34,27),(24,41),(14,27)],fill=redgem,outline=light)
        rect(d,(22,24,26,31),(255,191,157))
    elif kind=="Buckle":
        d.rounded_rectangle((5,14,43,37),radius=5,fill=gold,outline=light,width=3)
        d.rounded_rectangle((12,19,36,32),radius=3,fill=dark,outline=silver,width=2)
        d.polygon([(24,19),(29,26),(24,32),(19,26)],fill=gem,outline=light)
    elif kind=="Medallion":
        d.ellipse((7,5,41,41),fill=gold,outline=light,width=3)
        d.ellipse((12,10,36,36),fill=(83,56,104),outline=(246,223,151),width=2)
        d.polygon([(24,13),(28,22),(35,24),(28,28),(24,35),(20,28),(13,24),(20,22)],fill=gem)
    elif kind=="Watch":
        rect(d,(21,2,27,11),gold); rect(d,(21,37,27,46),gold)
        d.ellipse((7,9,41,41),fill=(166,180,197),outline=light,width=3)
        d.ellipse((12,14,36,36),fill=(31,29,47),outline=gold,width=2)
        rect(d,(23,17,25,25),light); rect(d,(24,24,31,26),light)
    return im

accessories={name:accessory_icon(name) for name in ("Pendant","Ring","Bracelet","Brooch","Charm","Buckle","Medallion","Watch")}

# Weapons / Runes / Accessory sheet.
image,draw=board("WEAPONS / RUNES / ACCESSORIES","Higher-detail pixel icons • Adventure Time weapon studies + generic accessory shape studies")
for index,(name,sprite) in enumerate(weapons.items()):
    x=64+index*500; y=150; panel(draw,(x,y,x+450,y+300))
    draw.rectangle((x+28,y+22,x+422,y+205),fill=(18,14,29),outline=(73,56,97),width=2)
    enlarged=scale_nearest(sprite,3)
    image.paste(enlarged,(x+225-enlarged.width//2,y+30),enlarged)
    txt(draw,(x+25,y+225),name.upper(),18,GOLD,True)
    txt(draw,(x+25,y+258),"FRANCHISE ITEM STUDY",12,MUTED)
panel(draw,(64,485,1536,690)); txt(draw,(91,505),"PASSIVE RUNE BUFFS",20,GOLD,True)
for index,(name,sprite) in enumerate(runes.items()):
    x=116+index*225
    enlarged=scale_nearest(sprite,3); image.paste(enlarged,(x,545),enlarged)
    txt(draw,(x-3,647),name,14,TEXT,True)
panel(draw,(64,715,1536,930)); txt(draw,(91,734),"ACCESSORY SHAPE STUDIES",20,GOLD,True)
txt(draw,(920,742),"Generic silhouettes only • not approved canon item names",12,MUTED)
for index,(name,sprite) in enumerate(accessories.items()):
    x=100+index*175
    enlarged=scale_nearest(sprite,2); image.paste(enlarged,(x,770),enlarged)
    txt(draw,(x-7,880),name.upper(),12,TEXT,True)
image.save(OUT/"weapons-runes-equipment.png")

# Dedicated accessory board with larger icons and a note about the content boundary.
image,draw=board("ACCESSORY SHAPE LIBRARY","8 distinct silhouettes for the two accessory slots • final item identities still need approval")
for index,(name,sprite) in enumerate(accessories.items()):
    col=index%4; row=index//4
    x=74+col*380; y=160+row*370
    panel(draw,(x,y,x+340,y+320))
    draw.rectangle((x+24,y+22,x+316,y+235),fill=(18,14,29),outline=(73,56,97),width=2)
    enlarged=scale_nearest(sprite,5)
    image.paste(enlarged,(x+170-enlarged.width//2,y+35),enlarged)
    txt(draw,(x+24,y+255),name.upper(),20,GOLD,True)
    txt(draw,(x+24,y+286),"ACCESSORY SLOT CANDIDATE",12,MUTED)
txt(draw,(76,945),"These are neutral shape studies, not new Adventure Time canon items. Only approved/source-backed items enter the final catalogue.",12,(209,190,223))
image.save(OUT/"accessory-shape-studies.png")

# Collection cards with the larger sprites and more generous portrait frames.
image,draw=board("CHARACTER COLLECTION CARDS","Collection UI only • high-detail sprite previews • no deck / no draw / no card combat")
for index,(name,sprite) in enumerate(list(characters.items())[:4]):
    x=64+index*375; y=160; panel(draw,(x,y,x+335,y+720))
    draw.rectangle((x+18,y+18,x+317,y+62),fill=(60,40,77),outline=GOLD,width=2)
    txt(draw,(x+32,y+30),"CHARACTER",15,GOLD,True)
    draw.rectangle((x+22,y+82,x+313,y+380),fill=(18,14,29),outline=(87,68,117),width=2)
    enlarged=scale_nearest(sprite,4)
    image.paste(enlarged,(x+167-enlarged.width//2,y+102),enlarged)
    txt(draw,(x+22,y+410),name.upper(),19,TEXT,True)
    txt(draw,(x+22,y+449),"CLASS: TBD",14,MUTED)
    txt(draw,(x+22,y+482),"LEVEL: —   RARITY: TBD",12,MUTED)
    txt(draw,(x+22,y+530),"HP",12,(223,116,139)); draw.rectangle((x+77,y+526,x+290,y+543),fill=(61,47,73)); draw.rectangle((x+79,y+528,x+218,y+541),fill=RED)
    txt(draw,(x+22,y+570),"MANA",12,(127,173,232)); draw.rectangle((x+77,y+566,x+290,y+583),fill=(61,47,73)); draw.rectangle((x+79,y+568,x+173,y+581),fill=BLUE)
    draw.rectangle((x+22,y+625,x+313,y+678),fill=(57,42,82),outline=(126,99,164),width=2)
    txt(draw,(x+77,y+642),"VIEW DETAILS",14,TEXT,True)
image.save(OUT/"character-collection-cards.png")

# Battle + five equipment slots, including two different accessory shape samples.
image,draw=board("BATTLE + EQUIPMENT UI CONCEPT","Discord-ready presentation • team of three • Attack / Skill / Defend / Item")
panel(draw,(64,150,1536,500)); txt(draw,(94,175),"TURN-BASED BATTLE / TEAM OF THREE",22,GOLD,True)
for index,(name,sprite) in enumerate(list(characters.items())[:3]):
    x=100+index*300
    draw.rectangle((x,218,x+250,450),fill=(20,15,32),outline=(80,62,108),width=2)
    enlarged=scale_nearest(sprite,3)
    image.paste(enlarged,(x+125-enlarged.width//2,222),enlarged)
    txt(draw,(x+18,365),name,14,TEXT,True)
    draw.rectangle((x+18,391,x+230,405),fill=(61,47,73)); draw.rectangle((x+20,393,x+155,403),fill=RED)
    txt(draw,(x+18,420),"HP —   MANA —",11,MUTED)
for index,label in enumerate(("ATTACK","SKILL","DEFEND","ITEM")):
    x=1045+(index%2)*205; y=255+(index//2)*76
    draw.rectangle((x,y,x+176,y+52),fill=(64,45,91),outline=GOLD,width=2)
    txt(draw,(x+31,y+17),label,14,TEXT,True)
panel(draw,(64,535,1536,930)); txt(draw,(94,557),"FIVE EQUIPMENT SLOTS",22,GOLD,True)
slots=[("WEAPON",weapons["Grass Sword"]),("ARMOR",None),("RUNE",runes["HP"]),("ACCESSORY 1",accessories["Pendant"]),("ACCESSORY 2",accessories["Medallion"])]
for index,(label,sprite) in enumerate(slots):
    x=90+index*285
    draw.rectangle((x,615,x+245,865),fill=(20,15,32),outline=(86,66,115),width=2)
    if sprite is not None:
        factor=3 if sprite.width>=48 else 4
        enlarged=scale_nearest(sprite,factor)
        image.paste(enlarged,(x+122-enlarged.width//2,625),enlarged)
    else:
        draw.rectangle((x+90,660,x+155,750),fill=(85,71,106),outline=GOLD,width=3)
        draw.rectangle((x+101,672,x+144,740),fill=(116,95,137))
    txt(draw,(x+17,795),label,13,TEXT,True)
    txt(draw,(x+17,823),"ITEM SLOT",11,MUTED)
image.save(OUT/"battle-equipment-ui.png")

# Crypt route concept.
image,draw=board("THE HOLLOW CRYPT","Branching exploration map • persistent run condition • temporary Run Relics")
routes=[((220,390),(470,280)),((220,390),(470,520)),((470,280),(710,390)),((470,520),(710,390)),((710,390),(950,280)),((710,390),(950,520)),((950,280),(1190,390)),((950,520),(1190,390))]
for start,end in routes: draw.line((*start,*end),fill=(122,92,165),width=8)
rooms=[(220,390,"START"),(470,280,"BATTLE"),(470,520,"EVENT"),(710,390,"ELITE"),(950,280,"TREASURE"),(950,520,"MERCHANT"),(1190,390,"BOSS")]
for x,y,label in rooms:
    color=(73,53,101) if label not in ("BOSS","ELITE") else (102,41,65)
    draw.rounded_rectangle((x-88,y-42,x+88,y+42),radius=5,fill=color,outline=GOLD,width=3)
    bounds=draw.textbbox((0,0),label,font=font(15,True))
    draw.text((x-(bounds[2]-bounds[0])//2,y-11),label,font=font(15,True),fill=TEXT)
txt(draw,(80,850),"Map and room schedule are examples only; final generation and reward rules remain open.",14,MUTED)
image.save(OUT/"hollow-crypt-map.png")
