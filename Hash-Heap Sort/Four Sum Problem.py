def fourSum(arr, target):
	dict = {}
	n = len(arr)
	res = set()

	for i in range(n - 1):
		for j in range(i + 1, n):

			val = target - (arr[i] + arr[j])

			for x, y in dict.setdefault(val, []):
				if i == x or i == y or j == x or j == y:
					continue
				res.add(tuple(sorted([arr[x], arr[y], arr[i], arr[j]])))
			dict.setdefault(arr[i] + arr[j], []).append([i, j])
	return res

# Driver Code

if __name__ == '__main__':

	arr = [1, 5, 1, 0, 6, 0]
	k = 7
	print(fourSum(arr, k))