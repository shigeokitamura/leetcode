# https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75

import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.s = set()
        self.heap = []

        for i in range(1, 1001):
            heapq.heappush(self.heap, i)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        self.s.add(smallest)

        return smallest

    def addBack(self, num: int) -> None:
        if num in self.s:
            self.s.remove(num)
            heapq.heappush(self.heap, num)

if __name__ == "__main__":
    s = SmallestInfiniteSet()
    print(s.addBack(2)) # None
    print(s.popSmallest()) # 1
    print(s.popSmallest()) # 2
    print(s.popSmallest()) # 3
    print(s.addBack(1)) # None
    print(s.popSmallest()) # 1
    print(s.popSmallest()) # 4
    print(s.popSmallest()) # 5
