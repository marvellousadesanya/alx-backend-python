#!/usr/bin/env python3
"""
This module defines a function that converts a key-value pair to a tuple.
"""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a key-value pair to a tuple, where the second element is the square of the value.

    Args:
        k: The key as a string.
        v: The value as an int or float.

    Returns:
        A tuple with the key and the square of the value, where the square is a float.
    """
    return (k, float(v ** 2))
