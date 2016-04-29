import math

def swap(array, a, b):
	array[a], array[b] = array[b], array[a]

def middle_index(array):
	length = len(array)
	middle = math.ceil(length / 2) - 1
	return middle

def median_of_medians(array, first, last):
	medians = []
	counter = first
	list_of_scrim = []
	while counter < last:
		if counter + 4 < last:
			list_of_scrim.append(array[counter:counter+5])
		else:
			list_of_scrim.append(array[counter:last])
		list_of_scrim[-1].sort()
		counter += 5
	for sub_array in list_of_scrim:
		middle = middle_index(sub_array)
		median = sub_array[middle]
		medians.append(median)
	medians.sort()
	big_middle = middle_index(medians)
	return medians[big_middle]

def deterministic_selection(array, order_statistic, first, last):
	if not order_statistic in range(1, len(array)):
		print('Order statistic out of range')
		return 'Error'
	if last-first > 0:
		big_median = median_of_medians(array, first, last)
		pivot_index = array.index(big_median)
		pivot = pivot_index
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
			return deterministic_selection(array, order_statistic, first, i-1)
		elif i < len(array) - order_statistic+1:
			return deterministic_selection(array, order_statistic, i, last)
		else:
			return array[i-1]
	else:
		return array[first]


stanford_array = [8, 3, 2, 5, 1, 4, 7, 6]

print(deterministic_selection(stanford_array, 2, 0, len(stanford_array)))
