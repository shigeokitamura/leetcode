# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix_product = 1
        suffix_product = 1

        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]
            result[n - i - 1] *= suffix_product
            suffix_product *= nums[n - i - 1]

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))
