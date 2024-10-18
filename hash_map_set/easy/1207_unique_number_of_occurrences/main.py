# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        values = list(counter.values())

        return len(set(values)) == len(values)

if __name__ == "__main__":
    s = Solution()
    print(s.uniqueOccurrences([1,2,2,1,1,3])) # true
    print(s.uniqueOccurrences([1, 2])) # false
    print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])) # true
    print(s.uniqueOccurrences([3,5,-2,-3,-6,-6])) # false
