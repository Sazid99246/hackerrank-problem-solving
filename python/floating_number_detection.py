import re
pattern = r"^[+-]?\d*\.\d+$"
T = int(input())

for testcase in range(T):
    N = input()
    if re.match(pattern, N):
        print(True)
    else:
        print(False)
