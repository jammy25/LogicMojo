# Time Complexity --> O(n*n)
# Space Complexity --> O(1)
def majorityElement(arr, n):

	maxCount = 0

	for i in range(n):
		count = 0
		
		for j in range(n):
			if (arr[i] == arr[j]):
				count += 1

		if (count > maxCount):
			maxCount = count
			index = i

	if (maxCount > n // 2):
		print(arr[index])
	else:
		print("No majority element")

# Driver_Code
# arr = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2 ]
arr = [3,2,3]
n = len(arr)

# Function_call
majorityElement(arr, n)