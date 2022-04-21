#!/usr/bin/python3
"""
    This script contains a function for implementing
    minimum number of operations algorithm
"""


def minOperations(n):
    """Calculates the fewest number of operations"""
    ops = 0
    idx = 2
    if n < 2:
        return 0
    while idx < n + 1:
        while n % idx == 0:
            ops += idx
            n /= idx
        idx += 1
    return ops
