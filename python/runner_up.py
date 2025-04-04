if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    out = []
    for n in arr:
        if n not in out:
            out.append(n)
    out.sort()
    print(out[len(out) - 2])
