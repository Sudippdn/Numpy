import numpy as np 

l1 = [1,2,3]
l2 = [1,2,3]

a1 = np.array([1,2,3])
a2 = a1 * np.array([1,2,3])
print(a1,a2)
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

# Methods to perform dotproduct in python array
# Method 1:
dot = np.dot(a1,a2)
print(dot)

# Method 2:
sum = a1*a2
dot  = (a1*a2).sum() # or dot = sum.sum()
# print(sum)
print(dot)