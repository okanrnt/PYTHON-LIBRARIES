import numpy as np

#1- seven rows and five columns in which each entry is equal to one 
x = np.ones((7,5))

#2-four rows and six columns in which each entry is equal to zero
x = np.zeros((4,6))

#3- write an array is equal to one and equal to 0 the wanted indecies
def framed_zeros(num_rows, num_cols):
    x = np.ones((num_rows, num_cols))
    x[1:-1, 1:-1] = 0
    return x

#4- write an array is equal to zero and equal to 1 the wanted indecies
def alternate_ones_zeros(num_rows,num_cols):
    x = np.zeros((num_rows,num_cols))
    x[::2,::2] = 1
    x[1::2,1::2] = 1
    return x

#5- binary
def invert_binary(ndarray):
    return 1-ndarray

#6- write a 1-dimensional array with the integers from 0 to 100 (inclusive)
int_0_to_100 = np.arange(0,101)

#7- write a 1-dimensional array with the even numbers from 2 to 1000 (inclusive)
even_2_to_1000 = np.arange(2,1001,2)

#8- returns a 2-dimensional array with shape
def numbered_table(size):
    x = np.arange(1,size**2+1)
    return x.reshape(size,size)


#9- from 1-dimensional to 2-dimensional
def dim1_to_dim2(ndarray):
    return ndarray.reshape(1,len(ndarray))

# Alternative solution
def dim1_to_dim2(ndarray):
    return ndarray[np.newaxis]

#10- takes as input a 1-dimensional ndarray and returns a single column 2-dimensional ndarray containing those values
def row_to_col(ndarray):
    return ndarray.reshape(len(ndarray),1)
#Alternative
def row_to_col(ndarray):
    return ndarray[:,np.newaxis]

#11- write a 10 by 10 ndarray in which each entry is equal to 5
fives = np.full((10,10),5)

#12- indexing and shaping
x = np.ones((10,10))
x[:5,5:] = 2
x[5:,:5] = 3
x[5:,5:] = 4

#13- indexing and shaping
array = np.arange(1,26).reshape(5,5)
x = np.tile(array,(2,2))