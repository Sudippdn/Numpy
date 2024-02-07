import numpy as np 

a = np.array([[1,6,2],[3,4,3]]) # multi-dimentional array
print(a)
# print(a.shape) # shape gives the no of rows and no of column

print(a[0,:]) # outputs: [1 6 2]
print(a[:,0]) # outputs [1,3]
print(a.T) # transpose array, outputs: [[1 3]
                                    #   [6 4]
                                    #   [2 3]] 

c = np.diag(a) # this will give digonals matrix of a
print(np.diag(a)) # on doing double diagonals we are getting identity matrix  

d = np.arange(1,9)
print(d)
print(d.shape)
e = d.reshape(2,4) # this will shape the matrix into 2x4 matrix
print(e)