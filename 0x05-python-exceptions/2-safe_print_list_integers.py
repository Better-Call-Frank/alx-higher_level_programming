#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            try:
                print("{:d}".format(element), end=" ")
                count += 1
                if count == x:
                    break
            except (TypeError, ValueError):
                continue
        print()
        return count
    except:
        raise Exception("An exception occurred while accessing the list.")
