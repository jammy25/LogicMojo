class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

def buildUtil(inOrder, postOrder, inStart, inEnd, pIndex):

	if (inStart > inEnd):
		return None

	# Pick current node from Postorder traversal
    # using postIndex and decrement postIndex
	root = Node(postOrder[pIndex[0]])
	pIndex[0] -= 1

	# If this node has no children
    # then return
	if (inStart == inEnd):
		return root

	# Else find the index of this node
    # in Inorder traversal
	iIndex = search(inOrder, inStart, inEnd, root.data)
	root.right = buildUtil(inOrder, postOrder, iIndex + 1, inEnd, pIndex)
	root.left = buildUtil(inOrder, postOrder, inStart, iIndex - 1, pIndex)

	return root

# This function mainly initializes index
# of root and calls buildUtil()
def buildTree(inOrder, postOrder, n):
	pIndex = [n - 1]
	return buildUtil(inOrder, postOrder, 0, n - 1, pIndex)


# Function to find index of value in
# arr[start...end]. The function assumes
# that value is postsent in inOrder[]
def search(arr, start, end, value):
	i = 0
	for i in range(start, end + 1):
		if (arr[i] == value):
			break
	return i

# This function is here just to test
def preOrder(root):
	if root == None:
		return
	print(root.data, end = ' ')
	preOrder(root.left)
	preOrder(root.right)

# Driver Code
if __name__ == '__main__':

	inOrder = [4, 8, 2, 5, 1, 6, 3, 7]
	postOrder = [8, 4, 5, 2, 6, 7, 3, 1]
	n = len(inOrder)

	root = buildTree(inOrder, postOrder, n)
	print("Preorder of the constructed tree:")
	preOrder(root)