# -*- coding: UTF-8

s = input()
o = {}
sol = ""

for char in s:
	# Add new letters and increment existing ones
	# link https://stackoverflow.com/questions/1692388/python-list-of-dict-if-exists-increment-a-dict-value-if-not-append-a-new-dic
	o[char] = o.get(char, 0) + 1

# Even length string: all characters must have an even number of appearances
if not len(s) % 2 and not any([x % 2 for x in o.values()]):
		
		# Costruct first half of solution
		sol = "".join([k * int((v/2)) for k, v in o.items()])

		# Second half is first half reverse
		sol += sol[::-1]

# Odd length string
else:

	# Filter to characters with odd & even appearances
	odds = dict(filter(lambda kv: kv[1] % 2, o.items()))
	evens = dict(filter(lambda kv: not kv[1] % 2, o.items()))

	# In the case where s has an odd length, the solutions requires 1 letter with odd records (to go in the middle)
	if len(odds) == 1:
		sol = "".join([k * int(v/2) for k, v in evens.items()])
		sol += list(odds.keys())[0] * list(odds.values())[0] + sol[::-1]

print(sol if sol else "NO SOLUTION")
