# TC --> O(n), SC --> O(n)

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def leafNodes(root):
	if root != None:
		leafNodes(root.left)
		if (root.left == None and root.right == None):
			print(root.data)
		leafNodes(root.right)

def leftInternalNodes(root):
	if root:
		if root.left:
			print(root.data)
			leftInternalNodes(root.left)
		elif root.right:
			print(root.data)
			leftInternalNodes(root.right)

def rightInternalNodes(root):
	if root:
		if root.right:
			rightInternalNodes(root.right)
			print(root.data)

		elif root.left:
			rightInternalNodes(root.left)
			print(root.data)

def printBoundary(root):
	if root:
		print(root.data)

		leftInternalNodes(root.left)

		leafNodes(root.left)
		leafNodes(root.right)

		rightInternalNodes(root.right)

# Driver Code
if __name__ == '__main__':

	root = Node(20)
	root.left = Node(8)
	root.left.left = Node(4)
	root.left.right = Node(12)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)
	root.right = Node(22)
	root.right.right = Node(25)
	printBoundary(root)