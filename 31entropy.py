#this only works for a list of numbers.
import sys
import math      #if I run this script or program,
                #if I add arguments to command line
probs = []     #will only work if I use numbers.
for arg in sys.argv[1:]: #only one string in list , but using slice or REVEAL part of a string, or in this case REVEAL each string starting from one to all strings.
	f = float(arg)      #can't convert string into floating point number? unless an iteration number. I guess is from sq bracket earlier.
	if f <= 0 or f >= 1: #each argument I use should be in this interval or else get error message.
		sys.exit('error: not a probability')
	probs.append(float(arg)) #each argument I added, will be added to probs list.
	
total = 0
for p in probs:
	total = total + p #if p is a number in list then will add up like a sum.
if not math.isclose(total, 1.0):
	sys.exit('error: probs must sum to 1.0')
	            #if we have a list of numbers, then p should equal it's number value
h = 0           #but p can still have value if a number
for p in probs: #for item in container:
	h = h - p*math.log2(p) 
	
print(f'{h:.4f}') # we will format h to have 
				   # 4 places after decimal point.

# I tried:
# python3 31entropy.py 0.5 0.5
# python3 31entropy.py 0.25 0.25 0.25 0.25
# python3 31entropy.py 0.4 0.3 0.2 0.1
# python3 31entropy.py 0.5 0.6 error, doesn't sum to 100%
# python3 31entropy.py 0.5 -1  error, have one value less than zero
# python3 31entropy.py 0.1667 0.1667 0.1667 0.1667 0.1667 0.1667
#for dice but having issues because total not close enough to one. so error message.

