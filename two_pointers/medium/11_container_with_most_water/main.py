# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        left_pointer = 0
        right_pointer = n - 1

        while left_pointer < right_pointer:
            water = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
            max_water = max(max_water, water)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))

