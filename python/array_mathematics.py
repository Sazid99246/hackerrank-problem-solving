import numpy as np

n, m = map(int, input().split())

a = np.array([list(map(int, input().split())) for _ in range(n)])
b = np.array([list(map(int, input().split())) for _ in range(n)])

operations = [
    'add',
    'subtract',
    'multiply',
    'floor_divide',
    'mod',
    'power'
]

for op in operations:
    func = getattr(np, op)
    print(f"{func(a, b)}")
