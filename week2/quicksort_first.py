import random
from random import randint

global count
count = 0

def swap(array, a, b):
	array[a], array[b] = array[b], array[a]

def quicksort(array, first, last):
	if last-first > 1:
		global count
		count = count + last - first - 1
		pivot_index = first
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

		if i < last+1:
			quicksort(array, first, i-1)
			quicksort(array, i, last)

	return array

#Running the function with arrays
stanford_array = [8, 3, 2, 5, 1, 4, 7, 6]
already_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#100,000 non-sorted integers
content = []
with open('ShouldBe615.txt') as f:
	for line in f:
		content.append(int(line))

print(quicksort(content, 0, len(content)))
print(count)
