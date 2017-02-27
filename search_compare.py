#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program does stuff.
"""


import time
import random


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    end = time.time()

    return found, end-start

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, -1))


def ordered_sequential_search(a_list, item):
    start = time.time()
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

    end = time.time()

    return found, end-start

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(test_list, -1))


def binary_search_recursive(a_list, item):
    start = time.time()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        found = True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)

    end = time.time()

    return found, end-start

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search_recursive(test_list, -1))


def binary_search_iterative(a_list, item):
    start = time.time()
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

    end = time.time()

    return found, end-start

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(binary_search_iterative(test_list, -1))


def num_gen(value):
    myrandom = random.sample(xrange(0, value), value)
    return myrandom


def main():
    list_tests = {'t500': 500, 't1000': 1000, 't10000': 10000}

    for i in list_tests.values():
        new_list = num_gen(i)
        count = 0
        test_results = {'insert': 0, 'shell': 0, 'gap': 0, 'python': 0}
        while count < 100:



if __name__ == '__main__':
    main()