#!/usr/bin/python3

""" Module to make change for a given amount of money.
Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total.

    Args:
        coins (list of int): The values of the coins in the pile.
        total (int): The total amount of money to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total.
    """
    if total <= 0:
        return 0

    if coins is None or len(coins) == 0:
        return -1

    # Sort coins in descending order to start with the largest coin
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        # Use as many of the current coin as possible while total is greater
        # move to the next coin when current coin cannot be used
        while total >= coin:
            total -= coin  # Subtract the coin value from the total
            count += 1  # Increment the count of coins used

    if total != 0:  # If we cannot make the exact change, return -1
        return -1

    return count

    # n = len(coins)
    # i = 0
    # count = 0

    # while i < n:
    #     # If the coin value is less than or equal to the remaining total
    #     if coins[i] <= total:
    #         total -= coins[i]  # Subtract the coin value from the total
    #         count += 1  # Increment the count of coins used
    #     else:
    #         i += 1  # Move to the next coin

    # # If the total is not zero, it means exact change cannot be made
    # if total != 0:
    #     return -1

    # return count  # Return the count of coins used to make the total