def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[l] > arr[largest]:
		largest = l
	if r < n and arr[r] > arr[largest]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)

def buildHeap(arr, n):
	startIdx = n // 2 - 1
	for i in range (startIdx, -1, -1):
		heapify(arr, n, i)

def printHeap(arr, n):
	print("array representation of heap: ")
	for i in range(n):
		print(arr[i], end = ' ')
	print()
 
# Driver Code

if __name__ == '__main__':

	arr = [3, 5, 9, 6, 8, 20, 10, 12, 19, 18, 2]
	n = len(arr)

	buildHeap(arr, n)
	printHeap(arr, n)