"""
we are given a set of coins and our task is to form a sum of money n using the coins.
 The values of the coins are coins Æ {200,100,50,20,10,5,2,1}, and each coin can be used as many
times we want. What is the minimum number of coins needed?

greedy algo
"""


def coinch(amt):
    coins = { 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0 }
    for k, v in coins.items():
        while amt // k >= 1:
            coins[ k ] += 1
            amt -= k
    return print(sum(coins.values()))

