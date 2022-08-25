class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

def maxPathSum(root, pathSum = 0, maxSum = 0):
	if root is None:
		maxSum = max(maxSum, pathSum)
		return maxSum

	pathSum += root.data
	maxSum = maxPathSum(root.left, pathSum, maxSum)
	maxSum = maxPathSum(root.right, pathSum, maxSum)
	return maxSum

# Driver Code

if __name__ == '__main__':
	root = Node(6)
	root.left = Node(4)
	root.left.left = Node(6)
	root.left.right = Node(5)
	root.right = Node(10)
	root.right.left = Node(8)
	root.right.right = Node(12)

	print(maxPathSum(root))