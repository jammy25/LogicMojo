class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__ (self):
		self.head = None
	def insert(self, new_data):
		new_node = Node(new_data)

		if self.head is None:
			self.head = new_node
			return
		curr_node = self.head
		while curr_node.next:
			curr_node = curr_node.next
		curr_node.next = new_node

	def mergeSort(self, node):
		if (node == None or node.next == None):

			return node

		middle = self.getMiddle(node)
		middle_next = middle.next

		middle.next = None

		left = self.mergeSort(node)
		right = self.mergeSort(middle_next)

		sortedList = self.sortedMerge(left, right)
		return sortedList

	def sortedMerge(self, first, second):

		temp = None

		if first == None:
			return second
		if second == None:
			return first

		if first.data <= second.data:
			temp = first
			temp.next = self.sortedMerge(first.next, second)

		else:
			temp = second
			temp.next = self.sortedMerge(first, second.next)
		return temp

	def getMiddle(self, head):
		if (head == None):
			return head
		slow = head
		fast = head

		while (fast.next != None and fast.next.next != None):
			slow = slow.next
			fast = fast.next.next

		return slow

def print_LL(head):
	if head is None:
		print(' ')
		return
	curr_node = head
	while curr_node:
		print(curr_node.data, end = ' -> ')
		curr_node = curr_node.next
	print('X')

# Driver Code

if __name__ == '__main__':

	list1 = LinkedList()
	list1.insert(4)
	list1.insert(2)
	list1.insert(8)
	list1.insert(5)
	list1.insert(1)
	list1.insert(6)
	list1.insert(3)
	list1.insert(7)

	print_LL(list1.head)

	print("Sorted Linked List is: ")
	list1.head1 = list1.mergeSort(list1.head)
	print_LL(list1.head1)