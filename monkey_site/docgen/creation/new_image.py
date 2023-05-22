import os
import random
from datetime import datetime
from django.conf import settings
from PIL import Image, ImageDraw
from .text_formating import recordNumber, docNumber, dateExpiry, patronRand
from .bezier import signatureLine
from .objects import Pic, Text
from .metadata import metadataMaker


def merger(back, front = None):
    if isinstance(front, Pic):
        if back.size[:2] == front.size[:2]:      
            opacityImg = Image.alpha_composite(back.image.convert("RGBA"), front.image.convert("RGBA"))
            back.image.paste(opacityImg, (front.x, front.y))
        else:
            back.image.paste(front.image, (front.x, front.y))
        if front.path == 'new_faces':
            os.remove(front.path)
    elif isinstance(front, Text):
        canvas = ImageDraw.Draw(back.image)
        canvas.text((front.x, front.y), front.text, fill=front.TEXT_COLOR, font=front.font)
    else:
        signatureLine(60, 80, back.image)
        

def docMaking(data):
    smallText = 28
    row1 = 700
    row2 = 1055
    now = datetime.now()
    
    face = Pic('https://thispersondoesnotexist.xyz/', random.randint(197, 205), random.randint(267, 275), [280, 388, random.randint(8, 18)])
    back = Pic('doc_templates', 0, 0, [1500, 1000, random.randint(3, 13)])
    dirt = Pic('dirt', 0, 0, [back.size[0], back.size[1]])

    merger(back, face)
    merger(back, Text(text='Signature', x=227, y=692))
    merger(back) # подпись
    
    merger(back, Text(text='Surname', x=row1, y=276))
    merger(back, Text(size=smallText, text=data['surname'], x=row1, y=315))
    merger(back, Text(text='Name', x=row1, y=377))
    merger(back, Text(size=smallText, text=data['name'], x=row1, y=416))
    merger(back, Text(size=smallText, text=data['patronymic'] if data['patronymic'] else patronRand(data['sex']), x=row1, y=520))
    merger(back, Text(text='Sex', x=row1, y=579))
    merger(back, Text(size=smallText, text=data['sex'].upper(), x=row1, y=618))
    merger(back, Text(text='Date of birth', x=row1, y=683))
    merger(back, Text(size=smallText, text=data['birthday'].replace('-', '.'), x=row1, y=721))
    merger(back, Text(text='Date of expiry', x=row1, y=795))
    merger(back, Text(size=smallText, text=dateExpiry(), x=row1, y=830))
     
    merger(back, Text(text='Country', x=row2, y=585))
    merger(back, Text(size=smallText, text=data['inputState'], x=row2, y=620))
    merger(back, Text(text='Record No.', x=row2, y=684))
    merger(back, Text(size=smallText, text=recordNumber(2, 5), x=row2, y=728))
    merger(back, Text(text='Document No.', x=row2, y=795))
    merger(back, Text(size=smallText, text=docNumber(8), x=row2, y=832))
    merger(back, dirt)
    
    imageName = f'photo_{now.strftime("%Y_%m_%d_%H_%M_%S")}.jpeg'
    imagePath = os.path.join(settings.MEDIA_ROOT, 'docs/completed', imageName)
    back.image.save(imagePath, quality=70)
    
    # скаченный фейс уже не нужен
    if 'new_faces' in face.path:
        os.remove(face.path)
   
    if data['metadata']:
        metadataMaker(imagePath, data['inputState'], data['name'], data['surname'], back.size[0], back.size[1])
        
    return imagePath