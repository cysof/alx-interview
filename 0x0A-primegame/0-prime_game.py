#!/usr/bin/python3

""" Function to determine the winner of a game played x times
with the numbers in nums.
By Maria and Ben taking turns picking prime numbers from a list.
"""


def isWinner(x, nums):
    """
    Function that determines the winner of a game played x times
    with the numbers in nums.

    Args:
      x (int): Number of rounds to be played.
      nums (list): List of integers where each integer represents
                  the maximum number in the range [1, n] for each game.

    Returns:
      str: "Maria" if Maria wins more games, "Ben" if Ben wins more games.
          None if there's a tie.
    """
    # If there are no games to be played or the nums list is empty, return None
    if x < 1 or not nums:
        return None

    def sieve(n):
        """
        Sieve of Eratosthenes to find all prime numbers less than
        or equal to n.

        Args:
          n (int): The upper limit to find primes within.

        Returns:
          list: A list of prime numbers up to n.
        """
        # initialize a boolean list to find prime numbers up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
        p = 2
        # Loop over each number to mark its multiples as non-prime
        while (p * p <= n):
            if is_prime[p]:
                for multiple in range(p * p, n + 1, p):
                    is_prime[multiple] = False
            p += 1
        # Return the list of primes by checking the boolean list
        return [num for num, prime in enumerate(is_prime) if prime]

    # find the maximum number in nums to determine the range for the sieve
    max_n = max(nums)
    primes = sieve(max_n)  # generate all primes up to max_n

    def play_game(n):
        """
        Simulate the game for a given n and return the winner.

        Args:
        n (int): The maximum number in the range [1, n] for the game.

        Returns:
        int: 0 if Ben wins, 1 if Maria wins.
        """
        # set of all prime numbers up to n
        primes_set = set(primes)
        # list of primes that are within the range [1, n]
        primes_in_game = [p for p in primes if p <= n]
        current_player = 0  # 0 for Maria, 1 for Ben

        # simulate the game until there are no primes left to pick
        while primes_in_game:
            # Maria or Ben picks the smallest prime number available
            prime = primes_in_game.pop(0)
            primes_set.remove(prime)
            # remove all multiples of the picked prime number from the game
            multiples = range(prime, n + 1, prime)
            primes_in_game = [p for p in primes_in_game if p not in multiples]
            # switch player after each pick
            current_player = 1 - current_player  # 0 to 1 or 1 to 0

        # If current_player is 0, Ben wins, otherwise Maria wins
        return current_player  # 0 if Ben wins, 1 if Maria wins

    # Initialize counters for wins by Maria and Ben
    maria_wins = 0
    ben_wins = 0

    # Play the game for each number in nums
    for n in nums:
        winner = play_game(n)
        if winner == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner based on the number of games won by each
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
