from itertools import combinations
n = int(input())
s = input().split()
k = int(input())
l = len(list(combinations(s, k)))
counter = 0
for i in list(combinations(s, k)):
    if 'a' in i:
        counter += 1
print(counter/l)
