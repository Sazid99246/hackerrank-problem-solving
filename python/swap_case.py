def swap_case(s):
    result = ""
    for i in s:
        if i.isupper():
            result += i.lower()
        else:
            result += i.upper()
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
