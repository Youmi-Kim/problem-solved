import sys
input = sys.stdin.readline

N = int(input())

def fac(i):
	if i == 0 or i == 1:
		return 1
	return i * fac(i-1)

print(fac(N))