import numpy as np
data=np.loadtxt("C:/Users/LabCom/Desktop/6622790291/grade.tsv",delimiter=" ",dtype=float)
list1=data[:,1:]
credits=np.array([3,2,1,3,3,3])
gpa_array=[]
for i in range(0,len(list1)):
    multiplied=np.multiply(credits,list1[i])
    sumed=np.sum(multiplied)
    credits_summed=np.sum(credits)
    gpa_array.append(np.divide(sumed,credits_summed))
print("Student ID","   GPA")
for i in range(0,len(list1)):
    print("%i   %.2f" %(data[i][0],gpa_array[i]))

    