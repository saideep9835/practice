# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2



import math


def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True  # Special Case
    elif n % 2 == 0:
        return False
    else:
        for factor in range(3, math.floor(math.sqrt(n) + 1), 2):
            if n % factor == 0:
                return False
        return True

def s(n):
    x = [int(i) for i in str(n)]
    a = sum(x)
    if isPrime(a):
        return True
    return False
def isadditive(n):
    if isPrime(n) and s(n):
        return True
    return False
def fun_nth_additive_prime(n):
	a=0
	b=1

	while(a<=abs(n)):
		b+=1
		if(isadditive(b)):
			a+=1
		
	return b
	