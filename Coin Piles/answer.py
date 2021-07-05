t = int(input())
ans = []

for i in range(t):
	# Parse a and b where a < b
	a, b = [int(x) for x in input().split()]
	if a > b: a, b = b, a

	# If not divisible by 3: no solution
	if (a + b) % 3:
		ans.append("NO")
		continue
	
	# For equal values divisible by 3, always solution
	if a == b:
		ans.append("YES")
		continue
	# Solutions of equation set	
	m = abs(int((2*b - a) / 3))
	n = abs(int((m - a) / 2))

	if b - 2*m - n == a - 2*n - m== 0:
		ans.append("YES")
	else:
		ans.append("NO")

print(*ans, sep="\n")
