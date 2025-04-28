import re
regex_pattern = r"^[789]\d{9}$"

n = int(input())
for i in range(n):
    check = bool(re.match(regex_pattern, input()))
    if check == True:
        print("YES")
    else:
        print("NO")
