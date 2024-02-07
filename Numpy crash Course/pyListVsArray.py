import numpy as np

# l = [1,2,3] #list as l
# a = np.array([1,2,3]) # array as a 
# l.append(4) # or l = l + [4]
# print(l)  # output [1, 2, 3, 4]
# a = a - np.array([4])
# print(a)  # output [-3 -2 -1]

# Methods of arthemetic in numpy
# 1. if you mentioned only one array inside the numpy array then
#    it will be same for remaining positions of the array
# Example:
# mul = np.array([1,2,3])
# mul = mul * np.array([3]) # it can be written as mul = mul * 3
# print(mul)    # output = [3,6,9]

# 2. if not then you need to mention the same number of array enements 
#    to do arithmetic operations
# Example:
multiply = np.array([1, 2, 3])
print(multiply)
multiply = multiply * np.array([3, 4, 5])
print(multiply)  # [1, 2, 3, 4]
#                     # [1 2 3]
#                     # [3  8 15]

# Key points:
# In array, we can't add new element like in the list as array doesn't recognize append
