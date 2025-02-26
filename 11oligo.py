def mT(A, C, G, T):
	S = A + C + G + T
	if A < 0 or C < 0 or G < 0 or T < 0:
		return 'not possible'
	elif S <= 13 and S > 0: 
		return (A + T)*2 + (G + C)*4
	elif S > 13: 
		return 64.9 + 41*(G + C - 16.4) / (A+T+G+C)
	else:
		return None
print(mT(10,20,30,40))
print(mT(1,2,3,4))
print(mT(0,1,0,0))
print(mT(0,0,0,0))
print(mT(-2,2,4,4))
print(mT(-1,20,30,40))