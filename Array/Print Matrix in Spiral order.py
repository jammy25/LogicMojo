def spiralOrder(rowend, columnend, arr):

	rowbegin = columnbegin = 0

	while rowbegin < rowend and columnbegin < columnend:
		for i in range(columnbegin, columnend):
			print(arr[rowbegin][i], end = " ")
		rowbegin += 1

		for i in range(rowbegin, rowend):
			print(arr[i][columnend - 1], end = " ")
		columnend -= 1

		# if rowbegin < rowend:
		if rowend > rowbegin:
			for i in range(columnend - 1, columnbegin - 1, -1):
				print(arr[rowend - 1][i], end = " ")
			rowend -= 1

		if columnbegin < columnend:
		# if columnend > columnbegin:
			for i in range(rowend - 1, rowbegin - 1, -1):
				print(arr[i][columnbegin], end = " ")
			columnbegin += 1

# Driver Code
arr =[[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
rowend = 4
columnend = 4
# Function Call
spiralOrder(rowend, columnend, arr)