def add_node(v):
	if v in graph:
		print(v, "node present in graph")
	else:
		graph[v] = []
def add_edge(v1, v2, e):
	if v1 not in graph:
		print(v1, "node not present")
	elif v2 not in graph:
		print(v2, "node not present")
	else:
		temp = [v2, e]
		graph[v1].append(temp)
def print_graph():
	for node in graph:
		for edges in graph[node]:
			print(node, " -> ", edges[0], " edge weight: ", edges[1])

graph = {}

add_node(1)
add_node(2)
add_node(3)
add_node(4)

add_edge(1, 2, 10)
add_edge(1, 3, 5)
add_edge(2, 3, 4)
add_edge(3, 4, 14)
add_edge(4, 1, 15)
print(graph)
print_graph()