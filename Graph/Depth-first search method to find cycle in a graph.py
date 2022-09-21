from collections import defaultdict

class Graph:
	def __init__(self, n):
		self.n = n
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def dfs(self, u, parent, visited):
		visited.add(u)
		for v in self.graph[u]:
			if v == parent:
				continue
			if v in visited:
				return True
			if self.dfs(v, u, visited):
				return True
		return False

	def is_Cyclic(self):
		visited = set()
		for u in self.graph:
			if u in visited:
				continue
			if self.dfs(u, None, visited):
				return True
		return False

# Driver Code

if __name__ == '__main__':
	# TC: 1
	g = Graph(5)
	g.add_edge(1, 0)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(0, 3)
	g.add_edge(3, 4)

	if g.is_Cyclic():
		print("Graph contains cycle")
	else:
		print("Graph does not contain cycle")

	# TC: 2
	g1 = Graph(3)
	g1.add_edge(0, 1)
	g1.add_edge(1, 2)

	if g1.is_Cyclic():
		print("Graph contains cycle")
	else:
		print("Graph does not contain cycle")