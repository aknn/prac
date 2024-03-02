'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the
ith customer has in the  jth bank.
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
'''

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealths = list(map(lambda account: sum(account), accounts))
        return max(wealths)

x = Solution()
y = [[1,2,3],[3,2,1]]
print(x.maximumWealth(y))