# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2
def isPrime(n):
    if n <= 1:
        return False
  
   
    for i in range(2, n):
        if n % i == 0:
            return False
  
    return True
def ispalindrome(n):
	x = [int(i) for i in str(n)]
	b = x[::-1]
	if x == b:
		return True
	return False

def fun_nth_palindromic_prime(n):
	a=0
	b=0

	while(a<=abs(n)):
		b+=1
		if(isPrime(b) and ispalindrome(b)):
			a+=1
		
	return b