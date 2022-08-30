class Node:
	def __init__ (self, data):
		self.next = None
		self.data = data

def display(node):
	while node:
		print(node.data, end = ' -> ')
		node = node.next
	print("Null")

def rearrangeLL(head):
	if head is None:
		return

	mid = findMiddle(head)
	mid = reverse(mid)

	mergeLL(head, mid)

def findMiddle(head):
	prev = None
	fast = slow = head

	while fast and fast.next:
		prev = slow
		slow = slow.next
		fast = fast.next.next

	if fast and fast.next is None:
		prev = slow
		slow = slow.next

	prev.next = None
	return slow

def reverse(head):
	result = None
	current = head

	while current:
		next = current.next
		current.next = result
		result = current
		current = next
	return result

def mergeLL(a, b):
	if a is None:
		return b

	if b is None:
		return a

	recur = mergeLL(a.next, b.next)

	result = a
	a.next = b
	b.next = recur

	return result

# Driver Code

if __name__ == '__main__':

	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)
	head.next.next.next.next.next = Node(6)
	head.next.next.next.next.next.next = Node(7)

	print("Original Linked List: ")
	display(head)

	print("Rarrange Linked List")
	rearrangeLL(head)
	display(head)