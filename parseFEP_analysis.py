import numpy as np
import matplotlib.pylab as plt
#%matplotlib inline

def func_read_file(filename):
    data=[]

    first_line_flag=0
    
    data_f=open(filename,"r")
    for line in data_f:     
        if first_line_flag==0:
            first_line_flag+=1
            continue;
        cols=line.strip("\n").split("\t")
    
        data_line=[]
        for i in range(len(cols)):
            data_line.append(float(cols[i]))

        data.append(data_line)
    
    data_f.close()
    
    data=np.array(data)
    return np.transpose(data)

## Forward and Backward Plot
    
data_filename="./ParseFEP_mg_annihilation_forward.log"
data_forward=func_read_file(data_filename)

data_filename="./ParseFEP_mg_annihilation_backward.log"
data_backward=func_read_file(data_filename)

plt.plot(data_forward[0],data_forward[2],"o",markersize=5, color="k",label="forward")
plt.plot(data_backward[0],data_backward[2],"v",markersize=5, color="k",label="backward")
plt.errorbar(data_forward[0],data_forward[2],yerr=data_forward[3],color='k')
plt.errorbar(data_backward[0],data_backward[2],yerr=data_backward[3],color='k')

plt.legend(frameon=False)

plt.ylabel(r"$\Delta$G (kcal/mol)")
plt.xlabel(r"$\lambda$")

## BAR plot

data_filename="./ParseFEP_mg_annihilation_BAR.log"
data_BAR=func_read_file(data_filename)

plt.plot(data_BAR[1],data_BAR[3],"x",markersize=5, color="k")
plt.errorbar(data_BAR[1],data_BAR[3],yerr=data_BAR[6],color='k')

plt.ylabel(r"$\Delta$A$^{BAR}$ (kcal/mol)")
plt.xlabel(r"$\lambda$")