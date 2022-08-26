class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

def mirrorBT(root):
	if root is None:
		return

	left = mirrorBT(root.left)
	right = mirrorBT(root.right)

	root.left = right
	root.right = left

	return root

def inOrder(root):
	if root is None:
		return
	inOrder(root.left)
	print(root.data, end = ' ')
	inOrder(root.right)

# Driver Code

if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.right.left = Node(5)
	root.right.right = Node(4)

	print("Inorder traversal of the constructed tree is") 
	inOrder(root)
	mirrorBT(root)
	print("\nInorder traversal of the mirror tree is ") 
	inOrder(root)