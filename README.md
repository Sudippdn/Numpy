# Numpy
<code style="color: red"> Numpy </code>
is a python library that is used while working with array. In the this library, we can differenciate between array and list and while calculating the execution time, we found numpy executes more than 180 times faster than list. It can be use to calculate eigen values and eigenvectors of a matrices. Numpy also contais in-build function to interpret linear algebra which are shown below along with the examples.

## Differnce between numpy and list

### Inputs
```python
import numpy as np 

l1 = [1,2,3]
l2 = [1,2,3]

a1 = np.array([1,2,3])
a2 = a1 * np.array([1,2,3])
print(a1,a2) # output = [1 2 3] [1 4 9]
```
### a. Dot Product using list
```python
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)
```
### b. Dot product using numpy
```python
dot = np.dot(a1,a2)
print(dot)  # output = 36
```
## Comparing executin Time
```python
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
```
## EigenValue and EigenVectors
Numpy is widely used in mathematics and this python library makes it easy to calculate eigenValue and eigenVectosrs
```python
import numpy as np 

a = np.array([[1,2],[3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvalues)
print(eigenvectors)
```
## .shape
<code style="color: red"> .shape </code> --> Get the Shape of an Array​​, NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
```python
import numpy as np 
a = np.array([[1,6,2],[3,4,3]]) # multi-dimentional array
print(a.shape) # shape gives the no of rows and no of column
```
Numpy array slicing
```python
print(a[0,:]) # outputs: [1 6 2]
print(a[:,0]) # outputs [1,3]
```
### Transpose matrix
```python
print(a.T) # transpose array, outputs: [[1 3]
                                    #   [6 4]
                                    #   [2 3]]
```
### np.diag(attribute)
```python
c = np.diag(a) # this will give digonals matrix of a
print(np.diag(a)) # on doing double diagonals we are getting identity matrix  
```
### Arrange data
```python
d = np.arange(1,9)
print(d)
```
### Reshape 
```python
print(d.shape)
e = d.reshape(2,4) # this will shape the matrix into 2x4 matrix
print(e)
```
## Linear Algebra
```python
import numpy as np 
from timeit import default_timer as timer 
import timer_for_linalg # calling timer_for_linalg to print the time taken by each methods

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
```
### timer section
```python
from linear_system import dot, solve
from timeit import default_timer as timer 
T =1
start = timer()
for t in range(T):
    dot()
end = timer()
t1 = end - start

start = timer()
for t in range(T):
    solve()
end = timer()
t2 = end - start

print("Time taken by dot:", t1)
print("Time taken by solve:", t2)
print("Timing ratio =",t1/t2)
```
