#Test values

	# test1:            3,3,3,0,0

	# test2:            3,3,2,0,0

	# test3:            3,3,1,1,0

	# test4:            7,1,0,0,0

	# test5:            6,3,2,1,0

	# test6:            7,3,3,0,0

	# test7:            3,1,1,1,1

	# test8:            5,0,0,0,0

# Read the adjacency_list from a file
from write_adjacency_list import write_adjacency_list

adjacency_list = write_adjacency_list('SCC.txt')


def generate_reverse_list(graph):
	reverse_list = {}
	for node in graph:
		if node not in reverse_list:
			reverse_list[node] = {'explored': False, 'edges': []}
		for neighbor in graph[node]['edges']:
			if neighbor not in reverse_list:
				reverse_list[neighbor] = {'explored': False, 'edges': []}
			if node not in reverse_list[neighbor]['edges']:
				reverse_list[neighbor]['edges'].append(node)
	return reverse_list

def kosaraju(graph):
	order_list = []
	reverse_list = generate_reverse_list(graph)
	for node in reverse_list:
		reverse_count(reverse_list, node, order_list)
	finishing_times = order_list
	print(finishing_times)
	final_score = count_components(finishing_times, graph)
	return final_score


def reverse_count(graph, starting_vertex, order_list):
	starting_node = graph[starting_vertex]
	if not starting_node['explored']:
		starting_node['explored'] = True
		for node in starting_node['edges']:
			reverse_count(graph, node, order_list)
		order_list.append(starting_vertex)
	return order_list

def count_components(order, graph):
	leaderboard = [0, 0, 0, 0, 0]
	for node in reversed(order):
		counter = 0
		node_score = tracked_dfs(node, graph, counter)
		for index, score in enumerate(leaderboard):
			if node_score > score:
				leaderboard[index+1:len(leaderboard)] = leaderboard[index:len(leaderboard)-1]
				leaderboard[index] = node_score
				break
	return leaderboard


def tracked_dfs(starting_vertex, graph, counter):
	if not graph[starting_vertex]['explored']:
		graph[starting_vertex]['explored'] = True
		for neighbor in graph[starting_vertex]['edges']:
			counter = tracked_dfs(neighbor, graph, counter)
		counter += 1
		return counter
	else:
		return counter

print(kosaraju(adjacency_list))
