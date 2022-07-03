# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

def maxIndexDiff(arr, n):

	maxDiff = 0
	
	for i in range(n):
		j = n - 1
		while (j > i):
			if arr[j] > arr[i] and maxDiff < (j - i):
				maxDiff = j - i
			j -= 1

	return maxDiff

####################_Efficient_Method_#######################

# Time Complexity: O(n)
# Auxiliary Space: O(n)

def findDiff(arr, n):
	MaxDiff = 0
	leftMin = [0] * n
	rightMax = [0] * n

	leftMin[0] = arr[0]
	for i in range(1, n):
		leftMin[i] = min(arr[i], leftMin[i - 1])

	rightMax[n - 1] = arr[n - 1]
	for j in range(n - 2, -1, -1):
		rightMax[j] = max(arr[j], rightMax[j + 1])

	i, j, MaxDiff = 0, 0, -1
	while (j < n and i < n):
		if (leftMin[i] <= rightMax[j]):
			MaxDiff = max(MaxDiff, j - i)
			j = j + 1
		else:
			i = i + 1
	return  MaxDiff

# Driver Code
array = [[34, 8, 10, 3, 2, 80, 30, 33, 1],
		 [9, 10, 2, 6, 7, 12, 8, 1],
         [35, 9, 12, 3, 2, 70, 31, 33, 1],
         [1, 2, 3, 4, 5, 6],
         [9, 2, 3, 4, 5, 6, 7, 8, 18, 0],
         [6, 5, 4, 3, 2, 1]]
for arr in array:
	print(maxIndexDiff(arr, len(arr)))
	print(findDiff(arr, len(arr)))