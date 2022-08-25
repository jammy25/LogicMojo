class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

first_node_level = 0
def printLeftView(root, level):

	global first_node_level
	if root is None:
		return

	if (first_node_level < level):
		print(root.data, end = ' ')
		first_node_level = level

	printLeftView(root.left, level + 1)
	printLeftView(root.right, level + 1)

# Driver Code

if __name__ == '__main__':

# test case 1
	# root = Node(13)
	# root.left = Node(10)
	# root.left.left = Node(8)
	# root.left.right = Node(12)
	# root.left.left.right = Node(11)
	# root.left.left.right.left = Node(22)
	# root.left.left.right.right = Node(24)
	# root.right = Node(18)
	# root.right.right = Node(20)

# test case 2
	root = Node(4)
	root.left = Node(5)
	root.right = Node(2)
	root.right.left = Node(3)
	root.right.right = Node(1)
	root.right.left.left = Node(6)
	root.right.left.right = Node(7)

	printLeftView(root, 1)