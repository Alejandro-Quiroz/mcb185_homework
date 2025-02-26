
#24savingthrows by Alejandro Quiroz
'''
#1
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
#because the dc number order does not matter.
'''
'''
a = '"dc is 5"'
b = '"dc is 10"'
c = '"dc is 15"'
probability_of_success = 1/20
o = 15/20
p = 10/20
q = 5/20
for i in range(4):
	if i == 0:
		print('status',a,b,c)
	if i == 1:
		print('normal',o,p,q)
	if i == 2: 
		r = o + o 
		s = p + p 
		t = q + q
		print('with advantage',r,s,t)
	if i == 3:
		u = o ** 2
		v = p ** 2
		w = q ** 2
		print('with disadvantage',u,v,w)
'''
'''
#2
import math
import random
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
'''

'''
#3 for 3 separate functions
#24savingthrows.py into separate functions 
#each for normal,advantage,or disadvantage status.
import math
import random
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
'''


'''
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
'''

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
	