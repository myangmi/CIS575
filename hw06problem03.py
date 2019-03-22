'''
    Author: Joseph Webster & Michael Yangmi
    Date: 03.13.19
    Class: CIS 575 | Introduction to Algorithm Analysis
    Professor: Dr. Torben Amtoft
'''

# Problem 3
# Write a program that for a given n generates an Almost-Ordered array of size n, in that index i contains i, except if i mod 13 = 12 in which case it contains (i + 13) mod n. 

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
		
# get the size of n
array = AlmostOrdered(int(input('Please enter an \'n\': ')))

# print the array
print(array)