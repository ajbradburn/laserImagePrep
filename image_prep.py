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
pnm_intermediate = "{}-intermediate.pnm".format(filename)
svg_new = "{}-new.svg".format(filename)

os.system("convert {}.png {}".format(filename, pnm_intermediate))

os.system("potrace {} -s -o {}".format(pnm_intermediate, svg_new))

os.system("rm {}".format(pnm_intermediate))
