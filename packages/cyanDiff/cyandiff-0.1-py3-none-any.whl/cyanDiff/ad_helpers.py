#!/usr/bin/env python3

"""Additional useful functions to provide additional utility to users.

The main function defined here is :class:`make_vars()` which gives the user access to variables
which can then be used for defining functions that can be used for AD. 
"""

from .ad_types import DiffObject

def make_vars(num_vars: int):
    """Provide variables for the user to define functions for AD.

    :param num_vars: number of variables to be provided.
    :type num_vars: int
    :return: list of variables of :class:`DiffObject` type if :class:`num_vars` is greater than 1, 
    return single variable of :class:`DiffObject` type otherwise.
    :rtype: :class:`list`, :class:`DiffObject`
    """
    if num_vars == 1:
        return DiffObject()
    retval = []
    for _ in range(num_vars):
        retval.append(DiffObject())
    return retval