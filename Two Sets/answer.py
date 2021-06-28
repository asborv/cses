from itertools import chain

n = int(input())
a, b = [], []

# Not possible if arithmetic sum is odd
if ((n * (n+1))/2) % 2:
	print("NO")
else:
	print("YES")

	# Manually sets (1, 2) and (3) if n is odd
	should_fix_123 = n % 2

	# n is even: pairs from min and max converging on middle
	if not should_fix_123:
		l = [(r, n - r + 1) for r in range(1, int(n/2 + 1))]

	# Same as above, but start at 4
	else:
		l = [(r, n - i) for i, r in enumerate(range(4, n + 1))]
		
		# Halves the list as the above comprehension generates a 2x all the pairs
		l = l[:len(l)//2]

		# Manually add (1, 2) and (3)
		a.append((1, 2))
		b.append((3,))

	# Half of l in a and b
	a.extend(l[len(l)//2:])
	b.extend(l[:len(l)//2])

	# Flatten lists
	a = list(chain(*a))
	b = list(chain(*b))

	# Output
	print(len(a))
	print(*a)
	print(len(b))
	print(*b)
