import time
import sys
import numpy as np

def comparision():
    size = 10
    l1 = range(size)
    print(sys.getsizeof(5) * len(l1))

    a1 = np.arange(size)
    print(a1.size * a1.itemsize)

    l2 = range(size)
    a2 = np.arange(size)

    start = time.time()
    result = [(x + y) for x, y in zip(l1, l2)]
    print("time", (time.time() - start) * 1000)

    start = time.time()
    resul = a1 + a2
    print("time", (time.time() - start) * 1000)

def operations():
    a=np.array([1,2,3,4])  # 1 dimensional
    a2=np.array([[1,2,3,3],[1,3,6,2],[1,4,6,3]])  # 2 dimensional
    print(a2.ndim)     # gives dimension of np array
    print(a2)
    print(a.itemsize)  # gives bytesize of each element
    print(a.dtype)   # dives datatype of elements
    a3=np.array([1,2,3,4],dtype=np.int8)
    print(a3.size)
    print(a2.shape)

    # creating array of complex numbers
    a3 = np.array([1, 2, 3, 4], dtype=complex)

    print(np.zeros((2,3)))   # create array with elements zero argument dimension
    print(np.ones((2,3)))

    print(np.arange(0,10))   # similar to range
    print(np.arange(1,10,2))

    print(np.linspace(1,5,10))  # create 10 numbers with linearly spaced between 1 & 5

    a2.reshape(4,3) # change dimension of array

    print(a2.ravel())  # converts to one dimensional array  dont change original but returns new wirh 1 d
    print(a2)


    print("min = ",a.min(),"  max = ",a.max(), "mean =",a.mean(), "sum = ",a.sum())

    # axis=0  => column axis = 1 =>  rows
    print(a2.sum(axis=1))  # sum of each rows
    print(a2.sum(axis=0))  # sum of columns

    print(np.sqrt(a))  # gives sqrt of each elements

    print(np.std(a2))  # gives standard deviation

    d = np.arange(1,10)
    e = np.arange(1,10)
    print(d+e)
    print(d-e)
    print(d*e)
    print(d/e)
    print(d.dot(e))   # matrix product

def more_fun():
    print(np.arange(1,11).reshape(2,5))


    # SLICING
    a=np.arange(1,10)
    print(a[0:2])
    print(a[-1])

    b=np.arange(30).reshape(5,6)
    print(b)
    print(b[1])
    print(b[0,1])
    print(b[0:2,3])
    print(b[-1])
    print(b[-1,0:2])
    print(b[:,4])
    print(b[:,1:3])
    print(b[1,:])

    # ITERATE THROUGH ALL THE ELEMENTS
    for elements in a.flat:
        print(elements)

    # stack two arrays
    d=np.arange(0, 10).reshape(2, 5)
    e=np.arange(10,20).reshape(2,5)
    print(np.vstack((d,e)))   # vertical stacking
    print(np.hstack((d,e)))  # horizontal stack

    print(np.hsplit(d,5)) # splits d into 5 equal array  horizontal
    print(np.vsplit(d, 2))  # splits d into 5 equal array vertically

    s=e>4
    print(s)

    print(e[s])  # returns numbers which  are true

    e[s]=1   # replaces number where true with 1
    print(e)


def iteration():
    d = np.arange(0, 10).reshape(2, 5)


    for x in np.nditer(d,order='C'):   # row major order
        print(x ,end=" ")

    for x in np.nditer(d,order='F'):    # column major order
        print(x , end=" ")

    for x in np.nditer(d,order='F',flags=["external_loop"]):  # print columns
        print(x)

    for x in np.nditer(d,op_flags=["readwrite"]):    # modify array
        x[...]=x*x
    print(d)

    f = np.arange(10, 20).reshape(2, 5)

    for x,y in np.nditer([d,f]):   # only possible if two array dimension same or any one is 1
        print(x,y)



if __name__ =="__main__":
    iteration()