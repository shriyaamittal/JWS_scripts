####
## Analysis/plots from parseFEP.log file
####

import numpy as np
input_filename="ParseFEP"

f_in=open(input_filename+".log","r")

output_filename=input_filename+"_forward.log"
f_out=open(output_filename,"w")
f_out.write("λ\t\tΔΔA\t\tΔA\t\tδε\n")

for line in f_in:
    if "forward:" in line and "gc" not in line:
        cols=line.split(" ")
        out_line=""
        for i in range(1,len(cols)):
            if cols[i]!="" and cols[i]!="\n":
                out_line+=cols[i]+"\t"
        out_line=out_line[:-1]+"\n"
        f_out.write(out_line)
        
f_in.close()
f_out.close()

f_in=open(input_filename+".log","r")

output_filename=input_filename+"_backward.log"
f_out=open(output_filename,"w")
f_out.write("λ\t\tΔΔA\t\tΔA\t\tδε\n")

for line in f_in:
    if "backward:" in line and "gc" not in line:
        cols=line.split(" ")
        out_line=""
        for i in range(1,len(cols)):
            if cols[i]!="" and cols[i]!="\n":
                out_line+=cols[i]+"\t"
        out_line=out_line[:-1]+"\n"
        f_out.write(out_line)
        
f_in.close()
f_out.close()

f_in=open(input_filename+".log","r")

output_filename=input_filename+"_BAR.log"
f_out=open(output_filename,"w")
f_out.write("λ\t\tλ+δλ\t\tΔΔA\t\tΔA\t\tC\t\tΔδe\t\tδe\n")
f_out.write("0.00000"+"\t"+"0.00000"+"\t"+"0.00000"+"\t"+"0.00000"+"\t"+"0.00000"+"\t"+"0.00000"+"\t"+"0.00000"+"\n")

for line in f_in:
    if "BAR-estimator:" in line and "λ" not in line and "total" not in line:
        cols=line.split(" ")
        out_line=""
        for i in range(1,len(cols)):
            if cols[i]!="" and cols[i]!="\n":
                out_line+=cols[i]+"\t"
        out_line=out_line[:-1]+"\n"
        f_out.write(out_line)
        
f_in.close()
f_out.close()