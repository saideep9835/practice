# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit=abs(digit)
	x = [int(i) for i in str(digit)]
	a = x[::-1]
	
	if k>len(a)-1:
		return 0
	return a[k]

	
