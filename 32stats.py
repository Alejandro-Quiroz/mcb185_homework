#32stats.py by Alejandro Quiroz

import math
import random
import sys

#even sample
def if_even(n):
	if n % 2 == 0:
		return True
	else: 
		return False

#odd sample
def if_odd(n):
	if n % 2 != 0:
		return True
	else:
		return False

		                #sys.argv is a list of one string
data = []          #use list of numbers
for i in sys.argv[1:]:  #can add numbers in terminal or command line
	f = float(i)       #will use each number argument added in command line to become added to list as a floating point number.
	data.append(f) #I will add each number added, into list called data
		# no need for if statement
		# since no need to specify the kind of numbers
		# to report error message with sys.exit('error, not a prob!')

dev_sq_sum = 0
sum = 0
for iteration in range(len(data)):
	sum = sum + data[iteration]
	mean = sum / len(data)
	
for iteration in range(len(data)):
	#std_avg = sqrt of everything: sum(x-avg)**2 / n-1
	dev_sq = (data[iteration] - mean)**2
	dev_sq_sum = dev_sq_sum + dev_sq
std = math.sqrt(dev_sq_sum/((len(data))-1))

min_value = data[0] 
max_value = data[0] 
data.sort()
for j, k in enumerate(data): 
	#z-score = data_point - avg / std
	z_score = data[j] - mean / std
	print(j,k,'z_score=',z_score)	
	#z_score is something you print as you go or iterate
	#print within loop to get all z_scores.
	
	if k < min_value:  
		min_value = k
	if k > max_value:
		max_value = k
	#I can also use sort method
	# data.sort() and give index zero
	# data.sort(reverse=True) and give index zero
	
	#median: if odd n, then display middle number
	#	((n+1)/2)th number
	#median: if even n, then avg of both middle numbers
	#	[ ((n+1)/2)th number + ((n+1)/2)th number ] / 2
	if if_odd(len(data)):
		number_th = int((len(data)) / 2)
		median = data[number_th]
	else: 
		number_th_first = int((len(data)/2))
		number_th_second = int((len(data)/2 + 1))
		median = (data[number_th_first - 1] + data[number_th_second - 1]) / 2


#adding N50 Contig is a consensous sequence of some length.
#we start with the longest and move towards smallest
#until we reached half of total sum as a position.
data.sort(reverse=True)
sum=0
for i in range(len(data)):
	sum = sum + data[i]
halfway = sum/2

total = 0
for dat in data:
	total = total + dat
	if total > halfway:
		print('N50=',dat,'with sum of',total)
		break

print('sample size=',j+1) #to print final calculation.
print('min_value=',min_value)
print('max_value=',max_value)
print('mean=',mean)
print('std=',std)
print('median=',median)
#print('N50=',dat)
#printing a mode would be fun.

#python3 32stats.py 1 2 3 4 5 4 3 
# in command line