from collections import defaultdict

class Node:
	def __init__ (self, data):
		self.left = self.right = None
		self.data = data

class LRUcache:

	def __init__ (self, capacity: int):
		self.capacity = capacity
		self.current_capacity = 0
		self.head = self.tail = None
		self.cache = defaultdict(list)

	def update(self, key):
		node = self.cache[key][0]
		if node == self.head:
			return
		if node == self.tail:
			self.tail = node.prev
			self.tail.next = None
		else:
			node.prev.next = node.next
			node.next.prev = node.prev

		node.prev = None
		node.next = self.head
		self.head.prev = node
		self.head = node

	def get(self, key: int) -> int:
		if not self.cache[key]:
			return -1
		self.update(key)
		return self.cache[key][1]

	def put(self, key: int, value: int) -> None:
		if self.cache[key]:
			self.update(key)
			self.cache[key][1] = value
			return
		if self.current_capacity < self.capacity:
			node = Node(key)
			if not self.head:
				self.head = self.tail = node
			else:
				self.head.prev = node
				node.next = self.head
				self.head = node

			self.cache[key] = [node, value]
			self.current_capacity += 1
			return
		# delete lru node
		node = self.tail
		self.cache[node.data] = []
		self.tail = self.tail.prev
		if self.tail:
			self.tail.next = None

		# add new node
		node = Node(key)
		node.next = self.head
		if self.head:
			self.head.prev = node
			self.head = node
			self.cache[key] = [node, value]

# Driver Code

if __name__ == '__main__':

	obj = LRUcache(2)
	obj.put(1, 1)
	obj.put(2, 2)
	print(obj.get(1))
	obj.put(3, 3)
	print(obj.get(2))
	obj.put(4, 4)
	print(obj.get(1))
	print(obj.get(3))	
	print(obj.get(4))