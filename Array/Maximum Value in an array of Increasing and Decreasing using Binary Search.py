def max(arr, start, end):
	if start == end:
		return arr[start]
	if end == start + 1:
		if arr[start] > arr[end]:
			return arr[start]
		else:
			return arr[end]
	
	mid = (start + end)//2

	if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
		return arr[mid]
	if arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
		return max(arr, mid + 1, end)
	if arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
		# return arr[start]
		return max(arr, start, mid - 1)

arr = [3, 5,15, 50, 11, 10, 8, 6]
# start = 0
n = len(arr)
a = max(arr, 0, n - 1)
print("The maximum element is:", a)