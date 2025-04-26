from collections import deque

d = deque()
n = int(input())

for i in range(n):
    command = input().split()
    if command[0] == "append":
        d.append(command[1])
    if command[0] == "appendleft":
        d.appendleft(command[1])
    if command[0] == "clear":
        d.clear()
    if command[0] == "extend":
        d.extend(command[1])
    if command[0] == "extendleft":
        d.extendleft(command[1])
    if command[0] == "count":
        d.count(command[1])
    if command[0] == "pop":
        d.pop()
    if command[0] == "popleft":
        d.popleft()
    if command[0] == "remove":
        d.remove(command[1])
    if command[0] == "reverse":
        d.reverse()
print(" ".join(d))
