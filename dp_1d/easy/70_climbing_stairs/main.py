# https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def climbStairs(self, n: int) -> int:
        # For n = 1 and n = 2, return the result directly
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the DP list
        dp = [0] * (n + 1)
        dp[1] = 1 # There's only 1 way to reach the 1st step
        dp[2] = 2 # There are 2 ways to reach the 2nd step

        # Calculate for steps 3 to n
        for i in range(3, n + 1):
            # Ways to reach step i = ways to reach step (i-1) + ways to reach (i-2)
            dp[i] = dp[i - 1] + dp[i - 2]

        # Return the result for n steps
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(1))
    print(s.climbStairs(2))
    print(s.climbStairs(3))
    print(s.climbStairs(4))
    print(s.climbStairs(5))
    print(s.climbStairs(6))
    print(s.climbStairs(7))
    print(s.climbStairs(8))
