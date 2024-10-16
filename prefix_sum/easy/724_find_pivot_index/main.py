# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        len_nums = len(nums)
        sum_left = [0] * len_nums # sum_left[i] is the sum of all the numbers to the left of index i
        sum_right = [0] * len_nums # sum_right[i] is the sum of all the numbers to the right of index i

        sum_left[0] = 0
        sum_right[0] = sum(nums[1:])

        if sum_left[0] == sum_right[0]:
            return 0

        for i in range(1, len_nums):
            sum_left[i] = sum_left[i-1] + nums[i-1]
            sum_right[i] = sum_right[i-1] - nums[i]

            if sum_left[i] == sum_right[i]:
                return i

        return -1

if __name__ == "__main__":
    s = Solution()

    print(s.pivotIndex([1,7,3,6,5,6])) # 3
    print(s.pivotIndex([1,2,3])) # -1
    print(s.pivotIndex([2,1,-1])) # 0
    print(s.pivotIndex([-1,-1,0,0,-1,-1])) # 2
