'''NumPy Broadcasting Practice Problems'''
#1- write an array
x = np.zeros((5,5))
x += np.arange(5).reshape((5,1))

#2- multiply each of its entries by five
x = array2d*5

#3- set all even entries to zero and all odd entries to one
x = array2d%2

#4- set all even entries to zero. Odd entries should remain unchanged
x *= (array2d % 2)

#alternative
x[x%2==0] = 0

#5-  set all odd entries to zero. Even entries should remain unchanged
x *= (1 - array2d % 2)

#6- takes as input a positive integer n and generates an n by n ndarray such that entry (i, j) is equal to i + j
def generate_sums(n):
    x = np.arange(n)
    return x + x.reshape((n, 1))

#7-calculate the minimum distance between two points
def min_distance(points, target):
    # x and y coordiantes of both sets of points
    x = points[:, 0]
    y = points[:, 1]
    # the distance between target and all other points
    distances = np.sqrt((x - target[0]) ** 2 + (y - target[1]) ** 2)
    return distances.min()


'''NumPy Sorting Practice Problems'''
#1- returns True if the ndarray is sorted and False otherwise
def check_sorted(x):
    return np.all(x[:-1] <= x[1:])

#2- sort an array
x_sorted = np.sort(array)


#3- don't keep the original ndarray
array.sort()

#4- sort each of its row
array2d.sort(axis=1)

#5- sort each of its columns
array2d.sort(axis=0)

#6- returns sorted indexes in a array
sorted_indexes = np.argsort(array)

#7- sort the first seven value in an array
seven_smallest = np.sort(x)[:7]

# Alternative answer
seven_smallest = np.partition(x, 7)[:7]