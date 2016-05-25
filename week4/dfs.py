# Read the adjacency_list from a file
adjacency_list = {}
with open('8_nodes.txt') as f:
	for line in f:
		split_line = line.split()
		first_character = int(split_line[0])

		adjacency_list[first_character] = {'explored': False, 'edges': []}

		for i in range(1, len(split_line)):
			adjacency_list[first_character]['edges'].append( int(split_line[i]) )

def depth_first_search(adjacency_list, starting_vertex):
	starting_node = adjacency_list[starting_vertex]
	starting_node['explored'] = True
	for node in starting_node['edges']:
		if not adjacency_list[node]['explored']:
			depth_first_search(adjacency_list, node)
