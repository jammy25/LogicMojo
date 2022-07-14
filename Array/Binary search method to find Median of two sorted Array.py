def median(arr1, arr2):
	# Assumtion arr1 and arr2 cannot be 0
	n = len(arr1)
	m = len(arr2)
	if (n > m):
		return median(arr2, arr1)

	start = 0
	end = n
	realMidinMergedArray = (n + m + 1) // 2

	while (start <= end):
		mid = (start + end) // 2
		leftArr1Size = mid
		leftArr2Size = realMidinMergedArray - mid

		# checking overflow of indices
		leftArr1 = arr1[leftArr1Size - 1] if (leftArr1Size > 0) else float("-inf")
		leftArr2 = arr2[leftArr2Size - 1] if (leftArr2Size > 0) else float('-inf')
		rightArr1 = arr1[leftArr1Size] if (leftArr1Size < n) else float('inf')
		rightArr2 = arr2[leftArr2Size] if (leftArr2Size < n) else float('inf')

		# if correct partition is done
		if leftArr1 <= rightArr2 and leftArr2 <= rightArr1:
			if ((m + n) % 2 == 0):
				return (max(leftArr1, leftArr2) + min(rightArr1, rightArr2)) / 2
			return max(leftArr1, leftArr2)

		elif (leftArr1 > rightArr2):
			end = mid - 1
		else:
			start = mid + 1

# Driver Code
# arr1 = [1, 3, 4, 7, 10, 12]
# arr2 = [2, 3, 6, 15]
arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
print(median(arr1, arr2))