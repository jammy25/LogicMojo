from  collections import defaultdict

class Graph:
	def __init__(self, n):
		self.graph = defaultdict(list)
		self.n = n

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def dfs(self, u, visited):
		visited.add(u)
		for v in self.graph[u]:
			if v not in visited:
				self.dfs(v, visited)

	def is_strongly_connected(self):
		for node in range(self.n):
			visited = set()
			self.dfs(node, visited)
			if len(visited) < self.n:
				return False
		return True

# Driver Code

if __name__ == '__main__':

	# TC: 1
	# g = Graph(5)
	# g.add_edge(0, 1)
	# g.add_edge(1, 2)
	# g.add_edge(2, 3)
	# g.add_edge(3, 0)
	# g.add_edge(2, 4)
	# g.add_edge(4, 2)

	# TC: 2
	g = Graph(4)
	g.add_edge(0, 1)
	g.add_edge(1, 2)
	g.add_edge(2, 3)
	print(g.is_strongly_connected())
