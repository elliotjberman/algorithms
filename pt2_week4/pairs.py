import math
import heapq

graph = {0: {}}

with open('g3.txt') as f:
	first = True
	for line in f:
		if not first:
			split_line = line.split()
			node_id = int(split_line[0])
			neighbor = int(split_line[1])
			edge_weight = int(split_line[2])
			if node_id not in graph:
				graph[node_id] = {}
				graph[0][node_id] = 0
			if neighbor not in graph:
				graph[neighbor] = {}
				graph[0][neighbor] = 0
			graph[node_id][neighbor] = edge_weight
		first = False

print("File read")

def bellman_ford(input_graph):
	distances = [math.inf] * len(input_graph)
	for node in input_graph:
		distances[node] = math.inf
	distances[0] = 0

	n = 0
	while n < len(input_graph):
		changed = False
		for node in input_graph:
			for neighbor, edge in input_graph[node].items():
				if distances[neighbor] > distances[node] + edge:
					distances[neighbor] = distances[node] + edge
					changed = True
		if changed == False:
			break
		n += 1

	for node in input_graph:
		for neighbor, edge in input_graph[node].items():
			if distances[neighbor] > distances[node] + edge:
				raise ValueError("Negative cycle in graph")

	return distances

def reweight(input_graph, bf_distances):
	del input_graph[0]
	for node in input_graph:
		for neighbor, edge in input_graph[node].items():
			input_graph[node][neighbor] = input_graph[node][neighbor] + bf_distances[node] - bf_distances[neighbor]
	return input_graph


def dijkstra_shortest_path(graph, starting_node, end, meta_processed):
	processed_nodes = {}
	unvisited = [] # heap

	for node in graph:
		if node != starting_node:
			heapq.heappush(unvisited, (math.inf, node))
		else:
			heapq.heappush(unvisited, (0, node))

	while len(processed_nodes) < len(graph):
		current_length, current_node = heapq.heappop(unvisited)
		while current_node in processed_nodes:
			current_length, current_node = heapq.heappop(unvisited)
		processed_nodes[current_node] = current_length
		meta_processed[current_node] = current_length

		for neighbor, length in graph[current_node].items():
			tentative_length = length + processed_nodes[current_node]
			if neighbor not in processed_nodes:
				heapq.heappush(unvisited, (tentative_length, neighbor))

	return processed_nodes[end]

def find_shortest_pairs(input_graph):
	distances = bellman_ford(input_graph)
	print("Bellman-Ford computed")
	updated_graph = reweight(input_graph, distances)
	print("Graph reweighted")

	shortest_path = 0

	for source in updated_graph:
		paths = {}
		for destination in updated_graph:
			if source != destination:
				if destination not in paths:
					test_value = dijkstra_shortest_path(updated_graph, source, destination, paths) - distances[source] + distances[destination]
				else:
					test_value = paths[destination] - distances[source] + distances[destination]
				shortest_path = min(shortest_path, test_value)

	return shortest_path

results = find_shortest_pairs(graph)
print(results)
