#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for items in range(x):
            try:
                print("{:d}".format(my_list[item]), end='')
                num += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        pass
    print()
    return num
