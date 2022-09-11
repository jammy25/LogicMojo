def pow(x, n):

	if (n == 0):
		return 1
	result = pow(x, int(n / 2))

	if (n % 2 == 0):
		return result * result

	else:
		if (n > 0):
			return x * result * result
		else:
			return (result * result) / x

# Driver Code

if __name__ == '__main__':

	x, n = 2, 3
	print(pow(x, n))