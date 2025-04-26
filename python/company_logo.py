from collections import Counter


if __name__ == '__main__':
    s = input()
    counter_dict = Counter(sorted(s)).most_common(3)
    for i, j in counter_dict:
        print(i, j)
