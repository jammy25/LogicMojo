class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def height(root):
	if root is None:
		return 0
	return max(height(root.left), height(root.right)) + 1

def isTreeBalanced(root):
	if root is None:
		return True

	lh = height(root.left)
	rh = height(root.right)

	if (abs(lh - rh) <= 1) and isTreeBalanced(root.left) is True and isTreeBalanced(root.right) is True:
		return True

	return False

# Driver Code
if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.left.left.left = Node(8)
	if isTreeBalanced(root):
		print("Tree is balanced")
	else:
		print("Tree is not balanced")
