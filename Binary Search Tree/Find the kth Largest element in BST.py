class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
        
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return
        elif root.data > key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
            
    return root

# Function to find the k-th 
# largest element in a given tree
def kthLargestUtil(root, k, c):
	# Base cases, the second condition 
    # is important to avoid unnecessary
    # recursive calls 
    if root is None or c[0] >= k:
        return
    # Follow reverse inorder traversal 
    # so that the largest element is 
    # visited first
    kthLargestUtil(root.right, k, c)
    # Increment count of visited nodes 
    c[0] += 1
    
    # If c becomes k now, then this is 
    # the k'th largest 
    if c[0] == k:
        print (root.data)
    # Recur for left subtree     
    kthLargestUtil(root.left, k, c)

 # Function to find k'th largest element   
def kthLargest(root, k):

	# Initialize count of nodes
	# visited as 0
	c = [0]

	# Note that c is passed by reference
	kthLargestUtil(root, k, c)

# Driver Code
if __name__ == '__main__':

# Test case 1:
	# keys = [15, 10, 20, 8, 12, 16, 25]

	# root = None
	# for data in keys:
	# 	root = insert(root, data)

	# k = 2
	# result = kthlargest(root, k)

# Test Case 2:
    r = Node(20)
    r = insert(r, 8)
    r = insert(r, 4)
    r = insert(r, 22)
    r = insert(r, 12)
    r = insert(r, 10)
    r = insert(r, 14)
    
    kthLargest(r, 2)