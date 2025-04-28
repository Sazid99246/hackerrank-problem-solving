import numpy as np

N, M, P = map(int, input().split(" "))
print(np.array([list(map(int, input().split())) for _ in range(N+M)]))
