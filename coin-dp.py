

def leastCoins(coins, amount):
        '''
        :type coins: list of int
        :type amount: int
        :rtype: int
        '''
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            print(f'i is {i}')
            for j in range(0, len(coins)):
                print(f'j is {j}')
                if coins[j] <= i:
                    print(f'coins[{j}] <= {i}')
                    print(f'i - coins[j] , {i - coins[j]}')
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
                    print(f'dp[i] is {dp[i]}')
                print(f'dp is {dp}')

        return -1 if dp[amount] > amount else dp[amount]

print(leastCoins([1,2,5], 11))