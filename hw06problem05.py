'''
Author: Joseph Webster & Michael Yangmi
Date: 03.13.19
Class: CIS 575 | Introduction to Algorithm Analysis
Professor: Dr. Torben Amtoft
'''
# Problem 5
# Write a program that implements the HeapSort algorithm. 
# Recall that the first step is to convert the array into a heap, as done by the pseudo-code
#	for i <- n downto 1
#		SIFT(i)
# Where SIFT is defined on the lecture slides (Max-Heapify). 

# global variable to keep track of swaps.
swaps = 0

# this function was inspired by: https://www.geeksforgeeks.org/heap-sort/
def Heapify(array, n, i): 
	global swaps
	largest = i # Initialize largest as root 
	left_child = 2 * i + 1
	right_child = 2 * i + 2

	# See if left child of root exists and is greater than root 
	if left_child < n and array[i] < array[left_child]: 
		largest = left_child 

	# See if right child of root exists and is greater than root 
	if right_child < n and array[largest] < array[right_child]: 
		largest = right_child

	# Check if the largest index is not i
	if largest != i: 
		array[i], array[largest] = array[largest], array[i] 
		swaps = swaps + 1 
		Heapify(array, n, largest) 

# The main function to sort an array 
# this function was inspired by: https://www.geeksforgeeks.org/heap-sort/
def HeapSort(array): 
	global swaps
	n = len(array) 
	
	# Construct a heap. 
	for i in range(n, -1, -1): 
		Heapify(array, n, i) 

	# remove the elements after being sorted, one-by-one 
	for i in range(n-1, 0, -1): 
		array[i], array[0] = array[0], array[i] # swap
		swaps = swaps + 1
		Heapify(array, i, 0) 

# Generate an array of 'pseudo-random' values with a size 'n'.
def PseudoRandom(n):
	# create a list of all 1's of size 'n'; the initial values do not matter as they will be overwritten.
	array = [1] * n
	
	# initialize a counter.
	i = 0

	# loop from 0, 1, 2, ..., n and fill the arrays with pseudo-random values.
	while (i < n):
		array[i] = (13 * i) % n
		i = i + 1
	return array

# Produces an almost ordered array of given length 'n'.
def AlmostOrdered(n):
	# initialize the array with no values 
	array = [None] * n

	# initialize a counter.
	i = 0

	# loop from 0, 1, 2, ..., n and fill the arrays with almost ordered values.
	while (i < n):
		if i % 13 == 12:
			array[i] = (i + 13) % n
		else:
			array[i] = i
		i = i + 1
	return array

# 'n' should equal, 100, then 1000, then 10,000
pseudo_random_array = PseudoRandom(int(100))
almost_ordered_array = AlmostOrdered(int(100))
HeapSort(pseudo_random_array)
print('Pseudo-Random Swaps: ' + str(swaps))
swaps = 0
HeapSort(almost_ordered_array)
print('Almost-Ordered Swaps: ' + str(swaps))
swaps = 0

pseudo_random_array = PseudoRandom(int(1000))
almost_ordered_array = AlmostOrdered(int(1000))
HeapSort(pseudo_random_array)
print('Pseudo-Random Swaps: ' + str(swaps))
swaps = 0
HeapSort(almost_ordered_array)
print('Almost-Ordered Swaps: ' + str(swaps))
swaps = 0

pseudo_random_array = PseudoRandom(int(10000))
almost_ordered_array = AlmostOrdered(int(10000))
HeapSort(pseudo_random_array)
print('Pseudo-Random Swaps: ' + str(swaps))
swaps = 0
HeapSort(almost_ordered_array)
print('Almost-Ordered Swaps: ' + str(swaps))
swaps = 0
