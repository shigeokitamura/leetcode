# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums) - 1

        left = 0
        right = 0
        zero = 1

        while (right < len(nums)):
            if nums[right] == 0:
                zero -= 1

            if zero < 0:
                if nums[left] == 0:
                    zero += 1

                left += 1
            right += 1

        return right - left - 1


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray([1, 1, 0, 1])) # 3
    print(s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1])) # 5
    print(s.longestSubarray([1, 1, 1])) # 2
