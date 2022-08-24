class Node:
	def __init__ (self,data):
		self.left = self.right = None
		self.data = data

def find_LCA(root, data1, data2):
	if root is None:
		return

	if (root.data == data1 or root.data == data2):
		return root

	left = find_LCA(root.left, data1, data2)
	right = find_LCA(root.right, data1, data2)

	if left and right:
		return root

	if left:
		return left
	else:
		return right

# function to find distance of any node
# from root
def find_distance_from_LCA(root, data):

	# case when we reach a beyond leaf node
    # or when tree is empty
    if root is None:
    	return -1

    if root.data == data:
    	return 0

    left = find_distance_from_LCA(root.left, data)
    right = find_distance_from_LCA(root.right, data)
    distance = max(left, right)

    if distance >= 0:
    	return (distance + 1)
    else:
    	return -1

# function to find distance between two
# nodes in a binary tree
def dist_between_two_nodes(root, data1, data2):
	lca = find_LCA(root, data1, data2)
	if lca:
		return find_distance_from_LCA(lca, data1) + find_distance_from_LCA(lca, data2)
	else:
		return -1

# Driver Code

if __name__ == '__main__':

	root = Node(12)
	root.left = Node(4)
	root.left.left = Node(13)
	root.left.left.left = Node(2)
	root.left.right = Node(9)
	root.left.right.right = Node(22)
	root.left.right.left = Node(26)
	root.right = Node(25)
	root.right.left = Node(16)
	root.right.right = Node(32)
 
	print(dist_between_two_nodes(root, 2, 26))
	print(dist_between_two_nodes(root, 2, 16))
