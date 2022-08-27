class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None

def display(node):
	while node:
		print(node.data, end = ' -> ')
		node = node.next
	print(X)

def findLength(head):
	ptr = head
	count = 0

	while (ptr != None):
		count += 1
		ptr = ptr.next

	return count

def desiredNode(head1, head2):
	len1 = findLength(head1)
	len2 = findLength(head2)

	if (len1 > len2):
		diff = len1 - len2
		return findIntersection(diff, head1, head2)

	else:
		diff = len2 - len1
		return findIntersection(diff, head2, head1)

def findIntersection(diff, node1, node2):

	head1 = node1
	head2 = node2
	for i in range(diff):
		if head1 == None:
			return -1

		head1 = head1.next

	while (head1 != None and head2 != None):
		if (head1.data == head2.data):
			return head1.data

		head1 = head1.next
		head2 = head2.next

	return -1

# Driver Code

if __name__ == '__main__':

	headA = Node(2)
	headB = Node(5)
	headA.next = Node(3)
	headA.next.next = Node(3)
	headA.next.next.next = Node(1)
	headA.next.next.next.next = Node(0)
	headB.next = Node(1)
	headB.next.next = Node(0)

# TC 2
	# headA = Node(4)
	# headB = Node(5)
	# headA.next = Node(7)
	# headA.next.next = Node(9)
	# headB.next = headA.next

	print(desiredNode(headA, headB))