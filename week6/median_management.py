import heapq

numbers=[]
with open('median_big.txt') as f:
	for line in f:
		numbers.append(int(line))

def median_management(integer_list):
	medians = []
	low = []
	high = []
	heapq.heapify(low)
	heapq.heapify(high)

	for integer in integer_list:
		choose_heap(low, high, integer)
		medians.append(find_median(low, high))
	return medians


def find_median(low_heap, high_heap):
	low_size = len(low_heap)
	high_size = len(high_heap)
	difference = low_size - high_size
	if difference > -1:
		return low_heap[0]*-1
	else:
		return high_heap[0]

def choose_heap(low_heap, high_heap, value):
	if low_heap and high_heap:
		if value > low_heap[0]*-1:
			heapq.heappush(high_heap, value)
		else:
			heapq.heappush(low_heap, value*-1)
	else:
		heapq.heappush(low_heap, value*-1)
	low_size = len(low_heap)
	high_size = len(high_heap)
	difference = low_size - high_size
	if difference > 1:
		pop = heapq.heappop(low_heap)*-1
		heapq.heappush(high_heap, pop)
	if difference < -1:
		pop = heapq.heappop(high_heap)
		heapq.heappush(low_heap, pop*-1)

answer = median_management(numbers)
print("medians: " + str(answer))
sum_answer = sum(answer)
print("modulo: " + str(sum_answer % 10000))
