import sys
import os
import shutil

# Check for file name. sys.argv will contain the python file called at index 0.
if len(sys.argv) <= 1:
  print("Missing filename.")
  exit()
else:
  print("File name provided. Processing...")

filename = os.path.splitext(sys.argv[1])[0]
svg_original = "{}-original.svg".format(filename)
png_normal = "{}-normal.png".format(filename)
png_inverted = "{}-inverted.png".format(filename)
pnm_intermediate = "{}-intermediate.pnm".format(filename)
#svg_inverted = "{}-inverted.svg".format(filename)
svg_new = "{}-new.svg".format(filename)

shutil.copy("{}.svg".format(filename), svg_original)

import xml.etree.ElementTree as ET
tree = ET.parse(svg_original)
root = tree.getroot()
width = root.attrib['width']
height = root.attrib['height']

os.system("cairosvg {} -d 2400 -b white -o {}".format(svg_original, png_normal))

os.system("convert {} -channel rgb -negate {}".format(png_normal, png_inverted))

os.system("rm {}".format(png_normal))

os.system("convert {} {}".format(png_inverted, pnm_intermediate))
#os.system("convert {} {}".format(png_normal, pnm_intermediate))

os.system("rm {}".format(png_inverted))

#os.system("potrace {} -W {} -H {} -s -o {}".format(pnm_intermediate, width, height, svg_inverted))
os.system("potrace {} -W {} -H {} -s -o {}".format(pnm_intermediate, width, height, svg_new))

os.system("rm {}".format(pnm_intermediate))
