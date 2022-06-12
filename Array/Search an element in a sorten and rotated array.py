def findNumber(array, start, end, value): 
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == value:
        return mid
    if array[start] <= array[mid]:
        if array[start] <= value and array[mid] >= value:
            return findNumber(array, start, mid - 1, value)
        else:
            return findNumber(array, mid + 1, end, value)
    
    elif array[end] <= array[mid]:
        if array[end] >= value and array[mid] <= value:
            return findNumber(array, mid + 1, end, value)
        else:
            return findNumber(array, start, mid - 1, value)

array = [5, 6, 7, 8, 9, 10, 1, 2, 3]
start = 0
end = len(array) - 1
value = 8
a = findNumber(array, start, end, value)
print(a)