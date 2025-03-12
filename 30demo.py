
s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1,s2)

print('hey "dude" don\'t tell me what to do')

#concatenation
t = 'hello' + 'world'
print(t)
#repetition
polyA = 'A' * 100
print(polyA)

#'1' is less than '10' (as 'a' is less than 'ace')
#'2' is greater than '1000' (as 'b' is greater than 'ant')

n = 32
n1 = 33
n2 = 34
# i tried number,dec 1 or 2 or 3 
# but their ascii symbol is a button and displays nothing.
c = ' '
c1 = '!'
c2 = '"'
print(len(s))
print(chr(n)) #prints a space symbol
print(chr(n1))
print(chr(n2))
print(ord(c))
print(ord(c1))
print(ord(c2))

#most string operations use method syntax rather than function syntax.
#variable,dot,name of operation, then parenthesis.

# variable.FUNCTION or method syntax

a = 'h'
b = 'w'

s.count(s1)
print(s.count(s1))

s.endswith(s1)
print(s.endswith(s1))

s.startswith(s1)
print(s.startswith(s1))

s.upper() #doesn't convert string, but rather returns a new copy that is all upper case.
print(s.upper()) 

s.lower()
print(s.lower())

s.rstrip()
print(s.rstrip()) #still don't know what does

s.replace(a, b)
print(s.replace(a,b))


#python strings are immutable, 
#meaning you can't change them.


print(s.replace('o', ''))
print(s.replace('o','').replace('r','i'))

import math
print(f'{math.pi}')
print(f'{math.pi:.3f}')
print(f'{1e6 * math.pi:e}')
print(f'{"hello world":>20}')
print(f'{"hello world":.>20}')
print(f'{20:<10} {10}')

# f-strings , modern best way to format strings
# str.format() , old method
# printf-style , similar to or from C programing language

#indexes or ipe , index position extract
seq = 'GAATTC'
print(seq[0], seq[1]) #output has space inbetween for some reason.

print(seq[-1]) #indexes can be negative, they count backwars from the right of the string to the left.

print(seq[4], seq[5]) #if print 6, then will say error, index out of range.

for nt in seq:
	print(nt) #prints vertically of course.	
for nt in seq:
	print(nt)
print()        #does same,..., it ends the code.

for nt in seq: #nt and seq are variables. seq is also a container.
	print(nt, end='') #this will force no spaces between outputs. So prints horizontally.
print()        #allows to not be part of next 3 outputs.
for nt in seq:
	print(nt, end='')
#prints horizontally and no spaces between outputs.
#I just want to see, how looks, in different order.
for nt in seq:
	print(nt, end='')
for nt in seq:
	print(nt, end='')
print() #did not print blank next line. overide by no space?
#okay, the last two For-Loops, joined horizontally no space !

#trying again in reverse order.
for nt in seq:
	print(nt, end='')
print() #allows a line space at end if no next output? Ends printing.
for nt in seq:
	print(nt, end='')
#both For-Loops seem to do the same thing.

#now I know why we print print() at end.
#To disconnect from the next code
# the code for no space inbetween.
for i in range(len(seq)): #got connect to latest For-Loop.
	print(i, seq[i])

for nt in seq: #just printing correct horizontal again.
	print(nt, end='')
print()

for i in range(len(seq)): #better version
	print(i, seq[i])      #prints vertically.

for i in range(len(seq)):  #not better version
	print(i, seq[i], end='') #prints horizontally but for outputs only, not for items being printed within print function.
print()                     #and there is space between i and seq[i] which is confusing.
for i in range(len(seq)):      #just showing
	print(i, seq[i], end=',')   #myself
print()                         #how bad
for i in range(len(seq)):       #the code
	print(i, seq[i], end=' , ')  #evolves
print()                        #with comma and space.


#slice is a subset of container.
s = 'ABCDEFGHIJ'
print(s[0:5])   # sq bracket to slice or REVEAL part of the string.

print(s[0:8:2]) #like range, 0 to 8, spaced by 2 numerically
print(s[0:9:3])

#prints first 5 letters 0,1,2,3,4 because 5 is max.
print(s[0:5], s[:5]) #if no number at begining of colon, assumes 0th position in string.
print(s[5:len(s)], s[5:]) # if no number at end of colon, assumes last position in string.

#last one goes backwards from J to A
print(s, s[::], s[::1], s[::-1])

dna = 'ATGCTGTAA'             #9 characters in string
for i in range(0, len(dna), 3): #9 iterations max or 9 outcomes or 9 runs    and     show a per 3 iterations.
	codon = dna[i:i+3] #starting point to max so 0,1,2  3,4,5  6,7,8
	print(i, codon)    # printing every possible codon here.

#back to tuples
tax = ('Homo', 'sapiens', 9606) #tuple can contain multiple outputs, values, and strings in parenthesis.
print(tax)

#s[0] = 'C'
#tax[0] = 'human'
# creates errors because you can't change tuples and strings.

#find inside the tuple or string or container.
print(tax[0])
print(tax[::-1])



nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])     #remember, sq bracket is for finding index inside string.

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)): # max 4 or 4 iterations or 0,1,2,3
	print(nts[i], names[i]) # these two i are different in refering to different For-Loops that label a specific tuple or string earlier.



#finally enumerate
for i, nt in enumerate(nts): # i refers to numerically what's inside string.
	print(i, nt)             # nt refers to non-numerically what's inside string.

#finally zip
for nt, name in zip(nts, names):
	print(nt, name) #skipping identifying numerical part
                    #identifying inside for each iteration aligned otherwise error if not exact alignment such as including uracil in names tuple.

#utilize 1st i numerically, then nt name non-numerically, and prints all 3 aligned.
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

                 #i'm starting to think
	#a container is a variable set to only one string.
	#a tupple is variable set to many, with parenthesis.
	#a list is variable set to many, with sq bracket.
	#the responsibility is to keep tupple or list:
	# as only one data type:
	# int or float or string or None or boolean expression question answer.


#tuples and strings are immutable. Cannot be changed
#lists (or containers?) are mutable. can be changed.
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
#oh i think containers (fundamental concept) such as tuple or list [char array or vector array]
#I think now container is just variable set to string
# sq bracket not needed
#but list definitely requires string.

nts.append('C')
print(nts)

last = nts.pop() #designates or targets last element in list.
print(last)     #and printing the removed element.

nts.sort() #can sort with int and floats, or just strings. not mixed.
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts #not creating a copy, but another name to same list since setting a new equals variable. Or extending equation.
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)
#can copy with list.copy()

# the list() function without arguments creates an empty list
items = list()
print(items)
items.append('eggs')
print(items)

stuff = [] # also can create empty list this way
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph) #breaks down string to many strings in list.
print(aas)        #tuple vs list

#split() and join()
text = 'good day          to you'
words = text.split() #was able to identify characters together separated by space.
print(words) #by default, the delimiter is any number of spaces.

#for TSV or CSV data, split on \t or comma
line = '1.41,2.72,3.14'
print(line.split(','))

#from list of strings, to back to one string
s = '-'.join(aas) #joins list of strings by dash to one string.
print(s)
s = ''.join(aas)   #joins list of strings to one string.
print(s)
# I noticed, before dot is one string use, and after function name is list use or strings use.
# the delimiter is what limits or separates things or characters or columns.

#for item in container:
# should be
#for item in items:
#or 
#for element in elements:
#this is because we have a string, and we are searching within string.
#we have a container; or a variable set to a string.
#searching items in containers by in , find() , index()
#really searching string in list of strings?X
if 'A' in alph: 
	print('yay')  #use first if don't know if element is in list or tuple.
if 'a' in alph: 
	print('no')    

print('is there index G?', alph.index('G')) #gives number
#print('is there index Z?', alph.index('Z')) #gives error because substring not found.

print('did we find G?', alph.find('G')) #gives number
print('did we find Z?', alph.find('Z'))  #gives -1 because substring not found.
# only works for string and not tuples or lists

print(chr(32)) #just to print ascii symbol space.


#practice problems 
#write function that returns min value of list

groceries = [ 'apple' , 'orange' , 'spinich', 'kale' , 'steak' ]
card_values = [ 'A' , 'K' , 'Q' , 'J' , '10' , '9' , '8' , '7' , '6' , '5' , '4' , '3' , '2' , '1' ]
bills = [ 500 , 400 , 100 , 200 , 300 ]
mixed0 = [ 3 , 3.1 , 2.1 , 10.1 ]
mixed1 = [ 4.1 , 4 , '1' , '5' ]
mixed2 = [ 5 , 5.1 , 'word' , 'anotherword' ]

probabilities0 = [0.2,0.3,0.5]
probabilities1 = [0,0.3,0.5]

#string
#container
#tupple
#list

def min_val_list(items):     #don't use word lists because can be confusing with concept list vs tuple.
	min = items[0]      #seems like, whether use string or list, indexing can still be applied.
	for item in items[1:]:   #index position extract , skipped zeroth iteration because already using it as variable to return.
# i in this new-For-Loop is not iteration, because using sq brackets , this For-Loop is indexing or extracting everything in list.
# so if list of word then will give 0th word.
# but if list of numbers then i will equal a number and will actually compare as numbers.
# sq bracket refers to indexing the string or list.
		if item < min:      
			min = item
	return min
	
print(min_val_list(groceries))
print(min_val_list(card_values))
print(min_val_list(bills))
print(min_val_list(mixed0))
#print(min_val_list(mixed0)) error cuz str and int use
#print(min_val_list(mixed2)) error cuz str and int use

#seems like, whether using string or list, indexing still can be applied.

#don't use built in functions min() max() sum()

#write function that returns both min and max values of list
def both_min_max(items):
	min = items[0]
	max = items[0]
	for i in items: # i is recognized as item and not an iteration number like 0 or 1 or 2 since this is a -For item in container-Loop.
		if i < min:
			min = i
		if i > max:
			max = i
	return min , max
print(both_min_max(groceries))
print(both_min_max(card_values))
print(both_min_max(bills))
print(both_min_max(mixed0))
#then why use sq bracket in first problem?
#lets try with max and both with sq bracket.
def max_val_list(items):
	max = items[0]
	for item in items: # each item has a value even if comparing strings as order or iteration position value. If just one letter, then alphabetical order or value.
		if item > max:
			max = item
	return max
print(max_val_list(groceries))
print(max_val_list(card_values))
print(max_val_list(bills))
print(max_val_list(mixed0))
def both_min_max2(elements):
	min = elements[0]
	max = elements[0] # just setting to something, will change after if conditions checks the real highest value.
	for element in elements[0:]:
		if element < min:
			min = element
		if element > max:
			max = element
	return min, max
print(both_min_max2(groceries))
print(both_min_max2(card_values))
print(both_min_max2(bills))
print(both_min_max2(mixed0))
#use sort method 
def min_of_list(items):
	items.sort()
	return items[0]
print(min_of_list(groceries))
print(min_of_list(card_values))
print(min_of_list(bills))
print(min_of_list(mixed0))
def max_of_list(items):
	items.sort(reverse=True)
	return items[0]
print(max_of_list(groceries))
print(max_of_list(card_values))
print(max_of_list(bills))
print(max_of_list(mixed0))
#but side-effect is re-ordering which user may not want.

#write function that returns mean of values of list.
def mean(list_of_numbers):
	total = 0
	for item in list_of_numbers:
		total = total + item
	return total / len(list_of_numbers)
#print(mean(groceries))    can't compute ouput of strings into string output.
#print(mean(card_values))  can't compute mean of strings into string output.
print(mean(bills))
print(mean(mixed0))




#write function that computes entropy of probability distribution.
import math 
def entropy(probs):
	h = 0
	for p in probs:
		if p != 0 and p <= 1:
			h = h - p * math.log2(p) #use neg log for positive output, so really adding.
	return h
print(entropy([0.2, 0.3, 0.5])) #more complex than coin toss but not by a lot.
print(entropy(probabilities0))
#print(entropy(probabilities1))




#more options with equal prob increases complexity or bits of info.
#if some options and not equally available then decreases complexity or bits of info 
#because polarized or no surprise or predictability increases for a particular option.
#typically, more options increases complexity or bit of info.

#write function that computes Kullback-Leibler distance between two sets of probability distributions.
#Kullback-Leibler distance
#relative entropy
#comparing histograms for probabilities
#distribution of P vs distribution of Q
#distance of prob Pi to prob Qi
# D(P//Q) = sum of i=1 to n , Pi*log2(Pi/Qi)
def KLD(P,Q):
	distance = 0
	for p, q in zip(P,Q):
		distance = distance + p*math.log2(p/q)
	return distance
p1 = [0.4,0.3,0.2,0.1]
p2 = (0.1,0.3,0.4,0.2)
print(KLD(p1, p2))

#sys.argv complete list of words on command line
# system argument vector
#must import sys
import sys
print(sys.argv[0]) #first word is this file name.
                   # or the name of my program.
#print(sys.argv[1]) gives error , list index out of range
#so no other argument in this list of one string.

print(sys.argv) #this is just one string in list; my file name.

#if i try running
#python3 30demo.py with additional arguments
#then will print each as string in list.

#built in functions int() and float() 
#can convert strings to those
i = int('42')
x = float('0.61803')
print(i*x)

x = float('hello') #cannot convert string into float, error.

#we do not go over assert, try , except , raise
# in MCB185
#for custom message in errors: use sys.exit()

# 31entropy.py     new program or script
# in separate file because just adding error messages
# to entropy calculation.
# but will only work for a list of numbers.

# Combination Comparisons when pairing

# +all-vs-all combination    (or 2-by-2 matrix) only works for pairing 2 things together or base of 2**x
# +allowing self-comparisons (or only half matrix with diagonal)
# +not allowing self comparisons (or half matrix with no diagonal)

for i in range(0, len(list)):
	for j in range(X, len(list)):

# using the same list twice
# to create graphical axis with same list
# or in other words... making a matrix

# the X indicates the starting point for your 2nd axis
# therefore, can create each of the 3 pairing comparisons
# X = 0     (for all combinations)
# or X = i  (for half matrix with diagonal)
# or X = i+1 (for half matrix without diagonal)

#32entropy.py , the better entropy code
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






#homework
#32stats.py
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

added = 0
'''
	added = added + data[j] #to splice or REVEAL index,position,extract
	mean = added/(j+1) # i didn't use data because data not necessarily a number, data is a list.
'''
#should I have separate loops for mean and std
#Or have loop within loop but need final mean or std
dev_sq_sum = 0
sum = 0
#For-Loops want to do last calc in outer loop, 
# priority calc inside inner loop.

for iteration in range(len(data)):
	sum = sum + data[iteration]
	mean = sum / len(data)
	
for iteration in range(len(data)):
	#std_avg = sqrt of everything: sum(x-avg)**2 / n-1
	dev_sq = (data[iteration] - mean)**2
	dev_sq_sum = dev_sq_sum + dev_sq
std = math.sqrt(dev_sq_sum/((len(data))-1))

#intitializing is supposed to be outside of loop.	
min_value = data[0] #just choosing arbitrary option from list
max_value = data[0] #for just creating variable 
for j, k in enumerate(data): #enumerate already knows the container needs to be numbered as iteration ,and identify everything inside with label.
	#z-score = data_point - avg / std
	z_score = (data[j] - mean) / std #standardizing avg at zero
	print(j,k,'z_score=',z_score)	
	#z_score is something you print as you go or iterate
	#print within loop to get all z_scores.
	

	if k < data[0]:     #X and compare or adjust later.
		min_value = k
	if k > data[0]:     #X wrong
		max_value = k
	#I can also use sort method
	# data.sort()
	# data.sort(reverse=True)
	
	#median: if odd n, then display middle number
	#	((n+1)/2)th number
	#median: if even n, then avg of both middle numbers
	#	[ ((n+1)/2)th number + ((n+1)/2)th number ] / 2
	if if_odd(len(data)):
		number_th = int((len(data) + 1) / 2)
		median = data[number_th - 1]
	elif if_even(len(data)):
		number_th_first = int((len(data)/2))
		number_th_second = int((len(data)/2 + 1))
		median = (data[number_th_first - 1] + data[number_th_second - 1]) / 2
	
print('sample size=',j+1) #to print final calculation.
print('min_value=',min_value)
print('max_value=',max_value)
print('mean=',mean)
print('std=',std)
print('median=',median)

#printing a mode would be fun.
#python3 32stats.py 1 2 3 4 5 6 7 8 9 10 9 9 9 9
#python3 32stats.py 1 2 3 4 5 6 7 8 9 10 9 9 9 9 9
# in commmand line

#second try with Max_value fixed!
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

added = 0
'''
	added = added + data[j] #to splice or REVEAL index,position,extract
	mean = added/(j+1) # i didn't use data because data not necessarily a number, data is a list.
'''
#should I have separate loops for mean and std
#Or have loop within loop but need final mean or std
dev_sq_sum = 0
sum = 0
#For-Loops want to do last calc in outer loop, 
# priority calc inside inner loop.

for iteration in range(len(data)):
	sum = sum + data[iteration]
	mean = sum / len(data)
	
for iteration in range(len(data)):
	#std_avg = sqrt of everything: sum(x-avg)**2 / n-1
	dev_sq = (data[iteration] - mean)**2
	dev_sq_sum = dev_sq_sum + dev_sq
std = math.sqrt(dev_sq_sum/((len(data))-1))

# 3 6 7 6
min_value = data[0] #just choosing arbitrary option from list
max_value = data[0] #for just creating variable 
for j, k in enumerate(data): #enumerate already knows the container needs to be numbered as iteration ,and identify everything inside with label.
	#z-score = data_point - avg / std
	z_score = data[j] - mean / std
	print(j,k,'z_score=',z_score)	
	#z_score is something you print as you go or iterate
	#print within loop to get all z_scores.
	
	if k < min_value:     #and compare or adjust later.
		min_value = k
	if k > max_value:
		max_value = k
		
	#I can also use sort method
	# data.sort()
	# data.sort(reverse=True)
	
	#median: if odd n, then display middle number
	#	((n+1)/2)th number
	#median: if even n, then avg of both middle numbers
	#	[ ((n+1)/2)th number + ((n+1)/2)th number ] / 2
	if if_odd(len(data)):
		number_th = int((len(data) + 1) / 2)
		median = data[number_th - 1]
	elif if_even(len(data)):
		number_th_first = int((len(data)/2))
		number_th_second = int((len(data)/2 + 1))
		median = (data[number_th_first - 1] + data[number_th_second - 1]) / 2
	#for median, must use sort!
print('sample size=',j+1) #to print final calculation.
print('min_value=',min_value)
print('max_value=',max_value)
print('mean=',mean)
print('std=',std)
print('median=',median)

#printing a mode would be fun.



#32stats.py with N50
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



#unit 3 paper assessment in class
import sys
import math      
'''             
list = []     
for arg in sys.argv[1:]: 
	f = float(arg)     
	if f <= 0 or f >= 1: 
		sys.exit('error: not a probability')
	list.append(float(arg))

sum = 0
for probability in list:
	sum = sum + probability
if not math.isclose(sum, 1.0):
	sys.exit('error: probs must sum to 1.0')
print(list)
'''

#create list of numbers 
# &
#and write function that checks if list is 
#part of normal probability distribution

probs = [0.5, 0.4, 0.1]

def is_prob(probs):
	for prob in probs:
		if prob < 0 or prob > 1:
			return False #want to return False to exit function, if return True then will end the function.
	sum = 0
	for prob in probs:
		sum = sum + prob
	return math.isclose(sum, 1.0)
	
print(is_prob(probs))



numbers = [5,15,10]
numberss = [1,2,4,3]

#create function for median
def calc_median(elements):

	elements.sort()
	
	mid_one = int(len(elements)/2)
	mid_two = int(len(elements)/2) + 1
	
	if len(elements) % 2 == 0:
		return (elements[mid_one-1] + elements[mid_two-1]) / 2
	else:
		return elements[int(len(elements)/2)]
			
print(calc_median(probs))
print(calc_median(numbers))
print(calc_median(numberss))

'''
dirty median
	elements.sort()
	return elements[len(elements)//2]
'''	

#33birthday.py
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared=0
for i in range(trials):
	birthday_list_of_23 = []
	
	for peep in range(people):
		bday = random.randint(0,days-1) #to include endpoints. But still 365 days.
		if bday in birthday_list_of_23:
			shared = shared + 1
			#print(bday, 'is duplicate birthday')
			break
		birthday_list_of_23.append(bday)
	#print(shared/trials,'for peep') #to watch grow.
	#print(shared, '=shared within 23 students')
	#print(len(birthday_list_of_23),'=length of bday list')
	#print(i, len(birthday_list_of_23))

print(shared/trials, 'for shared/trials')

#python3 33birthday.py 10000 365 23
#in commmand line

#34birthday.py
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


shared = 0

for i in range(trials):
	calendar = [0]*days
	for j in range(people):
		bday = random.randint(0,days-1) #includes endpoints. Want to start at zero to 354, together is 365 days or zeros, but want to include 0th iteration for indexing, positioning, extracting the 0th or first number in list.
		calendar[bday] = calendar[bday] + 1
		if calendar[bday] >= 2:
			shared += 1
			break
print(shared/trials)
# python3 34birthday.py 10000 365 23
# in command line


#35scoringmatrix.py 
import sys

nts = sys.argv[1]
matched = sys.argv[2]
mismatched = sys.argv[3]



print('   ', end='')          #3 space , no space
for nt in nts:
	print(nt, end='  ')        # 3 space end to form a sentence or line 
print()


for nt0 in nts:
	print(nt0, end=' ')                 # 1 space
	for nt1 in nts:       #once print A, before printing the next letter C, we need to print +1 -1 -1 -1 with a pattern of +1 changing towards rights.
		if nt0 == nt1:
			print(matched, end=' ')     # 1 space
		else:
			print(mismatched, end=' ')   # 1 space
	print('\n')
	
# python3 35scoringmatrix.py ACGT +1 -1
# in commmand line

#35scoringmatrix.py
#looks tighter
import sys

nts = sys.argv[1]
matched = sys.argv[2]
mismatched = sys.argv[3]

print('   ', end='')          #3 space , no space
for nt in nts:
	print(nt, end='  ')        # 3 space
print()

for nt0 in nts:
	print(nt0, end=' ')                 # 1 space
	for nt1 in nts:       #once print A, before printing the next letter C, we need to print +1 -1 -1 -1 with a pattern of +1 changing towards rights.
		if nt0 == nt1:
			print(matched, end=' ')     # 1 space
		else:
			print(mismatched, end=' ')   # 1 space
	print('\n', end='') #with end, allows no horizontal line spaces.	
# python3 35scoringmatrix.py ACGT +1 -1
# in commmand line

#assessment example
#create output that shows position, frame, codon separated by tabs.
nuc_seq = 'ATGCTGTAA'

for i in range(0,len(nuc_seq)-2): #so really 0 to 6, because 7 max, 7 iterations, 0-6, but doing +1 to start at 1 and end at 7.
	reading_frame = (i % 3) + 1
	codon = nuc_seq[i:i+3]
	print(i+1,reading_frame, codon, sep='	') # if i print ,end='   ' then will seperate each output by 3 spaces consistenctly, like in a sentence.
	#but ,sep='tab' allows me to just seperate every output or iteration with tab as or for their own each line in output terminal.
#this neutral looks better, to print vertically
#i also need i to start at zero
#so i can use i = 0 for starting codon 

#assessment unit 3
import math
def is_prob(list_of_probs):
	for prob in list_of_probs:
		if prob < 0 or prob > 1:
			return False
	sum = 0
	for prob in list_of_probs:
		sum = sum + prob
	return math.isclose(sum, 1.0):

