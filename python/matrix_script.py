import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

B = [matrix[a][i] for i in range(m) for a in range(n)]
B = "".join(B)

pat = r'(?<=[a-zA-Z])[^a-zA-Z]{1,}(?=[a-zA-Z])'
C = re.sub(pat, ' ', B)
print(C)
