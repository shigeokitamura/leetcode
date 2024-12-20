# https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city):
            visited[city] = True
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1

        return provinces

if __name__ == "__main__":
    s = Solution()

    print(s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])) # 2
    print(s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])) # 3
