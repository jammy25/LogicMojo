# def knows(x, y):
# 	return mat[x][y]

def findCelebrity(n):
	x = 0
	y = n - 1
	celebrity = -1
	while x < y:

		if mat[x][y] == 1:
			x += 1
		else:
			y -= 1
	
	celebrity = x
		
	return celebrity

# Driver Code
mat = [ [ 0, 0, 1, 0 ], 
        [ 0, 0, 1, 0 ], 
        [ 0, 0, 0, 0 ], 
        [ 0, 0, 1, 0 ] ]
# Test_case: 2
# mat = [ [1,1,0],
#         [0,1,0],
#         [1,1,1] ]
n = len(mat)

a = findCelebrity(n)
print(a)