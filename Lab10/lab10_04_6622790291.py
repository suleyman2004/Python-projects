import numpy as np
data=np.loadtxt("C:/Users/LabCom/Desktop/6622790291/sales.tsv",delimiter="\t",dtype=int)
mat=data[:,1:]
s=np.sum(mat,axis=1)
print(s)
asc_ind=np.argsort(s)
print(asc_ind)
asc_val=s[asc_ind]
print(asc_ind)


for i in range(1,len(s)+1):
    print(data[asc_ind[-i],0],s[asc_ind[-i]])