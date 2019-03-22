'''
	Author: Joseph Webster & Michael Yangmi
	Date: 03.13.19
	Class: CIS 575 | Introduction to Algorithm Analysis
	Professor: Dr. Torben Amtoft
'''

# Problem 1
# Write a program that implements the Insertion Algorithm.

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
	return list, swaps

# Test Values
test_list = [54, 12, 42, 24, 38, 9, 15, 2, 4] 

# Print Test Values Pre-Sort
print('\nPre-Sorted Array:')
for i in range(len(test_list)): 
    print(f'Location: {i} \nValue: {test_list[i]}\n')
	
# Call InsertionSort
test_list, swaps = InsertionSort(test_list)
	
# Print Test Values Post-Sort
print('\nPost-Sorted Array:')
for i in range(len(test_list)): 
    print(f'Location: {i} \nValue: {test_list[i]}\n')
	
# Print the number of swaps
print('Number of swaps: ' + str(swaps))