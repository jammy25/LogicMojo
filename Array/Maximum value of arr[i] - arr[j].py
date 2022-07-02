# Time Complexity: O(n^2)
# Auxiliary Space: O(1)

def maxIndexDiff(arr, n):

	maxDiff = -1
	
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
	maxDiff = 0
	leftMin = [0] * n
	rightMax = [0] * n

	leftMin[0] = 0
	for i in range(1, n):
		leftMin[i] = min(arr[i], leftMin[i - 1])

	rightMax[n - 1] = n - 1
	for j in range(n - 2, 0, -1):
		rightMax[j] = max(arr[j], rightMax[j + 1])

	i, j, maxDiff = 0, 0, -1
	while (j < n and i < n):
		if (leftMin <= rightMax):
			maxDiff = max(maxDiff, j - i)
			j = j + 1
		else:
			i = i + 1
	return  maxDiff

# Driver Code
arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
print(maxIndexDiff(arr, len(arr)))
print(findDiff(arr, len(arr)))