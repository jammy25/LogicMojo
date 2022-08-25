class Node:
	def __init__ (self, data):
		self.data = data
		self.left = self.right = None

def inorder(root):

	if root is None:
		return

	s1 = []
	curr = root

	while (curr or len(s1) > 0):

		while (curr != None):

			s1.append(curr)
			curr = curr.left

		curr = s1.pop()

		print(curr.data, end = ' ')
		curr = curr.right

# Driver Code

if __name__ == '__main__':

	root = Node(6)
	root.left = Node(4)
	root.left.right = Node(5)
	root.right = Node(10)
	root.right.left = Node(8)
	root.right.right = Node(12)

	inorder(root)
