from collections import Counter
n= int(input())
words= Counter([input() for _ in range(n)])
print(len(words.keys()))
print(*words.values())