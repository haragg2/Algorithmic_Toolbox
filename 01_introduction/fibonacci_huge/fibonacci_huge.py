# Uses python3
n, m = map(int, input().split())
period=1
if n==0:print('0')
elif n==1: print('1')
else:
	A=[0,1]
	for i in range(2,n+1):
		A.append((A[i-1]+A[i-2])%m)
		if A[i-1]==0 and A[i]==1:
			period=i-1
			break
	if period!=1:print(A[n%period])
	else:print(A[n])
