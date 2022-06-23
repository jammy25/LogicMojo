def searchElement(mat, n, x): 
    i = 0
    j = n - 1
    while (i < n and j >= 0):
       if mat[i][j] == x:
           print("Value found at: (", i,",", j,")")
           return
       if mat[i][j] > x:
           j -= 1
       else:
           i += 1
    print("Value not found")

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
n = len(mat)
x = 15
searchElement(mat, n, x)