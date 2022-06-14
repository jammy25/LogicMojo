def findNextNumber(arr, n):
	for i in range(n - 1, 0, -1):
		if arr[i] > arr[i - 1]:
			break
		
	if i == 1 and arr[i] <= arr[i - 1]:
		print("Next number not possible")
		return

	x = arr[i - 1]
	smallest = i
	for j in range(i + 1, n):
		if arr[j]  > x and arr[j] < arr[smallest]:
			smallest = j
	arr[smallest], arr[i - 1] = arr[i - 1], arr[smallest]

	x = 0

	for j in range(i):
		x = x * 10 + arr[j]

	arr = sorted(arr[i:])

	for j in range(n - i):
		x = x * 10 + arr[j]
	print("Next number with set of digits is", x)

# Driver code
digits = "534976"
# digits = "218765"
arr = list(map(int, digits))
findNextNumber(arr, len(arr)) 