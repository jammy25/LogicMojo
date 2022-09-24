from collections import deque

def largest_region(matrix):
	X = [-1, -1, -1, 0, 1, 0, 1, 1]
	Y = [-1, 1, 0, -1, -1, 1, 0, 1]
	def BFS(i, j):
		queue = deque([[i, j]])
		visited.add((i, j))
		region = 0
		while queue:
			i, j = queue.popleft()
			region += 1

			for k in range(8):
				x, y = i + X[k], j + Y[k]
				if 0 <= x < m and 0 <= y < n and matrix[x][y]:
					if (x, y) in visited:
						continue
					queue.append([x, y])
					visited.add((x, y))
		return region

	m, n = len(mat), len(mat[0])
	visited = set()
	max_region = 0
	for i in range(m):
		for j in range(n):
			if matrix[i][j] and (i, j) not in visited:
				max_region = max(max_region, BFS(i, j))
	return max_region

# Driver Code

if __name__ == '__main__':

	mat = [[0, 0, 1, 1, 0],
		   [1, 0, 1, 1, 0],
		   [0, 1, 0, 0, 0],
		   [0, 0, 0, 0, 1],
		   [0, 0, 1, 1, 0]]

	print(largest_region(mat))