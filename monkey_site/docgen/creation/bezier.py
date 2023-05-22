import numpy as np
from PIL import ImageDraw
from .objects import Point
import random


def PointMaker(area):
    x = random.randint(area['x'][0], area['x'][1])
    y = random.randint(area['y'][0], area['y'][1])
    return Point(x, y)


def signatureLine(smallArea: int, bigArea: int, image):
    points = []
    for _ in range(smallArea):
        area = {'x': [210, 286], 'y': [700, 770]}
        points.append(PointMaker(area))
    for _ in range(bigArea):
        area = {'x': [210, 522], 'y': [700, 928]}
        points.append(PointMaker(area))
    
    pointsBezier = []
    for i in points:
        pointsBezier.append([i.x, i.y])
    
    draw = ImageDraw.Draw(image)
    
    points = np.array(pointsBezier)
    pointsCount = 100
    curve = bezierCurve(points, pointsCount)
    
    # каждый раз строим линию по двум точкам: текущая и ближайшая 
    for i in range(pointsCount - 1):
        draw.line((curve[i][0], curve[i][1], curve[i+1][0], curve[i+1][1]), fill=(124, 40, 240), width=3)



# Curve
def binomialCoefficient(n, k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))


def bezierCurve(points, count):
    t = np.linspace(0, 1, count)
    n = len(points) - 1
    curve = np.zeros((count, 2))

    for i in range(count):
        for j in range(n + 1):
            curve[i] += points[j] * \
                binomialCoefficient(n, j) * (1 - t[i])**(n - j) * t[i]**j

    return curve
