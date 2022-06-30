def find2Element(arr, n):
	
	xor = arr[0]

	for i in range(1, n):
		xor ^= arr[i]

	most_rightBit = xor & ~(xor - 1)

	a = 0
	b = 0
	for i in range(n):
		x = arr[i]
		if (most_rightBit & x) != 0:
			a ^= x
		else:
			b ^= x
	return a, b

#Driver Code
array = [[4,5,4,5,3,2,9,3,9,8],
	     [2, 4, 7, 9, 2, 4],
	     [5, 4, 1, 4, 3, 5, 1, 2],
	     [1,1,2,2,3,3,4,5,5,6,7,7]]
for arr in array:
	print(find2Element(arr, len(arr)))
