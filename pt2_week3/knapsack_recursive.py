# Come back to this

import time

loaded_items = []
with open('knapsack_big.txt') as f:
	first = True
	for line in f:
		split_line = line.split()
		if first:
			knapsack_size = int(split_line[0])
		else:
			loaded_items.append((int(split_line[0]), int(split_line[1])))
		first = False
print('Finished reading input')

def knapsack(items, capacity, starting_index=0):
	weight = items[0][1]
	if capacity < 1:
		value = 0
	else:
		value = knapsack(items, capacity-weight, starting_index + 1)

	return value

result = knapsack(loaded_items, knapsack_size)
print(result)
