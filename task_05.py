#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05, a function to return reverse of nested list """


def flip_keys(to_flip):
    """ A fuction that return the reversed of nested list inner elements

    args:
        to_flip(LIST): Nested list to be reversed

    returns:
        list: Return the original nested list with its inner elements reversed

    exampls:
        >>> flip_keys([(1, 2, 3), 'abc'])
        [(3, 2, 1), 'cba']

        >>> flip_keys([(1, 2, 3), 'hello']
        [(3, 2, 1), 'olleh']
    """
    counter = 0
    new = []
    for values in to_flip:

        if counter < len(to_flip):
            new.append(values[::-1])

        counter += 1

    # new = [v[::-1] for v in to_flip]
    return new
