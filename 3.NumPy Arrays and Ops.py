#NumPy (Numerical Python) is a Python library for fast numerical computations.
#It provides an array object that is much faster and more efficient than Python lists.
import numpy as np 

print("\n----------------------------CREATING NUMPY ARRAYS----------------------------")

# From a Python list
array1=np.array([1,2,3,4,5,6,7,8])
print("\nOriginal Array (1D): ",array1)

#initializing 2D Array
array2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("\n2D Array:\n",array2)

#initializing zero/empty Array
zero_arr=np.zeros((2,3)) #empty array with 2 rows and 3 columns
print("\nEmpty Array:\n",zero_arr)

#initializing array of 1s
ones_arr=np.ones((2,3)) #array of ones with 2 rows and 3 columns
print("\nArray of Ones:\n",ones_arr)

#initializing array of range of numbers
range_arr=np.arange(0, 11, 2) #start=0, end= till 11, jump=2
print("\nRange of Numbers: ",range_arr)

#generate 5 random numbers with range of 0-1
rand_num=np.random.rand(5) #generate 5 random
print("\nRandom Numbers between 0 and 1: ",rand_num)

#generate 5 random numbers with range of 0-10
rand_int=np.random.randint(0, 10, size=5) #start=0, end=10, size=5
print("\n5 Random Numbers between 0 and 10: ",rand_int)

#generate 3 random numbers from the lists defined.
rand_list=np.random.choice([1,2,3,4,5,6,7,8,9,10],size=3) #initialize list and define the size
print("\n3 Random numbers from a list: ",rand_list)

#generate random array of numbers with 2 rows and 3 columns, range 0-1
rand_arr=np.random.rand(2,3) 
rand_arr=rand_arr * 5 + 5 #to extend the range from 0-1 to 5-10
print("\nRandom Array of 2x3:\n",rand_arr)


print("\n----------------------------ARITHMETIC OPERATIONS----------------------------")
a=np.array([6,8,10,15,20])
b=np.array([3,4,3,5,10])

print("\nArray a: ",a)
print("Array b: ",b)
print("Addition of Array a and b: ",a+b)
print("Subtraction of Array b from a: ",a-b)
print("Multiplication of Array a with b: ",a*b)
print("Division of Array a and b: ",a/b)


print("\n----------------------------AGGREGATE FUNCTIONS----------------------------")

agg_arr=np.array([3,6,12,9,15])
print("\nOriginal array: ",agg_arr)
print("Sum: ",agg_arr.sum())
print("Min: ",agg_arr.min())
print("Max: ",agg_arr.max())
print("Mean: ",agg_arr.mean()) #average
print("Standard Deviation: ",agg_arr.std()) #measures how spread out a set of data points are from their average (mean)
print("Median: ",np.median(agg_arr)) #middle element of sorted array, not a function of numpy, so written differently

print("\n----------------------------LINEAR ALGEBRA OPERATIONS----------------------------")
matrix1=np.array([[12,5],[6,3]])
matrix2=np.array([[8,4],[7,9]])
print("\nMatrix Multiplication: \n",np.dot(matrix1,matrix2)) #number of matrix 1 must equal rows of matrix 2
print("\nTranspose of matrix 1: \n",np.transpose(matrix1)) #flip the rows into columns
print("\nDeterminant of matrix 1: ",np.linalg.det(matrix1)) #must be square matrix, a*d-b*c
print("\nInverse of matrix 1:\n",np.linalg.inv(matrix1)) #flip the diagonal entries, negative the non diagonal, then divide by determinant

print("\n----------------------------INDEXING AND SLICING----------------------------")
arr3=np.array([3,5,7,6,9])
print("\nOriginal Array: ",arr3)
print("First Index: ",arr3[0])
print("Last Index: ",arr3[-1])
print("Slicing: ",arr3[0:3])
print("Every Second Element: ",arr3[::2])
print("Reversing: ",arr3[::-1])

print("\n----------------------------EXPLORING ARRAYS----------------------------")
print("\nOriginal Array:\n",array2)
print("Shape:",array2.shape)
print("Size:",array2.size)
print("Dimention:",array2.ndim)
print("Reshaping (5,2):\n",array2.reshape(5,2)) #the number of elements should remain the same
print("Flattening Array: ",array2.flatten()) #multidimentional Array --> 1D array

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print("Array 1:",a1)
print("Array 1:",a2)
print("Stacking Array Horzontally: ",np.hstack((a1,a2))) #combining arrays Horzontally
print("Stacking Array Vertically:\n",np.vstack((a1,a2))) #combining arrays Vertically
print("Printing > 5: ",a2[a2>5])