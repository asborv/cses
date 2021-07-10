# Base case, n = 1
a0 = ["0", "1"]
n = int(input())

# Recursive algorithm:
# link: https://en.wikipedia.org/wiki/Gray_code#Constructing_an_n-bit_Gray_code 

def gray_code(n, l=a0):
	# Base case
	if n == 1:
		return l

	# Continue until all pemutations are covered
	elif len(l) != 2**n:
		a1 = ["0" + s for s in l]
		a2 = ["1" + s for s in l[::-1]]

		return gray_code(n, a1 + a2)

	return l

print(*gray_code(n), sep="\n")
