# Uses python3
import sys

def gcd_euclidean(a, b):
	if a==0:return b
	elif b==0:return a
	else:
		x=min(a,b)
		y=max(a,b)
		z=y%x
		w=gcd_euclidean(x, z)
	return w
a, b = map(int, input().split())
print(gcd_euclidean(a, b))
