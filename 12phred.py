# Q score
# Quality score
# PHRED score
# P is probability of an incorrect call
# 10**(Q/-10) = P 
# Q = -10 * (math.log10(P)) 
import math

def phred_to_error(symbol):
	q = ord(symbol) - 33
	
	P = 10**(q / -10)
	return P
print(phred_to_error('A'))
print(phred_to_error('0'))
print(phred_to_error('@'))
print(phred_to_error('!'))
print(phred_to_error('('))

def error_to_phred(p):
	q = -10 * (math.log10(p))
	i = int(q // 1) + 33
	return chr(i)
print(error_to_phred(0.0006))
print(error_to_phred(0.003))
print(error_to_phred(0.85))
print(error_to_phred(.50))
print(error_to_phred(.25))



'''
#ascii value to symbol
#us chr funct to find ascii symbol
# we also want to use simple symbols starting at ! which is 33 the lowest
print(chr(32)) #will result in space character
print(chr(33))
print(chr(34))

print(chr(48))
print(chr(49))
print(chr(50))

print(chr(58))
print(chr(59))
print(chr(60))

print(chr(64))
print(chr(65))
print(chr(66))

print(chr(97))
print(chr(98))
print(chr(99))

print(chr(127)) #says Del button but there's no output?

#ascii symbol to value
#use ordinance with one char string to calc decimal value or integer
print(ord(' '))
print(ord('!'))
print(ord('"'))
print(ord('#'))
print(ord('$'))
print(ord('%'))

print(ord('0'))
print(ord('1'))
print(ord('2'))

print(ord(':'))
print(ord(';'))
print(ord('<'))

print(ord('@'))
print(ord('A'))
print(ord('B'))

print(ord('a'))
print(ord('b'))
print(ord('c'))
'''