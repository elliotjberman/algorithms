import math

def binary_search(array, value, offset=0):
	if len(array) > 1:
		middle = math.ceil((len(array)-1)/2)
		test = array[middle]
		if test == value:
			return middle + offset
		elif test < value:
			return binary_search(array[middle:], value, middle+offset)
		else:
			return binary_search(array[:middle], value, offset)

	return offset
