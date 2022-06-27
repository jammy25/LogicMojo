def maxSubarraySum(arr, n):

    max_so_far = arr[0]
    max_ending_here = 0

    for i in range(n):
        max_ending_here += arr[i]
        if max_ending_here < 0:
            max_ending_here = 0

        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far

# Driver Code
# arr = [-2, -3, 4, -1, -2, 1, 5, -3]
arr = [-5, 6, -7, 1, 4, -8, 16]
n = len(arr)
a = maxSubarraySum(arr, n)
print(a)