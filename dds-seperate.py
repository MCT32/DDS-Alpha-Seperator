import argparse
import pathlib
from PIL import Image

parser = argparse.ArgumentParser(
    prog = 'dds-seperate',
    description = 'Seperates the alpha channel of a DDS texture.'
)

parser.add_argument('filename', type=pathlib.Path)
parser.add_argument('color', type=pathlib.Path)
parser.add_argument('alpha', type=pathlib.Path)

args = parser.parse_args()

with Image.open(args.filename) as im:
    alpha = im.getchannel('A')
    im.putalpha(255)

    im.save(args.color)
    alpha.save(args.alpha)
