# Time Complexity = O(m*n)
# Space Complexity = O(1)

def first(arr, low, high):

    if high >= low:

        mid = low + (high - low) // 2

        if ( (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1):
            return mid
        elif (arr[mid] == 0):
            return first(arr, (mid + 1), high)
        else:
            return first(arr, low, mid - 1)

    return -1

def rowWithMax1s(mat):
    
    Row, Column = len(mat), len(mat[0])
    max_row_index, Max = 0, -1

    for i in range(Row):

        index = first(mat[i], 0, Column - 1)
        if (index != -1 and Column - index > Max):
            Max = Column - index
            max_row_index = i

    return max_row_index


# Driver Code
mat = [[[0,1,1,1],[0,0,1,1],[0,0,0,1],[1,1,1,1]],
       [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]],
       [[1, 1, 1],[0, 0, 0],[1, 1, 0],[1, 0, 0]],
       [[0, 0, 0, 1, 1],[0, 0, 1, 1, 1],[0, 0, 0, 0, 0],[0, 1, 1, 1, 1],[0, 0, 0, 0, 1]]]
for matrix in mat:
    print(rowWithMax1s(matrix))