# -*- coding: UTF-8

s = input()
o = {}

for char in s:
	# link https://stackoverflow.com/questions/1692388/python-list-of-dict-if-exists-increment-a-dict-value-if-not-append-a-new-dic
	o[char] = o.get(char, 0) + 1

if not len(s) % 2:
	print("Lengde pÃ¥ s partall")
	if not any([x % 2 for x in o.values()]):
		print("Alle verdier partall")
		
		# Costruct first half of solution
		sol1 = "".join([k * int((v/2)) for k, v in o.items()])

		# Second half is first half reverse
		sol = sol1 + sol1[::-1]
		print(sol)
	
	else:
		print("Noen verdier har oddetal. Ikkje mulig lÃsning.")
		print("NO SOLUTION")
else:
	print("Lengde pÃ¥s er oddetall")

	odds = dict(filter(lambda kv: kv[1] % 2, o.items()))
	evens = dict(filter(lambda kv: not kv[1] % 2, o.items()))

	# In the case where s has an odd length, the solutions requires 1 letter with odd records (to go in the middle)
	if len(odds) != 1:
		print("NO SOLUTION")
	else:
		sol1 = "".join([k * int(v/2) for k, v in evens.items()])
		sol = sol1 + list(odds.keys())[0] * list(odds.values())[0] + sol1[::-1]

		print(sol)
