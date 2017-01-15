# Uses python3
n = int(input())
if n==0:print('0')
elif n==1: print('1')
else:
	A=[0,1]
	for i in range(2,n+1):
		A.append((A[i-1]+A[i-2])%10)
	print(sum(A)%10)
