from collections import Counter

x = int(input())
shoes_list = dict(Counter(list(map(int, input().split()))))
n = int(input())
total = 0
for i in range(n):
    size, price = map(int, input().split())
    if size in shoes_list.keys() and shoes_list[size] != 0:
        total += price
        shoes_list[size] -= 1
print(total)
