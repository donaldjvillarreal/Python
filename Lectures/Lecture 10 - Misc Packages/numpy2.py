import numpy as np

a = np.array([[1, 2, 3], [44, 55, 66], [777.7, 888.8, 999.9]], float)
print(a)
print()

#Index
print(a[0,2])
print()

#Transpose
print(a.T)
print()

#Inverse
print(np.linalg.inv(a)) #If you're just doing linear algebra stuff look into numpy mats
print()
