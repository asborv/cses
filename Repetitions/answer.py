import re


s = input()

# Matches repeating A, C, G or T
pattern = r"(A+|C+|G+|T+)"

# Sorting key
by_length = lambda s: len(s)

# Finds all Repeating letter sequences and sorts them
m = re.findall(pattern, s)
m.sort(reverse=True, key=by_length)

print(len(m[0]))
