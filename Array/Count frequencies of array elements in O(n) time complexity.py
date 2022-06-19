def printFrequency(arr, n):

	for i in range(n):
		arr[i] = arr[i] - 1

	for i in range(n):
		arr[arr[i] % n] = n + arr[arr[i] % n]

	for i in range(n):
		print(i + 1, "-->", arr[i] // n)

arr = [5, 1, 2, 5, 5, 5, 1, 1, 2, 2]
n = len(arr)
printFrequency(arr, n)