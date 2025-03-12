
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

shared=0
for i in range(trials):
	birthday_list_of_23 = []
	
	for peep in range(people):
		bday = random.randint(1,days) #to include endpoints.
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

	
	



'''
birthday_list = []
student = []

for i in range(trials):
	bday = random.randint(1,365)
	if bday != i:
		birthday_list.append(bday)
'''




'''
birthday_list = []
students = []

#for item in container:
#for item in items:
for arg in sys.argv[1:]: #a list with only one string; my file name.
	birthday_list.append(arg)


trials_students = 23
for i in range(trials_students):
	for j, (student, bday) in enumerate(zip(students, birthday_list):
		bday = random.randint(1, 365)
		if i 
	birthday_list.append(bday)
'''