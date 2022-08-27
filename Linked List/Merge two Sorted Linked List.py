class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None

def display(node):
	while node:
		print(node.data, end = ' -> ')
		node = node.next
	print("X")

def mergeSort(first, second):
	# first, second = head1, head2
	temp = Node(0)

	if (first == None):
		return second
	if (second == None):
		return first

	if first.data <= second.data:
		temp = first
		first = temp.next

	else:
		pass

	new_list = temp

	while (first != None and second != None):

		if (first.data <= second.data):
			
			temp.next = first
			temp = first
			first = temp.next
		else:

			temp.next = second
			temp = second
			second = temp.next

	if (first == None):
		temp.next = second
	if (second == None):
		temp.next = first

	return new_list.next

# Driver Code

if __name__ == '__main__':

	first = Node(2)
	first.next = Node(4)
	first.next.next = Node(5)
	first.next.next.next = Node(8)

	second = Node(1) 
	second.next = Node(3)
	second.next.next = Node(6)
	second.next.next.next = Node(7)

	node = mergeSort(first, second)
	display(node)