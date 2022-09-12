# function which generates all possible n pairs of balanced parentheses.
# open : count of the number of open parentheses used in generating the current string s.
# close : count of the number of closed parentheses used in generating the current string s.
# s : currently generated string.
# res : a vector of strings to store all the valid parentheses.

def generateParenthesis(n, open, close, s, res):

	# if the count of both open and close parentheses reaches n, it means we have generated a valid parentheses.
    # So, we add the currently generated string s to the final ans and return.
	if (open == n and close == n):
		res.append(s)
		return

	else:

		 # At any index i in the generation of the string s, we can put an open parentheses only if its count until that time is less than n.
		if (open < n):
			generateParenthesis(n, open + 1, close, s + "{", res)

		# At any index i in the generation of the string s, we can put a closed parentheses only if its count until that time is less than the count of open parentheses.
		if (open > close):
			generateParenthesis(n, open, close + 1, s + "}", res)

# Driver Code

if __name__ == '__main__':

	res = []
	n = 2
	generateParenthesis(n, 0, 0, "", res)

	for s in res:
		print(s)