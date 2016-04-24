# Coming back to this later
# NOT FINISHED
def merge_sort_by_x(points):
	if len(points) > 1:
		middle = len(points) // 2
		left_half = points[:middle]
		right_half = points[middle:]

		merge_sort_by_x(left_half)
		merge_sort_by_x(right_half)

		i = 0
		j = 0
		k = 0
		while i < len(left_half) and j < len(right_half):
			if left_half[i][0] < right_half[j][0]:
				points[k] = left_half[i]
				i+=1
			else:
				points[k] = right_half[j]
				j+=1
			k+=1
		while i < len(left_half):
			points[k] = left_half[i]
			i+=1
			k+=1
		while j < len(right_half):
			points[k] = right_half[j]
			j+=1
			k+=1

def closest_pair(points):
	merge_sort_by_x(points)
	middle = len(points) // 2
	left_half = points[:middle]
	right_half = points[middle:]


test_points = [[0,2], [1,-4], [5,2], [0,0], [-2,2], [-5,2]]
closest_pair(test_points)
