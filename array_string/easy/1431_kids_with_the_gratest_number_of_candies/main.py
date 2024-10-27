# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        max_candy = max(candies)

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max_candy:
                result[i] = True

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.kidsWithCandies([2,3,5,1,3])) # 3
    print(s.kidsWithCandies([4,2,1,1,2])) # 1
    print(s.kidsWithCandies([12,1,12])) # 10
