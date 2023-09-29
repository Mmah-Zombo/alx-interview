#!/usr/bin/python3
"""money change"""


def makeChange(coins, total):
    """function that calculates changes"""
    if total < 0:
        return 0
    if total == 0:
        return 0

    dp = [float('inf')] * (total + 1)

    # Base case: Zero coins needed to make change for 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
