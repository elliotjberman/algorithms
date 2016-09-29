from union_find import UnionFind
import time
import copy

numbers = set()

with open('big_bin.txt') as f:
	for line in f:
		if len(line) > 23:
			line = line.replace(" ", "")
			numbers.add(int(line, 2))

def flip_bit(binary, index):
	binary = binary ^ (1 << index)
	return binary

def generate_variations(binary_string, collection):
	counter = 0
	while counter < 24:
		new_guy = flip_bit(binary_string, counter)
		collection.add(new_guy)
		counter += 1

def generate_neighbors(binary_string):
	neighbors = set()
	generate_variations(binary_string, neighbors)
	first_pass = copy.deepcopy(neighbors)

	for neighbor in first_pass:
		generate_variations(neighbor, neighbors)

	return neighbors

def find_k(input_list):
	clusters = UnionFind()
	for number in input_list:
		if not clusters.in_union(number):
			clusters.add(number)
		neighbors = generate_neighbors(number)
		for neighbor in neighbors:
			if neighbor in numbers:
				clusters.union(number, neighbor)
	return clusters.size


print(find_k(numbers))
