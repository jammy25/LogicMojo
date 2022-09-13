def powerSet(str1, index, curr):
	n = len(str1)

	if (index == n):
		return

	print(curr)

	for i in range(index + 1, n):
		curr += str1[i]
		powerSet(str1, i, curr)

		curr = curr.replace(curr[len(curr) - 1], "")

	return

# Driver Code

if __name__ == '__main__':
	str = "123"
	powerSet(str, -1, "")