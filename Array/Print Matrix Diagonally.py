rowend = 4
columnend = 5
def diagonalPrint(matrix) : 
    for k in range(0, rowend):
        i = k
        j = 0
        
        while i >= 0:
            print(matrix[i][j], end = " ")
            i = i - 1
            j = j + 1
     
    for k in range(1, columnend):
        i = rowend - 1
        j = k
         
        while j <= columnend - 1:
             print(matrix[i][j], end = " ")
             i = i - 1
             j = j + 1
    print()

matrix = [ [1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10], 
        [11, 12, 13, 14, 15], 
        [16, 17, 18, 19, 20],] 
diagonalPrint(matrix)