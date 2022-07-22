class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.lchild = None
		self.rchild = None

# Recursive function to insert a 
# key into a BST
def insert(node, data):
	if node == None:
		return Node(data)

	# Otherwise recur down the tree
	if node.data > data:
		node.lchild = insert(node.lchild, data)
	else:
		node.rchild = insert(node.rchild, data)

	return node

# Function to find the k-th 
# largest element in a given tree
def kthlargestBST(root, k, c):

	if root == None or c[0] >= k:
		return

	# Follow reverse inorder traversal 
	# so that largest element is
	# visited first
	kthlargestBST(root.rchild, k, c)

	#increment count of visited nodes
	c[0] += 1

	# If c becomes k now, then this
	# is the k'th largest
	if c[0] == k:
		print ('Kth largest element is', root.data)
		return

	# Recur for left subtree
	kthlargestBST(root.lchild, k, c)

def kthlargest(root, k):

	# Initialize count of nodes
	# visited as 0
	c = [0]

	kthlargestBST(root, k, c)

# Driver Code
if __name__ == '__main__':

	keys = [15, 10, 20, 8, 12, 16, 25]

	root = None
	for data in keys:
		root = insert(root, data)

	k = 2
	result = kthlargest(root, k)