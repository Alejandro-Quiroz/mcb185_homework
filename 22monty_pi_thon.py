import random
import math

points_inside = 0
total_points = 0
while True:
	x = random.random()
	y = random.random()
	total_points += 1
# we want to record if point lands in circle
	if math.sqrt(x**2 + y**2) <= 1:
		points_inside += 1
		
	finding_pi = 4 * (points_inside/total_points)
	print(finding_pi)
# multiplying by 4 because 
# generating x and y direction
# random.random() which is 0 to 1 on both axis
# or 1/4 of the graph
# otherwise
# if want a full circle and square
# use random.random(-1,1)