from PIL import Image, ImageDraw, ImageFont, ImageOps 
import textwrap
import os, sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


img = Image.open(resource_path("images/template_1.png"))

d = ImageDraw.Draw(img)

fnt = ImageFont.truetype(resource_path("fonts/trebuc.ttf"), 20)
#fnt = ImageFont.truetype("ariblk.ttf", 25)
fntWorkTitle = ImageFont.truetype(resource_path("fonts/trebuc.ttf"), 15)

username = input("Enter you username Here ")
jobTitle = input("Enter your job title ")
direction = input("Enter your job direction ")
contact = input("Enter your contact ")
 
y = 60
d.text((260,y), username, font= fnt, fill= (47,132,88))
y+=30
lines = textwrap.wrap(jobTitle, width=50)

for x in lines:
    d.text((262,y), x, font= fnt, fill= (241,147,59))
    y+=20
 #d.text((262,90), jobTitle, font= fnt, fill= (4,126,79))

y+=5
d.text((262,y), ""+direction, font= fntWorkTitle, fill= (0,0,0))

y+=20
d.text((262,y), "Cocody 2 Plateaux, Boulvard Latrille Immeuble K-Garden", font= fntWorkTitle, fill= (0,0,0))

y+=20
d.text((262,y), "(+225) "+contact, font= fntWorkTitle, fill= (0,0,0))

img.save(resource_path("edited.png"))
# Chef de Département Redevance, Purge et Indemnisation Chargé du Recouvrement et du Marketing.
# 07 07 92 77 44

