class Node:
	def __init__ (self, data):
		self.data = data
		self.prev = None
		self.next = None

class DoublyLinkedList:
	def __init__ (self):
		self.head = None
		self.tail = None

	def printDLL(self):
		if self.head is None:
			print("DLL is empty")

		else:
			ptr = self.head
			while ptr:
				print(ptr.data, end = ' ')
				ptr = ptr.next

	def insert(self, data):
		newNode = Node(data)

		if (self.head == None):
			self.head = self.tail = newNode
			self.head.previous = None
			self.tail.next = None
		else:
			self.tail.next = newNode
			newNode.previous = self.tail
			self.tail = newNode
			self.tail.next = None

	def search(self, x):
		ptr = self.head

		if (ptr == None):
			print ("Empty list")
			return

		while (ptr != None):
			if (ptr.data == x):
				print("Found")
				break
			ptr = ptr.next
	
	def deleteNode(self, x):
		ptr = self.head

		if (ptr == None):
			print("LL is empty")
			return

		while (ptr != None):

			if (ptr.data == x):

				if (self.head == ptr):
					self.head = ptr.next

				if (ptr.next != None):
					ptr.next.prev = ptr.prev

				if (ptr.prev != None):
					ptr.prev.next = ptr.next

				break

			ptr = ptr.next

# Driver Code

if __name__ == '__main__':

	 Dlist = DoublyLinkedList()
	 Dlist.insert(1)
	 Dlist.insert(2)
	 Dlist.insert(3)
	 Dlist.insert(4)
	 Dlist.insert(5)

	 Dlist.printDLL()
	 print()
	 Dlist.search(5)
	 Dlist.deleteNode(3)
	 Dlist.printDLL()