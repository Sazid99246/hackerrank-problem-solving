if __name__ == '__main__':
    N = int(input())
    result = []

    for i in range(N):
        command = input("").split(" ")
        if command[0] == "print":
            print(result)
        elif command[0] == "append":
            element = int(command[1])
            result.append(element)
        elif command[0] == "insert":
            index = int(command[1])
            element = int(command[2])
            result.insert(index, element)
        elif command[0] == "pop":
            result.pop()
        elif command[0] == "remove":
            element = int(command[1])
            if element in result:
                result.remove(element)
        elif command[0] == "sort":
            result.sort()
        elif command[0] == "reverse":
            result.reverse()
