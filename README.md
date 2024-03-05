###### *I will be uploading NumPy documentations here*
<img src = "https://github.com/Sudippdn/Numpy/blob/main/Image/logo.png" height = 400, breadth = 500>

[TABLE OF CONTENTS](https://github.com/Sudippdn/Numpy)

S.N.| Topics
----|--------
1   | [Introduction](#Introduction)
2   | [Installation](#installation)
3   | [Import Numpy](#import)
4   | [NumPy Array](#npArray)
5   | [Making Array](#making_array)
6   | [Comparison Between Array and Numpy](#comparison)
7   | [Shape and Reshape in NumPy](#shape_reshape)
8   | [NumPy Array Slicing](#slicing)
9   | [Transpose of Matrix in NumPy](#transpose)
10  | [Diagonal](#diag)
11  | [Arange](#arange)
12  | [Eigen Value and Eigen Vector](#EvEV)
13  | [Linear Algebra](#LA)
14  | [Timing Comparison](#timing_comparison)


<a name = "Introduction"></a>
# Introduction

<code style="color: red"> Numpy </code>
(Numerical Python) is a python library that provides multidimentional array. Numpy has ndarray at its core which encapsulated n-dimentional array of the homogeneous data type. In the this library, we can differenciate between array and list and while calculating the execution time, we found numpy executes more than 180 times faster than list. It can be use to calculate eigen values and eigenvectors of a matrices. Numpy also contais in-build function to interpret linear algebra which are shown below along with the examples.

<a name = "installation"></a>
## How to install NumPy in IDE?
You can install numpy package in VS Code using the following command in terminal but first you should have pip install in the same path of your python file.

![](https://github.com/Sudippdn/Numpy/blob/main/Image/installNumpy.png)

<a name = "import"></a>
### How to import NumPy in your python file?
TO import NumPy module in your, use the following code:

![](https://github.com/Sudippdn/Numpy/blob/main/Image/importNumpy.png)

<a name = "npArray"></a>
### Array in NumPy
You can implement array in NumPy by passing list inside the argument(paranthesis).

![](https://github.com/Sudippdn/Numpy/blob/main/Image/ArrayinNumpy.png)

```python
import numpy as np 
a1 = np.array([1,2,3])
a2 = a1 * np.array([1,2,3])
print(a1,a2) # output = [1 2 3] [1 4 9]
```

<a name = "making_array"></a>
>## Array Creation in NumPy
>
>There are 6 general mechanisms for creating arrays:
>- Conversion from other Python structures (i.e. lists and tuples)
>- Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)
>- Replicating, joining, or mutating existing arrays
>- Reading arrays from disk, either from standard or custom formats
>- Creating arrays from raw bytes through the use of strings or buffers
>- Use of special library functions (e.g., random)

<a name = "comparison"></a>
### [Differnce between numpy and list](https://github.com/Sudippdn/Numpy)

### Dot product between python list and NumPy array
#### a. Dot Product using list
```python
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)
```
#### b. Dot product using numpy
```python
dot = np.dot(a1,a2)
print(dot)  # output = 36
```
#### Comparing execution Time
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
##### _While runing the above code, if is found that array is 125+ times faster than Python list_
![](https://github.com/Sudippdn/Numpy/blob/main/Image/LvAExecution%20TIme.png)

<a name = "shape_reshape"></a>
### shape and reshape
                                              
<code style="color: red"> shape </code> --> NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding element, which means that the shape function will give the dimention of the dataset in NumPy.

 ![](https://github.com/Sudippdn/Numpy/blob/main/Image/shape.png)

<code style="color: red"> .reshape(rows, columns) </code> --> Reshape will make a matrix form from the arrange. So, it depends upon if arrange has proper elements or not.
```python
import numpy as np 
a = np.arrange(8,14)
b = a.shape # shape gives the no of rows and no of column
c = b.reshape(2,4)
print(c)
# outputs: [ 6  7  8  9 10 11 12 13] # print(a)
            [[ 6  7  8  9]
             [10 11 12 13]]
```

<a name = "slicing"></a>
#### Numpy array slicing
```python
print(a[0,:]) # outputs: [1 6 2]
print(a[:,0]) # outputs [1,3]
```
![](https://github.com/Sudippdn/Numpy/blob/main/Image/slicing.png)

<a name = "transpose"></a>
#### Transpose matrix
```python
print(a.T) # transpose array, outputs: [[1 3]
                                    #   [6 4]
                                    #   [2 3]]
```
### Array attributes of NumPy
This section covers the ndim, ndmin,size, dig, and dtype attributes of an array.
### diag
#### - For 1d array
This will give digonals matrix of a. In this function, when 1D array is passed, it will create a n x n diagonal matrix

![](https://github.com/Sudippdn/Numpy/blob/main/Image/ndiag%20for%201-D%20array.png)

#### - For multidimentional array
When we pass multi-dimentional array in diag, it will take a diagonal elements to make diagonal matrix which can be seen from the picture below:

![](https://github.com/Sudippdn/Numpy/blob/main/Image/ndiag%20for%20multi-D%20array.png)

```python
c = np.diag(a) # this will give digonals matrix of a
print(np.diag(a))  
```
![](https://github.com/Sudippdn/Numpy/blob/main/Image/ndiag%20for%201-D%20array.png)
#### - Arange data
```python
d = np.arange(1,9)
print(d)
```
#### - Reshape 
```python
print(d.shape)
e = d.reshape(2,4) # this will shape the matrix into 2x4 matrix
print(e)
```

<a name = "arange"></a>
#### - arange
<code style="color: red"> np.arrange(starting, ending) </code> --> takes two attributes and display the range values while printing.  

![](https://github.com/Sudippdn/Numpy/blob/main/Image/arange%20and%20reshape.png)

<a name = "EvEV"></a>
### EigenValue and EigenVectors
Numpy is widely used in mathematics and this python library makes it easy to calculate eigenValue and eigenVectosrs
```python
import numpy as np 

a = np.array([[1,2],[3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvalues)
print(eigenvectors)
```
<a name = "LA"></a>
### Linear Algebra
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

<a name = "timing_comparison"></a>
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
