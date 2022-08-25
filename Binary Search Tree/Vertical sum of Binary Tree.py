class TNode:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

class DLLNode:
	def __init__(self, data):
		self.prev = self.next = None
		self.data = data

def verticalSumDLLUtil(root, head):
	head.data = head.data + root.data

	if root.left:
		if (head.prev == None):
			head.prev = DLLNode(0)
			head.prev.next = head

		verticalSumDLLUtil(root.left, head.prev)

	if root.right:
		if head.next == None:
			head.next = DLLNode(0)
			head.next.prev = head

		verticalSumDLLUtil(root.right, head.next)

# Function to print vertical sum of Tree.
# It uses verticalSumDLLUtil() to calculate sum.
def verticalSumDLL(root):
	head = DLLNode(0)
	verticalSumDLLUtil(root, head)

	while head.prev	!= None:
		head = head.prev

	while head:
		print(head.data, end = ' ')
		head = head.next

# Driver Code

if __name__ == '__main__':

	root = TNode(13)
	root.left = TNode(10)
	root.left.left = TNode(8)
	root.left.right = TNode(12)
	root.left.right.left = TNode(11)
	root.right = TNode(18)
	root.right.right = TNode(20)
	root.right.right.left = TNode(22)

	verticalSumDLL(root)