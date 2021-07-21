# Write the function fun_threelines_area(d1, d2, d3) 
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.

import math

def fun_threelines_area(a, b, c):
	v = (a+b+c)/2
	g = math.sqrt(v*(v-a)*(v-b)*(v-c))
	return int(g)
	
