class Node:
	def __init__(self, data):
		self.left = self.right = None
		self.data = data

def findNode_distanceDown(root, k):
	if root is None:
		return
	if k == 0:
			print(root.data, end =' ')
	else:
		findNode_distanceDown(root.left, k - 1)
		findNode_distanceDown(root.right, k - 1)

def printNode(root, target, k):
	if root is None:
		return -1
	if root == target:
		findNode_distanceDown(root, k)
		return 1

	dLeft = printNode(root.left, target, k)
	if dLeft != -1:

		if dLeft == k:
			print(root.data)
		else:
			findNode_distanceDown(root.right, k - dLeft - 1)
		return 1 + dLeft
		

	dRight =printNode(root.right, target, k)
	if dRight != -1:

		if dRight == k:
			print(root.data)
		else:
			findNode_distanceDown(root.left, k - dRight - 1)
		return 1 + dRight
	return -1

# Driver Code
if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.left.left = Node(4)
	root.left.left.left = Node(9)
	root.left.right = Node(5)
	root.left.right.left = Node(6)
	root.left.right.left.left = Node(12)
	root.left.right.left.left.right = Node(19)
	root.left.right.right = Node(7)
	root.left.right.right.right = Node(10)
	root.left.right.right.right.right = Node(11)
	root.right = Node(23)
	root.right.right = Node(32)

	target = root.left.right
	printNode(root, target, 3)