import argparse
import sys
import os
import shutil

# Create the parser.
parser = argparse.ArgumentParser(description="Process an SVG file for use in LightBurn. Invert it if indicated.")

# Add the arguments.
parser.add_argument("filename", type=str, help="The name of the file to be processed.")
parser.add_argument("--invert", action="store_true", help="Do you want to invert the colors (black and white) of the svg?")

# Parse the arguments.
args = parser.parse_args()

# Access the arguments.
filename = args.filename
invert = args.invert

print("Processing file {}.".format(filename))
print("Invert option for file is: {}".format(invert))

# Prepare the filenames that will be used in the process.
filename = os.path.splitext(sys.argv[1])[0]
svg_original = "{}-original.svg".format(filename)
png_normal = "{}-normal.png".format(filename)
pnm_intermediate = "{}-intermediate.pnm".format(filename)
svg_new = "{}-new.svg".format(filename)
if invert:
  png_inverted = "{}-inverted.png".format(filename)
  svg_inverted = "{}-inverted.svg".format(filename)

shutil.copy("{}.svg".format(filename), svg_original)

import xml.etree.ElementTree as ET
tree = ET.parse(svg_original)
root = tree.getroot()
width = root.attrib['width']
height = root.attrib['height']

os.system("cairosvg {} -d 2400 -b white -o {}".format(svg_original, png_normal))

if invert:
  os.system("convert {} -channel rgb -negate {}".format(png_normal, png_inverted))
  os.system("rm {}".format(png_normal))
  os.system("convert {} {}".format(png_inverted, pnm_intermediate))
  os.system("rm {}".format(png_inverted))
else:
  os.system("convert {} {}".format(png_normal, pnm_intermediate))
  os.system("rm {}".format(png_normal))

#os.system("potrace {} -W {} -H {} -s -o {}".format(pnm_intermediate, width, height, svg_inverted))
os.system("potrace {} -W {} -H {} -s -o {}".format(pnm_intermediate, width, height, svg_new))

os.system("rm {}".format(pnm_intermediate))
