def fun(s):
    if '@' in s:
        list_c = s.split('@')
        if '.' in list_c[1]:
            list_c[1] = list_c[1].split('.')
            if list_c[1][1].isalpha() and len(list_c[1][1]) <= 3:
                if list_c[1][0].isalnum():
                    if list_c[0].replace('-', '').replace('_', '').isalnum():
                        return True
    return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
