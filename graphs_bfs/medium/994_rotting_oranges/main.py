# https://leetcode.com/problems/rotting-oranges/description/?envType=study-plan-v2&envId=leetcode-75

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        time, fresh_count = 0, 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh_count += 1

        # Directions for adjacent cells
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] # right, down, left, up

        # BFS to simulate rotting
        while queue and fresh_count > 0:
            for i in range(len(queue)):
                i, j = queue.popleft()
                for dr, dc in directions:
                    row, col = dr + i, dc + j

                    if (row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1):
                        continue

                    # Rotten the fresh orange
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh_count -= 1
            time += 1

        return time if fresh_count == 0 else -1

if __name__ == "__main__":
    s = Solution()

    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) # 4
    print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])) # -1
    print(s.orangesRotting([[0,2]])) # 0
