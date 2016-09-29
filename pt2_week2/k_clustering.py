from union_find import UnionFind
from queue import PriorityQueue

graph = {}

with open('clustering1.txt') as f:
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
			# graph[neighbor][node] = cost

def k_cluster(k, input_graph):
	clusters = UnionFind()
	edges = []
	for node in input_graph.keys():
		clusters.add(node)
		for neighbor, weight in input_graph[node].items():
			edges.append((weight, (node, neighbor)))
	edges.sort(key=lambda x: x[0])
	index = 0
	while clusters.size > 4:
		next_edge = edges[index]
		nodes = next_edge[1]
		clusters.union(nodes[0], nodes[1])
		index += 1

	index = 0
	while index < len(edges):
		next_edge = edges[index]
		nodes = next_edge[1]
		if clusters[nodes[0]] != clusters[nodes[1]]:
			return next_edge[0]
		index += 1

print(k_cluster(4, graph))
