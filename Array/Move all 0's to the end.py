def sort0(arr, n):
	
	cnt = 0
	for i in range(n):
		if arr[i] != 0:
			arr[cnt] = arr[i]
			cnt += 1
			i += 1
	while cnt < n:
		arr[cnt] = 0
		cnt += 1
	return arr

# Driver code
arr = [1, 3, 0, 0,4, 0, 9]
# arr = [0,1,0,3,12]
n = len(arr)
a = sort0(arr, n)
print(a)