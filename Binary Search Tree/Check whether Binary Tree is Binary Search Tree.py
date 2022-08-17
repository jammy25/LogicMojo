INT_max = 4294967295
INT_min = -4294967295

class Node:
	def __init__(self, key):
		self.right = None
		self.left = None
		self.data = key

def isBST(root):
	return (isBSTUtil(root, INT_min, INT_max))

def isBSTUtil(root, min, max):
	if root is None:
		return True

	if root.data < min or root.data > max:
		return False

	return(isBSTUtil(root.left, min, root.data - 1) and 
		isBSTUtil(root.right, root.data + 1, max))

# Driver Code
if __name__ == '__main__':

	root = Node(4)
	root.left = Node(2)
	root.right = Node(5)
	root.left.left = Node(1)
	root.left.right = Node(3)

	if (isBST(root)):
		print("Is BST")
	else:
		print("Not a BST")