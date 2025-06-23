#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: No filepath provided."
  echo "Usage: $0 <path to project>/<filename without -[F|B]_[Cu|Mask|Paste].svg>"
  exit 1
fi

echo "The provided filepath is: $1"

python3 create_powershell.py "$1"

if [ -e "$1-F_Cu.svg" ]; then
  python3 circuit_prep.py "$1-F_Cu.svg" --invert
fi

if [ -e "$1-B_Cu.svg" ]; then
  python3 circuit_prep.py "$1-B_Cu.svg" --invert --mirror
fi

if [ -e "$1-F_Mask.svg" ]; then
  python3 circuit_prep.py "$1-F_Mask.svg"
fi

if [ -e "$1-B_Mask.svg" ]; then
  python3 circuit_prep.py "$1-B_Mask.svg" --mirror
fi

if [ -e "$1-F_Paste.svg" ]; then
  python3 circuit_prep.py "$1-F_Paste.svg"
fi

if [ -e "$1-B_Paste.svg" ]; then
  python3 circuit_prep.py "$1-B_Paste.svg" --mirror
fi
