from collections import defaultdict

class Graph:

	def __init__(self, directed = False):
		self.directed = directed
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)
		if self.directed is False:
			self.graph[v].append(u)
		else:
			self.graph[v] = self.graph[v]
	def topoSortVisit(self, s, visited, sortlist):
		visited[s] = True
		for i in self.graph[s]:
			if not visited[i]:
				self.topoSortVisit(i, visited, sortlist)
		sortlist.insert(0, s)
	def topoSort(self):
		visited = {i: False for i in self.graph}
		sortlist = []
		for v in self.graph:
			if not visited[v]:
				self.topoSortVisit(v, visited, sortlist)
		print(sortlist)

# Driver Code

if __name__ == '__main__':

	g = Graph(directed = True)
	g.add_edge(1, 2)
	g.add_edge(1, 3)
	g.add_edge(2, 4)
	g.add_edge(2, 5)
	g.add_edge(3, 4)
	g.add_edge(3, 6)
	g.add_edge(4, 6)

	print("Topological Sort:")
	g.topoSort()