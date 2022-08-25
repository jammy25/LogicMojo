class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

def reverseLevelOrder(root):
	stack = []
	queue = []
	queue.append(root)

	while (len(queue) > 0):
		root = queue.pop(0)
		stack.append(root)

		if (root.right):
			queue.append(root.right)

		if (root.left):
			queue.append(root.left)

	while (len(stack) > 0):
		root = stack.pop()
		print(root.data, end = ' ')

# Driver Code
if __name__ == '__main__':

	root = Node(1) 
	root.left = Node(2) 
	root.right = Node(3) 
	root.left.left = Node(4) 
	root.left.right = Node(5)

	reverseLevelOrder(root)