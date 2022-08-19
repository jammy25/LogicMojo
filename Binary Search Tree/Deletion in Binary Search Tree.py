class Node:
	def __init__(self, data):
		self.left = self.right = None
		self.data = data

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data, end = ' -> ')
		inorder(root.right)

def delete(root, data, value):
	if root is None:
		return root

	if (root.data > value):
		if root.left:
			root.left = delete(root.left, root.data, value)
		else:
			print("Given node is not present")
	# return root

	if (root.data < value):
		if root.right:
			root.right = delete(root.right, value)
		else:
			print("Given node is not present")
	

	# If the root node is a leaf node
	# if not root.left and not root.right:
	# 	return None

	# If only one child exist
	else:	
		if not root.left:
			temp = root.right
			root = None
			return temp
		if (root.right is None):
			temp = root.left
			root = None
			return temp

		node = root.left
		while node.left:
			node = node.left
		root.data = node.data
		root.right = delete(node.data, value)
	return root

	# # If both child exist
	# succParent = root

	# succ = root.right

	# while succ.left != None:
	# 	succParent = succ
	# 	succ = succ.left

	# if succParent != root:
	# 	succParent.left = succ.right
	# else:
	# 	succParent.right = succ.right

	# root.key = succ.key

	# return root

# Driver Code
if __name__ == '__main__':

	root = Node(50)
	root.left = Node(30)
	root.left.left = Node(20)
	root.left.right = Node(40)
	root.right = Node(70)
	root.right.left = Node(60)
	root.right.right = Node(80)

	delete(root, root.data, 30)