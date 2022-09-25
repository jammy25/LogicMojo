from heapq import heappush, heappop
from collections import defaultdict

class Graph:
	def __init__(self, n):
		self.graph = defaultdict(list)
		self.n = n

	def add_edge(self, u, v, w):
		self.graph[u].append([v, w])

	def dijkstra(self, u):
		queue = [[0, u]]
		distance = [float('inf')] * (self.n + 1)
		distance[u] = 0
		visited = set()
		while queue:
			dist, u = heappop(queue)
			visited.add(u)
			for v, w in self.graph[u]:
				if distance[v] <= (dist + w) or v in visited:
					continue
				heappush(queue, [dist + w, v])
				distance[v] = dist + w
		return distance

# Driver Code

if __name__ == '__main__':

	g = Graph(6)
	g.add_edge(1, 2, 2)
	g.add_edge(2, 3, 1)
	g.add_edge(1, 3, 4)
	g.add_edge(3, 5, 3)
	g.add_edge(5, 6, 5)
	g.add_edge(5, 4, 2)
	g.add_edge(4, 6, 1)
	g.add_edge(2, 4, 7)
	g.add_edge(2, 1, 3)

	dv = g.dijkstra(1)
	print(dv[1:])