for i in range(1,101):
	if i % 3 == 0 and i % 5 != 0: print('Fizz')
	if i % 5 == 0 and i % 3 != 0: print('Buzz')
	if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
	if i % 3 > 0 and i % 5 > 0: print(i)

# or 

# write fizzbuzz fast
for i in range(1,101):
	if i % 3 == 0 and i % 5 != 0: print('Fizz')
	if i % 5 == 0 and i % 3 != 0: print('Buzz')
	if i % 3 == 0 and i % 5 == 0: print('FizzBuzz')
	if i % 3 != 0 and i % 5 != 0: print(i)