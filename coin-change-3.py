class Solution:
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        
        dp = [-1 for _ in range(amount + 1)]
        coins.sort()
        
        i = 0
        while i < len(coins) and coins[i] < len(dp):
            dp[coins[i]] = 1
            i += 1
                
        for curAmount in range(len(dp)):
            i = 0
            while i < len(coins) and coins[i] < len(dp):
                dpCoin = curAmount - coins[i]
                if dpCoin >= 0 and dp[dpCoin] != -1:
                    if dp[curAmount] != -1:
                        dp[curAmount] = min(dp[curAmount], dp[dpCoin] + 1)
                    else:
                        dp[curAmount] = dp[dpCoin] + 1
                i += 1
                
        
        return dp[amount]

coins = [474,83,404,3]
amount = 264   
res = Solution().coinChange(coins, amount)
print(res)
