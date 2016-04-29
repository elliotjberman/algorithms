from random import randint

def swap(array, a, b):
	array[a], array[b] = array[b], array[a]

def random_select(array, order_statistic, first, last):
	if order_statistic < 1 or order_statistic > len(array):
		print('Order statistic out of range')
		return 'Error'
	if last-first > 0:
		pivot_index = randint(first, last-1)
		pivot = array[pivot_index]
		swap(array, first, pivot_index)

		i = first + 1
		j = first + 1

		while j < last:
			if array[j] < pivot:
				swap(array, j, i)
				i+=1
			j+=1
		swap(array, i-1, first)

		if i > len(array) - order_statistic+1:
			return random_select(array, order_statistic, first, i-1)
		elif i < len(array) - order_statistic+1:
			return random_select(array, order_statistic, i, last)
		else:
			return array[i-1]
	else:
		return array[first]


stanford_array = [8, 3, 2, 5, 1, 4, 7, 6]

print(random_select(stanford_array, 2, 0, len(stanford_array)))
