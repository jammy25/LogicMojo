NO_OF_CHARS = 256

def a(string):
    List = []
    for i in string:
        List.append(i)
    return List
    
def b(List):
    return "".join(List)
    
def removeDuplicates(string):
    bin_hash = [0] * NO_OF_CHARS
    input_index = 0
    result_index = 0
    temp = ""
    mutablestring = a(string)
    
    while input_index != len(mutablestring):
        temp = mutablestring[input_index]
        if bin_hash[ord(temp)] == 0:
            bin_hash[ord(temp)] = 1
            mutablestring[result_index] = mutablestring[input_index]
            result_index += 1
        input_index += 1
        
    return b(mutablestring[0:result_index])
    
# Driver Code
string = "cbacdcbc"
print(removeDuplicates(string))