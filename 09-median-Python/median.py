# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	l = 0
	h = len(a)-1
	b = (h+l)//2
	if a == []:
		return None
	elif len(a)%2!=0:
		
		return a[b]
	else:
		return (a[b+1]+a[b])/2