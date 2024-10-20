# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.75
    print(s.findMaxAverage([5], 1)) # 5.0
    print(s.findMaxAverage([0,1,1,3,3], 4)) # 2.0
    print(s.findMaxAverage([1,3,1,4,2], 4)) # 2.5
    print(s.findMaxAverage([0,4,0,3,2], 1)) # 4.0
