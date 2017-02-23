#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program does stuff.
"""


def sequential_search(a_list, item):
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))


def ordered_sequential_search():
    return
def binary_search_iterative():
    return
def binary_search_recursive():
    return


def main():
    print


if __name__ == '__main__':
    main()