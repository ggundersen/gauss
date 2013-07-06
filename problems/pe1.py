def pe1():
	result = 0
	for i in range(1000):
		if i % 3 == 0 or i % 5 == 0:
			result += i
	return result

def magic():
	threes = []
	fives = []
	for i in range(5000):
		if i % 3 == 0:
			threes.append(i)
		if i % 5 == 0:
			fives.append(i)

	return [threes, fives]
