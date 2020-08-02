# YUKTI
'YUKTI' is program, intended for those who are inexperienced in and new to the interrelated fields of Computational Biology and Bioinformatics, which helps its user perform an assisted experiment involving Molecular Docking Simulation in a simple manner. The pseudonymous creator of this program, AhiYantra (@ahiyantra), hopes that it'll allow its users to gain a better understanding of the two fields through firsthand experience and he'll keep improving this program indefinitely until he decides that it no longer requires any additional improvements, which means that the preparations required for using it will keep decreasing. The name used for this program is a word with several meanings but the creator's preferred meaning is "device"/"gadget". Before the current version of this program was created, it originally existed as a bunch of interdependent scripts written using Python to help decrease the amount of manual work its creator had to do alone as a part of his internship research project during the eighth & final semester of his four years long education as a student pursuing Bachelor in Technology for Biotechnology (2016 CE - 2020 CE). Please don't forget to cite the creator if you use this program in any projects. Your citation will help acknowledge & recognize all the dedication, time and energy which went into creating this open-source program. Both acknowledgement & recognition are important sources of motivation for those who create open-source programs. Make sure to read the "notes" section, written by the creator in first-person perspective, for several major & minor details regarding the program.

Notes:

1) 'YUKTI' works together with "AutoDock"/"AutoGrid", which needs to be installed beforehand. Also use "AutoDock Tools" to convert all your PDB files into PDBQT files. Although you don't need to alter "sunya.py" in any manner, you may need to take a look at "yukti.py" and replace the values of variables/numbers/addresses as per necessary to ensure that they fit the preferences/requirements of your experiment and those of the OS you've installed on your PC, such as Windows, Macintosh & Linux.

2) Although both "AutoDock"/"AutoGrid" (older software) and "AutoDock Vina" (newer software) were created by Scripps Research Institute, the latter is supposed to be better than the former. "AutoDock Tools" was also created by Scripps Research Institute. I was forced to use "AutoDock"/"AutoGrid" due to circumstantial reasons (following strict direct instructions from my superiors) but i was originally planning to use "AutoDock Vina" instead.

3) 'YUKTI' works though four scripts written using Python. The scripts "yukti.py" and "sunya.py" are both written in the 3rd version of Python but rely on "prepare_gpf4.py" and "prepare_dpf4.py" which are both written in the 2nd version of Python. All scripts except "yukti.py" run automatically as a part of the experiment and hence won't need to be executed separately.

4) The scripts "prepare_gpf4.py" and "prepare_dpf4.py" are pre-included in the "AutoDock Tools" installation and were prepared by Scripps Research Institute. As of now, their versions which i provide alongside 'YUKTI' ("yukti.py" and "sunya.py") may be specific to the OS i was using while performing the experiments & preparing the scripts, which is Linux.

5) In file & system addresses, Windows uses "\\" while both Linux and Macintosh use "/". Using the wrong symbol will make the scripts useless by causing errors. While preparing the current versions of my Python scripts, I was using 2 proteins as targets with 10 compounds as ligands. Your number of chosen targets and ligands may be different.
