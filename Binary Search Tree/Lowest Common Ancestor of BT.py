class Node:
	def __init__(self, data):
		self.left = self.right = None
		self.data = data

def LCA(root, data1, data2):
	if root is None:
		return

	if (root.data == data1 or root.data == data2):
		return root

	left = LCA(root.left, data1, data2)
	right = LCA(root.right, data1, data2)

	if left and right:
		return root

	if left:
		return left
	else:
		return right

# Driver Code

if __name__ == '__main__':

	root = Node(12)
	root.left = Node(4)
	root.left.left = Node(13)
	root.left.left.left = Node(2)
	root.left.right = Node(9)
	root.left.right.left = Node(26)
	root.left.right.right = Node(22)
	root.right = Node(25)
	root.right.left = Node(16)
	root.right.right = Node(32)

	print(LCA(root, 2, 22).data)
	print(LCA(root, 13, 16).data)
	print(LCA(root, 16, 32).data)
	print(LCA(root, 2, 13).data)