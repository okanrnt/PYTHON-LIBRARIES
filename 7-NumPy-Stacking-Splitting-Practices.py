import numpy as np

#1- create a 2-dimensional array whose rows are the 1-dimensional arrays in a list
x = np.vstack(lst)


#2- create a 2-dimensional array resulting from stacking the 2-dimensional arrays in a list on top of each other
x = np.vstack(lst)

#3-  create a 2-dimensional array that results from sticking the 2-dimensional arrays in a list horizontally
x = np.hstack(lst)

#4-  split a 2-dimensional array vertically into parts, each with three rows
first_3,last_3 = np.split(array2d,2)

#5- split a 2-dimensional array vertically into parts, each with a single row
x_rows = np.split(array2d,6)

#6- split a 2-dimensional array vertically into parts, each with four rows
first_four, last_four = np.split(array2d,2)

#7- split a 2-dimensional array horizontally into parts, each with three columns
x1,x2,x3 = np.split(array2d,3,axis=1)

#8- split a 2-dimensional array horizontally into parts, each with two columns
x1,x2,x3,x4,x5 = np.split(array2d,5,axis=1)

#9- split a 2-dimensional array horizontally into two parts, each with half of the columns
first_half,second_half = np.split(array2d,2,axis=1)

#10- split a 2-dimensional array vertically into three uneven parts
x1,x2,x3 = np.split(array2d,[3,5])

#11- split a 2-dimensional array vertically into two uneven parts
x1,x2 = np.split(array2d,[2])

#12-  split a 2-dimensional array vertically into three uneven parts
x1,x2,x3 = np.split(array2d,[1,5])

#13- split a 2-dimensional array horizontally into three uneven parts
x1,x2,x3 = np.split(array2d,[2,6],axis=1)

#14- split  a 2-dimensional array horizontally into four uneven parts
x1,x2,x3,x4 = np.split(array2d,[2,4,7],axis=1)

#15- split  a 2-dimensional array horizontally into three uneven parts
x1,x2,x3 = np.split(array2d,[3,7],axis=1)