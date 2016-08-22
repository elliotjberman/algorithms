import math
import heapq

graph = {}
with open('big_graph.txt') as f:
	for line in f:
		split_line = line.split()
		node_id = int(split_line[0])
		edges = split_line[1:]
		node_neighbors = {}
		for edge in edges:
			edge_split = edge.split(',')
			neighbor = int(edge_split[0])
			node_neighbors[neighbor] = int(edge_split[1])
			if neighbor not in graph:
				graph[neighbor] = {}
		graph[node_id] = node_neighbors

def dijkstra_shortest_path(graph, starting_node, end):
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

		for neighbor, length in graph[current_node].items():
			tentative_length = length + processed_nodes[current_node]
			if neighbor not in processed_nodes:
				heapq.heappush(unvisited, (tentative_length, neighbor))

	return processed_nodes

results = dijkstra_shortest_path(graph, 1, 8)
for key, value in results.items():
	if key in (7,37,59,82,99,115,133,165,188,197):
		print(str(key) + ': ' + str(value))
