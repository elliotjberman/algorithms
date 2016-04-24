def mergesort(array):
	if len(array) > 1:
		middle  = len(array)//2
		a = array[:middle]
		b = array[middle:]

		mergesort(a)
		mergesort(b)

		i = 0
		j = 0
		k = 0
		while i < len(a) and j < len(b):
			if a[i] < b[j]:
				array[k] = a[i]
				i = i+1
			else:
				array[k] = b[j]
				j = j+1
			k = k+1
		while i < len(a):
			array[k] = a[i]
			i = i+1
			k = k+1
		while j < len(b):
			array[k] = b[j]
			j = j+1
			k = k+1
	return array

input_array = [5, 4, 1, 8, 7, 2, 6, 3]
print(mergesort(input_array))
