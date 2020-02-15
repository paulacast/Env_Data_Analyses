# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Name:         Numpy_Ecercises.py
#------------------------------------------------------------------------------


# Numpy Exercises
# The goal of these exercises is to get practice with Numpy arrays
# - For most of these you could type out the array structure, but the goal is 
#   use indexing and Numpy functions to complete the exercises

import numpy as np

# 1: Create a 1-D zeros array of size 10, but reassign the fifth value to 1
a_array_zeros = np.zeros([10])
a_array_zeros[4] = 1

# 2: Create a 1-D array with values ranging from 10 to 49
b_array = np.arange(10,50)

# 3: Reverse the array from #2 (first element becomes last)
c_array = np.flipud(b_array)

# 4: Create a 3x3 matrix with values ranging from 0 to 8
d_array = np.arange(0,9)
d_array = d_array.reshape(3,3)

# 5: Find the indices of non-zero elements in the array below (mask)
a = np.array([1,2,0,0,4,0])
mask = (a <= 0)
a_inverse = a[~mask]


# 6: Create a 3x3 identity matrix
f_matrix = np.eye(3)

# 7: Create a 10x10 array with random values and find the minimum and maximum values
g_array = np.random.rand(10,10)
g_array_min = g_array.min()
g_array_max = g_array.max()

# 8: Using the resulting matrix from #7, 
#       + print all the elements in column 4
#       + print all the elements in row 3
#       + print a 4x4 array of the element in the middle of the matrix
#       + print the last two values in column 10

print (g_array[:,3])
print(g_array[2])
print(g_array[5:9,5:9 ] )
g_array_column10 = g_array [:,9]
print (g_array_column10[8:10])

# 9: Create a random 1-D of size 30 and find the mean value

h_array = np.random.rand(30)
h_array_mean = h_array.mean()

# 10: Create a blank 8x8 matrix and fill it with a checkerboard pattern, 0 and 1
#       Using fancy indexing

blank_array = np.zeros([8,8])
blank_array[1::2,::2] = 1
blank_array[::2,1::2] = 1


# 11: Create a checkerboard 8x8 matrix using the tile function
a = np.array([[0,1],[1,0]])
tile = np.tile(a,(4,4))

# 12: Create a vector of size 10 with values ranging from 0 to 1, both included
vector = np.linspace(0, 1, 10)

# 13: Subtract the mean of each row of the matix below
X = np.random.rand(5, 10)
x_mean_perRow = X.mean(axis=1)
x_mean_row = np.array([x_mean_perRow])
sub = X - x_mean_row.T

# 14: Sort resulting array from #13 by the 3th column

sub_sort = sub[sub[:,2].argsort()]

# 15: Create two random 1-D arrays of length 10, merge them into a 2x10 array, 
#       then a 10x2 array

o_array = np.random.randint(1,1000,(10))
p_array = np.random.randint(1,1000,(10))

o_p_array = np.concatenate((o_array, p_array), axis=0)
o_p_array_2_10 = o_p_array.reshape(2,10)
o_p_array_10_2 = o_p_array.reshape(10,2)

# 16: Create a array of random integers between -100 and 100 of size 9x12, 
#       create a boolean mask of the negative values

q_array = np.random.randint(-100,100,[9,12])
mask = (q_array < 0)


# 17: Using the array and mask from #16, create a new array of just the negative values
q_array_negative = q_array[mask]


# 18: Using the array and mask from #16, modify the randow array so that the 
#       negative numbers are muliplied by 2 and the positive number are divided
#       by 2

q_array[mask] = q_array[mask] * 2
q_array[q_array > 0] = q_array[q_array >0] / 2


# 19: Offset sine waves (will require research...)

#   A) create two numpy arrays
#       (a) from 0 - 2, by 0.1 steps
#       (b) a calculated array that is the sine of array (a)


s_array = np.arange(0, 2, 0.1)
s_array_sin = np.sin(s_array)

#
#   B) Write code that can create two more arrays that are 
#       0.5 and -0.5 parallel offsets from the sine 
#       !!! Hint: sin + 0.5 and sin - 0.5 are not parallel offsets.

s_array_cos = np.cos(s_array)
s_plus_5_x =  s_array + ( 0.5 * s_array_cos / np.sqrt(1+(s_array_cos**2)))
s_minus_5_x = s_array + ( - 0.5 * s_array_cos / np.sqrt(1+(s_array_cos**2)))
s_plus_5_y = s_array_sin  + (0.5 / np.sqrt(1+(s_array_cos**2)))
s_minus_5_y = s_array_sin  + (-0.5 / np.sqrt(1+(s_array_cos**2)))



#   C) write a short description of where you found the information to compete 
#       this exercise.

#the formula to calculate the offset values comes from this link : https://math.stackexchange.com/questions/1677497/parallel-curve-to-a-sine-wave



