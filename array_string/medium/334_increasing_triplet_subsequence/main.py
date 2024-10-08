# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

import sys
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = sys.maxsize
        second_num = sys.maxsize

        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else: # first_num < second_num < num
                return True

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.increasingTriplet([1, 2, 3, 4, 5])) # True
    print(s.increasingTriplet([5, 4, 3, 2, 1])) # False
    print(s.increasingTriplet([2, 1, 5, 0, 4, 6])) # True
