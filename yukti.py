import os;
from shutil import copyfile;
from shutil import rmtree;

print("\n'YUKTI' (\"yukti.py\" and \"sunya.py\") is running now. Always make sure that you've properly converted all of your targets/proteins and ligands/compounds to the PDBQT file format before using this program in order to avoid any errors.\n\nNote: If you run 'YUKTI' more than once in the same folder/directory for any reason, then make sure to remove everything created during its previous run before you run it again because otherwise it'll all get deleted and also make sure to take a proper look at the \"read me\" file (this program's flexibility will keep improving until its development is complete and the preparations required for using it will keep decreasing).\n");

judge1 = os.path.exists("/home/number5/YUKTI/target_1");

if judge1 == True:
    rmtree("/home/number5/YUKTI/target_1");

os.mkdir("/home/number5/YUKTI/target_1");

folders1 = ["{}".format(x) for x in range(11)];
del folders1[0];

for f_variable in folders1:
    os.mkdir(os.path.join("/home/number5/YUKTI/target_1", f_variable));

src_path = "/home/number5/YUKTI/";
#fileA = "autodock4.exe";
#fileB = "autogrid4.exe";
fileC = "target_1.pdb";
fileD = "target_1.pdbqt";

for f_variable in folders1:
    dst_path = "/home/number5/YUKTI/target_1/"+str(f_variable)+"/";
    #copyfile(src_path+str(fileA), dst_path+str(fileA));
    #copyfile(src_path+str(fileB), dst_path+str(fileB));
    copyfile(src_path+str(fileC), dst_path+str(fileC));
    copyfile(src_path+str(fileD), dst_path+str(fileD));

judge2 = os.path.exists("/home/number5/YUKTI/target_2");

if judge2 == True:
    rmtree("/home/number5/YUKTI/target_2");

os.mkdir("/home/number5/YUKTI/target_2");

folders2 = ["{}".format(x) for x in range(11)];
del folders2[0];

for f_variable in folders2:
    os.mkdir(os.path.join("/home/number5/YUKTI/target_2", f_variable));

src_path = "/home/number5/YUKTI/";
#fileA = "autodock4.exe";
#fileB = "autogrid4.exe";
fileC = "target_2.pdb";
fileD = "target_2.pdbqt";

for f_variable in folders2:
    dst_path = "/home/number5/YUKTI/target_2/"+str(f_variable)+"/";
    #copyfile(src_path+str(fileA), dst_path+str(fileA));
    #copyfile(src_path+str(fileB), dst_path+str(fileB));
    copyfile(src_path+str(fileC), dst_path+str(fileC));
    copyfile(src_path+str(fileD), dst_path+str(fileD));

folders = ["{}".format(x) for x in range(11)];
del folders[0];

src_path1 = "/home/number5/YUKTI/Library-pdbqt/";

for f_variable in folders:
    dst_path1 = "/home/number5/YUKTI/target_1/"+str(f_variable)+"/";
    dst_path2 = "/home/number5/YUKTI/target_2/"+str(f_variable)+"/";
    copyfile(src_path1+"compound_"+str(f_variable)+".pdbqt", dst_path1+"compound_"+str(f_variable)+".pdbqt");
    copyfile(src_path1+"compound_"+str(f_variable)+".pdbqt", dst_path2+"compound_"+str(f_variable)+".pdbqt");
    
    copyfile("/home/number5/YUKTI/Library-pdb/compound_"+str(f_variable)+".pdb", dst_path1+"compound_"+str(f_variable)+".pdb");
    copyfile("/home/number5/YUKTI/Library-pdb/compound_"+str(f_variable)+".pdb", dst_path2+"compound_"+str(f_variable)+".pdb");

src_path2 = "/home/number5/YUKTI/";

for f_variable in folders:
    dst_path1 = "/home/number5/YUKTI/target_1/"+str(f_variable)+"/";
    dst_path2 = "/home/number5/YUKTI/target_2/"+str(f_variable)+"/";
    copyfile(src_path2+"prepare_gpf4.py", dst_path1+"prepare_gpf4.py");
    copyfile(src_path2+"prepare_gpf4.py", dst_path2+"prepare_gpf4.py");
    copyfile(src_path2+"prepare_dpf4.py", dst_path1+"prepare_dpf4.py");
    copyfile(src_path2+"prepare_dpf4.py", dst_path2+"prepare_dpf4.py");
    copyfile(src_path2+"sunya.py", dst_path1+"sunya.py");
    copyfile(src_path2+"sunya.py", dst_path2+"sunya.py");

index = list(range(0, 10));

location1 = "/home/number5/YUKTI/target_1";

folders1 = ["{}".format(x) for x in range(11)];
del folders1[0];

for i_variable1 in index:
    folders1[i_variable1] = os.path.join(location1, folders1[i_variable1]);

location2 = "/home/number5/YUKTI/target_2";

folders2 = ["{}".format(x) for x in range(11)];
del folders2[0];

for i_variable2 in index:
    folders2[i_variable2] = os.path.join(location2, folders2[i_variable2]);

numbers = list(range(0, 11));
del numbers[0];

autopython = "/home/number5/mgltools_x86_64Linux2_1.5.6/bin/pythonsh"; # location of 'pythonsh' 

for i_variable in index:
    
    holderA = autopython+" "+folders1[i_variable]+"/prepare_gpf4.py -l "+folders1[i_variable]+"/compound_"+str(numbers[i_variable])+".pdbqt -r "+folders1[i_variable]+"/target_1.pdbqt -p npts=\'60,60,60\' -p gridcenter=\'11.112,-7.196,1.36\' -o \'"+folders1[i_variable]+"/target.gpf\'";
    os.system(holderA);
    holderB = autopython+" "+folders1[i_variable]+"/prepare_dpf4.py -l "+folders1[i_variable]+"/compound_"+str(numbers[i_variable])+".pdbqt -r "+folders1[i_variable]+"/target_1.pdbqt -o \'"+folders1[i_variable]+"/compound_target.dpf\'";
    os.system(holderB);
    #holderC = "python3 "+folders1[i_variable]+"/sunya.py";
    #os.system(holderC);
    
    # insert replacement code to get rid of 'sunya.py'
    
    tempaddr = folders1[i_variable] + "/";
    #retrieved_address = __file__;
    #retrieved_address = retrieved_address.replace("sunya.py", "");
    retrieved_address = tempaddr;
    file_path = retrieved_address+"compound_target.dpf";

    fin = open(file_path, "rt");
    data = fin.read();
    data = data.replace('extended', 'bound');
    fin.close();

    fin = open(file_path, "wt");
    fin.write(data);
    fin.close();
    
    os.chdir(folders1[i_variable]);
    
    holderD = "autogrid4 -p "+folders1[i_variable]+"/target.gpf -l "+folders1[i_variable]+"/protein.glg";
    os.system(holderD);
    holderE = "autodock4 -p "+folders1[i_variable]+"/compound_target.dpf -l "+folders1[i_variable]+"/protein.dlg";
    os.system(holderE);
    
    with open('protein.dlg', 'r') as  f:
        content = f.read();
        holder1 = content.index("\n\nMODEL       ");
        holder2 = content.index("TER\nENDMDL\n");
        holder3 = content[holder1+1:holder2+11];
        
        output = open("bestmodel.pdb", "w");
        output.write(holder3);
        output.close();
        
        print("\nTarget 1's Compound "+str(i_variable+1)+" is done!\n");
        
    holderA = autopython+" "+folders2[i_variable]+"/prepare_gpf4.py -l "+folders2[i_variable]+"/compound_"+str(numbers[i_variable])+".pdbqt -r "+folders2[i_variable]+"/target_2.pdbqt -p npts=\'82,42,126\' -o \'"+folders2[i_variable]+"/target.gpf\'";
    os.system(holderA);
    holderB = autopython+" "+folders2[i_variable]+"/prepare_dpf4.py -l "+folders2[i_variable]+"/compound_"+str(numbers[i_variable])+".pdbqt -r "+folders2[i_variable]+"/target_2.pdbqt -o \'"+folders2[i_variable]+"/compound_target.dpf\'";
    os.system(holderB);
    #holderC = "python3 "+folders2[i_variable]+"/sunya.py";
    #os.system(holderC);
    
    # insert replacement code to get rid of 'sunya.py'
    
    tempaddr = folders2[i_variable] + "/";
    #retrieved_address = __file__;
    #retrieved_address = retrieved_address.replace("sunya.py", "");
    retrieved_address = tempaddr;
    file_path = retrieved_address+"compound_target.dpf";

    fin = open(file_path, "rt");
    data = fin.read();
    data = data.replace('extended', 'bound');
    fin.close();

    fin = open(file_path, "wt");
    fin.write(data);
    fin.close();
    
    os.chdir(folders2[i_variable]);
    
    holderD = "autogrid4 -p "+folders2[i_variable]+"/target.gpf -l "+folders2[i_variable]+"/protein.glg";
    os.system(holderD);
    holderE = "autodock4 -p "+folders2[i_variable]+"/compound_target.dpf -l "+folders2[i_variable]+"/protein.dlg";
    os.system(holderE);
    
    with open('protein.dlg', 'r') as  f:
        content = f.read();
        holder1 = content.index("\n\nMODEL       ");
        holder2 = content.index("TER\nENDMDL\n");
        holder3 = content[holder1+1:holder2+11];
        
        output = open("bestmodel.pdb", "w");
        output.write(holder3);
        output.close();
        
        print("\nTarget 2's Compound "+str(i_variable+1)+" is done!\n");

index = list(range(0, 10));
values1 = list(range(0, 10));
values2 = list(range(0, 10));

location1 = "/home/number5/YUKTI/target_1";

folders1 = ["{}".format(x) for x in range(11)];
del folders1[0];

for i_variable1 in index:
    folders1[i_variable1] = os.path.join(location1, folders1[i_variable1]);

location2 = "/home/number5/YUKTI/target_2";

folders2 = ["{}".format(x) for x in range(11)];
del folders2[0];

for i_variable2 in index:
    folders2[i_variable2] = os.path.join(location2, folders2[i_variable2]);

for i_variable in index:
	
    os.chdir(folders1[i_variable]);
    x = "target 1";
    y = "compound "+str(i_variable+1);
    with open('protein.dlg', 'r') as  f:
        content = f.read();
        holderA = content.index("|___________\n");
        holderB = content[holderA+35:holderA+43];
        #print("Binding Energy for "+x+"\'s "+y+"\'s best model: "+holderB);

        values1[index[i_variable]] = float(holderB);
	
    os.chdir(folders2[i_variable]);
    x = "target 2";
    y = "compound "+str(i_variable+1);
    with open('protein.dlg', 'r') as  f:
        content = f.read();
        holderA = content.index("|___________\n");
        holderC = content[holderA+35:holderA+43];
        #print("Binding Energy for "+x+"\'s "+y+"\'s best model: "+holderC);

        values2[index[i_variable]] = float(holderC);
	
dex = list(range(0, 10));
take1 = list(range(0, 10));
take2 = list(range(0, 10));

v1 = sorted(values1);
v2 = sorted(values2);

for d in dex:
    take1[d] = "Compound "+str(values1.index(v1[d])+1)+" at "+str(v1[d]);
    take2[d] = "Compound "+str(values2.index(v2[d])+1)+" at "+str(v2[d]);

print("Top 10 results in our library of ligands for Target 1 in ascending order:");
for d in dex:
    print(str(d+1)+". "+take1[d]);
print("Top 10 results in our library of ligands for Target 2 in ascending order:");
for d in dex:
    print(str(d+1)+". "+take2[d]);
print("The result rankings will also be available as \"top_results.txt\" and will be updated every time this program is run.");

os.chdir("/home/number5/YUKTI");

output = open("top_results.txt", "w");

output.write("Top 10 results in our library of ligands for Target 1 in ascending order:\n");
for d in dex:
    output.write(str(d+1)+". "+take1[d]+"\n");
output.write("Top 10 results in our library of ligands for Target 2 in ascending order:\n");
for d in dex:
    output.write(str(d+1)+". "+take2[d]+"\n");
output.write("The result rankings will also be presented on the console and will be updated every time this program is run.");

output.close();
