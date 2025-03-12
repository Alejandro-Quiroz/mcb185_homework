import sys

nts = sys.argv[1]
matched = sys.argv[2]
mismatched = sys.argv[3]



print('   ', end='')          #3 space , no space
for nt in nts:
	print(nt, end='  ')        # 3 space
print()


for nt0 in nts:
	print(nt0, end=' ')                 # 1 space
	for nt1 in nts:       #once print A, before printing the next letter C, we need to print +1 -1 -1 -1 with a pattern of +1 changing towards rights.
		if nt0 == nt1:
			print(matched, end=' ')     # 1 space
		else:
			print(mismatched, end=' ')   # 1 space
	print('\n', end='') #with end, allows no horizontal line spaces.
	
# python3 35scoringmatrix.py ACGT +1 -1
# in commmand line


	