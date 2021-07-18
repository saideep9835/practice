# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	x = [int(i) for i in str(n)]
	x.sort()
	c = 0
	n = x[0]
	for i in x:
		a = x.count(i)
		if a>c:
			c = a
			n = i
	return n
