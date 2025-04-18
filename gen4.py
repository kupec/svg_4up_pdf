import sys
from pathlib import Path


scale = 1
media_width = 210
media_height = 297

def px(size_in_mm):
    return size_in_mm / 25.4 * 96

W = px(media_width)
H = px(media_height)
cx = W/2
cy = H/2

opacity = 0.25

files = sys.argv[1:]
if len(files) != 4:
    print('Specify 4 files')
    sys.exit(1)

print(f'<svg width="{media_width}mm" height="{media_height}mm">')

def read_svg(file):
   return ''.join(Path(file).read_text().splitlines()[1:])

svg1 = read_svg(files[0])
print(f'<g opacity="{opacity}" transform="scale({scale})">{svg1}</g>')

svg2 = read_svg(files[1])
print(f'<g opacity="{opacity}" transform="translate({cx} 0) scale({scale})">{svg2}</g>')

svg3 = read_svg(files[2])
print(f'<g opacity="{opacity}" transform="translate(0 {cy}) scale({scale})">{svg3}</g>')

svg4 = read_svg(files[3])
print(f'<g opacity="{opacity}" transform="translate({cx} {cy}) scale({scale})">{svg4}</g>')

stroke = 'rgb(190, 190, 190)'
stroke_width = "0.25pt"
dasharray = '1 2'
print(f'<line x1="{cx}" y1="{0}" x2="{cx}" y2="{H}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-dasharray="{dasharray}"/>')
print(f'<line x1="{0}" y1="{cy}" x2="{W}" y2="{cy}" stroke="{stroke}" stroke-width="{stroke_width}" stroke-dasharray="{dasharray}"/>')

print(f'</svg>')
