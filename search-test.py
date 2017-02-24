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
    myrandom = random.sample(xrange(0), value)
    return myrandom

def main():
    new_list = num_gen(100)
    print(sequential_search(new_list, -1))