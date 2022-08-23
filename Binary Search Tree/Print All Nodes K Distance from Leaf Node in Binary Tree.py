class Node:
	def __init__(self, data):
		self.left = self.right = None
		self.data = data

def printKDistance(root, arr, visited, count, k):
	if root is None:
		return

	arr[count] = root.data
	visited[count] = False

	if (root.left == None and root.right == None and count - k >= 0 and visited[count - k] == False): 
		print(arr[count - k], end = ' ')
		visited[count - k] = True
		return

	printKDistance(root.left, arr, visited, count + 1, k)
	printKDistance(root.right, arr, visited, count + 1, k)

MAX_HEIGHT = 100000
def printKDistantfromLeaf(root, k): 
       global MAX_HEIGHT 
       arr = [None] * MAX_HEIGHT 
       visited = [False] * MAX_HEIGHT 
       printKDistance(root, arr, visited, 0, k) 

# Driver Code

if __name__ == '__main__':

	root = Node(3)
	root.left = Node(8)
	root.left.left = Node(11)
	root.left.right = Node(7)
	root.left.right.left = Node(6)
	root.left.right.right = Node(12)
	root.right = Node(9)
	root.right.right = Node(3)

	print("result value are:", end = ' ')
	printKDistantfromLeaf(root, 2)