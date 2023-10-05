#!/usr/bin/python3
"""a module with a prime number game"""


def is_prime(num):
    """checks if the number us prime"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """determines the winner"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count the number of prime numbers in the range [1, n]
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))

        # If the number of prime numbers is odd, Maria wins
        # If the number of prime numbers is even, Ben wins
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
