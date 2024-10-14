# https://leetcode.com/problems/unique-paths/description/?envType=study-plan-v2&envId=leetcode-75

import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array to store the number of unique paths to each cell
        dp = np.ones((m, n), dtype=np.int64)

        # Calculate the number of unique paths for each cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return int(dp[m-1][n-1])

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7)) # 28
    print(s.uniquePaths(3, 2)) # 3

