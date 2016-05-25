from write_adjacency_list import write_adjacency_list

adjacency_list = write_adjacency_list('test1.txt')

def iterative_depth_first_search(graph):
	explored_nodes = []
	for starting_vertex in graph:
		if not adjacency_list[starting_vertex]['explored']:
			adjacency_list[starting_vertex]['explored'] = True
			explored_nodes.append(starting_vertex)

			while len(explored_nodes):
				next_node = explored_nodes.pop()
				for node in adjacency_list[next_node]['edges']:
					if not adjacency_list[node]['explored']:
						adjacency_list[node]['explored'] = True
						explored_nodes.append(node)

iterative_depth_first_search(adjacency_list)
