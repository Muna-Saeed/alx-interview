#!/usr/bin/python3
"""
computes a minimum operations
that is needed in a CopyAll - Paste task
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): Target number of characters

    Returns:
        int: Fewest number of operations needed, or 0 if impossible to achieve
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations
