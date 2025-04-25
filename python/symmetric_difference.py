m = int(input())
set_m = set(map(int, input().split()))
n = int(input())
set_n = set(map(int, input().split()))
sym_diff = sorted(set_m.symmetric_difference(set_n))
for x in sym_diff:
    print(x)
