#!/bin/bash
echo $1
python3 circuit_prep.py $1-F_Cu.svg --invert
python3 circuit_prep.py $1-B_Cu.svg --invert
python3 circuit_prep.py $1-F_Mask.svg
python3 circuit_prep.py $1-B_Mask.svg
python3 circuit_prep.py $1-F_Paste.svg
python3 circuit_prep.py $1-B_Paste.svg
#python3 solder_resist_prep.py $1-F_Mask.svg
#python3 solder_resist_prep.py $1-B_Mask.svg
#python3 solder_resist_prep.py $1-F_Paste.svg
#python3 solder_resist_prep.py $1-B_Paste.svg
