# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isPrime(n):
    if n <= 1:
        return False
  
   
    for i in range(2, n):
        if n % i == 0:
            return False
  
    return True
def ishappynumber(n):
	# your code goes here
	c=0
	while(n!=0):
		c += (n%10)**2
		n=n//10

	if c==1:
		return True
	elif c<10:
		return False
	else:
		return ishappynumber(c)
def fun_nth_happy_prime(n):
	a=0
	b=0

	while(a<=abs(n)):
		b+=1
		if(ishappynumber(b) and isPrime(b)):
			a+=1
		
	return b