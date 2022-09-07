def groupAnagrams(words):

	A = [''.join(sorted(word)) for word in words]

	dict = {}
	for i, e in enumerate(A):
		dict.setdefault(e, []).append(i)
		
	for index in dict.values():
		print([words[i] for i in index])

# Driver Code

if __name__ ==	'__main__':

	words = ["cat", "dog", "tac", "got", "act"]

	groupAnagrams(words)