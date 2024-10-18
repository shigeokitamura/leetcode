# https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]

        for num in set(nums1):
            if num not in nums2:
                answer[0].append(num)

        for num in set(nums2):
            if num not in nums1:
                answer[1].append(num)

        return answer

if __name__ == "__main__":
    s = Solution()
    print(s.findDifference([1, 2, 3], [2, 4, 6])) # [[1,3],[4,6]]
    print(s.findDifference([1, 2, 3, 3], [1, 1, 2, 2])) # [[3],[]]
