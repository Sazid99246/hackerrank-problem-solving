import string

alph = list(string.ascii_lowercase)


def print_rangoli(size):

    n = size

    my_list = []

    for i in range(n-1, -1, -1):

        # add elements to my_list
        my_list.append(alph[i])

        # revese list
        rev_list = list(reversed(my_list))

        # create new list by join my_list & rev_list
        new_list = my_list + rev_list[1:]

        # print from top row to middle row
        print(("-".join(new_list)).center((size*2 - 1)*2 - 1, '-'))

    for i in range(n-1, 0, -1):
        # remove last element in the my_list
        my_list.pop()

        # revese list
        rev_list = list(reversed(my_list))

        # create new list by join my_list & rev_list
        new_list = my_list + rev_list[1:]

        # print from middle row to last row // PS: without middle row
        print(("-".join(new_list)).center((size*2 - 1)*2 - 1, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
