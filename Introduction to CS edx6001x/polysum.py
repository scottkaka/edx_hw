import math

def polysum(n,s):
	#The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    area = 0.25*n*(s**2)/math.tan(math.pi/n)
   #The perimeter of a polygon is: length of the boundary of the polygon-- sum of length of all sides
    perimeter = n*s
    return round(area + perimeter**2,4)