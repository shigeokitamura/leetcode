# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_count = 0

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                i -= 1
                zero_count += 1
            i += 1

        nums.extend([0] * zero_count)
        print(nums)


if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([0,1,0,3,12])
    s.moveZeroes([0])
    s.moveZeroes([0, 0, 1])
