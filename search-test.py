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


def num_gen(value):
    myrandom = random.sample(xrange(0, value), value)
    return myrandom


def main():
    new_list = num_gen(10000)
    print(sequential_search(new_list, -1))
    t1 = (Timer("sequential_search(new_list, -1)",
                setup="from __main__ import sequential_search, num_gen;new_list=num_gen(100);"))
    print(t1.timeit(number=1))


if __name__ == '__main__':
    main()