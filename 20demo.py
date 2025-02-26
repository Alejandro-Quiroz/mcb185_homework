
#unit-2-iteration
t = 1, 2 # this is a tuple, 
#variable that contains more than one value or output
print(t)
print(type(t), end=' ! \n')

person = 21, 'Steve', 57891.5 #name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y  # more than one output, tupple

print(midpoint(1,2,3,4))
m = midpoint(1,2,3,4) # m is now a tupple
mx, my = midpoint(1,2,3,4) # mx my unpacks the tuple
print(mx, my)

print(m) #same as print(midpoint(1,2,3,4)

print(m[0], m[1])

# while Loops
#while True:
#	print('hello') # will print infinite hello

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 0
while i < 3: # to set condition to not be infintie
	i = i +1
	print('hey', i)

i = 0
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)


for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)

for i in range(5): print(i)

#for i in range vs for item in container Loops
# in this unit, our containers are tuples
#variable, container, or tuple 
# inside are multiple values, outputs, functions, strings
basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
# this is a loop to output one string at a time in terminal
for i in range(len(basket)):
	print(basket[i])
# same output with length of numeric indices functions
# i for iteration? or run'th or execute function

for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else: print(i, 'is odd')

#21fizzbuzz.py
for i in range(1,101):
	if i % 3 == 0: print('Fizz')
	if i % 5 == 0: print('Buzz')
	if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
	if i % 3 > 0 and i % 5 > 0: print(i)


# triangular() sum of numbers from 1 to n
# n = 5
# 0+1+2+3+4+5=15
# range(#start, #not-reaching-max, #spaced)
def triangular(n):
	tri = 0
	for i in range(n+1): # i = #_of_runs
		tri = tri + i
	return tri
print(triangular(5))
# 0th_run: 0 + 0th_run
# 1st_run: 0 + 1st_run
# 2nd_run: 1 + 2nd_run
# 3rd_run: 3 + 3rd_run
# 4th_run: 6 + 4th_run
# 5th_run: 10 + 5th_run
print(triangular(10))
print(triangular(-10)) #range is max zero

#calc factorial of number !!!!!
def quadangular(n):
	if n == 0: return 1
	quad = n
	Limit = n-2 # to consider 0th calc and maxth calc
	m = n
	for i in range(Limit):
		m = m-1
		quad = quad * (m)
	return quad
print(quadangular(0))
print(quadangular(5))
print(quadangular(10))
print(quadangular(4))
print(quadangular(3))

def factorials(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
print(factorials(0))
print(factorials(5))
print(factorials(10))
print(factorials(4))
print(factorials(3))

#poisson
#computes Poisson probability of k events occuring with an expectation of n 
#n^k e^-n/k!
# i think normal distribution
# lambda = mean
# math.sqrt(mean) = z-score
# can ~ approximate
# example mean=50 math.sqrt(~49)=7=z-score standard deviation?
#import math
#def poisson(n, k):
#	return n**k * math.e**(-n / factorials(k))
#print(poisson(659,135))
#print(poisson(12,6))
#print(poisson(400, 485))


#solves n choose k
# n! / k!(n-k)!
def nchoosek(n, k):
	return factorials(n) / (factorials(k) * factorials(n - k))
print(nchoosek(659,135))
print(nchoosek(5,10))
print(nchoosek(10,5))

def nchoosekk(n, k):
	return quadangular(n) / (quadangular(k) * quadangular(n - k))
print(nchoosekk(659,135))
print(nchoosekk(5,10)) #got different number
print(nchoosekk(10,5))

#euler's number e
def eulerss(n):
	for i in range(n+1):
		e = (1 + 1/n)**n
	return e
print(eulerss(5))
print(eulerss(10))
print(eulerss(100))
print(eulerss(1000))

def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorials(n)
	return e
print(euler(5))
print(euler(10))
print(euler(100))
print(euler(1000))
# way better


#finding a prime number
def if_prime(x):
	for i in range(2,101):
		prime = x % i
		if prime == 0: print(x,'divisable by',i)
	return print(x,'is prime')
print(if_prime(3))
print(if_prime(9))
print(if_prime(21))
print(if_prime(53))

def is_prime(n):
	for den in range(2, n//2 +1):
		if n % den == 0: return False
	return True
print(is_prime(3))
print(is_prime(9))
print(is_prime(21))
print(is_prime(53))

# nilakantha , to switch loops back and forth
def nilakantha(limit):
	pi = 3
	for i in range(1, limit+1):
		n = 2 * i
		d = n * (n+1) * (n+2)
		if i % 2 == 0: pi = pi -4 / d
		else: pi = pi + 4 / d
	return pi 
print(nilakantha(5))
print(nilakantha(6))
print(nilakantha(10))

# tuple has parenthesis, container has sq brackets
import random
#random and math are modules you call forth.
for i in range(5):
	print(random.random()) # generates number 0 <= X < 1

for i in range(3):
	print(random.randint(1, 6)) # generates random integer between 1 and 6 and inclusive endpoints

random.seed(1) # holds first set of generated random numbers
print(random.random())
print(random.random())
random.seed(2) # holds second set of generated random numbers
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

# compound interest
# exponential interest
# e^-kt interest





#unit-2 assessment
import math
import random
def is_prime(n):
	for d in range(2, n//2 +1):
		r = n % d
		if r == 0: return False
	return True
for i in range(51, 0, -2):
	print(i, end="")
	if is_prime(i): print("*", end="")
	print() #if not, will print horizontally

# write fizzbuzz fast
# write fizzbuzz fast
for i in range(1,101):
	if i % 3 == 0 and i % 5 != 0: print(i,'Fizz')
	if i % 5 == 0 and i % 3 != 0: print(i,'Buzz')
	if i % 3 == 0 and i % 5 == 0: print(i,'FizzBuzz')
	if i % 3 != 0 and i % 5 != 0: print(i)

#avg for each stat is 10.5 or 3.5 for each dice
#without packaging in empty def functions
import random
a_total = 0
for i in range(3):
	a = random.randint(1,6)
	a_total = a + a_total
	print(i, a, a_total,)

b_total = 0
for i in range(3):
	b = random.randint(1,6)
	while b == 1: #just IF for once
		b = random.randint(1,6)
		# will skip while when not satisfied
		# loop within loop
	b_total = b + b_total
	print(i, b, b_total)
#otherwise will just print final i 
#if not in Loop Block

c_total = 0
for i in range(3):
	c = random.randint(1,6)
	r = random.randint(1,6)
	if r > c: c = r
	c_total = c + c_total
	print(i,c,c_total,r)

def minimum_number(d, e, f, g):
	if d <= e and d <= f and d <= g: return d
	if e <= f and e <= g: return e
	if f <= g: return f
	else: return g
d_total = 0
for i in range (3):
	d = random.randint(1,6)
	e = random.randint(1,6)
	f = random.randint(1,6)
	g = random.randint(1,6)
	d_total = d + e + f + g
	d_total2 = d_total - (minimum_number(d,e,f,g)) 
	print(i,d,e,f,g,d_total,d_total2)
	

#avg for each stat is 10.5 or 3.5 for each dice
#roll 3 six-sided dice
#since return needed for function,
#if return in Loop-Block
#then will only return first run calculation in a print later.
import random
def roll3d6():
	a_total = 0
	for i in range(3):
		a = random.randint(1,6)
		a_total = a + a_total
		return i, a, a_total
#sum avg for each dice manually than emperical statistic

#roll 3 six-sided dice but re-roll any 1 once
def roll3d6r1():
	b_total = 0
	for i in range(3):
		b = random.randint(1,6)
		if b == 1:
			b = random.randint(1,6)
		b_total = b + b_total
		return i, b, b_total

#roll a pair of six-sided dice 3x, take the max of roll
def roll3d6m2():
	c_total = 0
	for i in range(3):
		c = random.randint(1,6)
		r = random.randint(1,6)
		if c < r: c = r
		c_total = c + c_total
		return i,c,c_total,r

#roll 4 six-sided dice, drop lowest
def minimum_number(d, e, f, g):
	if d <= e and d <= f and d <= g: return d
	if e <= f and e <= g: return e
	if f <= g: return f
	else: return g
def roll4d6k3():
	d_total = 0
	for i in range(3):
		d = random.randint(1,6)
		e = random.randint(1,6)
		f = random.randint(1,6)
		g = random.randint(1,6)
		d_total = d + e + f + g
		d_total2 = d_total - (minimum_number(d,e,f,g)) 
		return i,d,e,f,g,d_total,d_total2

#functions don't print; they return something.
trials = 1000
#this is called Not-Hard-Coding
#because setting,assigning variables first outside
for func in (roll3d6, roll3d6r1, roll3d6m2, roll4d6k3):
	total = 0
	for i in range(trials):
		total = total + func()
	print(total/trials)


#avg for each stat is 10.5 or 3.5 for each dice
#roll 3 six-sided dice
#putting return outside the For-Loop;
#to return final calculation after # of runs
#which is inclusive of final sum of 3 dice rolls.
#and this only works if each function,
#returns only one output,value... not tupple or container.
import random
def roll3d6():
	a_total = 0
	for i in range(3):
		a = random.randint(1,6)
		a_total = a + a_total
	return a_total
#sum avg for each dice manually than emperical statistic

#roll 3 six-sided dice but re-roll any 1 once
def roll3d6r1():
	b_total = 0
	for i in range(3):
		b = random.randint(1,6)
		if b == 1:
			b = random.randint(1,6)
		b_total = b + b_total
	return b_total

#roll a pair of six-sided dice 3x, take the max of roll
def roll3d6m2():
	c_total = 0
	for i in range(3):
		c = random.randint(1,6)
		r = random.randint(1,6)
		if c < r: c = r
		c_total = c + c_total
	return c_total

#roll 4 six-sided dice, drop lowest
def minimum_number(d, e, f, g):
	if d <= e and d <= f and d <= g: return d
	if e <= f and e <= g: return e
	if f <= g: return f
	else: return g
def roll4d6k3():
	d_total = 0
	for i in range(3):
		d = random.randint(1,6)
		e = random.randint(1,6)
		f = random.randint(1,6)
		g = random.randint(1,6)
		d_total = d + e + f + g
		d_total2 = d_total - (minimum_number(d,e,f,g)) 
	return d_total2
		#if return is in For-Loop-Block then will 
		#return the first dice roll or 0th iteration

#functions don't print; they return something.
trials = 1000
for func in (roll3d6, roll3d6r1, roll3d6m2, roll4d6k3):
	total = 0
	for i in range(trials):
		total = total + func()
	print(total/trials)


#avg for each stat is 10.5 or 3.5 for each dice
#roll 3 six-sided dice
#this one actually works for every avg probability approximation
import random
def roll3d6():
	a_total = 0
	for i in range(3):
		a = random.randint(1,6)
		a_total = a + a_total
	return a_total
#sum avg for each dice manually than emperical statistic

#roll 3 six-sided dice but re-roll any 1 once
def roll3d6r1():
	b_total = 0
	for i in range(3):
		b = random.randint(1,6)
		if b == 1:
			b = random.randint(1,6)
		b_total = b + b_total
	return b_total

#roll a pair of six-sided dice 3x, take the max of roll
def roll3d6m2():
	c_total = 0
	for i in range(3):
		c = random.randint(1,6)
		r = random.randint(1,6)
		if c < r: c = r
		c_total = c + c_total
	return c_total

#roll 4 six-sided dice, drop lowest
def minimum_number(d, e, f, g):
	if d <= e and d <= f and d <= g: return d
	if e <= f and e <= g: return e
	if f <= g: return f
	else: return g
def roll4d6k3():
	d_total = 0
	for i in range(3):
		d = random.randint(1,6)
		e = random.randint(1,6)
		f = random.randint(1,6)
		g = random.randint(1,6)
		d_total = d + e + f + g
		d_total2 = d_total - (minimum_number(d,e,f,g)) 
	return d_total2
		#if return is in For-Loop-Block then will 
		#return the first dice roll or 0th iteration

#functions don't print; they return something.
trials = 1000
for func in (roll3d6, roll3d6r1, roll3d6m2, roll4d6k3):
	total = 0
	for i in range(trials):
		total = total + func()
	print(total/trials)
	#Outside For-Loop-Block to print final iteration 

trials = 1000
total = 0
for i in range(trials): total = total + roll3d6()
print(total/trials)
total = 0
for i in range(trials): total = total + roll3d6r1()
print(total/trials)
total = 0
for i in range(trials): total = total + roll3d6m2()
print(total/trials)
total = 0
for i in range(trials): total = total + roll4d6k3()
print(total/trials)

trials = 1000
funcs = (roll3d6, roll3d6r1, roll3d6m2, roll4d6k3)
names = ('3d6', '3d6r1', '3d6m2', '4d6k3')
#Loop for items in corresponding lists
for func, name in zip(funcs, names):
	total = 0
	for i in range(trials): total = total + func()
	print(name, total/trials, sep='\t')


# Pythagorean triples
import math
limit = 100
for a in range(1,limit):
	for b in range(a+1,limit):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0: print(a,b,c)

#Gregory-Leibniz series
#run endlessly
total = 0
total2 = 0
n = 0
while True:
	total = (-1)**(n) * 1/(1 + 2*n)
	n = n + 1
	total2 = total + total2 #self summation part
	pi = 4 * total2
	print(pi)	

#Gregory-Leibniz series
#run only 10 iterations
total = 0
total2 = 0
n = 0
while n <= 10:
	total = (-1)**(n) * 1/(1 + 2*n)
	n = n + 1
	total2 = total + total2 #self summation part
	pi = 4 * total2
	print(pi)

#Gregory-Leibniz series
#approximate pi to a level of precision then stops
#is considered cheating if use math.pi to reach precision
import math
total = 0
total2 = 0
n = 0
while True:
	total = (-1)**(n) * 1/(1 + 2*n)
	n = n + 1
	total2 = total + total2 #self summation part
	pi = 4 * total2
	print(pi)
#examine difference to print precision
	print(abs(pi - math.pi))
	if abs(pi - math.pi) < 0.00001:
		print('close enough')
		break
		#if no break,
		#then will continue calculating,printing forever.
#or if math.isclose(a, b): print('close enough')

#Gregory-Leibniz series
#use series to approximate pi
#stops after reaching some level of precision
#without using built-in pi
total = 0
total2 = 0
n = 0
pi_previous = 0
while True:
	total = (-1)**(n) * 1/(1 + 2*n)
	n = n + 1
	total2 = total + total2 #self summation part
	pi = 4 * total2
	print(pi,pi_previous)
	if abs(pi - pi_previous) < 0.00001:
		break
	pi_previous = pi


#24savingthrows.py
#0 or original bad code
import random
import math
print(random.randint(1,20))
fail = 'fail'
dc = 0
trials=100
for i in range(trials):
	success_x = 0
	success_y = 0
	success_z = 0
	for dc in range(5,16,5):
	#don't do... For-Loop if the number order does not matter
	#or if number going in order has no meaning
	#therefore, use dc as an input for a function
	#or create a separate For-Loop for each dc.
	#same with normal,advantage,disadvantage
	#there is no numerical order with this list
	#therefore use these terms as inputs for a function
	#or use these terms as separate For-Loop for each term
		if dc == 5:
			x = random.randint(1,20)
			if x<5:
				print(dc,x,fail)
			else:
				success_x = success_x + 1
				print(dc,x,'succeed',success_x)
		if dc == 10:
			y = random.randint(1,20)
			if y<10:
				print(dc,y,fail)
			else:
				success_y = success_y + 1
				print(dc,y,'succeed',success_y)
		if dc == 15:
			z = random.randint(1,20)
			if z<15:
				print(dc,z, fail)
			else:
				success_z = success_z + 1
				print(dc,z,'succeed',success_z)
	print(i,dc,'prob of success in dc of 5 is',success_x/trials)
	print(i,dc,'prob of success in dc of 10 is',success_y/trials)
	print(i,dc,'prob of success in dc of 15 is',success_z/trials)
#looks like too much info that's hard to follow
#because the dc number order does not matter in range.

#24savingthrows.py
#1 or basic
import random
import math
trials = 10000
success_dc5 = 0
success_dc10 = 0
success_dc15 = 0
for i in range(trials):
	roll = random.randint(0,20)
	if roll >= 5:
		success_dc5 = success_dc5 + 1
	if roll >= 10:
		success_dc10 = success_dc10 + 1
	if roll >= 15:
		success_dc15 = success_dc15 + 1
print('probability of success in dc5',success_dc5/trials, 16/20, sep=',')
print('probability of success in dc10',success_dc10/trials, 11/20, sep=', ')
print('probability of success in dc15',success_dc15/trials, 5/20, sep=' , ')

#24savingthrows.py 
#2 with function to package For-Loop
#and use difficulty_class and status as input
#parameters for the function.
trials=100
success = 0
failure = 0
#status
#advantage    = 3
#neutral      = 2
#disadvantage = 1
def saving_throws(dc,status):
	success = 0
	failure = 0
	theoretically = (20 - (dc - 1)) / 20
	for i in range(trials):
		roll1 = random.randint(1,20)
		roll2 = random.randint(1,20)
		if status == 1:
			if roll1 > roll2:
				roll1 = roll2
		elif status == 3:
			if roll1 < roll2: 
				roll1 = roll2
	
		if roll1 >= dc:
			success = success + 1
			print(i,dc,status,roll1,roll2, 'success', success/trials)
		else:
			failure = failure + 1
			print(i,dc,status,roll1,roll2, 'failure')
	print('probability of success is',success/trials, 'normally is', theoretically, sep=', ')
		#because is a function, in Loop, will print first iteration only
saving_throws(5,2)
saving_throws(10,2)
saving_throws(15,2)

#24savingthrows.py into separate functions 
#3 for normal,advantage,or disadvantage status.
trials=100
def sav_throw_norm(dc):
	success = 0
	failure = 0
	theoretically = (20 - (dc - 1)) / 20
	for i in range(trials):
		roll1 = random.randint(1,20)

		if roll1 >= dc:
			success = success + 1
			print(i,dc,roll1, 'success', success/trials)
		else:
			failure = failure + 1
			print(i,dc,roll1, 'failure')
	print('probability of success is',success/trials, 'normally is', theoretically, sep=', ')
		#because is a function, in Loop, will print first iteration only
sav_throw_norm(5)
sav_throw_norm(10)
sav_throw_norm(15)

trials=100
def sav_throw_adv(dc):
	success = 0
	failure = 0
	theoretically = (20 - (dc - 1)) / 20
	for i in range(trials):
		roll1 = random.randint(1,20)
		roll2 = random.randint(1,20)
		if roll1 < roll2:
			roll1 = roll2
			
		if roll1 >= dc:
			success = success + 1
			print(i,dc,roll1,roll2, 'success', success/trials)
		else:
			failure = failure + 1
			print(i,dc,roll1,roll2, 'failure')
	print('probability of success with adv is',success/trials, 'normally is', theoretically, sep=', ')
		#because is a function, in Loop, will print first iteration only
sav_throw_adv(5)
sav_throw_adv(10)
sav_throw_adv(15)

trials=100
def sav_throw_dis(dc):
	success = 0
	failure = 0
	theoretically = (20 - (dc - 1)) / 20
	for i in range(trials):
		roll1 = random.randint(1,20)
		roll2 = random.randint(1,20)
		if roll1 > roll2:
			roll1 = roll2
			
		if roll1 >= dc:
			success = success + 1
			print(i,dc,roll1,roll2, 'success', success/trials)
		else:
			failure = failure + 1
			print(i,dc,roll1,roll2, 'failure')
	print('probability of success with dis is',success/trials, 'normally is', theoretically, sep=', ')
		#because is a function, in Loop, will print first iteration only
sav_throw_dis(5)
sav_throw_dis(10)
sav_throw_dis(15)

#24savingthrows.py 
#4 function first, then For-Loop to use function
import random
trials=100
def saved(dc,status):
	success = 0
	failure = 0
	theoretically = (20 - (dc - 1)) / 20

	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if status == 'advantage':
		if roll1 < roll2:
			roll1 = roll2
	elif status == 'disadvantage':
		if roll1 > roll2: 
			roll1 = roll2

	if roll1 >= dc:
		return True
	return False
#or we could have included a unique function of the 3
#to use in each separate case in the double For-Loop.
for dc in range(5,16,5):
	print('dc:',dc)
	success_norm = 0
	success_adv = 0
	success_dis = 0
	for i in range(trials):
		if saved(dc,'normal'):
			success_norm += 1
		if saved(dc,'advantage'):
			success_adv += 1
		if saved(dc,'disadvantage'):
			success_dis += 1
	print('normal prob of success:',success_norm/trials)
	print('advantage prob of success:',success_adv/trials)
	print('disadvantage prob of success:',success_dis/trials)
	

#25deathsaves.py
import random
trials = 100000
stabilizes = 0
died = 0
revived = 0
for i in range(trials):
		success = 0
		failure = 0
		for turn in range(5):
			roll = random.randint(1,20) #roll is exclusive
			if roll == 1:
				failure = failure + 2
			elif roll == 20:
				revived = revived + 1
				break
			elif roll >= 10: 
				success = success + 1
			else: 
				failure = failure + 1

			if success == 3:
				stabilizes = stabilizes + 1
				break
			if failure >= 3:
				died = died + 1
				break
print('prob one dies:',died/trials)
print('prob one stabilizes:',stabilizes/trials)
print('prob one revives:',revived/trials)

#halfling person gets advantage
import random
trials = 100000
stabilizes = 0
died = 0
revived = 0
for i in range(trials):
		success = 0
		failure = 0
		for turn in range(5):
			roll = random.randint(1,20) #roll is exclusive
			roll2 = random.randint(1,20)
			if roll < roll2:
				roll = roll2
			if roll == 1:
				failure = failure + 2
			elif roll == 20:
				revived = revived + 1
				break
			elif roll >= 10: 
				success = success + 1
			else: 
				failure = failure + 1

			if success == 3:
				stabilizes = stabilizes + 1
				break
			if failure >= 3:
				died = died + 1
				break
print('prob halflings dies:',died/trials)
print('prob halflings stabilizes:',stabilizes/trials)
print('prob halflings revives:',revived/trials)

'''
import random
import math

def advantage:
	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if roll1 > roll2: return roll1
	return roll2
def disadvantage():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 < roll2: return roll1
	return roll2
	
trials = 1000000
dc = 5 #difficulty
sides = 6

for dc in range(1,7,1):
	nor = 0
	adv = 0
	dis = 0
	for i in range(trials):
		r1 = random.randint(1, sides)
		r2 = random.randint(1, sides)
		if r1 >= dc: nor += 1
		if r1 >= dc and r2 >= dc: dis +=1
		if r1 >= dc or r2 >= dc: adv +=1
	#print(i,roll)
	print(dc, nor/trials, dis/trials, adv/trials)
'''
'''
import random

trial = 5
die = 0
stable = 0
revive = 0

for i in range(trial):
	print('trial', i)
	failure = 0
	success = 0
	for i in range(5):
		r = random.randint(1,20)
		if r == 1: failure += 2
		elif r <= 9: failure += 1
		elif r <= 19: success += 1
		else: 
			revive += 1
			break
		if success == 3:
			stable += 1
			break 
		if failure >= 3:
			die += 1
'''





'''
import random
import math


x = random.random()
y = random.random()

print(x,y)

dis = math.sqrt(x**2 + y**2)
print(dis)
in_circle = dis <= 1
print(in_circle)

pi_appr = 0 # initializing
ins = 0
out = 0

while True:
	x = random.random()
	y = random.random()
	dis = math.sqrt(x**2 + y**2)
	in_circle = dis <= 1
	if in_circle:
		ins += 1
	else: out += 1
	pi_appr = ins / (ins + out) * 4 
	print(x, y, dis, in_circle,)
'''
'''
countin = 0
countout = 0

while True:
	dist = math.sqrt((random.random() 
'''
'''
import random
import math

ins = 0
out = 0

while True:
	x = random.random()
	y = random.random()
	d = math.sqrt(x**2 + y**2)
	if d <= 1: ins += 1
	tot += 1
	print()
'''

	
	
#for i in range(10):
	#if (random.random()**2 + random.random()**2)**0.5 <= 1: ins += 1
	#tot += 1
	#print(4 * ins/tot)
	#x = random.random()
	#y = random.random()
	#d = (x**2 + y**2)**0.5
	#print(x, y, d)
	#if d<= 1
	#else
'''	
import random
import math

def max_2d():
	r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	if r1 > r2: return r1
	return r2

n = 1000
total = 0
for i in range(n):
	r1 = random.randint(1, 6)
	if r1 == 1: r1 = random.randint(1, 6)
	r2 = random.randint(1, 6)
	if r2 == 1: r2 = random.randint(1, 6)
	r3 = random.randint(1, 6)
	if r3 == 1: r3 = random.randint(1, 6)
	total += r1 + r2 + r3
	#print(r1,r2,r3,total)
print(total / n)
'''
'''
import random
random.seed(25)
for i in range(10):
	print(random.random())
'''
'''
import random
def loaded_die():
	r = random.random()
	if r < 0.1: return 1
	if r < 0.2: return 2
	if r < 0.3: return 3
	if r < 0.4: return 4
	if r < 0.5: return 5
	return 6
	
for i in range(1000):
	print(random.guass())
'''

#sign = -1 
'''
toggle = True
for i in range(10):
	toggle = not toggle
	print(toggle)
	#print('+')


for i in range(10):
	n1 = i*2
	n2 = n1 +1
	n3 = 
'''