from collections import OrderedDict

n = int(input())
item_list = OrderedDict()

for i in range(n):
    item = input().split()
    key = ' '.join(item[:-1])
    value = int(item[-1])
    item_list[key] = item_list.get(key, 0)+value


for item, price in item_list.items():
    print(item, price)
