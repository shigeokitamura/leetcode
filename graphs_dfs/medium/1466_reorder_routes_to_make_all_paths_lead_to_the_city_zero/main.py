# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        for i in range(n):
            graph[i] = []

        for i, j in connections:
            graph[i].append((j, 1)) # 1 indicates original direction
            graph[j].append((i, 0)) # 0 indicates reversed direction

        reversed_edges = 0

        visited = [False] * n

        def dfs(node):
            nonlocal reversed_edges
            visited[node] = True
            for neighbor, direction in graph[node]:
                if not visited[neighbor]:
                    if direction == 1:
                        reversed_edges += 1
                    dfs(neighbor)

        # Start DFS from city 0
        dfs(0)
        return reversed_edges

if __name__ == "__main__":
    s = Solution()

    print(s.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])) # 3
    print(s.minReorder(5, [[1,0],[1,2],[3,2],[3,4]])) # 2
    print(s.minReorder(3, [[1,0],[2,0]])) # 0
