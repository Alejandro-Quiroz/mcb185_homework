
# 25deathsaves.py by Alejandro Quiroz
import random
import math

'''
#health = 100%
health = 0.99
while health < 1:
	health = health - 0.05
	print(health)
	if health <= 0:
		print(health, 'health=0')
		failure = 0
		success = 0
		for i in range(3):
			x = random.randint(1,20)
			if x < 10: failure = failure + 1
			else: success = success + 1
			
			if x == 1: 
				failure + 2
			if x == 20: 
				health = health + 1
				print('has revived')
	
			print(i,x,failure,success)
			if failure == 3:
				health = 1
				print('has died')
			if success == 3:
				print('stable but unconscious but alive')
		if failure != 3 and success !=3:
			print('next player turn')

prob_dies = (1/20)**3
prob_stabilizes = (1/2)**3
prob_revives = (1/20)**3

print('probability dies is',prob_dies)
print('probability stabilizes is',prob_stabilizes)
print('probability revives is',prob_revives)
'''

'''
trials = 1000
stable = 0
death = 0
revive = 0

for i in range(trials):
	success = 0
	failure = 0
	for i in range(5):
		roll = random.randint(1,20)
		if roll == 1: #exclusive
			failure += 2
		elif roll < 10: #exclusive
			failure += 1
		elif roll == 20: #exclusive
			revive += 1
			break
		else: success += 1
		if success == 3:
			stable += 1
			break
		elif failure >= 3:
			death += 1
			break 
print('probability of revive', revive/trials)
print('probability of stable', stable/trials)
print('probability of death', death/trials)
'''



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