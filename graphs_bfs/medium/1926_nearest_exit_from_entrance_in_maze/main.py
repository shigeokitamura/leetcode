# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/?envType=study-plan-v2&envId=leetcode-75

from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set((entrance[0], entrance[1]))

        while queue:
            r, c, steps = queue.popleft()

            # Check if it's an exit (not the entrance)
            if (r != entrance[0] or c != entrance[1]) and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1):
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == "." and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

        return -1  # No exit found


if __name__ == "__main__":
    s = Solution()

    print(s.nearestExit(
        maze=[["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],
        entrance=[1,2],
    )) # 1

    print(s.nearestExit(
        maze=[["+","+","+"],[".",".","."],["+","+","+"]],
        entrance=[1,0],
    )) # 2

    print(s.nearestExit(
        maze=[[".","+"]],
        entrance=[0,0],
    )) # -1
