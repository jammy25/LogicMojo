class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

def sumTree(root):
	if root is None:
		return 0

	oldvalue = root.data

	left = sumTree(root.left)
	right = sumTree(root.right)

	root.data = left + right

	return root.data + oldvalue

def inOrder(root):
	if root is None:
		return
	inOrder(root.left)
	print(root.data, end = ' ')
	inOrder(root.right)

# Driver Code

if __name__ == '__main__':

	root = Node(10)
	root.left = Node(-3)
	root.left.left = Node(9)
	root.left.right = Node(-4)
	root.right = Node(4)
	root.right.left = Node(6)
	root.right.right = Node(5)

	inOrder(root)
	print()
	sumTree(root)
	inOrder(root)