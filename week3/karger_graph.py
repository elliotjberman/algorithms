import random
import copy

adjacency_list = {}
with open('adjacency_list.txt') as f:
	for line in f:
		split_line = line.split()
		first_character = int(split_line[0])
		adjacency_list[first_character] = []
		for i in range(1, len(split_line)):
			adjacency_list[first_character].append( int(split_line[i]) )


def pick_random_node(adjacency_list):
	return random.choice(list(adjacency_list.keys()))

def merge(adjacency_list):
	choice = pick_random_node(adjacency_list)
	choice_edges = adjacency_list.pop(choice)
	staying_node = random.choice(choice_edges)
	adjacency_list[staying_node] = list(filter((choice).__ne__, adjacency_list[staying_node]))
	choice_edges = list(filter((staying_node).__ne__, choice_edges))

	for edge in choice_edges:
		adjacency_list[staying_node].append(edge)

	for node in adjacency_list:
		for edge in adjacency_list[node]:
			if edge == choice:
				adjacency_list[node] = list(filter((edge).__ne__, adjacency_list[node]))
				adjacency_list[node].append(staying_node)


def find_min_cut(adjacency_list):
	temp_list = copy.deepcopy(adjacency_list)
	while len(temp_list) > 2:
		merge(temp_list)
	keys = list(temp_list.keys())
	first = keys[0]
	result = len(temp_list[first])
	return result

results = []
for k in range(0, 100):
	results.append(find_min_cut(adjacency_list))

print(min(results))
