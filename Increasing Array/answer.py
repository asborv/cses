n = int(input())
l = [int(x) for x in input().split()]
total = 0

for i, x in enumerate(l):
	print(l)
	print(f"Observerer {x} og {l[i + 1]}")
	print(f"Indeks er: {i}")
	try:
		if x > l[i + 1]:
			print(f"{x} er stÃrre enn {l[i + 1]}")

			d = x - l[i + 1]
			total += d

			print(f"Differansen er {d}")
			print(f"Totalen er no: {total}")
			
			# BUG: Mutates wrong index
			l[i + i] = x

	except IndexError:
		print(f"{i} out of range")
		break
	print()
