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


def num_gen(value):
    myrandom = random.sample(xrange(0, value), value)
    return myrandom


def main():
    list_tests = {'t500': 500, 't1000': 1000, 't10000': 10000}

    for i in list_tests.values():
        new_list = num_gen(i)
        count = 0
        test_results = {'seq': 0, 'ordseq': 0, 'binrec': 0, 'biniter': 0}
        while count < 100:
            test_results['seq'] sequential_search(new_list, -1)
            test_results['ordseq'] ordered_sequential_search(new_list, -1)
            test_results['binrec'] binary_search_recursive(new_list, -1)
            test_results['biniter'] binary_search_iterative(new_list, -1)
            count += 1


if __name__ == '__main__':
    main()