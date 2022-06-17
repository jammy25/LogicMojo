def findPlatform(arrival, departure, n):
	arrival.sort()
	departure.sort()

	i = 0
	j = 0
	platform_needed = 1
	min_platform = 1
	while i < n and j < n:
	    
	    if arrival[i] <= departure[j]:
	        platform_needed += 1
	        i += 1
	        if platform_needed > min_platform:
	            min_platform = platform_needed
	    else:
	        platform_needed -= 1
	        j += 1
	return min_platform

# Driver code

# arrival = [100, 140, 150, 200, 215, 400] 
# departure = [110, 300, 220, 230, 315, 600]
arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arrival)
a = findPlatform(arrival, departure, n)
print(a)