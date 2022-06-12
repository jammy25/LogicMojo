# Time complexity -> O(n), Space complexity -> O(1)

# Function to sort array
def sort012(arr, arr_size):
	lo = 0
	mid = 0
	hi = arr_size - 1

	while mid <= hi:
		if arr[mid] == 0:
			arr[lo], arr[mid] = arr[mid], arr[lo]
			lo = lo + 1
			mid = mid + 1
		elif arr[mid] == 1:
			mid = mid + 1
		else:
			arr[hi], arr[mid] = arr[mid], arr[hi]
			hi = hi - 1
	return arr

# Driver code
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
a = sort012(arr, arr_size)
print(a)