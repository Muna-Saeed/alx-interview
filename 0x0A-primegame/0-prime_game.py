#!/usr/bin/python3
"""Module for Prime Game"""

def sieve_of_eratosthenes(max_n):
    """Find all prime numbers up to a given limit n"""
    if max_n < 2:
        return []
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= max_n):
        if primes[p]:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(max_n + 1) if primes[p]]

def count_primes(primes, n):
    """
    Counts the number of prime numbers
    up to n in each round.
    """
    count = 0
    for prime in primes:
        if prime <= n:
            count += 1
        else:
            break
    return count

def isWinner(x, nums):
    """
    Determines the winner based on
    the count of prime numbers
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 1:
            ben_wins += 1
            continue
        prime_count = count_primes(primes, n)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
