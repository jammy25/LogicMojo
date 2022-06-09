# Find out if a key exists in the sorted list
# array[left..right] or not using binary search algorithm
def binarySearch(array, left, right, key):
 
    #Practise Yourself : write your code here
    return None
    
if __name__ == '__main__':
 
    array = [2, 5, 6, 8, 9, 10]
    key = 5
    index = binarySearch(array, 0,len(array) - 1,key)
 
    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")