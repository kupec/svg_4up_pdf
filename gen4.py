import math
import sys
import os
from pathlib import Path

scale = float(os.environ.get('SCALE', 1))
rows = int(os.environ.get('ROWS', 2))
columns = int(os.environ.get('COLUMNS', 2))
media_width = float(os.environ.get('MEDIA_WIDTH', 210))
media_height = float(os.environ.get('MEDIA_HEIGHT', 297))
opacity = float(os.environ.get('OPACITY', 0.25))
rotate = bool(os.environ.get('ROTATE', False))

def px(size_in_mm):
    return size_in_mm / 25.4 * 96

W = px(media_width)
H = px(media_height)
cx = W/2
cy = H/2

files = sys.argv[1:]

print(f'<svg width="{media_width}mm" height="{media_height}mm">')

def read_svg(file):
   return ''.join(Path(file).read_text().splitlines()[1:])

for r in range(rows):
    for c in range(columns):
        svg = read_svg(files.pop(0))
        dx = c * W / columns
        dy = r * H / rows
        radius = min(W / columns, H / rows) / 2
        rot = '90' if rotate else 0
        print(f'<g opacity="{opacity}" transform="translate({dx} {dy}) rotate({rot} {radius} {radius}) scale({scale}) ">{svg}</g>')

stroke = 'rgb(190, 190, 190)'
stroke_width = "0.25pt"
dasharray = '1 2'

for r in range(1, rows):
    dy = r * H / rows
    print(f'<line x1="{0}" y1="{dy}" x2="{W}" y2="{dy}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-dasharray="{dasharray}"/>')
for c in range(1, columns):
    dx = c * W / columns
    print(f'<line x1="{dx}" y1="{0}" x2="{dx}" y2="{H}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-dasharray="{dasharray}"/>')

print(f'</svg>')
