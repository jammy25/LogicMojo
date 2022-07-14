def median(arr1, arr2, k):
	n = len(arr1)
	m = len(arr2)

	if n > m:
		return median(arr2, arr1, k)

	low = max(0, k - m)
	high = min(k, n)

	while low <= high:
		mid = (low + high) // 2
		leftArr1Size = mid
		leftArr2Size = k - leftArr1Size

		leftArr1 = arr1[leftArr1Size - 1] if (leftArr1Size > 0) else float('-inf')
		leftArr2 = arr2[leftArr2Size - 1] if (leftArr2Size > 0) else float('-inf')
		rightArr1 = arr1[leftArr1Size] if (leftArr1Size < n) else float('inf')
		rightArr2 = arr2[leftArr2Size] if (leftArr2Size < n) else float('inf')

		if leftArr1 <= rightArr2 and leftArr2 <= rightArr1:
			return max(leftArr1, leftArr2)
		elif (leftArr1 > rightArr2):
			high = mid - 1
		else:
			low = mid + 1

# Driver Code
arr1 = [ 2, 3, 6, 7, 9 ]
arr2 = [ 1, 4, 8, 10 ]
k = 5
# arr1 = [100, 112, 256, 349, 770]
# arr2 = [72, 86, 113, 119, 265, 445, 892]
# k = 7
print(median(arr1, arr2, k))