#1- find the max value 
maximum = ndarray.max()

#2- find the min value
minimum = ndarray.min()

#3- calculates the row and column indexes of the maximum value of a given 2-dimensional ndarray
def max_row_col(ndarray):
    index = ndarray.argmax()
    return np.unravel_index(index,ndarray.shape)

#4-  calculates the row and column indexes of the minimum value of a given 2-dimensional ndarray
def min_row_col(ndarray):
    return np.unravel_index(ndarray.argmin(),ndarray.shape)

#5- find the mean value
mean = ndarray.mean()

#6- find the rows mean
row_means = ndarray.mean(axis=1)

#7- find the col mean
col_means = ndarray.mean(axis=0)

#8- compute the row sums
row_sums = ndarray.sum(axis=1)

#9- compute the col sums
col_sums = ndarray.sum(axis=0)

#10- round the float values
x = ndarray.round(decimals=2)

#11- multiply an array and round it
percentages = (ndarray*100).round(decimals=0)

#12- replace its maximum value by 0
ndarray[ndarray.argmax()] = 0

#13- replace its minmum value by 0
ndarray[ndarray.argmin()] = 0

#14- from negative value to possitive value
x = np.absolute(ndarray)

#15- given an ndarray and a value, 
#calculates which value of the provided ndarray is the closest to the provided value
def closest_number(ndarray,value):
    absolute_x = np.absolute(ndarray-value)
    index = absolute_x.argmin()
    return ndarray[index]