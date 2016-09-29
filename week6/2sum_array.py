import time
from binary_search import binary_search

numbers = set()

with open('2sum_test2.txt') as f:
	for line in f:
		numbers.add(int(line))
def two_sum_array(input_table, low_target, high_target):
	positive_index = 0
	sorted_array = sorted(list(input_table))

	counter = 0
	loop = 0
	for target in range(low_target, high_target+1):
		loop+=1
		print(loop)
		index = binary_search(sorted_array, target)
		if index == 0:
			index = len(sorted_array)-1
		while index > -1:
			number = sorted_array[index]
			complement = target - number
			if complement in input_table and complement != number:
				counter += 1
				break
			index -=1
	print(time.clock())
	return counter
