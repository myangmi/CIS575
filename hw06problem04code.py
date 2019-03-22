'''
    Author: Joseph Webster & Michael Yangmi
    Date: 03.13.19
    Class: CIS 575 | Introduction to Algorithm Analysis
    Professor: Dr. Torben Amtoft
'''

# Problem 4
# Run your Insertion Sort algorithm on 6 test sets: Pseudo-Random input and Almost Ordered input, each of size 100, of size 1,000, and of size 10,000. Report the running times (the number ofswaps).

# Here is an iterative example.
def InsertionSort(list):
	
	i = 1
	swaps = 1
	
	while i < len(list):
	
		key = list[i]
		j = i - 1
		
		while 0 <= j and key < list[j]:
		
			list[j+1] = list[j]
			swaps = swaps + 1
			j = j - 1
			
		list[j+1] = key	
		i = i + 1
	return swaps

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
pseudo_random_swaps = InsertionSort(pseudo_random_array)
almost_ordered_swaps = InsertionSort(almost_ordered_array)
print('Pseudo-Random Swaps: ' + str(pseudo_random_swaps))
print('Almost-Ordered Swaps: ' + str(almost_ordered_swaps))

pseudo_random_array = PseudoRandom(int(1000))
almost_ordered_array = AlmostOrdered(int(1000))
pseudo_random_swaps = InsertionSort(pseudo_random_array)
almost_ordered_swaps = InsertionSort(almost_ordered_array)
print('Pseudo-Random Swaps: ' + str(pseudo_random_swaps))
print('Almost-Ordered Swaps: ' + str(almost_ordered_swaps))

pseudo_random_array = PseudoRandom(int(10000))
almost_ordered_array = AlmostOrdered(int(10000))
pseudo_random_swaps = InsertionSort(pseudo_random_array)
almost_ordered_swaps = InsertionSort(almost_ordered_array)
print('Pseudo-Random Swaps: ' + str(pseudo_random_swaps))
print('Almost-Ordered Swaps: ' + str(almost_ordered_swaps))