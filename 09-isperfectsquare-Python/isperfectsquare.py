# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math
def isperfectsquare(n):
	# your code goes here
	if type(n)==str:
		if n.isdigit():
			n=int(n)
			a = math.sqrt(n)
			b = a*a	
			if b==n:

				return True
	if type(n)==int and n>0 :
		a = math.sqrt(n)
		b = a*a
		if b==n:

			return True
		return False
	# elif  type(n)== str or n<0 or type(n)==float :
	return False

	
