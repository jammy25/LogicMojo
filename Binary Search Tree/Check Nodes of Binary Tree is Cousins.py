class Node:
	def __init__ (self, data):
		self.data = data
		self.left = self.right = None

def isSibling(root, a, b):

	if root is None:
		return 0

	return ((root.left == a and root.right == b) or
			(root.right == a and root.left == b) or
			(isSibling(root.left, a, b)) or
			(isSibling(root.right, a, b)))

def depth(root, ptr, level):

	if root is None:
		return 0

	if root == ptr:
		return level

	left = depth(root.left, ptr, level + 1)
	if left != 0:
		return left

	return depth(root.right, ptr, level + 1)

def isCousin(root, a, b):

	if ((depth(root, a, 1) == depth(root, b, 1)) and
			not (isSibling(root, a, b))):
		return True
	else:
		return False

# Driver Code

if __name__ == '__main__':

	root = Node(1)
	root.left = Node(4)
	root.left.left = Node(13)
	root.left.right = Node(12)
	root.left.right.left = Node(16)
	root.right = Node(25)
	root.right.right = Node(32)
	root.right.right.left = Node(26)
	root.right.right.right = Node(22)

	a = root.left.right
	b = root.left.left
	d = root.right.right

	print(isCousin(root, a, d))
	print(isCousin(root, a, b))