# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	d1 = (x2-x1)**2+(y2-y1)**2
	d2 = (x3-x2)**2+(y3-y2)**2
	d3 = (x3-x1)**2+(y3-y1)**2
	if(d2 == d1+d3 or d1 == d2+ d3 or d3 == d1+d2):
		return True
	else:
		return False
