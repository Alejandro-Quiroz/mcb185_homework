
def is_prime(n):
	for den in range(2, n//2 +1):
		if n % den == 0: return False
	return True
	
def au(n):
	x = 51
	for i in range(1,n+1):
		x = x - 2
		if is_prime(n) == True:
			return x, '*'
	return x
print(au(51))