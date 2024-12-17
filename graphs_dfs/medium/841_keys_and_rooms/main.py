# https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num_rooms = len(rooms)
        visited = [False] * num_rooms
        visited[0] = True
        stack = [0]

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    stack.append(key)

        return all(visited)

if __name__ == "__main__":
    s = Solution()

    print(s.canVisitAllRooms([[1],[2],[3],[]]))
    print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
