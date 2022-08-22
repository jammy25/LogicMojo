class Node:
	def __init__(self, data):
		self.left = self.right = None
		self.data = data

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data, end = ' ')
		inorder(root.right)

def delete(root, key):
	if not root:
		return root

	if root.data > key:
		root.left = delete(root.left, key)
	elif root.data < key:
		root.right = delete(root.right, key)

	else:
		if not root.left and not root.right:
			return None
		if not root.left:
			return root.right
		if not root.right:
			return root.left

		temp = root.left
		while temp.rigth:
			temp = temp.right
		temp.data, root.data = root.data, temp.data
		root.left = delete(root.left, temp.data)
	return root

# Driver Code
if __name__ == '__main__':
	root = Node(50)
	root.left = Node(30)
	root.left.left = Node(20)
	root.left.right = Node(40)
	root.right = Node(70)
	root.right.left = Node(60)
	root.right.right = Node(80)

	inorder(root)
	root = delete(root,40)
	print()
	inorder(root)