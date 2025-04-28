import email.utils
import re

n = int(input())
for _ in range(n):
    line = input()
    name, addr = email.utils.parseaddr(line)
    
    # Regex pattern to validate the email
    pattern = r"^[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,4}$"
    
    if re.match(pattern, addr):
        print(line)
