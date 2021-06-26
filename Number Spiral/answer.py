t = int(input())
l = []

for i in range(t):
	# y and x coordinates
	y, x = (int(n) for n in input().split())

	# Primary is max of x and y
	p, s = (y, x) if y >= x else (x, y)

	# Initial value
	v = 0

	# Adds initial of primary, then adds, subtracts secondary
	# x and y behaves identically for odd VS even
	if (p == x and p % 2) or (p == y and not p % 2):
		v += p**2
		v -= s - 1
	else:
		v += (p - 1)**2 + 1
		v += (s - 1)

	l.append(v)

print(*l, sep="\n")
