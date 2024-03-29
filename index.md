# "YUKTI" (yukti.py)

## introduction:

"YUKTI" (yukti.py) is a program, intended for the students of computational biology & bioinformatics, which allows its users to perform an assisted experiment involving molecular docking simulation techniques.

The previously pseudonymous creator of this program, 'AHIYANTRA' (@ahiyantra), hopes that it'll allow its users to gain a better understanding of the two fields through firsthand experience and he'll keep improving this program indefinitely until he decides that it no longer requires any additional improvements, which means that the preparations required for using it will keep decreasing. The name used for this program is a word with several meanings but the creator's preferred meaning is "device". Before the current version of this program was created, it originally existed as a bunch of interdependent scripts written using Python to help decrease the amount of manual work its creator had to do alone as a part of his internship research project during the eighth & final semester of his four years long education as a student pursuing a Bachelor of Technology for Biotechnology (06/2016 CE - 12/2020 CE).

Please don't forget to cite the creator if you use this program in any projects because your citation will help acknowledge/recognize all the dedication, time and energy which went into creating this open-source program. Both acknowledgement & recognition are important sources of motivation for those who create open-source programs. Make sure to read the "notes" section, for several major & minor details regarding the program.

### notes:

1) "YUKTI" works together with "AutoDock"/"AutoGrid", which needs to be installed beforehand. You must use "AutoDock Tools" to convert all your PDB files into PDBQT files. You may need to take a look at the program and replace the values of variables/numbers/addresses as per necessary to ensure that they fit the preferences/requirements of your experiment and those of the OS you've installed on your PC, such as Linux.

2) Although both "AutoDock"/"AutoGrid" (older software) and "AutoDock Vina" (newer software) were created by Scripps Research Institute, the latter is supposed to be better than the former. "AutoDock Tools" was also created by Scripps Research Institute. The creator of this program was forced to use "AutoDock"/"AutoGrid" due to circumstantial reasons (following strict direct instructions from his superiors) but he was originally planning to use "AutoDock Vina" instead.

3) "YUKTI" works though three scripts written using Python. The program is written in the 3rd version of Python but relies on "prepare_gpf4.py" and "prepare_dpf4.py" which are both written in the 2nd version of Python. All scripts except the program run automatically as a part of the experiment and hence won't need to be executed separately.

4) The scripts "prepare_gpf4.py" and "prepare_dpf4.py" are pre-included in the "AutoDock Tools" installation and were prepared by Scripps Research Institute. As of now, their versions which the creator of this program provides alongside 'YUKTI' ("yukti.py") are empty placeholder files & must be replaced by the actual scripts in order for the experiment to run. They may and may not be specific to the OS which is used while running the experiment, such as Linux.

5) In file & system addresses, Windows uses "\\" while both Linux and Macintosh use "/". Using the wrong symbol will make the scripts useless by causing errors. While preparing & testing the current version, the creator of this program was using 2 proteins as targets with 10 compounds as ligands. Your number of chosen targets and ligands may and may not be different.

> [return to the main page](https://ahiyantra.github.io)
> |
> [visit this project on github](https://github.com/ahiyantra/YUKTI)