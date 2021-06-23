n = int(input())
l = [int(x) for x in input().split()]
total = 0
i = 0

while True:
	if i == 0:
		i += 1
		continue

	try:
		if l[i] < l[i - 1]:
			d = l[i - 1] - l[i]
			total += d
			l[i] += d
	except IndexError:
		break

	i += 1

print(total)
