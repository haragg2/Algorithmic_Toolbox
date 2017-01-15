# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
	value = 0
	dat={weights[i]:(values[i]/weights[i]) for i in range(len(values))}
	while capacity>0 and dat :
		maxi=max(dat, key=dat.get)
		if maxi<capacity:
			value+=maxi*dat.get(maxi)
			capacity-=maxi
		else:
			value+=capacity*dat.get(maxi)
			capacity-=capacity
		del dat[maxi]
	return value
if __name__ == "__main__":
	data = list(map(int, sys.stdin.read().split()))
	n, capacity = data[0:2]
	values = data[2:(2 * n + 2):2]
	weights = data[3:(2 * n + 2):2]
	opt_value = get_optimal_value(capacity, weights, values)
	print("{:.4f}".format(opt_value))
