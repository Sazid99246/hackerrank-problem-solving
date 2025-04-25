def remove_dups(string):
    result = ""
    for s in string:
        if s not in result:
            result += s
    return result

def merge_the_tools(string, k):
    l = 0
    for i in range(0, len(string), k):
        chunk = string[i:i+k]
        print(remove_dups(chunk))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)