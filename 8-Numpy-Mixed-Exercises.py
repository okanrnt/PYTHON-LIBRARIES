import numpy as np

# making exercise using a few methods about Numpy library
np_array = np.array([10,15,30,45,60])
arange_array = np.arange(5,15)
space_arange_array = np.arange(50,100,5)
zeros_array = np.zeros((4,10))
ones_array = np.ones((5,10))
equal_array = np.arange(0,100,20)
random_array = np.random.randint(0,30,5)
float_array = np.linspace(-1,1,10)

# making a random array that has 15 items and I converted it to an (3x5) array.
random_array2 = random_array = np.random.randint(10,50,15)
random_shape = random_array2.reshape(3,5)
sum_rows = random_shape.sum(axis = 1)
sum_columns = random_shape.sum(axis = 0)
min_value = random_shape.min()
max_value = random_shape.max()
average_value = random_shape.mean()

# making an array that has 9 items and make indexing over its elements.
new_Array = np.arange(11,20)
select_items = new_Array[:3]
reverse_array = new_Array[::-1]
new_array_shape = new_Array.reshape(3,3)
first_row = new_array_shape[0]
select_special = new_array_shape[1,2]
all_first_elements = new_array_shape[:,0]
multiplication = new_array_shape ** 2

# making an array from -50 to 50 and printed the positive-even numbers with boolean.
boolean_array = np.arange(-50,50)
boolean_plus = 0 < boolean_array
boolean_plus_values = boolean_array[boolean_plus]
boolean_even = boolean_plus_values%2 == 0
boolean_even_values = boolean_plus_values[boolean_even]