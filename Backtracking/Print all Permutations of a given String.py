def permutation(word, low, high):

	if low == high:
		res.append(''.join(word))
		return

	for i in range(low, high):
		word[i], word[low] = word[low], word[i]
		permutation(word, low + 1, high)
		word[low], word[i] = word[i], word[low]

# Driver Code

if __name__ == '__main__':

	res = []
	word = ['A', 'B', 'C']
	permutation(word, 0, len(word))
	print(res)