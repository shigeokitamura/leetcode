# https://leetcode.com/problems/evaluate-division/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for i, (a, b) in enumerate(equations):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = values[i]
            graph[b][a] = 1.0 / values[i]

        result = []
        for c, d in queries:
            if c not in graph or d not in graph:
                result.append(-1.0) # Handle undefined variables
                continue

            visited = set()
            result.append(self.dfs(graph, c, d, visited))

        return result

    def dfs(self, graph: dict, start: str, end: str, visited: set):
        if start == end:
            return 1.0
        visited.add(start)
        for neighbor, weight in graph[start].items():
            if neighbor not in visited:
                path_result = self.dfs(graph, neighbor, end, set(visited))
                if path_result != -1.0:
                    return weight * path_result
        return -1.0


if __name__ == "__main__":
    s = Solution()

    print(s.calcEquation(
        equations=[["a","b"],["b","c"]],
        values=[2.0,3.0],
        queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],
    )) # [6.00000,0.50000,-1.00000,1.00000,-1.00000]

    print(s.calcEquation(
        equations=[["a","b"],["b","c"],["bc","cd"]],
        values=[1.5,2.5,5.0],
        queries=[["a","c"],["c","b"],["bc","cd"],["cd","bc"]],
    )) # [3.75000,0.40000,5.00000,0.20000]

    print(s.calcEquation(
        equations=[["a","b"]],
        values=[0.5],
        queries=[["a","b"],["b","a"],["a","c"],["x","y"]],
    )) # [0.50000,2.00000,-1.00000,-1.00000]
