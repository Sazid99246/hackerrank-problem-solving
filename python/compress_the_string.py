from itertools import groupby as gb

s = input()

res = [(len(list(group)), key) for key, group in gb(s)]

print(*[f'({count}, {key})' for count, key in res])
