no_of_chars = 256

def findMinWindow(string, pat):
	str_len = len(string)
	ptr_len = len(pat)

	if str_len < ptr_len:
		print("Window does not exist")
		return ""

	asci_str = [0] * no_of_chars
	asci_ptr = [0] * no_of_chars

	# Store occurrence of characters in the pattern
	for i in range(0, ptr_len):
		asci_ptr[ord(pat[i])] += 1

	start, start_index, min_len = 0, -1, float('inf')
	count = 0

	for j in range(0, str_len):
		asci_str[ord(string[j])] += 1

		if (asci_ptr[ord(string[j])] != 0 and
			asci_str[ord(string[j])] <=
			asci_ptr[ord(string[j])]):
			count += 1

		if (count == ptr_len):

			while (asci_str[ord(string[start])] > asci_ptr[ord(string[start])] or
					asci_ptr[ord(string[start])] == 0):

				if (asci_str[ord(string[start])] >
					asci_ptr[ord(string[start])]):
					asci_str[ord(string[start])] -= 1

				start += 1

			len_window = j - start + 1
			if min_len > len_window:

				min_len = len_window
				start_index = start

	if start_index == -1: 
	    print("window doesn't exists")  
	    return ""  
      
	return string[start_index : start_index + min_len]

# Driver Code

if __name__ == '__main__':

	string = "ADOBECODEBANC"
	pat = "ABC"

	print("Smallest window is: ")
	print(findMinWindow(string, pat))