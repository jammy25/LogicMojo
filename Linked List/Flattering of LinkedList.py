class Node:
	def __init__ (self, data):
		self.right = self.down = None
		self.data = data

class LinkedList:
	def __init__ (self):
		self.head = None

	def insert(self, href, data):
		new_node = Node(data)
		new_node.down = href
		href = new_node
		return href

	def printLL(self):
		temp = self.head
		while temp:
			print(temp.data, end = ' ')
			temp = temp.down

	def flattenLL(self, root):
		if (root is None or root.right == None):
			return root

		root.right = self.flattenLL(root.right)
		root = self.merge(root, root.right)

		return root

	def merge(self, first, second):
		if first == None:
			return second
		if second == None:
			return first

		result = None
		if first.data < second.data:
			result = first
			result.down = self.merge(first.down, second)
		else:
			result = second
			result.down = self.merge(first, second.down)

		return result

# Driver Code

if __name__ == '__main__':

	llist = LinkedList()
	llist.head = llist.insert(llist.head, 29)
	llist.head = llist.insert(llist.head, 7)
	llist.head = llist.insert(llist.head, 6)
	llist.head = llist.insert(llist.head, 4)

	llist.head.right = llist.insert(llist.head.right, 21)
	llist.head.right = llist.insert(llist.head.right, 12)

	llist.head = llist.flattenLL(llist.head)
	llist.printLL()