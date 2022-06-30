def Sqrt(num):

    if num == 0 or num == 1:
        return num   
    start = 1
    end = num

    while start <= end:
        mid = (start + end) // 2
            
        if (mid * mid == num):
            return mid
        if mid * mid < num:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    return answer
  
print(Sqrt(64))