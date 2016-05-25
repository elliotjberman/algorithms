def write_adjacency_list(filepath):
	adjacency_list = {}
	with open(filepath) as f:
		for line in f:
			split_line = line.split()
			first_character = int(split_line[0])
			second_character = int(split_line[1])
			if first_character not in adjacency_list:
				adjacency_list[first_character] = {'explored': False, 'edges': []}
			if second_character not in adjacency_list:
				adjacency_list[second_character] = {'explored': False, 'edges': []}
			adjacency_list[first_character]['edges'].append( second_character )
	print("finished reading file")
	return adjacency_list
