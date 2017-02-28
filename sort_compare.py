#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This program does stuff.
"""


import time
import random


def insertion_sort(a_list):
    """
    Args:
        a_list (list): List of random integers.
    Returns:
        a_list (list): List of random integers.
        end-start (float): Time difference from start to end of execution.
    Example:
        >> insertion_sort(a_list, item)
        >> False, 0.0001700
    """
    start = time.time()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]

        a_list[position] = current_value

    end = time.time()

    return a_list, end-start


def shell_sort(a_list):
    """
    Args:
        a_list (list): List of random integers.
    Returns:
        a_list (list): List of random integers.
        end-start (float): Time difference from start to end of execution.
    Example:
        >> insertion_sort(a_list, item)
        >> False, 0.0001700
    """
    start = time.time()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        sublist_count = sublist_count // 2

    end = time.time()

    return a_list, end-start


def gap_insertion_sort(a_list, start, gap):
    """
    Args:
        a_list (list): List of random integers.
    Returns:
        a_list (list): List of random integers.
        end-start (float): Time difference from start to end of execution.
    Example:
        >> insertion_sort(a_list, item)
        >> False, 0.0001700
    """
    startt = time.time()

    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

    end = time.time()

    return a_list, end-startt


def python_sort(a_list):
    """
    Args:
        a_list (list): List of random integers.
    Returns:
        a_list (list): List of random integers.
        end-start (float): Time difference from start to end of execution.
    Example:
        >> python_sort(a_list, item)
        >> 0.0001700
    """
    start = time.time()

    a_list.sort()

    end = time.time()

    return a_list, end-start


def num_gen(value):
    """
    Args:
        value (int): List of random integers.
    Returns:
        myrandom (list): List of random integers.
    Example:
        >> num_gen(value)
        >>
    """
    myrandom = random.sample(xrange(0, value), value)
    return myrandom


def main():
    """
    Args:
        None.
    Returns:
        None.
    Example:
        >>
        >> Insertion Sort took  0.0001800 seconds to run, on average
            Shell Sort took  0.0000000 seconds to run, on average
            Gap Insertion Sort took  0.0000100 seconds to run, on average
            Python Sort took  0.0000000 seconds to run, on average
            Insertion Sort took  0.0017900 seconds to run, on average
            Shell Sort took  0.0000000 seconds to run, on average
            Gap Insertion Sort took  0.0000000 seconds to run, on average
            Python Sort took  0.0000200 seconds to run, on average
            Insertion Sort took  0.0000900 seconds to run, on average
            Shell Sort took  0.0000000 seconds to run, on average
            Gap Insertion Sort took  0.0000000 seconds to run, on average
            Python Sort took  0.0000000 seconds to run, on average
    """
    list_tests = {'t500': 500, 't1000': 1000, 't10000': 10000}

    for i in list_tests.values():
        new_list = num_gen(i)
        count = 0
        test_results = {'insert': 0, 'shell': 0, 'gap': 0, 'python': 0}
        while count < 100:
            test_results['insert'] += insertion_sort(new_list)[1]
            test_results['shell'] += shell_sort(new_list)[1]
            test_results['gap'] += gap_insertion_sort(new_list)[1]
            test_results['python'] += python_sort(new_list)[1]
            count += 1

        print "Insertion Sort took %10.7f seconds to run, on average" % (test_results['insert'] / 100)
        print "Shell Sort took %10.7f seconds to run, on average" %  (test_results['shell'] / 100)
        print "Gap Insertion Sort took %10.7f seconds to run, on average" %  (test_results['gap'] / 100)
        print "Python Sort took %10.7f seconds to run, on average" %  (test_results['python'] / 100)


if __name__ == '__main__':
    main()