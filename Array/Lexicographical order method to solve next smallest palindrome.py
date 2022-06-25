def utilityFunction(arr, n):
	
	mid = int(n/2)
	leftsmaller = False
	i = mid - 1
	j = mid + 1 if (n % 2) else mid

	while (i >= 0 and arr[i] == arr[j]):
		i -= 1
		j += 1

	if (i < 0 or arr[i] < arr[j]):
		leftsmaller = True
	
	while (i >= 0):	
		arr[j] = arr[i]
		j += 1
		i -= 1
		
	if leftsmaller == True:
		carry = 1
		i = mid - 1
		
		if (n % 2 == 1):
			
			arr[mid] += carry
			carry = int(arr[mid] / 10)
			arr[mid] %= 10
			j = mid + 1

		else:
			j = mid

		while (i >= 0):

			arr[i] += carry
			carry = arr[i] / 10
			arr[i] %= 10
			arr[j] = arr[i]
			j += 1
			i -= 1

def generateNextPalindrome(arr, n):

	print("\nNext palindrome is:") 

	if( AreAll9s( arr, n ) == True): 
    
	    print( "1") 
	    for i in range(1, n): 
	        print( "0" ) 
	    print( "1") 

	else: 

	    utilityFunction ( arr, n ) 

	    printArray (arr, n) 

def AreAll9s(arr, n ): 
	for i in range(1, n): 
		if( arr[i] != 9 ) :
			return 0
	return 1

def printArray(arr, n): 

    for i in range(0, n): 
        print(int(arr[i])) 
    print() 

if __name__ == "__main__": 
    arr = [8, 3, 1, 7, 7, 9, 7, 9, 3, 2, 3] 
    n = len(arr) 
    generateNextPalindrome( arr, n )	