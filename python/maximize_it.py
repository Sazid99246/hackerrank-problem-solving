from itertools import product

K, M = map(int, input().split())
all_list = list()
for _ in range(K):
    all_list.append(list(map(int, input().split()))[1:])

S_max = 0
for item in set(product(*all_list)):
    S = sum(x**2 for x in item) % M
    if S > S_max:
        S_max = S

print(S_max)
