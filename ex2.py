#ex2.py by Alejandro Quiroz

import random

points_inside = 0
total_points = 0
while True:
	x = random.random()
	y = random.random()
	total_points = total_points + 1
# we want to record if point lands in circle
	if y - x**2 >= 0:
		points_inside = points_inside + 1
		
	above_inside = (points_inside/total_points)
	print(above_inside)