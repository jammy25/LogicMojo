class Node:
	def __init__(self, key):
		self.data = key
		self.left = self.right = None

def height(root):
	if root is None:
		return 0

	return (1 + max(height(root.left), height(root.right)))

def diameter(root):
	if root is None:
		return 0

	left_height = height(root.left)
	right_height = height(root.right)

	left_diameter = diameter(root.left)
	right_diameter = diameter(root.right)

	return max(left_height + right_height + 1, max(left_diameter, right_diameter))
	
# Driver Code
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	print(diameter(root))