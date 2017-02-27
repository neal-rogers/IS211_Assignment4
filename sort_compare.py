#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program does stuff.
"""


import time
import random


def insertion_sort(a_list):
    start = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]

        a_list[position] = current_value

    end = time.time()

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(a_list)
    return a_list, end-start


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end = time.time()

    return a_list, end-start


def gap_insertion_sort(a_list, start, gap):
    startt = time.time()

    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    end = time.time()

    return a_list, end-startt


def python_sort(a_list):
    start = time.time()

    a_list.sort()

    end = time.time()

    return a_list, end-start


def num_gen(value):
    myrandom = random.sample(xrange(0, value), value)
    return myrandom


def main():
    list_tests = {'t500': 500, 't1000': 1000, 't10000': 10000}

    for i in list_tests.values():



if __name__ == '__main__':
    main()