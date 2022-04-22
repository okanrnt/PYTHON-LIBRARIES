import numpy as np

# 1- find the datatpe
def get_datatype(x):
    return x.dtype

print(get_datatype(ndarray))

#2- change the datatype to float32
def change_datatype(x,datatype):
    return x.astype(datatype)

x = np.array([1, 2, 3, 4])
y = change_datatype(x, 'float32')
print(y.dtype)

# 3- get info for an array
def get_info(x):
    return x.ndim,x.shape,x.size

x = np.array([[1, 2], [3, 4]])
print(get_info(x))

# 4- get the range of int8 datatype
def get_int_range(int_dtype):
    info = np.iinfo(int_dtype)
    return info.min, info.max
   
print(get_int_range(np.uint8))

# 5- get the range of float32 datatype
def get_float_range(float_dtype):
    info = np.finfo(float_dtype)
    return info.min,info.max

print(get_float_range(np.float32))

# 6- find how many bytes it consumes in memory
num_bytes_array = ndarray.nbytes

#alternative
num_bytes_x = ndarray.size * ndarray.itemsize

# 7- multiply all values in an ndarray 
product = ndarray.prod(dtype=np.float64)

# 8- an ndarray with floating-point numbers, convert it to 64-bit integers
y = ndarray.astype('int64')

# 9- save an ndarray into a .npy file
np.save("file_name.npy",ndarray)

# 10- load an ndarray from a .npy file
x = np.load("file_name.npy")

# 11- get without nan values
y = ndarray[~np.isnan(ndarray)]

# 12- Remove from an ndarray all rows that contain at least one NaN value
x = ndarray[~np.isnan(ndarray).any(axis=1)]

# 13- Remove from an ndarray all columns that contain at least one NaN value
x = ndarray[:,~np.isnan(ndarray).any(axis=0)]

# 14- Replace all missing values from an ndarray by zeros
ndarray[np.isnan(ndarray)] = 0

# 15- Calculate the row sums of a ndarray
row_sums = np.nansum(ndarray,axis=1)

# 16- Calculate the row products of a ndarray 
row_products = np.nanprod(ndarray,axis=1)

# 17- Calculate the row means of a ndarray
row_means = np.nanmean(ndarray,axis=1)