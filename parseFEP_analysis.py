####
## Analysis/plots from parseFEP.log file
####

import numpy as np
import matplotlib.pylab as plt
%matplotlib inline

data_filename="./ParseFEP_forward.log"
data=[]

data_f=open(data_filename,"r")
for line in data_f:     
    cols=line.split(" ")
    
    data_line=[]
    for i in range(len(cols)):
        if cols[i]!="" and cols[i]!="\n" and i!=0:
            data_line.append(float(cols[i]))
#    print (data_line)
    
    data.append(data_line)
    
data_f.close()

data=np.array(data)
data_forward=np.transpose(data)

data_filename="./ParseFEP_backward.log"
data=[]

data_f=open(data_filename,"r")
for line in data_f:     
    cols=line.split(" ")
    
    data_line=[]
    for i in range(len(cols)):
        if cols[i]!="" and cols[i]!="\n" and i!=0:
            data_line.append(float(cols[i]))
#    print (data_line)
    
    data.append(data_line)
    
data_f.close()

data=np.array(data)
data_backward=np.transpose(data)

plt.errorbar(data_forward[0],data_forward[2],yerr=data_forward[3],color='k',label="forward")
plt.errorbar(data_backward[0],data_backward[2],yerr=data_backward[3],color='grey',label="backward")

plt.ylabel(r"$\Delta$G")
plt.xlabel(r"$\lambda$")

plt.legend(frameon=False)
