n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = set(map(int, input().split()))
arr3 = set(map(int, input().split()))

happiness = 0
for i in arr:
    if i in arr2:
        happiness += 1
    if i in arr3:
        happiness -= 1
print(happiness)
