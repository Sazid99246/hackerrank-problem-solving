def arrange(l):
    n = len(l)
    l1 = l[:]
    ls = []
    for i in range(n):
        if (l[len(l)-1] > l[0]):
            ls.append(l[len(l)-1])
            l.pop(len(l)-1)
        else:
            ls.append(l[0])
            l.pop(0)
    if (sorted(l1, reverse=True) == ls):
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ls = list(map(int, input().split()))
        print(arrange(ls))
