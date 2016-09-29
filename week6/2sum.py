import time
from binary_search import binary_search
from collections import deque

numbers = set()

with open('2sum_big.txt') as f:
	for line in f:
		numbers.add(int(line))
read_time = time.clock()
print(read_time)

def two_sum(input_table, low_target, high_target):
	counter = 0
	loop = 0
	for target in range(low_target, high_target+1):
		loop +=1
		if not loop % 100:
			print(time.clock())
		for number in input_table:
			complement = target - number
			if complement in input_table and complement != number:
				counter += 1
				break
	return counter

def two_sum_tricky(input_table, low_target, high_target):

	counter = 0
	loop = 0
	targets = set(range(low_target, high_target+1))
	for number in input_table:
		loop +=1
		if not loop % 10000:
			print(time.clock()-read_time)

		remove_list = []

		for target in targets:
				complement = target - number

				if complement in input_table and complement != number:
					remove_list.append(target)
					counter += 1
		for removable in remove_list:
			targets.remove(removable)
	return counter



answer = two_sum_tricky(numbers, -10000, 10000)
print(answer)
