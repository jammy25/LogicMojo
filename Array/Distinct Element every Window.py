def countWindowDistinct(arr, k):

	dist_count = 0

	for i in range(k):

		j = 0

		while j < i:
			if (arr[i] == arr[j]):
				break
			else:
				j += 1

		if (j == i):
			dist_count += 1

	return dist_count

def countDistinct(arr, n, k):

	for i in range(n - k + 1):
		print(countWindowDistinct(arr[i:k + i], k))

                                          
						#### Efficient Method using HashMap ####


from collections import defaultdict

def distinctCount(arr, n, k):

	hm = defaultdict(int)

	distinct_count = 0

# Traverse through first window

	for i in range(k):
		if hm[arr[i]] == 0:
			distinct_count += 1
		hm[arr[i]] += 1
	print(distinct_count)

# Traverse through remaining array

	for i in range(k, n):
		if hm[arr[i - k]] == 1:
			distinct_count -= 1
		hm[arr[i - k]] -= 1

# Add new element to the current window
	
		if hm[arr[i]] == 0:
			distinct_count += 1
		hm[arr[i]] += 1

		print(distinct_count)


# Driver Code
arr = [1, 2, 1, 3, 4, 2, 3]
n = len(arr)
k = 4
# countDistinct(arr, n, k)
distinctCount(arr, n, k)