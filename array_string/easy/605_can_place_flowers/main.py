# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        while(len(flowerbed) >= 2 and (flowerbed[0] + flowerbed[1]) == 0):
            n -= 1
            if n == 0:
                return True
            else:
                flowerbed.pop(0)
                flowerbed.pop(0)

                if len(flowerbed) <= 0:
                    if n == 0:
                        return True
                    else:
                        return False

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1

            if n <= 0:
                return True
            else:
                return False

        for i in range(len(flowerbed) - 2):
            if flowerbed[i] + flowerbed[i+1] + flowerbed[i+2] == 0:
                n -= 1
                flowerbed[i+1] = 1

        if flowerbed[-1] + flowerbed[-2] == 0:
            n -= 1

        if n <= 0:
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], 1)) # true
    print(s.canPlaceFlowers([1,0,0,0,1], 2)) # false
