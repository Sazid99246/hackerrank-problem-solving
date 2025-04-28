import re

S = input() 
k = input()

result = set()

for i in range(len(S)):
    if re.search(k, S[i:]):
        result.add((re.search(k, S[i:]).start() + i,
                   re.search(k, S[i:]).end()-1 + i))

result = sorted(list(result))

if not result:
    print((-1, -1))
else:
    for t in result:
        print(t)
