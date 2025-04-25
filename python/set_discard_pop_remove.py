n = int(input())
s = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "pop":
        if s:
            s.pop()
    elif command[0] == "remove":
        val = int(command[1])
        if val in s:
            s.remove(val)
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))
