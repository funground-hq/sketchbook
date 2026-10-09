"""A picture from the data folder

Put your own picture (PNG or JPEG) in the data folder and change the name below.
"""
import funground as f

photo = f.load_image("data/photo.png")       # found in the data folder next to this file


def setup():
    f.size(640, 400)


def draw():
    f.background("ivory")
    f.image(photo, 120, 50)


f.run()
