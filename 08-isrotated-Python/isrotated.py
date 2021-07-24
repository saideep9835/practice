# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	n=len(str1)
	for i in range(-1,n):
		str1=str1[i:] + str1[:i]
		if(str1 == str2):
			return True
	return False