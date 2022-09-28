from collections import defaultdict, deque

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)
	
	def add_edge(self, u, v):
		self.graph[u].append(v)

	def BFS(self, s):

		visited = set()
		queue = deque()
		queue.append(s)
		visited.add(s)
		while queue:
			node = queue.popleft()
			print(node, end = ' ')
			for i in self.graph[node]:
				if i not in visited:
					queue.append(i)
					visited.add(i)

# Driver Code

if __name__ == '__main__':

	 g = Graph()
	 g.add_edge(0, 1)
	 g.add_edge(0, 3)
	 g.add_edge(3, 1)
	 g.add_edge(3, 4)
	 g.add_edge(4, 2)
	 g.add_edge(2, 1)
	 g.add_edge(1, 5)
	 g.add_edge(1, 6)
	 g.BFS(0)