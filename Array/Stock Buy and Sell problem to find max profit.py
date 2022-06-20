def max_profit(prices, days):

    profit = 0

    for i in range(1, days):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit

# Driver Code

price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

a = max_profit(price, n)
print(a)