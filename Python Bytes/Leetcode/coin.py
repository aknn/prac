"""
we are given a set of coins and our task is to form a sum of money n using the coins.
 The values of the coins are coins Æ {200,100,50,20,10,5,2,1}, and each coin can be used as many
times we want. What is the minimum number of coins needed?

greedy algo
"""


def coinch(amt):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    count = 0
    for coin in coins:
        count += amt // coin
        amt %= coin
    return count

def test_coinch():
    assert coinch(150) == 2, "Test case 150 failed"  # 1x100 + 1x50
    assert coinch(140) == 3, "Test case 140 failed"  # 1x100 + 2x20
    assert coinch(99) == 6, "Test case 99 failed"    # 1x50 + 2x20 + 1x5 + 2x2
    assert coinch(0) == 0, "Test case 0 failed"      # No coins needed
    assert coinch(1) == 1, "Test case 1 failed"      # 1x1
    assert coinch(201) == 2, "Test case 201 failed"  # 1x200 + 1x1
    assert coinch(250) == 2, "Test case 250 failed"  # 1x200 + 1x50
    assert coinch(75) == 3, "Test case 75 failed"    # 1x50 + 1x20 + 1x5
    assert coinch(37) == 4, "Test case 37 failed"    # 1x20 + 1x10 + 1x5 + 1x2
    assert coinch(88) == 6, "Test case 88 failed"    # 1x50 + 1x20 + 1x10 + 1x5 + 1x2 + 1x1
    assert coinch(123) == 4, "Test case 123 failed"  # 1x100 + 1x20 + 1x2 + 1x1
    print("All test cases passed.")

test_coinch()

