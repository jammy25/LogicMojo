class Node:
	def __init__(self, data):
		self.left = self.right = self.next = None
		self.data = data

def inorder(root):
	if not root:
		return root
	inorder(root.left)
	print(root.data, end = ' -> ')
	if root.next:
		print(root.next.data)
	else:
		print("None")
	inorder(root.right)

def NextAvailbleNode(root):
	if root.left:
		return root.left
	if root.right:
		return root.right
	if root.next:
		return NextAvailbleNode(root.next)
	return None

def FindNextNode(root):
	if root is None:
		return root
	if root.left and root.right:
		root.left.next = root.right
		# if root.next:
		# 	root.right.next = root.next.NextAvailbleNode
	elif root.left and root.next:
		root.left.next = NextAvailbleNode(root.next)
	if root.right and root.next:
		root.right.next = NextAvailbleNode(root.next)
	FindNextNode(root.right)
	FindNextNode(root.left)

# Driver Code

if __name__ == '__main__':

	root = Node(6)
	root.left = Node(4)
	root.left.left = Node(12)
	root.left.left.left = Node(9)
	root.right = Node(10)
	root.right.left = Node(8)
	root.right.right = Node(12)
	root.right.right.right = Node(14)

	inorder(root)
	print()
	FindNextNode(root)
	inorder(root)