import numpy as np 

# speed test or executionSpeed
from timeit import default_timer as timer 

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)

T = 1000

def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i]*B[i]
    return dot

def dot2():
    dot = np.dot(a,b)

start = timer()
for t in range(T):
    dot1()
end = timer()
t1 = end-start

start = timer()
for t in range(T):
    dot2()
end = timer()
t2 = end-start

print("\n\nList calculation:",t1)
print("np.dot", t2)
print("ratio:", t1/t2)
print(" ")




