# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        grid_t = Counter(zip(*grid))
        grid = Counter(map(tuple, grid))

        count = 0
        for row in grid_t:
            count += grid_t[row] * grid[row]

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]])) # 1
    print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])) # 3
