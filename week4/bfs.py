from queue import *

def breadth_first_search(adjacency_list, starting_vertex):
	explored_nodes = Queue(maxsize=0)
	explored_nodes.put(starting_vertex)

	while not explored_nodes.empty():
		next_node = explored_nodes.get()
		for node in adjacency_list[next_node]['edges']:
			if not adjacency_list[node]['explored']:
				adjacency_list[node]['explored'] = True
				explored_nodes.put(node)


breadth_first_search(adjacency_list, 2)
