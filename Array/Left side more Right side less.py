def findElement(arr, n):
	
	leftMax = [None] * n
	leftMax[0] = arr[0]

	for i in range(1, n):
		leftMax[i] = max(leftMax[i - 1], arr[i - 1])

	rightMin = [None] * n
	rightMin[n - 1] = arr[n - 1]

	for i in range(n - 2, -1, -1):
		rightMin[i] = min(rightMin[i + 1], arr[i])

	for i in range(1, n - 1):
		if leftMax[i - 1] <= arr[i] <= rightMin[i + 1]:
			return i

	return -1

# Driver Code
arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
# arr = [6, 2, 5, 4, 7, 9, 11, 8, 10]
# arr = [5, 1, 4, 4]
n = len(arr)
a = findElement(arr, n)
print(a)