from itertools import permutations

s, k = input().split()

s = sorted(s)
k = int(k)

for permutation in permutations(s, k):
    print("".join(permutation))
