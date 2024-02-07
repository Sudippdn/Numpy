import numpy as np 

a = np.array([1,2,3])
print(f'\nOriginal list of array value: {a}')
a[0] = 10   # value of position at 0 = 1 is changed to 10
print(f"When 1st position is replaced by 10: {a}")

b = a * np.array([2,0,2])
print(f"Value after multiplying array data: {b}\n")
