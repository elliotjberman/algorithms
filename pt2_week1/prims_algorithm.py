graph = {}
import heapq
import math

with open('edges.txt') as f:
	for line in f:
		split_line = line.split()
		if len(split_line) > 2:
			node = int(split_line[0])
			neighbor = int(split_line[1])
			cost = int(split_line[2])
			if node not in graph:
				graph[node] = {}
			if neighbor not in graph:
				graph[neighbor] = {}
			graph[node][neighbor] = cost
			graph[neighbor][node] = cost

print(graph)
def prims(input_graph):
	visited = set()
	total_cost = 0
	unvisited = [] # heap
	heapq.heappush(unvisited, (0, 1))

	while len(visited) < len(graph):
		item = heapq.heappop(unvisited)
		cost = item[0]
		node = item[1]
		if node not in visited:
			visited.add(node)
			total_cost += cost
			for neighbor, cost in graph[node].items():
				heapq.heappush(unvisited, (cost, neighbor))

	return total_cost

print("total cost: " + str(prims(graph)))
