def findSingle(arr, n): 
    
    result = arr[0]

    for i in range(1, n):
    	
    	result = arr[i] ^ result 

    return result 

# Driver Code
array = [[6,2,4,3,4,2,3],
		  [4,1,2,1,2],
		  [2, 2, 1]]
for arr in array:
	print ('Element is', findSingle(arr, len(arr)))