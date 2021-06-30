from re import search
from functools import lru_cache
import sys

sys.setrecursionlimit(10**8)

@lru_cache(maxsize=None)
def factorial(m):
	"""Find the factorialn m! recursively."""
	return m * factorial(m - 1) if m else 1

# Cast to str and search for 0's in end of str
n = str(factorial(int(input())))
m = search("0+$", n)

print(len(m.group(0)) if m else 0)
