#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04, Looping lists with a for loop """


def process_data(data):
    """A fuction that take tuple or list as arg

    args:
        data(list): a list of numbers.

    return:
        returns the total sum of the data and the averege of the list with
        floating point precision
    examples:
        >>> process_data([1,3,5,7,9])
        (25, 5.0)
        process_data([1,3,5,7,9,8]))
        (33, 5.5)
        >>> process_data([1, 2, 3])
        (6, 2.0
    """

    total = 0
    for i in data:
        total = total+i

    average = total/float(len(data))

    return total, average
