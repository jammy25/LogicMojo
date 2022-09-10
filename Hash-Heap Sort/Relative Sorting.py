def relative_sorting(first, second):
	mapDict = {}
	result = []
	i = 0

	for num in first:
		mapDict.setdefault(num, 0)
		mapDict[num] += 1

	for num in second:
		while mapDict.get(num, 0):
			first[i] = num
			i += 1
			mapDict[num] -= 1

	for num in mapDict:
		while mapDict[num]:
			result.append(num)
			mapDict[num] -= 1

	result.sort()
	for num in result:
		first[i] = num
		i += 1

# Driver Code

if __name__ == '__main__':

	first = [5, 8, 9, 3, 5, 7, 1, 3, 4, 9, 3, 5, 1, 8, 4]
	second = [3, 5, 7, 2]

	relative_sorting(first, second)
	print("Sorted List: ", first)