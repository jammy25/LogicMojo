class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def doOverLap(l1, r1, l2, r2):
	if (l1.x > r2.x or l2.x > r1.x):
		return False
	if (r1.y > l2.y or r2.y > l1.y):
		return False
	return True

# Driver code
if __name__ == "__main__":
	l1 = point(0, 10)
	r1 = point(10, 0)
	l2 = point(5, 5)
	r2 = point(15, 0)

	if (doOverLap(l1, r1, l2, r2)):
		print("Rectangles overlap")
	else:
		print("Rectangles don't overlap")