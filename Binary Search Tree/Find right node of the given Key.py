class Node:
	def __init__(self, data):
		self.left = self.right = None
		self.data = data

desiredLevel = 0

def findRightNode(root, value, level = 0):
	global desiredLevel
	if (root == None):
		return

	if (root.data == value):
		desiredLevel = level
		return None

	if (desiredLevel != 0):
		if (level == desiredLevel):
			return root

	left = findRightNode(root.left, value, level + 1)
	if left != None:
		return left

	return findRightNode(root.right, value, level + 1)

# Driver Code
if __name__ == '__main__':

	root = Node(1)
	root.left = Node(4)
	root.left.left = Node(13)
	root.left.right = Node(12)
	root.right =Node(25)
	root.right.right = Node(32)
	root.right.right.left = Node(26)
	root.right.right.right = Node(22)

	print(findRightNode(root, 12).data)