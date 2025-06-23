import argparse
import sys
import os
import shutil

def os_escape(path):
  return "\"{}\"".format(path)

# Create the parser.
parser = argparse.ArgumentParser(description="Process an SVG file for use in LightBurn. Invert it if indicated.")

# Add the arguments.
parser.add_argument("path", type=str, help="The path to the KiCad project files.")
parser.add_argument("--invert", action="store_true", help="Do you want to invert the colors (black and white) of the svg?")
parser.add_argument("--mirror", action="store_true", help="Do you want to flip this image horizontally? (Normally useful for the back layers of a PCB.)")

# Parse the arguments.
args = parser.parse_args()

# Access the arguments.
path = args.path
invert = args.invert
mirror = args.mirror

# Prepare the filenames that will be used in the process.
filepath = os.path.split(path)[0]
filename = os.path.splitext(os.path.split(path)[1])[0]
svg_original = "{}/{}-original.svg".format(filepath, filename)
png_normal = "{}/{}-normal.png".format(filepath, filename)
pnm_intermediate = "{}/{}-intermediate.pnm".format(filepath, filename)
svg_new = "{}/{}-new.svg".format(filepath, filename)
if invert:
  png_inverted = "{}/{}-inverted.png".format(filepath, filename)
  svg_inverted = "{}/{}-inverted.svg".format(filepath, filename)

# Process the files.
print("Processing file {}.".format(path))
print("Invert option for file is: {}".format(invert))
print("Mirror option for file is: {}".format(mirror))

shutil.copy("{}/{}.svg".format(filepath, filename), svg_original)

import xml.etree.ElementTree as ET
tree = ET.parse(svg_original)
root = tree.getroot()
width = root.attrib['width']
height = root.attrib['height']

os.system("cairosvg {} -d 2400 -b white -o {}".format(os_escape(svg_original), os_escape(png_normal)))

if invert:
  os.system("convert {} -channel rgb -negate {}".format(os_escape(png_normal), os_escape(png_inverted)))
  os.system("rm {}".format(os_escape(png_normal)))
  if mirror:
    os.system("convert {} -flop {}".format(os_escape(png_inverted), os_escape(pnm_intermediate)))
  else:
    os.system("convert {} {}".format(os_escape(png_inverted), os_escape(pnm_intermediate)))
  os.system("rm {}".format(os_escape(png_inverted)))
else:
  if mirror:
    os.system("convert {} -flop {}".format(os_escape(png_normal), os_escape(pnm_intermediate)))
  else:
    os.system("convert {} {}".format(os_escape(png_normal), os_escape(pnm_intermediate)))
  os.system("rm {}".format(os_escape(png_normal)))

os.system("potrace {} -W {} -H {} -s -o {}".format(os_escape(pnm_intermediate), width, height, os_escape(svg_new)))

os.system("rm {}".format(os_escape(pnm_intermediate)))
