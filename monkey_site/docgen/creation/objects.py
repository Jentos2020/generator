import os
import random
from django.conf import settings
from .face_download import faceDownload, randImgSelect
from PIL import Image, ImageFont

class Point():
    __slots__ = ('x', 'y')

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'x:{self.x}\ny:{self.y}'


class Pic(Point):
    def __init__(self, path: str, x: int = 0, y: int = 0, size: list = [0, 0, 0]):
        super().__init__(x, y)
        self.path = faceDownload(path) if 'http' in path else randImgSelect(path)
        self.size = Pic.randSize(size)
        self.image = Pic.makeImg(self)

    def randSize(size: list):
        if len(size) > 2:
            size[2] /= 1000
            size[0] -= round(size[0] * size[2])
            size[1] -= round(size[1] * size[2])
        return size
    
    def makeImg(self):
        imgEdit = Image.open(self.path)
        newImg = imgEdit.resize((self.size[0],self.size[1]), Image.BILINEAR)
        return newImg

    def __repr__(self):
        return f'path:\t{self.path}\nx:\t{self.x}\ny:\t{self.y}\nwidth:\t{self.size[0]}\nheight:\t{self.size[1]}'



class Text(Point):
    FONT_PATH = os.path.join(settings.MEDIA_ROOT, 'docs/fonts/bookos.ttf')
    TEXT_COLOR = (52, 54, 78)
    
    def __init__(self, size: int = 32, text: str = '', x: int = 0, y: int = 0):
        super().__init__(x, y)
        self.x += random.randint(-2, 2)
        self.y += random.randint(-2, 2)
        self.text = text
        self.font = ImageFont.truetype(self.FONT_PATH, size)