# link https://math.stackexchange.com/questions/3266257/number-of-ways-two-knights-can-be-placed-such-that-they-dont-attack/3266324

n = int(input())

for k in range(1, n + 1):

	# Combinations on kxk board
	t = (k**2 * (k**2 - 1)) / 2
	
	# 2 x 2x3 and 3x2 board on kxk board
	m = 4 * (k - 1) * (k - 2)
	
	# Difference between combinations and attack positions
	print(int(t - m))
