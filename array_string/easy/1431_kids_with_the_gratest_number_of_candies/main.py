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
    print(s.kidsWithCandies("ABCABC", "ABC")) # "ABC"
    print(s.kidsWithCandies("ABABAB", "ABAB")) # "AB"
    print(s.kidsWithCandies("LEET", "CODE")) # ""
WIP
