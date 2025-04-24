def print_formatted(number):
    # Get the width of the binary representation of the largest number
    width = len(bin(number)[2:])
    for n in range(1, number + 1):
        decimal = str(n).rjust(width)
        octal = format(n, 'o').rjust(width)
        hexadecimal = format(n, 'X').rjust(width)
        binary = format(n, 'b').rjust(width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
