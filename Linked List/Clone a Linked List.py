class Node:
	def __init__ (self, data, next = None, random = None):
		self.next = self.random = None
		self.data = data

def traverse(head):
	while head:
		# print current node data and random pointer data
		if head.random:
			print(head.data, f"({head.random.data})", end = ' -> ')
		else:
			print(head.data, end = ' -> ')

		head = head.next

	print("Null")

def clonedLL(head):

# 1. Create duplicate of each node of the original linked list
	
	# traverse the original linked list
	ptr = head
	while ptr:
		
		# take pointer to the next node of original list
		next = ptr.next
		
		# duplicate each node of the linked list
		dup = Node(ptr.data)
		
		# associate each duplicate node with next child of the original node
		ptr.next = dup
		dup.next = next

		# advance to the next node of original list
		ptr = next

# 2. Update the random pointers of the duplicated nodes
	
	# traverse the modified linked list
	# set the ptr back to head
	ptr = head
	while ptr:

		# if random pointer for original node exists, set it for the clone
		if ptr.random:
			ptr.next.random = ptr.random.next

		# advance to the next node of original list
		ptr = ptr.next.next

# 3. Extract the duplicate nodes from the modified linked list

	# construct a dummy node whose next pointer points to the head
	# of the cloned linked list
	clone = Node(-1)
	# maintain a tail node for the clone
	tail = clone

	# traverse the modified linked list
	ptr = head
	while ptr:

		# take pointer to the next node in the original list
		next = ptr.next.next

		# extract the duplicate
		dup = ptr.next
		tail.next = dup
		tail = dup

		# restore the original linked list
		ptr.next = next
		# advance to the next node of original list
		ptr = next

	# return head node of the cloned list
	return clone.next

# Driver Code

if __name__ == '__main__':

	head = Node(3)
	head.next = Node(4)
	head.next.next = Node(5)
	head.next.next.next = Node(6)
	head.next.next.next.next = Node(7)

	head.random = head.next.next
	head.next.random = head
	head.next.next.random = head.next.next.next.next
	head.next.next.next.random = head.next.next.next.next
	head.next.next.next.next.random = head.next

	print("Originl List: ")
	traverse(head)

	clone = clonedLL(head)

	print("\nCloned List: ")
	traverse(clone)