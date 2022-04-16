import numpy as np

#1- the values at the even indexes of x
x = np.array(the_list)
even = x[::2]

#2- convert to the array from the list
x = np.array(the_list)
# assign the values at the odd indexes of x
odd = x[1::2] 

#3- Convert to the array from the list
x = np.array(the_list)
# reverse the array
reverse = x[::-1]

#4- returns an ndarray that contains the first half of the provided ndarray
def first_half(x):
    return x[:len(x)//2]

#5-  returns an ndarray containing the second half of the provided ndarray
def second_half(x):
    return x[len(x)//2:]

#6- combine two or more arrays
x = np.array(values1)
y = np.array(values2)

concat = np.concatenate([x,y])

#7-  reverse the values of a 1-dimensional ndarray while skipping every other value
x = np.array(values)
reverse_skip = x[1::2][::-1]

#8- obtain an ndarray where both the rows and the columns are in reverse order
# 2-dimensional ndarray
x = np.array(values)
rows = x[::-1]
reverse_2d = []
for row in rows:
    reverse_2d.append(row[::-1])
reverse_2d = np.array(reverse_2d)

#alternative
x = np.array(values)
reverse_2d = x[::-1, ::-1]


#9-  given a 2-dimensional array and a list of row indexes, 
#returns a 2-dimensional array consisting only of those rows

def select_rows(ndarray, row_indexes):
    return ndarray[row_indexes, :]

# Alternative solution
def select_rows(ndarray, row_indexes):
    return ndarray[row_indexes]

#10- returns a 2-dimensional array consisting only of those columns
def select_columns(ndarray,col_indexes):
    return ndarray[:,col_indexes]

#11- # increase the row in index that want 
def copy_row_k_times(ndarray,row_index,num_copies):
    return ndarray[[row_index]*num_copies]


#12- select rows and columns
x = array2d[:,[1,2]]
y = array2d[[0,2],:]
z = array2d[2,[1,2,3]]


#13- select cells
x = array2d[[1,3],0::2]
y = array2d[[0,2],1::2]
z = array2d[[0,2],1:4]

#14- select rows and columns

x = array2d[:,[2,3,4]]
y = array2d[[1,2,3],1::]
z = array2d[[0,1,2],0:4]

#15- given a 2-dimensional array and two row indexes, swaps those two rows
def swap_rows(ndarray, row_index1, row_index2):
    row1 = ndarray[row_index1].copy()
    ndarray[row_index1] = ndarray[row_index2]
    ndarray[row_index2] = row1

# Alternative solution
def swap_rows(ndarray, row_index1, row_index2):
    ndarray[[row_index1, row_index2]] = ndarray[[row_index2, row_index1]] 

#16-  given a 2-dimensional array and two column indexes, swaps those two columns
def swap_cols(ndarray,col_index1,col_index2):
    ndarray[:,[col_index1,col_index2]] = ndarray[:,[col_index2,col_index1]]