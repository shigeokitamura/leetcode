# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1
        operation = 0
        nums.sort()

        while left_pointer < right_pointer:
            nums_sum = nums[left_pointer] + nums[right_pointer]
            if nums_sum == k:
                left_pointer += 1
                right_pointer -= 1
                operation += 1
            elif nums_sum > k:
                right_pointer -= 1
            elif nums_sum < k:
                left_pointer += 1

        return operation

if __name__ == "__main__":
    s = Solution()
    print(s.maxOperations([1,2,3,4], 5))
    print(s.maxOperations([3,1,3,4,3], 6))
