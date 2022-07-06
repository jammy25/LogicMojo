# Time Complexity = O(n^2)
# Space Complexity = O(1)

def getInvCount(arr, n):
	inverse_count = 0
	for i in range(n):
		for j in range(i + 1, n):
			if (arr[i] > arr[j]):
				inverse_count += 1

	return inverse_count

############### Efficient Method ###################

# Time Complexity = O(nlogn)
# Space Complexity = O(n)

def mergeSort(arr, n):
	temp = [0] * n
	return _mergeSort(arr, temp, 0, n - 1)

def _mergeSort(arr, temp, left, right):
	inv_count = 0

	if (right > left):

		mid = (right + left) // 2

		inv_count += _mergeSort(arr, temp, left, mid)
		inv_count += _mergeSort(arr, temp, mid + 1, right)
		
		inv_count += merge(arr, temp, left, mid, right)

	return inv_count

def merge(arr, temp, left, mid, right):
	i, j, k = left, mid + 1, left
	inv_count = 0

	while i <= mid and j <= right:

		if arr[i] <= arr[j]:
			temp[k] = arr[i]
			k += 1
			i += 1
		else:
			temp[k] = arr[j]
			inv_count += (mid - i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp[k] = arr[j]
		k += 1
		j += 1

	for loop_var in range(left, right + 1):
		arr[loop_var] = temp[loop_var]

	return inv_count



# Driver Code
array = [[1, 20, 6, 4, 5],
	   [-1, 6, 3, 4, 7, 4],
	   [8, 4, 2, 1],
	   [5, 3, 2, 4, 1],
	   [9, 1, 6, 4, 5]]
for arr in array:
	print(getInvCount(arr, len(arr)))
	print(mergeSort(arr, len(arr)))