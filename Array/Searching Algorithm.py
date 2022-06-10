# Find out if a key exists in the sorted list
# array[left..right] or not using binary search algorithm
def binarySearch(array, left, right, key):
    if left > right:
        return -1
    mid = left + ((right - left)//2)
    if array[mid] == key:
        return mid
    elif key < array[mid]:
        return binarySearch(array, left, mid - 1, key)
    else:
        return binarySearch(array, mid + 1, right, key)

if __name__ == '__main__':
 
    array = [2, 5, 6, 8, 9, 10]
    key = 5
    index = binarySearch(array, 0,len(array) - 1,key)
 
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")