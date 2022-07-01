def findWater(arr, n):

	res = 0

	for i in range(1, n - 1):
		
		# Find max element on its Left 
		left = arr[i]
		for j in range(i):
			left = max(left, arr[j])
		# Find max element on its Right
		right = arr[i]
		for j in range(i + 1, n):
			right = max(right, arr[j])

		res = res + (min(left, right) - arr[i])

	return res

# Driver Code
arr = [[5,3,4,6,3,6],
	   [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
	   [3,2,1,4,6,5,3,1,2]]    
for array in arr:
	print(findWater(array, len(array)))