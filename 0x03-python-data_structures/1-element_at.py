#!/usr/bin/python3

# that retrieves an element from a list like in C.

def element_at(my_list, index):
    if index < 0 or index >= len(my_list):
        return
    return my_list[index]
