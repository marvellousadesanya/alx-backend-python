#!/usr/bin/env python3
"""
This module defines a function that computes the sum of a mixed list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Compute the sum of a mixed list of integers and floats.

    Args:
        mxd_lst: The mixed list of integers and floats to sum.

    Returns:
        The sum of the integers and floats in mxd_lst as a float.
    """
    return sum(mxd_lst)
