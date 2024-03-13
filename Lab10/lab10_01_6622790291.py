import numpy as np
a=int(input("Input size of matrix:"))
total_array=[]
for i in range(1,a+1,1):
    array=[]
    for j in range(1,a+1,1):
        b=int(input("Input element at row %d column %d: " %(j,i)))
        array.append(b)
    total_array.append(array)
np.array(total_array)
print("Output:")
print("Matrix:")
print(np.array)
determinant=np.linalg.det(np.array)
print("Determinat=",determinant)
print("Inverse Matrix=")
inverseMatrix=np.linalg.inv(np.array)
print(inverseMatrix)
    
        
    