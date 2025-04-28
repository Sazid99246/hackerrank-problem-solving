import numpy as np

n, m = map(int, input().split(' '))

arr = []

for i in range(n):
    row = list(map(int, input().split(' ')))

    arr.append(row)

print(np.prod(np.sum(arr, axis=0)))
