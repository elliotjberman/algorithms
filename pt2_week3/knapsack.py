loaded_items = []
with open('knapsack1.txt') as f:
	first = True
	for line in f:
		split_line = line.split()
		if first:
			knapsack_size = int(split_line[0])
		else:
			loaded_items.append((int(split_line[0]), int(split_line[1])))
		first = False


def knapsack(items, capacity):
	scores = [[0] * (capacity+1)]
	counter = 1
	for item in items:
		scores.append([0] * (capacity+1))
		testing_weight = 0

		while testing_weight <= capacity:
			previous = scores[counter-1][testing_weight]
			if item[1] > testing_weight:
				scores[counter][testing_weight] = previous
			else:
				remaining_weight = testing_weight - item[1]
				candidate = scores[counter-1][remaining_weight] + item[0]
				scores[counter][testing_weight] = max(candidate, previous)
			testing_weight += 1

		counter += 1

	return scores

results = knapsack(loaded_items, knapsack_size)

print(results[len(loaded_items)][knapsack_size])
