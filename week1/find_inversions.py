global count
count = 0

content = []
with open('new_integer_array.txt') as f:
	for line in f:
		content.append(int(line))

def count_inversions(array):
	if len(array) > 1:
		middle  = len(array)//2
		a = array[:middle]
		b = array[middle:]

		count_inversions(a)
		count_inversions(b)

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
				global count
				count = count + len(a)-i
			k = k+1
		while i < len(a):
			array[k] = a[i]
			i = i+1
			k = k+1
		while j < len(b):
			array[k] = b[j]
			j = j+1
			k = k+1

count_inversions(content)
print(count)
