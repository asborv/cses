n = int(input())

# All numbers from 1 to n (inclusive)
# TODO cache
S = {x for x in range(1, n + 1)}

s = {int(x) for x in input().split()}

print(*S.difference(s))
