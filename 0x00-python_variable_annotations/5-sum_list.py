#!/usr/bin/env python3
"""
This module defines a function that computes the sum of a list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Compute the sum of a list of floats.

    Args:
        input_list: The list of floats to sum.

    Returns:
        The sum of the floats in input_list.
    """
    return sum(input_list)
