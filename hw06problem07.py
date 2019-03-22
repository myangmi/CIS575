'''
Author: Joseph Webster & Michael Yangmi
Date: 03.13.19
Class: CIS 575 | Introduction to Algorithm Analysis
Professor: Dr. Torben Amtoft
'''

# global variable to hold the total amount of swaps.
swaps = 0

# global variables for representing a heap
g_heap_list = [10000]
current_size = 0

def PercolateUp(heap_list, i):
	global swaps
	while i // 2 > 0:
		if heap_list[i] < heap_list[i // 2]:
			heap_list[i // 2], heap_list[i] = heap_list[i], heap_list[i // 2]
			swaps = swaps + 1
		i = i // 2
	return heap_list
	
def PercolateDown(heap_list, current_size, i):
	global swaps
	while (i * 2) <= current_size:
		minimum_child = MinChild(heap_list, current_size, i)
		if heap_list[i] > heap_list[minimum_child]:
			heap_list[i], heap_list[minimum_child] = heap_list[minimum_child], heap_list[i]
			swaps = swaps + 1
		i = minimum_child	
	return heap_list
		
# Find the minimum child of the heap_list.
def MinChild(heap_list, current_size, i):
		if i * 2 + 1 > current_size:
			return i * 2
		else:
			if heap_list[i * 2] < heap_list[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1
				
# Constructs a heap with a given [empty] list and a list of values.
def Heapify(heap_list, array_list):
	i = len(array_list) // 2
	current_size = len(array_list)
	heap_list = [0] + array_list[:]
	while (i > 0):
		heap_list = PercolateDown(heap_list, current_size, i)
		i = i - 1
	return heap_list
	
	
# Deletes the minimum child and changes the working set from n -> n-1 -> n-2.
def DeleteMinChild(heap_list, current_size):
	temp_value = heap_list[1]
	heap_list[1] = heap_list[current_size]
	current_size = current_size - 1
	heap_list.pop()
	heap_list = PercolateDown(heap_list, current_size, 1)
	return temp_value	
	
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
	
def Sort(g_heap_list):
	count = 0
	while count < len(g_heap_list):
		DeleteMinChild(g_heap_list, len(g_heap_list))
		count = count + 1
# n = 100
print('N = 100\n')
g_heap_list = Heapify(g_heap_list, PseudoRandom(100));
Sort(g_heap_list)
print('PseudoRandom Swaps: ' + str(swaps))
swaps = 0
g_heap_list = Heapify(g_heap_list, AlmostOrdered(100));
Sort(g_heap_list)
print('AlmostOrdered Swaps: ' + str(swaps))
swaps = 0

# n = 1000
print('N = 1000\n')
g_heap_list = Heapify(g_heap_list, PseudoRandom(1000));
Sort(g_heap_list)
print('PseudoRandom Swaps: ' + str(swaps))
swaps = 0
g_heap_list = Heapify(g_heap_list, AlmostOrdered(1000));
Sort(g_heap_list)
print('AlmostOrdered Swaps: ' + str(swaps))
swaps = 0

# n = 10000
print('N = 10000\n')
g_heap_list = Heapify(g_heap_list, PseudoRandom(10000));
Sort(g_heap_list)
print('PseudoRandom Swaps: ' + str(swaps))
swaps = 0
g_heap_list = Heapify(g_heap_list, AlmostOrdered(10000));
Sort(g_heap_list)
print('AlmostOrdered Swaps: ' + str(swaps))
swaps = 0






