import re
text = input()
vowels = 'aeiouAEIOU'
consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
pattern = rf'(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])'

matches = re.findall(pattern, text)
if matches:
    for match in matches:
        print(match)
else:
    print(-1)
