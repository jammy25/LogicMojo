class Node:
	def __init__(self, key):
		self.left =  None
		self.right = None
		self.data = key

prev = None

def createLinkedList(root):
	if root == None:
		return
		
	head = createLinkedList(root.left)
	
	global prev
	if prev == None:
		head = root

	else:
		root.left = prev
		prev.right = root
	
	prev = root

	createLinkedList(root.right)

	return head

def print_dll(head):
	while head:
		print(head.data, end = ' -> ')
		head = head.right
	print('X')

# Driver Code

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    head = createLinkedList(root)
    print_dll(head)