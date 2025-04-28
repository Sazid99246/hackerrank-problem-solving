import re


def check(x):
    matches = re.findall(r"#(?:[a-fA-f0-9]{3}|[a-fA-f0-9]{6})(?=[;|,|)])", x)
    if matches:
        for i in range(len(matches)):
            print(matches[i])


for i in range(int(input())):
    x = input()
    check(x)
