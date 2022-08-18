class Node:
	def __init__(self, key):
		self.right = None
		self.left = None
		self.data = key

def findNode_distanceDown(root, k):
		if root is None:
			return
		if k == 0:
			print(root.data, end = ' ')
			
		else:
			findNode_distanceDown(root.left, k - 1)
			findNode_distanceDown(root.right, k - 1)

# Driver Code
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(8)

	findNode_distanceDown(root, 2)