"""A pattern in my colours

The colours come from palette.py, next to this file. Change them there and run this again.
"""
import funground as f
import palette


def setup():
    f.size(640, 400)


def draw():
    f.background(palette.BACKGROUND)
    f.no_stroke()
    for row in range(5):
        for column in range(8):
            f.fill(palette.COLOURS[(row + column) % len(palette.COLOURS)])
            f.circle(40 + column * 80, 40 + row * 80, 30)


f.run()
