# Uses python3
import sys

def get_change(m):
	if m==1 or m==5 or m==10:return 1
	A=[1,5,10,m]
	chg=0
	A.sort()
	i=A.index(m)-1
	while i>=0:
		if A[i]<=m:
			chg+=m//A[i]
			m=m%A[i]
		i-=1
	return chg
	
if __name__ == '__main__':
	m = int(sys.stdin.read())
	print(get_change(m))
