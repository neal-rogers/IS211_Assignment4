#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program does stuff.
"""


from timeit import Timer
import random


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


def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found == True
        else:
            if a_list[pos] > item:
                stop = True
    else:
        pos = pos+1

    return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))


def binary_search_recursive(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
    else:
        first = midpoint + 1

    return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search_recursive(test_list, 3))
print(binary_search_recursive(test_list, 13))


def binary_search_iterative():
    return


def main():
    seq_timer = Timer("sequential_search()", "from __main__ import sequential_search")
    print 'Sequential Search took %10.7f seconds to run, on average'.format(seq_timer.timeit(number=1000), "seconds")
    ord_timer = Timer("ordered_sequential_search()", "from __main__ import ordered_sequential_search")
    print 'Ordered Sequential Search took %10.7f seconds to run, on average'.format(ord_timer.timeit(number=1000), "seconds")
    brec_timer = Timer("binary_search_recursive()", "from __main__ import binary_search_recursive")
    print 'Recursive Binary Search took %10.7f seconds to run, on average'.format(brec_timer.timeit(number=1000), "seconds")
    bit_timer = Timer("binary_search_iterative()", "from __main__ import binary_search_iterative")
    print 'Iterative Binary Search took %10.7f seconds to run, on average'.format(bit_timer.timeit(number=1000), "seconds")


if __name__ == '__main__':
    main()