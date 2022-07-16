class DLLNode:

	def __init__(self, d):
		self.next = None
		self.prev = None
		self.data = d

class myStack:

	def __init__(self):
		self.head = None
		self.mid = None
		self.count = 0

def createMyStack():
	ms = myStack()
	ms.count = 0
	return ms

def push(ms, new_data):
	new_DLLNode = DLLNode(new_data)
	new_DLLNode.prev = None
	new_DLLNode.next = ms.head
	ms.count += 1
	
	''' Change mid pointer in two cases
	1) LL is empty
	2) Number of Nodes in the LL is Odd'''
	if (ms.count == 1):
		ms.mid = new_DLLNode
	else:
		ms.head.prev = new_DLLNode

	# update mid if ms -> count is odd
		if ((ms.count % 2) != 0):
			ms.mid = ms.mid.prev

	ms.head = new_DLLNode

def pop(ms):
	if(ms.count == 0):
		print("Stack is empty")
		return -1
	head = ms.head
	item = head.data
	ms.head = head.next

	''' If LL does not become empty,
	update prev of new head as Null'''
	if (ms.head != None):
		ms.head.prev = None
	ms.count -= 1

	'''update the mid pointer when
	we have even number of elements 
	in the stack, i.e, move down the mid pointer'''
	if(ms.count % 2 == 0):
		ms.mid = ms.mid.next
	return item

def findMiddle(ms):
	if (ms.count == 0):
		print('Stack is empty now')
		return -1
	return ms.mid.data

def deleteMiddle(ms):
	if(ms.count == 0):
		print('Stack is empty for now')
		return
	ms.count -= 1
	ms.mid.next.prev = ms.mid.prev
	ms.mid.prev.next = ms.mid.next

	if (ms.count % 2 == 1):
		ms.mid = ms.mid.next
	else:
		ms.mid = ms.mid.prev

# Driver Code
if __name__ == '__main__':

	ms = createMyStack()
	push(ms, 11)
	push(ms, 22)
	push(ms, 33)
	push(ms, 44)
	push(ms, 55)
	print(createMyStack)
	print('popped: ', pop(ms))
	print('popped: ', pop(ms))
	print('middle element: ', findMiddle(ms))
	deleteMiddle(ms)
	print('New Middle Element: ', findMiddle(ms))