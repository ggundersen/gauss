import gmath as g

def pe2():
	return ''

def magic(divisor):
	fgen = g.gen_fibonacci()
	result = []
	for i in range(300):
		f = fgen.next()
		if f % int(divisor) == 0:
			b = list(bin(f)[2:])
			result.append(b)
	return result
