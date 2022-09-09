import heapq

class Median_Finder:

	def __init__(self):
		self.max_heap = []
		self.min_heap = []

	def add_number(self, num):
		if not self.max_heap and not self.min_heap:
			heapq.heappush(self.min_heap, num)
			return
		if not self.max_heap:
			if num > self.min_heap[0]:
				heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
				heaqp.heappush(self.min_heap, num)
			else:
				heapq.heappush(self.max_heap, -num)
			return
		if len(self.max_heap) == len(self.min_heap):
			if num < -self.max_heap[0]:
				heapq.heappush(self.max_heap, -num)
			else:
				heapq.heappush(self.min_heap, num)
		elif len(self.max_heap) > len(self.min_heap):
			if num < -self.max.heap[0]:
				heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
				heapq.heappush(self.max_heap, -num)
			else:
				heapq.heappush(self.min_heap, num)
		else:
			if num > self.min_heap[0]:
				heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
				heapq.heappush(self.min_heap, num)
			else:
				heapq.heappush(self.max_heap, -num)


	def find_median(self):
		if len(self.max_heap) == len(self.min_heap):
			return(-self.max_heap[0] + self.min_heap[0]) / 2
		elif len(self.max_heap) > len(self.min_heap):
			return -self.max_heap[0]
		else:
			return self.min_heap[0]

# Driver Code

if __name__ == '__main__':

	s = Median_Finder()
	s.add_number(12)
	s.add_number(4)
	result = s.find_median()
	print(result)
	s.add_number(5)
	result = s.find_median()
	print(result)
	s.add_number(5)
	s.add_number(8)
	result = s.find_median()
	print(result)
