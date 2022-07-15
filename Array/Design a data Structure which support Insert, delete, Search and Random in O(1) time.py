import random

class MyDS:

	def __init__(self):

		self.arr = []
		self.hash = {}

	def insert(self, x):

		if x in self.hash:
			return

		# Else put element to the end of list
		s = len(self.arr)
		self.arr.append(x)
		
		# Also put it into hash
		self.hash[x] = s

	def delete(self, x):

		index = self.hash.get(x)
		if index == None:
			return
		del self.hash[x]

		# swap element to be deleted with last element in arr
		size = len(self.arr)
		last = self.arr[size - 1]
		self.arr[index], self.arr[size - 1] = self.arr[size - 1], self.arr[index]

		self.arr.remove(last)
		self.hash[last] = index

	def random(self):

		index = random.randrange(0, len(self.arr))
		return self.arr[index]

	def search(self, x):
		return self.hash.get(x, None)

# Driver Code
if __name__ == "__main__":
	ds = MyDS()
	ds.insert(10)
	ds.insert(20)
	ds.insert(30)
	ds.insert(40)
	print(ds.search(30))
	ds.delete(20)
	ds.insert(50)
	print(ds.search(50))
	print(ds.random())