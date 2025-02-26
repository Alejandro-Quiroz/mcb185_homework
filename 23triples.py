
import random
import math
def pythagorean_triples(a,b):
	c = math.sqrt(a**2 + b**2)
	return c
print(pythagorean_triples(3,4))

#for i in range


limit = 100
for a in range(1,limit):
	for b in range(a+1,limit):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0: print(a,b,c)
		#only works if if statement out here.

