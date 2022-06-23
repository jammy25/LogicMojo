def matrixRotation(mat):
	for x in range(int (N/2)):
		for y in range(x, N - x - 1):

			temp = mat[y][N - x - 1]

			mat[y][N - x - 1] = mat[x][y]

			mat[x][y] = mat[N - y - 1][x]

			mat[N - y - 1][x] = 		mat[N - x - 1][N - y - 1]

			mat[N - x - 1][N - y - 1] = temp

			# temp = mat[x][y]
			
			# mat[x][y] = mat[y][N - 1 - x]
			
			# mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]
			
			# mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]

			# mat[N - 1 - y][x] = temp

def displayMatrix(mat):
	for i in range(0, N):
		for j in range(0, N):
			print(mat[i][j], end = " ")
		print("")

# Driver Code
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
N = len(mat[0])
matrixRotation(mat)
displayMatrix(mat)