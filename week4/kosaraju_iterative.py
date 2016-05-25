#Test values

	# test1:            3,3,3,0,0

	# test2:            3,3,2,0,0

	# test3:            3,3,1,1,0

	# test4:            7,1,0,0,0

	# test5:            6,3,2,1,0

	# test6:            7,3,3,0,0

	# test7:            3,1,1,1,1

	# test8:            5,0,0,0,0

from write_adjacency_list import write_adjacency_list
import collections
import time

adjacency_list = write_adjacency_list('SCC.txt')

def generate_reverse_list(graph):
	reverse_list = {}
	for node in graph:
		if node not in reverse_list:
			reverse_list[node] = {'explored': False, 'edges': [], 'added_to_list': False}
		for neighbor in graph[node]['edges']:
			if neighbor not in reverse_list:
				reverse_list[neighbor] = {'explored': False, 'edges': [], 'added_to_list': False}
			if node not in reverse_list[neighbor]['edges']:
				reverse_list[neighbor]['edges'].append(node)
	print(time.clock())
	print("finished reversing list")
	return reverse_list

def kosaraju(graph):
	reverse_list = generate_reverse_list(graph)
	finishing_times = reverse_count(reverse_list)
	print(time.clock())
	print("finished first DFS")
	final_score = count_components(finishing_times, graph)
	print(time.clock())
	return final_score


def reverse_count(graph):
	order_list = collections.deque()
	for starting_node in graph:
		explored_nodes = collections.deque()
		explored_nodes.append(starting_node)
		while len(explored_nodes):
			next_node = explored_nodes.pop()
			if not graph[next_node]['explored']:
				graph[next_node]['explored'] = True
				explored_nodes.append(next_node)
				for node in graph[next_node]['edges']:
					if not graph[node]['explored']:
						# graph[node]['explored'] = True
						explored_nodes.append(node)
			else:
				if not graph[next_node]['added_to_list']:
					order_list.append(next_node)
					graph[next_node]['added_to_list'] = True
	return order_list

def count_components(order, graph):
	leaderboard = [0, 0, 0, 0, 0]
	for node in reversed(order):
		node_score = tracked_dfs(node, graph)
		for index, score in enumerate(leaderboard):
			if node_score > score:
				leaderboard[index+1:len(leaderboard)] = leaderboard[index:len(leaderboard)-1]
				leaderboard[index] = node_score
				break
	return leaderboard


def tracked_dfs(starting_node, graph):
	explored_nodes = collections.deque()
	counter = 0
	if not adjacency_list[starting_node]['explored']:
		adjacency_list[starting_node]['explored'] = True
		explored_nodes.append(starting_node)
		counter += 1

		while len(explored_nodes):
			next_node = explored_nodes.pop()
			for node in adjacency_list[next_node]['edges']:
				if not adjacency_list[node]['explored']:
					adjacency_list[node]['explored'] = True
					explored_nodes.append(node)
					counter += 1

	return counter

print(kosaraju(adjacency_list))
