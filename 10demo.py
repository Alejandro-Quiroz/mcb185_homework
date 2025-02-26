# 10demo.py by alex q

print("hello, again") # greeting

"""
this is a multi-line comment
this unit is about calculations
"""

print(1.5e-2)
print(5+5)
print(5*4)
print(2**5)

print(1000000//3) #throws away remainder or gives rounded off to lowest whole number, integer divide

print(100%3) #remainder 1 as answer
print(10%4) # remainder 2
print(25%4) # remainder 1

print(((50+(5*10))/100)*100) #precedence 100.0
print(50+(5*10)) # 100


a=abs(-5)
b=pow(2, 5)
c=round(2.5555, ndigits=2)
print(a)
print(b)
print(c)

import math
x=100
y=2.71828
z=4
print(math.ceil(y)) # rounds answer up to whole number
print(math.floor(y)) # rounds answer down to whole number
print(math.log(y)) # is log base e
print(math.log2(z)) # is log base 2
print(math.log10(x)) # is log base 10
print(math.sqrt(z)) 
print(math.pow(x, z)) # x to the power y
print(math.factorial(z)) #factorial of integer z

# import math recognizes:
# math.e as 2.71828
# math.pi as 3.14159
# math.inf as infinity
# math.nan as not a number (0/0)

print(0.1*1) # will be 0.1
print(0.1*3) # prints the 17th decimal place as random number because that is the limit of floating point numbers

f = 3 #parameter of function as one input
g = 4 #parameter of function as another input
h = math.sqrt(f**2 + g**2)
print(h)
print(type(f), type(g), type(h), sep=', ', end='!\n') #why is back slash and letter n necessary?


#can also keep all in one line
def pythagoras(f, g):
	h = math.sqrt(f**2 + g**2)
	return h

print(h) #because already defined f and g earlier
hyp = pythagoras(3,4)
print(hyp)
print(pythagoras(3,4)) #with no h variable

def circle_area(r): return (math.pi * r**2)
print(circle_area(3))

def circle_circum(r): return (2 * math.pi * r)
print(circle_circum(4))

def sphere_surface_area(r): return (2*r * 2*math.pi*r)
print(sphere_surface_area(5))

def sphere_volume(r): return ((4/3)*r**3*math.pi)
print(sphere_volume(5))

def rectangle_area(w, h): return w * h
print(rectangle_area(2, 10)) #overide in h

def triangle_area(w, h): return rectangle_area(w, h) / 2
print(triangle_area(2, 10))

def fahrenheit_to_celsius(f): return (f-32)*(5/9)
print(fahrenheit_to_celsius(33))
def celsius_to_fahrenheit(c): return (c*(9/5))+32
print(celsius_to_fahrenheit(33))

def MPH_to_KPH(m): return m*(1.60934/1)
print(MPH_to_KPH(60))
def KPH_to_MPH(k): return k*(0.621371/1)
print(KPH_to_MPH(90))

#compute dna concentration from 0d260

#arithmetic mean of 3 numbers
def mean_of_three(i,j,k): return (i+j+k)/3
print(mean_of_three(1,2,3))
#what mattered most was at the return answer

#geometric mean of 3 numbers
def geometric_mean_of_three(l,m,n):
	return (l * m * n)**(1/3)
print(geometric_mean_of_three(3,3,3))

#harmonic mean of three numbers
def harmonic_mean_of_three(o,p,q):
	return 3 / (1/o + 1/p + 1/q)
print(harmonic_mean_of_three(4,4,4))

#distance between two points
def distance_between_two(x1,y1,x2,y2):
	return math.sqrt((y2-y1)**2 + (x2-x1)**2)
print(distance_between_two(3,2,5,6))
print(math.sqrt(20))
print(20**0.5)


s = 'hello world'
print(s, type(s), type(a), sep=', ', end=' !\n')
#otherwise next asnwer 4 is right after exclamation


#Boolean expressions or asking questions or equality symbols
i = 2
j = 2
k = 3
if i == j:
	print('i equals j')
	print(i, j)

def is_even(x):
	if x % 2 == 0: return True
	return False
print(is_even(2))
print(is_even(3))
print(is_even(4))

k = i == j
print(type(k))
print(k)
#overiding value of k and reading solving left to right

#if elif else
if i < j:
	print('i < j')
elif i > j:
	print('i > j')
else: 
	print('i == j')
#or
if i < j: print('i < j')
elif i > j: print('i > j')
else: print('i == j')

if i < j: print('i < j')
elif i <= j: print('i <= j')
elif i == j: print('this will never print!')

#chaining and or not
if i < j or i > j: print('all things being equal, i and j are not')
if i < j and i > j: print('you are living in a strange world')
if not False: print(True)

#floating point warning
l = 0.3
m = 0.1 * 3
n = 30 / 100
print(l)
print(m)
print(n)
if l < m: print('l < m')
elif l > m: print('l > m')
else: print('l == m')
print(abs(l - m)) # the 5 is the random generated number 5.5e-17
if abs(l - m) < 1e-9: print('close enough')
#built in function for python to compare two values as same or not
if math.isclose(l, m): print('close enough')
o = 3.1
p = 1 * 3.1
q = 310/100
print(o)
print(p)
print(q)

#string comparison by ascii code value
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')
#comparing variables if diff such as string, numeric integer whole, floating point number, boolean
#thus error
#a = 1
#s = 'G'
#if a < s: print('a , s')

#a variable can also equal or be a NoneType which is None.
def silly(m, x, b):
	y = m * x + b
print(silly(2, 3, 4))
#y is computed but no return built to compute a direct function


#write a function that determines if a number is integer
def determine_if_number_is_integer(z):
	y = z % 1
	if y == 0: return True
	else: return False
print(determine_if_number_is_integer(-4))
print(determine_if_number_is_integer(4.1))

#if letter doesn't match any nucleotide, return None
#adenosinie triphosphate, not adenine
#guanosine triphosphate, not guanine
#cytidine triphosphate, not cystine
#thymidine triphosphate, not thymine
def molecular_weigth_nucleotide_g_per_mole(x):
	if x == 'A': return 507.18
	elif x == 'C': return 483.156
	elif x == 'G': return 523.18
	elif x == 'T': return 482.168
print(molecular_weigth_nucleotide_g_per_mole('A'))
print(molecular_weigth_nucleotide_g_per_mole('A'))
print(molecular_weigth_nucleotide_g_per_mole('B'))
print(molecular_weigth_nucleotide_g_per_mole('D'))



def return_maximum_of_three_numbers(r,s,t):
	if r >= s and r >= t: return r
	if s >= t: return s
	else: return t
print(return_maximum_of_three_numbers(100,1000,10000))
r = 10**6
s = 10**9
t = 10**12
print(return_maximum_of_three_numbers(r,s,t))
print(return_maximum_of_three_numbers(10**15,10**18,10**21))
print(return_maximum_of_three_numbers(r,s,t))


#return sensitivity, specificity, F1 score
tp = 0.50
fp = 0.05
tn = 0.35
fn = 0.10
def sensitivity(tp,fn):
	u = (tp / (tp + fn))
	return u 
print(sensitivity(tp,fn))

def specificity(tn, fp):
	v = tn / (tn + fp)
	return v 
print(specificity(tn,fp))

precision = 0.3
sensitivity = 0.4
def F1_score(precision,sensitivity):
	w = 2 * precision * sensitivity / (precision + sensitivity)
	return w
print(F1_score(precision,sensitivity))


#return shannon entropy for nt counts
'''
H entropy calc bit of info or complexity
if more options and equally available
then increases complexity or bits of info.

if some options and not equally available
then complexity decreases or bits of info decrease
thus one option more predictable than others
therefore predictablility increases
thus then more polarized, no surprise.
'''

# na = number of a nucleotides
# nc = number of c nucleotides
# ng = number of g nucleotides
# nt = number of t nucleotides
# pa = probability a
# pc = probability c
# pg = probability g
# pt = probability t
# se = shannon entropy

na = 64
nc = 128
ng = 64
nt = 64
def shannon_entropy(na,nc,ng,nt):
	total = na + nc + ng + nt
	pa = na / total
	pc = nc / total
	pg = ng / total
	pt = nt / total
	se_a = 0 # initialization
	se_c = 0
	se_g = 0
	se_t = 0
	if na != 0:
		se_a = -(math.log2(pa)) * (pa)
	if nc != 0: 
		se_c = -(math.log2(pc)) * (pc)
	if ng != 0: 
		se_g = -(math.log2(pg)) * (pg)
	if nt != 0: 
		se_t = -(math.log2(pt)) * (pt)
		
	return se_a + se_c + se_g + se_t
print(shannon_entropy(a,c,g,t))
print(shannon_entropy(16,128,16,16))
print(shannon_entropy(256,256,256,256))
print(shannon_entropy(0,32,0,0))
print(shannon_entropy(0,0,1,1))


	
#def tm(a,c,g,t):
	#length = (g+c)*4 + (a+t)*2
	#if length <= 13:
		#return 5
	#elif length <= 30:
		#return 4
	##else:
		#return 3
		
#def mt(a,c,g,t):
	#length = (g+c)*4 + (a+t)*2
	#if length <=13: return (g+c)*4 + (a+t)*2
	#elif length < 13 and length <100:
		#return 64.9 + 41 * (g+c -16.4) / length
	#else: return 3


#print(tm(1,2,3,4))

'''
print(ord('A'))
print(ord('B'))

print(chr(55))
print(chr(56))
print(chr(57))
print(chr(60))
print(chr(61))
print(chr(62))




print(ord('7'))
print(ord(','))
print(ord('>'))

#def symbol_to_prob(c):
#	pass 0.001
	
	
#def prob_to_symbol(p):
#	pass
	
#print(symbol_to_prob('9'))
#print(prob_to_symbol(0.003))

print(ord('K'))
'''

def complement_DNA(nt):
	#result = None
	if nt == 'A': return 'T'
	if nt == 'C': return 'G'
	if nt == 'G': return 'C'
	if nt == 'T': return 'A'
	else: return None
print(complement_DNA('C'))
print(complement_DNA('A'))
print(complement_DNA('B'))
print(complement_DNA('G'))
print(complement_DNA('T'))

def determine_valid_prob(x):
	if x>=0 and x<=1:
		return True
	else:
		return False
print(determine_valid_prob(0.5))
print(determine_valid_prob(-0.75))
print(determine_valid_prob(1.1))


def maximum_number(a, b, c, d):
	if a>=b and a>=c and a>=d: return a
	if b>=c and b>=d: return b
	if c>=d: return c
	return d

print(maximum_number(10,20,30,40))
print(maximum_number(5,5,10,1))
print(maximum_number(10,100,101,102))

def minimum_number(a, b, c, d):
	if a <= b and a <= c and a <= d: return a
	if b <= c and b <= d: return b
	if c <= d: return c
	else: return d

print(minimum_number(10,20,30,5))
print(minimum_number(1,4,0,5))
print(minimum_number(6,0,1,-2))

#Jaden's code
def low4(a,b,c,d):
	low = a
	if b < low: low = b
	if c < low: low = c
	if d < low: low = d
	return low
print(low4(1,2,3,4))
print(low4(4,3,2,1))
print(low4(2,3,4,1))

#one_star = 0.1 = 49
#two_star = 0.01 = 50
#three_star = 0.001 = 51
#four_star = 0.0001 = 52
#five_star = 0.00001 = 53

#star(ascii symbol), prob, ascii-value, quality-score (can be any number really, just have to associate it in mathematical function or relation to desired output)

import math
#remember that 5 stars (character) 
# is different from 5 (numerical value)
#  need to convert 5 symbol into number
# then convert number into right number 
# use number to convert into prob
def char_prob(stars):
	q = ord(stars) - 48 #53-48
	p = 10**-(q)         #10**-(5)
	return p
print(char_prob('5'))
print(char_prob('6'))



# convert prob to quality score
# quality score to ascii value
# ascii value to ascii symbol
def prob_char(prob):
	q = -math.log10(prob)
	asciiv = int(q//1) + 48 #cuz #//1 stills gives number throws away remainder but still has that #.0 or floating point number or decimal number
	char = chr(asciiv)
	return char
print(prob_char(0.01))

# what matters is the synonymous mathematical relation to go forward or backward
# 10**-x and -math.log10(p)
# or 
# 10**-q/10 and -10*math.log(p)
print(10**-3.5)
print(-10 * math.log10(0.00042))
print(-math.log10(0.01))
print(ord('5'))


# unit-1-assessment
#one_star = 0.1 = 49
#two_star = 0.01 = 50
#three_star = 0.001 = 51
#four_star = 0.0001 = 52
#five_star = 0.00001 = 53

#star(ascii symbol), prob, ascii-value, quality-score (can be any number really, just have to associate it in mathematical function or relation to desired output)

import math
#remember that 5 stars (character) 
# is different from 5 (numerical value)
#  need to convert 5 symbol into number
# then convert number into right number 
# use number to convert into prob
def char_prob(stars):
	q = ord(stars) - 48 #53-48
	p = 10**-(q)         #10**-(5)
	return p
print(char_prob('5'))
print(char_prob('6'))



# convert prob to quality score
# quality score to ascii value
# ascii value to ascii symbol
def prob_char(prob):
	q = -math.log10(prob)
	asciiv = int(q//1) + 48 #cuz #//1 stills gives number throws away remainder but still has that #.0 or floating point number or decimal number
	char = chr(asciiv)
	return char
print(prob_char(0.01))
print(prob_char(0.0015))

# what matters is the synonymous mathematical relation to go forward or backward
# 10**-x and -math.log10(p)
# or 
# 10**-q/10 and -10*math.log(p)