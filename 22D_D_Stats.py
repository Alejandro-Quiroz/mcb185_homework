#avg for each stat is 10.5 or 3.5 for each dice

#roll 3 six-sided dice
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
for func, name in zip(funcs, names):
	total = 0
	for i in range(trials): total = total + func()
	print(name, total/trials, sep='\t')
