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
print(sequential_search(test_list, -1))

def num_gen():
    myrandom = random.sample(xrange(500), 500)