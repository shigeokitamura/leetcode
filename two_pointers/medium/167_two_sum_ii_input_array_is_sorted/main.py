# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            nums_sum = numbers[left] + numbers[right]

            if nums_sum < target:
                left += 1
            elif nums_sum > target:
                right -= 1
            elif nums_sum == target:
                return [left + 1, right + 1]

if __name__ == "__main__":
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9)) # [1, 2]
    print(s.twoSum([2, 3, 4], 6)) # [1, 3]
    print(s.twoSum([-1, 0], -1)) # [1, 2]
