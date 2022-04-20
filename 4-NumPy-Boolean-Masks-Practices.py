import numpy as np

#1- even values
even_values = array2d[array2d%2 == 0]

#2- odd values
odd_values = array2d[array2d%2 == 1]

#3- positive values
positive_values = array2d[array2d>0]

#4- negative values
negative_values = array2d[array2d<0]

#5- compute the length of the positive,negative,zero values
def count_values(array2d):
    return len(array2d[array2d<0]),len(array2d[array2d==0]),len(array2d[array2d>0])

#6- sum is larger than 30
cols_larger_30 = array2d[:,array2d.sum(axis=0)>30]

#7- find the perfect squares
ceil_sqrt = np.ceil(np.sqrt(array))
squares = array[ceil_sqrt * ceil_sqrt == array]

#8- extract the rows without zeros in an array
mask = np.count_nonzero(array2d, axis=1) == array2d.shape[1]
rows_without_zeros = array2d[mask]

#9- extract the rows with zeros in an array
mask = np.count_nonzero(array2d, axis=1) < array2d.shape[1]
rows_with_zeros = array2d[mask]

#10- extract the cols without zeros in an array
mask = np.count_nonzero(array2d,axis=0) == array2d.shape[1]
cols_without_zeros = array2d[:,mask]


#11- extract the cols with zeros in an array
mask = np.count_nonzero(array2d, axis=0) < array2d.shape[0]
cols_with_zeros = array2d[:,mask]

#12- returns whether any student had a grade equal to 100
def has_perfect_score(grades):
    return (grades == 100).any()

#13- returns whether all students had a score of at least 50 or not
def all_passed(grades):
    return (grades > 50).all()

#14-  returns a dictionary that counts how many grades fall in each category
def grade_category_count(grades):
    ans = {}
    ans['A'] = grades[(grades >= 90) & (grades <= 100)].size
    ans['B'] = grades[(grades >= 80) & (grades <=  89)].size
    ans['C'] = grades[(grades >= 70) & (grades <=  79)].size
    ans['D'] = grades[(grades >= 65) & (grades <=  69)].size
    ans['E'] = grades[(grades >= 50) & (grades <=  64)].size
    ans['F'] = grades[(grades >=  0) & (grades <=  49)].size
    return ans


#15- multiply each value that is smaller than 100 by 2
array2d[array2d<100]*=2

#16-  turn every entry into an even number
array2d[array2d%2==1] += 1

#17- the value separating the lower half from the higher half
def partition_by_median(array):
    median = np.median(array)
    return array[array<=median],array[array>median]


#18- remove all of its values that are not whole numbers
x = array[np.round(array) == array]