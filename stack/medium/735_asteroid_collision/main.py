# https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if -asteroid > stack[-1]:
                    stack.pop()
                    continue
                elif -asteroid == stack[-1]:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack


if __name__ == "__main__":
    s = Solution()

    print(s.asteroidCollision([5, 10, -5])) # [5, 10]
    print(s.asteroidCollision([8, -8])) # []
    print(s.asteroidCollision([10, 2, -5])) # [10]
