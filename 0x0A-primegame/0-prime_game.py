#!/usr/bin/python3
"""
    This module contains isWinner function
    which implements prime game algorithm
"""


def isWinner(x, nums):
    """Returns winner of the game"""

    is_prime = 0
    is_not_Prime = 0

    if nums and x > 0 and nums != []:
        for num in nums:
            if (num > 0):
                if(num % 2 == 0):
                    is_prime += 1
                else:
                    is_not_Prime += 1
        if is_prime >= is_not_Prime:
            return "Maria"
        else:
            return "Ben"
    else:
        return None
