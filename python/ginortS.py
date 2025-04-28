line = input()

def sort_func(char = ''):
  if char.islower(): 
    return -3
  if char.isupper(): 
    return -2
  if char.isnumeric():
    if float(char) % 2 == 1: 
        return -1
    return 0

sorted_line = ''.join(sorted(sorted(line), key=sort_func,))
print(sorted_line)