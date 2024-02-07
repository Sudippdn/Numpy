from timeit import default_timer as timer
import random

T = 1

def suru():
    a = 0
    while a<10000:
        print(a)
        a += 1

start = timer()
for t in range(T):
    suru()
end = timer()
Timing = end-start

# print("The value of a is: ", answer)
print("Total time taken to run this code is",Timing)
