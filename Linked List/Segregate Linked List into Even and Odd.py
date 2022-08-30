class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None

head = None
def segregateEvenOdd():
	global head

	ptr = head
	evenStart = oddStart = None
	evenEnd = oddEnd = None

	while ptr:
		val = ptr.data

		if ((val % 2) != 0):
			if (oddStart == None):
				oddStart = ptr
				oddEnd = oddStart
			else:
				oddEnd.next = ptr
				oddEnd = oddEnd.next

		else:
			if (evenStart == None):
				evenStart = ptr
				evenEnd = evenStart
			else:
				evenEnd.next = ptr
				evenEnd = evenEnd.next 

		ptr = ptr.next

	if (oddStart == None or evenStart == None):
		return

	evenEnd.next = oddStart
	oddEnd.next = None

	head = evenStart

def display(node):
	while node:
		print(node.data, end = ' -> ')
		node = node.next
	print('Null')

# Driver Code

if __name__ == '__main__':

	head = Node(2)
	head.next = Node(5)
	head.next.next = Node(4)
	head.next.next.next = Node(6)
	head.next.next.next.next = Node(8)
	head.next.next.next.next.next = Node(3)
	head.next.next.next.next.next.next = Node(7)

# Test Case 2
	# head = Node(2)
	# head.next = Node(4)
	# head.next.next = Node(6)
	# head.next.next.next = Node(8)
	# head.next.next.next.next = Node(10)

	print("Original Linked List: ")
	display(head)

	segregateEvenOdd()
	print("\nSegregated Linked List: ")
	display(head)