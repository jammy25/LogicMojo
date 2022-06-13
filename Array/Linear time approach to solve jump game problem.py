def jump(arr, n):
	if n <= 1:
		return 0
	if arr[0] == 0:
		return -1

	a = arr[0]
	b = arr[0]
	jump = 1
	for i in range(1, n):
		if i == n - 1:
			return jump
		b -= 1
		a -= 1
		if arr[i] > b:
			b = arr[i]
		if a == 0:
			jump += 1
			a = b
		if b == 0:
			return -1
	return jump

# Driver code
# arr = [2, 3, 1, 1, 4]
arr = [3,2,1,0,4]
n = len(arr)
x = jump(arr, n)
print(x)