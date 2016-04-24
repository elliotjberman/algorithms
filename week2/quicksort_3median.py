import statistics
import random
from random import randint

global count
count = 0

def swap(array, a, b):
	array[a], array[b] = array[b], array[a]

def find_median(array, first, last):
	length = len(array[first:last])
	middle = round(length / 2) - 1
	middle += first

	choices = []
	choices.append(array[first])
	choices.append(array[middle])
	choices.append(array[last-1])

	print(array[first:last])
	print(choices)

	choices.sort()
	median = choices[1]

	print(median)
	print()

	if median == array[first]:
		return first
	elif median == array[last-1]:
		return last-1
	else:
		return middle

def quicksort(array, first, last):
	if last-first > 1:
		global count
		count = count + last - first - 1
		pivot_index = find_median(array, first, last)
		pivot = array[pivot_index]
		swap(array, first, pivot_index)
		i = first+1
		j = first+1
		while j < last:
			if array[j] < pivot:
				swap(array, j, i)
				i+=1
			j+=1
		swap(array, i-1, first)

		if i < last:
			quicksort(array, first, i-1)
			quicksort(array, i, last)

	return array

#Non-sorted integers
content = []
with open('100.txt') as f:
	for line in f:
		content.append(int(line))

print(quicksort(content, 0, len(content)))
print(count)
