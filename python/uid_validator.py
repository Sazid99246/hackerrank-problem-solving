import re


def valid_uid(uid):
    if len(uid) != 10:
        return False
    if not uid.isalnum():
        return False
    if len(set(uid)) != 10:
        return False
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    if len(re.findall(r'\d', uid)) < 3:
        return False

    return True


n = int(input())
for _ in range(n):
    uid = input().strip()
    print("Valid" if valid_uid(uid) else "Invalid")
