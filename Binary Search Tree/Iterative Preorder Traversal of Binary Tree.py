class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

def preOrder(root):
	if root is None:
		return

	stack = []
	stack.append(root)

	while (len(stack) > 0):

		root = stack.pop()
		print(root.data, end = ' ')

		if (root.right):
			stack.append(root.right)

		if (root.left):
			stack.append(root.left)

# Driver Code

if __name__ =='__main__':

	root = Node(6)
	root.left = Node(4)
	root.left.right = Node(5)
	root.right = Node(10)
	root.right.left = Node(8)
	root.right.right = Node(12)

	preOrder(root)