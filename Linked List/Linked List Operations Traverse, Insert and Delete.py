class Node:
	def __init__ (self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__ (self):
		self.head = None
		self.tail = None

	def insert(self, data):
		newNode = Node(data)

		if self.head is None:
			self.head = self.tail = newNode

		else:
			self.tail.next = newNode
			self.tail = newNode

	def search(self, value):
		ptr = self.head
		while (ptr != None):
			if (ptr.data == value):
				print("Yes")
			ptr = ptr.next
		print("No")
	def deleteNode(self, value):
		ptr = self.head
		prev = None
		if (ptr != None and ptr.data == value):
			head = ptr.next
			return

		while (ptr != None and ptr.data != value):
			prev = ptr
			ptr = ptr.next
		if (ptr == None):
			retrun
		prev.next = ptr.next

	def printLL(self):
		if self.head is None:
			print("LL is empty")
		else:
			ptr = self.head
			while (ptr != None):
				print(ptr.data, end = ' ')
				ptr = ptr.next

# Driver Code
if __name__ == '__main__':

	LL1 = LinkedList()
	LL1.insert(1)
	LL1.insert(2)
	LL1.insert(3)
	LL1.insert(4)
	LL1.insert(5)

	LL1.printLL()
	LL1.deleteNode(3)
	print()
	LL1.printLL()
	print()
	LL1.search(6)
	