class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

result = 0
def findMaxSumBT(root):
	global result
	if root is None:
		return 0

	left = findMaxSumBT(root.left)
	right = findMaxSumBT(root.right)

	max_value = max(max(left, right) + root.data, root.data)
	max_top = max(max_value, left + right + root.data)
	result = max(result, max_top)
	return max_value

# Driver Code

if __name__ == '__main__':

	root = Node(10) 
	root.left = Node(2)
	root.right = Node(15)
	root.left.left = Node(-4)
	root.left.right = Node(-6) 
	root.left.left.left = Node(28)
	root.left.left.right = Node(-22)
	root.right.right = Node(-25)
	root.right.right.left = Node(3)
	root.right.right.right = Node(4)

	findMaxSumBT(root)
	print(result)