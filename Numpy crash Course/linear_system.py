import numpy as np 
from timeit import default_timer as timer 
import timer_for_linalg # calling timer_for_linalg to print the time taken by each methods

# we can import and run other py files too
# import timer
# import eigenVector
# import Basic_Array
# import dot_product


T = 1

A = np.array([[1,1],[1.5,4.0]])
b = np.array([2200,5050])

# as we have formula, 
# Ax = b => x = inverse(A)*b
def dot():
    answer = np.linalg.inv(A).dot(b)
    print(answer)


def solve():
    answer = np.linalg.solve(A,b)
    print(answer)







