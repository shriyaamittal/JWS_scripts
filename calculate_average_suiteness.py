import os
import numpy as np

structure="RS8_no_overhang_primer_Urun"
num_structures=50

f_write=open(structure+".suiteness.txt","w")

for i in range(1,num_structures+1):
#for i in range(1,5):
	pdb_filename=structure+"."+str(i)+".pdb"

	os.system("rm data.csv")

	cmd="rna_suitename.macosclangrelease -s "+pdb_filename+" | grep -e \"Residue \" | awk -v OFS=, \'{print $1, $4, $5, $6,$NF}\' > data.csv"
	os.system(cmd)

	f=open("data.csv","r")
	suiteness=[]
	for line in f:
		s=float(line.split(",")[-1].strip("\n"))
		suiteness.append(s)
	f.close()
	avg_suiteness=round(np.average(suiteness),3)
	print (avg_suiteness)
	f_write.write(pdb_filename+","+str(avg_suiteness)+"\n")

f_write.close()
