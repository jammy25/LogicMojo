def countCandies(arr, n):
	if n == 0:
		return 0
	
	sum = 0
	left2right = [0] * n
	left2right[0] = 1
	right2left = [0] * n
	right2left[n - 1] = 1

	for i in range(1, n):
		if arr[i] > arr[i - 1]:
			left2right[i] = left2right[i - 1] + 1
		else:
			left2right[i] = 1
	for i in range(n - 2, 0, -1):
		if arr[i] > arr[i + 1]:
			right2left[i] = right2left[i + 1] + 1
		else:
			right2left[i] = 1
	for i in range(n):
		sum += max(left2right[i], right2left[i])
	return sum

# Driver Code
arr = [1, 5, 2, 1]
# arr = []
n = len(arr)
a = countCandies(arr, n)
print(a)