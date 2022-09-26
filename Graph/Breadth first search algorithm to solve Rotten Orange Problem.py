from collections import deque

def rotten_oranges(matrix):
	X = [-1, 0, 0, 1]
	Y = [0, -1, 1, 0]
	m, n = len(matrix), len(matrix[0])
	queue = deque()

	time = ones = 0
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 2:
				queue.append([i, j, time])
			elif matrix[i][j] == 1:
				ones += 1

	while queue:
		i, j, time = queue.popleft()
		for k in range(4):
			x, y = i + X[k], j + Y[k]
			if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1:
				matrix[x][y] = 2
				ones -= 1
				queue.append([x, y, time + 1])

	if ones:
		return -1
	return time

# Driver Code

if __name__ == '__main__':

	tc = [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]]

	for matrix in tc:
		print(rotten_oranges(matrix))