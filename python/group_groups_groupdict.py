import re

ser = re.search(r'([a-zA-Z0-9])\1', input())

if ser:
    print(ser.group()[0])
else:
    print(-1)
