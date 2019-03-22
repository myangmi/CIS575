'''
	Author: Joseph Webster & Michael Yangmi
	Date: 03.13.19
	Class: CIS 575 | Introduction to Algorithm Analysis
	Professor: Dr. Torben Amtoft
'''

# Problem 2
# Write a program that for a given n generates a Pseudo-Random array of size n, in that index i contains (13 · i) mod n.

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
	
# get the size of n
array = PseudoRandom(int(input('Please enter an \'n\': ')))

# print the array
print(array)