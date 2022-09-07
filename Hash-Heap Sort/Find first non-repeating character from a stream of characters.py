class Node:
	def __init__ (self, data):
		self.next = self.prev = None
		self.data = data

def first_non_repeating_char(stream):
	res = ''
	head = tail = None
	ascii_word = [0] * 256

	for ch in stream:
		# If the char has already appeared
		if ascii_word[ord(ch)] == -1:
			pass

		# char appears for the second time -> delete -> mark it for repeatition
		elif ascii_word[ord(ch)]:
			ptr = ascii_word[ord(ch)]
			
			if ptr == head:
				head = head.next
			elif ptr == tail:
				tail = tail.prev
				tail.next = None
			else:
				ptr.prev.next = ptr.next
				ptr.next.prev = ptr.prev

			ptr = None
			ascii_word[ord(ch)] = -1			

		# char appeared for the first time
		else:
			if not head:
				head = tail = Node(ch)
			else:
				tail.next = Node(ch)
				tail.next.prev = tail
				tail = tail.next
			ascii_word[ord(ch)] = tail

		if head:
			res += head.data
		else:
			res += "#"

	return res

# Driver Code

if __name__ == '__main__':

	print(first_non_repeating_char("ABCDBAGHC"))
	print(first_non_repeating_char("thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsoverthelazydog"))