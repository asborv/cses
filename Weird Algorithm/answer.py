n = int(input())
l = []

while n != 1:
	l.append(int(n))
	n = n / 2 if n % 2 == 0 else \
			n * 3 + 1

l.append(int(n))
print(*l)
