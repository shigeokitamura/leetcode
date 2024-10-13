# https://leetcode.com/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a list to store the minimum number of coins needed for each amount
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0  # 0 coins are needed to make amount 0

        for coin in coins:
            # For each coin, loop from the coin price to the target amount
            for i in range(coin, amount + 1):
                # Update the minimum number of coins needed to make the current amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] != float("inf"):
            return dp[amount]
        else:
            return -1

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11)) # 3
    print(s.coinChange([2], 3)) # -1
    print(s.coinChange([1], 0)) # 0
