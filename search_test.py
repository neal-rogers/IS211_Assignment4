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


def num_gen(value):
    myrandom = random.sample(xrange(0, value), value)
    return myrandom


def main():
    #new_list = num_gen(10000)
    #print(sequential_search(new_list, -1))

    list_tests = {'t500': 500, 't1000': 1000, 't10000': 10000}

    for i in list_tests.values():
        new_list = num_gen(i)
        count = 0
        test_results = {'seq': 0, 'ordseq': 0}
        while count < 100:
            test_results['seq'] += sequential_search(new_list, -1)[1]
            test_results['ordseq'] += ordered_sequential_search(new_list, -1)[1]
            count += 1

        print "Sequential Search took %10.7f seconds to run, on average" % (test_results['seq'] / 100)
        print "Ordered Sequential Search took %10.7f seconds to run, on average" % (test_results['ordseq'] / 100)


if __name__ == '__main__':
    main()