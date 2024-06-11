import argparse
import sys
import os
import shutil

def os_escape(path):
  return "\"{}\"".format(path)

remote_path = "Z:\\Electronics"

# Create the parser.
parser = argparse.ArgumentParser(description="Process an SVG file for use in LightBurn. Invert it if indicated.")

# Add the arguments.
parser.add_argument("path", type=str, help="The path to the KiCad project files.")

# Parse the arguments.
args = parser.parse_args()

# Access the arguments.
path = args.path

# Prepare the filenames that will be used in the process.
filepath = os.path.split(path)[0]
project_directory = os.path.split(path)[1]
full_remote_path = "{}\\{}".format(remote_path, project_directory)

# Open the powershell.
# Write to PowerShell script:
# print("$newDirectory = New-Item -Path {} -ItemType Directory -Force".format(full_remote_path))
# print("Get-ChildItem -Path .\ -Filter "*-new.svg" | Copy-Item -Destination {}".format(full_remote_path))
print("{}/copy_files.ps1".format(filepath));
with open("{}/copy_files.ps1".format(filepath), 'w') as file:
  file.write("$newDirectory = New-Item -Path \"{}\" -ItemType Directory -Force\r\n".format(full_remote_path))
  file.write("Get-ChildItem -Path .\\ -Filter \"*-new.svg\" | Copy-Item -Destination \"{}\"".format(full_remote_path))
