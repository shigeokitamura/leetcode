# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = highest_altitude = 0

        for g in gain:
            altitude += g
            highest_altitude = max(altitude, highest_altitude)

        return highest_altitude

if __name__ == "__main__":
    s = Solution()
    print(s.largestAltitude([-5,1,5,0,-7])) # 1
    print(s.largestAltitude([-4,-3,-2,-1,4,3,2])) # 0
