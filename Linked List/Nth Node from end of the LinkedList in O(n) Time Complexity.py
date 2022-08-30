class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None

def display(node):
	while node:
		print(node.data, end = ' -> ')
		node = node.next
	print("Null")

def removeNthNode(head, n):

	fast = slow = head
	while n:
		fast = fast.next
		n -= 1

	if fast == None:
		return head

	slow = slow.next
	while fast.next:
		fast = fast.next
		slow = slow.next
	return slow

# Driver Code

if __name__ == '__main__':

	head = Node(2)
	head.next = Node(3)
	head.next.next = Node(3)
	head.next.next.next = Node(1)
	head.next.next.next.next = Node(0)
	head.next.next.next.next.next = Node(12)
	head.next.next.next.next.next.next = Node(7)

	print(removeNthNode(head, 3).data)