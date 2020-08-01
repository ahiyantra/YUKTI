# This version of "editor.py"/"0.py" customizes itself when used for automated experiments.

import os;

retrieved_address = __file__
retrieved_address = retrieved_address.replace("sunya.py", "")
file_path = retrieved_address+"compound_target.dpf"

fin = open(file_path, "rt")
data = fin.read()
data = data.replace('extended', 'bound')
fin.close()

fin = open(file_path, "wt")
fin.write(data)
fin.close()
