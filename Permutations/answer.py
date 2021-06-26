n = int(input())

# No solutions for 2 and 3
if 2 <= n <= 3:
	print("NO SOLUTION")

else:
	evens = list(range(1, n + 1))[1::2]
	odds = list(range(1, n + 1))[::2]

	# Prints all evens, then odds
	print(*evens, *odds)
