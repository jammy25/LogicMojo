class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

def printBottom(root, dist, level, dict):
	if root is None:
		return

	if dist not in dict or level >= dict[dist][1]:
		dict[dist] = (root.data, level)

	printBottom(root.left, dist - 1, level + 1, dict)
	printBottom(root.right, dist + 1, level + 1, dict)

def BottomView(root):
	dict = {}
	printBottom(root, 0, 0, dict)
	for key in sorted(dict.keys()):
		print(dict.get(key)[0], end = ' ')

# Driver Code

if __name__ == '__main__':

	root = Node(13)
	root.left = Node(10)
	root.left.left = Node(8)
	root.left.right = Node(12)
	root.left.right.left = Node(11)
	root.right = Node(18)
	root.right.right = Node(20)
	root.right.right.left = Node(22)

	BottomView(root)