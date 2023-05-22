import random
import string
import pyexiv2
from datetime import datetime


def coordsGPS(country):
    if country == 'UA':
        return f'N: {round(random.uniform(50.663847, 48.620472), 6)}, E: {round(random.uniform(25.005734, 30.731940), 6)}'
    elif country == 'KZ':
        return (round(random.uniform(51.766265, 48.781882), 6), round(random.uniform(69.677228, 77.155819), 6))
    elif country == 'USA':
        return (round(random.uniform(44.652342, 34.716657), 6), round(random.uniform(-119.115197, -87.007688), 6))
    else:
        return (round(random.uniform(51.683947, 45.780337), 6), round(random.uniform(5.626380, 21.270911), 6))

def metadataMaker(imagePath, country, name, surname, width, height):
    now = datetime.now()
    image = pyexiv2.Image(imagePath)
    exif_data = image.read_exif()

    exif_data['Exif.Image.DateTimeOriginal'] = now.strftime("%Y:%m:%d %H:%M:%S")
    exif_data['Exif.Image.Model'] = "My Camera"
    exif_data['Exif.Image.DateTimeOriginal'] = now.strftime("%Y:%m:%d %H:%M:%S")
    exif_data['Exif.Image.FocalLength'] = f'{random.choice((12, 17, 24, 35, 50))}'
    exif_data['Exif.Image.ExposureTime'] = f'{random.choice((20, 100, 70, 420, 300, 60))}'
    exif_data['Exif.Image.ISOSpeedRatings'] = str(random.choice((200, 400, 100)))
    exif_data['Exif.Image.ExposureBiasValue'] = str(random.choice((0, 1)))
    exif_data['Exif.Image.Flash'] = 0
    exif_data['Exif.Image.Artist'] = f'{name} {surname}'
    exif_data['Exif.Image.ImageDescription'] = f'photo_{now.strftime("%Y-%m-%d-%H-%M-%S")}'
    # exif_data['Exif.Image.GPSInfo'] = coordsGPS(country)
    # exif_data['Exif.Image.ExifVersion'] = b"0220"
    exif_data['Exif.Image.MeteringMode'] = random.choice((1,2))
    exif_data['Exif.Image.ImageWidth'] = width
    exif_data['Exif.Image.Orientation'] = 1
    exif_data['Exif.Image.Make'] = "My Camera"
    exif_data['Exif.Image.ExposureProgram'] = random.choice((1, 3))
    exif_data['Exif.Image.MaxApertureValue'] = random.choice((2, 3, 5))
    exif_data['Exif.Image.FocalPlaneXResolution'] = random.choice((2660, 3504000, 2048000))
    exif_data['Exif.Image.FocalPlaneYResolution'] = random.choice((2660, 3072000, 2048000))
    exif_data['Exif.Image.ImageHistory'] = f"Processed by {''.join(random.choices(string.ascii_lowercase, k=4) + random.choices(string.digits, k=4))}"
    exif_data['Exif.Image.BrightnessValue'] = random.choice((0, 2))
    
    image.modify_exif(exif_data)
    image.close()