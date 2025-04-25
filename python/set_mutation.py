a_len = int(input())
a = set(map(int, input().split()))
n = int(input())

for i in range(n):
    option, size = input().split()
    other_set = set(map(int, input().split()))
    if option == "intersection_update":
        a.intersection_update(other_set)
    if option == "update":
        a.update(other_set)
    if option == "symmetric_difference_update":
        a.symmetric_difference_update(other_set)
    if option == "difference_update":
        a.difference_update(other_set)

print(sum(a))
