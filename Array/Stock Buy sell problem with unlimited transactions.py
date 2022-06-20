def stockBuySell(price, n):
	# prices must be given for atleast two days
	if (n == 1):
		return
	# Traverse
	i = 0
	while i < n - 1:

		while ((i < (n - 1)) and (price[i + 1] <= price[i])):
			i += 1
		
		if i == n - 1:
			break
		# store index of minima
		buy = i
		i += 1

		while ((i < n) and (price[i] >= price[i - 1])):
			i += 1
		# store index of maxima
		sell = i - 1

		print(price[buy] + price[sell])

#
price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

stockBuySell(price, n)