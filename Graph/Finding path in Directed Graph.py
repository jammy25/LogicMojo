from collections import defaultdict

class Graph:
	def __init__(self, n):
		self.graph = defaultdict(list)
		self.n = n

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def dfs(self, src, dest, path, visited, paths):
		if src == dest:
			paths.append(path[:])
			return
		for node in self.graph[src]:
			if node in visited:
				continue
			visited.add(node)
			self.dfs(node, dest, path + [node], visited, paths)
			visited.remove(node)

	def find_all_paths(self, src, dest):
		paths = []
		visited = set()
		visited.add(src)
		self.dfs(src, dest, [src], visited, paths)
		return paths

# Driver Code

if __name__ == '__main__':

	g = Graph(4)
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(0, 3)
	g.add_edge(2, 0)
	g.add_edge(2, 1)
	g.add_edge(1, 3)

	# TC 01
	print(g.find_all_paths(2, 3))
	# TC 02
	print(g.find_all_paths(0, 3))