class Node:
	def __init__(self, data):
		self.left = self.right = None
		self.data = data

def printSpiralOrder(root):
	if root is None:
		return

	stack1 = []
	stack2 = []
	stack1.append(root)

	while (not len(stack1) == 0 or not len(stack2) == 0):

		while (not len(stack1) == 0):
			n1 = stack1[-1]
			stack1.pop()
			print(n1.data, end = ' ')

			if n1.right:
				stack2.append(n1.right)

			if n1.left:
				stack2.append(n1.left)

		while (not len(stack2) == 0):
			n2 = stack2[-1]
			stack2.pop()
			print(n2.data, end = ' ')

			if n2.left:
				stack1.append(n2.left)
			if n2.right:
				stack1.append(n2.right)

# Driver Code

if __name__  == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.left.left = Node(4)
	root.left.left.left = Node(8)
	root.left.left.right = Node(4)
	root.left.right = Node(5)
	root.left.right.left = Node(10)
	root.right = Node(3)
	root.right.left = Node(6)
	root.right.left.right = Node(16)
	root.right.right = Node(7)
	root.right.right.left = Node(17)

	printSpiralOrder(root)