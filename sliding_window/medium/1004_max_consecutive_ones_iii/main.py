# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0

        while (right < len(nums)):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1

                left += 1
            right += 1

        return right - left


if __name__ == "__main__":
    s = Solution()
    print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)) # 6
    print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3)) # 10
