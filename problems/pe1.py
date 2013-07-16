def main(cap):
	ans = 0
	for i in range(cap):
		if i % div_1 == 0 or i % div_2 == 0:
			ans += i
	return ans